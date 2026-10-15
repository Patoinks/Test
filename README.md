# OKX Long / Short Fundamental Scanner

Hourly scanner restricted to public companies exposed by the **OKX EEA TradFi / Stock Perpetual API universe**.

**Last scan:** 2026-10-15 18:22 UTC  
**Availability scope:** user-confirmed OKX EEA Stock Futures / X-Perp  
**OKX stock/ETF markets in configured universe:** 72  
**Public companies analysed:** 55  
**SHORT CORE:** 5  
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
| 1 | Taiwan Semiconductor Manufactur | TSM | -2.8% | -8.8% | -5.8% | 88 | +5 | **93** | **CORE** | yes |
| 2 | Credo Technology Group Holding  | CRDO | -3.1% | -18.0% | -10.6% | 82 | +8 | **90** | **CORE** | yes |
| 3 | Applied Materials, Inc. | AMAT | -4.2% | -16.0% | -10.1% | 81 | +8 | **89** | **CORE** | yes |
| 4 | Marvell Technology, Inc. | MRVL | -3.8% | -14.1% | -8.9% | 79 | +7 | **86** | **CORE** | yes |
| 5 | Broadcom Inc. | AVGO | -2.4% | -6.2% | -4.3% | 82 | +3 | **85** | **CORE** | yes |
| 6 | NVIDIA Corporation | NVDA | -1.9% | -5.9% | -3.9% | 82 | +3 | **85** | **CORE** | yes |
| 7 | Advanced Micro Devices, Inc. | AMD | -3.4% | -11.2% | -7.3% | 79 | +6 | **85** | **CORE** | yes |
| 8 | Corning Incorporated | GLW | -4.6% | -12.1% | -8.3% | 78 | +7 | **85** | **CORE** | yes |
| 9 | Sandisk Corporation | SNDK | -4.0% | -16.3% | -10.2% | 77 | +8 | **85** | **CORE** | yes |
| 10 | Western Digital Corporation | WDC | -5.5% | -12.5% | -9.0% | 76 | +7 | **83** | **CORE** | yes |

## Final model + Price Timing — SHORT

| Rank | Company | OKX | 24h | 7d | 50/50 move | Base SHORT | Timing adj. | Final | Signal | Prev. SHORT? |
|---:|---|---|---:|---:|---:|---:|---:|---:|---|---|
| 1 | USA Rare Earth, Inc. | USAR | 5.3% | -13.9% | -4.3% | 100 | -3 | **97** | **CORE** | yes |
| 2 | Moderna, Inc. | MRNA | 5.1% | 20.8% | 12.9% | 80 | +10 | **90** | **CORE** | yes |
| 3 | Rocket Lab Corporation | RKLB | -10.2% | -22.3% | -16.2% | 100 | -13 | **87** | **CORE** | yes |
| 4 | Cerebras Systems Inc. | CBRS | -2.6% | -17.9% | -10.3% | 92 | -8 | **84** | **CORE** | yes |
| 5 | IonQ, Inc. | IONQ | 4.4% | -16.9% | -6.3% | 88 | -5 | **83** | **CORE** | yes |
| 6 | Nebius Group N.V. | NBIS | -3.2% | -18.1% | -10.6% | 84 | -9 | **75** | **CORE** | yes |
| 7 | AST SpaceMobile, Inc. | ASTS | 3.4% | -23.5% | -10.0% | 80 | -8 | **72** | **WATCH** | yes |
| 8 | Okta, Inc. | OKTA | -1.9% | -5.6% | -3.7% | 60 | -3 | **57** | **WATCH** | yes |

## Combined model — LONG

Weighted score: **70% fundamental + 30% P/E trend**.

| Rank | Company | OKX | Fundamental LONG | P/E trend LONG | Combined | Signal |
|---:|---|---|---:|---:|---:|---|
| 1 | Taiwan Semiconductor Manufactur | `TSM` | 90 | 85 | **88** | **CORE** |
| 2 | Applovin Corporation | `APP` | 83 | 80 | **82** | **CORE** |
| 3 | Credo Technology Group Holding  | `CRDO` | 75 | 100 | **82** | **CORE** |
| 4 | NVIDIA Corporation | `NVDA` | 75 | 100 | **82** | **CORE** |
| 5 | Broadcom Inc. | `AVGO` | 75 | 100 | **82** | **CORE** |
| 6 | Applied Materials, Inc. | `AMAT` | 77 | 91 | **81** | **CORE** |
| 7 | Robinhood Markets, Inc. | `HOOD` | 77 | 86 | **80** | **CORE** |
| 8 | Marvell Technology, Inc. | `MRVL` | 70 | 100 | **79** | **CORE** |
| 9 | Advanced Micro Devices, Inc. | `AMD` | 70 | 100 | **79** | **CORE** |
| 10 | Corning Incorporated | `GLW` | 70 | 96 | **78** | **CORE** |

