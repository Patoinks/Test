# OKX Long / Short Fundamental Scanner

Hourly scanner restricted to public companies exposed by the **OKX EEA TradFi / Stock Perpetual API universe**.

**Last scan:** 2026-10-14 07:45 UTC  
**Availability scope:** user-confirmed OKX EEA Stock Futures / X-Perp  
**OKX stock/ETF markets in configured universe:** 72  
**Public companies analysed:** 55  
**SHORT CORE:** 6  
**LONG CORE:** 4

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
| 1 | Taiwan Semiconductor Manufactur | TSM | 0.0% | -5.7% | -2.9% | 88 | +2 | **90** | **CORE** | yes |
| 2 | Applied Materials, Inc. | AMAT | 0.0% | -10.8% | -5.4% | 81 | +4 | **85** | **CORE** | yes |
| 3 | Broadcom Inc. | AVGO | 0.0% | -5.1% | -2.5% | 82 | +2 | **84** | **CORE** | yes |
| 4 | NVIDIA Corporation | NVDA | -0.0% | -3.8% | -1.9% | 82 | +2 | **84** | **CORE** | yes |
| 5 | Applovin Corporation | APP | 0.0% | -3.2% | -1.6% | 82 | +1 | **83** | **CORE** | yes |
| 6 | Micron Technology, Inc. | MU | -0.0% | -12.4% | -6.2% | 77 | +5 | **82** | **CORE** | yes |
| 7 | Sandisk Corporation | SNDK | 0.0% | -12.4% | -6.2% | 77 | +5 | **82** | **CORE** | yes |
| 8 | Advanced Micro Devices, Inc. | AMD | -0.0% | -6.2% | -3.1% | 79 | +2 | **81** | **CORE** | yes |
| 9 | Marvell Technology, Inc. | MRVL | -0.0% | -5.6% | -2.8% | 79 | +2 | **81** | **CORE** | yes |
| 10 | Credo Technology Group Holding  | CRDO | 0.0% | -9.9% | -4.9% | 76 | +4 | **80** | **CORE** | yes |

## Final model + Price Timing — SHORT

| Rank | Company | OKX | 24h | 7d | 50/50 move | Base SHORT | Timing adj. | Final | Signal | Prev. SHORT? |
|---:|---|---|---:|---:|---:|---:|---:|---:|---|---|
| 1 | Rocket Lab Corporation | RKLB | -0.0% | -10.7% | -5.4% | 100 | -4 | **96** | **CORE** | yes |
| 2 | USA Rare Earth, Inc. | USAR | 0.0% | -14.7% | -7.4% | 100 | -6 | **94** | **CORE** | yes |
| 3 | Cerebras Systems Inc. | CBRS | -0.0% | -14.8% | -7.4% | 98 | -6 | **92** | **CORE** | yes |
| 4 | Nebius Group N.V. | NBIS | -0.0% | -12.8% | -6.4% | 90 | -5 | **85** | **CORE** | yes |
| 5 | IonQ, Inc. | IONQ | 0.0% | -16.0% | -8.0% | 88 | -6 | **82** | **CORE** | yes |
| 6 | Moderna, Inc. | MRNA | 0.0% | 10.1% | 5.0% | 72 | +4 | **76** | **CORE** | yes |
| 7 | AST SpaceMobile, Inc. | ASTS | 0.0% | -22.4% | -11.2% | 80 | -9 | **71** | **WATCH** | yes |
| 8 | Okta, Inc. | OKTA | 0.0% | 3.9% | 2.0% | 61 | +2 | **63** | **WATCH** | yes |
| 9 | IREN LIMITED | IREN | 0.0% | -10.1% | -5.0% | 64 | -4 | **60** | **WATCH** | yes |
| 10 | Lumentum Holdings Inc. | LITE | 0.0% | -11.1% | -5.5% | 59 | -4 | **55** | **WATCH** | no |

## Combined model — LONG

Weighted score: **70% fundamental + 30% P/E trend**.

