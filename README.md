# OKX Long / Short Fundamental Scanner

Hourly scanner restricted to public companies exposed by the **OKX EEA TradFi / Stock Perpetual API universe**.

**Last scan:** 2026-10-17 00:32 UTC  
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
| 1 | Taiwan Semiconductor Manufactur | TSM | -2.3% | -9.0% | -5.6% | 88 | +5 | **93** | **CORE** | yes |
| 2 | Credo Technology Group Holding  | CRDO | -4.9% | -21.6% | -13.3% | 82 | +11 | **93** | **CORE** | yes |
| 3 | Sandisk Corporation | SNDK | -6.8% | -17.9% | -12.4% | 82 | +10 | **92** | **CORE** | yes |
| 4 | Applied Materials, Inc. | AMAT | -4.8% | -19.3% | -12.0% | 81 | +10 | **91** | **CORE** | yes |
| 5 | Marvell Technology, Inc. | MRVL | -5.6% | -17.2% | -11.4% | 79 | +9 | **88** | **CORE** | yes |
| 6 | Broadcom Inc. | AVGO | -4.5% | -9.1% | -6.8% | 82 | +5 | **87** | **CORE** | yes |
| 7 | Advanced Micro Devices, Inc. | AMD | -6.0% | -13.0% | -9.5% | 79 | +8 | **87** | **CORE** | yes |
| 8 | Robinhood Markets, Inc. | HOOD | -4.9% | -9.3% | -7.1% | 80 | +6 | **86** | **CORE** | yes |
| 9 | Corning Incorporated | GLW | -4.6% | -15.8% | -10.2% | 78 | +8 | **86** | **CORE** | yes |
| 10 | Applovin Corporation | APP | -4.7% | -3.9% | -4.3% | 82 | +3 | **85** | **CORE** | yes |

## Final model + Price Timing — SHORT

| Rank | Company | OKX | 24h | 7d | 50/50 move | Base SHORT | Timing adj. | Final | Signal | Prev. SHORT? |
|---:|---|---|---:|---:|---:|---:|---:|---:|---|---|
| 1 | USA Rare Earth, Inc. | USAR | -5.0% | -16.1% | -10.5% | 100 | -8 | **92** | **CORE** | yes |
| 2 | Rocket Lab Corporation | RKLB | -8.0% | -25.5% | -16.7% | 100 | -13 | **87** | **CORE** | yes |
| 3 | IonQ, Inc. | IONQ | -8.9% | -21.6% | -15.3% | 88 | -12 | **76** | **CORE** | yes |
| 4 | Nebius Group N.V. | NBIS | -12.2% | -25.2% | -18.7% | 84 | -15 | **69** | **WATCH** | yes |
| 5 | Cerebras Systems Inc. | CBRS | -10.5% | -22.5% | -16.5% | 82 | -13 | **69** | **WATCH** | yes |
| 6 | AST SpaceMobile, Inc. | ASTS | -8.5% | -20.2% | -14.4% | 80 | -12 | **68** | **WATCH** | yes |
| 7 | Moderna, Inc. | MRNA | -7.8% | -3.1% | -5.5% | 72 | -4 | **68** | **WATCH** | yes |

## Combined model — LONG

Weighted score: **70% fundamental + 30% P/E trend**.

| Rank | Company | OKX | Fundamental LONG | P/E trend LONG | Combined | Signal |
|---:|---|---|---:|---:|---:|---|
| 1 | Taiwan Semiconductor Manufactur | `TSM` | 90 | 85 | **88** | **CORE** |
| 2 | Applovin Corporation | `APP` | 83 | 80 | **82** | **CORE** |
| 3 | Sandisk Corporation | `SNDK` | 82 | 82 | **82** | **CORE** |
| 4 | Credo Technology Group Holding  | `CRDO` | 75 | 100 | **82** | **CORE** |
| 5 | Broadcom Inc. | `AVGO` | 75 | 100 | **82** | **CORE** |
| 6 | NVIDIA Corporation | `NVDA` | 75 | 100 | **82** | **CORE** |
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
| 3 | IonQ, Inc. | `IONQ` | 88 | 0 | **88** | **CORE** |
| 4 | Nebius Group N.V. | `NBIS` | 84 | 0 | **84** | **WATCH** |
| 5 | Cerebras Systems Inc. | `CBRS` | 82 | 0 | **82** | **WATCH** |
| 6 | AST SpaceMobile, Inc. | `ASTS` | 80 | 0 | **80** | **WATCH** |
| 7 | Moderna, Inc. | `MRNA` | 72 | 0 | **72** | **WATCH** |
| 8 | Okta, Inc. | `OKTA` | 80 | 13 | **60** | **WATCH** |

