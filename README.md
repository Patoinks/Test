# OKX Long / Short Fundamental Scanner

Hourly scanner restricted to public companies exposed by the **OKX EEA TradFi / Stock Perpetual API universe**.

**Last scan:** 2026-10-15 13:30 UTC  
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
| 1 | Taiwan Semiconductor Manufactur | TSM | -4.7% | -10.5% | -7.6% | 88 | +6 | **94** | **CORE** | yes |
| 2 | Sandisk Corporation | SNDK | -6.4% | -18.4% | -12.4% | 82 | +10 | **92** | **CORE** | yes |
| 3 | Credo Technology Group Holding  | CRDO | -5.0% | -19.7% | -12.3% | 82 | +10 | **92** | **CORE** | yes |
| 4 | Applied Materials, Inc. | AMAT | -3.1% | -15.0% | -9.1% | 81 | +7 | **88** | **CORE** | yes |
| 5 | Marvell Technology, Inc. | MRVL | -5.5% | -15.6% | -10.5% | 79 | +8 | **87** | **CORE** | yes |
| 6 | NVIDIA Corporation | NVDA | -2.7% | -6.6% | -4.6% | 82 | +4 | **86** | **CORE** | yes |
| 7 | Advanced Micro Devices, Inc. | AMD | -4.9% | -12.5% | -8.7% | 79 | +7 | **86** | **CORE** | yes |
| 8 | Broadcom Inc. | AVGO | -2.3% | -6.1% | -4.2% | 82 | +3 | **85** | **CORE** | yes |
| 9 | Robinhood Markets, Inc. | HOOD | -3.3% | -8.7% | -6.0% | 80 | +5 | **85** | **CORE** | yes |
| 10 | Micron Technology, Inc. | MU | -4.3% | -15.6% | -10.0% | 77 | +8 | **85** | **CORE** | yes |

## Final model + Price Timing — SHORT

| Rank | Company | OKX | 24h | 7d | 50/50 move | Base SHORT | Timing adj. | Final | Signal | Prev. SHORT? |
|---:|---|---|---:|---:|---:|---:|---:|---:|---|---|
| 1 | USA Rare Earth, Inc. | USAR | -3.6% | -21.2% | -12.4% | 100 | -10 | **90** | **CORE** | yes |
| 2 | Rocket Lab Corporation | RKLB | -8.1% | -20.5% | -14.3% | 100 | -11 | **89** | **CORE** | yes |
| 3 | Moderna, Inc. | MRNA | -1.0% | 13.7% | 6.4% | 80 | +5 | **85** | **CORE** | yes |
| 4 | Cerebras Systems Inc. | CBRS | -3.1% | -18.4% | -10.7% | 92 | -9 | **83** | **CORE** | yes |
| 5 | IonQ, Inc. | IONQ | -2.1% | -22.0% | -12.0% | 88 | -10 | **78** | **CORE** | yes |
| 6 | Nebius Group N.V. | NBIS | -5.5% | -20.0% | -12.8% | 84 | -10 | **74** | **WATCH** | yes |
| 7 | AST SpaceMobile, Inc. | ASTS | -2.4% | -27.8% | -15.1% | 80 | -12 | **68** | **WATCH** | yes |
| 8 | Okta, Inc. | OKTA | -3.9% | -7.6% | -5.7% | 60 | -5 | **55** | **WATCH** | yes |

## Combined model — LONG

Weighted score: **70% fundamental + 30% P/E trend**.

