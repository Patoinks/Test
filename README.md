# OKX Long / Short Fundamental Scanner

Hourly scanner restricted to public companies exposed by the **OKX EEA TradFi / Stock Perpetual API universe**.

**Last scan:** 2026-10-12 19:35 UTC  
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
| 1 | Taiwan Semiconductor Manufactur | TSM | -1.7% | -8.2% | -4.9% | 82 | +4 | **86** | **CORE** | yes |
| 2 | NVIDIA Corporation | NVDA | -1.1% | -5.1% | -3.1% | 82 | +3 | **85** | **CORE** | yes |
| 3 | Applied Materials, Inc. | AMAT | -1.7% | -8.1% | -4.9% | 81 | +4 | **85** | **CORE** | yes |
| 4 | Applovin Corporation | APP | -1.8% | -3.5% | -2.6% | 82 | +2 | **84** | **CORE** | yes |
| 5 | Sandisk Corporation | SNDK | -5.5% | -12.3% | -8.9% | 77 | +7 | **84** | **CORE** | yes |
| 6 | Broadcom Inc. | AVGO | -1.7% | -2.0% | -1.9% | 82 | +1 | **83** | **CORE** | yes |
| 7 | Advanced Micro Devices, Inc. | AMD | -2.5% | -6.1% | -4.3% | 79 | +3 | **82** | **CORE** | yes |
| 8 | Marvell Technology, Inc. | MRVL | -2.6% | -1.2% | -1.9% | 79 | +2 | **81** | **CORE** | yes |
| 9 | Oracle Corporation | ORCL | -2.8% | -3.5% | -3.2% | 78 | +3 | **81** | **CORE** | yes |
| 10 | Micron Technology, Inc. | MU | -3.7% | -6.9% | -5.3% | 77 | +4 | **81** | **CORE** | yes |

## Final model + Price Timing — SHORT

| Rank | Company | OKX | 24h | 7d | 50/50 move | Base SHORT | Timing adj. | Final | Signal | Prev. SHORT? |
|---:|---|---|---:|---:|---:|---:|---:|---:|---|---|
| 1 | Rocket Lab Corporation | RKLB | -3.5% | -9.8% | -6.7% | 100 | -5 | **95** | **CORE** | yes |
| 2 | USA Rare Earth, Inc. | USAR | -5.6% | -13.2% | -9.4% | 100 | -8 | **92** | **CORE** | yes |
| 3 | Cerebras Systems Inc. | CBRS | -10.0% | -18.6% | -14.3% | 98 | -11 | **87** | **CORE** | yes |
| 4 | IonQ, Inc. | IONQ | -9.0% | -15.5% | -12.3% | 91 | -10 | **81** | **CORE** | yes |
| 5 | Nebius Group N.V. | NBIS | -5.3% | -10.0% | -7.7% | 87 | -6 | **81** | **CORE** | yes |
| 6 | AST SpaceMobile, Inc. | ASTS | 1.0% | -12.0% | -5.5% | 80 | -4 | **76** | **CORE** | yes |
| 7 | Moderna, Inc. | MRNA | -5.6% | 4.5% | -0.6% | 72 | +0 | **72** | **WATCH** | yes |
| 8 | Okta, Inc. | OKTA | -2.2% | 4.0% | 0.9% | 61 | +1 | **62** | **WATCH** | yes |
| 9 | IREN LIMITED | IREN | -0.1% | -13.2% | -6.6% | 64 | -5 | **59** | **WATCH** | yes |
| 10 | Lumentum Holdings Inc. | LITE | -10.3% | -9.3% | -9.8% | 63 | -8 | **55** | **WATCH** | yes |

## Combined model — LONG

Weighted score: **70% fundamental + 30% P/E trend**.

| Rank | Company | OKX | Fundamental LONG | P/E trend LONG | Combined | Signal |
|---:|---|---|---:|---:|---:|---|
| 1 | Applovin Corporation | `APP` | 83 | 80 | **82** | **CORE** |
| 2 | Taiwan Semiconductor Manufactur | `TSM` | 82 | 81 | **82** | **CORE** |
| 3 | NVIDIA Corporation | `NVDA` | 75 | 100 | **82** | **CORE** |
| 4 | Broadcom Inc. | `AVGO` | 75 | 100 | **82** | **CORE** |
| 5 | Applied Materials, Inc. | `AMAT` | 77 | 91 | **81** | **CORE** |
| 6 | Advanced Micro Devices, Inc. | `AMD` | 70 | 100 | **79** | **CORE** |
| 7 | Marvell Technology, Inc. | `MRVL` | 70 | 100 | **79** | **CORE** |
| 8 | Oracle Corporation | `ORCL` | 70 | 95 | **78** | **CORE** |
| 9 | Sandisk Corporation | `SNDK` | 75 | 82 | **77** | **CORE** |
| 10 | Micron Technology, Inc. | `MU` | 75 | 82 | **77** | **CORE** |