## Combined model — SHORT

Weighted score: **70% fundamental + 30% P/E trend**.

| Rank | Company | OKX | Fundamental SHORT | P/E trend SHORT | Combined | Signal |
|---:|---|---|---:|---:|---:|---|
| 1 | USA Rare Earth, Inc. | `USAR` | 100 | 0 | **100** | **CORE** |
| 2 | Rocket Lab Corporation | `RKLB` | 100 | 0 | **100** | **CORE** |
| 3 | Cerebras Systems Inc. | `CBRS` | 92 | 0 | **92** | **CORE** |
| 4 | IonQ, Inc. | `IONQ` | 88 | 0 | **88** | **CORE** |
| 5 | Nebius Group N.V. | `NBIS` | 84 | 0 | **84** | **WATCH** |
| 6 | Moderna, Inc. | `MRNA` | 80 | 0 | **80** | **WATCH** |
| 7 | AST SpaceMobile, Inc. | `ASTS` | 80 | 0 | **80** | **WATCH** |
| 8 | Okta, Inc. | `OKTA` | 80 | 13 | **60** | **WATCH** |

## P/E Compression + Growth — LONG

| Rank | Company | OKX | Trail P/E | Fwd P/E | P/E change | EPS +1y | Rev +1y | Rev trend | LONG score | Signal |
|---:|---|---|---:|---:|---:|---:|---:|---|---:|---|
| 1 | Credo Technology Group Holding  | `CRDO` | 68.1 | 17.9 | -73.7% | 53.7% | 54.8% | decelerating | **100** | **CORE** |
| 2 | Marvell Technology, Inc. | `MRVL` | 74.9 | 32.4 | -56.7% | 72.9% | 63.2% | accelerating | **100** | **CORE** |
| 3 | NVIDIA Corporation | `NVDA` | 28.3 | 13.6 | -51.9% | 70.9% | 68.2% | decelerating | **100** | **CORE** |
| 4 | Advanced Micro Devices, Inc. | `AMD` | 149.0 | 35.0 | -76.5% | 107.7% | 74.8% | accelerating | **100** | **CORE** |
| 5 | Broadcom Inc. | `AVGO` | 44.5 | 17.4 | -60.9% | 66.4% | 64.2% | decelerating | **100** | **CORE** |
| 6 | Corning Incorporated | `GLW` | 64.9 | 30.7 | -52.6% | 33.0% | 19.6% | accelerating | **96** | **CORE** |
| 7 | AXT Inc | `AXT` | 1390.8 | 24.7 | -98.2% | 159.2% | 111.3% | decelerating | **96** | **CORE** |
| 8 | Coherent Corp. | `COHR` | 65.4 | 17.4 | -73.4% | 49.2% | 38.9% | decelerating | **95** | **CORE** |
| 9 | Oracle Corporation | `ORCL` | 22.9 | 12.1 | -47.1% | 35.1% | 45.7% | accelerating | **95** | **CORE** |
| 10 | Arm Holdings plc | `ARM` | 265.9 | 78.1 | -70.6% | 37.5% | 36.2% | accelerating | **95** | **CORE** |

## P/E Expansion + Weakening — SHORT

| Rank | Company | OKX | Trail P/E | Fwd P/E | P/E change | EPS +1y | Rev +1y | Rev trend | SHORT score | Signal |
|---:|---|---|---:|---:|---:|---:|---:|---|---:|---|
| 1 | SOFTBANK GROUP CORP | `SOFTBANK` | 5.6 | 16.4 | 191.0% | -14.5% | 6.9% | decelerating | **86** | **CORE** |
| 2 | Hyperliquid Strategies Inc | `PURR` | 3.2 | 26.1 | 705.4% | 51.0% | 31.4% | decelerating | **55** | **WATCH** |
| 3 | Amazon.com, Inc. | `AMZN` | 20.7 | 24.2 | 16.8% | -18.2% | 14.6% | decelerating | **52** | **WATCH** |
| 4 | Alphabet Inc. | `GOOGL` | 17.8 | 22.9 | 28.4% | -26.9% | 24.4% | accelerating | **50** | **WATCH** |

