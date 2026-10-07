from __future__ import annotations

import math
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd
import yfinance as yf


BTC_TICKER = "BTC-USD"
HK_ASSETS = {
    "Hang Seng Index": "^HSI",
    "Hang Seng TECH": "HSTECH.HK",
    "Xiaomi": "1810.HK",
}

INTRADAY_PERIOD = "60d"
INTRADAY_INTERVAL = "5m"
LAG_MINUTES = (0, 5, 15, 30, 60)
BTC_DROP_THRESHOLD_5M = -0.0025
HK_TZ = "Asia/Hong_Kong"

REPORT_DIR = Path("reports")
DATA_DIR = Path("data")
REPORT_DIR.mkdir(exist_ok=True)
DATA_DIR.mkdir(exist_ok=True)


def _num(value):
    try:
        x = float(value)
        return x if math.isfinite(x) else None
    except (TypeError, ValueError):
        return None


def _fmt_corr(value):
    x = _num(value)
    return "—" if x is None else f"{x:+.2f}"


def _fmt_pct(value, digits=2):
    x = _num(value)
    return "—" if x is None else f"{x * 100:+.{digits}f}%"


def _fmt_rate(value, digits=0):
    x = _num(value)
    return "—" if x is None else f"{x * 100:.{digits}f}%"


def _history(symbol, period, interval):
    frame = yf.Ticker(symbol).history(
        period=period,
        interval=interval,
        auto_adjust=False,
        prepost=False,
        actions=False,
    )
    if frame is None or frame.empty or "Close" not in frame.columns:
        raise RuntimeError(f"No {interval} history for {symbol}")

    frame = frame.copy()
    idx = pd.DatetimeIndex(frame.index)
    if idx.tz is None:
        if symbol.endswith(".HK") or symbol == "^HSI":
            idx = idx.tz_localize(HK_TZ)
        else:
            idx = idx.tz_localize("UTC")
    idx = idx.tz_convert("UTC")
    if interval == "5m":
        idx = idx.floor("5min")

    frame.index = idx
    frame = frame[~frame.index.duplicated(keep="last")].sort_index()
    return frame


def _continuous_returns(close):
    close = close.dropna().sort_index()
    returns = close.pct_change(fill_method=None)
    delta = close.index.to_series().diff()
    return returns.where(delta <= pd.Timedelta(minutes=7))


def _lag_pair(market_returns, btc_returns, lag_minutes):
    target_index = market_returns.index
    lookup_index = target_index - pd.Timedelta(minutes=lag_minutes)

    btc_lead = btc_returns.reindex(lookup_index)
    btc_lead.index = target_index

    return pd.concat(
        [
            btc_lead.rename("btc_return"),
            market_returns.rename("market_return"),
        ],
        axis=1,
    ).dropna()


def _intraday_metrics(asset_name, asset_ticker, btc_close):
    market_frame = _history(asset_ticker, INTRADAY_PERIOD, INTRADAY_INTERVAL)
    market_close = market_frame["Close"].dropna()
    market_returns = _continuous_returns(market_close)
    btc_returns = _continuous_returns(btc_close)

    lag_rows = []
    for lag in LAG_MINUTES:
        pair = _lag_pair(market_returns, btc_returns, lag)
        corr = pair["btc_return"].corr(pair["market_return"]) if len(pair) >= 20 else None
        lag_rows.append(
            {
                "asset": asset_name,
                "ticker": asset_ticker,
                "lag_minutes": lag,
                "intraday_corr": corr,
                "intraday_samples": len(pair),
            }
        )

    valid_lags = [row for row in lag_rows if _num(row["intraday_corr"]) is not None]
    best = max(valid_lags, key=lambda row: row["intraday_corr"]) if valid_lags else None

    same_time = next((row for row in lag_rows if row["lag_minutes"] == 0), None)
    same_pair = _lag_pair(market_returns, btc_returns, 0)
    drops = same_pair[same_pair["btc_return"] <= BTC_DROP_THRESHOLD_5M]
    drop_hit_rate = float((drops["market_return"] < 0).mean()) if len(drops) else None
    avg_market_on_btc_drop = float(drops["market_return"].mean()) if len(drops) else None

    return {
        "asset": asset_name,
        "ticker": asset_ticker,
        "corr_same_5m": same_time["intraday_corr"] if same_time else None,
        "samples_same_5m": same_time["intraday_samples"] if same_time else 0,
        "best_btc_lead_minutes": best["lag_minutes"] if best else None,
        "best_btc_lead_corr": best["intraday_corr"] if best else None,
        "best_btc_lead_samples": best["intraday_samples"] if best else 0,
        "btc_drop_threshold_5m": BTC_DROP_THRESHOLD_5M,
        "btc_drop_events_5m": len(drops),
        "btc_drop_hit_rate_5m": drop_hit_rate,
        "avg_market_return_on_btc_drop_5m": avg_market_on_btc_drop,
    }, lag_rows


