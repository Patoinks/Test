# OKX Long / Short Fundamental Scanner

Hourly scanner restricted to public companies exposed by the **OKX EEA TradFi / Stock Perpetual API universe**.

**Last scan:** 2026-10-23 18:26 UTC  
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
| 1 | Credo Technology Group Holding  | CRDO | -8.2% | -11.9% | -10.1% | 82 | +8 | **90** | **CORE** | yes |
| 2 | Taiwan Semiconductor Manufactur | TSM | 1.2% | 1.1% | 1.1% | 88 | -1 | **87** | **CORE** | yes |
| 3 | Corning Incorporated | GLW | 0.9% | -5.2% | -2.2% | 83 | +2 | **85** | **CORE** | yes |
| 4 | Sandisk Corporation | SNDK | 0.1% | -2.9% | -1.4% | 82 | +1 | **83** | **CORE** | yes |
| 5 | Applovin Corporation | APP | -0.5% | -1.2% | -0.8% | 82 | +1 | **83** | **CORE** | yes |
| 6 | Applied Materials, Inc. | AMAT | 1.1% | -7.3% | -3.1% | 81 | +2 | **83** | **CORE** | yes |
| 7 | NVIDIA Corporation | NVDA | -0.2% | -1.1% | -0.6% | 82 | +0 | **82** | **CORE** | yes |
| 8 | Broadcom Inc. | AVGO | 0.5% | -1.2% | -0.4% | 82 | +0 | **82** | **CORE** | yes |
| 9 | Robinhood Markets, Inc. | HOOD | -0.9% | -3.2% | -2.0% | 80 | +2 | **82** | **CORE** | yes |
| 10 | Bloom Energy Corporation | BE | -11.6% | -13.1% | -12.4% | 70 | +10 | **80** | **CORE** | yes |

## Final model + Price Timing — SHORT

| Rank | Company | OKX | 24h | 7d | 50/50 move | Base SHORT | Timing adj. | Final | Signal | Prev. SHORT? |
|---:|---|---|---:|---:|---:|---:|---:|---:|---|---|
| 1 | Rocket Lab Corporation | RKLB | 2.3% | 3.0% | 2.6% | 100 | +2 | **100** | **CORE** | yes |
| 2 | USA Rare Earth, Inc. | USAR | -2.2% | -10.7% | -6.5% | 100 | -5 | **95** | **CORE** | yes |
| 3 | IonQ, Inc. | IONQ | 0.8% | 0.4% | 0.6% | 85 | +0 | **85** | **CORE** | yes |
| 4 | Nebius Group N.V. | NBIS | 0.8% | -3.1% | -1.1% | 84 | -1 | **83** | **CORE** | yes |
| 5 | AST SpaceMobile, Inc. | ASTS | 2.9% | -1.9% | 0.5% | 80 | +0 | **80** | **CORE** | yes |
| 6 | Cerebras Systems Inc. | CBRS | 4.3% | -10.7% | -3.2% | 75 | -3 | **72** | **WATCH** | yes |
| 7 | Moderna, Inc. | MRNA | -1.1% | -8.1% | -4.6% | 72 | -4 | **68** | **WATCH** | yes |
| 8 | Okta, Inc. | OKTA | 5.6% | 13.5% | 9.6% | 60 | +8 | **68** | **WATCH** | yes |
| 9 | Tesla, Inc. | TSLA | -0.8% | 4.8% | 2.0% | 59 | +2 | **61** | **WATCH** | yes |

## Combined model — LONG

Weighted score: **70% fundamental + 30% P/E trend**.

| Rank | Company | OKX | Fundamental LONG | P/E trend LONG | Combined | Signal |
|---:|---|---|---:|---:|---:|---|
| 1 | Taiwan Semiconductor Manufactur | `TSM` | 90 | 85 | **88** | **CORE** |
| 2 | Corning Incorporated | `GLW` | 77 | 96 | **83** | **CORE** |
| 3 | Applovin Corporation | `APP` | 83 | 80 | **82** | **CORE** |
| 4 | Sandisk Corporation | `SNDK` | 82 | 82 | **82** | **CORE** |
| 5 | Credo Technology Group Holding  | `CRDO` | 75 | 100 | **82** | **CORE** |
| 6 | NVIDIA Corporation | `NVDA` | 75 | 100 | **82** | **CORE** |
| 7 | Broadcom Inc. | `AVGO` | 75 | 100 | **82** | **CORE** |
| 8 | Applied Materials, Inc. | `AMAT` | 77 | 91 | **81** | **CORE** |
| 9 | Robinhood Markets, Inc. | `HOOD` | 77 | 86 | **80** | **CORE** |
| 10 | Western Digital Corporation | `WDC` | 75 | 90 | **80** | **CORE** |