## P/E Compression + Growth — LONG

| Rank | Company | OKX | Trail P/E | Fwd P/E | P/E change | EPS +1y | Rev +1y | Rev trend | LONG score | Signal |
|---:|---|---|---:|---:|---:|---:|---:|---|---:|---|
| 1 | Credo Technology Group Holding  | `CRDO` | 60.2 | 17.5 | -70.9% | 53.7% | 54.8% | decelerating | **100** | **CORE** |
| 2 | Marvell Technology, Inc. | `MRVL` | 74.9 | 31.2 | -58.3% | 72.9% | 63.2% | accelerating | **100** | **CORE** |
| 3 | Advanced Micro Devices, Inc. | `AMD` | 134.9 | 33.6 | -75.1% | 107.7% | 74.8% | accelerating | **100** | **CORE** |
| 4 | Broadcom Inc. | `AVGO` | 43.3 | 17.0 | -60.9% | 66.4% | 64.2% | decelerating | **100** | **CORE** |
| 5 | NVIDIA Corporation | `NVDA` | 27.1 | 13.5 | -50.3% | 70.9% | 68.2% | decelerating | **100** | **CORE** |
| 6 | Corning Incorporated | `GLW` | 60.6 | 30.2 | -50.1% | 33.0% | 19.6% | accelerating | **96** | **CORE** |
| 7 | AXT Inc | `AXT` | 1286.8 | 22.9 | -98.2% | 159.2% | 111.3% | decelerating | **96** | **CORE** |
| 8 | Oracle Corporation | `ORCL` | 20.1 | 11.7 | -42.0% | 35.0% | 45.7% | accelerating | **95** | **CORE** |
| 9 | Coherent Corp. | `COHR` | 56.5 | 16.6 | -70.7% | 49.2% | 38.9% | decelerating | **95** | **CORE** |
| 10 | Arm Holdings plc | `ARM` | 234.8 | 74.4 | -68.3% | 37.5% | 36.2% | accelerating | **95** | **CORE** |

## P/E Expansion + Weakening — SHORT

| Rank | Company | OKX | Trail P/E | Fwd P/E | P/E change | EPS +1y | Rev +1y | Rev trend | SHORT score | Signal |
|---:|---|---|---:|---:|---:|---:|---:|---|---:|---|
| 1 | SOFTBANK GROUP CORP | `SOFTBANK` | 5.6 | 16.7 | 196.5% | -14.5% | 6.9% | decelerating | **86** | **CORE** |
| 2 | Alphabet Inc. | `GOOGL` | 17.1 | 22.3 | 30.4% | -26.8% | 24.8% | accelerating | **60** | **WATCH** |
| 3 | Hyperliquid Strategies Inc | `PURR` | 2.8 | 24.5 | 767.6% | 51.0% | 31.4% | decelerating | **55** | **WATCH** |
| 4 | Amazon.com, Inc. | `AMZN` | 20.1 | 23.9 | 19.0% | -18.2% | 14.6% | decelerating | **52** | **WATCH** |

## Top SHORT candidates

