# OKX Long / Short Fundamental Scanner

Hourly scanner restricted to public companies exposed by the **OKX EEA TradFi / Stock Perpetual API universe**.

**Last scan:** 2026-10-08 16:35 UTC  
**Availability scope:** user-confirmed OKX EEA Stock Futures / X-Perp  
**OKX stock/ETF markets in configured universe:** 72  
**Public companies analysed:** 55  
**SHORT CORE:** 6  
**LONG CORE:** 3

## Model

Profitable companies use a PEG-like valuation framework plus growth and free-cash-flow quality. Loss-making/speculative-growth companies use **P/S, EV/Sales, operating margin and FCF** as the primary valuation lens, because huge EPS-growth percentages can be distorted by a tiny or negative base. Asset-proxy companies such as MSTR are excluded from the sales-multiple model and need a separate NAV/premium framework.

### SHORT CORE

Two routes: (1) classic expensive/slow-growth companies, or (2) loss-making companies with extreme sales multiples and weak margins/cash generation. A loss-making company at >=40x P/S or EV/Sales gets a minimum short-risk score of 80.

### LONG CORE

Requires established profitability, reasonable forward valuation, strong growth and positive FCF yield. Speculative/loss-making names cannot qualify for LONG CORE from PEG alone.

Scores are 0-100 heuristics. Revenue acceleration helps LONG and penalizes SHORT; deceleration does the opposite. Funding is not applicable to these Spot xStocks markets.

### Separate P/E trend model

This second ranking does **not replace** the main model. It compares trailing P/E with forward P/E and then checks whether expected EPS and revenue direction support the move. Falling forward P/E with positive growth raises the P/E-trend LONG score; rising forward P/E with weakening growth raises the P/E-trend SHORT score. Extreme absolute forward P/E is penalized on the LONG side.

### Price Timing / Dislocation layer

The final ranking adds entry timing without allowing price momentum to create a thesis by itself. Price move = **50% 24h return + 50% 7-day return**. A 25% absolute weighted move is maximum timing stress and can adjust the final score by up to 20 points. If a name is already LONG-qualified now or was LONG-qualified in the previous hourly run, a fall boosts LONG and a rally reduces it. If it is already SHORT-qualified, a rally boosts SHORT and a fall reduces it.

## Final model + Price Timing — LONG

| Rank | Company | OKX | 24h | 7d | 50/50 move | Base LONG | Timing adj. | Final | Signal | Prev. LONG? |
|---:|---|---|---:|---:|---:|---:|---:|---:|---|---|
| 1 | Applovin Corporation | APP | -1.7% | -1.7% | -1.7% | 82 | +1 | **83** | **CORE** | yes |
| 2 | NVIDIA Corporation | NVDA | -0.8% | 2.0% | 0.6% | 82 | +0 | **82** | **CORE** | yes |
| 3 | Taiwan Semiconductor Manufactur | TSM | -1.6% | 1.1% | -0.3% | 82 | +0 | **82** | **CORE** | yes |
| 4 | Applied Materials, Inc. | AMAT | 0.4% | -1.3% | -0.5% | 81 | +0 | **81** | **CORE** | yes |
| 5 | Sandisk Corporation | SNDK | -2.8% | -8.0% | -5.4% | 77 | +4 | **81** | **CORE** | yes |
| 6 | Western Digital Corporation | WDC | -1.3% | -13.5% | -7.4% | 74 | +6 | **80** | **CORE** | yes |
| 7 | Broadcom Inc. | AVGO | -1.0% | 8.4% | 3.7% | 82 | -3 | **79** | **CORE** | yes |
| 8 | Marvell Technology, Inc. | MRVL | -2.5% | 3.6% | 0.6% | 79 | +0 | **79** | **CORE** | yes |
| 9 | Oracle Corporation | ORCL | -0.9% | 3.0% | 1.0% | 78 | -1 | **77** | **CORE** | yes |
| 10 | Robinhood Markets, Inc. | HOOD | -1.4% | -2.8% | -2.1% | 75 | +2 | **77** | **CORE** | yes |

## Final model + Price Timing — SHORT

