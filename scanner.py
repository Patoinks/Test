from __future__ import annotations

import base64
import csv
import hashlib
import hmac
import math
import os
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlencode

import pandas as pd
import requests
import yfinance as yf

OKX_BASE = os.getenv("OKX_BASE_URL", "https://eea.okx.com").rstrip("/")
OKX_REQUIRE_EEA = os.getenv("OKX_REQUIRE_EEA", "1") == "1"
ALLOW_STATIC_FALLBACK = os.getenv("ALLOW_STATIC_OKX_FALLBACK", "0") == "1"
OKX_API_KEY = os.getenv("OKX_API_KEY", "").strip()
OKX_API_SECRET = os.getenv("OKX_API_SECRET", "").strip()
OKX_API_PASSPHRASE = os.getenv("OKX_API_PASSPHRASE", "").strip()
OKX_GROUP_IDS = {"6", "7"}  # SWAP RWA / stock-perpetual fee groups
USER_AVAILABLE_SYMBOLS = [
    x.strip().upper()
    for x in os.getenv("OKX_AVAILABLE_SYMBOLS", "").split(",")
    if x.strip()
]
ASSET_PROXY_SYMBOLS = {"MSTR", "BMNR", "PURI"}  # treasury/asset-proxy names need NAV/premium analysis

ETF_SYMBOLS = {"SOXL", "SPY", "QQQ", "EWY", "SNX", "DRAM", "SOXS", "KORU", "SKDD", "MUU"}
PRIVATE_SYNTHETIC_SYMBOLS = {"SPCX", "OPENAI", "ANTHROPIC", "ZHIPU", "MINIMAX"}
NON_FUNDAMENTAL_SYMBOLS = ETF_SYMBOLS | PRIVATE_SYNTHETIC_SYMBOLS

USER_UNAVAILABLE_SYMBOLS = {
    x.strip().upper()
    for x in os.getenv("OKX_UNAVAILABLE_SYMBOLS", "TWLO,DKNG").split(",")
    if x.strip()
}
MAX_WORKERS = int(os.getenv("MAX_WORKERS", "6"))
TIMEOUT = 20

# Price-dislocation / entry-timing layer.
# 24h and 7-day price moves carry equal weight.
PRICE_TIMING_24H_WEIGHT = 0.50
PRICE_TIMING_7D_WEIGHT = 0.50
PRICE_TIMING_FULL_MOVE = 0.25
PRICE_TIMING_MAX_ADJUSTMENT = 20
FINAL_WATCH_THRESHOLD = 55
FINAL_CORE_THRESHOLD = 75

if OKX_REQUIRE_EEA and "eea.okx.com" not in OKX_BASE:
    raise RuntimeError(
        f"Refusing to scan non-EEA OKX domain: {OKX_BASE}. "
        "Set OKX_REQUIRE_EEA=0 only for an intentional global diagnostic run."
    )

# Symbols where the OKX TradFi label is not the Yahoo Finance ticker.
YAHOO_MAP = {
    "LGELECTRONICS": "066570.KS",
    "NAVER": "035420.KS",
    "HANMI": "042700.KS",
    "SOFTBANK": "9984.T",
    "ZHONGJI": "300308.SZ",
    "KIOXIA": "285A.T",
    "POPMART": "9992.HK",
    "XIAOMI": "1810.HK",
    "SKHY": "000660.KS",
    "SKHYNIX": "000660.KS",
    "SAMSUNG": "005930.KS",
    "AXT": "AXTI",
    "PURI": "PURR",
}

# Current OKX Europe TradFi universe fallback.
# Core list comes from OKX's Delta-Neutral FAQ (updated 2026-09-01),
# with later September equity-perp listings added from official OKX announcements.
# ETFs/private/non-equity assets are harmless here: fetch_fundamentals() keeps
# only Yahoo quoteType == EQUITY with a valid market cap.
FALLBACK_OKX_SYMBOLS = sorted(set("""
AAPL AMD AMZN AVGO CRCL EWY GOOGL INTC IWM LITE META MRVL MSFT MSTR MU NVDA
QQQ SKHY SNDK SPCX SPY TSLA TSM ASTS BMNR COIN DELL HOOD IBM IREN LLY NFLX
ORCL PLTR USAR ADBE AMAT ASML CRWD CSCO GEV GME HIMS ONDS TER VRT XLE AAOI
ALAB APP ARM BE BSP CBRS COHR CRWV NBIS ON RKLB SHAZ SMCI TWLO CIEN CRM DKNG
HPE KO LRCX NOW POPMART RDDT SMH SNOW TTWO XIAOMI APLD BOT BX ISRG OKTA RIVN
UNH WDC ZM GLW JNJ KLAC QCOM ROK STRC
INTC PANW BB RDW LUNR CRDO FLNC CGNX WEN TSEM KIOXIA XOM AMC GPRO
LGELECTRONICS NAVER HANMI ZHONGJI SOFTBANK
SKHYNIX BMNR SNX ZHIPU ANTHROPIC OPENAI PURI DRAM SOXS MRNA KORU AXT
SAMSUNG IONQ MINIMAX SKDD MUU
""".split()))

DISCOVERY_SCOPE = "OKX EEA public catalogue"

REPORT_DIR = Path("reports")
DATA_DIR = Path("data")
REPORT_DIR.mkdir(exist_ok=True)
DATA_DIR.mkdir(exist_ok=True)


def n(value):
    try:
        x = float(value)
        return x if math.isfinite(x) else None
    except (TypeError, ValueError):
        return None


def pct(value):
    x = n(value)
    return None if x is None else x * 100.0


def fmt_num(value, digits=1):
    x = n(value)
    return "—" if x is None else f"{x:.{digits}f}"


def fmt_pct(value, digits=1):
    x = n(value)
    return "—" if x is None else f"{x * 100:.{digits}f}%"


def okx_get(path, params=None):
    r = requests.get(f"{OKX_BASE}{path}", params=params or {}, timeout=TIMEOUT)
    r.raise_for_status()
    payload = r.json()
    if payload.get("code") not in (None, "0", 0):
        raise RuntimeError(f"OKX error: {payload.get('code')} {payload.get('msg')}")
    return payload.get("data", [])


def okx_private_get(path, params=None):
    """Authenticated read-only GET for account-scoped instrument availability."""
    if not (OKX_API_KEY and OKX_API_SECRET and OKX_API_PASSPHRASE):
        raise RuntimeError("OKX account credentials are not configured.")

    params = params or {}
    query = urlencode(params)
    request_path = path + (f"?{query}" if query else "")
    timestamp = datetime.now(timezone.utc).isoformat(timespec="milliseconds").replace("+00:00", "Z")
    prehash = f"{timestamp}GET{request_path}"
    signature = base64.b64encode(
        hmac.new(
            OKX_API_SECRET.encode("utf-8"),
            prehash.encode("utf-8"),
            hashlib.sha256,
        ).digest()
    ).decode("utf-8")

    headers = {
        "OK-ACCESS-KEY": OKX_API_KEY,
        "OK-ACCESS-SIGN": signature,
        "OK-ACCESS-TIMESTAMP": timestamp,
        "OK-ACCESS-PASSPHRASE": OKX_API_PASSPHRASE,
    }
    r = requests.get(f"{OKX_BASE}{request_path}", headers=headers, timeout=TIMEOUT)
    r.raise_for_status()
    payload = r.json()
    if payload.get("code") not in (None, "0", 0):
        raise RuntimeError(f"OKX private API error: {payload.get('code')} {payload.get('msg')}")
    return payload.get("data", [])