def _btc_price_asof(btc_close, timestamp):
    if btc_close.empty:
        return None
    timestamp = pd.Timestamp(timestamp)
    if timestamp.tzinfo is None:
        timestamp = timestamp.tz_localize("UTC")
    else:
        timestamp = timestamp.tz_convert("UTC")
    if timestamp < btc_close.index.min():
        return None
    return _num(btc_close.asof(timestamp))


def _overnight_rows(asset_name, asset_ticker, btc_close):
    daily = _history(asset_ticker, "6mo", "1d")
    daily = daily[["Open", "Close"]].dropna().sort_index()
    rows = []

    for i in range(1, len(daily)):
        prev_idx = daily.index[i - 1]
        curr_idx = daily.index[i]
        prev_day = pd.Timestamp(prev_idx).tz_convert(HK_TZ).date()
        curr_day = pd.Timestamp(curr_idx).tz_convert(HK_TZ).date()

        prev_close = _num(daily.iloc[i - 1]["Close"])
        curr_open = _num(daily.iloc[i]["Open"])
        if not prev_close or not curr_open:
            continue

        btc_start_hk = pd.Timestamp(prev_day).tz_localize(HK_TZ) + pd.Timedelta(hours=16, minutes=10)
        btc_end_hk = pd.Timestamp(curr_day).tz_localize(HK_TZ) + pd.Timedelta(hours=9, minutes=30)

        btc_start = _btc_price_asof(btc_close, btc_start_hk.tz_convert("UTC"))
        btc_end = _btc_price_asof(btc_close, btc_end_hk.tz_convert("UTC"))
        if not btc_start or not btc_end:
            continue

        rows.append(
            {
                "asset": asset_name,
                "ticker": asset_ticker,
                "session_date_hk": str(curr_day),
                "btc_overnight_return": (btc_end / btc_start) - 1.0,
                "hk_open_gap": (curr_open / prev_close) - 1.0,
            }
        )

    return rows


def _overnight_metrics(rows):
    if not rows:
        return {
            "overnight_corr": None,
            "overnight_samples": 0,
            "btc_down_overnight_events": 0,
            "btc_down_gap_hit_rate": None,
            "avg_gap_when_btc_down": None,
        }

    df = pd.DataFrame(rows)
    corr = df["btc_overnight_return"].corr(df["hk_open_gap"]) if len(df) >= 8 else None
    down = df[df["btc_overnight_return"] < 0]

    return {
        "overnight_corr": corr,
        "overnight_samples": len(df),
        "btc_down_overnight_events": len(down),
        "btc_down_gap_hit_rate": float((down["hk_open_gap"] < 0).mean()) if len(down) else None,
        "avg_gap_when_btc_down": float(down["hk_open_gap"].mean()) if len(down) else None,
    }


def _append_history(summary_rows, timestamp):
    if not summary_rows:
        return
    path = DATA_DIR / "hk_btc_history.csv"
    frame = pd.DataFrame(summary_rows).copy()
    frame.insert(0, "timestamp_utc", timestamp)
    frame.to_csv(path, mode="a", header=not path.exists(), index=False)


