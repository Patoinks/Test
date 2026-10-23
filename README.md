# OKX Long / Short Fundamental Scanner

Hourly scanner restricted to public companies exposed by the **OKX EEA TradFi / Stock Perpetual API universe**.

**Last scan:** 2026-10-23 07:39 UTC  
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
| 1 | Taiwan Semiconductor Manufactur | TSM | -0.0% | -0.1% | -0.0% | 88 | +0 | **88** | **CORE** | yes |
| 2 | Corning Incorporated | GLW | 0.0% | -6.1% | -3.0% | 83 | +2 | **85** | **CORE** | yes |
| 3 | Credo Technology Group Holding  | CRDO | -0.0% | -4.1% | -2.0% | 82 | +2 | **84** | **CORE** | yes |
| 4 | Applied Materials, Inc. | AMAT | 0.0% | -8.2% | -4.1% | 81 | +3 | **84** | **CORE** | yes |
| 5 | Sandisk Corporation | SNDK | -0.0% | -3.0% | -1.5% | 82 | +1 | **83** | **CORE** | yes |
| 6 | Broadcom Inc. | AVGO | 0.0% | -1.7% | -0.8% | 82 | +1 | **83** | **CORE** | yes |
| 7 | NVIDIA Corporation | NVDA | -0.0% | -0.9% | -0.4% | 82 | +0 | **82** | **CORE** | yes |
| 8 | Applovin Corporation | APP | 0.0% | -0.7% | -0.3% | 82 | +0 | **82** | **CORE** | yes |
| 9 | Robinhood Markets, Inc. | HOOD | -0.0% | -2.3% | -1.2% | 80 | +1 | **81** | **CORE** | yes |
| 10 | Advanced Micro Devices, Inc. | AMD | 0.0% | -3.9% | -2.0% | 79 | +2 | **81** | **CORE** | yes |

## Final model + Price Timing — SHORT

| Rank | Company | OKX | 24h | 7d | 50/50 move | Base SHORT | Timing adj. | Final | Signal | Prev. SHORT? |
|---:|---|---|---:|---:|---:|---:|---:|---:|---|---|
| 1 | Rocket Lab Corporation | RKLB | -0.0% | 0.7% | 0.4% | 100 | +0 | **100** | **CORE** | yes |
| 2 | USA Rare Earth, Inc. | USAR | -0.0% | -8.6% | -4.3% | 100 | -3 | **97** | **CORE** | yes |
| 3 | IonQ, Inc. | IONQ | 0.0% | -0.4% | -0.2% | 85 | +0 | **85** | **CORE** | yes |
| 4 | AST SpaceMobile, Inc. | ASTS | -0.0% | -4.6% | -2.3% | 80 | -2 | **78** | **CORE** | yes |
| 5 | Nebius Group N.V. | NBIS | 0.0% | -3.8% | -1.9% | 80 | -2 | **78** | **CORE** | yes |
| 6 | Cerebras Systems Inc. | CBRS | -0.0% | -14.4% | -7.2% | 75 | -6 | **69** | **WATCH** | yes |
| 7 | Moderna, Inc. | MRNA | -0.0% | -7.1% | -3.5% | 72 | -3 | **69** | **WATCH** | yes |
| 8 | Okta, Inc. | OKTA | -0.0% | 7.5% | 3.8% | 60 | +3 | **63** | **WATCH** | yes |
| 9 | Tesla, Inc. | TSLA | 0.0% | 5.6% | 2.8% | 59 | +2 | **61** | **WATCH** | yes |

## Combined model — LONG

Weighted score: **70% fundamental + 30% P/E trend**.

| Rank | Company | OKX | Fundamental LONG | P/E trend LONG | Combined | Signal |
|---:|---|---|---:|---:|---:|---|
| 1 | Taiwan Semiconductor Manufactur | `TSM` | 90 | 85 | **88** | **CORE** |
| 2 | Corning Incorporated | `GLW` | 77 | 96 | **83** | **CORE** |
| 3 | Applovin Corporation | `APP` | 83 | 80 | **82** | **CORE** |
| 4 | Sandisk Corporation | `SNDK` | 82 | 82 | **82** | **CORE** |
| 5 | Credo Technology Group Holding  | `CRDO` | 75 | 100 | **82** | **CORE** |
| 6 | Broadcom Inc. | `AVGO` | 75 | 100 | **82** | **CORE** |
| 7 | NVIDIA Corporation | `NVDA` | 75 | 100 | **82** | **CORE** |
| 8 | Applied Materials, Inc. | `AMAT` | 77 | 91 | **81** | **CORE** |
| 9 | Robinhood Markets, Inc. | `HOOD` | 77 | 86 | **80** | **CORE** |
| 10 | Advanced Micro Devices, Inc. | `AMD` | 70 | 100 | **79** | **CORE** |

