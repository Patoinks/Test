# OKX Long / Short Fundamental Scanner

Hourly scanner restricted to public companies exposed by the **OKX EEA TradFi / Stock Perpetual API universe**.

**Last scan:** 2026-10-03 17:20 UTC  
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

### Separate P/E trend model

This second ranking does **not replace** the main model. It compares trailing P/E with forward P/E and then checks whether expected EPS and revenue direction support the move. Falling forward P/E with positive growth raises the P/E-trend LONG score; rising forward P/E with weakening growth raises the P/E-trend SHORT score. Extreme absolute forward P/E is penalized on the LONG side.

## Combined model — LONG

Weighted score: **70% fundamental + 30% P/E trend**.

| Rank | Company | OKX | Fundamental LONG | P/E trend LONG | Combined | Signal |
|---:|---|---|---:|---:|---:|---|
| 1 | NVIDIA Corporation | `NVDA` | 75 | 90 | **80** | **CORE** |
| 2 | Marvell Technology, Inc. | `MRVL` | 65 | 100 | **76** | **CORE** |
| 3 | Advanced Micro Devices, Inc. | `AMD` | 65 | 100 | **76** | **CORE** |
| 4 | Robinhood Markets, Inc. | `HOOD` | 70 | 86 | **75** | **CORE** |
| 5 | Micron Technology, Inc. | `MU` | 62 | 75 | **66** | **WATCH** |

## Combined model — SHORT

Weighted score: **70% fundamental + 30% P/E trend**.

| Rank | Company | OKX | Fundamental SHORT | P/E trend SHORT | Combined | Signal |
|---:|---|---|---:|---:|---:|---|
| 1 | Cerebras Systems Inc. | `CBRS` | 88 | 0 | **88** | **CORE** |
| 2 | Nebius Group N.V. | `NBIS` | 80 | 0 | **80** | **WATCH** |

## P/E Compression + Growth — LONG

| Rank | Company | OKX | Trail P/E | Fwd P/E | P/E change | EPS +1y | Rev +1y | Rev trend | LONG score | Signal |
|---:|---|---|---:|---:|---:|---:|---:|---|---:|---|
| 1 | Marvell Technology, Inc. | `MRVL` | 88.4 | 40.3 | -54.4% | 60.3% | 50.9% | accelerating | **100** | **CORE** |
| 2 | Advanced Micro Devices, Inc. | `AMD` | 156.1 | 40.7 | -73.9% | 105.7% | 73.2% | accelerating | **100** | **CORE** |
| 3 | NVIDIA Corporation | `NVDA` | 29.6 | 14.9 | -49.6% | 68.6% | 66.0% | decelerating | **90** | **CORE** |
| 4 | Robinhood Markets, Inc. | `HOOD` | 50.1 | 32.8 | -34.5% | 33.8% | 27.8% | accelerating | **86** | **CORE** |
| 5 | Micron Technology, Inc. | `MU` | 14.5 | 5.2 | -63.7% | 16.0% | 14.1% | decelerating | **75** | **CORE** |
| 6 | Tesla, Inc. | `TSLA` | 346.3 | 171.4 | -50.5% | 23.4% | 13.7% | accelerating | **55** | **WATCH** |
| 7 | Meta Platforms, Inc. | `META` | 27.3 | 20.9 | -23.7% | 9.3% | 20.6% | decelerating | **51** | **WATCH** |

## P/E Expansion + Weakening — SHORT

| Rank | Company | OKX | Trail P/E | Fwd P/E | P/E change | EPS +1y | Rev +1y | Rev trend | SHORT score | Signal |
|---:|---|---|---:|---:|---:|---:|---:|---|---:|---|
| 1 | Alphabet Inc. | `GOOGL` | 17.2 | 22.8 | 32.2% | -27.6% | 23.3% | decelerating | **70** | **CORE** |
| 2 | Amazon.com, Inc. | `AMZN` | 20.0 | 24.0 | 20.3% | -18.4% | 14.4% | decelerating | **60** | **WATCH** |
| 3 | Circle Internet Group, Inc. | `CRCL` | 16.6 | 54.2 | 226.8% | 29.3% | 23.7% | accelerating | **50** | **WATCH** |

## Top SHORT candidates

| Rank | Company | OKX market | SHORT score | Signal | P/S | EV/S | Op margin | Fwd P/E | Rev +1y | FCF yield |
|---:|---|---|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Cerebras Systems Inc. | `xCBRS/USDC` | **88** | **CORE** | 58.1 | 48.6 | -265.0% | 130.7 | 232.7% | — |
| 2 | Nebius Group N.V. | `xNBIS/USDC` | **80** | **WATCH** | 45.5 | 50.7 | -0.2% | -69.6 | 268.8% | -15.6% |
| 3 | Tesla, Inc. | `xTSLA/USDC` | **63** | **WATCH** | 14.1 | 13.9 | 1.4% | 171.4 | 13.7% | 0.3% |

