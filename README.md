# OKX Long / Short Fundamental Scanner

Hourly scanner restricted to public companies exposed by the **OKX EEA TradFi / Stock Perpetual API universe**.

**Last scan:** 2026-10-20 13:37 UTC  
**Availability scope:** user-confirmed OKX EEA Stock Futures / X-Perp  
**OKX stock/ETF markets in configured universe:** 72  
**Public companies analysed:** 55  
**SHORT CORE:** 4  
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
| 1 | Taiwan Semiconductor Manufactur | TSM | -0.2% | -5.8% | -3.0% | 88 | +2 | **90** | **CORE** | yes |
| 2 | Credo Technology Group Holding  | CRDO | -4.0% | -16.4% | -10.2% | 82 | +8 | **90** | **CORE** | yes |
| 3 | Corning Incorporated | GLW | -2.3% | -12.6% | -7.5% | 83 | +6 | **89** | **CORE** | yes |
| 4 | Applied Materials, Inc. | AMAT | -1.6% | -12.4% | -7.0% | 81 | +6 | **87** | **CORE** | yes |
| 5 | NVIDIA Corporation | NVDA | -1.1% | -6.0% | -3.5% | 82 | +3 | **85** | **CORE** | yes |
| 6 | Broadcom Inc. | AVGO | -0.2% | -6.6% | -3.4% | 82 | +3 | **85** | **CORE** | yes |
| 7 | Robinhood Markets, Inc. | HOOD | 0.0% | -12.6% | -6.3% | 80 | +5 | **85** | **CORE** | yes |
| 8 | Marvell Technology, Inc. | MRVL | -2.2% | -13.7% | -8.0% | 79 | +6 | **85** | **CORE** | yes |
| 9 | Advanced Micro Devices, Inc. | AMD | -0.7% | -11.7% | -6.2% | 79 | +5 | **84** | **CORE** | yes |
| 10 | Applovin Corporation | APP | 0.0% | -1.2% | -0.6% | 82 | +0 | **82** | **CORE** | yes |

## Final model + Price Timing — SHORT

| Rank | Company | OKX | 24h | 7d | 50/50 move | Base SHORT | Timing adj. | Final | Signal | Prev. SHORT? |
|---:|---|---|---:|---:|---:|---:|---:|---:|---|---|
| 1 | USA Rare Earth, Inc. | USAR | -1.7% | -12.1% | -6.9% | 100 | -6 | **94** | **CORE** | yes |
| 2 | Rocket Lab Corporation | RKLB | -2.2% | -21.8% | -12.0% | 100 | -10 | **90** | **CORE** | yes |
| 3 | IonQ, Inc. | IONQ | 0.2% | -11.2% | -5.5% | 85 | -4 | **81** | **CORE** | yes |
| 4 | Nebius Group N.V. | NBIS | -3.4% | -20.5% | -11.9% | 84 | -10 | **74** | **WATCH** | yes |
| 5 | Cerebras Systems Inc. | CBRS | -1.2% | -20.1% | -10.6% | 82 | -9 | **73** | **WATCH** | yes |
| 6 | AST SpaceMobile, Inc. | ASTS | -4.5% | -15.0% | -9.7% | 80 | -8 | **72** | **WATCH** | yes |
| 7 | Moderna, Inc. | MRNA | -2.9% | 1.8% | -0.5% | 72 | +0 | **72** | **WATCH** | yes |

## Combined model — LONG

Weighted score: **70% fundamental + 30% P/E trend**.

| Rank | Company | OKX | Fundamental LONG | P/E trend LONG | Combined | Signal |
|---:|---|---|---:|---:|---:|---|
| 1 | Taiwan Semiconductor Manufactur | `TSM` | 90 | 85 | **88** | **CORE** |
| 2 | Corning Incorporated | `GLW` | 77 | 96 | **83** | **CORE** |
| 3 | Applovin Corporation | `APP` | 83 | 80 | **82** | **CORE** |
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
| 3 | IonQ, Inc. | `IONQ` | 85 | 0 | **85** | **CORE** |
| 4 | Nebius Group N.V. | `NBIS` | 84 | 0 | **84** | **WATCH** |
| 5 | Cerebras Systems Inc. | `CBRS` | 82 | 0 | **82** | **WATCH** |
| 6 | AST SpaceMobile, Inc. | `ASTS` | 80 | 0 | **80** | **WATCH** |
| 7 | Moderna, Inc. | `MRNA` | 72 | 0 | **72** | **WATCH** |
| 8 | Okta, Inc. | `OKTA` | 80 | 13 | **60** | **WATCH** |