## Combined model — SHORT

Weighted score: **70% fundamental + 30% P/E trend**.

| Rank | Company | OKX | Fundamental SHORT | P/E trend SHORT | Combined | Signal |
|---:|---|---|---:|---:|---:|---|
| 1 | Rocket Lab Corporation | `RKLB` | 100 | 0 | **100** | **CORE** |
| 2 | USA Rare Earth, Inc. | `USAR` | 100 | 0 | **100** | **CORE** |
| 3 | Cerebras Systems Inc. | `CBRS` | 98 | 0 | **98** | **CORE** |
| 4 | IonQ, Inc. | `IONQ` | 91 | 0 | **91** | **CORE** |
| 5 | Nebius Group N.V. | `NBIS` | 87 | 0 | **87** | **CORE** |
| 6 | AST SpaceMobile, Inc. | `ASTS` | 80 | 0 | **80** | **WATCH** |
| 7 | Moderna, Inc. | `MRNA` | 72 | 0 | **72** | **WATCH** |
| 8 | Okta, Inc. | `OKTA` | 80 | 18 | **61** | **WATCH** |

## P/E Compression + Growth — LONG

| Rank | Company | OKX | Trail P/E | Fwd P/E | P/E change | EPS +1y | Rev +1y | Rev trend | LONG score | Signal |
|---:|---|---|---:|---:|---:|---:|---:|---|---:|---|
| 1 | NVIDIA Corporation | `NVDA` | 28.7 | 14.2 | -50.3% | 70.9% | 68.2% | decelerating | **100** | **CORE** |
| 2 | Broadcom Inc. | `AVGO` | 45.4 | 18.3 | -59.6% | 66.4% | 64.1% | decelerating | **100** | **CORE** |
| 3 | Advanced Micro Devices, Inc. | `AMD` | 151.3 | 37.7 | -75.1% | 107.2% | 74.6% | accelerating | **100** | **CORE** |
| 4 | Marvell Technology, Inc. | `MRVL` | 88.2 | 36.8 | -58.3% | 72.6% | 63.1% | accelerating | **100** | **CORE** |
| 5 | Credo Technology Group Holding  | `CRDO` | 71.7 | 20.9 | -70.9% | 53.7% | 54.8% | decelerating | **96** | **CORE** |
| 6 | AXT Inc | `AXT` | 1561.8 | 27.8 | -98.2% | 159.2% | 111.3% | decelerating | **96** | **CORE** |
| 7 | Corning Incorporated | `GLW` | 67.1 | 33.5 | -50.1% | 33.0% | 19.6% | accelerating | **96** | **CORE** |
| 8 | Oracle Corporation | `ORCL` | 21.5 | 12.5 | -42.0% | 35.1% | 45.7% | accelerating | **95** | **CORE** |
| 9 | Applied Materials, Inc. | `AMAT` | 43.0 | 27.0 | -37.3% | 44.5% | 34.9% | accelerating | **91** | **CORE** |
| 10 | Coherent Corp. | `COHR` | 69.8 | 20.5 | -70.7% | 49.1% | 38.8% | decelerating | **91** | **CORE** |

## P/E Expansion + Weakening — SHORT

| Rank | Company | OKX | Trail P/E | Fwd P/E | P/E change | EPS +1y | Rev +1y | Rev trend | SHORT score | Signal |
|---:|---|---|---:|---:|---:|---:|---:|---|---:|---|
| 1 | SOFTBANK GROUP CORP | `SOFTBANK` | 6.8 | 19.7 | 191.0% | -14.5% | 6.9% | decelerating | **86** | **CORE** |
| 2 | Alphabet Inc. | `GOOGL` | 17.7 | 23.2 | 31.0% | -27.3% | 23.6% | decelerating | **70** | **CORE** |
| 3 | Hyperliquid Strategies Inc | `PURR` | 3.2 | 28.1 | 767.6% | 51.0% | 31.4% | decelerating | **55** | **WATCH** |
| 4 | Amazon.com, Inc. | `AMZN` | 20.9 | 24.8 | 18.8% | -18.3% | 14.5% | decelerating | **52** | **WATCH** |