| Rank | Company | OKX | Fundamental LONG | P/E trend LONG | Combined | Signal |
|---:|---|---|---:|---:|---:|---|
| 1 | Taiwan Semiconductor Manufactur | `TSM` | 90 | 85 | **88** | **CORE** |
| 2 | Applovin Corporation | `APP` | 83 | 80 | **82** | **CORE** |
| 3 | Sandisk Corporation | `SNDK` | 82 | 82 | **82** | **CORE** |
| 4 | Credo Technology Group Holding  | `CRDO` | 75 | 100 | **82** | **CORE** |
| 5 | NVIDIA Corporation | `NVDA` | 75 | 100 | **82** | **CORE** |
| 6 | Broadcom Inc. | `AVGO` | 75 | 100 | **82** | **CORE** |
| 7 | Applied Materials, Inc. | `AMAT` | 77 | 91 | **81** | **CORE** |
| 8 | Robinhood Markets, Inc. | `HOOD` | 77 | 86 | **80** | **CORE** |
| 9 | Marvell Technology, Inc. | `MRVL` | 70 | 100 | **79** | **CORE** |
| 10 | Advanced Micro Devices, Inc. | `AMD` | 70 | 100 | **79** | **CORE** |

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
| 1 | Credo Technology Group Holding  | `CRDO` | 66.8 | 17.6 | -73.7% | 53.7% | 54.8% | decelerating | **100** | **CORE** |
| 2 | Marvell Technology, Inc. | `MRVL` | 73.6 | 31.8 | -56.7% | 72.9% | 63.2% | accelerating | **100** | **CORE** |
| 3 | NVIDIA Corporation | `NVDA` | 28.1 | 13.5 | -51.9% | 70.9% | 68.2% | decelerating | **100** | **CORE** |
| 4 | Advanced Micro Devices, Inc. | `AMD` | 146.7 | 34.5 | -76.5% | 107.7% | 74.8% | accelerating | **100** | **CORE** |
| 5 | Broadcom Inc. | `AVGO` | 44.6 | 17.4 | -60.9% | 66.4% | 64.1% | decelerating | **100** | **CORE** |
| 6 | Corning Incorporated | `GLW` | 65.3 | 30.9 | -52.6% | 33.0% | 19.6% | accelerating | **96** | **CORE** |
| 7 | AXT Inc | `AXT` | 1437.5 | 25.6 | -98.2% | 159.2% | 111.3% | decelerating | **96** | **CORE** |
| 8 | Coherent Corp. | `COHR` | 66.2 | 17.6 | -73.4% | 49.2% | 38.9% | decelerating | **95** | **CORE** |
| 9 | Oracle Corporation | `ORCL` | 22.2 | 11.7 | -47.1% | 35.1% | 45.7% | accelerating | **95** | **CORE** |
| 10 | Arm Holdings plc | `ARM` | 254.5 | 74.8 | -70.6% | 37.5% | 36.2% | accelerating | **95** | **CORE** |

## P/E Expansion + Weakening — SHORT

| Rank | Company | OKX | Trail P/E | Fwd P/E | P/E change | EPS +1y | Rev +1y | Rev trend | SHORT score | Signal |
|---:|---|---|---:|---:|---:|---:|---:|---|---:|---|
| 1 | SOFTBANK GROUP CORP | `SOFTBANK` | 5.6 | 16.4 | 191.0% | -14.5% | 6.9% | decelerating | **86** | **CORE** |
| 2 | Hyperliquid Strategies Inc | `PURR` | 3.0 | 24.3 | 705.4% | 51.0% | 31.4% | decelerating | **55** | **WATCH** |
| 3 | Amazon.com, Inc. | `AMZN` | 20.5 | 23.9 | 16.8% | -18.3% | 14.5% | decelerating | **52** | **WATCH** |
| 4 | Alphabet Inc. | `GOOGL` | 17.6 | 22.5 | 28.4% | -26.9% | 24.4% | accelerating | **50** | **WATCH** |

## Top SHORT candidates