## Combined model — SHORT

Weighted score: **70% fundamental + 30% P/E trend**.

| Rank | Company | OKX | Fundamental SHORT | P/E trend SHORT | Combined | Signal |
|---:|---|---|---:|---:|---:|---|
| 1 | Rocket Lab Corporation | `RKLB` | 100 | 0 | **100** | **CORE** |
| 2 | USA Rare Earth, Inc. | `USAR` | 100 | 0 | **100** | **CORE** |
| 3 | IonQ, Inc. | `IONQ` | 85 | 0 | **85** | **CORE** |
| 4 | Nebius Group N.V. | `NBIS` | 84 | 0 | **84** | **WATCH** |
| 5 | AST SpaceMobile, Inc. | `ASTS` | 80 | 0 | **80** | **WATCH** |
| 6 | Cerebras Systems Inc. | `CBRS` | 75 | 0 | **75** | **WATCH** |
| 7 | Moderna, Inc. | `MRNA` | 72 | 0 | **72** | **WATCH** |
| 8 | Okta, Inc. | `OKTA` | 80 | 13 | **60** | **WATCH** |
| 9 | Tesla, Inc. | `TSLA` | 78 | 15 | **59** | **WATCH** |

## P/E Compression + Growth — LONG

| Rank | Company | OKX | Trail P/E | Fwd P/E | P/E change | EPS +1y | Rev +1y | Rev trend | LONG score | Signal |
|---:|---|---|---:|---:|---:|---:|---:|---|---:|---|
| 1 | Credo Technology Group Holding  | `CRDO` | 53.0 | 15.4 | -71.0% | 53.9% | 55.0% | decelerating | **100** | **CORE** |
| 2 | NVIDIA Corporation | `NVDA` | 26.8 | 13.3 | -50.3% | 70.9% | 68.2% | decelerating | **100** | **CORE** |
| 3 | Broadcom Inc. | `AVGO` | 43.4 | 16.7 | -61.5% | 66.7% | 64.3% | decelerating | **100** | **CORE** |
| 4 | Advanced Micro Devices, Inc. | `AMD` | 132.2 | 32.9 | -75.1% | 107.7% | 74.9% | accelerating | **100** | **CORE** |
| 5 | Marvell Technology, Inc. | `MRVL` | 75.3 | 31.2 | -58.5% | 73.7% | 63.3% | accelerating | **100** | **CORE** |
| 6 | Corning Incorporated | `GLW` | 57.4 | 28.5 | -50.4% | 33.6% | 20.0% | accelerating | **96** | **CORE** |
| 7 | AXT Inc | `AXT` | 1315.2 | 23.4 | -98.2% | 159.2% | 111.3% | decelerating | **96** | **CORE** |
| 8 | Oracle Corporation | `ORCL` | 20.1 | 11.7 | -41.9% | 35.0% | 45.7% | accelerating | **95** | **CORE** |
| 9 | Coherent Corp. | `COHR` | 51.0 | 15.1 | -70.4% | 48.3% | 38.3% | decelerating | **95** | **CORE** |
| 10 | Arm Holdings plc | `ARM` | 218.5 | 69.1 | -68.4% | 37.5% | 36.4% | accelerating | **95** | **CORE** |

## P/E Expansion + Weakening — SHORT

| Rank | Company | OKX | Trail P/E | Fwd P/E | P/E change | EPS +1y | Rev +1y | Rev trend | SHORT score | Signal |
|---:|---|---|---:|---:|---:|---:|---:|---|---:|---|
| 1 | SOFTBANK GROUP CORP | `SOFTBANK` | 5.0 | 14.5 | 191.0% | -14.5% | 6.9% | decelerating | **86** | **CORE** |
| 2 | Hyperliquid Strategies Inc | `PURR` | 2.8 | 24.0 | 767.6% | 51.0% | 31.4% | decelerating | **55** | **WATCH** |
| 3 | Amazon.com, Inc. | `AMZN` | 20.0 | 23.8 | 19.2% | -18.2% | 14.6% | decelerating | **52** | **WATCH** |
| 4 | Alphabet Inc. | `GOOGL` | 16.2 | 21.0 | 29.8% | -26.6% | 25.3% | accelerating | **50** | **WATCH** |