## Combined model — SHORT

Weighted score: **70% fundamental + 30% P/E trend**.

| Rank | Company | OKX | Fundamental SHORT | P/E trend SHORT | Combined | Signal |
|---:|---|---|---:|---:|---:|---|
| 1 | Rocket Lab Corporation | `RKLB` | 100 | 0 | **100** | **CORE** |
| 2 | USA Rare Earth, Inc. | `USAR` | 100 | 0 | **100** | **CORE** |
| 3 | IonQ, Inc. | `IONQ` | 85 | 0 | **85** | **CORE** |
| 4 | AST SpaceMobile, Inc. | `ASTS` | 80 | 0 | **80** | **WATCH** |
| 5 | Nebius Group N.V. | `NBIS` | 80 | 0 | **80** | **WATCH** |
| 6 | Cerebras Systems Inc. | `CBRS` | 75 | 0 | **75** | **WATCH** |
| 7 | Moderna, Inc. | `MRNA` | 72 | 0 | **72** | **WATCH** |
| 8 | Okta, Inc. | `OKTA` | 80 | 13 | **60** | **WATCH** |
| 9 | Tesla, Inc. | `TSLA` | 78 | 15 | **59** | **WATCH** |

## P/E Compression + Growth — LONG

| Rank | Company | OKX | Trail P/E | Fwd P/E | P/E change | EPS +1y | Rev +1y | Rev trend | LONG score | Signal |
|---:|---|---|---:|---:|---:|---:|---:|---|---:|---|
| 1 | Credo Technology Group Holding  | `CRDO` | 57.7 | 16.8 | -71.0% | 53.9% | 55.0% | decelerating | **100** | **CORE** |
| 2 | Broadcom Inc. | `AVGO` | 41.3 | 16.7 | -59.6% | 66.7% | 64.3% | decelerating | **100** | **CORE** |
| 3 | NVIDIA Corporation | `NVDA` | 26.8 | 13.3 | -50.3% | 70.9% | 68.2% | decelerating | **100** | **CORE** |
| 4 | Advanced Micro Devices, Inc. | `AMD` | 141.1 | 32.2 | -77.2% | 107.7% | 74.9% | accelerating | **100** | **CORE** |
| 5 | Marvell Technology, Inc. | `MRVL` | 80.4 | 30.5 | -62.1% | 73.7% | 63.3% | accelerating | **100** | **CORE** |
| 6 | Corning Incorporated | `GLW` | 56.9 | 28.2 | -50.4% | 33.6% | 20.0% | accelerating | **96** | **CORE** |
| 7 | AXT Inc | `AXT` | 1031.2 | 22.9 | -97.8% | 159.2% | 111.3% | decelerating | **96** | **CORE** |
| 8 | Oracle Corporation | `ORCL` | 19.7 | 11.4 | -41.9% | 35.0% | 45.7% | accelerating | **95** | **CORE** |
| 9 | Coherent Corp. | `COHR` | 50.4 | 14.9 | -70.4% | 48.3% | 38.3% | decelerating | **95** | **CORE** |
| 10 | Arm Holdings plc | `ARM` | 233.4 | 68.5 | -70.7% | 37.5% | 36.4% | accelerating | **95** | **CORE** |

## P/E Expansion + Weakening — SHORT

| Rank | Company | OKX | Trail P/E | Fwd P/E | P/E change | EPS +1y | Rev +1y | Rev trend | SHORT score | Signal |
|---:|---|---|---:|---:|---:|---:|---:|---|---:|---|
| 1 | SOFTBANK GROUP CORP | `SOFTBANK` | 5.0 | 14.5 | 191.0% | -14.5% | 6.9% | decelerating | **86** | **CORE** |
| 2 | Hyperliquid Strategies Inc | `PURR` | 2.7 | 23.5 | 767.6% | 51.0% | 31.4% | decelerating | **55** | **WATCH** |
| 3 | Amazon.com, Inc. | `AMZN` | 20.1 | 24.0 | 19.2% | -18.2% | 14.6% | decelerating | **52** | **WATCH** |
| 4 | Alphabet Inc. | `GOOGL` | 16.3 | 21.1 | 29.8% | -26.6% | 25.3% | accelerating | **50** | **WATCH** |