## Top SHORT candidates

| Rank | Company | OKX market | SHORT score | Signal | P/S | EV/S | Op margin | Fwd P/E | Rev +1y | FCF yield |
|---:|---|---|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Rocket Lab Corporation | `RKLB-USDT-SWAP` | **100** | **CORE** | 44.2 | 43.2 | -24.6% | 818.1 | 40.8% | -0.7% |
| 2 | USA Rare Earth, Inc. | `USAR-USDT-SWAP` | **100** | **CORE** | 309.8 | 76.6 | -795.6% | 362.3 | 870.1% | -7.0% |
| 3 | Cerebras Systems Inc. | `CBRS-USDT-SWAP` | **92** | **CORE** | 48.1 | 39.9 | -265.0% | 108.2 | 232.7% | — |
| 4 | IonQ, Inc. | `IONQ-USDT-SWAP` | **88** | **CORE** | 53.9 | 40.2 | -408.2% | -24.4 | 77.6% | -0.7% |
| 5 | Nebius Group N.V. | `NBIS-USDT-SWAP` | **84** | **WATCH** | 33.7 | 39.2 | -0.2% | -50.6 | 268.0% | -21.0% |
| 6 | Okta, Inc. | `OKTA-USDT-SWAP` | **80** | **CORE** | 11.8 | 11.3 | 13.3% | 47.5 | 10.0% | 2.9% |
| 7 | AST SpaceMobile, Inc. | `ASTS-USDT-SWAP` | **80** | **WATCH** | 147.1 | 120.1 | -544.6% | -33.9 | 247.3% | -10.6% |
| 8 | Moderna, Inc. | `MRNA-USDT-SWAP` | **80** | **WATCH** | 42.6 | 38.8 | -557.9% | -53.6 | 16.1% | 0.3% |
| 9 | Tesla, Inc. | `TSLA-USDT-SWAP` | **63** | **WATCH** | 13.7 | 13.7 | 1.4% | 166.1 | 13.5% | 0.3% |

## Top LONG candidates

| Rank | Company | OKX market | LONG score | Signal | P/S | EV/S | Op margin | Fwd P/E | Rev +1y | FCF yield |
|---:|---|---|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Taiwan Semiconductor Manufactur | `TSM-USDT-SWAP` | **90** | **CORE** | 0.5 | 3.5 | 60.3% | 18.5 | 35.2% | 33.7% |
| 2 | Applovin Corporation | `APP-USDT-SWAP` | **83** | **CORE** | 13.5 | 12.9 | 77.7% | 13.5 | 26.0% | 3.4% |
| 3 | Robinhood Markets, Inc. | `HOOD-USDT-SWAP` | **77** | **WATCH** | 18.6 | 18.2 | 43.9% | 29.7 | 29.2% | — |
| 4 | Applied Materials, Inc. | `AMAT-USDT-SWAP` | **77** | **WATCH** | 11.0 | 11.4 | 33.7% | 23.2 | 35.2% | 0.9% |
| 5 | Credo Technology Group Holding  | `CRDO-USDT-SWAP` | **75** | **WATCH** | 20.5 | 20.7 | 25.2% | 17.9 | 54.8% | 0.8% |
| 6 | Micron Technology, Inc. | `MU-USDT-SWAP` | **75** | **CORE** | 7.7 | 7.5 | 80.7% | 4.4 | 15.5% | 2.8% |
| 7 | Broadcom Inc. | `AVGO-USDT-SWAP` | **75** | **WATCH** | 18.1 | 18.9 | 54.3% | 17.4 | 64.2% | 1.9% |
| 8 | Sandisk Corporation | `SNDK-USDT-SWAP` | **75** | **CORE** | 9.6 | 9.9 | 78.5% | 5.1 | 18.9% | 4.0% |
| 9 | NVIDIA Corporation | `NVDA-USDT-SWAP` | **75** | **WATCH** | 17.3 | 17.5 | 66.2% | 13.6 | 68.2% | 0.8% |
| 10 | Western Digital Corporation | `WDC-USDT-SWAP` | **75** | **WATCH** | 10.0 | 10.1 | 43.6% | 10.4 | 37.2% | 1.8% |