| Rank | Company | OKX | 24h | 7d | 50/50 move | Base SHORT | Timing adj. | Final | Signal | Prev. SHORT? |
|---:|---|---|---:|---:|---:|---:|---:|---:|---|---|
| 1 | Cerebras Systems Inc. | CBRS | -3.2% | -0.0% | -1.6% | 100 | -1 | **99** | **CORE** | yes |
| 2 | Rocket Lab Corporation | RKLB | -4.0% | -2.0% | -3.0% | 100 | -2 | **98** | **CORE** | yes |
| 3 | USA Rare Earth, Inc. | USAR | -4.5% | -8.4% | -6.4% | 100 | -5 | **95** | **CORE** | yes |
| 4 | Nebius Group N.V. | NBIS | -3.6% | -1.5% | -2.5% | 90 | -2 | **88** | **CORE** | yes |
| 5 | IonQ, Inc. | IONQ | -3.1% | -8.9% | -6.0% | 91 | -5 | **86** | **CORE** | yes |
| 6 | AST SpaceMobile, Inc. | ASTS | -6.8% | -0.9% | -3.8% | 80 | -3 | **77** | **CORE** | yes |
| 7 | Moderna, Inc. | MRNA | -0.1% | 3.9% | 1.9% | 72 | +2 | **74** | **WATCH** | yes |
| 8 | Lumentum Holdings Inc. | LITE | -3.3% | 2.7% | -0.3% | 67 | +0 | **67** | **WATCH** | yes |
| 9 | Okta, Inc. | OKTA | 1.9% | 4.5% | 3.2% | 61 | +3 | **64** | **WATCH** | yes |
| 10 | IREN LIMITED | IREN | -6.3% | -10.9% | -8.6% | 68 | -7 | **61** | **WATCH** | yes |

## Combined model — LONG

Weighted score: **70% fundamental + 30% P/E trend**.

| Rank | Company | OKX | Fundamental LONG | P/E trend LONG | Combined | Signal |
|---:|---|---|---:|---:|---:|---|
| 1 | Applovin Corporation | `APP` | 83 | 80 | **82** | **CORE** |
| 2 | Taiwan Semiconductor Manufactur | `TSM` | 82 | 81 | **82** | **CORE** |
| 3 | NVIDIA Corporation | `NVDA` | 75 | 100 | **82** | **CORE** |
| 4 | Broadcom Inc. | `AVGO` | 75 | 100 | **82** | **CORE** |
| 5 | Applied Materials, Inc. | `AMAT` | 77 | 91 | **81** | **CORE** |
| 6 | Marvell Technology, Inc. | `MRVL` | 70 | 100 | **79** | **CORE** |
| 7 | Oracle Corporation | `ORCL` | 70 | 95 | **78** | **CORE** |
| 8 | Sandisk Corporation | `SNDK` | 75 | 82 | **77** | **CORE** |
| 9 | Credo Technology Group Holding  | `CRDO` | 67 | 96 | **76** | **CORE** |
| 10 | Advanced Micro Devices, Inc. | `AMD` | 65 | 100 | **76** | **CORE** |

## Combined model — SHORT

Weighted score: **70% fundamental + 30% P/E trend**.

| Rank | Company | OKX | Fundamental SHORT | P/E trend SHORT | Combined | Signal |
|---:|---|---|---:|---:|---:|---|
| 1 | Cerebras Systems Inc. | `CBRS` | 100 | 0 | **100** | **CORE** |
| 2 | Rocket Lab Corporation | `RKLB` | 100 | 0 | **100** | **CORE** |
| 3 | USA Rare Earth, Inc. | `USAR` | 100 | 0 | **100** | **CORE** |
| 4 | IonQ, Inc. | `IONQ` | 91 | 0 | **91** | **CORE** |
| 5 | Nebius Group N.V. | `NBIS` | 90 | 0 | **90** | **CORE** |
| 6 | AST SpaceMobile, Inc. | `ASTS` | 80 | 0 | **80** | **WATCH** |
| 7 | Moderna, Inc. | `MRNA` | 72 | 0 | **72** | **WATCH** |
| 8 | IREN LIMITED | `IREN` | 68 | 0 | **68** | **WATCH** |
| 9 | Lumentum Holdings Inc. | `LITE` | 67 | 0 | **67** | **WATCH** |
| 10 | Okta, Inc. | `OKTA` | 80 | 18 | **61** | **WATCH** |

## P/E Compression + Growth — LONG