## Top SHORT candidates

| Rank | Company | OKX market | SHORT score | Signal | P/S | EV/S | Op margin | Fwd P/E | Rev +1y | FCF yield |
|---:|---|---|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Rocket Lab Corporation | `RKLB-USDT-SWAP` | **100** | **CORE** | 42.6 | 37.0 | -24.6% | 890.9 | 38.2% | -0.8% |
| 2 | USA Rare Earth, Inc. | `USAR-USDT-SWAP` | **100** | **CORE** | 274.4 | 63.7 | -795.6% | 321.0 | 870.1% | -7.9% |
| 3 | IonQ, Inc. | `IONQ-USDT-SWAP` | **85** | **CORE** | 51.2 | 39.8 | -408.2% | -23.2 | 77.6% | -0.7% |
| 4 | Nebius Group N.V. | `NBIS-USDT-SWAP` | **80** | **WATCH** | 29.8 | 33.8 | -0.2% | -44.2 | 266.0% | -23.8% |
| 5 | Okta, Inc. | `OKTA-USDT-SWAP` | **80** | **CORE** | 11.5 | 10.7 | 13.3% | 46.0 | 10.0% | 2.9% |
| 6 | AST SpaceMobile, Inc. | `ASTS-USDT-SWAP` | **80** | **WATCH** | 130.9 | 111.3 | -544.6% | -30.1 | 247.3% | -11.9% |
| 7 | Tesla, Inc. | `TSLA-USDT-SWAP` | **78** | **WATCH** | 14.3 | 14.5 | 1.4% | 171.1 | 13.3% | 0.3% |
| 8 | Cerebras Systems Inc. | `CBRS-USDT-SWAP` | **75** | **WATCH** | 38.0 | 28.6 | -265.0% | 85.5 | 232.7% | — |
| 9 | Moderna, Inc. | `MRNA-USDT-SWAP` | **72** | **WATCH** | 36.3 | 34.6 | -557.9% | -44.7 | 15.8% | 0.4% |

## Top LONG candidates

| Rank | Company | OKX market | LONG score | Signal | P/S | EV/S | Op margin | Fwd P/E | Rev +1y | FCF yield |
|---:|---|---|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Taiwan Semiconductor Manufactur | `TSM-USDT-SWAP` | **90** | **CORE** | 0.4 | 2.8 | 58.7% | 17.6 | 37.5% | 56.3% |
| 2 | Applovin Corporation | `APP-USDT-SWAP` | **83** | **CORE** | 13.0 | 13.0 | 77.7% | 12.9 | 26.0% | 3.6% |
| 3 | Sandisk Corporation | `SNDK-USDT-SWAP` | **82** | **CORE** | 9.0 | 8.9 | 78.5% | 4.7 | 18.9% | 4.2% |
| 4 | Corning Incorporated | `GLW-USDT-SWAP` | **77** | **WATCH** | 6.3 | 6.7 | 15.6% | 28.2 | 20.0% | 0.7% |
| 5 | Robinhood Markets, Inc. | `HOOD-USDT-SWAP` | **77** | **WATCH** | 17.6 | 17.4 | 43.9% | 28.3 | 29.3% | — |
| 6 | Applied Materials, Inc. | `AMAT-USDT-SWAP` | **77** | **WATCH** | 9.7 | 9.6 | 33.7% | 20.3 | 35.3% | 1.0% |
| 7 | Credo Technology Group Holding  | `CRDO-USDT-SWAP` | **75** | **WATCH** | 19.2 | 18.8 | 25.2% | 16.8 | 55.0% | 0.8% |
| 8 | Broadcom Inc. | `AVGO-USDT-SWAP` | **75** | **WATCH** | 17.3 | 17.7 | 54.3% | 16.7 | 64.3% | 2.0% |
| 9 | Micron Technology, Inc. | `MU-USDT-SWAP` | **75** | **CORE** | 7.3 | 7.0 | 80.7% | 4.1 | 15.7% | 3.0% |
| 10 | NVIDIA Corporation | `NVDA-USDT-SWAP` | **75** | **WATCH** | 16.9 | 16.8 | 66.2% | 13.3 | 68.2% | 0.8% |

