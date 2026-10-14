# OKX Long / Short Fundamental Scanner

Hourly scanner restricted to public companies exposed by the **OKX EEA TradFi / Stock Perpetual API universe**.

**Last scan:** 2026-10-14 13:48 UTC  
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
| 1 | Taiwan Semiconductor Manufactur | TSM | -1.3% | -7.0% | -4.2% | 88 | +3 | **91** | **CORE** | yes |
| 2 | Credo Technology Group Holding  | CRDO | -3.4% | -13.0% | -8.2% | 82 | +7 | **89** | **CORE** | yes |
| 3 | Applied Materials, Inc. | AMAT | -2.1% | -12.7% | -7.4% | 81 | +6 | **87** | **CORE** | yes |
| 4 | Broadcom Inc. | AVGO | -1.5% | -6.5% | -4.0% | 82 | +3 | **85** | **CORE** | yes |
| 5 | NVIDIA Corporation | NVDA | -1.2% | -4.9% | -3.1% | 82 | +2 | **84** | **CORE** | yes |
| 6 | Applovin Corporation | APP | -1.1% | -4.3% | -2.7% | 82 | +2 | **84** | **CORE** | yes |
| 7 | Marvell Technology, Inc. | MRVL | -3.2% | -8.7% | -6.0% | 79 | +5 | **84** | **CORE** | yes |
| 8 | Advanced Micro Devices, Inc. | AMD | -2.7% | -8.8% | -5.8% | 79 | +5 | **84** | **CORE** | yes |
| 9 | Oracle Corporation | ORCL | -6.3% | -6.6% | -6.4% | 78 | +5 | **83** | **CORE** | yes |
| 10 | Sandisk Corporation | SNDK | -1.8% | -14.0% | -7.9% | 77 | +6 | **83** | **CORE** | yes |

## Final model + Price Timing — SHORT

| Rank | Company | OKX | 24h | 7d | 50/50 move | Base SHORT | Timing adj. | Final | Signal | Prev. SHORT? |
|---:|---|---|---:|---:|---:|---:|---:|---:|---|---|
| 1 | Rocket Lab Corporation | RKLB | -1.4% | -11.9% | -6.7% | 100 | -5 | **95** | **CORE** | yes |
| 2 | USA Rare Earth, Inc. | USAR | -3.1% | -17.4% | -10.2% | 100 | -8 | **92** | **CORE** | yes |
| 3 | Cerebras Systems Inc. | CBRS | -3.8% | -18.1% | -10.9% | 98 | -9 | **89** | **CORE** | yes |
| 4 | IonQ, Inc. | IONQ | -4.9% | -20.1% | -12.5% | 88 | -10 | **78** | **CORE** | yes |
| 5 | Moderna, Inc. | MRNA | 1.5% | 11.7% | 6.6% | 72 | +5 | **77** | **CORE** | yes |
| 6 | Nebius Group N.V. | NBIS | -8.2% | -19.9% | -14.1% | 87 | -11 | **76** | **CORE** | yes |
| 7 | AST SpaceMobile, Inc. | ASTS | -5.1% | -26.4% | -15.8% | 80 | -13 | **67** | **WATCH** | yes |
| 8 | Okta, Inc. | OKTA | 0.4% | 4.4% | 2.4% | 61 | +2 | **63** | **WATCH** | yes |
| 9 | IREN LIMITED | IREN | -7.2% | -16.5% | -11.8% | 64 | -9 | **55** | **WATCH** | yes |

## Combined model — LONG

Weighted score: **70% fundamental + 30% P/E trend**.

| Rank | Company | OKX | Fundamental LONG | P/E trend LONG | Combined | Signal |
|---:|---|---|---:|---:|---:|---|
| 1 | Taiwan Semiconductor Manufactur | `TSM` | 90 | 85 | **88** | **CORE** |
| 2 | Applovin Corporation | `APP` | 83 | 80 | **82** | **CORE** |
| 3 | Credo Technology Group Holding  | `CRDO` | 75 | 100 | **82** | **CORE** |
| 4 | Broadcom Inc. | `AVGO` | 75 | 100 | **82** | **CORE** |
| 5 | NVIDIA Corporation | `NVDA` | 75 | 100 | **82** | **CORE** |
| 6 | Applied Materials, Inc. | `AMAT` | 77 | 91 | **81** | **CORE** |
| 7 | Advanced Micro Devices, Inc. | `AMD` | 70 | 100 | **79** | **CORE** |
| 8 | Marvell Technology, Inc. | `MRVL` | 70 | 100 | **79** | **CORE** |
| 9 | Oracle Corporation | `ORCL` | 70 | 95 | **78** | **CORE** |
| 10 | Micron Technology, Inc. | `MU` | 75 | 82 | **77** | **CORE** |