## Top SHORT candidates

| Rank | Company | OKX market | SHORT score | Signal | P/S | EV/S | Op margin | Fwd P/E | Rev +1y | FCF yield |
|---:|---|---|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Rocket Lab Corporation | `RKLB-USDT-SWAP` | **100** | **CORE** | 54.7 | 50.2 | -24.6% | 1118.0 | 41.3% | -0.6% |
| 2 | USA Rare Earth, Inc. | `USAR-USDT-SWAP` | **100** | **CORE** | 337.8 | 118.2 | -795.6% | 395.0 | 870.1% | -6.4% |
| 3 | Cerebras Systems Inc. | `CBRS-USDT-SWAP` | **98** | **CORE** | 51.6 | 47.8 | -265.0% | 116.0 | 232.7% | — |
| 4 | IonQ, Inc. | `IONQ-USDT-SWAP` | **91** | **CORE** | 59.7 | 53.3 | -408.2% | -28.1 | 79.0% | -0.6% |
| 5 | Nebius Group N.V. | `NBIS-USDT-SWAP` | **87** | **CORE** | 39.2 | 46.3 | -0.2% | -58.8 | 268.0% | -18.1% |
| 6 | Okta, Inc. | `OKTA-USDT-SWAP` | **80** | **CORE** | 12.9 | 12.5 | 13.3% | 51.8 | 10.0% | 2.6% |
| 7 | AST SpaceMobile, Inc. | `ASTS-USDT-SWAP` | **80** | **WATCH** | 173.7 | 143.0 | -544.6% | -40.0 | 259.9% | -9.0% |
| 8 | Moderna, Inc. | `MRNA-USDT-SWAP` | **72** | **WATCH** | 38.0 | 38.6 | -557.9% | -47.8 | 16.1% | 0.4% |
| 9 | Tesla, Inc. | `TSLA-USDT-SWAP` | **63** | **WATCH** | 14.4 | 14.3 | 1.4% | 173.4 | 13.6% | 0.3% |

## Top LONG candidates

| Rank | Company | OKX market | LONG score | Signal | P/S | EV/S | Op margin | Fwd P/E | Rev +1y | FCF yield |
|---:|---|---|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Applovin Corporation | `APP-USDT-SWAP` | **83** | **CORE** | 13.3 | 13.6 | 77.7% | 13.1 | 26.4% | 3.5% |
| 2 | Taiwan Semiconductor Manufactur | `TSM-USDT-SWAP` | **82** | **CORE** | 0.5 | 3.7 | 60.3% | 20.3 | 35.8% | 31.6% |
| 3 | Applied Materials, Inc. | `AMAT-USDT-SWAP` | **77** | **WATCH** | 12.8 | 13.0 | 33.7% | 27.0 | 34.9% | 0.8% |
| 4 | Micron Technology, Inc. | `MU-USDT-SWAP` | **75** | **CORE** | 8.4 | 8.5 | 80.7% | 4.8 | 16.5% | 2.6% |
| 5 | Broadcom Inc. | `AVGO-USDT-SWAP` | **75** | **WATCH** | 19.0 | 19.8 | 54.3% | 18.3 | 64.1% | 1.8% |
| 6 | Sandisk Corporation | `SNDK-USDT-SWAP` | **75** | **CORE** | 10.7 | 11.2 | 78.5% | 5.6 | 18.9% | 3.6% |
| 7 | Western Digital Corporation | `WDC-USDT-SWAP` | **75** | **WATCH** | 11.3 | 11.1 | 43.6% | 11.8 | 36.9% | 1.6% |
| 8 | NVIDIA Corporation | `NVDA-USDT-SWAP` | **75** | **WATCH** | 18.1 | 18.2 | 66.2% | 14.2 | 68.2% | 0.8% |
| 9 | Robinhood Markets, Inc. | `HOOD-USDT-SWAP` | **70** | **WATCH** | 19.8 | 19.7 | 43.9% | 31.6 | 28.9% | — |
| 10 | Marvell Technology, Inc. | `MRVL-USDT-SWAP` | **70** | **WATCH** | 25.5 | 25.7 | 16.7% | 36.8 | 63.1% | 1.0% |