## P/E Compression + Growth — LONG

| Rank | Company | OKX | Trail P/E | Fwd P/E | P/E change | EPS +1y | Rev +1y | Rev trend | LONG score | Signal |
|---:|---|---|---:|---:|---:|---:|---:|---|---:|---|
| 1 | Credo Technology Group Holding  | `CRDO` | 58.8 | 17.1 | -70.9% | 53.7% | 54.8% | decelerating | **100** | **CORE** |
| 2 | NVIDIA Corporation | `NVDA` | 27.1 | 13.5 | -50.3% | 70.9% | 68.2% | decelerating | **100** | **CORE** |
| 3 | Broadcom Inc. | `AVGO` | 42.6 | 17.2 | -59.6% | 66.4% | 64.1% | decelerating | **100** | **CORE** |
| 4 | Marvell Technology, Inc. | `MRVL` | 76.3 | 31.6 | -58.5% | 73.7% | 63.3% | accelerating | **100** | **CORE** |
| 5 | Advanced Micro Devices, Inc. | `AMD` | 136.3 | 33.9 | -75.1% | 107.7% | 74.8% | accelerating | **100** | **CORE** |
| 6 | Corning Incorporated | `GLW` | 59.5 | 29.7 | -50.2% | 33.1% | 19.7% | accelerating | **96** | **CORE** |
| 7 | AXT Inc | `AXT` | 1336.1 | 23.8 | -98.2% | 159.2% | 111.3% | decelerating | **96** | **CORE** |
| 8 | Oracle Corporation | `ORCL` | 20.3 | 11.8 | -42.0% | 35.0% | 45.7% | accelerating | **95** | **CORE** |
| 9 | Coherent Corp. | `COHR` | 53.9 | 15.8 | -70.7% | 49.2% | 38.9% | decelerating | **95** | **CORE** |
| 10 | Arm Holdings plc | `ARM` | 228.2 | 72.3 | -68.3% | 37.5% | 36.2% | accelerating | **95** | **CORE** |

## P/E Expansion + Weakening — SHORT

| Rank | Company | OKX | Trail P/E | Fwd P/E | P/E change | EPS +1y | Rev +1y | Rev trend | SHORT score | Signal |
|---:|---|---|---:|---:|---:|---:|---:|---|---:|---|
| 1 | SOFTBANK GROUP CORP | `SOFTBANK` | 5.3 | 15.4 | 191.0% | -14.5% | 6.9% | decelerating | **86** | **CORE** |
| 2 | Hyperliquid Strategies Inc | `PURR` | 2.8 | 24.3 | 767.6% | 51.0% | 31.4% | decelerating | **55** | **WATCH** |
| 3 | Amazon.com, Inc. | `AMZN` | 21.1 | 25.1 | 19.0% | -18.1% | 14.6% | decelerating | **52** | **WATCH** |
| 4 | Alphabet Inc. | `GOOGL` | 17.2 | 22.3 | 29.9% | -26.7% | 25.3% | accelerating | **50** | **WATCH** |

## Top SHORT candidates

