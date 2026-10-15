# OKX Long / Short Fundamental Scanner

Hourly scanner restricted to public companies exposed by the **OKX EEA TradFi / Stock Perpetual API universe**.

**Last scan:** 2026-10-15 22:25 UTC  
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
| 1 | Taiwan Semiconductor Manufactur | TSM | -1.8% | -7.8% | -4.8% | 88 | +4 | **92** | **CORE** | yes |
| 2 | Applied Materials, Inc. | AMAT | -3.7% | -15.6% | -9.7% | 81 | +8 | **89** | **CORE** | yes |
| 3 | Credo Technology Group Holding  | CRDO | -0.4% | -15.7% | -8.1% | 82 | +6 | **88** | **CORE** | yes |
| 4 | NVIDIA Corporation | NVDA | -1.8% | -5.7% | -3.8% | 82 | +3 | **85** | **CORE** | yes |
| 5 | Marvell Technology, Inc. | MRVL | -1.6% | -12.2% | -6.9% | 79 | +6 | **85** | **CORE** | yes |
| 6 | Broadcom Inc. | AVGO | -0.6% | -4.4% | -2.5% | 82 | +2 | **84** | **CORE** | yes |
| 7 | Advanced Micro Devices, Inc. | AMD | -1.5% | -9.4% | -5.5% | 79 | +4 | **83** | **CORE** | yes |
| 8 | Sandisk Corporation | SNDK | -0.6% | -13.3% | -7.0% | 77 | +6 | **83** | **CORE** | yes |
| 9 | Corning Incorporated | GLW | -1.7% | -9.4% | -5.6% | 78 | +4 | **82** | **CORE** | yes |
| 10 | Western Digital Corporation | WDC | -2.1% | -9.4% | -5.7% | 76 | +5 | **81** | **CORE** | yes |

## Final model + Price Timing — SHORT

| Rank | Company | OKX | 24h | 7d | 50/50 move | Base SHORT | Timing adj. | Final | Signal | Prev. SHORT? |
|---:|---|---|---:|---:|---:|---:|---:|---:|---|---|
| 1 | USA Rare Earth, Inc. | USAR | 7.5% | -12.2% | -2.4% | 100 | -2 | **98** | **CORE** | yes |
| 2 | Rocket Lab Corporation | RKLB | -6.6% | -19.2% | -12.9% | 100 | -10 | **90** | **CORE** | yes |
| 3 | Moderna, Inc. | MRNA | 4.5% | 20.1% | 12.3% | 80 | +10 | **90** | **CORE** | yes |
| 4 | IonQ, Inc. | IONQ | 9.3% | -12.9% | -1.8% | 88 | -1 | **87** | **CORE** | yes |
| 5 | Cerebras Systems Inc. | CBRS | 0.5% | -15.3% | -7.4% | 92 | -6 | **86** | **CORE** | yes |
| 6 | Nebius Group N.V. | NBIS | 1.3% | -14.2% | -6.5% | 84 | -5 | **79** | **CORE** | yes |
| 7 | AST SpaceMobile, Inc. | ASTS | 5.5% | -21.9% | -8.2% | 80 | -7 | **73** | **WATCH** | yes |
| 8 | Okta, Inc. | OKTA | -1.6% | -5.3% | -3.5% | 60 | -3 | **57** | **WATCH** | yes |

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
| 7 | Marvell Technology, Inc. | `MRVL` | 70 | 100 | **79** | **CORE** |
| 8 | Advanced Micro Devices, Inc. | `AMD` | 70 | 100 | **79** | **CORE** |
| 9 | Corning Incorporated | `GLW` | 70 | 96 | **78** | **CORE** |
| 10 | Oracle Corporation | `ORCL` | 70 | 95 | **78** | **CORE** |

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
| 1 | Credo Technology Group Holding  | `CRDO` | 70.0 | 18.4 | -73.7% | 53.7% | 54.8% | decelerating | **100** | **CORE** |
| 2 | NVIDIA Corporation | `NVDA` | 28.4 | 13.6 | -51.9% | 70.9% | 68.2% | decelerating | **100** | **CORE** |
| 3 | Marvell Technology, Inc. | `MRVL` | 76.6 | 33.1 | -56.7% | 72.9% | 63.2% | accelerating | **100** | **CORE** |
| 4 | Broadcom Inc. | `AVGO` | 45.4 | 17.8 | -60.9% | 66.4% | 64.2% | decelerating | **100** | **CORE** |
| 5 | Advanced Micro Devices, Inc. | `AMD` | 152.0 | 35.7 | -76.5% | 107.7% | 74.8% | accelerating | **100** | **CORE** |
| 6 | Corning Incorporated | `GLW` | 66.9 | 31.7 | -52.6% | 33.0% | 19.6% | accelerating | **96** | **CORE** |
| 7 | AXT Inc | `AXT` | 1447.8 | 25.7 | -98.2% | 159.2% | 111.3% | decelerating | **96** | **CORE** |
| 8 | Coherent Corp. | `COHR` | 67.0 | 17.8 | -73.4% | 49.2% | 38.9% | decelerating | **95** | **CORE** |
| 9 | Oracle Corporation | `ORCL` | 23.1 | 12.2 | -47.1% | 35.1% | 45.7% | accelerating | **95** | **CORE** |
| 10 | Arm Holdings plc | `ARM` | 272.0 | 79.9 | -70.6% | 37.5% | 36.2% | accelerating | **95** | **CORE** |