| Rank | Company | OKX market | SHORT score | Signal | P/S | EV/S | Op margin | Fwd P/E | Rev +1y | FCF yield |
|---:|---|---|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Rocket Lab Corporation | `RKLB-USDT-SWAP` | **100** | **CORE** | 45.2 | 43.2 | -24.6% | 836.5 | 41.3% | -0.7% |
| 2 | USA Rare Earth, Inc. | `USAR-USDT-SWAP` | **100** | **CORE** | 283.5 | 76.6 | -795.6% | 331.0 | 870.1% | -7.6% |
| 3 | Cerebras Systems Inc. | `CBRS-USDT-SWAP` | **92** | **CORE** | 47.8 | 39.9 | -265.0% | 107.6 | 232.7% | — |
| 4 | IonQ, Inc. | `IONQ-USDT-SWAP` | **88** | **CORE** | 50.6 | 40.2 | -408.2% | -22.6 | 77.6% | -0.7% |
| 5 | Nebius Group N.V. | `NBIS-USDT-SWAP` | **84** | **WATCH** | 32.9 | 39.2 | -0.2% | -49.4 | 268.0% | -21.5% |
| 6 | Okta, Inc. | `OKTA-USDT-SWAP` | **80** | **CORE** | 11.6 | 11.3 | 13.3% | 46.5 | 10.0% | 2.9% |
| 7 | AST SpaceMobile, Inc. | `ASTS-USDT-SWAP` | **80** | **WATCH** | 138.8 | 120.1 | -544.6% | -32.0 | 247.3% | -11.2% |
| 8 | Moderna, Inc. | `MRNA-USDT-SWAP` | **80** | **WATCH** | 40.1 | 38.8 | -557.9% | -50.5 | 16.1% | 0.3% |
| 9 | Tesla, Inc. | `TSLA-USDT-SWAP` | **63** | **WATCH** | 13.7 | 13.7 | 1.4% | 166.2 | 13.5% | 0.3% |

## Top LONG candidates

| Rank | Company | OKX market | LONG score | Signal | P/S | EV/S | Op margin | Fwd P/E | Rev +1y | FCF yield |
|---:|---|---|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Taiwan Semiconductor Manufactur | `TSM-USDT-SWAP` | **90** | **CORE** | 0.5 | 3.5 | 60.3% | 18.3 | 35.2% | 34.4% |
| 2 | Applovin Corporation | `APP-USDT-SWAP` | **83** | **CORE** | 12.9 | 12.9 | 77.7% | 12.8 | 26.0% | 3.6% |
| 3 | Sandisk Corporation | `SNDK-USDT-SWAP` | **82** | **CORE** | 9.4 | 9.9 | 78.5% | 4.9 | 18.9% | 4.1% |
| 4 | Robinhood Markets, Inc. | `HOOD-USDT-SWAP` | **77** | **WATCH** | 17.8 | 18.2 | 43.9% | 28.5 | 29.2% | — |
| 5 | Applied Materials, Inc. | `AMAT-USDT-SWAP` | **77** | **WATCH** | 11.1 | 11.4 | 33.7% | 23.4 | 35.2% | 0.9% |
| 6 | Credo Technology Group Holding  | `CRDO-USDT-SWAP` | **75** | **WATCH** | 20.1 | 20.7 | 25.2% | 17.6 | 54.8% | 0.8% |
| 7 | Micron Technology, Inc. | `MU-USDT-SWAP` | **75** | **CORE** | 7.4 | 7.5 | 80.7% | 4.3 | 15.5% | 2.9% |
| 8 | Broadcom Inc. | `AVGO-USDT-SWAP` | **75** | **WATCH** | 18.1 | 18.9 | 54.3% | 17.4 | 64.1% | 1.9% |
| 9 | NVIDIA Corporation | `NVDA-USDT-SWAP` | **75** | **WATCH** | 17.2 | 17.5 | 66.2% | 13.5 | 68.2% | 0.8% |
| 10 | Western Digital Corporation | `WDC-USDT-SWAP` | **75** | **WATCH** | 10.0 | 10.1 | 43.6% | 10.5 | 37.2% | 1.8% |

## Analyst consensus (12-month price target) — most upside