def classify_tradfi_instruments(instruments):
    out = []
    seen = set()
    for item in instruments:
        if item.get("state") != "live":
            continue
        inst_id = item.get("instId", "")
        if not inst_id.endswith("-USDT-SWAP"):
            continue

        okx_symbol = inst_id.split("-")[0]
        is_rwa_group = str(item.get("groupId")) in OKX_GROUP_IDS
        is_known_tradfi = okx_symbol in FALLBACK_OKX_SYMBOLS
        if not (is_rwa_group or is_known_tradfi):
            continue
        if okx_symbol in USER_UNAVAILABLE_SYMBOLS:
            continue
        if inst_id in seen:
            continue
        seen.add(inst_id)
        out.append(
            {
                "okx_symbol": okx_symbol,
                "inst_id": inst_id,
                "max_leverage": n(item.get("lever")),
            }
        )
    return out


def discover_okx_stock_perps():
    """
    Prefer the authenticated account instrument catalogue when read-only OKX
    credentials are configured. That endpoint reflects instruments available to
    the current account. Without credentials, use the public EEA live catalogue.
    """
    global DISCOVERY_SCOPE

    # Highest-confidence source: the exact xStocks/USDC universe confirmed
    # by the user from the OKX EEA app. This avoids public-catalogue products
    # that may not actually be exposed in the user's UI/account.
    if USER_AVAILABLE_SYMBOLS:
        DISCOVERY_SCOPE = "user-confirmed OKX EEA Stock Futures / X-Perp"
        return [
            {
                "okx_symbol": symbol,
                "inst_id": f"{symbol}-USDT-SWAP",
                "max_leverage": None,
                "product_type": "STOCK_PERP",
            }
            for symbol in USER_AVAILABLE_SYMBOLS
        ]

    if OKX_API_KEY and OKX_API_SECRET and OKX_API_PASSPHRASE:
        try:
            account_instruments = okx_private_get(
                "/api/v5/account/instruments",
                {"instType": "SWAP"},
            )
            account_out = classify_tradfi_instruments(account_instruments)
            if account_out:
                DISCOVERY_SCOPE = "OKX account-specific available instruments (EEA)"
                print(
                    f"Account catalogue: {len(account_instruments)} SWAP instruments total; "
                    f"{len(account_out)} live TradFi/RWA candidates matched."
                )
                return account_out
            print("WARN: authenticated account catalogue returned no TradFi/RWA matches; using EEA public catalogue.")
        except Exception as exc:
            print(f"WARN: account-specific instrument lookup failed: {exc}; using EEA public catalogue.")

    instruments = okx_get("/api/v5/public/instruments", {"instType": "SWAP"})
    out = classify_tradfi_instruments(instruments)
    if out:
        DISCOVERY_SCOPE = "OKX EEA public catalogue (account filter not configured)"
        print(
            f"EEA catalogue: {len(instruments)} SWAP instruments total; "
            f"{len(out)} live TradFi/RWA candidates matched."
        )
        return out

    # Fail closed by default. A stale/global fallback can create false positives
    # for EEA users (e.g. showing a contract that exists globally but not in Europe).
    if ALLOW_STATIC_FALLBACK:
        DISCOVERY_SCOPE = "static diagnostic fallback (NOT account availability)"
        print(
            "WARN: EEA public catalogue returned no RWA groups; "
            "using the static fallback ONLY because ALLOW_STATIC_OKX_FALLBACK=1."
        )
        return [
            {
                "okx_symbol": symbol,
                "inst_id": f"{symbol}-USDT-SWAP",
                "max_leverage": 5.0,
            }
            for symbol in FALLBACK_OKX_SYMBOLS
        ]

    raise RuntimeError(
        "EEA OKX public catalogue returned no live TradFi/RWA perpetuals. "
        "Scanner stopped instead of falling back to a possibly global/stale universe."
    )


def get_funding(inst_id):
    try:
        rows = okx_get("/api/v5/public/funding-rate", {"instId": inst_id})
        if not rows:
            return None, None
        row = rows[0]
        rate = n(row.get("fundingRate"))
        if rate is None:
            return None, None

        funding_ms = n(row.get("fundingTime"))
        next_ms = n(row.get("nextFundingTime"))
        interval_hours = 8.0
        if funding_ms and next_ms and next_ms > funding_ms:
            interval_hours = (next_ms - funding_ms) / 3_600_000
            if interval_hours <= 0 or interval_hours > 24:
                interval_hours = 8.0

        annualized = rate * (24.0 / interval_hours) * 365.0
        return rate, annualized
    except Exception:
        return None, None


def dataframe_value(df, row_name, col_name):
    try:
        if df is None or len(df) == 0:
            return None
        if row_name not in df.index or col_name not in df.columns:
            return None
        return n(df.loc[row_name, col_name])
    except Exception:
        return None


def get_price_changes(t, current_price):
    """Return approximate 24h and 7-calendar-day returns from Yahoo daily bars."""
    try:
        history = t.history(period="12d", interval="1d", auto_adjust=False)
        if history is None or history.empty or "Close" not in history.columns:
            return None, None

        closes = history["Close"].dropna()
        if closes.empty:
            return None, None

        latest = n(current_price)
        if latest is None:
            latest = n(closes.iloc[-1])
        if latest is None or latest <= 0:
            return None, None

        idx_tz = getattr(closes.index, "tz", None)
        now_ts = pd.Timestamp.now(tz=idx_tz) if idx_tz is not None else pd.Timestamp.now()

        def baseline(days):
            target = now_ts - pd.Timedelta(days=days)
            eligible = closes[closes.index <= target]
            if eligible.empty:
                return None
            return n(eligible.iloc[-1])

        base_24h = baseline(1)
        base_7d = baseline(7)
        change_24h = (latest / base_24h) - 1.0 if base_24h and base_24h > 0 else None
        change_7d = (latest / base_7d) - 1.0 if base_7d and base_7d > 0 else None
        return change_24h, change_7d
    except Exception:
        return None, None