## P/E Expansion + Weakening — SHORT

| Rank | Company | OKX | Trail P/E | Fwd P/E | P/E change | EPS +1y | Rev +1y | Rev trend | SHORT score | Signal |
|---:|---|---|---:|---:|---:|---:|---:|---|---:|---|
| 1 | SOFTBANK GROUP CORP | `SOFTBANK` | 6.2 | 16.4 | 163.8% | -14.5% | 6.9% | decelerating | **86** | **CORE** |
| 2 | Hyperliquid Strategies Inc | `PURR` | 3.3 | 26.5 | 705.4% | 51.0% | 31.4% | decelerating | **55** | **WATCH** |
| 3 | Amazon.com, Inc. | `AMZN` | 20.9 | 24.4 | 16.8% | -18.2% | 14.6% | decelerating | **52** | **WATCH** |
| 4 | Alphabet Inc. | `GOOGL` | 17.8 | 22.9 | 28.4% | -26.9% | 24.4% | accelerating | **50** | **WATCH** |

## Top SHORT candidates

| Rank | Company | OKX market | SHORT score | Signal | P/S | EV/S | Op margin | Fwd P/E | Rev +1y | FCF yield |
|---:|---|---|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Rocket Lab Corporation | `RKLB-USDT-SWAP` | **100** | **CORE** | 45.9 | 43.2 | -24.6% | 850.1 | 40.8% | -0.7% |
| 2 | USA Rare Earth, Inc. | `USAR-USDT-SWAP` | **100** | **CORE** | 316.0 | 76.6 | -795.6% | 369.7 | 870.1% | -6.8% |
| 3 | Cerebras Systems Inc. | `CBRS-USDT-SWAP` | **92** | **CORE** | 49.6 | 39.9 | -265.0% | 111.6 | 232.7% | — |
| 4 | IonQ, Inc. | `IONQ-USDT-SWAP` | **88** | **CORE** | 56.5 | 40.2 | -408.2% | -25.6 | 77.6% | -0.6% |
| 5 | Nebius Group N.V. | `NBIS-USDT-SWAP` | **84** | **WATCH** | 35.3 | 39.2 | -0.2% | -53.0 | 268.0% | -20.1% |
| 6 | Okta, Inc. | `OKTA-USDT-SWAP` | **80** | **CORE** | 11.9 | 11.3 | 13.3% | 47.6 | 10.0% | 2.8% |
| 7 | AST SpaceMobile, Inc. | `ASTS-USDT-SWAP` | **80** | **WATCH** | 150.1 | 120.1 | -544.6% | -34.6 | 247.3% | -10.4% |
| 8 | Moderna, Inc. | `MRNA-USDT-SWAP` | **80** | **WATCH** | 42.4 | 38.8 | -557.9% | -53.3 | 16.1% | 0.3% |
| 9 | Tesla, Inc. | `TSLA-USDT-SWAP` | **63** | **WATCH** | 13.8 | 13.7 | 1.4% | 167.1 | 13.5% | 0.3% |