| Rank | Company | OKX market | SHORT score | Signal | P/S | EV/S | Op margin | Fwd P/E | Rev +1y | FCF yield |
|---:|---|---|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Rocket Lab Corporation | `RKLB-USDT-SWAP` | **100** | **CORE** | 41.7 | 37.1 | -24.6% | 873.4 | 38.2% | -0.8% |
| 2 | USA Rare Earth, Inc. | `USAR-USDT-SWAP` | **100** | **CORE** | 282.6 | 72.3 | -795.6% | 330.6 | 870.1% | -7.6% |
| 3 | IonQ, Inc. | `IONQ-USDT-SWAP` | **85** | **CORE** | 50.7 | 39.3 | -408.2% | -23.0 | 77.6% | -0.7% |
| 4 | Nebius Group N.V. | `NBIS-USDT-SWAP` | **84** | **WATCH** | 33.0 | 36.0 | -0.2% | -46.2 | 268.0% | -21.5% |
| 5 | Cerebras Systems Inc. | `CBRS-USDT-SWAP` | **82** | **WATCH** | 41.6 | 32.7 | -265.0% | 93.6 | 232.7% | — |
| 6 | Okta, Inc. | `OKTA-USDT-SWAP` | **80** | **CORE** | 10.6 | 10.1 | 13.3% | 42.5 | 10.0% | 3.2% |
| 7 | AST SpaceMobile, Inc. | `ASTS-USDT-SWAP` | **80** | **WATCH** | 135.0 | 119.4 | -544.6% | -31.1 | 247.3% | -11.6% |
| 8 | Moderna, Inc. | `MRNA-USDT-SWAP` | **72** | **WATCH** | 39.5 | 38.9 | -557.9% | -49.2 | 15.7% | 0.3% |
| 9 | Tesla, Inc. | `TSLA-USDT-SWAP` | **63** | **WATCH** | 14.0 | 13.8 | 1.4% | 169.3 | 13.5% | 0.3% |

## Top LONG candidates

| Rank | Company | OKX market | LONG score | Signal | P/S | EV/S | Op margin | Fwd P/E | Rev +1y | FCF yield |
|---:|---|---|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Taiwan Semiconductor Manufactur | `TSM-USDT-SWAP` | **90** | **CORE** | 0.4 | 2.9 | 58.7% | 17.9 | 37.5% | 55.3% |
| 2 | Applovin Corporation | `APP-USDT-SWAP` | **83** | **CORE** | 13.2 | 13.3 | 77.7% | 13.1 | 26.0% | 3.5% |
| 3 | Corning Incorporated | `GLW-USDT-SWAP` | **77** | **WATCH** | 6.6 | 7.2 | 15.6% | 29.7 | 19.7% | 0.7% |
| 4 | Robinhood Markets, Inc. | `HOOD-USDT-SWAP` | **77** | **WATCH** | 17.6 | 17.4 | 43.9% | 28.3 | 29.2% | — |
| 5 | Applied Materials, Inc. | `AMAT-USDT-SWAP` | **77** | **WATCH** | 10.5 | 10.6 | 33.7% | 22.0 | 35.4% | 1.0% |
| 6 | Credo Technology Group Holding  | `CRDO-USDT-SWAP` | **75** | **WATCH** | 19.6 | 20.0 | 25.2% | 17.1 | 54.8% | 0.8% |
| 7 | Broadcom Inc. | `AVGO-USDT-SWAP` | **75** | **WATCH** | 17.9 | 18.3 | 54.3% | 17.2 | 64.1% | 1.9% |
| 8 | Micron Technology, Inc. | `MU-USDT-SWAP` | **75** | **CORE** | 7.6 | 7.4 | 80.7% | 4.3 | 15.7% | 2.9% |
| 9 | Sandisk Corporation | `SNDK-USDT-SWAP` | **75** | **CORE** | 9.7 | 9.7 | 78.5% | 5.1 | 18.9% | 3.9% |
| 10 | NVIDIA Corporation | `NVDA-USDT-SWAP` | **75** | **WATCH** | 17.1 | 17.2 | 66.2% | 13.5 | 68.2% | 0.8% |

## Analyst consensus (12-month price target) — most upside