## Top SHORT candidates

| Rank | Company | OKX market | SHORT score | Signal | P/S | EV/S | Op margin | Fwd P/E | Rev +1y | FCF yield |
|---:|---|---|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Rocket Lab Corporation | `RKLB-USDT-SWAP` | **100** | **CORE** | 43.5 | 37.0 | -24.6% | 911.0 | 38.2% | -0.8% |
| 2 | USA Rare Earth, Inc. | `USAR-USDT-SWAP` | **100** | **CORE** | 268.3 | 63.7 | -795.6% | 313.8 | 870.1% | -8.0% |
| 3 | IonQ, Inc. | `IONQ-USDT-SWAP` | **85** | **CORE** | 51.6 | 39.8 | -408.2% | -23.4 | 77.6% | -0.7% |
| 4 | Nebius Group N.V. | `NBIS-USDT-SWAP` | **84** | **WATCH** | 32.2 | 33.8 | -0.2% | -44.6 | 266.0% | -22.0% |
| 5 | Okta, Inc. | `OKTA-USDT-SWAP` | **80** | **CORE** | 12.1 | 10.7 | 13.3% | 48.6 | 10.0% | 2.8% |
| 6 | AST SpaceMobile, Inc. | `ASTS-USDT-SWAP` | **80** | **WATCH** | 134.7 | 111.3 | -544.6% | -31.0 | 247.3% | -11.6% |
| 7 | Tesla, Inc. | `TSLA-USDT-SWAP` | **78** | **WATCH** | 14.2 | 11.4 | 2.6% | 171.7 | 13.3% | 0.4% |
| 8 | Cerebras Systems Inc. | `CBRS-USDT-SWAP` | **75** | **WATCH** | 39.6 | 28.6 | -265.0% | 89.2 | 232.7% | — |
| 9 | Moderna, Inc. | `MRNA-USDT-SWAP` | **72** | **WATCH** | 35.9 | 34.6 | -557.9% | -44.2 | 15.8% | 0.4% |

## Top LONG candidates

| Rank | Company | OKX market | LONG score | Signal | P/S | EV/S | Op margin | Fwd P/E | Rev +1y | FCF yield |
|---:|---|---|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Taiwan Semiconductor Manufactur | `TSM-USDT-SWAP` | **90** | **CORE** | 0.4 | 2.8 | 58.7% | 17.8 | 37.5% | 55.6% |
| 2 | Applovin Corporation | `APP-USDT-SWAP` | **83** | **CORE** | 12.9 | 13.0 | 77.7% | 12.8 | 26.0% | 3.6% |
| 3 | Sandisk Corporation | `SNDK-USDT-SWAP` | **82** | **CORE** | 9.0 | 8.9 | 78.5% | 4.7 | 18.9% | 4.2% |
| 4 | Corning Incorporated | `GLW-USDT-SWAP` | **77** | **WATCH** | 6.4 | 6.7 | 15.6% | 28.5 | 20.0% | 0.7% |
| 5 | Robinhood Markets, Inc. | `HOOD-USDT-SWAP` | **77** | **WATCH** | 17.5 | 17.4 | 43.9% | 28.0 | 29.3% | — |
| 6 | Applied Materials, Inc. | `AMAT-USDT-SWAP` | **77** | **WATCH** | 9.8 | 9.6 | 33.7% | 20.5 | 35.3% | 1.0% |
| 7 | Credo Technology Group Holding  | `CRDO-USDT-SWAP` | **75** | **WATCH** | 17.7 | 18.8 | 25.2% | 15.4 | 55.0% | 0.9% |
| 8 | Broadcom Inc. | `AVGO-USDT-SWAP` | **75** | **WATCH** | 17.4 | 17.7 | 54.3% | 16.7 | 64.3% | 2.0% |
| 9 | Micron Technology, Inc. | `MU-USDT-SWAP` | **75** | **CORE** | 7.5 | 7.0 | 80.7% | 4.3 | 15.7% | 2.9% |
| 10 | NVIDIA Corporation | `NVDA-USDT-SWAP` | **75** | **WATCH** | 16.9 | 16.8 | 66.2% | 13.3 | 68.2% | 0.8% |

