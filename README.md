# OKX Long / Short Fundamental Scanner

Hourly scanner restricted to public companies exposed by the **OKX EEA TradFi / Stock Perpetual API universe**.

**Last scan:** 2026-10-29 05:56 UTC  
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
| 1 | Taiwan Semiconductor Manufactur | TSM | -0.0% | 6.6% | 3.3% | 88 | -3 | **85** | **CORE** | yes |
| 2 | Applovin Corporation | APP | -0.0% | -1.6% | -0.8% | 82 | +1 | **83** | **CORE** | yes |
| 3 | Robinhood Markets, Inc. | HOOD | -0.0% | -5.3% | -2.7% | 80 | +2 | **82** | **CORE** | yes |
| 4 | NVIDIA Corporation | NVDA | -0.0% | 1.5% | 0.7% | 82 | -1 | **81** | **CORE** | yes |
| 5 | Credo Technology Group Holding  | CRDO | -0.0% | 6.7% | 3.4% | 82 | -3 | **79** | **CORE** | yes |
| 6 | Broadcom Inc. | AVGO | 0.0% | 8.8% | 4.4% | 82 | -4 | **78** | **CORE** | yes |
| 7 | Corning Incorporated | GLW | 0.0% | 5.8% | 2.9% | 80 | -2 | **78** | **CORE** | yes |
| 8 | Applied Materials, Inc. | AMAT | 0.0% | 10.8% | 5.4% | 81 | -4 | **77** | **CORE** | yes |
| 9 | Marvell Technology, Inc. | MRVL | 0.0% | 12.6% | 6.3% | 79 | -5 | **74** | **WATCH** | yes |
| 10 | Advanced Micro Devices, Inc. | AMD | -0.0% | 13.9% | 6.9% | 79 | -6 | **73** | **WATCH** | yes |

## Final model + Price Timing — SHORT

| Rank | Company | OKX | 24h | 7d | 50/50 move | Base SHORT | Timing adj. | Final | Signal | Prev. SHORT? |
|---:|---|---|---:|---:|---:|---:|---:|---:|---|---|
| 1 | Rocket Lab Corporation | RKLB | 0.0% | 14.4% | 7.2% | 100 | +6 | **100** | **CORE** | yes |
| 2 | USA Rare Earth, Inc. | USAR | 0.0% | 8.8% | 4.4% | 100 | +4 | **100** | **CORE** | yes |
| 3 | IonQ, Inc. | IONQ | -0.0% | 4.1% | 2.0% | 88 | +2 | **90** | **CORE** | yes |
| 4 | Nebius Group N.V. | NBIS | 0.0% | 14.6% | 7.3% | 84 | +6 | **90** | **CORE** | yes |
| 5 | AST SpaceMobile, Inc. | ASTS | 0.0% | 9.1% | 4.6% | 80 | +4 | **84** | **CORE** | yes |
| 6 | Cerebras Systems Inc. | CBRS | 0.0% | 3.3% | 1.7% | 75 | +1 | **76** | **CORE** | yes |
| 7 | Moderna, Inc. | MRNA | 0.0% | 5.7% | 2.8% | 72 | +2 | **74** | **WATCH** | yes |
| 8 | Lumentum Holdings Inc. | LITE | -0.0% | 21.4% | 10.7% | 59 | +9 | **68** | **WATCH** | yes |
| 9 | Okta, Inc. | OKTA | -0.0% | 10.6% | 5.3% | 61 | +4 | **65** | **WATCH** | yes |
| 10 | IREN LIMITED | IREN | -0.0% | 13.1% | 6.5% | 60 | +5 | **65** | **WATCH** | yes |

## Combined model — LONG

Weighted score: **70% fundamental + 30% P/E trend**.

| Rank | Company | OKX | Fundamental LONG | P/E trend LONG | Combined | Signal |
|---:|---|---|---:|---:|---:|---|
| 1 | Taiwan Semiconductor Manufactur | `TSM` | 90 | 85 | **88** | **CORE** |
| 2 | Applovin Corporation | `APP` | 83 | 80 | **82** | **CORE** |
| 3 | NVIDIA Corporation | `NVDA` | 75 | 100 | **82** | **CORE** |
| 4 | Credo Technology Group Holding  | `CRDO` | 75 | 100 | **82** | **CORE** |
| 5 | Broadcom Inc. | `AVGO` | 75 | 100 | **82** | **CORE** |
| 6 | Applied Materials, Inc. | `AMAT` | 77 | 91 | **81** | **CORE** |
| 7 | Robinhood Markets, Inc. | `HOOD` | 77 | 86 | **80** | **CORE** |
| 8 | Corning Incorporated | `GLW` | 77 | 86 | **80** | **CORE** |
| 9 | Marvell Technology, Inc. | `MRVL` | 70 | 100 | **79** | **CORE** |
| 10 | Advanced Micro Devices, Inc. | `AMD` | 70 | 100 | **79** | **CORE** |