## Analyst consensus (12-month price target) — most upside

| Rank | Company | OKX | Price | Analyst mean target | Gap | Analysts | Currency |
|---:|---|---|---:|---:|---:|---:|---|
| 1 | IREN LIMITED | `IREN` | 29.25 | 78.14 | **167.1%** | 18 | USD |
| 2 | SK hynix | `SKHYNIX` | 1262000.00 | 3141024.80 | **148.9%** | 38 | KRW |
| 3 | Hyperliquid Strategies Inc | `PURR` | 9.65 | 22.32 | **131.2%** | 4 | USD |
| 4 | SamsungElec | `SAMSUNG` | 210000.00 | 478905.62 | **128.1%** | 36 | KRW |
| 5 | Cerebras Systems Inc. | `CBRS` | 137.81 | 291.64 | **111.6%** | 11 | USD |
| 6 | CoreWeave, Inc. | `CRWV` | 67.26 | 140.76 | **109.3%** | 38 | USD |
| 7 | Applied Optoelectronics, Inc. | `AAOI` | 80.72 | 163.40 | **102.4%** | 5 | USD |
| 8 | BitMine Immersion Technologies, | `BMNR` | 23.14 | 45.87 | **98.2%** | 3 | USD |
| 9 | IonQ, Inc. | `IONQ` | 32.79 | 64.06 | **95.4%** | 14 | USD |
| 10 | Rocket Lab Corporation | `RKLB` | 53.17 | 103.39 | **94.4%** | 18 | USD |
| 11 | Western Digital Corporation | `WDC` | 344.14 | 668.50 | **94.3%** | 24 | USD |
| 12 | Oracle Corporation | `ORCL` | 133.52 | 237.97 | **78.2%** | 41 | USD |
| 13 | Applovin Corporation | `APP` | 276.02 | 480.08 | **73.9%** | 31 | USD |
| 14 | Micron Technology, Inc. | `MU` | 904.99 | 1560.57 | **72.4%** | 46 | USD |
| 15 | AST SpaceMobile, Inc. | `ASTS` | 43.58 | 74.28 | **70.5%** | 12 | USD |

## Analyst consensus (12-month price target) — most downside

| Rank | Company | OKX | Price | Analyst mean target | Gap | Analysts | Currency |
|---:|---|---|---:|---:|---:|---:|---|
| 1 | Moderna, Inc. | `MRNA` | 237.90 | 123.61 | **-48.0%** | 18 | USD |
| 2 | Apple Inc. | `AAPL` | 341.96 | 329.38 | **-3.7%** | 39 | USD |

Price/target uses the underlying Yahoo Finance share quote, not the OKX derivative. Minimum 3 analysts; unreliable price scales and missing coverage excluded. Targets are analyst opinions, not guaranteed forecasts.

## All OKX companies — our ratio + LONG/SHORT scores