def fetch_fundamentals(item):
    okx_symbol = item["okx_symbol"]
    # Explicitly skip ETFs and private/pre-IPO synthetic markets so ticker
    # collisions (for example SNX) can never be mistaken for a public company.
    if okx_symbol in NON_FUNDAMENTAL_SYMBOLS:
        return None
    yahoo_symbol = YAHOO_MAP.get(okx_symbol, okx_symbol.replace(".", "-"))
    t = yf.Ticker(yahoo_symbol)

    try:
        info = t.get_info() or {}
    except Exception:
        info = {}

    quote_type = str(info.get("quoteType") or "").upper()
    market_cap = n(info.get("marketCap"))

    # Keep companies only: excludes ETFs, indices, commodities, private assets, etc.
    if quote_type != "EQUITY" or not market_cap or market_cap <= 0:
        return None

    price = n(info.get("currentPrice") or info.get("regularMarketPrice"))
    price_change_24h, price_change_7d = get_price_changes(t, price)
    price_timing_move = (
        (PRICE_TIMING_24H_WEIGHT * price_change_24h)
        + (PRICE_TIMING_7D_WEIGHT * price_change_7d)
        if price_change_24h is not None and price_change_7d is not None
        else None
    )

    trailing_pe = n(info.get("trailingPE"))
    forward_pe = n(info.get("forwardPE"))
    price_to_sales = n(info.get("priceToSalesTrailing12Months"))
    enterprise_value = n(info.get("enterpriseValue"))
    total_revenue = n(info.get("totalRevenue"))
    ev_to_sales = (
        enterprise_value / total_revenue
        if enterprise_value is not None and total_revenue is not None and total_revenue > 0
        else None
    )
    operating_margin = n(info.get("operatingMargins"))
    profit_margin = n(info.get("profitMargins"))
    fcf = n(info.get("freeCashflow"))
    fcf_yield = (fcf / market_cap) if fcf is not None and market_cap else None
    # Guard against currency/unit mismatches in synthetic/foreign quote feeds.
    if fcf_yield is not None and abs(fcf_yield) > 1.0:
        fcf_yield = None

    growth_df = None
    earnings_df = None
    revenue_df = None
    try:
        growth_df = t.growth_estimates
    except Exception:
        pass
    try:
        earnings_df = t.earnings_estimate
    except Exception:
        pass
    try:
        revenue_df = t.revenue_estimate
    except Exception:
        pass

    # Prefer the explicit analyst +1y EPS growth field when available.
    eps_growth_1y = dataframe_value(earnings_df, "+1y", "growth")
    if eps_growth_1y is None:
        eps_growth_1y = dataframe_value(growth_df, "+1y", "stock")
    if eps_growth_1y is None:
        eps_growth_1y = n(info.get("earningsGrowth"))

    revenue_growth_0y = dataframe_value(revenue_df, "0y", "growth")
    revenue_growth_1y = dataframe_value(revenue_df, "+1y", "growth")
    if revenue_growth_1y is None:
        revenue_growth_1y = n(info.get("revenueGrowth"))

    revenue_decelerating = (
        revenue_growth_0y is not None
        and revenue_growth_1y is not None
        and revenue_growth_1y < revenue_growth_0y
    )
    revenue_accelerating = (
        revenue_growth_0y is not None
        and revenue_growth_1y is not None
        and revenue_growth_1y > revenue_growth_0y
    )

    # Our core ratio: forward P/E divided by expected EPS growth percentage.
    peg_1y = None
    if forward_pe is not None and eps_growth_1y is not None and eps_growth_1y > 0:
        peg_1y = forward_pe / (eps_growth_1y * 100.0)

    # Separate P/E trend model: compares trailing vs forward P/E, then checks
    # whether earnings/revenue direction supports that multiple compression
    # (LONG) or expansion (SHORT). This is intentionally separate from the
    # main fundamental LONG/SHORT model.
    pe_change_pct = None
    pe_trend_long_score = 0
    pe_trend_short_score = 0
    pe_trend_long_reasons = []
    pe_trend_short_reasons = []

    valid_pe_pair = (
        trailing_pe is not None
        and forward_pe is not None
        and trailing_pe > 0
        and forward_pe > 0
    )
    if valid_pe_pair:
        pe_change_pct = (forward_pe / trailing_pe) - 1.0

        # LONG side: falling forward multiple + still-growing fundamentals.
        compression = -pe_change_pct
        if compression > 0:
            if compression >= 0.50:
                pe_trend_long_score += 50
            elif compression >= 0.30:
                pe_trend_long_score += 40
            elif compression >= 0.20:
                pe_trend_long_score += 30
            elif compression >= 0.10:
                pe_trend_long_score += 22
            else:
                pe_trend_long_score += 12
            pe_trend_long_reasons.append(
                f"P/E compresses {trailing_pe:.1f}x -> {forward_pe:.1f}x ({compression:.1%})"
            )

        if eps_growth_1y is not None:
            if eps_growth_1y >= 0.50:
                pe_trend_long_score += 25
                pe_trend_long_reasons.append("EPS +1y >= 50%")
            elif eps_growth_1y >= 0.25:
                pe_trend_long_score += 20
                pe_trend_long_reasons.append("EPS +1y >= 25%")
            elif eps_growth_1y >= 0.10:
                pe_trend_long_score += 12
                pe_trend_long_reasons.append("EPS +1y >= 10%")
            elif eps_growth_1y > 0:
                pe_trend_long_score += 5
                pe_trend_long_reasons.append("EPS +1y positive")
            else:
                pe_trend_long_score -= 30
                pe_trend_long_reasons.append("Penalty: EPS not growing")

        if revenue_growth_1y is not None:
            if revenue_growth_1y >= 0.30:
                pe_trend_long_score += 20
                pe_trend_long_reasons.append("Revenue +1y >= 30%")
            elif revenue_growth_1y >= 0.15:
                pe_trend_long_score += 15
                pe_trend_long_reasons.append("Revenue +1y >= 15%")
            elif revenue_growth_1y >= 0.05:
                pe_trend_long_score += 8
                pe_trend_long_reasons.append("Revenue +1y >= 5%")
            elif revenue_growth_1y > 0:
                pe_trend_long_score += 4
                pe_trend_long_reasons.append("Revenue +1y positive")
            else:
                pe_trend_long_score -= 25
                pe_trend_long_reasons.append("Penalty: revenue not growing")

        if revenue_accelerating:
            pe_trend_long_score += 5
            pe_trend_long_reasons.append("Revenue growth accelerating")
        elif revenue_decelerating:
            pe_trend_long_score -= 5
            pe_trend_long_reasons.append("Penalty: revenue growth rate decelerating")

        # Sanity check on the absolute forward multiple. Compression from an
        # extreme valuation is useful information, but should not dominate.
        if forward_pe <= 20:
            pe_trend_long_score += 10
            pe_trend_long_reasons.append("Forward P/E <= 20")
        elif forward_pe <= 35:
            pe_trend_long_score += 6
            pe_trend_long_reasons.append("Forward P/E <= 35")
        elif forward_pe <= 50:
            pe_trend_long_score += 2
            pe_trend_long_reasons.append("Forward P/E <= 50")
        elif forward_pe > 120:
            pe_trend_long_score -= 20
            pe_trend_long_reasons.append("Penalty: forward P/E > 120")
        elif forward_pe > 80:
            pe_trend_long_score -= 10
            pe_trend_long_reasons.append("Penalty: forward P/E > 80")

        # SHORT side: expanding forward multiple + weakening fundamentals.
        expansion = pe_change_pct
        if expansion > 0:
            if expansion >= 0.50:
                pe_trend_short_score += 50
            elif expansion >= 0.30:
                pe_trend_short_score += 40
            elif expansion >= 0.20:
                pe_trend_short_score += 30
            elif expansion >= 0.10:
                pe_trend_short_score += 22
            else:
                pe_trend_short_score += 12
            pe_trend_short_reasons.append(
                f"P/E expands {trailing_pe:.1f}x -> {forward_pe:.1f}x ({expansion:.1%})"
            )

        if eps_growth_1y is not None:
            if eps_growth_1y < 0:
                pe_trend_short_score += 25
                pe_trend_short_reasons.append("EPS +1y negative")
            elif eps_growth_1y < 0.10:
                pe_trend_short_score += 15
                pe_trend_short_reasons.append("EPS +1y < 10%")
            elif eps_growth_1y < 0.20:
                pe_trend_short_score += 8
                pe_trend_short_reasons.append("EPS +1y < 20%")

        if revenue_growth_1y is not None:
            if revenue_growth_1y < 0:
                pe_trend_short_score += 20
                pe_trend_short_reasons.append("Revenue +1y negative")
            elif revenue_growth_1y < 0.05:
                pe_trend_short_score += 12
                pe_trend_short_reasons.append("Revenue +1y < 5%")
            elif revenue_growth_1y < 0.10:
                pe_trend_short_score += 6
                pe_trend_short_reasons.append("Revenue +1y < 10%")

        if revenue_decelerating:
            pe_trend_short_score += 5
            pe_trend_short_reasons.append("Revenue growth decelerating")
        elif revenue_accelerating:
            pe_trend_short_score -= 5
            pe_trend_short_reasons.append("Mitigation: revenue growth accelerating")

        if forward_pe >= 100:
            pe_trend_short_score += 10
            pe_trend_short_reasons.append("Forward P/E >= 100")
        elif forward_pe >= 50:
            pe_trend_short_score += 5
            pe_trend_short_reasons.append("Forward P/E >= 50")

    pe_trend_long_score = max(0, min(100, pe_trend_long_score))
    pe_trend_short_score = max(0, min(100, pe_trend_short_score))

    pe_trend_long_core = (
        valid_pe_pair
        and pe_change_pct < 0
        and pe_trend_long_score >= 75
        and eps_growth_1y is not None
        and eps_growth_1y > 0
        and revenue_growth_1y is not None
        and revenue_growth_1y > 0
    )
    pe_trend_long_watch = (
        valid_pe_pair
        and pe_change_pct < 0
        and not pe_trend_long_core
        and pe_trend_long_score >= 50
        and eps_growth_1y is not None
        and eps_growth_1y > 0
        and revenue_growth_1y is not None
        and revenue_growth_1y > 0
    )
    pe_trend_short_core = (
        valid_pe_pair
        and pe_change_pct > 0
        and pe_trend_short_score >= 70
        and (
            (eps_growth_1y is not None and eps_growth_1y < 0)
            or (revenue_growth_1y is not None and revenue_growth_1y < 0)
        )
    )
    pe_trend_short_watch = (
        valid_pe_pair
        and pe_change_pct > 0
        and not pe_trend_short_core
        and pe_trend_short_score >= 50
    )

    pe_trend_long_signal = (
        "CORE" if pe_trend_long_core else "WATCH" if pe_trend_long_watch else "—"
    )
    pe_trend_short_signal = (
        "CORE" if pe_trend_short_core else "WATCH" if pe_trend_short_watch else "—"
    )

    # Regime detection: PEG/EPS growth can be badly distorted when earnings
    # start from a tiny or negative base. In that case, use sales multiples,
    # margins and cash generation as the primary valuation lens.
    asset_proxy = okx_symbol in ASSET_PROXY_SYMBOLS

    speculative_growth = (
        not asset_proxy
        and (
            (operating_margin is not None and operating_margin < 0)
            or (profit_margin is not None and profit_margin < 0)
            or trailing_pe is None
            or (trailing_pe is not None and trailing_pe <= 0)
        )
    )

    extreme_sales_valuation = (
        (price_to_sales is not None and price_to_sales >= 40)
        or (ev_to_sales is not None and ev_to_sales >= 40)
    )

    # SHORT score: expensive valuation relative to growth and business quality.
    short_score = 0
    short_reasons = []

    if forward_pe is not None and forward_pe > 40:
        short_score += 20
        short_reasons.append("Forward P/E > 40")
    if forward_pe is not None and forward_pe >= 100:
        short_score += 10
        short_reasons.append("Forward P/E >= 100")
    if trailing_pe is not None and trailing_pe > 40:
        short_score += 10
        short_reasons.append("Trailing P/E > 40")

    # PEG matters mainly for established profitable companies.
    if not speculative_growth:
        if peg_1y is not None and peg_1y > 2.5:
            short_score += 20
            short_reasons.append("Ratio/PEG > 2.5")
        if eps_growth_1y is not None and eps_growth_1y < 0.20:
            short_score += 20
            short_reasons.append("EPS growth < 20%")
    else:
        # Progressive sales-multiple penalty. This avoids the old cliff where
        # a loss-making name at ~30-39x sales was treated too similarly to one
        # at ~25x. High multiples now get progressively more expensive from 20x.
        if price_to_sales is not None:
            if price_to_sales >= 50:
                short_score += 28
                short_reasons.append("P/S >= 50")
            elif price_to_sales >= 40:
                short_score += 25
                short_reasons.append("P/S >= 40")
            elif price_to_sales >= 30:
                short_score += 22
                short_reasons.append("P/S >= 30")
            elif price_to_sales >= 25:
                short_score += 18
                short_reasons.append("P/S >= 25")
            elif price_to_sales >= 20:
                short_score += 14
                short_reasons.append("P/S >= 20")
            elif price_to_sales >= 15:
                short_score += 10
                short_reasons.append("P/S >= 15")
        if ev_to_sales is not None:
            if ev_to_sales >= 50:
                short_score += 28
                short_reasons.append("EV/Sales >= 50")
            elif ev_to_sales >= 40:
                short_score += 25
                short_reasons.append("EV/Sales >= 40")
            elif ev_to_sales >= 30:
                short_score += 22
                short_reasons.append("EV/Sales >= 30")
            elif ev_to_sales >= 25:
                short_score += 18
                short_reasons.append("EV/Sales >= 25")
            elif ev_to_sales >= 20:
                short_score += 14
                short_reasons.append("EV/Sales >= 20")
            elif ev_to_sales >= 15:
                short_score += 10
                short_reasons.append("EV/Sales >= 15")
        if operating_margin is not None and operating_margin < 0:
            short_score += 15
            short_reasons.append("Negative operating margin")
        if profit_margin is not None and profit_margin < 0:
            short_score += 10
            short_reasons.append("Negative net margin")

    if fcf_yield is not None:
        if fcf_yield < 0:
            short_score += 15
            short_reasons.append("Negative FCF yield")
        elif fcf_yield < 0.025:
            short_score += 8
            short_reasons.append("FCF yield < 2.5%")

    if revenue_decelerating:
        short_score += 10
        short_reasons.append("Revenue growth decelerating")
    if revenue_accelerating:
        short_score -= 5
        short_reasons.append("Mitigation: revenue growth accelerating")
    if speculative_growth and revenue_growth_1y is not None:
        if revenue_growth_1y >= 1.0:
            short_score -= 10
            short_reasons.append("Mitigation: revenue growth >= 100%")
        elif revenue_growth_1y >= 0.50:
            short_score -= 5
            short_reasons.append("Mitigation: revenue growth >= 50%")

    # Extreme-sales-multiple override: a loss-making company at >40x sales
    # cannot receive a low short-risk score just because EPS growth is huge.
    if speculative_growth and extreme_sales_valuation:
        short_score = max(short_score, 80)
        short_reasons.append("Override: loss-making + >=40x sales valuation")

    if asset_proxy:
        short_score = min(short_score, 25)
        short_reasons.append("Asset-proxy exception: sales multiples ignored")

    short_score = max(0, min(100, short_score))

    classic_short_core = (
        not speculative_growth
        and forward_pe is not None
        and forward_pe > 40
        and peg_1y is not None
        and peg_1y > 2.5
        and eps_growth_1y is not None
        and eps_growth_1y < 0.20
    )
    speculative_short_core = (
        speculative_growth
        and short_score >= 85
        and extreme_sales_valuation
        and (
            (fcf_yield is not None and fcf_yield < 0)
            or (operating_margin is not None and operating_margin <= -0.20)
        )
    )
    short_core = classic_short_core or speculative_short_core
    short_watch = (
        (not short_core)
        and (
            (
                not speculative_growth
                and forward_pe is not None
                and forward_pe > 40
                and eps_growth_1y is not None
                and eps_growth_1y < 0.25
                and (peg_1y is None or peg_1y > 2.0)
            )
            or (
                speculative_growth
                and short_score >= 65
                and (
                    (price_to_sales is not None and price_to_sales >= 15)
                    or (ev_to_sales is not None and ev_to_sales >= 15)
                    or (forward_pe is not None and forward_pe >= 100)
                )
            )
        )
    )

    if short_core:
        short_signal = "CORE"
    elif short_watch:
        short_signal = "WATCH"
    else:
        short_signal = "—"

    # LONG score: reasonable valuation + strong expected growth + cash generation.
    # It is deliberately the mirror image of the short thesis, not a buy order.
    long_score = 0
    long_reasons = []

    if forward_pe is not None and forward_pe > 0:
        if forward_pe <= 20:
            long_score += 20
            long_reasons.append("Forward P/E <= 20")
        elif forward_pe <= 30:
            long_score += 12
            long_reasons.append("Forward P/E <= 30")
        elif forward_pe <= 40:
            long_score += 5
            long_reasons.append("Forward P/E <= 40")

    if not speculative_growth and peg_1y is not None and peg_1y > 0:
        if peg_1y <= 1.0:
            long_score += 30
            long_reasons.append("Ratio/PEG <= 1.0")
        elif peg_1y <= 1.5:
            long_score += 20
            long_reasons.append("Ratio/PEG <= 1.5")
        elif peg_1y <= 2.0:
            long_score += 8
            long_reasons.append("Ratio/PEG <= 2.0")

    if eps_growth_1y is not None:
        if speculative_growth:
            # Huge EPS percentages from a tiny/negative base are not treated
            # as a full-quality growth signal.
            if eps_growth_1y >= 0.25:
                long_score += 5
                long_reasons.append("Speculative EPS growth bonus capped")
            elif eps_growth_1y < 0:
                long_score -= 10
                long_reasons.append("Penalty: EPS shrinking")
        else:
            if eps_growth_1y >= 0.25:
                long_score += 20
                long_reasons.append("EPS growth >= 25%")
            elif eps_growth_1y >= 0.15:
                long_score += 12
                long_reasons.append("EPS growth >= 15%")
            elif eps_growth_1y < 0:
                long_score -= 15
                long_reasons.append("Penalty: EPS shrinking")

    if fcf_yield is not None:
        if fcf_yield >= 0.04:
            long_score += 15
            long_reasons.append("FCF yield >= 4%")
        elif fcf_yield >= 0.025:
            long_score += 8
            long_reasons.append("FCF yield >= 2.5%")
        elif fcf_yield < 0:
            long_score -= 15
            long_reasons.append("Penalty: negative FCF")

    if speculative_growth:
        if price_to_sales is not None and price_to_sales >= 40:
            long_score -= 25
            long_reasons.append("Penalty: P/S >= 40")
        elif price_to_sales is not None and price_to_sales >= 30:
            long_score -= 22
            long_reasons.append("Penalty: P/S >= 30")
        elif price_to_sales is not None and price_to_sales >= 25:
            long_score -= 18
            long_reasons.append("Penalty: P/S >= 25")
        elif price_to_sales is not None and price_to_sales >= 20:
            long_score -= 14
            long_reasons.append("Penalty: P/S >= 20")
        elif price_to_sales is not None and price_to_sales >= 15:
            long_score -= 10
            long_reasons.append("Penalty: P/S >= 15")
        if ev_to_sales is not None and ev_to_sales >= 40:
            long_score -= 25
            long_reasons.append("Penalty: EV/Sales >= 40")
        elif ev_to_sales is not None and ev_to_sales >= 30:
            long_score -= 22
            long_reasons.append("Penalty: EV/Sales >= 30")
        elif ev_to_sales is not None and ev_to_sales >= 25:
            long_score -= 18
            long_reasons.append("Penalty: EV/Sales >= 25")
        elif ev_to_sales is not None and ev_to_sales >= 20:
            long_score -= 14
            long_reasons.append("Penalty: EV/Sales >= 20")
        elif ev_to_sales is not None and ev_to_sales >= 15:
            long_score -= 10
            long_reasons.append("Penalty: EV/Sales >= 15")
        if operating_margin is not None and operating_margin < 0:
            long_score -= 15
            long_reasons.append("Penalty: negative operating margin")
        if extreme_sales_valuation:
            long_score = min(long_score, 25)
            long_reasons.append("Cap: extreme sales valuation")

    if revenue_growth_1y is not None:
        if revenue_growth_1y >= 0.15:
            long_score += 10
            long_reasons.append("Revenue growth >= 15%")
        elif revenue_growth_1y >= 0.08:
            long_score += 5
            long_reasons.append("Revenue growth >= 8%")
        elif revenue_growth_1y < 0:
            long_score -= 10
            long_reasons.append("Penalty: revenue shrinking")

    if revenue_accelerating:
        long_score += 5
        long_reasons.append("Revenue growth accelerating")
    elif revenue_decelerating:
        long_score -= 5
        long_reasons.append("Penalty: revenue growth decelerating")

    if asset_proxy:
        long_score = min(long_score, 25)
        long_reasons.append("Asset-proxy exception: requires NAV/premium model")

    long_score = max(0, min(100, long_score))

    long_core = (
        not speculative_growth
        and forward_pe is not None
        and 0 < forward_pe <= 35
        and peg_1y is not None
        and 0 < peg_1y <= 1.5
        and eps_growth_1y is not None
        and eps_growth_1y >= 0.15
        and revenue_growth_1y is not None
        and revenue_growth_1y >= 0.08
        and fcf_yield is not None
        and fcf_yield >= 0.025
    )
    long_watch = (
        not speculative_growth
        and long_score >= 55
        and forward_pe is not None
        and forward_pe > 0
        and peg_1y is not None
        and 0 < peg_1y <= 2.0
        and eps_growth_1y is not None
        and eps_growth_1y >= 0.10
    )

    if long_core:
        long_signal = "CORE"
    elif long_watch:
        long_signal = "WATCH"
    else:
        long_signal = "—"

    # Combined model: 70% fundamental + 30% P/E trend when a valid
    # trailing/forward P/E pair exists. If P/E trend is unavailable, preserve
    # the fundamental score instead of treating missing data as a zero signal.
    if valid_pe_pair:
        combined_long_score = round((0.70 * long_score) + (0.30 * pe_trend_long_score))
        combined_short_score = round((0.70 * short_score) + (0.30 * pe_trend_short_score))
    else:
        combined_long_score = long_score
        combined_short_score = short_score

    if valid_pe_pair:
        combined_long_signal = (
            "CORE" if combined_long_score >= 75
            else "WATCH" if combined_long_score >= 55
            else "—"
        )
        combined_short_signal = (
            "CORE" if combined_short_score >= 75
            else "WATCH" if combined_short_score >= 55
            else "—"
        )
    else:
        combined_long_signal = long_signal
        combined_short_signal = short_signal

    funding_rate, funding_annualized = get_funding(item["inst_id"])

    return {
        "okx_symbol": okx_symbol,
        "yahoo_symbol": yahoo_symbol,
        "company": info.get("shortName") or info.get("longName") or yahoo_symbol,
        "inst_id": item["inst_id"],
        "max_leverage": item.get("max_leverage"),
        "price": price,
        "market_cap": market_cap,
        "price_change_24h": price_change_24h,
        "price_change_7d": price_change_7d,
        "price_timing_move": price_timing_move,
        "trailing_pe": trailing_pe,
        "forward_pe": forward_pe,
        "price_to_sales": price_to_sales,
        "ev_to_sales": ev_to_sales,
        "operating_margin": operating_margin,
        "profit_margin": profit_margin,
        "speculative_growth": speculative_growth,
        "asset_proxy": asset_proxy,
        "eps_growth_1y": eps_growth_1y,
        "peg_1y": peg_1y,
        "fcf_yield": fcf_yield,
        "revenue_growth_0y": revenue_growth_0y,
        "revenue_growth_1y": revenue_growth_1y,
        "revenue_decelerating": revenue_decelerating,
        "revenue_accelerating": revenue_accelerating,
        "pe_change_pct": pe_change_pct,
        "pe_trend_long_score": pe_trend_long_score,
        "pe_trend_long_signal": pe_trend_long_signal,
        "pe_trend_long_reasons": "; ".join(pe_trend_long_reasons),
        "pe_trend_short_score": pe_trend_short_score,
        "pe_trend_short_signal": pe_trend_short_signal,
        "pe_trend_short_reasons": "; ".join(pe_trend_short_reasons),
        "combined_long_score": combined_long_score,
        "combined_long_signal": combined_long_signal,
        "combined_short_score": combined_short_score,
        "combined_short_signal": combined_short_signal,
        "funding_rate": funding_rate,
        "funding_annualized": funding_annualized,
        "short_score": short_score,
        "short_signal": short_signal,
        "short_reasons": "; ".join(short_reasons),
        "long_score": long_score,
        "long_signal": long_signal,
        "long_reasons": "; ".join(long_reasons),
        # Backward-compatible aliases for existing consumers.
        "score": short_score,
        "signal": short_signal,
        "reasons": "; ".join(short_reasons),
    }