## Combined model — SHORT

Weighted score: **70% fundamental + 30% P/E trend**.

| Rank | Company | OKX | Fundamental SHORT | P/E trend SHORT | Combined | Signal |
|---:|---|---|---:|---:|---:|---|
| 1 | Rocket Lab Corporation | `RKLB` | 100 | 0 | **100** | **CORE** |
| 2 | USA Rare Earth, Inc. | `USAR` | 100 | 0 | **100** | **CORE** |
| 3 | IonQ, Inc. | `IONQ` | 88 | 0 | **88** | **CORE** |
| 4 | Nebius Group N.V. | `NBIS` | 84 | 0 | **84** | **WATCH** |
| 5 | AST SpaceMobile, Inc. | `ASTS` | 80 | 0 | **80** | **WATCH** |
| 6 | Cerebras Systems Inc. | `CBRS` | 75 | 0 | **75** | **WATCH** |
| 7 | Moderna, Inc. | `MRNA` | 72 | 0 | **72** | **WATCH** |
| 8 | Okta, Inc. | `OKTA` | 80 | 18 | **61** | **WATCH** |
| 9 | Tesla, Inc. | `TSLA` | 78 | 15 | **59** | **WATCH** |

## P/E Compression + Growth — LONG

| Rank | Company | OKX | Trail P/E | Fwd P/E | P/E change | EPS +1y | Rev +1y | Rev trend | LONG score | Signal |
|---:|---|---|---:|---:|---:|---:|---:|---|---:|---|
| 1 | NVIDIA Corporation | `NVDA` | 27.2 | 13.5 | -50.3% | 70.9% | 68.2% | decelerating | **100** | **CORE** |
| 2 | Credo Technology Group Holding  | `CRDO` | 61.6 | 17.9 | -71.0% | 53.9% | 55.0% | decelerating | **100** | **CORE** |
| 3 | Broadcom Inc. | `AVGO` | 44.9 | 18.1 | -59.8% | 66.9% | 64.4% | decelerating | **100** | **CORE** |
| 4 | Marvell Technology, Inc. | `MRVL` | 82.8 | 34.3 | -58.5% | 73.6% | 63.3% | accelerating | **100** | **CORE** |
| 5 | Advanced Micro Devices, Inc. | `AMD` | 147.6 | 36.5 | -75.3% | 108.3% | 75.1% | accelerating | **100** | **CORE** |
| 6 | AXT Inc | `AXT` | 1609.5 | 28.6 | -98.2% | 159.2% | 111.3% | decelerating | **96** | **CORE** |
| 7 | Oracle Corporation | `ORCL` | 22.7 | 13.1 | -42.0% | 35.0% | 45.7% | accelerating | **95** | **CORE** |
| 8 | Coherent Corp. | `COHR` | 58.2 | 17.2 | -70.4% | 48.0% | 38.1% | decelerating | **95** | **CORE** |
| 9 | Arm Holdings plc | `ARM` | 243.2 | 76.9 | -68.4% | 37.5% | 36.4% | accelerating | **95** | **CORE** |
| 10 | Bloom Energy Corporation | `BE` | 138.2 | 43.0 | -68.9% | 62.7% | 56.0% | decelerating | **92** | **CORE** |

## P/E Expansion + Weakening — SHORT

| Rank | Company | OKX | Trail P/E | Fwd P/E | P/E change | EPS +1y | Rev +1y | Rev trend | SHORT score | Signal |
|---:|---|---|---:|---:|---:|---:|---:|---|---:|---|
| 1 | SOFTBANK GROUP CORP | `SOFTBANK` | 5.5 | 16.1 | 191.0% | -14.5% | 6.9% | decelerating | **86** | **CORE** |
| 2 | Hyperliquid Strategies Inc | `PURR` | 3.1 | 26.9 | 767.6% | 51.0% | 31.4% | decelerating | **55** | **WATCH** |
| 3 | Amazon.com, Inc. | `AMZN` | 20.5 | 24.4 | 18.9% | -18.3% | 14.6% | decelerating | **52** | **WATCH** |
| 4 | Alphabet Inc. | `GOOGL` | 17.0 | 21.4 | 26.1% | -26.4% | 25.5% | accelerating | **50** | **WATCH** |