## Analyst consensus (12-month price target) — most upside

| Rank | Company | OKX | Price | Analyst mean target | Gap | Analysts | Currency |
|---:|---|---|---:|---:|---:|---:|---|
| 1 | Cerebras Systems Inc. | `CBRS` | 108.94 | 282.55 | **159.4%** | 11 | USD |
| 2 | Hyperliquid Strategies Inc | `PURR` | 8.68 | 22.32 | **157.2%** | 4 | USD |
| 3 | CoreWeave, Inc. | `CRWV` | 55.60 | 136.21 | **145.0%** | 38 | USD |
| 4 | SK hynix | `SKHYNIX` | 1277000.00 | 3096288.00 | **142.5%** | 38 | KRW |
| 5 | Applied Optoelectronics, Inc. | `AAOI` | 68.07 | 160.00 | **135.1%** | 5 | USD |
| 6 | SamsungElec | `SAMSUNG` | 215500.00 | 478905.62 | **122.2%** | 36 | KRW |
| 7 | IonQ, Inc. | `IONQ` | 31.16 | 64.06 | **105.6%** | 14 | USD |
| 8 | BitMine Immersion Technologies, | `BMNR` | 22.50 | 45.87 | **103.9%** | 3 | USD |
| 9 | Rocket Lab Corporation | `RKLB` | 51.22 | 102.15 | **99.4%** | 20 | USD |
| 10 | AST SpaceMobile, Inc. | `ASTS` | 38.77 | 74.28 | **91.6%** | 12 | USD |
| 11 | Coherent Corp. | `COHR` | 207.82 | 394.79 | **90.0%** | 24 | USD |
| 12 | Oracle Corporation | `ORCL` | 125.54 | 236.54 | **88.4%** | 41 | USD |
| 13 | Micron Technology, Inc. | `MU` | 856.49 | 1561.91 | **82.4%** | 45 | USD |
| 14 | SOFTBANK GROUP CORP | `SOFTBANK` | 4276.00 | 7782.47 | **82.0%** | 18 | JPY |
| 15 | Applovin Corporation | `APP` | 264.28 | 476.85 | **80.4%** | 31 | USD |

## Analyst consensus (12-month price target) — most downside

| Rank | Company | OKX | Price | Analyst mean target | Gap | Analysts | Currency |
|---:|---|---|---:|---:|---:|---:|---|
| 1 | Moderna, Inc. | `MRNA` | 202.63 | 135.84 | **-33.0%** | 19 | USD |
| 2 | Apple Inc. | `AAPL` | 348.22 | 328.35 | **-5.7%** | 39 | USD |
| 3 | Coca-Cola Company (The) | `KO` | 95.34 | 95.12 | **-0.2%** | 24 | USD |

Price/target uses the underlying Yahoo Finance share quote, not the OKX derivative. Minimum 3 analysts; unreliable price scales and missing coverage excluded. Targets are analyst opinions, not guaranteed forecasts.

## All OKX companies — our ratio + LONG/SHORT scores