| Rank | Company | OKX market | SHORT score | Signal | P/S | EV/S | Op margin | Fwd P/E | Rev +1y | FCF yield |
|---:|---|---|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Rocket Lab Corporation | `RKLB-USDT-SWAP` | **100** | **CORE** | 42.3 | 36.7 | -24.6% | 884.3 | 38.8% | -0.8% |
| 2 | USA Rare Earth, Inc. | `USAR-USDT-SWAP` | **100** | **CORE** | 300.4 | 80.8 | -795.6% | 351.3 | 870.1% | -7.2% |
| 3 | IonQ, Inc. | `IONQ-USDT-SWAP` | **88** | **CORE** | 51.4 | 40.0 | -408.2% | -23.3 | 77.6% | -0.7% |
| 4 | Nebius Group N.V. | `NBIS-USDT-SWAP` | **84** | **WATCH** | 31.0 | 35.1 | -0.2% | -46.5 | 268.0% | -21.4% |
| 5 | Cerebras Systems Inc. | `CBRS-USDT-SWAP` | **82** | **WATCH** | 44.4 | 34.9 | -265.0% | 99.9 | 232.7% | — |
| 6 | Okta, Inc. | `OKTA-USDT-SWAP` | **80** | **CORE** | 10.7 | 9.9 | 13.3% | 42.8 | 10.0% | 3.2% |
| 7 | AST SpaceMobile, Inc. | `ASTS-USDT-SWAP` | **80** | **WATCH** | 137.2 | 116.2 | -544.6% | -31.6 | 247.3% | -11.4% |
| 8 | Moderna, Inc. | `MRNA-USDT-SWAP` | **72** | **WATCH** | 39.1 | 37.3 | -557.9% | -49.1 | 16.1% | 0.3% |
| 9 | Tesla, Inc. | `TSLA-USDT-SWAP` | **63** | **WATCH** | 13.5 | 13.3 | 1.4% | 163.6 | 13.5% | 0.3% |

## Top LONG candidates

| Rank | Company | OKX market | LONG score | Signal | P/S | EV/S | Op margin | Fwd P/E | Rev +1y | FCF yield |
|---:|---|---|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Taiwan Semiconductor Manufactur | `TSM-USDT-SWAP` | **90** | **CORE** | 0.5 | 3.5 | 60.3% | 17.9 | 37.5% | 34.2% |
| 2 | Applovin Corporation | `APP-USDT-SWAP` | **83** | **CORE** | 13.0 | 13.1 | 77.7% | 13.0 | 26.0% | 3.6% |
| 3 | Sandisk Corporation | `SNDK-USDT-SWAP` | **82** | **CORE** | 9.3 | 9.2 | 78.5% | 4.9 | 18.9% | 4.1% |
| 4 | Robinhood Markets, Inc. | `HOOD-USDT-SWAP` | **77** | **WATCH** | 18.0 | 17.8 | 43.9% | 28.8 | 29.3% | — |
| 5 | Applied Materials, Inc. | `AMAT-USDT-SWAP` | **77** | **WATCH** | 10.5 | 10.5 | 33.7% | 22.2 | 35.2% | 0.9% |
| 6 | Credo Technology Group Holding  | `CRDO-USDT-SWAP` | **75** | **WATCH** | 20.0 | 19.6 | 25.2% | 17.5 | 54.8% | 0.8% |
| 7 | Broadcom Inc. | `AVGO-USDT-SWAP` | **75** | **WATCH** | 17.6 | 18.0 | 54.3% | 17.0 | 64.2% | 1.9% |
| 8 | Micron Technology, Inc. | `MU-USDT-SWAP` | **75** | **CORE** | 7.5 | 7.2 | 80.7% | 4.2 | 15.7% | 2.9% |
| 9 | NVIDIA Corporation | `NVDA-USDT-SWAP` | **75** | **WATCH** | 17.1 | 17.0 | 66.2% | 13.5 | 68.2% | 0.8% |
| 10 | Western Digital Corporation | `WDC-USDT-SWAP` | **75** | **WATCH** | 9.6 | 9.2 | 43.6% | 10.0 | 37.2% | 1.8% |

## Analyst consensus (12-month price target) — most upside