## Combined model — SHORT

Weighted score: **70% fundamental + 30% P/E trend**.

| Rank | Company | OKX | Fundamental SHORT | P/E trend SHORT | Combined | Signal |
|---:|---|---|---:|---:|---:|---|
| 1 | Rocket Lab Corporation | `RKLB` | 100 | 0 | **100** | **CORE** |
| 2 | USA Rare Earth, Inc. | `USAR` | 100 | 0 | **100** | **CORE** |
| 3 | Cerebras Systems Inc. | `CBRS` | 98 | 0 | **98** | **CORE** |
| 4 | IonQ, Inc. | `IONQ` | 88 | 0 | **88** | **CORE** |
| 5 | Nebius Group N.V. | `NBIS` | 87 | 0 | **87** | **CORE** |
| 6 | AST SpaceMobile, Inc. | `ASTS` | 80 | 0 | **80** | **WATCH** |
| 7 | Moderna, Inc. | `MRNA` | 72 | 0 | **72** | **WATCH** |
| 8 | Okta, Inc. | `OKTA` | 80 | 18 | **61** | **WATCH** |

## P/E Compression + Growth — LONG

| Rank | Company | OKX | Trail P/E | Fwd P/E | P/E change | EPS +1y | Rev +1y | Rev trend | LONG score | Signal |
|---:|---|---|---:|---:|---:|---:|---:|---|---:|---|
| 1 | Credo Technology Group Holding  | `CRDO` | 67.9 | 19.8 | -70.9% | 53.7% | 54.8% | decelerating | **100** | **CORE** |
| 2 | Broadcom Inc. | `AVGO` | 44.9 | 18.1 | -59.6% | 66.4% | 64.1% | decelerating | **100** | **CORE** |
| 3 | NVIDIA Corporation | `NVDA` | 28.5 | 14.2 | -50.3% | 70.9% | 68.2% | decelerating | **100** | **CORE** |
| 4 | Advanced Micro Devices, Inc. | `AMD` | 150.3 | 37.5 | -75.1% | 107.2% | 74.6% | accelerating | **100** | **CORE** |
| 5 | Marvell Technology, Inc. | `MRVL` | 82.5 | 35.7 | -56.7% | 72.9% | 63.2% | accelerating | **100** | **CORE** |
| 6 | Corning Incorporated | `GLW` | 66.7 | 33.3 | -50.1% | 33.0% | 19.6% | accelerating | **96** | **CORE** |
| 7 | AXT Inc | `AXT` | 1583.0 | 28.1 | -98.2% | 159.2% | 111.3% | decelerating | **96** | **CORE** |
| 8 | Oracle Corporation | `ORCL` | 21.0 | 12.2 | -42.0% | 35.1% | 45.7% | accelerating | **95** | **CORE** |
| 9 | Coherent Corp. | `COHR` | 67.8 | 19.9 | -70.7% | 49.2% | 38.9% | decelerating | **95** | **CORE** |
| 10 | Applied Materials, Inc. | `AMAT` | 39.2 | 24.6 | -37.2% | 44.4% | 35.2% | accelerating | **91** | **CORE** |

## P/E Expansion + Weakening — SHORT

| Rank | Company | OKX | Trail P/E | Fwd P/E | P/E change | EPS +1y | Rev +1y | Rev trend | SHORT score | Signal |
|---:|---|---|---:|---:|---:|---:|---:|---|---:|---|
| 1 | SOFTBANK GROUP CORP | `SOFTBANK` | 6.2 | 18.1 | 191.0% | -14.5% | 6.9% | decelerating | **86** | **CORE** |
| 2 | Alphabet Inc. | `GOOGL` | 18.0 | 23.4 | 30.1% | -26.9% | 24.1% | accelerating | **60** | **WATCH** |
| 3 | Hyperliquid Strategies Inc | `PURR` | 3.1 | 27.3 | 767.6% | 51.0% | 31.4% | decelerating | **55** | **WATCH** |
| 4 | Amazon.com, Inc. | `AMZN` | 20.9 | 24.8 | 18.9% | -18.3% | 14.5% | decelerating | **52** | **WATCH** |