| Rank | Company | OKX | Trail P/E | Fwd P/E | P/E change | EPS +1y | Rev +1y | Rev trend | LONG score | Signal |
|---:|---|---|---:|---:|---:|---:|---:|---|---:|---|
| 1 | NVIDIA Corporation | `NVDA` | 29.8 | 14.8 | -50.3% | 70.9% | 68.2% | decelerating | **100** | **CORE** |
| 2 | Broadcom Inc. | `AVGO` | 47.6 | 19.2 | -59.6% | 66.4% | 64.1% | decelerating | **100** | **CORE** |
| 3 | Marvell Technology, Inc. | `MRVL` | 91.3 | 38.1 | -58.3% | 72.6% | 63.1% | accelerating | **100** | **CORE** |
| 4 | Advanced Micro Devices, Inc. | `AMD` | 161.7 | 40.3 | -75.1% | 107.2% | 74.6% | accelerating | **100** | **CORE** |
| 5 | Credo Technology Group Holding  | `CRDO` | 78.1 | 22.7 | -70.9% | 53.7% | 54.8% | decelerating | **96** | **CORE** |
| 6 | AXT Inc | `AXT` | 1864.5 | 33.1 | -98.2% | 159.2% | 111.3% | decelerating | **96** | **CORE** |
| 7 | Oracle Corporation | `ORCL` | 22.3 | 12.9 | -42.0% | 35.1% | 45.6% | accelerating | **95** | **CORE** |
| 8 | Corning Incorporated | `GLW` | 72.6 | 36.2 | -50.1% | 33.0% | 19.3% | accelerating | **92** | **CORE** |
| 9 | Applied Materials, Inc. | `AMAT` | 45.1 | 28.3 | -37.3% | 44.4% | 34.8% | accelerating | **91** | **CORE** |
| 10 | Coherent Corp. | `COHR` | 77.0 | 22.6 | -70.7% | 49.1% | 38.8% | decelerating | **91** | **CORE** |

## P/E Expansion + Weakening — SHORT

| Rank | Company | OKX | Trail P/E | Fwd P/E | P/E change | EPS +1y | Rev +1y | Rev trend | SHORT score | Signal |
|---:|---|---|---:|---:|---:|---:|---:|---|---:|---|
| 1 | SOFTBANK GROUP CORP | `SOFTBANK` | 6.9 | 20.5 | 195.5% | -14.5% | 6.9% | decelerating | **86** | **CORE** |
| 2 | Alphabet Inc. | `GOOGL` | 17.5 | 23.2 | 32.2% | -27.6% | 23.3% | decelerating | **70** | **CORE** |
| 3 | Hyperliquid Strategies Inc | `PURR` | 3.4 | 29.9 | 767.6% | 51.0% | 31.4% | decelerating | **55** | **WATCH** |
| 4 | Amazon.com, Inc. | `AMZN` | 20.8 | 24.7 | 18.8% | -18.4% | 14.5% | decelerating | **52** | **WATCH** |

## Top SHORT candidates

| Rank | Company | OKX market | SHORT score | Signal | P/S | EV/S | Op margin | Fwd P/E | Rev +1y | FCF yield |
|---:|---|---|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Rocket Lab Corporation | `RKLB-USDT-SWAP` | **100** | **CORE** | 57.4 | 53.1 | -24.6% | 1279.1 | 41.6% | -0.6% |
| 2 | USA Rare Earth, Inc. | `USAR-USDT-SWAP` | **100** | **CORE** | 360.2 | 130.7 | -795.6% | 421.3 | 870.1% | -6.0% |
| 3 | Cerebras Systems Inc. | `CBRS-USDT-SWAP` | **100** | **CORE** | 59.2 | 51.6 | -265.0% | 133.1 | 232.7% | — |
| 4 | IonQ, Inc. | `IONQ-USDT-SWAP` | **91** | **CORE** | 65.9 | 55.6 | -408.2% | -31.0 | 79.0% | -0.5% |
| 5 | Nebius Group N.V. | `NBIS-USDT-SWAP` | **90** | **CORE** | 45.9 | 49.6 | -0.2% | -65.5 | 268.8% | -15.5% |
| 6 | Okta, Inc. | `OKTA-USDT-SWAP` | **80** | **CORE** | 12.6 | 11.7 | 13.3% | 50.7 | 10.0% | 2.7% |
| 7 | AST SpaceMobile, Inc. | `ASTS-USDT-SWAP` | **80** | **WATCH** | 190.9 | 168.2 | -544.6% | -44.0 | 259.9% | -8.2% |
| 8 | Moderna, Inc. | `MRNA-USDT-SWAP` | **72** | **WATCH** | 35.2 | 33.5 | -557.9% | -44.1 | 15.8% | 0.4% |
| 9 | IREN LIMITED | `IREN-USDT-SWAP` | **68** | **WATCH** | 20.2 | 24.3 | -102.5% | -9.1 | 160.9% | -29.5% |
| 10 | Lumentum Holdings Inc. | `LITE-USDT-SWAP` | **67** | **WATCH** | 32.3 | 32.7 | 28.0% | 30.2 | 55.5% | 0.2% |