| Rank | Company | OKX | Price | Analyst mean target | Gap | Analysts | Currency |
|---:|---|---|---:|---:|---:|---:|---|
| 1 | IREN LIMITED | `IREN` | 29.14 | 78.14 | **168.2%** | 18 | USD |
| 2 | SK hynix | `SKHYNIX` | 1262000.00 | 3141024.80 | **148.9%** | 38 | KRW |
| 3 | Hyperliquid Strategies Inc | `PURR` | 9.00 | 22.32 | **148.1%** | 4 | USD |
| 4 | CoreWeave, Inc. | `CRWV` | 61.95 | 141.47 | **128.3%** | 38 | USD |
| 5 | SamsungElec | `SAMSUNG` | 210000.00 | 478905.62 | **128.1%** | 36 | KRW |
| 6 | BitMine Immersion Technologies, | `BMNR` | 21.16 | 45.87 | **116.7%** | 3 | USD |
| 7 | Cerebras Systems Inc. | `CBRS` | 137.07 | 291.64 | **112.8%** | 11 | USD |
| 8 | IonQ, Inc. | `IONQ` | 30.77 | 64.06 | **108.2%** | 14 | USD |
| 9 | Applied Optoelectronics, Inc. | `AAOI` | 81.01 | 163.40 | **101.7%** | 5 | USD |
| 10 | Western Digital Corporation | `WDC` | 345.89 | 668.50 | **93.3%** | 24 | USD |
| 11 | Rocket Lab Corporation | `RKLB` | 54.37 | 105.05 | **93.2%** | 19 | USD |
| 12 | Oracle Corporation | `ORCL` | 129.19 | 237.97 | **84.2%** | 41 | USD |
| 13 | Applovin Corporation | `APP` | 263.28 | 480.08 | **82.3%** | 31 | USD |
| 14 | AST SpaceMobile, Inc. | `ASTS` | 41.13 | 74.28 | **80.6%** | 12 | USD |
| 15 | Micron Technology, Inc. | `MU` | 874.41 | 1560.57 | **78.5%** | 46 | USD |

## Analyst consensus (12-month price target) — most downside

| Rank | Company | OKX | Price | Analyst mean target | Gap | Analysts | Currency |
|---:|---|---|---:|---:|---:|---:|---|
| 1 | Moderna, Inc. | `MRNA` | 224.05 | 123.61 | **-44.8%** | 18 | USD |
| 2 | Apple Inc. | `AAPL` | 347.10 | 329.38 | **-5.1%** | 39 | USD |

Price/target uses the underlying Yahoo Finance share quote, not the OKX derivative. Minimum 3 analysts; unreliable price scales and missing coverage excluded. Targets are analyst opinions, not guaranteed forecasts.

## All OKX companies — our ratio + LONG/SHORT scores