| Company | OKX | P/S | EV/S | Op margin | Fwd P/E | EPS +1y | Rev +1y | FCF yield | LONG | SHORT |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Rocket Lab Corporation | `RKLB` | 42.6 | 37.0 | -24.6% | 890.9 | 66.8% | 38.2% | -0.8% | **0** | **100 CORE** |
| USA Rare Earth, Inc. | `USAR` | 274.4 | 63.7 | -795.6% | 321.0 | 105.3% | 870.1% | -7.9% | **0** | **100 CORE** |
| Taiwan Semiconductor Manufactur | `TSM` | 0.4 | 2.8 | 58.7% | 17.6 | 33.6% | 37.5% | 56.3% | **90 CORE** | **10** |
| IonQ, Inc. | `IONQ` | 51.2 | 39.8 | -408.2% | -23.2 | 21.3% | 77.6% | -0.7% | **0** | **85 CORE** |
| Applovin Corporation | `APP` | 13.0 | 13.0 | 77.7% | 12.9 | 27.1% | 26.0% | 3.6% | **83 CORE** | **10** |
| Sandisk Corporation | `SNDK` | 9.0 | 8.9 | 78.5% | 4.7 | 24.0% | 18.9% | 4.2% | **82 CORE** | **10** |
| Okta, Inc. | `OKTA` | 11.5 | 10.7 | 13.3% | 46.0 | 11.4% | 10.0% | 2.9% | **8** | **80 CORE** |
| AST SpaceMobile, Inc. | `ASTS` | 130.9 | 111.3 | -544.6% | -30.1 | 44.3% | 247.3% | -11.9% | **0** | **80 WATCH** |
| Nebius Group N.V. | `NBIS` | 29.8 | 33.8 | -0.2% | -44.2 | -191.4% | 266.0% | -23.8% | **0** | **80 WATCH** |
| Tesla, Inc. | `TSLA` | 14.3 | 14.5 | 1.4% | 171.1 | 23.7% | 13.3% | 0.3% | **12** | **78 WATCH** |
| Corning Incorporated | `GLW` | 6.3 | 6.7 | 15.6% | 28.2 | 33.6% | 20.0% | 0.7% | **77 WATCH** | **13** |
| Applied Materials, Inc. | `AMAT` | 9.7 | 9.6 | 33.7% | 20.3 | 44.6% | 35.3% | 1.0% | **77 WATCH** | **3** |
| Robinhood Markets, Inc. | `HOOD` | 17.6 | 17.4 | 43.9% | 28.3 | 36.5% | 29.3% | — | **77 WATCH** | **5** |
| Credo Technology Group Holding  | `CRDO` | 19.2 | 18.8 | 25.2% | 16.8 | 53.9% | 55.0% | 0.8% | **75 WATCH** | **28** |
| Broadcom Inc. | `AVGO` | 17.3 | 17.7 | 54.3% | 16.7 | 66.7% | 64.3% | 2.0% | **75 WATCH** | **28** |
| NVIDIA Corporation | `NVDA` | 16.9 | 16.8 | 66.2% | 13.3 | 70.9% | 68.2% | 0.8% | **75 WATCH** | **18** |
| Micron Technology, Inc. | `MU` | 7.3 | 7.0 | 80.7% | 4.1 | 17.2% | 15.7% | 3.0% | **75 CORE** | **30** |
| Western Digital Corporation | `WDC` | 10.3 | 9.9 | 43.6% | 10.0 | 61.5% | 37.9% | 1.7% | **75 WATCH** | **18** |
| Cerebras Systems Inc. | `CBRS` | 38.0 | 28.6 | -265.0% | 85.5 | 371.3% | 232.7% | — | **0** | **75 WATCH** |
| Moderna, Inc. | `MRNA` | 36.3 | 34.6 | -557.9% | -44.7 | 42.6% | 15.8% | 0.4% | **0** | **72 WATCH** |
| Advanced Micro Devices, Inc. | `AMD` | 20.1 | 19.9 | 17.2% | 32.2 | 107.7% | 74.9% | 1.1% | **70 WATCH** | **13** |
| Marvell Technology, Inc. | `MRVL` | 21.3 | 20.9 | 16.7% | 30.5 | 73.7% | 63.3% | 1.2% | **70 WATCH** | **13** |
| Oracle Corporation | `ORCL` | 5.3 | 7.2 | 35.6% | 11.4 | 35.0% | 45.7% | -12.0% | **70 WATCH** | **10** |
| XIAOMI-W | `XIAOMI` | 1.6 | 1.3 | 4.0% | 17.8 | 36.8% | 19.7% | -1.3% | **70 WATCH** | **10** |
| Adobe Inc. | `ADBE` | 4.1 | 4.1 | 34.8% | 9.8 | 12.4% | 9.1% | 8.9% | **65 WATCH** | **30** |
| Coherent Corp. | `COHR` | 5.7 | 6.0 | 11.8% | 14.9 | 48.3% | 38.3% | -1.6% | **60 WATCH** | **35** |
| Microsoft Corporation | `MSFT` | 11.7 | 11.8 | 45.1% | 22.0 | 20.0% | 19.7% | 0.4% | **59 WATCH** | **23** |
| Apple Inc. | `AAPL` | 10.9 | 10.9 | 32.6% | 36.4 | 8.4% | 10.4% | 2.1% | **5** | **58** |
| Coca-Cola Company (The) | `KO` | 8.2 | 8.8 | 34.9% | 27.1 | 6.7% | -0.1% | 1.3% | **0** | **58** |
| Meta Platforms, Inc. | `META` | 7.2 | 7.9 | 34.8% | 18.6 | 16.0% | 21.3% | 1.3% | **57 WATCH** | **38** |
| Bloom Energy Corporation | `BE` | 20.6 | 20.6 | 17.1% | 44.1 | 61.0% | 55.6% | 0.8% | **55 WATCH** | **48** |
| AXT Inc | `AXT` | 26.9 | 24.4 | 21.9% | 22.9 | 159.2% | 111.3% | -1.3% | **52** | **35** |
| Super Micro Computer, Inc. | `SMCI` | 0.6 | 0.7 | 13.4% | 6.0 | 19.7% | 16.3% | -37.8% | **52** | **45** |
| Lumentum Holdings Inc. | `LITE` | 22.6 | 22.0 | 28.0% | 21.0 | 64.9% | 57.2% | 0.3% | **0** | **51** |
| Netflix, Inc. | `NFLX` | 5.6 | 5.7 | 34.6% | 17.8 | 5.1% | 10.8% | 9.2% | **35** | **50** |
| IREN LIMITED | `IREN` | 14.2 | 17.0 | -102.5% | -6.4 | -16.4% | 164.0% | -42.0% | **0** | **50** |
| Palantir Technologies Inc. | `PLTR` | 76.6 | 75.1 | 47.1% | 83.5 | 45.2% | 50.0% | 0.5% | **33** | **48** |
| Intel Corporation | `INTC` | 7.9 | 8.2 | 12.2% | 40.5 | 38.1% | 15.2% | 1.1% | **10** | **48** |
| SK hynix | `SKHYNIX` | 4.9 | 4.2 | 76.3% | 2.7 | 31.9% | 54.3% | 6.0% | **45** | **5** |
| SK hynix | `SKHY` | 4.9 | 4.2 | 76.3% | 2.7 | 31.9% | 54.3% | 6.0% | **45** | **5** |
| SamsungElec | `SAMSUNG` | 2.9 | 2.6 | 52.2% | 3.0 | 51.5% | 38.3% | 5.0% | **45** | **10** |
| Arm Holdings plc | `ARM` | 43.5 | 42.9 | 7.6% | 68.5 | 37.5% | 36.4% | 0.6% | **43** | **33** |
| Circle Internet Group, Inc. | `CRCL` | 7.6 | 7.0 | 4.9% | 58.6 | 30.0% | 26.7% | 0.9% | **43** | **33** |
| Coinbase Global, Inc. | `COIN` | 7.4 | 7.0 | -13.9% | 56.0 | 271.1% | 30.2% | 6.0% | **20** | **40** |
| SOFTBANK GROUP CORP | `SOFTBANK` | 3.0 | 6.4 | -11.6% | 14.5 | -14.5% | 6.9% | -9.0% | **0** | **40** |
| CoreWeave, Inc. | `CRWV` | 4.0 | 10.1 | -1.9% | -29.3 | 11.4% | 105.6% | -29.6% | **0** | **40** |
| Dell Technologies Inc. | `DELL` | 1.9 | 2.1 | 12.0% | 15.1 | 9.6% | 18.4% | 2.1% | **33** | **38** |
| Amazon.com, Inc. | `AMZN` | 3.5 | 3.6 | 13.7% | 24.0 | -18.2% | 14.6% | 0.1% | **0** | **38** |
| Fluence Energy, Inc. | `FLNC` | 0.4 | 0.4 | -8.9% | -12.6 | 60.4% | 26.9% | 0.2% | **5** | **28** |
| Hyperliquid Strategies Inc | `PURR` | 255.3 | 166.9 | 9595.1% | 23.5 | 51.0% | 31.4% | — | **25** | **10** |
| BitMine Immersion Technologies, | `BMNR` | 221.8 | 216.3 | 8.4% | 23.9 | 103.2% | 421.8% | -3.8% | **25** | **25** |
| Strategy Inc | `MSTR` | 123.9 | 150.1 | -6808.1% | 2.9 | 168.2% | 2.2% | -36.6% | **25** | **25** |
| QUALCOMM Incorporated | `QCOM` | 4.2 | 4.3 | 18.5% | 17.0 | -2.8% | 4.7% | 5.5% | **25** | **15** |
| Applied Optoelectronics, Inc. | `AAOI` | 9.7 | 9.3 | -12.9% | 14.8 | 576.8% | 156.5% | -15.3% | **10** | **25** |
| Alphabet Inc. | `GOOGL` | 8.9 | 8.7 | 34.0% | 21.1 | -26.6% | 25.3% | 0.6% | **12** | **23** |

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