| Rank | Company | OKX | Fundamental LONG | P/E trend LONG | Combined | Signal |
|---:|---|---|---:|---:|---:|---|
| 1 | Taiwan Semiconductor Manufactur | `TSM` | 90 | 85 | **88** | **CORE** |
| 2 | Applovin Corporation | `APP` | 83 | 80 | **82** | **CORE** |
| 3 | NVIDIA Corporation | `NVDA` | 75 | 100 | **82** | **CORE** |
| 4 | Broadcom Inc. | `AVGO` | 75 | 100 | **82** | **CORE** |
| 5 | Applied Materials, Inc. | `AMAT` | 77 | 91 | **81** | **CORE** |
| 6 | Advanced Micro Devices, Inc. | `AMD` | 70 | 100 | **79** | **CORE** |
| 7 | Marvell Technology, Inc. | `MRVL` | 70 | 100 | **79** | **CORE** |
| 8 | Oracle Corporation | `ORCL` | 70 | 95 | **78** | **CORE** |
| 9 | Micron Technology, Inc. | `MU` | 75 | 82 | **77** | **CORE** |
| 10 | Sandisk Corporation | `SNDK` | 75 | 82 | **77** | **CORE** |

## Combined model — SHORT

Weighted score: **70% fundamental + 30% P/E trend**.

| Rank | Company | OKX | Fundamental SHORT | P/E trend SHORT | Combined | Signal |
|---:|---|---|---:|---:|---:|---|
| 1 | Rocket Lab Corporation | `RKLB` | 100 | 0 | **100** | **CORE** |
| 2 | USA Rare Earth, Inc. | `USAR` | 100 | 0 | **100** | **CORE** |
| 3 | Cerebras Systems Inc. | `CBRS` | 98 | 0 | **98** | **CORE** |
| 4 | Nebius Group N.V. | `NBIS` | 90 | 0 | **90** | **CORE** |
| 5 | IonQ, Inc. | `IONQ` | 88 | 0 | **88** | **CORE** |
| 6 | AST SpaceMobile, Inc. | `ASTS` | 80 | 0 | **80** | **WATCH** |
| 7 | Moderna, Inc. | `MRNA` | 72 | 0 | **72** | **WATCH** |
| 8 | Okta, Inc. | `OKTA` | 80 | 18 | **61** | **WATCH** |

## P/E Compression + Growth — LONG

| Rank | Company | OKX | Trail P/E | Fwd P/E | P/E change | EPS +1y | Rev +1y | Rev trend | LONG score | Signal |
|---:|---|---|---:|---:|---:|---:|---:|---|---:|---|
| 1 | NVIDIA Corporation | `NVDA` | 28.9 | 14.4 | -50.3% | 70.9% | 68.2% | decelerating | **100** | **CORE** |
| 2 | Broadcom Inc. | `AVGO` | 44.8 | 18.4 | -58.9% | 66.4% | 64.1% | decelerating | **100** | **CORE** |
| 3 | Advanced Micro Devices, Inc. | `AMD` | 154.5 | 38.5 | -75.1% | 107.2% | 74.6% | accelerating | **100** | **CORE** |
| 4 | Marvell Technology, Inc. | `MRVL` | 88.4 | 36.9 | -58.3% | 72.6% | 63.1% | accelerating | **100** | **CORE** |
| 5 | Credo Technology Group Holding  | `CRDO` | 70.3 | 20.5 | -70.9% | 53.7% | 54.8% | decelerating | **96** | **CORE** |
| 6 | Corning Incorporated | `GLW` | 68.1 | 34.0 | -50.1% | 33.0% | 19.6% | accelerating | **96** | **CORE** |
| 7 | AXT Inc | `AXT` | 1615.8 | 28.7 | -98.2% | 159.2% | 111.3% | decelerating | **96** | **CORE** |
| 8 | Oracle Corporation | `ORCL` | 22.4 | 13.0 | -42.0% | 35.1% | 45.7% | accelerating | **95** | **CORE** |
| 9 | Applied Materials, Inc. | `AMAT` | 40.1 | 25.1 | -37.3% | 44.5% | 35.2% | accelerating | **91** | **CORE** |
| 10 | Coherent Corp. | `COHR` | 70.4 | 20.6 | -70.7% | 49.1% | 38.8% | decelerating | **91** | **CORE** |

## P/E Expansion + Weakening — SHORT

| Rank | Company | OKX | Trail P/E | Fwd P/E | P/E change | EPS +1y | Rev +1y | Rev trend | SHORT score | Signal |
|---:|---|---|---:|---:|---:|---:|---:|---|---:|---|
| 1 | SOFTBANK GROUP CORP | `SOFTBANK` | 6.2 | 18.1 | 191.0% | -14.5% | 6.9% | decelerating | **86** | **CORE** |
| 2 | Alphabet Inc. | `GOOGL` | 17.8 | 23.2 | 30.7% | -27.1% | 23.9% | decelerating | **70** | **CORE** |
| 3 | Hyperliquid Strategies Inc | `PURR` | 3.2 | 27.6 | 767.6% | 51.0% | 31.4% | decelerating | **55** | **WATCH** |
| 4 | Amazon.com, Inc. | `AMZN` | 20.8 | 24.7 | 18.9% | -18.3% | 14.5% | decelerating | **52** | **WATCH** |