| Rank | Company | OKX | Price | Analyst mean target | Gap | Analysts | Currency |
|---:|---|---|---:|---:|---:|---:|---|
| 1 | IREN LIMITED | `IREN` | 26.02 | 77.81 | **199.1%** | 18 | USD |
| 2 | SK hynix | `SKHYNIX` | 1223000.00 | 3096288.00 | **153.2%** | 38 | KRW |
| 3 | Hyperliquid Strategies Inc | `PURR` | 8.97 | 22.32 | **148.7%** | 4 | USD |
| 4 | Cerebras Systems Inc. | `CBRS` | 119.19 | 282.55 | **137.1%** | 11 | USD |
| 5 | CoreWeave, Inc. | `CRWV` | 58.84 | 138.34 | **135.1%** | 38 | USD |
| 6 | SamsungElec | `SAMSUNG` | 211500.00 | 478905.62 | **126.4%** | 36 | KRW |
| 7 | Applied Optoelectronics, Inc. | `AAOI` | 74.48 | 160.00 | **114.8%** | 5 | USD |
| 8 | BitMine Immersion Technologies, | `BMNR` | 21.61 | 45.87 | **112.2%** | 3 | USD |
| 9 | IonQ, Inc. | `IONQ` | 30.85 | 64.06 | **107.7%** | 14 | USD |
| 10 | Rocket Lab Corporation | `RKLB` | 50.21 | 102.15 | **103.4%** | 20 | USD |
| 11 | Western Digital Corporation | `WDC` | 349.18 | 650.67 | **86.3%** | 24 | USD |
| 12 | AST SpaceMobile, Inc. | `ASTS` | 39.99 | 74.28 | **85.7%** | 12 | USD |
| 13 | Oracle Corporation | `ORCL` | 129.35 | 237.36 | **83.5%** | 41 | USD |
| 14 | Coherent Corp. | `COHR` | 222.03 | 405.22 | **82.5%** | 23 | USD |
| 15 | Applovin Corporation | `APP` | 269.14 | 476.85 | **77.2%** | 31 | USD |

## Analyst consensus (12-month price target) — most downside

| Rank | Company | OKX | Price | Analyst mean target | Gap | Analysts | Currency |
|---:|---|---|---:|---:|---:|---:|---|
| 1 | Moderna, Inc. | `MRNA` | 220.25 | 129.22 | **-41.3%** | 18 | USD |
| 2 | Apple Inc. | `AAPL` | 340.66 | 328.35 | **-3.6%** | 39 | USD |

Price/target uses the underlying Yahoo Finance share quote, not the OKX derivative. Minimum 3 analysts; unreliable price scales and missing coverage excluded. Targets are analyst opinions, not guaranteed forecasts.

## All OKX companies — our ratio + LONG/SHORT scores