def load_previous_snapshot():
    """Load prior hourly scores so previous LONG/SHORT status can gate timing."""
    path = DATA_DIR / "latest.csv"
    if not path.exists():
        return {}
    try:
        df = pd.read_csv(path)
    except Exception:
        return {}

    out = {}
    for _, row in df.iterrows():
        symbol = str(row.get("okx_symbol") or "").strip().upper()
        if not symbol:
            continue

        def row_num(*keys):
            for key in keys:
                if key in row:
                    value = n(row.get(key))
                    if value is not None:
                        return value
            return None

        out[symbol] = {
            "long_score": row_num("timed_long_score", "combined_long_score", "long_score"),
            "short_score": row_num("timed_short_score", "combined_short_score", "short_score"),
        }
    return out


def apply_price_timing(rows, previous_snapshot):
    """
    Final timing layer:
      - move = 50% x 24h return + 50% x 7-day return.
      - price action only changes a side if it is already qualified now, or was
        qualified in the previous hourly run.
      - LONG + falling price => stronger LONG; LONG + rally => weaker LONG.
      - SHORT + rising price => stronger SHORT; SHORT + fall => weaker SHORT.
    """
    for row in rows:
        move = n(row.get("price_timing_move"))
        if move is None:
            strength = 0
            raw_adjustment = 0
        else:
            strength = round(
                min(100.0, (abs(move) / PRICE_TIMING_FULL_MOVE) * 100.0)
            )
            raw_adjustment = round(
                (strength / 100.0) * PRICE_TIMING_MAX_ADJUSTMENT
            )

        previous = previous_snapshot.get(row["okx_symbol"], {})
        previous_long_score = n(previous.get("long_score"))
        previous_short_score = n(previous.get("short_score"))
        was_longable = (
            previous_long_score is not None
            and previous_long_score >= FINAL_WATCH_THRESHOLD
        )
        was_shortable = (
            previous_short_score is not None
            and previous_short_score >= FINAL_WATCH_THRESHOLD
        )

        base_long = int(row["combined_long_score"])
        base_short = int(row["combined_short_score"])
        long_eligible = base_long >= FINAL_WATCH_THRESHOLD or was_longable
        short_eligible = base_short >= FINAL_WATCH_THRESHOLD or was_shortable

        long_adjustment = 0
        short_adjustment = 0
        if move is not None:
            if long_eligible:
                long_adjustment = (
                    raw_adjustment if move < 0
                    else -raw_adjustment if move > 0
                    else 0
                )
            if short_eligible:
                short_adjustment = (
                    raw_adjustment if move > 0
                    else -raw_adjustment if move < 0
                    else 0
                )

        timed_long_score = max(0, min(100, base_long + long_adjustment))
        timed_short_score = max(0, min(100, base_short + short_adjustment))

        row["timing_strength"] = strength
        row["timing_long_adjustment"] = long_adjustment
        row["timing_short_adjustment"] = short_adjustment
        row["previous_longable"] = was_longable
        row["previous_shortable"] = was_shortable
        row["timed_long_score"] = timed_long_score
        row["timed_short_score"] = timed_short_score
        row["timed_long_signal"] = (
            "CORE" if timed_long_score >= FINAL_CORE_THRESHOLD
            else "WATCH" if timed_long_score >= FINAL_WATCH_THRESHOLD
            else "—"
        )
        row["timed_short_signal"] = (
            "CORE" if timed_short_score >= FINAL_CORE_THRESHOLD
            else "WATCH" if timed_short_score >= FINAL_WATCH_THRESHOLD
            else "—"
        )