def _write_report(summary_rows, lag_rows, overnight_rows, timestamp):
    pd.DataFrame(summary_rows).to_csv(DATA_DIR / "hk_btc_latest.csv", index=False)
    pd.DataFrame(lag_rows).to_csv(DATA_DIR / "hk_btc_lags_latest.csv", index=False)
    pd.DataFrame(overnight_rows).to_csv(DATA_DIR / "hk_btc_overnight_latest.csv", index=False)
    _append_history(summary_rows, timestamp)

    lines = [
        "# BTC ↔ Hong Kong Correlation Scanner",
        "",
        f"**Updated:** {timestamp}",
        "",
        "Purpose: test whether Bitcoin weakness is associated with Hong Kong market weakness,",
        "without mixing ordinary intraday co-movement with the overnight period when HKEX is closed.",
        "",
        "## Summary",
        "",
        "| Asset | Same 5m corr | Best BTC lead | Best corr | BTC -0.25%/5m events | HK down hit-rate | Avg HK return on BTC drop | Overnight corr | BTC-down -> negative open | Avg opening gap when BTC down |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]

    for row in summary_rows:
        best_lag = row.get("best_btc_lead_minutes")
        best_lag_text = "—" if best_lag is None else f"{int(best_lag)}m"
        lines.append(
            f"| {row['asset']} | {_fmt_corr(row.get('corr_same_5m'))} | "
            f"{best_lag_text} | {_fmt_corr(row.get('best_btc_lead_corr'))} | "
            f"{int(row.get('btc_drop_events_5m') or 0)} | "
            f"{_fmt_rate(row.get('btc_drop_hit_rate_5m'))} | "
            f"{_fmt_pct(row.get('avg_market_return_on_btc_drop_5m'))} | "
            f"{_fmt_corr(row.get('overnight_corr'))} | "
            f"{_fmt_rate(row.get('btc_down_gap_hit_rate'))} | "
            f"{_fmt_pct(row.get('avg_gap_when_btc_down'))} |"
        )

    lines += [
        "",
        "## BTC lead / lag detail",
        "",
        "0m means the same 5-minute bar. 15m means the BTC return happened 15 minutes before the Hong Kong return.",
        "",
        "| Asset | BTC lead | Correlation | Samples |",
        "|---|---:|---:|---:|",
    ]
    for row in lag_rows:
        lines.append(
            f"| {row['asset']} | {int(row['lag_minutes'])}m | "
            f"{_fmt_corr(row.get('intraday_corr'))} | {int(row.get('intraday_samples') or 0)} |"
        )

    lines += [
        "",
        "## Method",
        "",
        "- Intraday: 5-minute returns over the latest ~60 days available from Yahoo Finance.",
        "- Session gaps and the HK lunch break are excluded from the intraday return pairs.",
        "- Stress test: when BTC falls at least 0.25% in a 5-minute bar, measure how often HK is also down and the average HK return.",
        "- Overnight: BTC return from 16:10 HKT after the previous HK session to 09:30 HKT at the next continuous-session open, compared with the next HK opening gap.",
        "- Assets: Hang Seng Index, Hang Seng TECH, and Xiaomi 1810.HK.",
        "",
        "Correlation is descriptive, not proof of causality or a trade signal. The short intraday history available at 5-minute resolution can change materially as new sessions are added.",
    ]

    (REPORT_DIR / "hk_btc_latest.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def run_hk_btc_correlation(timestamp=None):
    if timestamp is None:
        timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    btc_frame = _history(BTC_TICKER, INTRADAY_PERIOD, INTRADAY_INTERVAL)
    btc_close = btc_frame["Close"].dropna()

    summary_rows = []
    lag_rows = []
    all_overnight_rows = []

    for asset_name, asset_ticker in HK_ASSETS.items():
        summary, asset_lags = _intraday_metrics(asset_name, asset_ticker, btc_close)
        overnight_rows = _overnight_rows(asset_name, asset_ticker, btc_close)
        summary.update(_overnight_metrics(overnight_rows))
        summary_rows.append(summary)
        lag_rows.extend(asset_lags)
        all_overnight_rows.extend(overnight_rows)

    _write_report(summary_rows, lag_rows, all_overnight_rows, timestamp)
    return summary_rows


if __name__ == "__main__":
    rows = run_hk_btc_correlation()
    for row in rows:
        print(
            f"{row['asset']}: same5m={_fmt_corr(row.get('corr_same_5m'))} "
            f"bestLead={row.get('best_btc_lead_minutes')}m "
            f"bestCorr={_fmt_corr(row.get('best_btc_lead_corr'))} "
            f"overnight={_fmt_corr(row.get('overnight_corr'))}"
        )
