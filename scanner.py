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
    revenue_accelerating = (
        revenue_growth_0y is not None
        and revenue_growth_1y is not None
        and revenue_growth_1y > revenue_growth_0y
    )

    # Our core ratio: forward P/E divided by expected EPS growth percentage.
    peg_1y = None
    if forward_pe is not None and eps_growth_1y is not None and eps_growth_1y > 0:
        peg_1y = forward_pe / (eps_growth_1y * 100.0)

    # SHORT score: expensive valuation relative to expected growth.
    short_score = 0
    short_reasons = []

    if forward_pe is not None and forward_pe > 40:
        short_score += 25
        short_reasons.append("Forward P/E > 40")
    if trailing_pe is not None and trailing_pe > 40:
        short_score += 15
        short_reasons.append("Trailing P/E > 40")
    if peg_1y is not None and peg_1y > 2.5:
        short_score += 20
        short_reasons.append("Ratio/PEG > 2.5")
    if eps_growth_1y is not None and eps_growth_1y < 0.20:
        short_score += 20
        short_reasons.append("EPS growth < 20%")
    if fcf_yield is not None and fcf_yield < 0.025:
        short_score += 10
        short_reasons.append("FCF yield < 2.5%")
    if revenue_decelerating:
        short_score += 10
        short_reasons.append("Revenue growth decelerating")
    if revenue_accelerating:
        short_score -= 10
        short_reasons.append("Penalty: revenue growth accelerating")
    short_score = max(0, min(100, short_score))

    short_core = (
        forward_pe is not None
        and forward_pe > 40
        and peg_1y is not None
        and peg_1y > 2.5
        and eps_growth_1y is not None
        and eps_growth_1y < 0.20
    )
    short_watch = (
        forward_pe is not None
        and forward_pe > 40
        and eps_growth_1y is not None
        and eps_growth_1y < 0.25
        and (peg_1y is None or peg_1y > 2.0)
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

    if peg_1y is not None and peg_1y > 0:
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

    long_score = max(0, min(100, long_score))

    long_core = (
        forward_pe is not None
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
        long_score >= 55
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

    funding_rate, funding_annualized = get_funding(item["inst_id"])

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
        "revenue_accelerating": revenue_accelerating,
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
        "trailing_pe",
        "forward_pe",
        "eps_growth_1y",
        "peg_1y",
        "fcf_yield",
        "revenue_growth_0y",
        "revenue_growth_1y",
        "funding_annualized",
        "short_score",
        "short_signal",
        "long_score",
        "long_signal",
    ]
    exists = path.exists()
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
        "| Company | OKX | Our ratio | Fwd P/E | Trail P/E | EPS +1y | Rev +1y | FCF yield | LONG | SHORT | Funding ann. |",
        "|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for r in ordered:
        long_label = f"{r['long_score']} {r['long_signal']}" if r["long_signal"] != "—" else str(r["long_score"])
        short_label = f"{r['short_score']} {r['short_signal']}" if r["short_signal"] != "—" else str(r["short_score"])
        lines.append(
            f"| {r['company']} | `{r['okx_symbol']}` | {fmt_num(r['peg_1y'], 2)} | "
            f"{fmt_num(r['forward_pe'])} | {fmt_num(r['trailing_pe'])} | "
            f"{fmt_pct(r['eps_growth_1y'])} | {fmt_pct(r['revenue_growth_1y'])} | "
            f"{fmt_pct(r['fcf_yield'])} | **{long_label}** | **{short_label}** | "
            f"{fmt_pct(r['funding_annualized'])} |"
        )
    return lines


def candidate_table(rows, side, limit=15):
    score_key = f"{side}_score"
    signal_key = f"{side}_signal"
    ranked = sorted(rows, key=lambda r: (r[score_key], r["peg_1y"] or 9999), reverse=True)
    candidates = [r for r in ranked if r[signal_key] != "—"][:limit]

    lines = [
        f"| Rank | Company | OKX perp | {side.upper()} score | Signal | Our ratio | Fwd P/E | EPS +1y | Rev +1y | FCF yield | Funding ann. |",
        "|---:|---|---|---:|---|---:|---:|---:|---:|---:|---:|",
    ]
    for i, r in enumerate(candidates, 1):
        lines.append(
            f"| {i} | {r['company']} | `{r['inst_id']}` | **{r[score_key]}** | "
            f"**{r[signal_key]}** | {fmt_num(r['peg_1y'], 2)} | {fmt_num(r['forward_pe'])} | "
            f"{fmt_pct(r['eps_growth_1y'])} | {fmt_pct(r['revenue_growth_1y'])} | "
            f"{fmt_pct(r['fcf_yield'])} | {fmt_pct(r['funding_annualized'])} |"
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
        "## Top SHORT candidates",
        "",
        *candidate_table(rows, "short"),
        "",
        "## Top LONG candidates",
        "",
        *candidate_table(rows, "long"),
        "",
        "## All companies",
        "",
        *full_table_lines(rows),
        "",
        "The scanner is a research ranking, not a trade instruction. Funding is a live carry input and can change rapidly.",
    ]
    (REPORT_DIR / "latest.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_readme(rows, universe_count, timestamp):
    short_core = sum(r["short_signal"] == "CORE" for r in rows)
    long_core = sum(r["long_signal"] == "CORE" for r in rows)

    lines = [
        "# OKX Long / Short Fundamental Scanner",
        "",
        "Hourly scanner restricted to public companies represented in the **OKX TradFi / Stock Perpetual** universe.",
        "",
        f"**Last scan:** {timestamp}  ",
        f"**OKX TradFi/RWA instruments discovered:** {universe_count}  ",
        f"**Public companies analysed:** {len(rows)}  ",
        f"**SHORT CORE:** {short_core}  ",
        f"**LONG CORE:** {long_core}",
        "",
        "## Our ratio",
        "",
        "**Our ratio = Forward P/E ÷ expected EPS growth (%)**. It is PEG-like: lower can indicate more growth per unit of valuation; very high can indicate expensive valuation relative to expected growth.",
        "",
        "### SHORT CORE",
        "",
        "`Forward P/E > 40` + `Our ratio > 2.5` + `EPS growth < 20%`.",
        "",
        "### LONG CORE",
        "",
        "`Forward P/E <= 35` + `Our ratio <= 1.5` + `EPS growth >= 15%` + `Revenue growth >= 8%` + `FCF yield >= 2.5%`.",
        "",
        "Scores are 0-100 heuristics. Revenue acceleration helps LONG and penalizes SHORT; deceleration does the opposite. Funding is shown separately because it affects the cost/carry of holding an OKX perpetual.",
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
        "OKX public market data provides the TradFi/perpetual context and funding. Yahoo Finance/yfinance supplies valuation, cash-flow and analyst-growth estimates. Availability can differ by OKX account/jurisdiction.",
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

    rows.sort(
        key=lambda r: (max(r["long_score"], r["short_score"]), r["long_score"]),
        reverse=True,
    )

    write_latest_csv(rows)
    append_history(rows, timestamp)
    write_report(rows, len(universe), timestamp)
    write_readme(rows, len(universe), timestamp)

    print(f"Scanned {len(rows)} public companies from {len(universe)} OKX TradFi/RWA perps.")
    print("Top SHORT:")
    for r in sorted(rows, key=lambda x: x["short_score"], reverse=True)[:5]:
        print(
            f"  {r['okx_symbol']:>12} short={r['short_score']:3} {r['short_signal']:<5} "
            f"ratio={fmt_num(r['peg_1y'],2)} fwdPE={fmt_num(r['forward_pe'])}"
        )
    print("Top LONG:")
    for r in sorted(rows, key=lambda x: x["long_score"], reverse=True)[:5]:
        print(
            f"  {r['okx_symbol']:>12} long={r['long_score']:3} {r['long_signal']:<5} "
            f"ratio={fmt_num(r['peg_1y'],2)} fwdPE={fmt_num(r['forward_pe'])}"
        )


if __name__ == "__main__":
    main()