## Top LONG candidates

| Rank | Company | OKX market | LONG score | Signal | P/S | EV/S | Op margin | Fwd P/E | Rev +1y | FCF yield |
|---:|---|---|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | NVIDIA Corporation | `xNVDA/USDC` | **75** | **WATCH** | 18.6 | 18.5 | 66.2% | 14.9 | 66.0% | 0.7% |
| 2 | Robinhood Markets, Inc. | `xHOOD/USDC` | **70** | **WATCH** | 20.6 | 20.4 | 43.9% | 32.8 | 27.8% | — |
| 3 | Marvell Technology, Inc. | `xMRVL/USDC` | **65** | **WATCH** | 25.9 | 25.4 | 16.7% | 40.3 | 50.9% | 1.0% |
| 4 | Advanced Micro Devices, Inc. | `xAMD/USDC` | **65** | **WATCH** | 25.1 | 24.8 | 17.2% | 40.7 | 73.2% | 0.9% |
| 5 | Micron Technology, Inc. | `xMU/USDC` | **62** | **WATCH** | 9.1 | 8.8 | 80.7% | 5.2 | 14.1% | 2.4% |

## All OKX companies — our ratio + LONG/SHORT scores

| Company | OKX | P/S | EV/S | Op margin | Fwd P/E | EPS +1y | Rev +1y | FCF yield | LONG | SHORT |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Cerebras Systems Inc. | `CBRS` | 58.1 | 48.6 | -265.0% | 130.7 | 371.3% | 232.7% | — | **0** | **88 CORE** |
| Nebius Group N.V. | `NBIS` | 45.5 | 50.7 | -0.2% | -69.6 | -147.8% | 268.8% | -15.6% | **0** | **80 WATCH** |
| NVIDIA Corporation | `NVDA` | 18.6 | 18.5 | 66.2% | 14.9 | 68.6% | 66.0% | 0.7% | **75 WATCH** | **18** |
| Robinhood Markets, Inc. | `HOOD` | 20.6 | 20.4 | 43.9% | 32.8 | 33.8% | 27.8% | — | **70 WATCH** | **5** |
| Marvell Technology, Inc. | `MRVL` | 25.9 | 25.4 | 16.7% | 40.3 | 60.3% | 50.9% | 1.0% | **65 WATCH** | **33** |
| Advanced Micro Devices, Inc. | `AMD` | 25.1 | 24.8 | 17.2% | 40.7 | 105.7% | 73.2% | 0.9% | **65 WATCH** | **33** |
| Tesla, Inc. | `TSLA` | 14.1 | 13.9 | 1.4% | 171.4 | 23.4% | 13.7% | 0.3% | **22** | **63 WATCH** |
| Micron Technology, Inc. | `MU` | 9.1 | 8.8 | 80.7% | 5.2 | 16.0% | 14.1% | 2.4% | **62 WATCH** | **38** |
| Lumentum Holdings Inc. | `LITE` | 32.3 | 31.9 | 28.0% | 31.3 | 59.5% | 52.8% | 0.2% | **0** | **59** |
| Apple Inc. | `AAPL` | 10.4 | 10.5 | 32.6% | 34.8 | 8.6% | 10.5% | 2.2% | **5** | **58** |
| Intel Corporation | `INTC` | 11.1 | 11.2 | 12.2% | 57.9 | 35.6% | 14.2% | 0.8% | **5** | **48** |
| Circle Internet Group, Inc. | `CRCL` | 7.6 | 6.5 | 4.9% | 54.2 | 29.3% | 23.7% | 0.9% | **43** | **23** |
| Coinbase Global, Inc. | `COIN` | 8.0 | 7.6 | -13.9% | 64.7 | 245.0% | 29.3% | 5.5% | **20** | **40** |
| CoreWeave, Inc. | `CRWV` | 6.5 | 12.6 | -1.9% | -49.6 | 15.4% | 104.1% | -18.4% | **0** | **40** |
| Meta Platforms, Inc. | `META` | 8.1 | 8.2 | 34.8% | 20.9 | 9.3% | 20.6% | 1.2% | **17** | **38** |
| Alphabet Inc. | `GOOGL` | 9.4 | 9.2 | 34.0% | 22.8 | -27.6% | 23.3% | 0.5% | **2** | **38** |
| Amazon.com, Inc. | `AMZN` | 3.5 | 3.7 | 13.7% | 24.0 | -18.4% | 14.4% | 0.1% | **0** | **38** |
| Strategy Inc | `MSTR` | 128.0 | 161.0 | -6808.1% | 3.2 | 157.5% | 2.2% | -35.4% | **25** | **25** |

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