def write_latest_csv(rows):
    path = DATA_DIR / "latest.csv"
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    pd.DataFrame(rows).to_csv(path, index=False)


def append_history(rows, timestamp):
    if not rows:
        return

    path = DATA_DIR / "history.csv"
    fields = [
        "timestamp_utc",
        "okx_symbol",
        "company",
        "inst_id",
        "price",
        "market_cap",
        "price_change_24h",
        "price_change_7d",
        "price_timing_move",
        "timing_strength",
        "timing_long_adjustment",
        "timing_short_adjustment",
        "previous_longable",
        "previous_shortable",
        "timed_long_score",
        "timed_long_signal",
        "timed_short_score",
        "timed_short_signal",
        "trailing_pe",
        "forward_pe",
        "price_to_sales",
        "ev_to_sales",
        "operating_margin",
        "profit_margin",
        "speculative_growth",
        "eps_growth_1y",
        "peg_1y",
        "fcf_yield",
        "revenue_growth_0y",
        "revenue_growth_1y",
        "pe_change_pct",
        "pe_trend_long_score",
        "pe_trend_long_signal",
        "pe_trend_short_score",
        "pe_trend_short_signal",
        "combined_long_score",
        "combined_long_signal",
        "combined_short_score",
        "combined_short_signal",
        "funding_annualized",
        "short_score",
        "short_signal",
        "long_score",
        "long_signal",
    ]
    exists = path.exists()

    # history.csv previously used a shorter schema. Preserve it once and start
    # a clean file so later backtests never mix incompatible row formats.
    if exists:
        try:
            with path.open("r", newline="", encoding="utf-8") as existing_file:
                old_header = next(csv.reader(existing_file), [])
        except Exception:
            old_header = []
        if old_header != fields:
            legacy = DATA_DIR / (
                "history_legacy_"
                + datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
                + ".csv"
            )
            path.replace(legacy)
            exists = False
            print(f"WARN: migrated incompatible history.csv to {legacy}")

    with path.open("a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        if not exists:
            w.writeheader()
        for row in rows:
            w.writerow(
                {
                    "timestamp_utc": timestamp,
                    **{k: row.get(k) for k in fields if k != "timestamp_utc"},
                }
            )


def full_table_lines(rows):
    ordered = sorted(
        rows,
        key=lambda r: (max(r["long_score"], r["short_score"]), r["long_score"]),
        reverse=True,
    )
    lines = [
        "| Company | OKX | P/S | EV/S | Op margin | Fwd P/E | EPS +1y | Rev +1y | FCF yield | LONG | SHORT |",
        "|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for r in ordered:
        long_label = f"{r['long_score']} {r['long_signal']}" if r["long_signal"] != "—" else str(r["long_score"])
        short_label = f"{r['short_score']} {r['short_signal']}" if r["short_signal"] != "—" else str(r["short_score"])
        lines.append(
            f"| {r['company']} | `{r['okx_symbol']}` | {fmt_num(r['price_to_sales'], 1)} | "
            f"{fmt_num(r['ev_to_sales'], 1)} | {fmt_pct(r['operating_margin'])} | "
            f"{fmt_num(r['forward_pe'])} | {fmt_pct(r['eps_growth_1y'])} | "
            f"{fmt_pct(r['revenue_growth_1y'])} | {fmt_pct(r['fcf_yield'])} | "
            f"**{long_label}** | **{short_label}** |"
        )
    return lines


def pe_trend_table(rows, side, limit=10):
    score_key = f"pe_trend_{side}_score"
    signal_key = f"pe_trend_{side}_signal"
    ranked = sorted(rows, key=lambda r: r[score_key], reverse=True)
    candidates = [r for r in ranked if r[signal_key] != "—"][:limit]

    lines = [
        f"| Rank | Company | OKX | Trail P/E | Fwd P/E | P/E change | EPS +1y | Rev +1y | Rev trend | {side.upper()} score | Signal |",
        "|---:|---|---|---:|---:|---:|---:|---:|---|---:|---|",
    ]
    for i, r in enumerate(candidates, 1):
        rev_trend = (
            "accelerating"
            if r["revenue_accelerating"]
            else "decelerating"
            if r["revenue_decelerating"]
            else "stable/unknown"
        )
        lines.append(
            f"| {i} | {r['company']} | `{r['okx_symbol']}` | "
            f"{fmt_num(r['trailing_pe'])} | {fmt_num(r['forward_pe'])} | "
            f"{fmt_pct(r['pe_change_pct'])} | {fmt_pct(r['eps_growth_1y'])} | "
            f"{fmt_pct(r['revenue_growth_1y'])} | {rev_trend} | "
            f"**{r[score_key]}** | **{r[signal_key]}** |"
        )
    if not candidates:
        lines.append("| — | No candidates | — | — | — | — | — | — | — | — | — |")
    return lines


def combined_table(rows, side, limit=10):
    score_key = f"combined_{side}_score"
    signal_key = f"combined_{side}_signal"
    fundamental_key = f"{side}_score"
    pe_key = f"pe_trend_{side}_score"
    ranked = sorted(rows, key=lambda r: (r[score_key], r[fundamental_key], r[pe_key]), reverse=True)
    candidates = [r for r in ranked if r[signal_key] != "—"][:limit]

    lines = [
        f"| Rank | Company | OKX | Fundamental {side.upper()} | P/E trend {side.upper()} | Combined | Signal |",
        "|---:|---|---|---:|---:|---:|---|",
    ]
    for i, r in enumerate(candidates, 1):
        lines.append(
            f"| {i} | {r['company']} | `{r['okx_symbol']}` | "
            f"{r[fundamental_key]} | {r[pe_key]} | "
            f"**{r[score_key]}** | **{r[signal_key]}** |"
        )
    if not candidates:
        lines.append("| — | No candidates | — | — | — | — | — |")
    return lines


def timed_table(rows, side, limit=15):
    score_key = f"timed_{side}_score"
    signal_key = f"timed_{side}_signal"
    base_key = f"combined_{side}_score"
    adjustment_key = f"timing_{side}_adjustment"
    previous_key = f"previous_{side}able"
    ranked = sorted(
        rows,
        key=lambda r: (r[score_key], r[base_key], r["timing_strength"]),
        reverse=True,
    )
    candidates = [r for r in ranked if r[signal_key] != "—"][:limit]

    lines = [
        f"| Rank | Company | OKX | 24h | 7d | 50/50 move | Base {side.upper()} | Timing adj. | Final | Signal | Prev. {side.upper()}? |",
        "|---:|---|---|---:|---:|---:|---:|---:|---:|---|---|",
    ]
    for i, r in enumerate(candidates, 1):
        adjustment = int(r[adjustment_key])
        lines.append(
            f"| {i} | {r['company']} | {r['okx_symbol']} | "
            f"{fmt_pct(r['price_change_24h'])} | {fmt_pct(r['price_change_7d'])} | "
            f"{fmt_pct(r['price_timing_move'])} | {r[base_key]} | {adjustment:+d} | "
            f"**{r[score_key]}** | **{r[signal_key]}** | "
            f"{'yes' if r[previous_key] else 'no'} |"
        )
    if not candidates:
        lines.append("| — | No candidates | — | — | — | — | — | — | — | — | — |")
    return lines


def candidate_table(rows, side, limit=15):
    score_key = f"{side}_score"
    signal_key = f"{side}_signal"
    ranked = sorted(rows, key=lambda r: (r[score_key], r["peg_1y"] or 9999), reverse=True)
    candidates = [r for r in ranked if r[signal_key] != "—"][:limit]

    lines = [
        f"| Rank | Company | OKX market | {side.upper()} score | Signal | P/S | EV/S | Op margin | Fwd P/E | Rev +1y | FCF yield |",
        "|---:|---|---|---:|---|---:|---:|---:|---:|---:|---:|",
    ]
    for i, r in enumerate(candidates, 1):
        lines.append(
            f"| {i} | {r['company']} | `{r['inst_id']}` | **{r[score_key]}** | "
            f"**{r[signal_key]}** | {fmt_num(r['price_to_sales'], 1)} | "
            f"{fmt_num(r['ev_to_sales'], 1)} | {fmt_pct(r['operating_margin'])} | "
            f"{fmt_num(r['forward_pe'])} | {fmt_pct(r['revenue_growth_1y'])} | "
            f"{fmt_pct(r['fcf_yield'])} |"
        )
    if not candidates:
        lines.append("| — | No candidates | — | — | — | — | — | — | — | — | — |")
    return lines


def write_report(rows, universe_count, timestamp):
    lines = [
        "# OKX Long / Short Fundamental Scanner",
        "",
        f"**Updated:** {timestamp}",
        f"**OKX stock/RWA perps discovered:** {universe_count}",
        f"**Public companies with usable fundamentals:** {len(rows)}",
        "",
        "## Final model + Price Timing — SHORT",
        "",
        *timed_table(rows, "short"),
        "",
        "## Final model + Price Timing — LONG",
        "",
        *timed_table(rows, "long"),
        "",
        "## Top SHORT candidates — fundamentals only",
        "",
        *candidate_table(rows, "short"),
        "",
        "## Top LONG candidates — fundamentals only",
        "",
        *candidate_table(rows, "long"),
        "",
        "## Combined model — LONG",
        "",
        *combined_table(rows, "long"),
        "",
        "## Combined model — SHORT",
        "",
        *combined_table(rows, "short"),
        "",
        "## P/E Compression + Growth — LONG",
        "",
        *pe_trend_table(rows, "long"),
        "",
        "## P/E Expansion + Weakening — SHORT",
        "",
        *pe_trend_table(rows, "short"),
        "",
        "## All companies",
        "",
        *full_table_lines(rows),
        "",
        "The scanner is a research ranking, not a trade instruction. Speculative-growth names are scored primarily on sales valuation, margins and cash generation rather than PEG.",
    ]
    (REPORT_DIR / "latest.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_readme(rows, universe_count, timestamp):
    short_core = sum(r["short_signal"] == "CORE" for r in rows)
    long_core = sum(r["long_signal"] == "CORE" for r in rows)

    lines = [
        "# OKX Long / Short Fundamental Scanner",
        "",
        "Hourly scanner restricted to public companies exposed by the **OKX EEA TradFi / Stock Perpetual API universe**.",
        "",
        f"**Last scan:** {timestamp}  ",
        f"**Availability scope:** {DISCOVERY_SCOPE}  ",
        f"**OKX stock/ETF markets in configured universe:** {universe_count}  ",
        f"**Public companies analysed:** {len(rows)}  ",
        f"**SHORT CORE:** {short_core}  ",
        f"**LONG CORE:** {long_core}",
        "",
        "## Model",
        "",
        "Profitable companies use a PEG-like valuation framework plus growth and free-cash-flow quality. Loss-making/speculative-growth companies use **P/S, EV/Sales, operating margin and FCF** as the primary valuation lens, because huge EPS-growth percentages can be distorted by a tiny or negative base. Asset-proxy companies such as MSTR are excluded from the sales-multiple model and need a separate NAV/premium framework.",
        "",
        "### SHORT CORE",
        "",
        "Two routes: (1) classic expensive/slow-growth companies, or (2) loss-making companies with extreme sales multiples and weak margins/cash generation. A loss-making company at >=40x P/S or EV/Sales gets a minimum short-risk score of 80.",
        "",
        "### LONG CORE",
        "",
        "Requires established profitability, reasonable forward valuation, strong growth and positive FCF yield. Speculative/loss-making names cannot qualify for LONG CORE from PEG alone.",
        "",
        "Scores are 0-100 heuristics. Revenue acceleration helps LONG and penalizes SHORT; deceleration does the opposite. Funding is not applicable to these Spot xStocks markets.",
        "",
        "### Separate P/E trend model",
        "",
        "This second ranking does **not replace** the main model. It compares trailing P/E with forward P/E and then checks whether expected EPS and revenue direction support the move. Falling forward P/E with positive growth raises the P/E-trend LONG score; rising forward P/E with weakening growth raises the P/E-trend SHORT score. Extreme absolute forward P/E is penalized on the LONG side.",
        "",
        "### Price Timing / Dislocation layer",
        "",
        "The final ranking adds entry timing without allowing price momentum to create a thesis by itself. Price move = **50% 24h return + 50% 7-day return**. A 25% absolute weighted move is maximum timing stress and can adjust the final score by up to 20 points. If a name is already LONG-qualified now or was LONG-qualified in the previous hourly run, a fall boosts LONG and a rally reduces it. If it is already SHORT-qualified, a rally boosts SHORT and a fall reduces it.",
        "",
        "## Final model + Price Timing — LONG",
        "",
        *timed_table(rows, "long", 10),
        "",
        "## Final model + Price Timing — SHORT",
        "",
        *timed_table(rows, "short", 10),
        "",
        "## Combined model — LONG",
        "",
        "Weighted score: **70% fundamental + 30% P/E trend**.",
        "",
        *combined_table(rows, "long", 10),
        "",
        "## Combined model — SHORT",
        "",
        "Weighted score: **70% fundamental + 30% P/E trend**.",
        "",
        *combined_table(rows, "short", 10),
        "",
        "## P/E Compression + Growth — LONG",
        "",
        *pe_trend_table(rows, "long", 10),
        "",
        "## P/E Expansion + Weakening — SHORT",
        "",
        *pe_trend_table(rows, "short", 10),
        "",
        "## Top SHORT candidates",
        "",
        *candidate_table(rows, "short", 10),
        "",
        "## Top LONG candidates",
        "",
        *candidate_table(rows, "long", 10),
        "",
        "## All OKX companies — our ratio + LONG/SHORT scores",
        "",
        *full_table_lines(rows),
        "",
        "## Files",
        "",
        "- `scanner.py` — scanner and scoring logic",
        "- `reports/latest.md` — latest full report",
        "- `data/latest.csv` — latest machine-readable snapshot",
        "- `data/history.csv` — hourly history of **all companies** for later backtests",
        "- `.github/workflows/hourly-okx-scanner.yml` — hourly GitHub Action",
        "",
        "## Data",
        "",
        "The configured universe can be pinned to the exact OKX EEA xStocks/USDC markets confirmed in the user's app. When that allowlist is present it overrides the broader public catalogue. Yahoo Finance/yfinance supplies company valuation, cash-flow and analyst-growth estimates. ETFs can exist in the OKX universe but are excluded from the company-fundamentals ranking.",
        "",
        "### Optional account-accurate filter",
        "",
        "Add read-only GitHub Actions secrets `OKX_API_KEY`, `OKX_API_SECRET`, and `OKX_API_PASSPHRASE`. The scanner will then query the authenticated OKX EEA account-instruments endpoint and only score contracts available to that account. Do not grant Trade or Withdraw permission for this scanner.",
        "",
        "This is a quantitative research screen, not an automatic trading system. It does not place orders or select leverage.",
    ]
    Path("README.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main():
    started = datetime.now(timezone.utc)
    timestamp = started.strftime("%Y-%m-%d %H:%M UTC")

    universe = discover_okx_stock_perps()
    rows = []

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as pool:
        futures = {pool.submit(fetch_fundamentals, item): item for item in universe}
        for future in as_completed(futures):
            item = futures[future]
            try:
                row = future.result()
                if row:
                    rows.append(row)
            except Exception as exc:
                print(f"WARN {item['inst_id']}: {exc}")

    previous_snapshot = load_previous_snapshot()
    apply_price_timing(rows, previous_snapshot)

    rows.sort(
        key=lambda r: (
            max(r["timed_long_score"], r["timed_short_score"]),
            r["timed_long_score"],
        ),
        reverse=True,
    )

    write_latest_csv(rows)
    append_history(rows, timestamp)
    write_report(rows, len(universe), timestamp)
    write_readme(rows, len(universe), timestamp)

    print(f"Scanned {len(rows)} public companies from {len(universe)} OKX TradFi/RWA perps.")
    print("Top FINAL SHORT:")
    for r in sorted(rows, key=lambda x: x["timed_short_score"], reverse=True)[:5]:
        print(
            f"  {r['okx_symbol']:>12} finalShort={r['timed_short_score']:3} "
            f"{r['timed_short_signal']:<5} base={r['combined_short_score']:3} "
            f"24h={fmt_pct(r['price_change_24h'])} 7d={fmt_pct(r['price_change_7d'])} "
            f"timing={r['timing_short_adjustment']:+d}"
        )
    print("Top FINAL LONG:")
    for r in sorted(rows, key=lambda x: x["timed_long_score"], reverse=True)[:5]:
        print(
            f"  {r['okx_symbol']:>12} finalLong={r['timed_long_score']:3} "
            f"{r['timed_long_signal']:<5} base={r['combined_long_score']:3} "
            f"24h={fmt_pct(r['price_change_24h'])} 7d={fmt_pct(r['price_change_7d'])} "
            f"timing={r['timing_long_adjustment']:+d}"
        )
    print("Top FUNDAMENTAL SHORT:")
    for r in sorted(rows, key=lambda x: x["short_score"], reverse=True)[:5]:
        print(
            f"  {r['okx_symbol']:>12} short={r['short_score']:3} {r['short_signal']:<5} "
            f"ratio={fmt_num(r['peg_1y'],2)} fwdPE={fmt_num(r['forward_pe'])}"
        )
    print("Top COMBINED LONG:")
    for r in sorted(rows, key=lambda x: x["combined_long_score"], reverse=True)[:5]:
        print(
            f"  {r['okx_symbol']:>12} combinedLong={r['combined_long_score']:3} "
            f"{r['combined_long_signal']:<5} fundamental={r['long_score']:3} "
            f"peTrend={r['pe_trend_long_score']:3}"
        )
    print("Top COMBINED SHORT:")
    for r in sorted(rows, key=lambda x: x["combined_short_score"], reverse=True)[:5]:
        print(
            f"  {r['okx_symbol']:>12} combinedShort={r['combined_short_score']:3} "
            f"{r['combined_short_signal']:<5} fundamental={r['short_score']:3} "
            f"peTrend={r['pe_trend_short_score']:3}"
        )
    print("Top P/E TREND LONG:")
    for r in sorted(rows, key=lambda x: x["pe_trend_long_score"], reverse=True)[:5]:
        print(
            f"  {r['okx_symbol']:>12} peLong={r['pe_trend_long_score']:3} "
            f"{r['pe_trend_long_signal']:<5} trailPE={fmt_num(r['trailing_pe'])} "
            f"fwdPE={fmt_num(r['forward_pe'])} delta={fmt_pct(r['pe_change_pct'])}"
        )
    print("Top P/E TREND SHORT:")
    for r in sorted(rows, key=lambda x: x["pe_trend_short_score"], reverse=True)[:5]:
        print(
            f"  {r['okx_symbol']:>12} peShort={r['pe_trend_short_score']:3} "
            f"{r['pe_trend_short_signal']:<5} trailPE={fmt_num(r['trailing_pe'])} "
            f"fwdPE={fmt_num(r['forward_pe'])} delta={fmt_pct(r['pe_change_pct'])}"
        )
    print("Top LONG:")
    for r in sorted(rows, key=lambda x: x["long_score"], reverse=True)[:5]:
        print(
            f"  {r['okx_symbol']:>12} long={r['long_score']:3} {r['long_signal']:<5} "
            f"ratio={fmt_num(r['peg_1y'],2)} fwdPE={fmt_num(r['forward_pe'])}"
        )


if __name__ == "__main__":
    main()