## Analyst consensus (12-month price target) — most upside

| Rank | Company | OKX | Price | Analyst mean target | Gap | Analysts | Currency |
|---:|---|---|---:|---:|---:|---:|---|
| 1 | Hyperliquid Strategies Inc | `PURR` | 8.88 | 22.32 | **151.4%** | 4 | USD |
| 2 | Cerebras Systems Inc. | `CBRS` | 113.59 | 282.55 | **148.7%** | 11 | USD |
| 3 | CoreWeave, Inc. | `CRWV` | 54.89 | 136.21 | **148.2%** | 38 | USD |
| 4 | SK hynix | `SKHYNIX` | 1277000.00 | 3096288.00 | **142.5%** | 38 | KRW |
| 5 | Applied Optoelectronics, Inc. | `AAOI` | 68.33 | 160.00 | **134.1%** | 5 | USD |
| 6 | SamsungElec | `SAMSUNG` | 215500.00 | 478905.62 | **122.2%** | 36 | KRW |
| 7 | IonQ, Inc. | `IONQ` | 31.40 | 64.06 | **104.0%** | 14 | USD |
| 8 | BitMine Immersion Technologies, | `BMNR` | 22.55 | 45.87 | **103.4%** | 3 | USD |
| 9 | Rocket Lab Corporation | `RKLB` | 52.38 | 102.15 | **95.0%** | 20 | USD |
| 10 | Coherent Corp. | `COHR` | 210.21 | 394.79 | **87.8%** | 24 | USD |
| 11 | Credo Technology Group Holding  | `CRDO` | 149.46 | 279.09 | **86.7%** | 20 | USD |
| 12 | AST SpaceMobile, Inc. | `ASTS` | 39.90 | 74.28 | **86.2%** | 12 | USD |
| 13 | Oracle Corporation | `ORCL` | 128.10 | 236.54 | **84.6%** | 41 | USD |
| 14 | Western Digital Corporation | `WDC` | 344.90 | 636.08 | **84.4%** | 24 | USD |
| 15 | SOFTBANK GROUP CORP | `SOFTBANK` | 4276.00 | 7782.47 | **82.0%** | 18 | JPY |

## Analyst consensus (12-month price target) — most downside

| Rank | Company | OKX | Price | Analyst mean target | Gap | Analysts | Currency |
|---:|---|---|---:|---:|---:|---:|---|
| 1 | Moderna, Inc. | `MRNA` | 200.45 | 135.84 | **-32.2%** | 19 | USD |
| 2 | Apple Inc. | `AAPL` | 346.24 | 328.35 | **-5.2%** | 39 | USD |

Price/target uses the underlying Yahoo Finance share quote, not the OKX derivative. Minimum 3 analysts; unreliable price scales and missing coverage excluded. Targets are analyst opinions, not guaranteed forecasts.

## All OKX companies — our ratio + LONG/SHORT scores

