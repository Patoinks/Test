# OKX Long / Short Fundamental Scanner

Hourly scanner restricted to public companies exposed by the **OKX EEA TradFi / Stock Perpetual API universe**.

**Last scan:** 2026-09-29 16:31 UTC  
**Availability scope:** user-confirmed OKX EEA Spot xStocks  
**OKX stock/ETF markets in configured universe:** 22  
**Public companies analysed:** 18  
**SHORT CORE:** 0  
**LONG CORE:** 0

## Our ratio

**Our ratio = Forward P/E ÷ expected EPS growth (%)**. It is PEG-like: lower can indicate more growth per unit of valuation; very high can indicate expensive valuation relative to expected growth.

### SHORT CORE

`Forward P/E > 40` + `Our ratio > 2.5` + `EPS growth < 20%`.

### LONG CORE

`Forward P/E <= 35` + `Our ratio <= 1.5` + `EPS growth >= 15%` + `Revenue growth >= 8%` + `FCF yield >= 2.5%`.

Scores are 0-100 heuristics. Revenue acceleration helps LONG and penalizes SHORT; deceleration does the opposite. Funding is not applicable to these Spot xStocks markets.

## Top SHORT candidates

| Rank | Company | OKX market | SHORT score | Signal | Our ratio | Fwd P/E | EPS +1y | Rev +1y | FCF yield | Funding ann. |
|---:|---|---|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Tesla, Inc. | `xTSLA/USDC` | **60** | **WATCH** | 6.92 | 162.6 | 23.5% | 13.8% | 0.3% | — |

## Top LONG candidates

| Rank | Company | OKX market | LONG score | Signal | Our ratio | Fwd P/E | EPS +1y | Rev +1y | FCF yield | Funding ann. |
|---:|---|---|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Coinbase Global, Inc. | `xCOIN/USDC` | **80** | **WATCH** | 0.28 | 67.0 | 239.9% | 29.5% | 5.3% | — |
| 2 | NVIDIA Corporation | `xNVDA/USDC` | **75** | **WATCH** | 0.21 | 14.7 | 68.5% | 65.9% | 0.8% | — |
| 3 | Micron Technology, Inc. | `xMU/USDC` | **75** | **WATCH** | 0.06 | 6.6 | 118.6% | 92.1% | 0.6% | — |
| 4 | Robinhood Markets, Inc. | `xHOOD/USDC` | **70** | **WATCH** | 0.98 | 33.4 | 34.1% | 27.9% | — | — |
| 5 | Marvell Technology, Inc. | `xMRVL/USDC` | **70** | **WATCH** | 0.64 | 38.8 | 60.7% | 51.3% | 1.0% | — |
| 6 | Advanced Micro Devices, Inc. | `xAMD/USDC` | **70** | **WATCH** | 0.37 | 39.3 | 105.6% | 73.2% | 0.9% | — |
| 7 | Lumentum Holdings Inc. | `xLITE/USDC` | **67** | **WATCH** | 0.47 | 28.2 | 59.6% | 52.2% | 0.3% | — |
| 8 | Cerebras Systems Inc. | `xCBRS/USDC` | **60** | **WATCH** | 0.45 | 165.5 | 371.3% | 232.7% | — | — |

## All OKX companies — our ratio + LONG/SHORT scores

| Company | OKX | Our ratio | Fwd P/E | Trail P/E | EPS +1y | Rev +1y | FCF yield | LONG | SHORT | Funding ann. |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Coinbase Global, Inc. | `COIN` | 0.28 | 67.0 | — | 239.9% | 29.5% | 5.3% | **80 WATCH** | **15** | — |
| NVIDIA Corporation | `NVDA` | 0.21 | 14.7 | 29.1 | 68.5% | 65.9% | 0.8% | **75 WATCH** | **20** | — |
| Micron Technology, Inc. | `MU` | 0.06 | 6.6 | 24.2 | 118.6% | 92.1% | 0.6% | **75 WATCH** | **20** | — |
| Marvell Technology, Inc. | `MRVL` | 0.64 | 38.8 | 87.0 | 60.7% | 51.3% | 1.0% | **70 WATCH** | **15** | — |
| Advanced Micro Devices, Inc. | `AMD` | 0.37 | 39.3 | 157.4 | 105.6% | 73.2% | 0.9% | **70 WATCH** | **15** | — |
| Robinhood Markets, Inc. | `HOOD` | 0.98 | 33.4 | 51.0 | 34.1% | 27.9% | — | **70 WATCH** | **5** | — |
| Lumentum Holdings Inc. | `LITE` | 0.47 | 28.2 | — | 59.6% | 52.2% | 0.3% | **67 WATCH** | **20** | — |
| Cerebras Systems Inc. | `CBRS` | 0.45 | 165.5 | — | 371.3% | 232.7% | — | **60 WATCH** | **25** | — |
| Tesla, Inc. | `TSLA` | 6.92 | 162.6 | 330.1 | 23.5% | 13.8% | 0.3% | **22** | **60 WATCH** | — |
| Apple Inc. | `AAPL` | 4.02 | 34.5 | 37.9 | 8.6% | 10.5% | 2.2% | **5** | **60** | — |
| Strategy Inc | `MSTR` | 0.02 | 3.1 | — | 156.0% | 2.2% | -36.9% | **50** | **20** | — |
| Intel Corporation | `INTC` | 1.58 | 56.5 | — | 35.6% | 14.2% | 0.8% | **28** | **45** | — |
| Circle Internet Group, Inc. | `CRCL` | 1.79 | 55.3 | 16.9 | 30.9% | 24.1% | 0.9% | **43** | **25** | — |
| Meta Platforms, Inc. | `META` | 2.28 | 20.6 | 27.1 | 9.0% | 20.6% | 1.2% | **17** | **40** | — |
| Alphabet Inc. | `GOOGL` | — | 22.5 | 17.1 | -27.6% | 23.3% | 0.5% | **2** | **40** | — |
| Nebius Group N.V. | `NBIS` | — | -69.0 | — | -123.5% | 270.0% | -14.7% | **0** | **40** | — |
| CoreWeave, Inc. | `CRWV` | -3.20 | -47.4 | — | 14.8% | 104.0% | -19.1% | **0** | **40** | — |
| Amazon.com, Inc. | `AMZN` | — | 23.6 | 19.9 | -18.5% | 14.4% | 0.1% | **0** | **40** | — |

## Files

- `scanner.py` — scanner and scoring logic
- `reports/latest.md` — latest full report
- `data/latest.csv` — latest machine-readable snapshot
- `data/history.csv` — hourly history of **all companies** for later backtests
- `.github/workflows/hourly-okx-scanner.yml` — hourly GitHub Action

## Data

The configured universe can be pinned to the exact OKX EEA xStocks/USDC markets confirmed in the user's app. When that allowlist is present it overrides the broader public catalogue. Yahoo Finance/yfinance supplies company valuation, cash-flow and analyst-growth estimates. ETFs can exist in the OKX universe but are excluded from the company-fundamentals ranking.

### Optional account-accurate filter

Add read-only GitHub Actions secrets `OKX_API_KEY`, `OKX_API_SECRET`, and `OKX_API_PASSPHRASE`. The scanner will then query the authenticated OKX EEA account-instruments endpoint and only score contracts available to that account. Do not grant Trade or Withdraw permission for this scanner.

This is a quantitative research screen, not an automatic trading system. It does not place orders or select leverage.