| Rank | Company | OKX | Price | Analyst mean target | Gap | Analysts | Currency |
|---:|---|---|---:|---:|---:|---:|---|
| 1 | IREN LIMITED | `IREN` | 26.99 | 77.81 | **188.3%** | 18 | USD |
| 2 | SK hynix | `SKHYNIX` | 1272000.00 | 3141024.80 | **146.9%** | 38 | KRW |
| 3 | Hyperliquid Strategies Inc | `PURR` | 9.07 | 22.32 | **146.1%** | 4 | USD |
| 4 | Cerebras Systems Inc. | `CBRS` | 127.21 | 291.64 | **129.3%** | 11 | USD |
| 5 | CoreWeave, Inc. | `CRWV` | 61.39 | 140.58 | **129.0%** | 38 | USD |
| 6 | SamsungElec | `SAMSUNG` | 215500.00 | 478905.62 | **122.2%** | 36 | KRW |
| 7 | BitMine Immersion Technologies, | `BMNR` | 21.66 | 45.87 | **111.8%** | 3 | USD |
| 8 | Applied Optoelectronics, Inc. | `AAOI` | 75.57 | 160.00 | **111.7%** | 5 | USD |
| 9 | IonQ, Inc. | `IONQ` | 31.28 | 64.06 | **104.8%** | 14 | USD |
| 10 | Western Digital Corporation | `WDC` | 332.00 | 668.50 | **101.4%** | 24 | USD |
| 11 | Rocket Lab Corporation | `RKLB` | 50.84 | 102.26 | **101.1%** | 19 | USD |
| 12 | Oracle Corporation | `ORCL` | 128.23 | 237.36 | **85.1%** | 41 | USD |
| 13 | AST SpaceMobile, Inc. | `ASTS` | 40.66 | 74.28 | **82.7%** | 12 | USD |
| 14 | Applovin Corporation | `APP` | 266.13 | 480.08 | **80.4%** | 31 | USD |
| 15 | AXT Inc | `AXT` | 51.47 | 91.60 | **78.0%** | 5 | USD |

## Analyst consensus (12-month price target) — most downside

| Rank | Company | OKX | Price | Analyst mean target | Gap | Analysts | Currency |
|---:|---|---|---:|---:|---:|---:|---|
| 1 | Moderna, Inc. | `MRNA` | 218.01 | 123.61 | **-43.3%** | 18 | USD |
| 2 | Apple Inc. | `AAPL` | 343.46 | 329.38 | **-4.1%** | 39 | USD |

Price/target uses the underlying Yahoo Finance share quote, not the OKX derivative. Minimum 3 analysts; unreliable price scales and missing coverage excluded. Targets are analyst opinions, not guaranteed forecasts.

## All OKX companies — our ratio + LONG/SHORT scores