## Top SHORT candidates

| Rank | Company | OKX market | SHORT score | Signal | P/S | EV/S | Op margin | Fwd P/E | Rev +1y | FCF yield |
|---:|---|---|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Rocket Lab Corporation | `RKLB-USDT-SWAP` | **100** | **CORE** | 48.7 | 42.8 | -24.6% | 1019.3 | 38.2% | -0.7% |
| 2 | USA Rare Earth, Inc. | `USAR-USDT-SWAP` | **100** | **CORE** | 298.6 | 79.5 | -795.6% | 349.3 | 870.1% | -7.2% |
| 3 | IonQ, Inc. | `IONQ-USDT-SWAP` | **88** | **CORE** | 56.5 | 41.8 | -408.2% | -24.1 | 77.6% | -0.6% |
| 4 | Nebius Group N.V. | `NBIS-USDT-SWAP` | **84** | **WATCH** | 36.6 | 38.5 | -0.2% | -50.7 | 266.0% | -19.4% |
| 5 | Okta, Inc. | `OKTA-USDT-SWAP` | **80** | **CORE** | 12.7 | 11.9 | 13.3% | 50.9 | 10.1% | 2.7% |
| 6 | AST SpaceMobile, Inc. | `ASTS-USDT-SWAP` | **80** | **WATCH** | 142.8 | 120.5 | -544.6% | -32.9 | 264.2% | -10.9% |
| 7 | Tesla, Inc. | `TSLA-USDT-SWAP` | **78** | **WATCH** | 15.4 | 15.2 | 5.4% | 187.5 | 13.5% | 0.3% |
| 8 | Cerebras Systems Inc. | `CBRS-USDT-SWAP` | **75** | **WATCH** | 39.3 | 29.8 | -265.0% | 88.4 | 232.7% | — |
| 9 | Moderna, Inc. | `MRNA-USDT-SWAP` | **72** | **WATCH** | 38.4 | 36.6 | -557.9% | -46.7 | 16.3% | 0.3% |

## Top LONG candidates

| Rank | Company | OKX market | LONG score | Signal | P/S | EV/S | Op margin | Fwd P/E | Rev +1y | FCF yield |
|---:|---|---|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Taiwan Semiconductor Manufactur | `TSM-USDT-SWAP` | **90** | **CORE** | 0.5 | 3.0 | 58.7% | 18.8 | 37.6% | 52.8% |
| 2 | Applovin Corporation | `APP-USDT-SWAP` | **83** | **CORE** | 12.8 | 12.8 | 77.7% | 12.7 | 25.3% | 3.6% |
| 3 | Corning Incorporated | `GLW-USDT-SWAP` | **77** | **WATCH** | 6.4 | 7.1 | 18.8% | 29.0 | 21.1% | 0.8% |
| 4 | Robinhood Markets, Inc. | `HOOD-USDT-SWAP` | **77** | **WATCH** | 16.7 | 17.1 | 43.9% | 27.9 | 29.0% | — |
| 5 | Applied Materials, Inc. | `AMAT-USDT-SWAP` | **77** | **WATCH** | 10.7 | 10.6 | 33.7% | 22.5 | 35.3% | 0.9% |
| 6 | Credo Technology Group Holding  | `CRDO-USDT-SWAP` | **75** | **WATCH** | 20.5 | 20.1 | 25.2% | 17.9 | 55.0% | 0.8% |
| 7 | Micron Technology, Inc. | `MU-USDT-SWAP` | **75** | **CORE** | 8.4 | 8.1 | 80.7% | 4.8 | 15.7% | 2.6% |
| 8 | Broadcom Inc. | `AVGO-USDT-SWAP` | **75** | **WATCH** | 18.8 | 19.2 | 54.3% | 18.1 | 64.4% | 1.8% |
| 9 | Sandisk Corporation | `SNDK-USDT-SWAP` | **75** | **CORE** | 10.0 | 9.9 | 78.5% | 5.3 | 18.9% | 3.8% |
| 10 | NVIDIA Corporation | `NVDA-USDT-SWAP` | **75** | **WATCH** | 17.2 | 17.1 | 66.2% | 13.5 | 68.2% | 0.8% |