## Top SHORT candidates

| Rank | Company | OKX market | SHORT score | Signal | P/S | EV/S | Op margin | Fwd P/E | Rev +1y | FCF yield |
|---:|---|---|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Rocket Lab Corporation | `RKLB-USDT-SWAP` | **100** | **CORE** | 52.6 | 47.1 | -24.6% | 974.5 | 41.3% | -0.6% |
| 2 | USA Rare Earth, Inc. | `USAR-USDT-SWAP` | **100** | **CORE** | 311.5 | 94.4 | -795.6% | 364.3 | 870.1% | -6.9% |
| 3 | Cerebras Systems Inc. | `CBRS-USDT-SWAP` | **98** | **CORE** | 50.1 | 42.6 | -265.0% | 112.6 | 232.7% | — |
| 4 | IonQ, Inc. | `IONQ-USDT-SWAP` | **88** | **CORE** | 54.3 | 45.4 | -408.2% | -25.6 | 79.0% | -0.7% |
| 5 | Nebius Group N.V. | `NBIS-USDT-SWAP` | **87** | **CORE** | 35.6 | 43.4 | -0.2% | -53.4 | 268.0% | -19.9% |
| 6 | Okta, Inc. | `OKTA-USDT-SWAP` | **80** | **CORE** | 12.9 | 12.2 | 13.3% | 52.0 | 10.0% | 2.6% |
| 7 | AST SpaceMobile, Inc. | `ASTS-USDT-SWAP` | **80** | **WATCH** | 150.7 | 132.9 | -544.6% | -34.7 | 247.3% | -10.4% |
| 8 | Moderna, Inc. | `MRNA-USDT-SWAP` | **72** | **WATCH** | 39.3 | 37.0 | -557.9% | -49.5 | 16.1% | 0.3% |
| 9 | Tesla, Inc. | `TSLA-USDT-SWAP` | **63** | **WATCH** | 14.0 | 14.0 | 1.4% | 168.9 | 13.6% | 0.3% |

## Top LONG candidates

| Rank | Company | OKX market | LONG score | Signal | P/S | EV/S | Op margin | Fwd P/E | Rev +1y | FCF yield |
|---:|---|---|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Taiwan Semiconductor Manufactur | `TSM-USDT-SWAP` | **90** | **CORE** | 0.5 | 3.6 | 60.3% | 19.7 | 35.9% | 32.1% |
| 2 | Applovin Corporation | `APP-USDT-SWAP` | **83** | **CORE** | 13.2 | 13.4 | 77.7% | 13.1 | 26.0% | 3.5% |
| 3 | Applied Materials, Inc. | `AMAT-USDT-SWAP` | **77** | **WATCH** | 11.7 | 11.9 | 33.7% | 24.6 | 35.2% | 0.9% |
| 4 | Credo Technology Group Holding  | `CRDO-USDT-SWAP` | **75** | **WATCH** | 22.6 | 23.0 | 25.2% | 19.8 | 54.8% | 0.7% |
| 5 | Broadcom Inc. | `AVGO-USDT-SWAP` | **75** | **WATCH** | 18.9 | 19.5 | 54.3% | 18.1 | 64.1% | 1.8% |
| 6 | Micron Technology, Inc. | `MU-USDT-SWAP` | **75** | **CORE** | 8.0 | 7.8 | 80.7% | 4.6 | 15.7% | 2.7% |
| 7 | Sandisk Corporation | `SNDK-USDT-SWAP` | **75** | **CORE** | 10.4 | 10.5 | 78.5% | 5.5 | 18.9% | 3.7% |
| 8 | NVIDIA Corporation | `NVDA-USDT-SWAP` | **75** | **WATCH** | 18.0 | 18.1 | 66.2% | 14.2 | 68.2% | 0.8% |
| 9 | Western Digital Corporation | `WDC-USDT-SWAP` | **75** | **WATCH** | 10.9 | 10.6 | 43.6% | 11.4 | 36.8% | 1.6% |
| 10 | Robinhood Markets, Inc. | `HOOD-USDT-SWAP` | **70** | **WATCH** | 19.7 | 20.0 | 43.9% | 31.5 | 29.2% | — |

## Analyst consensus (12-month price target) — most upside