| Company | OKX | P/S | EV/S | Op margin | Fwd P/E | EPS +1y | Rev +1y | FCF yield | LONG | SHORT |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| USA Rare Earth, Inc. | `USAR` | 282.6 | 72.3 | -795.6% | 330.6 | 105.3% | 870.1% | -7.6% | **0** | **100 CORE** |
| Rocket Lab Corporation | `RKLB` | 41.7 | 37.1 | -24.6% | 873.4 | 66.8% | 38.2% | -0.8% | **0** | **100 CORE** |
| Taiwan Semiconductor Manufactur | `TSM` | 0.4 | 2.9 | 58.7% | 17.9 | 33.6% | 37.5% | 55.3% | **90 CORE** | **10** |
| IonQ, Inc. | `IONQ` | 50.7 | 39.3 | -408.2% | -23.0 | 21.3% | 77.6% | -0.7% | **0** | **85 CORE** |
| Nebius Group N.V. | `NBIS` | 33.0 | 36.0 | -0.2% | -46.2 | -191.4% | 268.0% | -21.5% | **0** | **84 WATCH** |
| Applovin Corporation | `APP` | 13.2 | 13.3 | 77.7% | 13.1 | 27.1% | 26.0% | 3.5% | **83 CORE** | **10** |
| Cerebras Systems Inc. | `CBRS` | 41.6 | 32.7 | -265.0% | 93.6 | 371.3% | 232.7% | — | **0** | **82 WATCH** |
| Okta, Inc. | `OKTA` | 10.6 | 10.1 | 13.3% | 42.5 | 11.4% | 10.0% | 3.2% | **8** | **80 CORE** |
| AST SpaceMobile, Inc. | `ASTS` | 135.0 | 119.4 | -544.6% | -31.1 | 44.3% | 247.3% | -11.6% | **0** | **80 WATCH** |
| Corning Incorporated | `GLW` | 6.6 | 7.2 | 15.6% | 29.7 | 33.1% | 19.7% | 0.7% | **77 WATCH** | **13** |
| Applied Materials, Inc. | `AMAT` | 10.5 | 10.6 | 33.7% | 22.0 | 44.6% | 35.4% | 1.0% | **77 WATCH** | **3** |
| Robinhood Markets, Inc. | `HOOD` | 17.6 | 17.4 | 43.9% | 28.3 | 36.5% | 29.2% | — | **77 WATCH** | **5** |
| Credo Technology Group Holding  | `CRDO` | 19.6 | 20.0 | 25.2% | 17.1 | 53.7% | 54.8% | 0.8% | **75 WATCH** | **28** |
| NVIDIA Corporation | `NVDA` | 17.1 | 17.2 | 66.2% | 13.5 | 70.9% | 68.2% | 0.8% | **75 WATCH** | **18** |
| Broadcom Inc. | `AVGO` | 17.9 | 18.3 | 54.3% | 17.2 | 66.4% | 64.1% | 1.9% | **75 WATCH** | **28** |
| Sandisk Corporation | `SNDK` | 9.7 | 9.7 | 78.5% | 5.1 | 24.0% | 18.9% | 3.9% | **75 CORE** | **10** |
| Micron Technology, Inc. | `MU` | 7.6 | 7.4 | 80.7% | 4.3 | 17.2% | 15.7% | 2.9% | **75 CORE** | **30** |
| Western Digital Corporation | `WDC` | 10.1 | 9.8 | 43.6% | 10.5 | 61.6% | 37.8% | 1.7% | **75 WATCH** | **18** |
| Moderna, Inc. | `MRNA` | 39.5 | 38.9 | -557.9% | -49.2 | 42.7% | 15.7% | 0.3% | **0** | **72 WATCH** |
| Marvell Technology, Inc. | `MRVL` | 22.0 | 22.1 | 16.7% | 31.6 | 73.7% | 63.3% | 1.2% | **70 WATCH** | **13** |
| Advanced Micro Devices, Inc. | `AMD` | 21.1 | 21.1 | 17.2% | 33.9 | 107.7% | 74.8% | 1.0% | **70 WATCH** | **13** |
| Oracle Corporation | `ORCL` | 5.5 | 7.4 | 35.6% | 11.8 | 35.0% | 45.7% | -11.7% | **70 WATCH** | **10** |
| XIAOMI-W | `XIAOMI` | 1.6 | 1.4 | 4.0% | 17.7 | 39.0% | 21.4% | -1.2% | **70 WATCH** | **10** |
| Adobe Inc. | `ADBE` | 3.8 | 3.7 | 34.8% | 9.1 | 12.4% | 9.1% | 9.5% | **65 WATCH** | **30** |
| Tesla, Inc. | `TSLA` | 14.0 | 13.8 | 1.4% | 169.3 | 24.4% | 13.5% | 0.3% | **22** | **63 WATCH** |
| Coherent Corp. | `COHR` | 6.1 | 6.6 | 11.8% | 15.8 | 49.2% | 38.9% | -1.5% | **60 WATCH** | **35** |
| Microsoft Corporation | `MSFT` | 11.9 | 12.1 | 45.1% | 22.4 | 19.9% | 19.7% | 0.4% | **59 WATCH** | **23** |
| Apple Inc. | `AAPL` | 10.6 | 10.8 | 32.6% | 35.6 | 8.4% | 10.4% | 2.2% | **5** | **58** |
| Coca-Cola Company (The) | `KO` | 8.1 | 8.6 | 34.9% | 26.6 | 6.7% | -0.1% | 1.3% | **0** | **58** |
| Bloom Energy Corporation | `BE` | 20.5 | 21.4 | 17.1% | 44.0 | 82.4% | 65.4% | 0.8% | **55 WATCH** | **48** |
| AXT Inc | `AXT` | 27.9 | 27.1 | 21.9% | 23.8 | 159.2% | 111.3% | -1.3% | **52** | **35** |
| Super Micro Computer, Inc. | `SMCI` | 0.5 | 0.7 | 13.4% | 5.9 | 22.8% | 17.3% | -40.1% | **52** | **25** |
| Lumentum Holdings Inc. | `LITE` | 24.1 | 24.5 | 28.0% | 22.3 | 65.3% | 57.0% | 0.3% | **0** | **51** |
| Netflix, Inc. | `NFLX` | 6.0 | 6.2 | 33.4% | 18.3 | 5.9% | 11.2% | 8.8% | **35** | **50** |
| IREN LIMITED | `IREN` | 14.5 | 18.2 | -102.5% | -6.5 | -16.4% | 164.0% | -41.2% | **0** | **50** |
| Palantir Technologies Inc. | `PLTR` | 74.9 | 74.3 | 47.1% | 81.6 | 45.2% | 50.1% | 0.5% | **33** | **48** |
| Intel Corporation | `INTC` | 8.4 | 8.8 | 12.2% | 42.6 | 38.1% | 15.2% | 1.0% | **10** | **48** |
| SK hynix | `SKHYNIX` | 4.7 | 4.4 | 76.3% | 2.6 | 31.9% | 54.3% | 6.3% | **45** | **5** |
| SK hynix | `SKHY` | 4.7 | 4.4 | 76.3% | 2.6 | 31.9% | 54.3% | 6.3% | **45** | **5** |
| SamsungElec | `SAMSUNG` | 2.8 | 2.6 | 52.2% | 2.9 | 51.4% | 37.9% | 5.0% | **45** | **10** |
| Arm Holdings plc | `ARM` | 45.9 | 46.6 | 7.6% | 72.3 | 37.5% | 36.2% | 0.6% | **43** | **33** |
| Circle Internet Group, Inc. | `CRCL` | 7.2 | 6.5 | 4.9% | 55.8 | 30.0% | 26.4% | 1.0% | **43** | **33** |
| Coinbase Global, Inc. | `COIN` | 7.3 | 7.0 | -13.9% | 56.5 | 265.3% | 30.0% | 6.0% | **20** | **40** |
| SOFTBANK GROUP CORP | `SOFTBANK` | 3.2 | 6.8 | -11.6% | 15.4 | -14.5% | 6.9% | -8.4% | **0** | **40** |
| CoreWeave, Inc. | `CRWV` | 4.3 | 10.5 | -1.9% | -31.9 | 12.6% | 104.7% | -28.0% | **0** | **40** |
| Dell Technologies Inc. | `DELL` | 1.9 | 2.1 | 12.0% | 14.9 | 9.6% | 18.4% | 2.1% | **33** | **38** |
| Meta Platforms, Inc. | `META` | 7.7 | 8.0 | 34.8% | 19.9 | 11.0% | 20.8% | 1.2% | **33** | **38** |
| Amazon.com, Inc. | `AMZN` | 3.6 | 3.8 | 13.7% | 25.1 | -18.1% | 14.6% | 0.1% | **0** | **38** |
| Fluence Energy, Inc. | `FLNC` | 0.4 | 0.4 | -8.9% | -12.9 | 60.4% | 27.7% | 0.2% | **5** | **28** |
| Hyperliquid Strategies Inc | `PURR` | 264.0 | 173.0 | 9595.1% | 24.3 | 51.0% | 31.4% | — | **25** | **10** |
| Strategy Inc | `MSTR` | 115.1 | 142.5 | -6808.1% | 2.7 | 168.2% | 2.2% | -39.4% | **25** | **25** |
| BitMine Immersion Technologies, | `BMNR` | 213.1 | 207.1 | 8.4% | 23.0 | 103.2% | 421.8% | -4.0% | **25** | **25** |
| QUALCOMM Incorporated | `QCOM` | 4.2 | 4.3 | 18.5% | 17.0 | -2.8% | 4.7% | 5.5% | **25** | **15** |
| Applied Optoelectronics, Inc. | `AAOI` | 10.6 | 10.8 | -12.9% | 16.2 | 576.8% | 156.5% | -14.0% | **10** | **25** |
| Alphabet Inc. | `GOOGL` | 9.4 | 9.2 | 34.0% | 22.3 | -26.7% | 25.3% | 0.5% | **12** | **23** |

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