## Top LONG candidates

| Rank | Company | OKX market | LONG score | Signal | P/S | EV/S | Op margin | Fwd P/E | Rev +1y | FCF yield |
|---:|---|---|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Applovin Corporation | `APP-USDT-SWAP` | **83** | **CORE** | 13.6 | 13.9 | 77.7% | 13.2 | 26.4% | 3.4% |
| 2 | Taiwan Semiconductor Manufactur | `TSM-USDT-SWAP` | **82** | **CORE** | 0.5 | 3.9 | 60.3% | 21.2 | 35.3% | 30.3% |
| 3 | Applied Materials, Inc. | `AMAT-USDT-SWAP` | **77** | **WATCH** | 13.4 | 13.3 | 33.7% | 28.3 | 34.8% | 0.7% |
| 4 | Broadcom Inc. | `AVGO-USDT-SWAP` | **75** | **WATCH** | 20.0 | 20.6 | 54.3% | 19.2 | 64.1% | 1.7% |
| 5 | Sandisk Corporation | `SNDK-USDT-SWAP` | **75** | **CORE** | 11.7 | 12.0 | 78.5% | 6.2 | 18.8% | 3.2% |
| 6 | Western Digital Corporation | `WDC-USDT-SWAP` | **75** | **WATCH** | 11.6 | 11.3 | 43.6% | 12.6 | 36.9% | 1.5% |
| 7 | NVIDIA Corporation | `NVDA-USDT-SWAP` | **75** | **WATCH** | 18.8 | 18.8 | 66.2% | 14.8 | 68.2% | 0.7% |
| 8 | Robinhood Markets, Inc. | `HOOD-USDT-SWAP` | **70** | **WATCH** | 19.7 | 19.8 | 43.9% | 31.4 | 28.6% | — |
| 9 | Marvell Technology, Inc. | `MRVL-USDT-SWAP` | **70** | **WATCH** | 26.4 | 26.6 | 16.7% | 38.1 | 63.1% | 1.0% |
| 10 | XIAOMI-W | `XIAOMI-USDT-SWAP` | **70** | **WATCH** | 1.4 | 1.2 | 4.0% | 15.4 | 22.6% | -1.4% |

## Analyst consensus (12-month price target) — most upside

| Rank | Company | OKX | Price | Analyst mean target | Gap | Analysts | Currency |
|---:|---|---|---:|---:|---:|---:|---|
| 1 | USA Rare Earth, Inc. | `USAR` | 12.64 | 35.56 | **181.3%** | 9 | USD |
| 2 | IREN LIMITED | `IREN` | 36.23 | 78.14 | **115.6%** | 18 | USD |
| 3 | Hyperliquid Strategies Inc | `PURR` | 11.06 | 22.32 | **101.9%** | 4 | USD |
| 4 | BitMine Immersion Technologies, | `BMNR` | 23.57 | 45.87 | **94.6%** | 3 | USD |
| 5 | SK hynix | `SKHYNIX` | 1681000.00 | 3141024.80 | **86.9%** | 38 | KRW |
| 6 | SamsungElec | `SAMSUNG` | 262000.00 | 478627.88 | **82.7%** | 36 | KRW |
| 7 | Applovin Corporation | `APP` | 276.61 | 495.72 | **79.2%** | 31 | USD |
| 8 | Cerebras Systems Inc. | `CBRS` | 169.50 | 291.64 | **72.1%** | 11 | USD |
| 9 | Western Digital Corporation | `WDC` | 399.95 | 673.50 | **68.4%** | 24 | USD |
| 10 | CoreWeave, Inc. | `CRWV` | 84.29 | 141.47 | **67.8%** | 38 | USD |
| 11 | Oracle Corporation | `ORCL` | 142.20 | 237.97 | **67.4%** | 41 | USD |
| 12 | IonQ, Inc. | `IONQ` | 40.07 | 66.63 | **66.3%** | 14 | USD |
| 13 | Rocket Lab Corporation | `RKLB` | 69.06 | 109.15 | **58.1%** | 20 | USD |
| 14 | Strategy Inc | `MSTR` | 150.28 | 236.80 | **57.6%** | 15 | USD |
| 15 | XIAOMI-W | `XIAOMI` | 23.66 | 34.63 | **46.4%** | 28 | HKD |