## Top LONG candidates

| Rank | Company | OKX market | LONG score | Signal | P/S | EV/S | Op margin | Fwd P/E | Rev +1y | FCF yield |
|---:|---|---|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Taiwan Semiconductor Manufactur | `TSM-USDT-SWAP` | **90** | **CORE** | 0.5 | 3.5 | 60.3% | 18.6 | 35.2% | 33.4% |
| 2 | Applovin Corporation | `APP-USDT-SWAP` | **83** | **CORE** | 13.7 | 12.9 | 77.7% | 13.6 | 26.0% | 3.4% |
| 3 | Applied Materials, Inc. | `AMAT-USDT-SWAP` | **77** | **WATCH** | 11.1 | 11.4 | 33.7% | 23.3 | 35.2% | 0.9% |
| 4 | Credo Technology Group Holding  | `CRDO-USDT-SWAP` | **75** | **WATCH** | 21.1 | 20.7 | 25.2% | 18.4 | 54.8% | 0.7% |
| 5 | Micron Technology, Inc. | `MU-USDT-SWAP` | **75** | **CORE** | 7.9 | 7.5 | 80.7% | 4.6 | 15.5% | 2.8% |
| 6 | Broadcom Inc. | `AVGO-USDT-SWAP` | **75** | **WATCH** | 18.4 | 18.9 | 54.3% | 17.8 | 64.2% | 1.9% |
| 7 | Sandisk Corporation | `SNDK-USDT-SWAP` | **75** | **CORE** | 10.0 | 9.9 | 78.5% | 5.2 | 18.9% | 3.8% |
| 8 | NVIDIA Corporation | `NVDA-USDT-SWAP` | **75** | **WATCH** | 17.3 | 17.5 | 66.2% | 13.6 | 68.2% | 0.8% |
| 9 | Western Digital Corporation | `WDC-USDT-SWAP` | **75** | **WATCH** | 10.3 | 10.1 | 43.6% | 10.8 | 37.2% | 1.7% |
| 10 | Corning Incorporated | `GLW-USDT-SWAP` | **70** | **WATCH** | 7.0 | 7.6 | 15.6% | 31.7 | 19.6% | 0.6% |

## Analyst consensus (12-month price target) — most upside

| Rank | Company | OKX | Price | Analyst mean target | Gap | Analysts | Currency |
|---:|---|---|---:|---:|---:|---:|---|
| 1 | IREN LIMITED | `IREN` | 30.39 | 78.14 | **157.1%** | 18 | USD |
| 2 | SK hynix | `SKHYNIX` | 1262000.00 | 3141024.80 | **148.9%** | 38 | KRW |
| 3 | SamsungElec | `SAMSUNG` | 210000.00 | 478905.62 | **128.1%** | 36 | KRW |
| 4 | Hyperliquid Strategies Inc | `PURR` | 9.80 | 22.32 | **127.8%** | 4 | USD |
| 5 | Cerebras Systems Inc. | `CBRS` | 142.17 | 291.64 | **105.1%** | 11 | USD |
| 6 | CoreWeave, Inc. | `CRWV` | 69.69 | 140.76 | **102.0%** | 38 | USD |
| 7 | BitMine Immersion Technologies, | `BMNR` | 23.36 | 45.87 | **96.3%** | 3 | USD |
| 8 | Applied Optoelectronics, Inc. | `AAOI` | 83.73 | 163.40 | **95.2%** | 5 | USD |
| 9 | Western Digital Corporation | `WDC` | 356.45 | 668.50 | **87.5%** | 24 | USD |
| 10 | Rocket Lab Corporation | `RKLB` | 55.25 | 103.39 | **87.1%** | 18 | USD |
| 11 | IonQ, Inc. | `IONQ` | 34.35 | 64.06 | **86.5%** | 14 | USD |
| 12 | Oracle Corporation | `ORCL` | 134.47 | 237.97 | **77.0%** | 41 | USD |
| 13 | Applovin Corporation | `APP` | 279.29 | 480.08 | **71.9%** | 31 | USD |
| 14 | Micron Technology, Inc. | `MU` | 931.24 | 1560.57 | **67.6%** | 46 | USD |
| 15 | AST SpaceMobile, Inc. | `ASTS` | 44.46 | 74.28 | **67.1%** | 12 | USD |