| Rank | Company | OKX | Price | Analyst mean target | Gap | Analysts | Currency |
|---:|---|---|---:|---:|---:|---:|---|
| 1 | IREN LIMITED | `IREN` | 32.30 | 78.14 | **141.9%** | 18 | USD |
| 2 | SK hynix | `SKHYNIX` | 1419000.00 | 3141024.80 | **121.4%** | 38 | KRW |
| 3 | Hyperliquid Strategies Inc | `PURR` | 10.09 | 22.32 | **121.3%** | 4 | USD |
| 4 | CoreWeave, Inc. | `CRWV` | 67.91 | 141.47 | **108.3%** | 38 | USD |
| 5 | SamsungElec | `SAMSUNG` | 232000.00 | 478905.62 | **106.4%** | 36 | KRW |
| 6 | Cerebras Systems Inc. | `CBRS` | 143.43 | 291.64 | **103.3%** | 11 | USD |
| 7 | IonQ, Inc. | `IONQ` | 33.04 | 66.63 | **101.7%** | 14 | USD |
| 8 | BitMine Immersion Technologies, | `BMNR` | 22.96 | 45.87 | **99.8%** | 3 | USD |
| 9 | Applovin Corporation | `APP` | 269.21 | 480.08 | **78.3%** | 31 | USD |
| 10 | Oracle Corporation | `ORCL` | 134.14 | 237.97 | **77.4%** | 41 | USD |
| 11 | Western Digital Corporation | `WDC` | 377.40 | 668.50 | **77.1%** | 24 | USD |
| 12 | Applied Optoelectronics, Inc. | `AAOI` | 93.64 | 163.40 | **74.5%** | 5 | USD |
| 13 | AST SpaceMobile, Inc. | `ASTS` | 44.65 | 74.28 | **66.3%** | 12 | USD |
| 14 | Rocket Lab Corporation | `RKLB` | 63.33 | 105.05 | **65.9%** | 19 | USD |
| 15 | Micron Technology, Inc. | `MU` | 945.26 | 1560.57 | **65.1%** | 46 | USD |

## Analyst consensus (12-month price target) — most downside

| Rank | Company | OKX | Price | Analyst mean target | Gap | Analysts | Currency |
|---:|---|---|---:|---:|---:|---:|---|
| 1 | Moderna, Inc. | `MRNA` | 219.56 | 122.67 | **-44.1%** | 18 | USD |
| 2 | Okta, Inc. | `OKTA` | 227.50 | 212.60 | **-6.5%** | 43 | USD |
| 3 | Apple Inc. | `AAPL` | 346.31 | 329.38 | **-4.9%** | 39 | USD |
| 4 | Palantir Technologies Inc. | `PLTR` | 208.93 | 205.27 | **-1.8%** | 26 | USD |

Price/target uses the underlying Yahoo Finance share quote, not the OKX derivative. Minimum 3 analysts; unreliable price scales and missing coverage excluded. Targets are analyst opinions, not guaranteed forecasts.

## All OKX companies — our ratio + LONG/SHORT scores