## Top SHORT candidates

| Rank | Company | OKX market | SHORT score | Signal | P/S | EV/S | Op margin | Fwd P/E | Rev +1y | FCF yield |
|---:|---|---|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Rocket Lab Corporation | `RKLB-USDT-SWAP` | **100** | **CORE** | 53.4 | 47.1 | -24.6% | 988.2 | 41.3% | -0.6% |
| 2 | USA Rare Earth, Inc. | `USAR-USDT-SWAP` | **100** | **CORE** | 321.4 | 94.4 | -795.6% | 376.0 | 870.1% | -6.7% |
| 3 | Cerebras Systems Inc. | `CBRS-USDT-SWAP` | **98** | **CORE** | 52.0 | 42.6 | -265.0% | 117.1 | 232.7% | — |
| 4 | Nebius Group N.V. | `NBIS-USDT-SWAP` | **90** | **CORE** | 41.5 | 43.4 | -0.2% | -58.1 | 268.0% | -17.1% |
| 5 | IonQ, Inc. | `IONQ-USDT-SWAP` | **88** | **CORE** | 57.1 | 45.4 | -408.2% | -26.9 | 79.0% | -0.6% |
| 6 | Okta, Inc. | `OKTA-USDT-SWAP` | **80** | **CORE** | 12.9 | 12.2 | 13.3% | 51.7 | 10.0% | 2.6% |
| 7 | AST SpaceMobile, Inc. | `ASTS-USDT-SWAP` | **80** | **WATCH** | 158.9 | 132.9 | -544.6% | -36.6 | 247.3% | -9.8% |
| 8 | Moderna, Inc. | `MRNA-USDT-SWAP` | **72** | **WATCH** | 38.7 | 37.0 | -557.9% | -48.7 | 16.1% | 0.3% |

## Top LONG candidates

| Rank | Company | OKX market | LONG score | Signal | P/S | EV/S | Op margin | Fwd P/E | Rev +1y | FCF yield |
|---:|---|---|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Taiwan Semiconductor Manufactur | `TSM-USDT-SWAP` | **90** | **CORE** | 0.5 | 3.6 | 60.3% | 19.9 | 35.9% | 31.7% |
| 2 | Applovin Corporation | `APP-USDT-SWAP` | **83** | **CORE** | 13.4 | 13.4 | 77.7% | 13.3 | 26.2% | 3.5% |
| 3 | Applied Materials, Inc. | `AMAT-USDT-SWAP` | **77** | **WATCH** | 11.9 | 11.9 | 33.7% | 25.1 | 35.2% | 0.8% |
| 4 | Broadcom Inc. | `AVGO-USDT-SWAP` | **75** | **WATCH** | 19.1 | 19.5 | 54.3% | 18.4 | 64.1% | 1.8% |
| 5 | Micron Technology, Inc. | `MU-USDT-SWAP` | **75** | **CORE** | 8.1 | 7.8 | 80.7% | 4.6 | 15.7% | 2.7% |
| 6 | Sandisk Corporation | `SNDK-USDT-SWAP` | **75** | **CORE** | 10.6 | 10.5 | 78.5% | 5.6 | 18.9% | 3.6% |
| 7 | NVIDIA Corporation | `NVDA-USDT-SWAP` | **75** | **WATCH** | 18.2 | 18.1 | 66.2% | 14.4 | 68.2% | 0.8% |
| 8 | Western Digital Corporation | `WDC-USDT-SWAP` | **75** | **WATCH** | 11.0 | 10.6 | 43.6% | 11.6 | 36.8% | 1.6% |
| 9 | Robinhood Markets, Inc. | `HOOD-USDT-SWAP` | **70** | **WATCH** | 20.1 | 20.0 | 43.9% | 32.2 | 29.2% | — |
| 10 | Marvell Technology, Inc. | `MRVL-USDT-SWAP` | **70** | **WATCH** | 25.6 | 25.1 | 16.7% | 36.9 | 63.1% | 1.0% |