## Analyst consensus (12-month price target) — most downside

| Rank | Company | OKX | Price | Analyst mean target | Gap | Analysts | Currency |
|---:|---|---|---:|---:|---:|---:|---|
| 1 | Moderna, Inc. | `MRNA` | 236.50 | 123.61 | **-47.7%** | 18 | USD |
| 2 | Apple Inc. | `AAPL` | 342.00 | 329.38 | **-3.7%** | 39 | USD |

Price/target uses the underlying Yahoo Finance share quote, not the OKX derivative. Minimum 3 analysts; unreliable price scales and missing coverage excluded. Targets are analyst opinions, not guaranteed forecasts.

## All OKX companies — our ratio + LONG/SHORT scores

| Company | OKX | P/S | EV/S | Op margin | Fwd P/E | EPS +1y | Rev +1y | FCF yield | LONG | SHORT |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| USA Rare Earth, Inc. | `USAR` | 316.0 | 76.6 | -795.6% | 369.7 | 105.3% | 870.1% | -6.8% | **0** | **100 CORE** |
| Rocket Lab Corporation | `RKLB` | 45.9 | 43.2 | -24.6% | 850.1 | 69.1% | 40.8% | -0.7% | **0** | **100 CORE** |
| Cerebras Systems Inc. | `CBRS` | 49.6 | 39.9 | -265.0% | 111.6 | 371.3% | 232.7% | — | **0** | **92 CORE** |
| Taiwan Semiconductor Manufactur | `TSM` | 0.5 | 3.5 | 60.3% | 18.6 | 27.9% | 35.2% | 33.4% | **90 CORE** | **10** |
| IonQ, Inc. | `IONQ` | 56.5 | 40.2 | -408.2% | -25.6 | 17.5% | 77.6% | -0.6% | **0** | **88 CORE** |
| Nebius Group N.V. | `NBIS` | 35.3 | 39.2 | -0.2% | -53.0 | -191.4% | 268.0% | -20.1% | **0** | **84 WATCH** |
| Applovin Corporation | `APP` | 13.7 | 12.9 | 77.7% | 13.6 | 27.3% | 26.0% | 3.4% | **83 CORE** | **10** |
| Okta, Inc. | `OKTA` | 11.9 | 11.3 | 13.3% | 47.6 | 11.4% | 10.0% | 2.8% | **8** | **80 CORE** |
| Moderna, Inc. | `MRNA` | 42.4 | 38.8 | -557.9% | -53.3 | 43.0% | 16.1% | 0.3% | **0** | **80 WATCH** |
| AST SpaceMobile, Inc. | `ASTS` | 150.1 | 120.1 | -544.6% | -34.6 | 44.3% | 247.3% | -10.4% | **0** | **80 WATCH** |
| Applied Materials, Inc. | `AMAT` | 11.1 | 11.4 | 33.7% | 23.3 | 44.4% | 35.2% | 0.9% | **77 WATCH** | **3** |
| Credo Technology Group Holding  | `CRDO` | 21.1 | 20.7 | 25.2% | 18.4 | 53.7% | 54.8% | 0.7% | **75 WATCH** | **28** |
| NVIDIA Corporation | `NVDA` | 17.3 | 17.5 | 66.2% | 13.6 | 70.9% | 68.2% | 0.8% | **75 WATCH** | **18** |
| Broadcom Inc. | `AVGO` | 18.4 | 18.9 | 54.3% | 17.8 | 66.4% | 64.2% | 1.9% | **75 WATCH** | **28** |
| Sandisk Corporation | `SNDK` | 10.0 | 9.9 | 78.5% | 5.2 | 24.0% | 18.9% | 3.8% | **75 CORE** | **10** |
| Western Digital Corporation | `WDC` | 10.3 | 10.1 | 43.6% | 10.8 | 61.2% | 37.2% | 1.7% | **75 WATCH** | **18** |
| Micron Technology, Inc. | `MU` | 7.9 | 7.5 | 80.7% | 4.6 | 15.8% | 15.5% | 2.8% | **75 CORE** | **30** |
| Marvell Technology, Inc. | `MRVL` | 22.9 | 22.9 | 16.7% | 33.1 | 72.9% | 63.2% | 1.1% | **70 WATCH** | **13** |
| Advanced Micro Devices, Inc. | `AMD` | 22.2 | 22.3 | 17.2% | 35.7 | 107.7% | 74.8% | 1.0% | **70 WATCH** | **13** |
| Corning Incorporated | `GLW` | 7.0 | 7.6 | 15.6% | 31.7 | 33.0% | 19.6% | 0.6% | **70 WATCH** | **13** |
| Oracle Corporation | `ORCL` | 5.7 | 7.4 | 35.6% | 12.2 | 35.1% | 45.7% | -11.2% | **70 WATCH** | **10** |
| Robinhood Markets, Inc. | `HOOD` | 19.0 | 18.2 | 43.9% | 30.3 | 36.5% | 29.2% | — | **70 WATCH** | **5** |
| XIAOMI-W | `XIAOMI` | 1.6 | 1.4 | 4.0% | 17.7 | 38.8% | 22.3% | -1.2% | **70 WATCH** | **10** |
| Adobe Inc. | `ADBE` | 3.8 | 3.7 | 34.8% | 9.1 | 12.4% | 9.1% | 9.5% | **65 WATCH** | **30** |
| Tesla, Inc. | `TSLA` | 13.8 | 13.7 | 1.4% | 167.1 | 24.4% | 13.5% | 0.3% | **22** | **63 WATCH** |
| Coherent Corp. | `COHR` | 6.9 | 7.5 | 11.8% | 17.8 | 49.2% | 38.9% | -1.3% | **60 WATCH** | **35** |
| IREN LIMITED | `IREN` | 16.9 | 19.8 | -102.5% | -7.6 | -16.4% | 164.0% | -35.2% | **0** | **60** |
| Microsoft Corporation | `MSFT` | 12.1 | 12.1 | 45.1% | 22.8 | 19.9% | 19.6% | 0.4% | **59 WATCH** | **23** |
| Lumentum Holdings Inc. | `LITE` | 26.1 | 26.3 | 28.0% | 24.1 | 65.3% | 57.0% | 0.3% | **0** | **59** |
| Apple Inc. | `AAPL` | 10.7 | 10.8 | 32.6% | 35.7 | 8.5% | 10.4% | 2.2% | **5** | **58** |
| Coca-Cola Company (The) | `KO` | 7.9 | 8.5 | 34.9% | 26.1 | 6.6% | -0.1% | 1.3% | **0** | **58** |
| Bloom Energy Corporation | `BE` | 22.4 | 22.7 | 17.1% | 48.0 | 82.1% | 65.5% | 0.8% | **55 WATCH** | **48** |
| AXT Inc | `AXT` | 30.3 | 29.5 | 21.9% | 25.7 | 159.2% | 111.3% | -1.2% | **52** | **35** |
| Super Micro Computer, Inc. | `SMCI` | 0.6 | 0.8 | 13.4% | 6.6 | 22.8% | 17.3% | -36.3% | **52** | **25** |
| Netflix, Inc. | `NFLX` | 6.3 | 6.2 | 33.4% | 19.1 | 6.0% | 11.2% | 8.4% | **35** | **50** |
| Palantir Technologies Inc. | `PLTR` | 78.3 | 77.0 | 47.1% | 85.5 | 45.2% | 50.1% | 0.4% | **33** | **48** |
| Intel Corporation | `INTC` | 8.8 | 9.3 | 12.2% | 45.3 | 37.8% | 14.8% | 1.0% | **5** | **48** |
| SK hynix | `SKHYNIX` | 4.9 | 4.4 | 76.3% | 2.7 | 31.8% | 54.4% | 6.1% | **45** | **5** |
| SK hynix | `SKHY` | 4.9 | 4.4 | 76.3% | 2.7 | 31.8% | 54.4% | 6.1% | **45** | **5** |
| SamsungElec | `SAMSUNG` | 2.8 | 2.5 | 52.2% | 2.9 | 50.9% | 37.9% | 5.1% | **45** | **10** |
| Circle Internet Group, Inc. | `CRCL` | 7.6 | 6.4 | 4.9% | 59.2 | 31.7% | 25.8% | 0.9% | **43** | **33** |
| Coinbase Global, Inc. | `COIN` | 8.0 | 7.2 | -13.9% | 61.1 | 261.1% | 29.8% | 5.5% | **20** | **40** |
| SOFTBANK GROUP CORP | `SOFTBANK` | 3.5 | 6.8 | -11.6% | 16.4 | -14.5% | 6.9% | -7.9% | **0** | **40** |
| CoreWeave, Inc. | `CRWV` | 5.1 | 10.9 | -1.9% | -37.9 | 15.5% | 104.6% | -23.6% | **0** | **40** |
| Dell Technologies Inc. | `DELL` | 2.0 | 2.3 | 12.0% | 15.8 | 9.6% | 18.4% | 2.0% | **33** | **38** |
| Meta Platforms, Inc. | `META` | 8.2 | 8.3 | 34.8% | 21.3 | 10.5% | 20.7% | 1.1% | **17** | **38** |
| Amazon.com, Inc. | `AMZN` | 3.5 | 3.7 | 13.7% | 24.4 | -18.2% | 14.6% | 0.1% | **0** | **38** |
| Arm Holdings plc | `ARM` | 50.7 | 48.6 | 7.6% | 79.9 | 37.5% | 36.2% | 0.5% | **35** | **33** |
| Fluence Energy, Inc. | `FLNC` | 0.5 | 0.4 | -8.9% | -14.2 | 60.4% | 27.7% | 0.2% | **5** | **28** |
| Hyperliquid Strategies Inc | `PURR` | 288.3 | 183.5 | 9595.1% | 26.5 | 51.0% | 31.4% | — | **25** | **10** |
| BitMine Immersion Technologies, | `BMNR` | 230.3 | 213.8 | 8.4% | 24.9 | 103.2% | 421.8% | -3.7% | **25** | **25** |
| Strategy Inc | `MSTR` | 128.6 | 148.1 | -6808.1% | 3.1 | 157.6% | 2.2% | -35.3% | **25** | **25** |
| QUALCOMM Incorporated | `QCOM` | 4.3 | 4.3 | 18.5% | 17.5 | -2.7% | 4.7% | 5.4% | **25** | **15** |
| Applied Optoelectronics, Inc. | `AAOI` | 11.9 | 11.9 | -12.9% | 18.2 | 576.8% | 156.5% | -12.5% | **10** | **25** |
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