## Analyst consensus (12-month price target) — most upside

| Rank | Company | OKX | Price | Analyst mean target | Gap | Analysts | Currency |
|---:|---|---|---:|---:|---:|---:|---|
| 1 | IREN LIMITED | `IREN` | 28.84 | 76.92 | **166.7%** | 18 | USD |
| 2 | Cerebras Systems Inc. | `CBRS` | 112.56 | 282.55 | **151.0%** | 11 | USD |
| 3 | Hyperliquid Strategies Inc | `PURR` | 9.97 | 22.32 | **123.9%** | 4 | USD |
| 4 | CoreWeave, Inc. | `CRWV` | 63.93 | 134.58 | **110.5%** | 38 | USD |
| 5 | BitMine Immersion Technologies, | `BMNR` | 22.05 | 45.87 | **108.0%** | 3 | USD |
| 6 | SamsungElec | `SAMSUNG` | 233000.00 | 478905.62 | **105.5%** | 36 | KRW |
| 7 | SK hynix | `SKHYNIX` | 1559000.00 | 3145761.50 | **101.8%** | 38 | KRW |
| 8 | IonQ, Inc. | `IONQ` | 32.43 | 64.06 | **97.5%** | 14 | USD |
| 9 | Applied Optoelectronics, Inc. | `AAOI` | 82.22 | 156.00 | **89.7%** | 5 | USD |
| 10 | Applovin Corporation | `APP` | 259.97 | 469.27 | **80.5%** | 31 | USD |
| 11 | AST SpaceMobile, Inc. | `ASTS` | 42.30 | 74.68 | **76.6%** | 12 | USD |
| 12 | Rocket Lab Corporation | `RKLB` | 58.60 | 102.15 | **74.3%** | 20 | USD |
| 13 | Strategy Inc | `MSTR` | 145.16 | 239.27 | **64.8%** | 15 | USD |
| 14 | Coherent Corp. | `COHR` | 239.59 | 394.40 | **64.6%** | 25 | USD |
| 15 | SOFTBANK GROUP CORP | `SOFTBANK` | 4744.00 | 7782.47 | **64.0%** | 18 | JPY |

## Analyst consensus (12-month price target) — most downside

| Rank | Company | OKX | Price | Analyst mean target | Gap | Analysts | Currency |
|---:|---|---|---:|---:|---:|---:|---|
| 1 | Moderna, Inc. | `MRNA` | 214.16 | 138.37 | **-35.4%** | 19 | USD |
| 2 | Okta, Inc. | `OKTA` | 222.66 | 214.72 | **-3.6%** | 43 | USD |
| 3 | Apple Inc. | `AAPL` | 343.83 | 332.39 | **-3.3%** | 38 | USD |

Price/target uses the underlying Yahoo Finance share quote, not the OKX derivative. Minimum 3 analysts; unreliable price scales and missing coverage excluded. Targets are analyst opinions, not guaranteed forecasts.

## All OKX companies — our ratio + LONG/SHORT scores