## Analyst consensus (12-month price target) — most upside

| Rank | Company | OKX | Price | Analyst mean target | Gap | Analysts | Currency |
|---:|---|---|---:|---:|---:|---:|---|
| 1 | IREN LIMITED | `IREN` | 34.80 | 78.14 | **124.5%** | 18 | USD |
| 2 | SK hynix | `SKHYNIX` | 1419000.00 | 3141024.80 | **121.4%** | 38 | KRW |
| 3 | Hyperliquid Strategies Inc | `PURR` | 10.23 | 22.32 | **118.2%** | 4 | USD |
| 4 | SamsungElec | `SAMSUNG` | 232000.00 | 478905.62 | **106.4%** | 36 | KRW |
| 5 | Cerebras Systems Inc. | `CBRS` | 149.09 | 291.64 | **95.6%** | 11 | USD |
| 6 | BitMine Immersion Technologies, | `BMNR` | 23.49 | 45.87 | **95.3%** | 3 | USD |
| 7 | IonQ, Inc. | `IONQ` | 34.73 | 66.63 | **91.9%** | 14 | USD |
| 8 | CoreWeave, Inc. | `CRWV` | 77.81 | 141.47 | **81.8%** | 38 | USD |
| 9 | Applovin Corporation | `APP` | 272.28 | 483.79 | **77.7%** | 31 | USD |
| 10 | Western Digital Corporation | `WDC` | 380.71 | 668.50 | **75.6%** | 24 | USD |
| 11 | Applied Optoelectronics, Inc. | `AAOI` | 97.78 | 163.40 | **67.1%** | 5 | USD |
| 12 | Oracle Corporation | `ORCL` | 143.20 | 237.97 | **66.2%** | 41 | USD |
| 13 | Micron Technology, Inc. | `MU` | 953.19 | 1560.57 | **63.7%** | 46 | USD |
| 14 | Rocket Lab Corporation | `RKLB` | 64.22 | 105.05 | **63.6%** | 19 | USD |
| 15 | AST SpaceMobile, Inc. | `ASTS` | 47.06 | 74.28 | **57.8%** | 12 | USD |

## Analyst consensus (12-month price target) — most downside

| Rank | Company | OKX | Price | Analyst mean target | Gap | Analysts | Currency |
|---:|---|---|---:|---:|---:|---:|---|
| 1 | Moderna, Inc. | `MRNA` | 216.25 | 122.67 | **-43.3%** | 18 | USD |
| 2 | Okta, Inc. | `OKTA` | 226.53 | 212.60 | **-6.2%** | 43 | USD |
| 3 | Apple Inc. | `AAPL` | 341.27 | 329.38 | **-3.5%** | 39 | USD |
| 4 | Palantir Technologies Inc. | `PLTR` | 208.67 | 205.27 | **-1.6%** | 26 | USD |

Price/target uses the underlying Yahoo Finance share quote, not the OKX derivative. Minimum 3 analysts; unreliable price scales and missing coverage excluded. Targets are analyst opinions, not guaranteed forecasts.

## All OKX companies — our ratio + LONG/SHORT scores