## Analyst consensus (12-month price target) — most downside

| Rank | Company | OKX | Price | Analyst mean target | Gap | Analysts | Currency |
|---:|---|---|---:|---:|---:|---:|---|
| 1 | Moderna, Inc. | `MRNA` | 196.31 | 121.00 | **-38.4%** | 18 | USD |
| 2 | Okta, Inc. | `OKTA` | 222.10 | 212.25 | **-4.4%** | 43 | USD |
| 3 | Apple Inc. | `AAPL` | 338.12 | 328.09 | **-3.0%** | 39 | USD |
| 4 | Super Micro Computer, Inc. | `SMCI` | 43.03 | 41.87 | **-2.7%** | 15 | USD |

Price/target uses the underlying Yahoo Finance share quote, not the OKX derivative. Minimum 3 analysts; unreliable price scales and missing coverage excluded. Targets are analyst opinions, not guaranteed forecasts.

## All OKX companies — our ratio + LONG/SHORT scores

| Company | OKX | P/S | EV/S | Op margin | Fwd P/E | EPS +1y | Rev +1y | FCF yield | LONG | SHORT |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Cerebras Systems Inc. | `CBRS` | 59.2 | 51.6 | -265.0% | 133.1 | 371.3% | 232.7% | — | **0** | **100 CORE** |
| Rocket Lab Corporation | `RKLB` | 57.4 | 53.1 | -24.6% | 1279.1 | 68.1% | 41.6% | -0.6% | **0** | **100 CORE** |
| USA Rare Earth, Inc. | `USAR` | 360.2 | 130.7 | -795.6% | 421.3 | 105.3% | 870.1% | -6.0% | **0** | **100 CORE** |
| IonQ, Inc. | `IONQ` | 65.9 | 55.6 | -408.2% | -31.0 | 18.1% | 79.0% | -0.5% | **0** | **91 CORE** |
| Nebius Group N.V. | `NBIS` | 45.9 | 49.6 | -0.2% | -65.5 | -147.8% | 268.8% | -15.5% | **0** | **90 CORE** |
| Applovin Corporation | `APP` | 13.6 | 13.9 | 77.7% | 13.2 | 27.6% | 26.4% | 3.4% | **83 CORE** | **10** |
| Taiwan Semiconductor Manufactur | `TSM` | 0.5 | 3.9 | 60.3% | 21.2 | 30.0% | 35.3% | 30.3% | **82 CORE** | **10** |
| Okta, Inc. | `OKTA` | 12.6 | 11.7 | 13.3% | 50.7 | 11.4% | 10.0% | 2.7% | **8** | **80 CORE** |
| AST SpaceMobile, Inc. | `ASTS` | 190.9 | 168.2 | -544.6% | -44.0 | 47.7% | 259.9% | -8.2% | **0** | **80 WATCH** |
| Applied Materials, Inc. | `AMAT` | 13.4 | 13.3 | 33.7% | 28.3 | 44.4% | 34.8% | 0.7% | **77 WATCH** | **13** |
| NVIDIA Corporation | `NVDA` | 18.8 | 18.8 | 66.2% | 14.8 | 70.9% | 68.2% | 0.7% | **75 WATCH** | **18** |
| Sandisk Corporation | `SNDK` | 11.7 | 12.0 | 78.5% | 6.2 | 23.7% | 18.8% | 3.2% | **75 CORE** | **10** |
| Western Digital Corporation | `WDC` | 11.6 | 11.3 | 43.6% | 12.6 | 58.2% | 36.9% | 1.5% | **75 WATCH** | **18** |
| Broadcom Inc. | `AVGO` | 20.0 | 20.6 | 54.3% | 19.2 | 66.4% | 64.1% | 1.7% | **75 WATCH** | **28** |
| Moderna, Inc. | `MRNA` | 35.2 | 33.5 | -557.9% | -44.1 | 42.9% | 15.8% | 0.4% | **0** | **72 WATCH** |
| Marvell Technology, Inc. | `MRVL` | 26.4 | 26.6 | 16.7% | 38.1 | 72.6% | 63.1% | 1.0% | **70 WATCH** | **13** |
| Robinhood Markets, Inc. | `HOOD` | 19.7 | 19.8 | 43.9% | 31.4 | 35.3% | 28.6% | — | **70 WATCH** | **5** |
| Oracle Corporation | `ORCL` | 6.0 | 8.0 | 35.6% | 12.9 | 35.1% | 45.6% | -10.6% | **70 WATCH** | **10** |
| XIAOMI-W | `XIAOMI` | 1.4 | 1.2 | 4.0% | 15.4 | 39.6% | 22.6% | -1.4% | **70 WATCH** | **10** |
| IREN LIMITED | `IREN` | 20.2 | 24.3 | -102.5% | -9.1 | -16.4% | 160.9% | -29.5% | **0** | **68 WATCH** |
| Credo Technology Group Holding  | `CRDO` | 26.0 | 25.5 | 25.2% | 22.7 | 53.7% | 54.8% | 0.6% | **67 WATCH** | **28** |
| Micron Technology, Inc. | `MU` | 9.1 | 8.9 | 80.7% | 5.2 | 17.1% | 16.0% | 2.4% | **67 WATCH** | **38** |
| Lumentum Holdings Inc. | `LITE` | 32.3 | 32.7 | 28.0% | 30.2 | 63.3% | 55.5% | 0.2% | **0** | **67 WATCH** |
| Advanced Micro Devices, Inc. | `AMD` | 25.0 | 25.3 | 17.2% | 40.3 | 107.2% | 74.6% | 0.9% | **65 WATCH** | **33** |
| Adobe Inc. | `ADBE` | 3.5 | 3.5 | 34.8% | 8.5 | 13.0% | 9.2% | 10.2% | **65 WATCH** | **30** |
| Tesla, Inc. | `TSLA` | 14.2 | 14.1 | 1.4% | 173.9 | 23.2% | 13.4% | 0.3% | **22** | **63 WATCH** |
| Corning Incorporated | `GLW` | 8.0 | 8.7 | 15.6% | 36.2 | 33.0% | 19.3% | 0.5% | **60 WATCH** | **13** |
| Microsoft Corporation | `MSFT` | 11.9 | 12.0 | 45.1% | 22.4 | 19.8% | 19.6% | 0.4% | **59 WATCH** | **23** |
| Dell Technologies Inc. | `DELL` | 2.4 | 2.6 | 12.0% | 20.0 | 0.8% | 16.5% | 1.6% | **25** | **58** |
| Coca-Cola Company (The) | `KO` | 7.5 | 8.0 | 34.9% | 24.7 | 6.8% | 0.2% | 1.4% | **7** | **58** |
| Apple Inc. | `AAPL` | 10.6 | 10.6 | 32.6% | 35.3 | 8.6% | 10.5% | 2.2% | **5** | **58** |
| Bloom Energy Corporation | `BE` | 26.2 | 27.6 | 17.1% | 56.1 | 82.6% | 65.0% | 0.7% | **55 WATCH** | **48** |
| Coherent Corp. | `COHR` | 8.7 | 9.5 | 11.8% | 22.6 | 49.1% | 38.8% | -1.0% | **52** | **35** |
| Super Micro Computer, Inc. | `SMCI` | 0.7 | 0.9 | 13.4% | 8.1 | 22.8% | 17.3% | -29.2% | **52** | **25** |
| Netflix, Inc. | `NFLX` | 6.1 | 6.2 | 33.4% | 18.7 | 6.1% | 11.2% | 8.6% | **35** | **50** |
| Palantir Technologies Inc. | `PLTR` | 77.3 | 74.3 | 47.1% | 84.4 | 44.7% | 49.7% | 0.5% | **33** | **48** |
| Intel Corporation | `INTC` | 10.2 | 10.6 | 12.2% | 52.6 | 36.9% | 14.8% | 0.8% | **5** | **48** |
| AXT Inc | `AXT` | 39.0 | 38.8 | 21.9% | 33.1 | 159.2% | 111.3% | -0.9% | **45** | **35** |
| SK hynix | `SKHYNIX` | 6.3 | 6.0 | 76.3% | 3.6 | 32.4% | 54.4% | 4.7% | **45** | **5** |
| SK hynix | `SKHY` | 6.3 | 6.0 | 76.3% | 3.6 | 32.4% | 54.4% | 4.7% | **45** | **5** |
| SamsungElec | `SAMSUNG` | 3.5 | 3.2 | 52.2% | 3.7 | 50.0% | 37.5% | 4.0% | **45** | **10** |
| Applied Optoelectronics, Inc. | `AAOI` | 16.1 | 17.1 | -12.9% | 24.5 | 576.8% | 156.5% | -9.3% | **0** | **45** |
| Circle Internet Group, Inc. | `CRCL` | 7.0 | 6.5 | 4.9% | 56.6 | 30.6% | 24.7% | 1.0% | **43** | **33** |
| Coinbase Global, Inc. | `COIN` | 7.6 | 7.4 | -13.9% | 61.4 | 267.7% | 29.9% | 5.8% | **20** | **40** |
| SOFTBANK GROUP CORP | `SOFTBANK` | 4.3 | 7.7 | -11.6% | 20.5 | -14.5% | 6.9% | -6.3% | **0** | **40** |
| CoreWeave, Inc. | `CRWV` | 6.1 | 12.5 | -1.9% | -46.5 | 15.4% | 104.3% | -19.6% | **0** | **40** |
| Meta Platforms, Inc. | `META` | 8.0 | 8.1 | 34.8% | 20.8 | 9.8% | 20.6% | 1.2% | **17** | **38** |
| Alphabet Inc. | `GOOGL` | 9.6 | 9.4 | 34.0% | 23.2 | -27.6% | 23.3% | 0.5% | **2** | **38** |
| Amazon.com, Inc. | `AMZN` | 3.6 | 3.8 | 13.7% | 24.7 | -18.4% | 14.5% | 0.1% | **0** | **38** |
| Arm Holdings plc | `ARM` | 58.3 | 60.3 | 7.6% | 91.9 | 37.5% | 36.2% | 0.4% | **35** | **33** |
| Fluence Energy, Inc. | `FLNC` | 0.5 | 0.5 | -8.9% | -27.5 | 70.1% | 35.3% | 0.2% | **5** | **28** |
| Hyperliquid Strategies Inc | `PURR` | 325.3 | 230.7 | 9595.1% | 29.9 | 51.0% | 31.4% | — | **25** | **10** |
| BitMine Immersion Technologies, | `BMNR` | 232.3 | 237.6 | 8.4% | 25.1 | 103.2% | 421.8% | -3.6% | **25** | **25** |
| Strategy Inc | `MSTR` | 120.2 | 155.9 | -6808.1% | 3.0 | 157.5% | 2.2% | -37.7% | **25** | **25** |
| QUALCOMM Incorporated | `QCOM` | 4.2 | 4.4 | 18.5% | 17.0 | -2.7% | 4.8% | 5.5% | **25** | **15** |