| Company | OKX | P/S | EV/S | Op margin | Fwd P/E | EPS +1y | Rev +1y | FCF yield | LONG | SHORT |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Rocket Lab Corporation | `RKLB` | 48.7 | 42.8 | -24.6% | 1019.3 | 66.8% | 38.2% | -0.7% | **0** | **100 CORE** |
| USA Rare Earth, Inc. | `USAR` | 298.6 | 79.5 | -795.6% | 349.3 | 105.3% | 870.1% | -7.2% | **0** | **100 CORE** |
| Taiwan Semiconductor Manufactur | `TSM` | 0.5 | 3.0 | 58.7% | 18.8 | 33.6% | 37.6% | 52.8% | **90 CORE** | **10** |
| IonQ, Inc. | `IONQ` | 56.5 | 41.8 | -408.2% | -24.1 | 21.3% | 77.6% | -0.6% | **0** | **88 CORE** |
| Nebius Group N.V. | `NBIS` | 36.6 | 38.5 | -0.2% | -50.7 | -191.4% | 266.0% | -19.4% | **0** | **84 WATCH** |
| Applovin Corporation | `APP` | 12.8 | 12.8 | 77.7% | 12.7 | 26.3% | 25.3% | 3.6% | **83 CORE** | **10** |
| Okta, Inc. | `OKTA` | 12.7 | 11.9 | 13.3% | 50.9 | 11.4% | 10.1% | 2.7% | **8** | **80 CORE** |
| AST SpaceMobile, Inc. | `ASTS` | 142.8 | 120.5 | -544.6% | -32.9 | 44.3% | 264.2% | -10.9% | **0** | **80 WATCH** |
| Tesla, Inc. | `TSLA` | 15.4 | 15.2 | 5.4% | 187.5 | 23.8% | 13.5% | 0.3% | **12** | **78 WATCH** |
| Robinhood Markets, Inc. | `HOOD` | 16.7 | 17.1 | 43.9% | 27.9 | 41.9% | 29.0% | — | **77 WATCH** | **5** |
| Corning Incorporated | `GLW` | 6.4 | 7.1 | 18.8% | 29.0 | 34.0% | 21.1% | 0.8% | **77 WATCH** | **13** |
| Applied Materials, Inc. | `AMAT` | 10.7 | 10.6 | 33.7% | 22.5 | 44.6% | 35.3% | 0.9% | **77 WATCH** | **3** |
| NVIDIA Corporation | `NVDA` | 17.2 | 17.1 | 66.2% | 13.5 | 70.9% | 68.2% | 0.8% | **75 WATCH** | **18** |
| Credo Technology Group Holding  | `CRDO` | 20.5 | 20.1 | 25.2% | 17.9 | 53.9% | 55.0% | 0.8% | **75 WATCH** | **28** |
| Broadcom Inc. | `AVGO` | 18.8 | 19.2 | 54.3% | 18.1 | 66.9% | 64.4% | 1.8% | **75 WATCH** | **28** |
| Sandisk Corporation | `SNDK` | 10.0 | 9.9 | 78.5% | 5.3 | 24.0% | 18.9% | 3.8% | **75 CORE** | **10** |
| Micron Technology, Inc. | `MU` | 8.4 | 8.1 | 80.7% | 4.8 | 17.2% | 15.7% | 2.6% | **75 CORE** | **30** |
| Western Digital Corporation | `WDC` | 10.2 | 10.2 | 47.7% | 9.8 | 63.4% | 40.5% | 1.8% | **75 WATCH** | **18** |
| Cerebras Systems Inc. | `CBRS` | 39.3 | 29.8 | -265.0% | 88.4 | 371.3% | 232.7% | — | **0** | **75 WATCH** |
| Moderna, Inc. | `MRNA` | 38.4 | 36.6 | -557.9% | -46.7 | 42.5% | 16.3% | 0.3% | **0** | **72 WATCH** |
| Marvell Technology, Inc. | `MRVL` | 23.9 | 23.5 | 16.7% | 34.3 | 73.6% | 63.3% | 1.1% | **70 WATCH** | **13** |
| Advanced Micro Devices, Inc. | `AMD` | 22.9 | 22.6 | 17.2% | 36.5 | 108.3% | 75.1% | 0.9% | **70 WATCH** | **13** |
| Oracle Corporation | `ORCL` | 6.1 | 8.0 | 35.6% | 13.1 | 35.0% | 45.7% | -10.5% | **70 WATCH** | **10** |
| XIAOMI-W | `XIAOMI` | 1.5 | 1.3 | 4.0% | 17.2 | 36.8% | 19.7% | -1.3% | **70 WATCH** | **10** |
| Adobe Inc. | `ADBE` | 3.7 | 3.8 | 34.8% | 9.1 | 12.4% | 9.1% | 9.6% | **65 WATCH** | **30** |
| Coherent Corp. | `COHR` | 6.6 | 6.9 | 11.8% | 17.2 | 48.0% | 38.1% | -1.4% | **60 WATCH** | **35** |
| IREN LIMITED | `IREN` | 16.5 | 18.8 | -102.5% | -7.2 | -16.4% | 164.0% | -36.2% | **0** | **60** |
| Microsoft Corporation | `MSFT` | 11.9 | 12.0 | 45.1% | 22.4 | 19.9% | 19.7% | 0.4% | **59 WATCH** | **23** |
| Lumentum Holdings Inc. | `LITE` | 27.5 | 26.8 | 28.0% | 25.6 | 63.9% | 57.6% | 0.3% | **0** | **59** |
| Apple Inc. | `AAPL` | 10.7 | 10.8 | 32.6% | 36.0 | 8.4% | 10.4% | 2.1% | **5** | **58** |
| Coca-Cola Company (The) | `KO` | 7.7 | 8.3 | 33.4% | 26.0 | 5.7% | -2.7% | 1.1% | **0** | **58** |
| Meta Platforms, Inc. | `META` | 6.6 | 6.6 | 35.4% | 17.4 | 16.7% | 21.6% | 1.1% | **57 WATCH** | **38** |
| Dell Technologies Inc. | `DELL` | 2.1 | 2.2 | 12.0% | 16.3 | 16.2% | 19.2% | 1.9% | **57 WATCH** | **38** |
| Bloom Energy Corporation | `BE` | 17.6 | 17.7 | 18.5% | 43.0 | 62.7% | 56.0% | -0.0% | **40** | **55** |
| Super Micro Computer, Inc. | `SMCI` | 0.6 | 0.8 | 13.4% | 6.4 | 19.7% | 16.3% | -35.1% | **52** | **45** |
| AXT Inc | `AXT` | 33.6 | 31.0 | 21.9% | 28.6 | 159.2% | 111.3% | -1.1% | **52** | **35** |
| Netflix, Inc. | `NFLX` | 5.2 | 5.3 | 34.6% | 16.4 | 5.1% | 10.7% | 9.9% | **35** | **50** |
| Palantir Technologies Inc. | `PLTR` | 76.8 | 75.4 | 47.1% | 84.2 | 44.7% | 50.4% | 0.5% | **33** | **48** |
| Intel Corporation | `INTC` | 8.9 | 9.1 | 12.2% | 43.9 | 41.6% | 15.8% | 1.0% | **10** | **48** |
| SK hynix | `SKHYNIX` | 5.8 | 5.2 | 76.3% | 3.1 | 35.4% | 55.9% | 5.1% | **45** | **5** |
| SK hynix | `SKHY` | 5.8 | 5.2 | 76.3% | 3.1 | 35.4% | 55.9% | 5.1% | **45** | **5** |
| SamsungElec | `SAMSUNG` | 3.1 | 3.0 | 52.2% | 3.2 | 51.5% | 38.3% | 4.6% | **45** | **10** |
| Coinbase Global, Inc. | `COIN` | 7.1 | 6.7 | -13.9% | 53.8 | 283.2% | 30.0% | 6.2% | **20** | **40** |
| SOFTBANK GROUP CORP | `SOFTBANK` | 3.4 | 6.7 | -11.6% | 16.1 | -14.5% | 6.9% | -8.1% | **0** | **40** |
| CoreWeave, Inc. | `CRWV` | 4.6 | 10.7 | -1.9% | -32.5 | 9.7% | 105.6% | -25.8% | **0** | **40** |
| Amazon.com, Inc. | `AMZN` | 3.5 | 3.7 | 13.7% | 24.4 | -18.3% | 14.6% | 0.1% | **0** | **38** |
| Arm Holdings plc | `ARM` | 48.9 | 48.2 | 7.6% | 76.9 | 37.5% | 36.4% | 0.5% | **35** | **33** |
| Circle Internet Group, Inc. | `CRCL` | 7.1 | 6.6 | 4.9% | 55.3 | 27.1% | 27.3% | 1.0% | **35** | **33** |
| Fluence Energy, Inc. | `FLNC` | 0.5 | 0.4 | -8.9% | -11.7 | 59.3% | 25.4% | 0.2% | **5** | **28** |
| Hyperliquid Strategies Inc | `PURR` | 293.3 | 193.9 | 9595.1% | 26.9 | 51.0% | 31.4% | — | **25** | **10** |
| Strategy Inc | `MSTR` | 123.4 | 149.6 | -6808.1% | 6.1 | 168.0% | 2.5% | -36.7% | **25** | **25** |
| BitMine Immersion Technologies, | `BMNR` | 217.4 | 211.8 | 8.4% | 23.5 | 103.2% | 421.8% | -3.9% | **25** | **25** |
| QUALCOMM Incorporated | `QCOM` | 4.4 | 4.5 | 18.5% | 18.0 | -2.8% | 4.6% | 5.2% | **25** | **15** |
| Applied Optoelectronics, Inc. | `AAOI` | 11.7 | 11.3 | -12.9% | 17.9 | 576.8% | 156.5% | -12.7% | **10** | **25** |
| Alphabet Inc. | `GOOGL` | 8.9 | 8.7 | 34.0% | 21.4 | -26.4% | 25.5% | 0.6% | **12** | **23** |

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