| Company | OKX | P/S | EV/S | Op margin | Fwd P/E | EPS +1y | Rev +1y | FCF yield | LONG | SHORT |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Rocket Lab Corporation | `RKLB` | 52.6 | 47.1 | -24.6% | 974.5 | 75.5% | 41.3% | -0.6% | **0** | **100 CORE** |
| USA Rare Earth, Inc. | `USAR` | 311.5 | 94.4 | -795.6% | 364.3 | 105.3% | 870.1% | -6.9% | **0** | **100 CORE** |
| Cerebras Systems Inc. | `CBRS` | 50.1 | 42.6 | -265.0% | 112.6 | 371.3% | 232.7% | — | **0** | **98 CORE** |
| Taiwan Semiconductor Manufactur | `TSM` | 0.5 | 3.6 | 60.3% | 19.7 | 30.9% | 35.9% | 32.1% | **90 CORE** | **10** |
| IonQ, Inc. | `IONQ` | 54.3 | 45.4 | -408.2% | -25.6 | 18.1% | 79.0% | -0.7% | **0** | **88 CORE** |
| Nebius Group N.V. | `NBIS` | 35.6 | 43.4 | -0.2% | -53.4 | -191.4% | 268.0% | -19.9% | **0** | **87 CORE** |
| Applovin Corporation | `APP` | 13.2 | 13.4 | 77.7% | 13.1 | 27.3% | 26.0% | 3.5% | **83 CORE** | **10** |
| Okta, Inc. | `OKTA` | 12.9 | 12.2 | 13.3% | 52.0 | 11.4% | 10.0% | 2.6% | **8** | **80 CORE** |
| AST SpaceMobile, Inc. | `ASTS` | 150.7 | 132.9 | -544.6% | -34.7 | 44.3% | 247.3% | -10.4% | **0** | **80 WATCH** |
| Applied Materials, Inc. | `AMAT` | 11.7 | 11.9 | 33.7% | 24.6 | 44.4% | 35.2% | 0.9% | **77 WATCH** | **3** |
| Credo Technology Group Holding  | `CRDO` | 22.6 | 23.0 | 25.2% | 19.8 | 53.7% | 54.8% | 0.7% | **75 WATCH** | **28** |
| Broadcom Inc. | `AVGO` | 18.9 | 19.5 | 54.3% | 18.1 | 66.4% | 64.1% | 1.8% | **75 WATCH** | **28** |
| NVIDIA Corporation | `NVDA` | 18.0 | 18.1 | 66.2% | 14.2 | 70.9% | 68.2% | 0.8% | **75 WATCH** | **18** |
| Micron Technology, Inc. | `MU` | 8.0 | 7.8 | 80.7% | 4.6 | 17.1% | 15.7% | 2.7% | **75 CORE** | **30** |
| Sandisk Corporation | `SNDK` | 10.4 | 10.5 | 78.5% | 5.5 | 24.0% | 18.9% | 3.7% | **75 CORE** | **10** |
| Western Digital Corporation | `WDC` | 10.9 | 10.6 | 43.6% | 11.4 | 60.4% | 36.8% | 1.6% | **75 WATCH** | **18** |
| Moderna, Inc. | `MRNA` | 39.3 | 37.0 | -557.9% | -49.5 | 43.0% | 16.1% | 0.3% | **0** | **72 WATCH** |
| Advanced Micro Devices, Inc. | `AMD` | 23.3 | 23.7 | 17.2% | 37.5 | 107.2% | 74.6% | 0.9% | **70 WATCH** | **13** |
| Marvell Technology, Inc. | `MRVL` | 24.7 | 25.1 | 16.7% | 35.7 | 72.9% | 63.2% | 1.0% | **70 WATCH** | **13** |
| Oracle Corporation | `ORCL` | 5.7 | 7.9 | 35.6% | 12.2 | 35.1% | 45.7% | -11.3% | **70 WATCH** | **10** |
| Robinhood Markets, Inc. | `HOOD` | 19.7 | 20.0 | 43.9% | 31.5 | 36.4% | 29.2% | — | **70 WATCH** | **5** |
| XIAOMI-W | `XIAOMI` | 1.6 | 1.3 | 4.0% | 17.2 | 38.8% | 22.3% | -1.3% | **70 WATCH** | **10** |
| Adobe Inc. | `ADBE` | 3.6 | 3.6 | 34.8% | 8.7 | 12.9% | 9.1% | 10.0% | **65 WATCH** | **30** |
| IREN LIMITED | `IREN` | 18.0 | 22.1 | -102.5% | -8.1 | -16.4% | 160.9% | -33.1% | **0** | **64** |
| Tesla, Inc. | `TSLA` | 14.0 | 14.0 | 1.4% | 168.9 | 24.5% | 13.6% | 0.3% | **22** | **63 WATCH** |
| Coherent Corp. | `COHR` | 7.7 | 8.2 | 11.8% | 19.9 | 49.2% | 38.9% | -1.2% | **60 WATCH** | **35** |
| Corning Incorporated | `GLW` | 7.4 | 8.0 | 15.6% | 33.3 | 33.0% | 19.6% | 0.6% | **60 WATCH** | **13** |
| Microsoft Corporation | `MSFT` | 12.2 | 12.3 | 45.1% | 23.0 | 19.8% | 19.6% | 0.4% | **59 WATCH** | **23** |
| Lumentum Holdings Inc. | `LITE` | 28.5 | 29.0 | 28.0% | 26.3 | 65.3% | 57.0% | 0.3% | **0** | **59** |
| Coca-Cola Company (The) | `KO` | 7.8 | 8.3 | 34.9% | 25.7 | 6.7% | 0.1% | 1.3% | **7** | **58** |
| Apple Inc. | `AAPL` | 10.8 | 10.7 | 32.6% | 36.1 | 8.6% | 10.5% | 2.1% | **5** | **58** |
| Bloom Energy Corporation | `BE` | 24.2 | 25.0 | 17.1% | 52.0 | 82.2% | 64.4% | 0.7% | **55 WATCH** | **48** |
| AXT Inc | `AXT` | 33.1 | 31.1 | 21.9% | 28.1 | 159.2% | 111.3% | -1.1% | **52** | **35** |
| Super Micro Computer, Inc. | `SMCI` | 0.6 | 0.8 | 13.4% | 7.0 | 22.8% | 17.3% | -34.3% | **52** | **25** |
| Netflix, Inc. | `NFLX` | 6.1 | 6.2 | 33.4% | 18.7 | 5.9% | 11.2% | 8.6% | **35** | **50** |
| Palantir Technologies Inc. | `PLTR` | 81.6 | 80.0 | 47.1% | 89.1 | 45.2% | 50.1% | 0.4% | **33** | **48** |
| Intel Corporation | `INTC` | 9.4 | 9.7 | 12.2% | 48.3 | 37.2% | 14.9% | 0.9% | **5** | **48** |
| SK hynix | `SKHYNIX` | 5.3 | 5.1 | 76.3% | 3.0 | 32.4% | 54.4% | 5.5% | **45** | **5** |
| SK hynix | `SKHY` | 5.3 | 5.1 | 76.3% | 3.0 | 32.4% | 54.4% | 5.5% | **45** | **5** |
| SamsungElec | `SAMSUNG` | 3.1 | 2.8 | 52.2% | 3.2 | 50.9% | 38.0% | 4.6% | **45** | **10** |
| Circle Internet Group, Inc. | `CRCL` | 7.3 | 6.8 | 4.9% | 56.7 | 31.7% | 25.8% | 1.0% | **43** | **33** |
| Coinbase Global, Inc. | `COIN` | 7.9 | 7.6 | -13.9% | 60.0 | 261.3% | 29.8% | 5.6% | **20** | **40** |
| SOFTBANK GROUP CORP | `SOFTBANK` | 3.8 | 7.1 | -11.6% | 18.1 | -14.5% | 6.9% | -7.2% | **0** | **40** |
| CoreWeave, Inc. | `CRWV` | 4.9 | 11.7 | -1.9% | -37.0 | 15.4% | 104.3% | -24.3% | **0** | **40** |
| Dell Technologies Inc. | `DELL` | 2.2 | 2.6 | 12.0% | 17.8 | 9.6% | 18.4% | 1.8% | **33** | **38** |
| Meta Platforms, Inc. | `META` | 8.4 | 8.6 | 34.8% | 21.7 | 10.4% | 20.7% | 1.1% | **17** | **38** |
| Amazon.com, Inc. | `AMZN` | 3.6 | 3.8 | 13.7% | 24.8 | -18.3% | 14.5% | 0.1% | **0** | **38** |
| Arm Holdings plc | `ARM` | 50.9 | 52.2 | 7.6% | 80.3 | 37.5% | 36.2% | 0.5% | **35** | **33** |
| Fluence Energy, Inc. | `FLNC` | 0.5 | 0.4 | -8.9% | -24.6 | 70.1% | 35.3% | 0.2% | **5** | **28** |
| Hyperliquid Strategies Inc | `PURR` | 296.8 | 199.4 | 9595.1% | 27.3 | 51.0% | 31.4% | — | **25** | **10** |
| Strategy Inc | `MSTR` | 128.2 | 155.0 | -6808.1% | 3.0 | 157.6% | 2.2% | -35.3% | **25** | **25** |
| BitMine Immersion Technologies, | `BMNR` | 226.3 | 226.0 | 8.4% | 24.4 | 103.2% | 421.8% | -3.7% | **25** | **25** |
| QUALCOMM Incorporated | `QCOM` | 4.2 | 4.4 | 18.5% | 17.2 | -2.7% | 4.8% | 5.5% | **25** | **15** |
| Applied Optoelectronics, Inc. | `AAOI` | 13.3 | 13.5 | -12.9% | 20.3 | 576.8% | 156.5% | -11.2% | **2** | **25** |
| Alphabet Inc. | `GOOGL` | 9.8 | 9.5 | 34.0% | 23.4 | -26.9% | 24.1% | 0.5% | **12** | **23** |

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