## Analyst consensus (12-month price target) — most upside

| Rank | Company | OKX | Price | Analyst mean target | Gap | Analysts | Currency |
|---:|---|---|---:|---:|---:|---:|---|
| 1 | USA Rare Earth, Inc. | `USAR` | 11.86 | 35.56 | **199.9%** | 9 | USD |
| 2 | IREN LIMITED | `IREN` | 35.15 | 78.14 | **122.3%** | 18 | USD |
| 3 | Hyperliquid Strategies Inc | `PURR` | 10.41 | 22.32 | **114.5%** | 4 | USD |
| 4 | Cerebras Systems Inc. | `CBRS` | 147.76 | 291.64 | **97.4%** | 11 | USD |
| 5 | SK hynix | `SKHYNIX` | 1605000.00 | 3141024.80 | **95.7%** | 38 | KRW |
| 6 | BitMine Immersion Technologies, | `BMNR` | 23.88 | 45.87 | **92.1%** | 3 | USD |
| 7 | SamsungElec | `SAMSUNG` | 250500.00 | 478905.62 | **91.2%** | 36 | KRW |
| 8 | IonQ, Inc. | `IONQ` | 36.30 | 66.63 | **83.6%** | 14 | USD |
| 9 | Applovin Corporation | `APP` | 272.08 | 487.66 | **79.2%** | 31 | USD |
| 10 | CoreWeave, Inc. | `CRWV` | 81.04 | 141.47 | **74.6%** | 38 | USD |
| 11 | Oracle Corporation | `ORCL` | 137.46 | 237.97 | **73.1%** | 41 | USD |
| 12 | Western Digital Corporation | `WDC` | 388.78 | 670.79 | **72.5%** | 24 | USD |
| 13 | Applied Optoelectronics, Inc. | `AAOI` | 100.25 | 163.40 | **63.0%** | 5 | USD |
| 14 | Rocket Lab Corporation | `RKLB` | 65.83 | 106.33 | **61.5%** | 21 | USD |
| 15 | Micron Technology, Inc. | `MU` | 990.95 | 1555.13 | **56.9%** | 46 | USD |

## Analyst consensus (12-month price target) — most downside

| Rank | Company | OKX | Price | Analyst mean target | Gap | Analysts | Currency |
|---:|---|---|---:|---:|---:|---:|---|
| 1 | Moderna, Inc. | `MRNA` | 212.32 | 122.67 | **-42.2%** | 18 | USD |
| 2 | Okta, Inc. | `OKTA` | 226.96 | 212.60 | **-6.3%** | 43 | USD |
| 3 | Apple Inc. | `AAPL` | 340.66 | 328.09 | **-3.7%** | 39 | USD |
| 4 | Palantir Technologies Inc. | `PLTR` | 207.75 | 203.35 | **-2.1%** | 26 | USD |

Price/target uses the underlying Yahoo Finance share quote, not the OKX derivative. Minimum 3 analysts; unreliable price scales and missing coverage excluded. Targets are analyst opinions, not guaranteed forecasts.

## All OKX companies — our ratio + LONG/SHORT scores