## Files

- `scanner.py` — scanner and scoring logic
- `hk_btc_correlation.py` — BTC/Hong Kong correlation scanner
- `reports/latest.md` — latest full report
- `reports/hk_btc_latest.md` — BTC vs Hang Seng/HSTECH/Xiaomi correlation report
- `data/latest.csv` — latest machine-readable snapshot, including analyst targets/gap
- `data/history.csv` — hourly history of **all companies** for later backtests
- `data/hk_btc_history.csv` — rolling BTC/Hong Kong correlation history
- `.github/workflows/hourly-okx-scanner.yml` — hourly GitHub Action

## Data

The configured universe can be pinned to the exact OKX EEA xStocks/USDC markets confirmed in the user's app. When that allowlist is present it overrides the broader public catalogue. Yahoo Finance/yfinance supplies company valuation, cash-flow and analyst-growth estimates. ETFs can exist in the OKX universe but are excluded from the company-fundamentals ranking.

### Optional account-accurate filter

Add read-only GitHub Actions secrets `OKX_API_KEY`, `OKX_API_SECRET`, and `OKX_API_PASSPHRASE`. The scanner will then query the authenticated OKX EEA account-instruments endpoint and only score contracts available to that account. Do not grant Trade or Withdraw permission for this scanner.

This is a quantitative research screen, not an automatic trading system. It does not place orders or select leverage.
