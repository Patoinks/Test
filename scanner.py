from __future__ import annotations

import csv
import math
import os
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd
import requests
import yfinance as yf

OKX_BASE = os.getenv("OKX_BASE_URL", "https://eea.okx.com")
OKX_GROUP_IDS = {"6", "7"}  # SWAP RWA / stock-perpetual fee groups
MAX_WORKERS = int(os.getenv("MAX_WORKERS", "6"))
TIMEOUT = 20

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
""".split()))

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


def discover_okx_stock_perps():
    """
    Discover live OKX EEA TradFi/RWA perpetuals dynamically.
    groupId 6/7 are the RWA/stock SWAP fee groups in current OKX API docs.
    ETF/index/commodity instruments are allowed through discovery but are later
    excluded unless Yahoo identifies the underlying as an EQUITY.
    """
    instruments = okx_get("/api/v5/public/instruments", {"instType": "SWAP"})
    out = []
    for item in instruments:
        if item.get("state") != "live":
            continue
        if str(item.get("groupId")) not in OKX_GROUP_IDS:
            continue
        inst_id = item.get("instId", "")
        if not inst_id.endswith("-USDT-SWAP"):
            continue
        okx_symbol = inst_id.split("-")[0]
        out.append(
            {
                "okx_symbol": okx_symbol,
                "inst_id": inst_id,
                "max_leverage": n(item.get("lever")),
            }
        )
    if out:
        return out

    # Some public OKX endpoints omit the RWA fee-group catalogue depending on
    # region/IP. Fall back to the current official OKX Europe TradFi universe.
    print("WARN: OKX public catalogue did not expose RWA groups; using official fallback universe.")
    return [
        {
            "okx_symbol": symbol,
            "inst_id": f"{symbol}-USDT-SWAP",
            "max_leverage": 5.0,
        }
        for symbol in FALLBACK_OKX_SYMBOLS
    ]


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


def fetch_fundamentals(item):
    okx_symbol = item["okx_symbol"]
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

    trailing_pe = n(info.get("trailingPE"))
    forward_pe = n(info.get("forwardPE"))
    fcf = n(info.get("freeCashflow"))
    fcf_yield = (fcf / market_cap) if fcf is not None and market_cap else None

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

    # Our PEG: forward P/E divided by expected EPS growth percentage.
    peg_1y = None
    if forward_pe is not None and eps_growth_1y is not None and eps_growth_1y > 0:
        peg_1y = forward_pe / (eps_growth_1y * 100.0)

    # Transparent 0-100 score based on the rules from the discussion.
    score = 0
    reasons = []

    if forward_pe is not None and forward_pe > 40:
        score += 25
        reasons.append("Forward P/E > 40")
    if trailing_pe is not None and trailing_pe > 40:
        score += 15
        reasons.append("Trailing P/E > 40")
    if peg_1y is not None and peg_1y > 2.5:
        score += 20
        reasons.append("PEG(1y) > 2.5")
    if eps_growth_1y is not None and eps_growth_1y < 0.20:
        score += 20
        reasons.append("EPS growth < 20%")
    if fcf_yield is not None and fcf_yield < 0.025:
        score += 10
        reasons.append("FCF yield < 2.5%")
    if revenue_decelerating:
        score += 10
        reasons.append("Revenue growth decelerating")

    core = (
        forward_pe is not None
        and forward_pe > 40
        and peg_1y is not None
        and peg_1y > 2.5
        and eps_growth_1y is not None
        and eps_growth_1y < 0.20
    )

    funding_rate, funding_annualized = get_funding(item["inst_id"])

    # WATCH still requires a clear valuation-vs-growth mismatch.
    # This deliberately excludes expensive companies whose earnings are
    # expected to grow fast enough to keep PEG low.
    watch = (
        forward_pe is not None
        and forward_pe > 40
        and eps_growth_1y is not None
        and eps_growth_1y < 0.25
        and (peg_1y is None or peg_1y > 2.0)
    )

    if core:
        signal = "CORE"
    elif watch:
        signal = "WATCH"
    else:
        signal = "NO SIGNAL"

    return {
        "okx_symbol": okx_symbol,
        "yahoo_symbol": yahoo_symbol,
        "company": info.get("shortName") or info.get("longName") or yahoo_symbol,
        "inst_id": item["inst_id"],
        "max_leverage": item.get("max_leverage"),
        "price": n(info.get("currentPrice") or info.get("regularMarketPrice")),
        "market_cap": market_cap,
        "trailing_pe": trailing_pe,
        "forward_pe": forward_pe,
        "eps_growth_1y": eps_growth_1y,
        "peg_1y": peg_1y,
        "fcf_yield": fcf_yield,
        "revenue_growth_0y": revenue_growth_0y,
        "revenue_growth_1y": revenue_growth_1y,
        "revenue_decelerating": revenue_decelerating,
        "funding_rate": funding_rate,
        "funding_annualized": funding_annualized,
        "score": score,
        "signal": signal,
        "reasons": "; ".join(reasons),
    }


def write_latest_csv(rows):
    path = DATA_DIR / "latest.csv"
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    pd.DataFrame(rows).to_csv(path, index=False)


def append_core_history(rows, timestamp):
    core_rows = [r for r in rows if r["signal"] == "CORE"]
    if not core_rows:
        return

    path = DATA_DIR / "history.csv"
    fields = [
        "timestamp_utc",
        "okx_symbol",
        "company",
        "inst_id",
        "score",
        "trailing_pe",
        "forward_pe",
        "eps_growth_1y",
        "peg_1y",
        "fcf_yield",
        "revenue_growth_1y",
        "funding_annualized",
    ]
    exists = path.exists()
    with path.open("a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        if not exists:
            w.writeheader()
        for row in core_rows:
            w.writerow(
                {
                    "timestamp_utc": timestamp,
                    **{k: row.get(k) for k in fields if k != "timestamp_utc"},
                }
            )


def write_report(rows, universe_count, timestamp):
    ranked = sorted(
        rows,
        key=lambda r: (r["score"], r["forward_pe"] or -1),
        reverse=True,
    )
    candidates = [r for r in ranked if r["signal"] != "NO SIGNAL"][:25]

    lines = [
        "# OKX Overvaluation Scanner",
        "",
        f"**Updated:** {timestamp}",
        f"**OKX stock/RWA perps discovered:** {universe_count}",
        f"**Public companies with usable fundamentals:** {len(rows)}",
        f"**CORE candidates:** {sum(r['signal'] == 'CORE' for r in rows)}",
        "",
        "CORE rule: **Forward P/E > 40 + PEG(1y) > 2.5 + expected EPS growth next year < 20%**.",
        "",
        "> Positive funding is generally favorable carry for a short; negative funding means the short generally pays. Funding is annualized mechanically from the current interval and can change quickly.",
        "",
    ]

    if not candidates:
        lines += ["No CORE/WATCH candidates in the current scan.", ""]
    else:
        lines += [
            "| Rank | Signal | Company | OKX perp | Score | Trail P/E | Fwd P/E | EPS +1y | PEG 1y | FCF yield | Rev +1y | Funding ann. |",
            "|---:|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|",
        ]
        for i, r in enumerate(candidates, 1):
            lines.append(
                f"| {i} | **{r['signal']}** | {r['company']} | `{r['inst_id']}` | "
                f"**{r['score']}** | {fmt_num(r['trailing_pe'])} | {fmt_num(r['forward_pe'])} | "
                f"{fmt_pct(r['eps_growth_1y'])} | {fmt_num(r['peg_1y'], 2)} | "
                f"{fmt_pct(r['fcf_yield'])} | {fmt_pct(r['revenue_growth_1y'])} | "
                f"{fmt_pct(r['funding_annualized'])} |"
            )
        lines.append("")

    lines += [
        "## Why each candidate scored",
        "",
    ]
    for r in candidates[:15]:
        lines.append(f"- **{r['okx_symbol']} ({r['score']}/100):** {r['reasons'] or 'No threshold flags'}")
    lines += [
        "",
        "## Interpretation",
        "",
        "- **CORE** = satisfies the three central valuation-vs-growth conditions.",
        "- **WATCH** = forward P/E > 40, expected EPS growth < 25%, plus PEG > 2 when calculable; it narrowly misses CORE.",
        "- This is a research screen, not a prediction that the stock will fall.",
        "- The scanner does not place trades or choose leverage.",
        "",
        "Data: OKX EEA public API + Yahoo Finance/yfinance. Analyst estimates and funding can change between runs.",
    ]

    (REPORT_DIR / "latest.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


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

    rows.sort(key=lambda r: (r["score"], r["forward_pe"] or -1), reverse=True)

    write_latest_csv(rows)
    append_core_history(rows, timestamp)
    write_report(rows, len(universe), timestamp)

    print(f"Scanned {len(rows)} public companies from {len(universe)} OKX TradFi/RWA perps.")
    for r in rows[:10]:
        print(
            f"{r['okx_symbol']:>12} score={r['score']:3} signal={r['signal']:<9} "
            f"fwdPE={fmt_num(r['forward_pe'])} PEG={fmt_num(r['peg_1y'],2)} "
            f"EPS+1y={fmt_pct(r['eps_growth_1y'])} funding={fmt_pct(r['funding_annualized'])}"
        )


if __name__ == "__main__":
    main()