| Company | OKX | P/S | EV/S | Op margin | Fwd P/E | EPS +1y | Rev +1y | FCF yield | LONG | SHORT |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Rocket Lab Corporation | `RKLB` | 54.7 | 50.2 | -24.6% | 1118.0 | 75.5% | 41.3% | -0.6% | **0** | **100 CORE** |
| USA Rare Earth, Inc. | `USAR` | 337.8 | 118.2 | -795.6% | 395.0 | 105.3% | 870.1% | -6.4% | **0** | **100 CORE** |
| Cerebras Systems Inc. | `CBRS` | 51.6 | 47.8 | -265.0% | 116.0 | 371.3% | 232.7% | — | **0** | **98 CORE** |
| IonQ, Inc. | `IONQ` | 59.7 | 53.3 | -408.2% | -28.1 | 18.1% | 79.0% | -0.6% | **0** | **91 CORE** |
| Nebius Group N.V. | `NBIS` | 39.2 | 46.3 | -0.2% | -58.8 | -191.4% | 268.0% | -18.1% | **0** | **87 CORE** |
| Applovin Corporation | `APP` | 13.3 | 13.6 | 77.7% | 13.1 | 27.5% | 26.4% | 3.5% | **83 CORE** | **10** |
| Taiwan Semiconductor Manufactur | `TSM` | 0.5 | 3.7 | 60.3% | 20.3 | 30.9% | 35.8% | 31.6% | **82 CORE** | **10** |
| Okta, Inc. | `OKTA` | 12.9 | 12.5 | 13.3% | 51.8 | 11.4% | 10.0% | 2.6% | **8** | **80 CORE** |
| AST SpaceMobile, Inc. | `ASTS` | 173.7 | 143.0 | -544.6% | -40.0 | 47.7% | 259.9% | -9.0% | **0** | **80 WATCH** |
| Applied Materials, Inc. | `AMAT` | 12.8 | 13.0 | 33.7% | 27.0 | 44.5% | 34.9% | 0.8% | **77 WATCH** | **13** |
| NVIDIA Corporation | `NVDA` | 18.1 | 18.2 | 66.2% | 14.2 | 70.9% | 68.2% | 0.8% | **75 WATCH** | **18** |
| Sandisk Corporation | `SNDK` | 10.7 | 11.2 | 78.5% | 5.6 | 24.0% | 18.9% | 3.6% | **75 CORE** | **10** |
| Broadcom Inc. | `AVGO` | 19.0 | 19.8 | 54.3% | 18.3 | 66.4% | 64.1% | 1.8% | **75 WATCH** | **28** |
| Micron Technology, Inc. | `MU` | 8.4 | 8.5 | 80.7% | 4.8 | 17.1% | 16.5% | 2.6% | **75 CORE** | **30** |
| Western Digital Corporation | `WDC` | 11.3 | 11.1 | 43.6% | 11.8 | 58.2% | 36.9% | 1.6% | **75 WATCH** | **18** |
| Moderna, Inc. | `MRNA` | 38.0 | 38.6 | -557.9% | -47.8 | 43.0% | 16.1% | 0.4% | **0** | **72 WATCH** |
| Advanced Micro Devices, Inc. | `AMD` | 23.4 | 23.8 | 17.2% | 37.7 | 107.2% | 74.6% | 0.9% | **70 WATCH** | **13** |
| Oracle Corporation | `ORCL` | 5.8 | 7.9 | 35.6% | 12.5 | 35.1% | 45.7% | -11.0% | **70 WATCH** | **10** |
| Marvell Technology, Inc. | `MRVL` | 25.5 | 25.7 | 16.7% | 36.8 | 72.6% | 63.1% | 1.0% | **70 WATCH** | **13** |
| Robinhood Markets, Inc. | `HOOD` | 19.8 | 19.7 | 43.9% | 31.6 | 35.9% | 28.9% | — | **70 WATCH** | **5** |
| XIAOMI-W | `XIAOMI` | 1.4 | 1.3 | 4.0% | 16.0 | 38.8% | 22.3% | -1.4% | **70 WATCH** | **10** |
| Credo Technology Group Holding  | `CRDO` | 23.9 | 25.1 | 25.2% | 20.9 | 53.7% | 54.8% | 0.7% | **67 WATCH** | **28** |
| Adobe Inc. | `ADBE` | 3.6 | 3.7 | 34.8% | 8.6 | 13.0% | 9.2% | 10.1% | **65 WATCH** | **30** |
| IREN LIMITED | `IREN` | 19.6 | 22.4 | -102.5% | -8.8 | -16.4% | 160.9% | -30.5% | **0** | **64** |
| Tesla, Inc. | `TSLA` | 14.4 | 14.3 | 1.4% | 173.4 | 24.8% | 13.6% | 0.3% | **22** | **63 WATCH** |
| Lumentum Holdings Inc. | `LITE` | 29.8 | 32.5 | 28.0% | 27.8 | 63.4% | 56.4% | 0.3% | **0** | **63** |
| Corning Incorporated | `GLW` | 7.4 | 8.4 | 15.6% | 33.5 | 33.0% | 19.6% | 0.6% | **60 WATCH** | **13** |
| Microsoft Corporation | `MSFT` | 12.1 | 12.1 | 45.1% | 22.8 | 19.8% | 19.6% | 0.4% | **59 WATCH** | **23** |
| Dell Technologies Inc. | `DELL` | 2.4 | 2.6 | 12.0% | 19.6 | 0.8% | 16.5% | 1.7% | **25** | **58** |
| Coca-Cola Company (The) | `KO` | 7.7 | 8.2 | 34.9% | 25.4 | 6.7% | 0.1% | 1.4% | **7** | **58** |
| Apple Inc. | `AAPL` | 10.6 | 10.6 | 32.6% | 35.5 | 8.6% | 10.5% | 2.2% | **5** | **58** |
| Bloom Energy Corporation | `BE` | 24.8 | 26.6 | 17.1% | 53.1 | 82.0% | 64.4% | 0.7% | **55 WATCH** | **48** |
| AXT Inc | `AXT` | 32.6 | 33.0 | 21.9% | 27.8 | 159.2% | 111.3% | -1.1% | **52** | **35** |
| Coherent Corp. | `COHR` | 8.0 | 8.9 | 11.8% | 20.5 | 49.1% | 38.8% | -1.1% | **52** | **35** |
| Super Micro Computer, Inc. | `SMCI` | 0.7 | 0.9 | 13.4% | 7.5 | 22.8% | 17.3% | -32.0% | **52** | **25** |
| Netflix, Inc. | `NFLX` | 6.1 | 6.2 | 33.4% | 18.6 | 6.1% | 11.2% | 8.6% | **35** | **50** |
| Palantir Technologies Inc. | `PLTR` | 81.1 | 80.1 | 47.1% | 88.6 | 45.2% | 49.8% | 0.4% | **33** | **48** |
| Intel Corporation | `INTC` | 9.4 | 9.9 | 12.2% | 48.6 | 36.9% | 14.8% | 0.9% | **5** | **48** |
| SK hynix | `SKHYNIX` | 6.0 | 6.0 | 76.3% | 3.4 | 32.4% | 54.4% | 4.9% | **45** | **5** |
| SK hynix | `SKHY` | 6.0 | 6.0 | 76.3% | 3.4 | 32.4% | 54.4% | 4.9% | **45** | **5** |
| SamsungElec | `SAMSUNG` | 3.4 | 3.2 | 52.2% | 3.5 | 50.8% | 37.6% | 4.2% | **45** | **10** |
| Circle Internet Group, Inc. | `CRCL` | 7.3 | 6.8 | 4.9% | 57.6 | 31.2% | 25.1% | 1.0% | **43** | **33** |
| Coinbase Global, Inc. | `COIN` | 7.8 | 7.5 | -13.9% | 58.5 | 268.1% | 29.6% | 5.7% | **20** | **40** |
| SOFTBANK GROUP CORP | `SOFTBANK` | 4.1 | 7.5 | -11.6% | 19.7 | -14.5% | 6.9% | -6.6% | **0** | **40** |
| CoreWeave, Inc. | `CRWV` | 5.9 | 12.0 | -1.9% | -44.2 | 15.4% | 104.3% | -20.3% | **0** | **40** |
| Meta Platforms, Inc. | `META` | 8.3 | 8.1 | 34.8% | 21.5 | 9.7% | 20.6% | 1.1% | **17** | **38** |
| Alphabet Inc. | `GOOGL` | 9.7 | 9.4 | 34.0% | 23.2 | -27.3% | 23.6% | 0.5% | **2** | **38** |
| Amazon.com, Inc. | `AMZN` | 3.6 | 3.8 | 13.7% | 24.8 | -18.3% | 14.5% | 0.1% | **0** | **38** |
| Arm Holdings plc | `ARM` | 52.8 | 54.5 | 7.6% | 83.2 | 37.5% | 36.2% | 0.5% | **35** | **33** |
| Applied Optoelectronics, Inc. | `AAOI` | 14.3 | 15.2 | -12.9% | 21.8 | 576.8% | 156.5% | -10.4% | **0** | **35** |
| Fluence Energy, Inc. | `FLNC` | 0.5 | 0.5 | -8.9% | -26.7 | 70.1% | 35.3% | 0.2% | **5** | **28** |
| Hyperliquid Strategies Inc | `PURR` | 306.2 | 217.8 | 9595.1% | 28.1 | 51.0% | 31.4% | — | **25** | **10** |
| Strategy Inc | `MSTR` | 121.9 | 156.6 | -6808.1% | 3.1 | 157.6% | 2.2% | -37.2% | **25** | **25** |
| BitMine Immersion Technologies, | `BMNR` | 235.3 | 231.3 | 8.4% | 25.4 | 103.2% | 421.8% | -3.6% | **25** | **25** |
| QUALCOMM Incorporated | `QCOM` | 4.2 | 4.3 | 18.5% | 17.1 | -2.7% | 4.8% | 5.5% | **25** | **15** |

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