| Company | OKX | P/S | EV/S | Op margin | Fwd P/E | EPS +1y | Rev +1y | FCF yield | LONG | SHORT |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| USA Rare Earth, Inc. | `USAR` | 283.5 | 76.6 | -795.6% | 331.0 | 105.3% | 870.1% | -7.6% | **0** | **100 CORE** |
| Rocket Lab Corporation | `RKLB` | 45.2 | 43.2 | -24.6% | 836.5 | 75.5% | 41.3% | -0.7% | **0** | **100 CORE** |
| Cerebras Systems Inc. | `CBRS` | 47.8 | 39.9 | -265.0% | 107.6 | 371.3% | 232.7% | — | **0** | **92 CORE** |
| Taiwan Semiconductor Manufactur | `TSM` | 0.5 | 3.5 | 60.3% | 18.3 | 27.9% | 35.2% | 34.4% | **90 CORE** | **10** |
| IonQ, Inc. | `IONQ` | 50.6 | 40.2 | -408.2% | -22.6 | 17.5% | 77.6% | -0.7% | **0** | **88 CORE** |
| Nebius Group N.V. | `NBIS` | 32.9 | 39.2 | -0.2% | -49.4 | -191.4% | 268.0% | -21.5% | **0** | **84 WATCH** |
| Applovin Corporation | `APP` | 12.9 | 12.9 | 77.7% | 12.8 | 27.3% | 26.0% | 3.6% | **83 CORE** | **10** |
| Sandisk Corporation | `SNDK` | 9.4 | 9.9 | 78.5% | 4.9 | 24.0% | 18.9% | 4.1% | **82 CORE** | **10** |
| Okta, Inc. | `OKTA` | 11.6 | 11.3 | 13.3% | 46.5 | 11.4% | 10.0% | 2.9% | **8** | **80 CORE** |
| Moderna, Inc. | `MRNA` | 40.1 | 38.8 | -557.9% | -50.5 | 43.0% | 16.1% | 0.3% | **0** | **80 WATCH** |
| AST SpaceMobile, Inc. | `ASTS` | 138.8 | 120.1 | -544.6% | -32.0 | 44.3% | 247.3% | -11.2% | **0** | **80 WATCH** |
| Applied Materials, Inc. | `AMAT` | 11.1 | 11.4 | 33.7% | 23.4 | 44.4% | 35.2% | 0.9% | **77 WATCH** | **3** |
| Robinhood Markets, Inc. | `HOOD` | 17.8 | 18.2 | 43.9% | 28.5 | 36.5% | 29.2% | — | **77 WATCH** | **5** |
| Credo Technology Group Holding  | `CRDO` | 20.1 | 20.7 | 25.2% | 17.6 | 53.7% | 54.8% | 0.8% | **75 WATCH** | **28** |
| NVIDIA Corporation | `NVDA` | 17.2 | 17.5 | 66.2% | 13.5 | 70.9% | 68.2% | 0.8% | **75 WATCH** | **18** |
| Micron Technology, Inc. | `MU` | 7.4 | 7.5 | 80.7% | 4.3 | 15.8% | 15.5% | 2.9% | **75 CORE** | **30** |
| Broadcom Inc. | `AVGO` | 18.1 | 18.9 | 54.3% | 17.4 | 66.4% | 64.1% | 1.9% | **75 WATCH** | **28** |
| Western Digital Corporation | `WDC` | 10.0 | 10.1 | 43.6% | 10.5 | 61.2% | 37.2% | 1.8% | **75 WATCH** | **18** |
| Marvell Technology, Inc. | `MRVL` | 22.0 | 22.9 | 16.7% | 31.8 | 72.9% | 63.2% | 1.2% | **70 WATCH** | **13** |
| Advanced Micro Devices, Inc. | `AMD` | 21.5 | 22.3 | 17.2% | 34.5 | 107.7% | 74.8% | 1.0% | **70 WATCH** | **13** |
| Corning Incorporated | `GLW` | 6.8 | 7.6 | 15.6% | 30.9 | 33.0% | 19.6% | 0.6% | **70 WATCH** | **13** |
| Oracle Corporation | `ORCL` | 5.5 | 7.4 | 35.6% | 11.7 | 35.1% | 45.7% | -11.7% | **70 WATCH** | **10** |
| XIAOMI-W | `XIAOMI` | 1.6 | 1.4 | 4.0% | 17.7 | 38.8% | 22.3% | -1.2% | **70 WATCH** | **10** |
| Adobe Inc. | `ADBE` | 3.7 | 3.7 | 34.8% | 8.9 | 12.4% | 9.1% | 9.8% | **65 WATCH** | **30** |
| Tesla, Inc. | `TSLA` | 13.7 | 13.7 | 1.4% | 166.2 | 24.4% | 13.5% | 0.3% | **22** | **63 WATCH** |
| Coherent Corp. | `COHR` | 6.8 | 7.5 | 11.8% | 17.6 | 49.2% | 38.9% | -1.3% | **60 WATCH** | **35** |
| IREN LIMITED | `IREN` | 16.2 | 19.8 | -102.5% | -7.3 | -16.4% | 160.9% | -36.8% | **0** | **60** |
| Microsoft Corporation | `MSFT` | 11.9 | 12.1 | 45.1% | 22.5 | 19.9% | 19.6% | 0.4% | **59 WATCH** | **23** |
| Lumentum Holdings Inc. | `LITE` | 25.4 | 26.3 | 28.0% | 23.5 | 65.3% | 57.0% | 0.3% | **0** | **59** |
| Coca-Cola Company (The) | `KO` | 8.0 | 8.5 | 34.9% | 26.5 | 6.7% | 0.1% | 1.3% | **7** | **58** |
| Apple Inc. | `AAPL` | 10.9 | 10.8 | 32.6% | 36.2 | 8.6% | 10.5% | 2.1% | **5** | **58** |
| Bloom Energy Corporation | `BE` | 21.3 | 22.7 | 17.1% | 45.8 | 82.1% | 65.5% | 0.8% | **55 WATCH** | **48** |
| AXT Inc | `AXT` | 30.0 | 29.5 | 21.9% | 25.6 | 159.2% | 111.3% | -1.2% | **52** | **35** |
| Super Micro Computer, Inc. | `SMCI` | 0.6 | 0.8 | 13.4% | 6.5 | 22.8% | 17.3% | -37.0% | **52** | **25** |
| Netflix, Inc. | `NFLX` | 6.2 | 6.2 | 33.4% | 18.8 | 5.9% | 11.2% | 8.5% | **35** | **50** |
| Palantir Technologies Inc. | `PLTR` | 76.4 | 77.0 | 47.1% | 83.4 | 45.2% | 50.1% | 0.5% | **33** | **48** |
| Intel Corporation | `INTC` | 8.7 | 9.3 | 12.2% | 44.6 | 37.8% | 14.8% | 1.0% | **5** | **48** |
| SK hynix | `SKHY` | 4.9 | 5.0 | 76.3% | 2.7 | 32.4% | 54.4% | 6.1% | **45** | **5** |
| SK hynix | `SKHYNIX` | 4.9 | 5.0 | 76.3% | 2.7 | 32.4% | 54.4% | 6.1% | **45** | **5** |
| SamsungElec | `SAMSUNG` | 2.8 | 2.8 | 52.2% | 2.9 | 50.9% | 38.0% | 5.1% | **45** | **10** |
| Arm Holdings plc | `ARM` | 47.4 | 48.6 | 7.6% | 74.8 | 37.5% | 36.2% | 0.5% | **43** | **33** |
| Circle Internet Group, Inc. | `CRCL` | 6.6 | 6.4 | 4.9% | 51.5 | 31.7% | 25.8% | 1.1% | **43** | **33** |
| Coinbase Global, Inc. | `COIN` | 7.4 | 7.2 | -13.9% | 56.0 | 261.1% | 29.8% | 6.0% | **20** | **40** |
| SOFTBANK GROUP CORP | `SOFTBANK` | 3.5 | 7.2 | -11.6% | 16.4 | -14.5% | 6.9% | -7.9% | **0** | **40** |
| CoreWeave, Inc. | `CRWV` | 4.5 | 10.9 | -1.9% | -33.8 | 15.4% | 104.3% | -26.6% | **0** | **40** |
| Dell Technologies Inc. | `DELL` | 2.0 | 2.3 | 12.0% | 16.0 | 9.6% | 18.4% | 2.0% | **33** | **38** |
| Meta Platforms, Inc. | `META` | 8.1 | 8.3 | 34.8% | 21.0 | 10.4% | 20.7% | 1.2% | **17** | **38** |
| Amazon.com, Inc. | `AMZN` | 3.5 | 3.7 | 13.7% | 23.9 | -18.3% | 14.5% | 0.1% | **0** | **38** |
| Fluence Energy, Inc. | `FLNC` | 0.4 | 0.4 | -8.9% | -13.3 | 66.2% | 29.9% | 0.2% | **5** | **28** |
| Hyperliquid Strategies Inc | `PURR` | 264.7 | 183.5 | 9595.1% | 24.3 | 51.0% | 31.4% | — | **25** | **10** |
| Strategy Inc | `MSTR` | 117.1 | 148.1 | -6808.1% | 2.8 | 157.6% | 2.2% | -38.7% | **25** | **25** |
| BitMine Immersion Technologies, | `BMNR` | 208.6 | 213.8 | 8.4% | 22.5 | 103.2% | 421.8% | -4.1% | **25** | **25** |
| QUALCOMM Incorporated | `QCOM` | 4.1 | 4.3 | 18.5% | 16.6 | -2.7% | 4.7% | 5.7% | **25** | **15** |
| Applied Optoelectronics, Inc. | `AAOI` | 11.5 | 11.9 | -12.9% | 17.6 | 576.8% | 156.5% | -12.9% | **10** | **25** |
| Alphabet Inc. | `GOOGL` | 9.4 | 9.3 | 34.0% | 22.5 | -26.9% | 24.4% | 0.5% | **12** | **23** |

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
