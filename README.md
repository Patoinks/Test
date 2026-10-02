# OKX Long / Short Fundamental Scanner

Hourly scanner restricted to public companies exposed by the **OKX EEA TradFi / Stock Perpetual API universe**.

**Last scan:** 2026-10-02 20:48 UTC  
**Availability scope:** user-confirmed OKX EEA Spot xStocks  
**OKX stock/ETF markets in configured universe:** 22  
**Public companies analysed:** 18  
**SHORT CORE:** 1  
**LONG CORE:** 0

## Model

Profitable companies use a PEG-like valuation framework plus growth and free-cash-flow quality. Loss-making/speculative-growth companies use **P/S, EV/Sales, operating margin and FCF** as the primary valuation lens, because huge EPS-growth percentages can be distorted by a tiny or negative base. Asset-proxy companies such as MSTR are excluded from the sales-multiple model and need a separate NAV/premium framework.

### SHORT CORE

Two routes: (1) classic expensive/slow-growth companies, or (2) loss-making companies with extreme sales multiples and weak margins/cash generation. A loss-making company at >=40x P/S or EV/Sales gets a minimum short-risk score of 80.

### LONG CORE

Requires established profitability, reasonable forward valuation, strong growth and positive FCF yield. Speculative/loss-making names cannot qualify for LONG CORE from PEG alone.

Scores are 0-100 heuristics. Revenue acceleration helps LONG and penalizes SHORT; deceleration does the opposite. Funding is not applicable to these Spot xStocks markets.

## Top SHORT candidates

| Rank | Company | OKX market | SHORT score | Signal | P/S | EV/S | Op margin | Fwd P/E | Rev +1y | FCF yield |
|---:|---|---|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Cerebras Systems Inc. | `xCBRS/USDC` | **88** | **CORE** | 58.1 | 49.7 | -265.0% | 130.7 | 232.7% | — |
| 2 | Nebius Group N.V. | `xNBIS/USDC` | **80** | **WATCH** | 48.7 | 48.6 | -0.2% | -69.6 | 268.8% | -14.6% |
| 3 | Tesla, Inc. | `xTSLA/USDC` | **63** | **WATCH** | 14.1 | 13.2 | 1.4% | 171.3 | 13.7% | 0.3% |

## Top LONG candidates

| Rank | Company | OKX market | LONG score | Signal | P/S | EV/S | Op margin | Fwd P/E | Rev +1y | FCF yield |
|---:|---|---|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | NVIDIA Corporation | `xNVDA/USDC` | **75** | **WATCH** | 18.6 | 18.3 | 66.2% | 14.9 | 66.0% | 0.7% |
| 2 | Robinhood Markets, Inc. | `xHOOD/USDC` | **70** | **WATCH** | 20.6 | 20.1 | 43.9% | 32.8 | 27.8% | — |
| 3 | Marvell Technology, Inc. | `xMRVL/USDC` | **65** | **WATCH** | 25.9 | 25.0 | 16.7% | 40.3 | 51.2% | 1.0% |
| 4 | Advanced Micro Devices, Inc. | `xAMD/USDC` | **65** | **WATCH** | 25.1 | 24.1 | 17.2% | 40.7 | 73.2% | 0.9% |
| 5 | Micron Technology, Inc. | `xMU/USDC` | **62** | **WATCH** | 9.1 | 9.0 | 80.7% | 5.2 | 14.1% | 2.3% |

## All OKX companies — our ratio + LONG/SHORT scores

| Company | OKX | P/S | EV/S | Op margin | Fwd P/E | EPS +1y | Rev +1y | FCF yield | LONG | SHORT |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Cerebras Systems Inc. | `CBRS` | 58.1 | 49.7 | -265.0% | 130.7 | 371.3% | 232.7% | — | **0** | **88 CORE** |
| Nebius Group N.V. | `NBIS` | 48.7 | 48.6 | -0.2% | -69.6 | -147.8% | 268.8% | -14.6% | **0** | **80 WATCH** |
| NVIDIA Corporation | `NVDA` | 18.6 | 18.3 | 66.2% | 14.9 | 68.6% | 66.0% | 0.7% | **75 WATCH** | **18** |
| Robinhood Markets, Inc. | `HOOD` | 20.6 | 20.1 | 43.9% | 32.8 | 33.8% | 27.8% | — | **70 WATCH** | **5** |
| Marvell Technology, Inc. | `MRVL` | 25.9 | 25.0 | 16.7% | 40.3 | 60.7% | 51.2% | 1.0% | **65 WATCH** | **33** |
| Advanced Micro Devices, Inc. | `AMD` | 25.1 | 24.1 | 17.2% | 40.7 | 105.7% | 73.2% | 0.9% | **65 WATCH** | **33** |
| Tesla, Inc. | `TSLA` | 14.1 | 13.2 | 1.4% | 171.3 | 23.5% | 13.7% | 0.3% | **22** | **63 WATCH** |
| Micron Technology, Inc. | `MU` | 9.1 | 9.0 | 80.7% | 5.2 | 16.0% | 14.1% | 2.3% | **62 WATCH** | **38** |
| Lumentum Holdings Inc. | `LITE` | 32.3 | 30.8 | 28.0% | 31.3 | 59.5% | 52.8% | 0.2% | **0** | **59** |
| Apple Inc. | `AAPL` | 10.4 | 10.4 | 32.6% | 34.8 | 8.6% | 10.5% | 2.2% | **5** | **58** |
| Intel Corporation | `INTC` | 11.1 | 11.3 | 12.2% | 57.9 | 35.6% | 14.2% | 0.8% | **5** | **48** |
| Circle Internet Group, Inc. | `CRCL` | 7.6 | 6.7 | 4.9% | 54.2 | 29.3% | 23.7% | 0.9% | **43** | **23** |
| Coinbase Global, Inc. | `COIN` | 8.0 | 7.9 | -13.9% | 64.5 | 239.9% | 29.4% | 5.5% | **20** | **40** |
| CoreWeave, Inc. | `CRWV` | 6.5 | 12.5 | -1.9% | -49.6 | 15.4% | 104.1% | -18.4% | **0** | **40** |
| Meta Platforms, Inc. | `META` | 8.1 | 8.2 | 34.8% | 20.9 | 9.3% | 20.6% | 1.2% | **17** | **38** |
| Alphabet Inc. | `GOOGL` | 9.4 | 9.0 | 34.0% | 22.8 | -27.6% | 23.3% | 0.5% | **2** | **38** |
| Amazon.com, Inc. | `AMZN` | 3.5 | 3.6 | 13.7% | 24.0 | -18.4% | 14.4% | 0.1% | **0** | **38** |
| Strategy Inc | `MSTR` | 128.0 | 161.4 | -6808.1% | 3.2 | 156.0% | 2.2% | -35.4% | **25** | **25** |

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