| Company | OKX | P/S | EV/S | Op margin | Fwd P/E | EPS +1y | Rev +1y | FCF yield | LONG | SHORT |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| USA Rare Earth, Inc. | `USAR` | 300.4 | 80.8 | -795.6% | 351.3 | 105.3% | 870.1% | -7.2% | **0** | **100 CORE** |
| Rocket Lab Corporation | `RKLB` | 42.3 | 36.7 | -24.6% | 884.3 | 65.5% | 38.8% | -0.8% | **0** | **100 CORE** |
| Taiwan Semiconductor Manufactur | `TSM` | 0.5 | 3.5 | 60.3% | 17.9 | 33.5% | 37.5% | 34.2% | **90 CORE** | **10** |
| IonQ, Inc. | `IONQ` | 51.4 | 40.0 | -408.2% | -23.3 | 21.3% | 77.6% | -0.7% | **0** | **88 CORE** |
| Nebius Group N.V. | `NBIS` | 31.0 | 35.1 | -0.2% | -46.5 | -191.4% | 268.0% | -21.4% | **0** | **84 WATCH** |
| Applovin Corporation | `APP` | 13.0 | 13.1 | 77.7% | 13.0 | 27.3% | 26.0% | 3.6% | **83 CORE** | **10** |
| Sandisk Corporation | `SNDK` | 9.3 | 9.2 | 78.5% | 4.9 | 24.0% | 18.9% | 4.1% | **82 CORE** | **10** |
| Cerebras Systems Inc. | `CBRS` | 44.4 | 34.9 | -265.0% | 99.9 | 371.3% | 232.7% | — | **0** | **82 WATCH** |
| Okta, Inc. | `OKTA` | 10.7 | 9.9 | 13.3% | 42.8 | 11.4% | 10.0% | 3.2% | **8** | **80 CORE** |
| AST SpaceMobile, Inc. | `ASTS` | 137.2 | 116.2 | -544.6% | -31.6 | 44.3% | 247.3% | -11.4% | **0** | **80 WATCH** |
| Applied Materials, Inc. | `AMAT` | 10.5 | 10.5 | 33.7% | 22.2 | 44.4% | 35.2% | 0.9% | **77 WATCH** | **3** |
| Robinhood Markets, Inc. | `HOOD` | 18.0 | 17.8 | 43.9% | 28.8 | 36.6% | 29.3% | — | **77 WATCH** | **5** |
| Credo Technology Group Holding  | `CRDO` | 20.0 | 19.6 | 25.2% | 17.5 | 53.7% | 54.8% | 0.8% | **75 WATCH** | **28** |
| Broadcom Inc. | `AVGO` | 17.6 | 18.0 | 54.3% | 17.0 | 66.4% | 64.2% | 1.9% | **75 WATCH** | **28** |
| Micron Technology, Inc. | `MU` | 7.5 | 7.2 | 80.7% | 4.2 | 17.2% | 15.7% | 2.9% | **75 CORE** | **30** |
| NVIDIA Corporation | `NVDA` | 17.1 | 17.0 | 66.2% | 13.5 | 70.9% | 68.2% | 0.8% | **75 WATCH** | **18** |
| Western Digital Corporation | `WDC` | 9.6 | 9.2 | 43.6% | 10.0 | 61.2% | 37.2% | 1.8% | **75 WATCH** | **18** |
| Moderna, Inc. | `MRNA` | 39.1 | 37.3 | -557.9% | -49.1 | 43.0% | 16.1% | 0.3% | **0** | **72 WATCH** |
| Marvell Technology, Inc. | `MRVL` | 21.7 | 21.3 | 16.7% | 31.2 | 72.9% | 63.2% | 1.2% | **70 WATCH** | **13** |
| Advanced Micro Devices, Inc. | `AMD` | 20.9 | 20.7 | 17.2% | 33.6 | 107.7% | 74.8% | 1.0% | **70 WATCH** | **13** |
| Corning Incorporated | `GLW` | 6.7 | 7.1 | 15.6% | 30.2 | 33.0% | 19.6% | 0.6% | **70 WATCH** | **13** |
| Oracle Corporation | `ORCL` | 5.4 | 7.3 | 35.6% | 11.7 | 35.0% | 45.7% | -11.8% | **70 WATCH** | **10** |
| XIAOMI-W | `XIAOMI` | 1.6 | 1.4 | 4.0% | 17.4 | 38.8% | 22.3% | -1.3% | **70 WATCH** | **10** |
| Adobe Inc. | `ADBE` | 3.7 | 3.7 | 34.8% | 8.9 | 12.4% | 9.1% | 9.8% | **65 WATCH** | **30** |
| Tesla, Inc. | `TSLA` | 13.5 | 13.3 | 1.4% | 163.6 | 24.4% | 13.5% | 0.3% | **22** | **63 WATCH** |
| Coherent Corp. | `COHR` | 6.4 | 6.7 | 11.8% | 16.6 | 49.2% | 38.9% | -1.4% | **60 WATCH** | **35** |
| IREN LIMITED | `IREN` | 15.0 | 17.8 | -102.5% | -6.8 | -16.4% | 164.0% | -39.7% | **0** | **60** |
| Microsoft Corporation | `MSFT` | 11.8 | 12.0 | 45.1% | 22.3 | 19.9% | 19.7% | 0.4% | **59 WATCH** | **23** |
| Apple Inc. | `AAPL` | 10.7 | 10.8 | 32.6% | 35.9 | 8.5% | 10.4% | 2.1% | **5** | **58** |
| Coca-Cola Company (The) | `KO` | 8.1 | 8.7 | 34.9% | 26.6 | 6.7% | -0.1% | 1.3% | **0** | **58** |
| Bloom Energy Corporation | `BE` | 20.9 | 21.0 | 17.1% | 44.8 | 82.4% | 65.4% | 0.8% | **55 WATCH** | **48** |
| AXT Inc | `AXT` | 26.9 | 24.4 | 21.9% | 22.9 | 159.2% | 111.3% | -1.3% | **52** | **35** |
| Super Micro Computer, Inc. | `SMCI` | 0.5 | 0.7 | 13.4% | 5.9 | 22.8% | 17.3% | -39.7% | **52** | **25** |
| Lumentum Holdings Inc. | `LITE` | 24.8 | 24.2 | 28.0% | 22.9 | 65.3% | 57.0% | 0.3% | **0** | **51** |
| Netflix, Inc. | `NFLX` | 6.1 | 6.2 | 33.4% | 18.6 | 5.9% | 11.2% | 8.6% | **35** | **50** |
| Palantir Technologies Inc. | `PLTR` | 72.6 | 71.1 | 47.1% | 79.1 | 45.2% | 50.1% | 0.5% | **33** | **48** |
| Intel Corporation | `INTC` | 8.3 | 8.6 | 12.2% | 42.7 | 37.8% | 15.1% | 1.0% | **10** | **48** |
| SK hynix | `SKHYNIX` | 4.9 | 4.4 | 76.3% | 2.7 | 31.8% | 54.4% | 6.0% | **45** | **5** |
| SK hynix | `SKHY` | 4.9 | 4.4 | 76.3% | 2.7 | 31.8% | 54.4% | 6.0% | **45** | **5** |
| SamsungElec | `SAMSUNG` | 2.9 | 2.6 | 52.2% | 3.0 | 50.9% | 37.9% | 5.0% | **45** | **10** |
| Arm Holdings plc | `ARM` | 47.2 | 46.5 | 7.6% | 74.4 | 37.5% | 36.2% | 0.5% | **43** | **33** |
| Circle Internet Group, Inc. | `CRCL` | 7.2 | 6.6 | 4.9% | 56.0 | 29.6% | 26.4% | 1.0% | **43** | **33** |
| Coinbase Global, Inc. | `COIN` | 7.6 | 7.2 | -13.9% | 58.0 | 267.6% | 30.1% | 5.8% | **20** | **40** |
| SOFTBANK GROUP CORP | `SOFTBANK` | 3.5 | 6.9 | -11.6% | 16.7 | -14.5% | 6.9% | -7.8% | **0** | **40** |
| CoreWeave, Inc. | `CRWV` | 4.5 | 10.5 | -1.9% | -33.0 | 14.9% | 104.6% | -26.8% | **0** | **40** |
| Dell Technologies Inc. | `DELL` | 1.9 | 2.1 | 12.0% | 15.1 | 9.6% | 18.4% | 2.1% | **33** | **38** |
| Meta Platforms, Inc. | `META` | 7.9 | 8.0 | 34.8% | 20.5 | 10.8% | 20.8% | 1.2% | **25** | **38** |
| Amazon.com, Inc. | `AMZN` | 3.5 | 3.6 | 13.7% | 23.9 | -18.2% | 14.6% | 0.1% | **0** | **38** |
| Fluence Energy, Inc. | `FLNC` | 0.4 | 0.4 | -8.9% | -12.8 | 60.4% | 27.7% | 0.2% | **5** | **28** |
| Hyperliquid Strategies Inc | `PURR` | 266.8 | 175.1 | 9595.1% | 24.5 | 51.0% | 31.4% | — | **25** | **10** |
| BitMine Immersion Technologies, | `BMNR` | 213.5 | 208.0 | 8.4% | 23.0 | 103.2% | 421.8% | -4.0% | **25** | **25** |
| Strategy Inc | `MSTR` | 116.3 | 143.1 | -6808.1% | 2.8 | 168.2% | 2.2% | -39.0% | **25** | **25** |
| QUALCOMM Incorporated | `QCOM` | 4.2 | 4.3 | 18.5% | 16.9 | -2.8% | 4.7% | 5.6% | **25** | **15** |
| Applied Optoelectronics, Inc. | `AAOI` | 10.8 | 10.4 | -12.9% | 16.4 | 576.8% | 156.5% | -13.8% | **10** | **25** |
| Alphabet Inc. | `GOOGL` | 9.3 | 9.1 | 34.0% | 22.3 | -26.8% | 24.8% | 0.5% | **12** | **23** |

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