| Company | OKX | P/S | EV/S | Op margin | Fwd P/E | EPS +1y | Rev +1y | FCF yield | LONG | SHORT |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| USA Rare Earth, Inc. | `USAR` | 309.8 | 76.6 | -795.6% | 362.3 | 105.3% | 870.1% | -7.0% | **0** | **100 CORE** |
| Rocket Lab Corporation | `RKLB` | 44.2 | 43.2 | -24.6% | 818.1 | 69.1% | 40.8% | -0.7% | **0** | **100 CORE** |
| Cerebras Systems Inc. | `CBRS` | 48.1 | 39.9 | -265.0% | 108.2 | 371.3% | 232.7% | — | **0** | **92 CORE** |
| Taiwan Semiconductor Manufactur | `TSM` | 0.5 | 3.5 | 60.3% | 18.5 | 27.9% | 35.2% | 33.7% | **90 CORE** | **10** |
| IonQ, Inc. | `IONQ` | 53.9 | 40.2 | -408.2% | -24.4 | 17.5% | 77.6% | -0.7% | **0** | **88 CORE** |
| Nebius Group N.V. | `NBIS` | 33.7 | 39.2 | -0.2% | -50.6 | -191.4% | 268.0% | -21.0% | **0** | **84 WATCH** |
| Applovin Corporation | `APP` | 13.5 | 12.9 | 77.7% | 13.5 | 27.3% | 26.0% | 3.4% | **83 CORE** | **10** |
| Okta, Inc. | `OKTA` | 11.8 | 11.3 | 13.3% | 47.5 | 11.4% | 10.0% | 2.9% | **8** | **80 CORE** |
| Moderna, Inc. | `MRNA` | 42.6 | 38.8 | -557.9% | -53.6 | 43.0% | 16.1% | 0.3% | **0** | **80 WATCH** |
| AST SpaceMobile, Inc. | `ASTS` | 147.1 | 120.1 | -544.6% | -33.9 | 44.3% | 247.3% | -10.6% | **0** | **80 WATCH** |
| Applied Materials, Inc. | `AMAT` | 11.0 | 11.4 | 33.7% | 23.2 | 44.4% | 35.2% | 0.9% | **77 WATCH** | **3** |
| Robinhood Markets, Inc. | `HOOD` | 18.6 | 18.2 | 43.9% | 29.7 | 36.5% | 29.2% | — | **77 WATCH** | **5** |
| Credo Technology Group Holding  | `CRDO` | 20.5 | 20.7 | 25.2% | 17.9 | 53.7% | 54.8% | 0.8% | **75 WATCH** | **28** |
| Sandisk Corporation | `SNDK` | 9.6 | 9.9 | 78.5% | 5.1 | 24.0% | 18.9% | 4.0% | **75 CORE** | **10** |
| NVIDIA Corporation | `NVDA` | 17.3 | 17.5 | 66.2% | 13.6 | 70.9% | 68.2% | 0.8% | **75 WATCH** | **18** |
| Broadcom Inc. | `AVGO` | 18.1 | 18.9 | 54.3% | 17.4 | 66.4% | 64.2% | 1.9% | **75 WATCH** | **28** |
| Western Digital Corporation | `WDC` | 10.0 | 10.1 | 43.6% | 10.4 | 61.2% | 37.2% | 1.8% | **75 WATCH** | **18** |
| Micron Technology, Inc. | `MU` | 7.7 | 7.5 | 80.7% | 4.4 | 15.8% | 15.5% | 2.8% | **75 CORE** | **30** |
| Marvell Technology, Inc. | `MRVL` | 22.4 | 22.9 | 16.7% | 32.4 | 72.9% | 63.2% | 1.1% | **70 WATCH** | **13** |
| Advanced Micro Devices, Inc. | `AMD` | 21.8 | 22.3 | 17.2% | 35.0 | 107.7% | 74.8% | 1.0% | **70 WATCH** | **13** |
| Corning Incorporated | `GLW` | 6.8 | 7.6 | 15.6% | 30.7 | 33.0% | 19.6% | 0.6% | **70 WATCH** | **13** |
| Oracle Corporation | `ORCL` | 5.6 | 7.4 | 35.6% | 12.1 | 35.1% | 45.7% | -11.3% | **70 WATCH** | **10** |
| XIAOMI-W | `XIAOMI` | 1.6 | 1.4 | 4.0% | 17.7 | 38.8% | 22.3% | -1.2% | **70 WATCH** | **10** |
| Adobe Inc. | `ADBE` | 3.8 | 3.7 | 34.8% | 9.1 | 12.4% | 9.1% | 9.6% | **65 WATCH** | **30** |
| Tesla, Inc. | `TSLA` | 13.7 | 13.7 | 1.4% | 166.1 | 24.4% | 13.5% | 0.3% | **22** | **63 WATCH** |
| Coherent Corp. | `COHR` | 6.8 | 7.5 | 11.8% | 17.4 | 49.2% | 38.9% | -1.3% | **60 WATCH** | **35** |
| IREN LIMITED | `IREN` | 16.3 | 19.8 | -102.5% | -7.3 | -16.4% | 164.0% | -36.6% | **0** | **60** |
| Microsoft Corporation | `MSFT` | 12.1 | 12.1 | 45.1% | 22.8 | 19.9% | 19.6% | 0.4% | **59 WATCH** | **23** |
| Lumentum Holdings Inc. | `LITE` | 25.5 | 26.3 | 28.0% | 23.5 | 65.3% | 57.0% | 0.3% | **0** | **59** |
| Apple Inc. | `AAPL` | 10.7 | 10.8 | 32.6% | 35.7 | 8.5% | 10.4% | 2.2% | **5** | **58** |
| Coca-Cola Company (The) | `KO` | 7.9 | 8.5 | 34.9% | 26.2 | 6.6% | -0.1% | 1.3% | **0** | **58** |
| Bloom Energy Corporation | `BE` | 21.8 | 22.7 | 17.1% | 46.7 | 82.1% | 65.5% | 0.8% | **55 WATCH** | **48** |
| AXT Inc | `AXT` | 29.1 | 29.5 | 21.9% | 24.7 | 159.2% | 111.3% | -1.2% | **52** | **35** |
| Super Micro Computer, Inc. | `SMCI` | 0.6 | 0.8 | 13.4% | 6.4 | 22.8% | 17.3% | -37.5% | **52** | **25** |
| Netflix, Inc. | `NFLX` | 6.3 | 6.2 | 33.4% | 19.1 | 6.0% | 11.2% | 8.4% | **35** | **50** |
| Palantir Technologies Inc. | `PLTR` | 77.8 | 77.0 | 47.1% | 85.0 | 45.2% | 50.1% | 0.5% | **33** | **48** |
| Intel Corporation | `INTC` | 8.7 | 9.3 | 12.2% | 44.5 | 37.8% | 14.8% | 1.0% | **5** | **48** |
| SK hynix | `SKHYNIX` | 4.9 | 4.4 | 76.3% | 2.7 | 31.8% | 54.4% | 6.1% | **45** | **5** |
| SK hynix | `SKHY` | 4.9 | 4.4 | 76.3% | 2.7 | 31.8% | 54.4% | 6.1% | **45** | **5** |
| SamsungElec | `SAMSUNG` | 2.8 | 2.5 | 52.2% | 2.9 | 50.9% | 37.9% | 5.1% | **45** | **10** |
| Circle Internet Group, Inc. | `CRCL` | 7.4 | 6.4 | 4.9% | 58.0 | 31.7% | 25.8% | 1.0% | **43** | **33** |
| Coinbase Global, Inc. | `COIN` | 7.8 | 7.2 | -13.9% | 59.4 | 261.1% | 29.8% | 5.7% | **20** | **40** |
| SOFTBANK GROUP CORP | `SOFTBANK` | 3.5 | 6.8 | -11.6% | 16.4 | -14.5% | 6.9% | -7.9% | **0** | **40** |
| CoreWeave, Inc. | `CRWV` | 4.9 | 10.9 | -1.9% | -36.6 | 15.5% | 104.6% | -24.5% | **0** | **40** |
| Dell Technologies Inc. | `DELL` | 1.9 | 2.3 | 12.0% | 15.3 | 9.6% | 18.4% | 2.1% | **33** | **38** |
| Meta Platforms, Inc. | `META` | 8.2 | 8.3 | 34.8% | 21.4 | 10.5% | 20.7% | 1.1% | **17** | **38** |
| Amazon.com, Inc. | `AMZN` | 3.5 | 3.7 | 13.7% | 24.2 | -18.2% | 14.6% | 0.1% | **0** | **38** |
| Arm Holdings plc | `ARM` | 49.6 | 48.6 | 7.6% | 78.1 | 37.5% | 36.2% | 0.5% | **35** | **33** |
| Fluence Energy, Inc. | `FLNC` | 0.5 | 0.4 | -8.9% | -13.7 | 60.4% | 27.7% | 0.2% | **5** | **28** |
| Hyperliquid Strategies Inc | `PURR` | 284.0 | 183.5 | 9595.1% | 26.1 | 51.0% | 31.4% | — | **25** | **10** |
| BitMine Immersion Technologies, | `BMNR` | 228.1 | 213.8 | 8.4% | 24.6 | 103.2% | 421.8% | -3.7% | **25** | **25** |
| Strategy Inc | `MSTR` | 125.9 | 148.1 | -6808.1% | 3.0 | 157.6% | 2.2% | -36.0% | **25** | **25** |
| QUALCOMM Incorporated | `QCOM` | 4.3 | 4.3 | 18.5% | 17.3 | -2.7% | 4.7% | 5.4% | **25** | **15** |
| Applied Optoelectronics, Inc. | `AAOI` | 11.5 | 11.9 | -12.9% | 17.5 | 576.8% | 156.5% | -12.9% | **10** | **25** |
| Alphabet Inc. | `GOOGL` | 9.6 | 9.3 | 34.0% | 22.9 | -26.9% | 24.4% | 0.5% | **12** | **23** |

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