| Company | OKX | P/S | EV/S | Op margin | Fwd P/E | EPS +1y | Rev +1y | FCF yield | LONG | SHORT |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Rocket Lab Corporation | `RKLB` | 53.4 | 47.1 | -24.6% | 988.2 | 75.5% | 41.3% | -0.6% | **0** | **100 CORE** |
| USA Rare Earth, Inc. | `USAR` | 321.4 | 94.4 | -795.6% | 376.0 | 105.3% | 870.1% | -6.7% | **0** | **100 CORE** |
| Cerebras Systems Inc. | `CBRS` | 52.0 | 42.6 | -265.0% | 117.1 | 371.3% | 232.7% | — | **0** | **98 CORE** |
| Taiwan Semiconductor Manufactur | `TSM` | 0.5 | 3.6 | 60.3% | 19.9 | 30.9% | 35.9% | 31.7% | **90 CORE** | **10** |
| Nebius Group N.V. | `NBIS` | 41.5 | 43.4 | -0.2% | -58.1 | -191.4% | 268.0% | -17.1% | **0** | **90 CORE** |
| IonQ, Inc. | `IONQ` | 57.1 | 45.4 | -408.2% | -26.9 | 18.1% | 79.0% | -0.6% | **0** | **88 CORE** |
| Applovin Corporation | `APP` | 13.4 | 13.4 | 77.7% | 13.3 | 27.5% | 26.2% | 3.5% | **83 CORE** | **10** |
| Okta, Inc. | `OKTA` | 12.9 | 12.2 | 13.3% | 51.7 | 11.4% | 10.0% | 2.6% | **8** | **80 CORE** |
| AST SpaceMobile, Inc. | `ASTS` | 158.9 | 132.9 | -544.6% | -36.6 | 44.3% | 247.3% | -9.8% | **0** | **80 WATCH** |
| Applied Materials, Inc. | `AMAT` | 11.9 | 11.9 | 33.7% | 25.1 | 44.5% | 35.2% | 0.8% | **77 WATCH** | **13** |
| NVIDIA Corporation | `NVDA` | 18.2 | 18.1 | 66.2% | 14.4 | 70.9% | 68.2% | 0.8% | **75 WATCH** | **18** |
| Broadcom Inc. | `AVGO` | 19.1 | 19.5 | 54.3% | 18.4 | 66.4% | 64.1% | 1.8% | **75 WATCH** | **28** |
| Micron Technology, Inc. | `MU` | 8.1 | 7.8 | 80.7% | 4.6 | 17.1% | 15.7% | 2.7% | **75 CORE** | **30** |
| Sandisk Corporation | `SNDK` | 10.6 | 10.5 | 78.5% | 5.6 | 24.0% | 18.9% | 3.6% | **75 CORE** | **10** |
| Western Digital Corporation | `WDC` | 11.0 | 10.6 | 43.6% | 11.6 | 60.4% | 36.8% | 1.6% | **75 WATCH** | **18** |
| Moderna, Inc. | `MRNA` | 38.7 | 37.0 | -557.9% | -48.7 | 43.0% | 16.1% | 0.3% | **0** | **72 WATCH** |
| Advanced Micro Devices, Inc. | `AMD` | 23.9 | 23.7 | 17.2% | 38.5 | 107.2% | 74.6% | 0.9% | **70 WATCH** | **13** |
| Marvell Technology, Inc. | `MRVL` | 25.6 | 25.1 | 16.7% | 36.9 | 72.6% | 63.1% | 1.0% | **70 WATCH** | **13** |
| Oracle Corporation | `ORCL` | 6.0 | 7.9 | 35.6% | 13.0 | 35.1% | 45.7% | -10.6% | **70 WATCH** | **10** |
| Robinhood Markets, Inc. | `HOOD` | 20.1 | 20.0 | 43.9% | 32.2 | 36.4% | 29.2% | — | **70 WATCH** | **5** |
| XIAOMI-W | `XIAOMI` | 1.6 | 1.3 | 4.0% | 17.2 | 38.8% | 22.3% | -1.3% | **70 WATCH** | **10** |
| Credo Technology Group Holding  | `CRDO` | 23.4 | 23.0 | 25.2% | 20.5 | 53.7% | 54.8% | 0.7% | **67 WATCH** | **28** |
| Adobe Inc. | `ADBE` | 3.5 | 3.6 | 34.8% | 8.5 | 12.9% | 9.1% | 10.2% | **65 WATCH** | **30** |
| IREN LIMITED | `IREN` | 19.4 | 22.1 | -102.5% | -8.7 | -16.4% | 160.9% | -30.8% | **0** | **64** |
| Tesla, Inc. | `TSLA` | 14.3 | 14.0 | 1.4% | 172.1 | 25.1% | 13.6% | 0.3% | **30** | **63** |
| Corning Incorporated | `GLW` | 7.5 | 8.0 | 15.6% | 34.0 | 33.0% | 19.6% | 0.6% | **60 WATCH** | **13** |
| Microsoft Corporation | `MSFT` | 12.2 | 12.3 | 45.1% | 23.0 | 19.8% | 19.6% | 0.4% | **59 WATCH** | **23** |
| Lumentum Holdings Inc. | `LITE` | 29.7 | 29.0 | 28.0% | 27.5 | 64.8% | 56.4% | 0.3% | **0** | **59** |
| Coca-Cola Company (The) | `KO` | 7.7 | 8.3 | 34.9% | 25.6 | 6.7% | 0.1% | 1.3% | **7** | **58** |
| Apple Inc. | `AAPL` | 10.7 | 10.7 | 32.6% | 35.6 | 8.6% | 10.5% | 2.2% | **5** | **58** |
| Bloom Energy Corporation | `BE` | 24.9 | 25.0 | 17.1% | 53.5 | 82.0% | 64.4% | 0.7% | **55 WATCH** | **48** |
| AXT Inc | `AXT` | 33.8 | 31.1 | 21.9% | 28.7 | 159.2% | 111.3% | -1.0% | **52** | **35** |
| Coherent Corp. | `COHR` | 8.0 | 8.2 | 11.8% | 20.6 | 49.1% | 38.8% | -1.1% | **52** | **35** |
| Super Micro Computer, Inc. | `SMCI` | 0.7 | 0.8 | 13.4% | 7.3 | 22.8% | 17.3% | -32.1% | **52** | **25** |
| Netflix, Inc. | `NFLX` | 6.1 | 6.2 | 33.4% | 18.5 | 5.9% | 11.2% | 8.7% | **35** | **50** |
| Palantir Technologies Inc. | `PLTR` | 81.5 | 80.0 | 47.1% | 88.7 | 45.2% | 50.1% | 0.4% | **33** | **48** |
| Intel Corporation | `INTC` | 9.5 | 9.7 | 12.2% | 49.2 | 37.2% | 14.9% | 0.9% | **5** | **48** |
| SK hynix | `SKHYNIX` | 5.3 | 5.1 | 76.3% | 3.0 | 32.4% | 54.4% | 5.5% | **45** | **5** |
| SK hynix | `SKHY` | 5.3 | 5.1 | 76.3% | 3.0 | 32.4% | 54.4% | 5.5% | **45** | **5** |
| SamsungElec | `SAMSUNG` | 3.1 | 2.8 | 52.2% | 3.2 | 50.9% | 38.0% | 4.6% | **45** | **10** |
| Circle Internet Group, Inc. | `CRCL` | 7.4 | 6.8 | 4.9% | 57.4 | 31.7% | 25.8% | 1.0% | **43** | **33** |
| Coinbase Global, Inc. | `COIN` | 7.9 | 7.6 | -13.9% | 60.4 | 261.3% | 29.8% | 5.6% | **20** | **40** |
| SOFTBANK GROUP CORP | `SOFTBANK` | 3.8 | 7.1 | -11.6% | 18.1 | -14.5% | 6.9% | -7.2% | **0** | **40** |
| CoreWeave, Inc. | `CRWV` | 5.7 | 11.7 | -1.9% | -42.4 | 15.4% | 104.3% | -21.2% | **0** | **40** |
| Dell Technologies Inc. | `DELL` | 2.4 | 2.6 | 12.0% | 19.1 | 9.6% | 18.4% | 1.7% | **33** | **38** |
| Meta Platforms, Inc. | `META` | 8.5 | 8.6 | 34.8% | 22.0 | 9.8% | 20.6% | 1.1% | **17** | **38** |
| Alphabet Inc. | `GOOGL` | 9.7 | 9.5 | 34.0% | 23.2 | -27.1% | 23.9% | 0.5% | **2** | **38** |
| Amazon.com, Inc. | `AMZN` | 3.6 | 3.8 | 13.7% | 24.7 | -18.3% | 14.5% | 0.1% | **0** | **38** |
| Arm Holdings plc | `ARM` | 52.9 | 52.2 | 7.6% | 83.4 | 37.5% | 36.2% | 0.5% | **35** | **33** |
| Fluence Energy, Inc. | `FLNC` | 0.5 | 0.4 | -8.9% | -25.5 | 70.1% | 35.3% | 0.2% | **5** | **28** |
| Hyperliquid Strategies Inc | `PURR` | 300.9 | 199.4 | 9595.1% | 27.6 | 51.0% | 31.4% | — | **25** | **10** |
| BitMine Immersion Technologies, | `BMNR` | 231.6 | 226.0 | 8.4% | 25.0 | 103.2% | 421.8% | -3.7% | **25** | **25** |
| Strategy Inc | `MSTR` | 121.8 | 155.0 | -6808.1% | 3.1 | 157.6% | 2.2% | -37.2% | **25** | **25** |
| QUALCOMM Incorporated | `QCOM` | 4.3 | 4.4 | 18.5% | 17.3 | -2.7% | 4.8% | 5.4% | **25** | **15** |
| Applied Optoelectronics, Inc. | `AAOI` | 13.9 | 13.5 | -12.9% | 21.2 | 576.8% | 156.5% | -10.7% | **2** | **25** |

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