| Company | OKX | P/S | EV/S | Op margin | Fwd P/E | EPS +1y | Rev +1y | FCF yield | LONG | SHORT |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Rocket Lab Corporation | `RKLB` | 43.5 | 37.0 | -24.6% | 911.0 | 66.8% | 38.2% | -0.8% | **0** | **100 CORE** |
| USA Rare Earth, Inc. | `USAR` | 268.3 | 63.7 | -795.6% | 313.8 | 105.3% | 870.1% | -8.0% | **0** | **100 CORE** |
| Taiwan Semiconductor Manufactur | `TSM` | 0.4 | 2.8 | 58.7% | 17.8 | 33.6% | 37.5% | 55.6% | **90 CORE** | **10** |
| IonQ, Inc. | `IONQ` | 51.6 | 39.8 | -408.2% | -23.4 | 21.3% | 77.6% | -0.7% | **0** | **85 CORE** |
| Nebius Group N.V. | `NBIS` | 32.2 | 33.8 | -0.2% | -44.6 | -191.4% | 266.0% | -22.0% | **0** | **84 WATCH** |
| Applovin Corporation | `APP` | 12.9 | 13.0 | 77.7% | 12.8 | 27.1% | 26.0% | 3.6% | **83 CORE** | **10** |
| Sandisk Corporation | `SNDK` | 9.0 | 8.9 | 78.5% | 4.7 | 24.0% | 18.9% | 4.2% | **82 CORE** | **10** |
| Okta, Inc. | `OKTA` | 12.1 | 10.7 | 13.3% | 48.6 | 11.4% | 10.0% | 2.8% | **8** | **80 CORE** |
| AST SpaceMobile, Inc. | `ASTS` | 134.7 | 111.3 | -544.6% | -31.0 | 44.3% | 247.3% | -11.6% | **0** | **80 WATCH** |
| Tesla, Inc. | `TSLA` | 14.2 | 11.4 | 2.6% | 171.7 | 23.7% | 13.3% | 0.4% | **12** | **78 WATCH** |
| Corning Incorporated | `GLW` | 6.4 | 6.7 | 15.6% | 28.5 | 33.6% | 20.0% | 0.7% | **77 WATCH** | **13** |
| Applied Materials, Inc. | `AMAT` | 9.8 | 9.6 | 33.7% | 20.5 | 44.6% | 35.3% | 1.0% | **77 WATCH** | **3** |
| Robinhood Markets, Inc. | `HOOD` | 17.5 | 17.4 | 43.9% | 28.0 | 36.5% | 29.3% | — | **77 WATCH** | **5** |
| Credo Technology Group Holding  | `CRDO` | 17.7 | 18.8 | 25.2% | 15.4 | 53.9% | 55.0% | 0.9% | **75 WATCH** | **28** |
| NVIDIA Corporation | `NVDA` | 16.9 | 16.8 | 66.2% | 13.3 | 70.9% | 68.2% | 0.8% | **75 WATCH** | **18** |
| Broadcom Inc. | `AVGO` | 17.4 | 17.7 | 54.3% | 16.7 | 66.7% | 64.3% | 2.0% | **75 WATCH** | **28** |
| Western Digital Corporation | `WDC` | 10.0 | 9.9 | 43.6% | 8.8 | 61.5% | 37.9% | 1.8% | **75 WATCH** | **18** |
| Micron Technology, Inc. | `MU` | 7.5 | 7.0 | 80.7% | 4.3 | 17.2% | 15.7% | 2.9% | **75 CORE** | **30** |
| Cerebras Systems Inc. | `CBRS` | 39.6 | 28.6 | -265.0% | 89.2 | 371.3% | 232.7% | — | **0** | **75 WATCH** |
| Moderna, Inc. | `MRNA` | 35.9 | 34.6 | -557.9% | -44.2 | 42.6% | 15.8% | 0.4% | **0** | **72 WATCH** |
| Advanced Micro Devices, Inc. | `AMD` | 20.5 | 19.9 | 17.2% | 32.9 | 107.7% | 74.9% | 1.0% | **70 WATCH** | **13** |
| Marvell Technology, Inc. | `MRVL` | 21.8 | 20.9 | 16.7% | 31.2 | 73.7% | 63.3% | 1.2% | **70 WATCH** | **13** |
| Oracle Corporation | `ORCL` | 5.4 | 7.2 | 35.6% | 11.7 | 35.0% | 45.7% | -11.8% | **70 WATCH** | **10** |
| XIAOMI-W | `XIAOMI` | 1.6 | 1.4 | 4.0% | 17.8 | 36.8% | 19.7% | -1.3% | **70 WATCH** | **10** |
| Adobe Inc. | `ADBE` | 4.0 | 4.1 | 34.8% | 9.6 | 12.4% | 9.1% | 9.1% | **65 WATCH** | **30** |
| Bloom Energy Corporation | `BE` | 18.2 | 20.6 | 17.1% | 36.8 | 61.0% | 55.6% | 0.9% | **60 WATCH** | **28** |
| Coherent Corp. | `COHR` | 5.8 | 6.0 | 11.8% | 15.1 | 48.3% | 38.3% | -1.6% | **60 WATCH** | **35** |
| Microsoft Corporation | `MSFT` | 11.7 | 11.8 | 45.1% | 22.1 | 20.0% | 19.7% | 0.4% | **59 WATCH** | **23** |
| Apple Inc. | `AAPL` | 10.8 | 10.9 | 32.6% | 36.2 | 8.4% | 10.4% | 2.1% | **5** | **58** |
| Coca-Cola Company (The) | `KO` | 8.0 | 8.8 | 34.9% | 26.4 | 6.7% | -0.1% | 1.3% | **0** | **58** |
| Meta Platforms, Inc. | `META` | 6.8 | 7.0 | 35.4% | 18.5 | 16.0% | 21.3% | 1.1% | **57 WATCH** | **38** |
| AXT Inc | `AXT` | 27.5 | 24.4 | 21.9% | 23.4 | 159.2% | 111.3% | -1.3% | **52** | **35** |
| Super Micro Computer, Inc. | `SMCI` | 0.6 | 0.7 | 13.4% | 5.9 | 19.7% | 16.3% | -37.9% | **52** | **45** |
| Lumentum Holdings Inc. | `LITE` | 23.0 | 22.0 | 28.0% | 21.3 | 64.9% | 57.2% | 0.3% | **0** | **51** |
| Netflix, Inc. | `NFLX` | 5.5 | 5.7 | 34.6% | 17.6 | 5.1% | 10.8% | 9.4% | **35** | **50** |
| IREN LIMITED | `IREN` | 14.1 | 17.0 | -102.5% | -6.4 | -16.4% | 164.0% | -42.3% | **0** | **50** |
| Palantir Technologies Inc. | `PLTR` | 76.5 | 75.1 | 47.1% | 83.4 | 45.2% | 50.0% | 0.5% | **33** | **48** |
| Intel Corporation | `INTC` | 8.1 | 8.2 | 12.2% | 41.2 | 38.1% | 15.2% | 1.1% | **10** | **48** |
| SK hynix | `SKHYNIX` | 4.9 | 4.4 | 76.3% | 2.7 | 31.9% | 54.3% | 6.0% | **45** | **5** |
| SK hynix | `SKHY` | 4.9 | 4.4 | 76.3% | 2.7 | 31.9% | 54.3% | 6.0% | **45** | **5** |
| SamsungElec | `SAMSUNG` | 2.9 | 2.6 | 52.2% | 3.0 | 51.5% | 38.3% | 5.0% | **45** | **10** |
| Arm Holdings plc | `ARM` | 43.9 | 42.9 | 7.6% | 69.1 | 37.5% | 36.4% | 0.6% | **43** | **33** |
| Circle Internet Group, Inc. | `CRCL` | 7.5 | 7.0 | 4.9% | 58.1 | 30.0% | 26.7% | 0.9% | **43** | **33** |
| Coinbase Global, Inc. | `COIN` | 7.3 | 7.0 | -13.9% | 55.1 | 271.1% | 30.2% | 6.1% | **20** | **40** |
| SOFTBANK GROUP CORP | `SOFTBANK` | 3.0 | 6.4 | -11.6% | 14.5 | -14.5% | 6.9% | -9.0% | **0** | **40** |
| CoreWeave, Inc. | `CRWV` | 4.0 | 10.1 | -1.9% | -28.8 | 11.4% | 105.6% | -30.0% | **0** | **40** |
| Dell Technologies Inc. | `DELL` | 1.9 | 2.1 | 12.0% | 15.4 | 9.6% | 18.4% | 2.1% | **33** | **38** |
| Amazon.com, Inc. | `AMZN` | 3.5 | 3.6 | 13.7% | 23.8 | -18.2% | 14.6% | 0.1% | **0** | **38** |
| Fluence Energy, Inc. | `FLNC` | 0.4 | 0.4 | -8.9% | -12.3 | 60.4% | 26.9% | 0.2% | **5** | **28** |
| Hyperliquid Strategies Inc | `PURR` | 261.2 | 166.9 | 9595.1% | 24.0 | 51.0% | 31.4% | — | **25** | **10** |
| Strategy Inc | `MSTR` | 126.2 | 150.1 | -6808.1% | 3.0 | 168.2% | 2.2% | -35.9% | **25** | **25** |
| BitMine Immersion Technologies, | `BMNR` | 222.2 | 216.3 | 8.4% | 24.0 | 103.2% | 421.8% | -3.8% | **25** | **25** |
| QUALCOMM Incorporated | `QCOM` | 4.3 | 4.3 | 18.5% | 17.2 | -2.8% | 4.7% | 5.5% | **25** | **15** |
| Applied Optoelectronics, Inc. | `AAOI` | 9.7 | 9.3 | -12.9% | 14.8 | 576.8% | 156.5% | -15.3% | **10** | **25** |
| Alphabet Inc. | `GOOGL` | 8.8 | 8.7 | 34.0% | 21.0 | -26.6% | 25.3% | 0.6% | **12** | **23** |

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
