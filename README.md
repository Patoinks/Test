# OKX Overvaluation Scanner

Hourly fundamental scanner for **OKX Europe TradFi / Stock Perpetuals**.

The project discovers live OKX stock/RWA perpetuals from the EEA public API, maps public-company underlyings to Yahoo Finance fundamentals, and ranks potential **overvaluation / short-research candidates** using the rules we defined:

- Forward P/E > 40
- Trailing P/E > 40
- PEG > 2.5
- Expected EPS growth next year < 20%
- FCF yield < 2.5%
- Expected revenue growth decelerating
- OKX perpetual funding shown separately as carry/risk context

## Signal

A **CORE** candidate must satisfy:

```
Forward P/E > 40
PEG > 2.5
Expected EPS growth (+1y) < 20%
```

The 0-100 score adds supporting evidence from trailing P/E, FCF yield and revenue deceleration.

This is a screening tool, not an automatic trading system. It never places orders.

## Outputs

Each hourly run writes:

- `reports/latest.md` — readable ranked report
- `data/latest.csv` — machine-readable snapshot
- `data/history.csv` — append-only history for future backtests

## Run locally

```bash
python -m pip install -r requirements.txt
python scanner.py
```

## Data sources

- OKX EEA public API: TradFi / Stock perpetual universe and funding
- Yahoo Finance via `yfinance`: valuation, cash flow and analyst growth estimates

## Scheduling

GitHub Actions runs the scanner every hour and commits changed reports/history back to the repository. GitHub scheduled workflows can start a few minutes late during busy periods.

## Important

Availability of a specific OKX TradFi instrument can differ by account and jurisdiction. The scanner uses the EEA public universe; always verify the instrument in your own OKX app before trading.
