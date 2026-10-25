# OKX Long / Short Fundamental Scanner

Hourly scanner restricted to public companies exposed by the **OKX EEA TradFi / Stock Perpetual API universe**.

**Last scan:** 2026-10-25 12:37 UTC  
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
| 1 | Taiwan Semiconductor Manufactur | TSM | -0.0% | 1.4% | 0.7% | 88 | -1 | **87** | **CORE** | yes |
| 2 | Credo Technology Group Holding  | CRDO | 0.0% | -13.2% | -6.6% | 82 | +5 | **87** | **CORE** | yes |
| 3 | Corning Incorporated | GLW | -0.0% | -6.3% | -3.1% | 83 | +3 | **86** | **CORE** | yes |
| 4 | Sandisk Corporation | SNDK | -0.0% | -4.7% | -2.4% | 82 | +2 | **84** | **CORE** | yes |
| 5 | Applied Materials, Inc. | AMAT | 0.0% | -7.8% | -3.9% | 81 | +3 | **84** | **CORE** | yes |
| 6 | Applovin Corporation | APP | 0.0% | -2.2% | -1.1% | 82 | +1 | **83** | **CORE** | yes |
| 7 | Broadcom Inc. | AVGO | 0.0% | -2.2% | -1.1% | 82 | +1 | **83** | **CORE** | yes |
| 8 | NVIDIA Corporation | NVDA | -0.0% | -1.5% | -0.7% | 82 | +1 | **83** | **CORE** | yes |
| 9 | Robinhood Markets, Inc. | HOOD | 0.0% | -3.8% | -1.9% | 80 | +2 | **82** | **CORE** | yes |
| 10 | Advanced Micro Devices, Inc. | AMD | 0.0% | -2.3% | -1.1% | 79 | +1 | **80** | **CORE** | yes |

## Final model + Price Timing — SHORT

| Rank | Company | OKX | 24h | 7d | 50/50 move | Base SHORT | Timing adj. | Final | Signal | Prev. SHORT? |
|---:|---|---|---:|---:|---:|---:|---:|---:|---|---|
| 1 | Rocket Lab Corporation | RKLB | 0.0% | 3.5% | 1.7% | 100 | +1 | **100** | **CORE** | yes |
| 2 | USA Rare Earth, Inc. | USAR | 0.0% | -11.5% | -5.7% | 100 | -5 | **95** | **CORE** | yes |
| 3 | IonQ, Inc. | IONQ | -0.0% | -0.0% | -0.0% | 88 | +0 | **88** | **CORE** | yes |
| 4 | AST SpaceMobile, Inc. | ASTS | -0.0% | -2.1% | -1.1% | 80 | -1 | **79** | **CORE** | yes |
| 5 | Nebius Group N.V. | NBIS | -0.0% | -4.1% | -2.0% | 80 | -2 | **78** | **CORE** | yes |
| 6 | Cerebras Systems Inc. | CBRS | 0.0% | -12.9% | -6.4% | 75 | -5 | **70** | **WATCH** | yes |
| 7 | Moderna, Inc. | MRNA | -0.0% | -8.2% | -4.1% | 72 | -3 | **69** | **WATCH** | yes |
| 8 | Okta, Inc. | OKTA | -0.0% | 13.8% | 6.9% | 60 | +6 | **66** | **WATCH** | yes |
| 9 | Tesla, Inc. | TSLA | -0.0% | 4.9% | 2.5% | 59 | +2 | **61** | **WATCH** | yes |

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
| 10 | Advanced Micro Devices, Inc. | `AMD` | 70 | 100 | **79** | **CORE** |

## Combined model — SHORT

Weighted score: **70% fundamental + 30% P/E trend**.

| Rank | Company | OKX | Fundamental SHORT | P/E trend SHORT | Combined | Signal |
|---:|---|---|---:|---:|---:|---|
| 1 | Rocket Lab Corporation | `RKLB` | 100 | 0 | **100** | **CORE** |
| 2 | USA Rare Earth, Inc. | `USAR` | 100 | 0 | **100** | **CORE** |
| 3 | IonQ, Inc. | `IONQ` | 88 | 0 | **88** | **CORE** |
| 4 | AST SpaceMobile, Inc. | `ASTS` | 80 | 0 | **80** | **WATCH** |
| 5 | Nebius Group N.V. | `NBIS` | 80 | 0 | **80** | **WATCH** |
| 6 | Cerebras Systems Inc. | `CBRS` | 75 | 0 | **75** | **WATCH** |
| 7 | Moderna, Inc. | `MRNA` | 72 | 0 | **72** | **WATCH** |
| 8 | Okta, Inc. | `OKTA` | 80 | 13 | **60** | **WATCH** |
| 9 | Tesla, Inc. | `TSLA` | 78 | 15 | **59** | **WATCH** |

## P/E Compression + Growth — LONG

| Rank | Company | OKX | Trail P/E | Fwd P/E | P/E change | EPS +1y | Rev +1y | Rev trend | LONG score | Signal |
|---:|---|---|---:|---:|---:|---:|---:|---|---:|---|
| 1 | Credo Technology Group Holding  | `CRDO` | 52.2 | 15.2 | -71.0% | 53.9% | 55.0% | decelerating | **100** | **CORE** |
| 2 | NVIDIA Corporation | `NVDA` | 26.7 | 13.3 | -50.3% | 70.9% | 68.2% | decelerating | **100** | **CORE** |
| 3 | Broadcom Inc. | `AVGO` | 41.1 | 16.6 | -59.7% | 66.7% | 64.3% | decelerating | **100** | **CORE** |
| 4 | Advanced Micro Devices, Inc. | `AMD` | 131.8 | 32.8 | -75.1% | 107.7% | 74.9% | accelerating | **100** | **CORE** |
| 5 | Marvell Technology, Inc. | `MRVL` | 75.2 | 31.2 | -58.5% | 73.7% | 63.3% | accelerating | **100** | **CORE** |
| 6 | Corning Incorporated | `GLW` | 56.7 | 28.1 | -50.4% | 33.6% | 20.0% | accelerating | **96** | **CORE** |
| 7 | AXT Inc | `AXT` | 1302.0 | 23.1 | -98.2% | 159.2% | 111.3% | decelerating | **96** | **CORE** |
| 8 | Oracle Corporation | `ORCL` | 19.8 | 11.5 | -41.9% | 35.0% | 45.7% | accelerating | **95** | **CORE** |
| 9 | Coherent Corp. | `COHR` | 50.8 | 15.0 | -70.4% | 48.3% | 38.3% | decelerating | **95** | **CORE** |
| 10 | Arm Holdings plc | `ARM` | 216.8 | 68.6 | -68.4% | 37.5% | 36.4% | accelerating | **95** | **CORE** |

## P/E Expansion + Weakening — SHORT

| Rank | Company | OKX | Trail P/E | Fwd P/E | P/E change | EPS +1y | Rev +1y | Rev trend | SHORT score | Signal |
|---:|---|---|---:|---:|---:|---:|---:|---|---:|---|
| 1 | SOFTBANK GROUP CORP | `SOFTBANK` | 5.0 | 14.5 | 191.0% | -14.5% | 6.9% | decelerating | **86** | **CORE** |
| 2 | Hyperliquid Strategies Inc | `PURR` | 2.7 | 23.7 | 767.6% | 51.0% | 31.4% | decelerating | **55** | **WATCH** |
| 3 | Amazon.com, Inc. | `AMZN` | 20.0 | 23.8 | 19.2% | -18.2% | 14.6% | decelerating | **52** | **WATCH** |
| 4 | Alphabet Inc. | `GOOGL` | 16.1 | 20.8 | 29.8% | -26.6% | 25.3% | accelerating | **50** | **WATCH** |

## Top SHORT candidates

| Rank | Company | OKX market | SHORT score | Signal | P/S | EV/S | Op margin | Fwd P/E | Rev +1y | FCF yield |
|---:|---|---|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Rocket Lab Corporation | `RKLB-USDT-SWAP` | **100** | **CORE** | 43.7 | 38.1 | -24.6% | 914.9 | 38.2% | -0.7% |
| 2 | USA Rare Earth, Inc. | `USAR-USDT-SWAP` | **100** | **CORE** | 265.9 | 58.2 | -795.6% | 311.0 | 870.1% | -8.1% |
| 3 | IonQ, Inc. | `IONQ-USDT-SWAP` | **88** | **CORE** | 54.5 | 40.0 | -408.2% | -23.3 | 77.6% | -0.7% |
| 4 | Nebius Group N.V. | `NBIS-USDT-SWAP` | **80** | **WATCH** | 29.7 | 33.7 | -0.2% | -44.1 | 266.0% | -23.9% |
| 5 | Okta, Inc. | `OKTA-USDT-SWAP` | **80** | **CORE** | 12.1 | 11.4 | 13.3% | 48.7 | 10.0% | 2.8% |
| 6 | AST SpaceMobile, Inc. | `ASTS-USDT-SWAP` | **80** | **WATCH** | 134.3 | 113.9 | -544.6% | -30.9 | 264.2% | -11.6% |
| 7 | Tesla, Inc. | `TSLA-USDT-SWAP` | **78** | **WATCH** | 14.2 | 13.9 | 2.6% | 172.0 | 13.5% | 0.3% |
| 8 | Cerebras Systems Inc. | `CBRS-USDT-SWAP` | **75** | **WATCH** | 38.7 | 29.2 | -265.0% | 87.0 | 232.7% | — |
| 9 | Moderna, Inc. | `MRNA-USDT-SWAP` | **72** | **WATCH** | 35.9 | 34.1 | -557.9% | -44.2 | 15.8% | 0.4% |

## Top LONG candidates

| Rank | Company | OKX market | LONG score | Signal | P/S | EV/S | Op margin | Fwd P/E | Rev +1y | FCF yield |
|---:|---|---|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Taiwan Semiconductor Manufactur | `TSM-USDT-SWAP` | **90** | **CORE** | 0.4 | 2.9 | 58.7% | 17.9 | 37.5% | 55.4% |
| 2 | Applovin Corporation | `APP-USDT-SWAP` | **83** | **CORE** | 12.8 | 12.8 | 77.7% | 12.7 | 26.0% | 3.7% |
| 3 | Sandisk Corporation | `SNDK-USDT-SWAP` | **82** | **CORE** | 8.8 | 8.7 | 78.5% | 4.6 | 18.9% | 4.3% |
| 4 | Corning Incorporated | `GLW-USDT-SWAP` | **77** | **WATCH** | 6.3 | 6.7 | 15.6% | 28.1 | 20.0% | 0.7% |
| 5 | Robinhood Markets, Inc. | `HOOD-USDT-SWAP` | **77** | **WATCH** | 17.3 | 17.1 | 43.9% | 27.8 | 29.3% | — |
| 6 | Applied Materials, Inc. | `AMAT-USDT-SWAP` | **77** | **WATCH** | 9.7 | 9.6 | 33.7% | 20.4 | 35.3% | 1.0% |
| 7 | Credo Technology Group Holding  | `CRDO-USDT-SWAP` | **75** | **WATCH** | 17.4 | 16.9 | 25.2% | 15.2 | 55.0% | 0.9% |
| 8 | Broadcom Inc. | `AVGO-USDT-SWAP` | **75** | **WATCH** | 17.2 | 17.6 | 54.3% | 16.6 | 64.3% | 2.0% |
| 9 | Micron Technology, Inc. | `MU-USDT-SWAP` | **75** | **CORE** | 7.5 | 7.2 | 80.7% | 4.2 | 15.7% | 2.9% |
| 10 | NVIDIA Corporation | `NVDA-USDT-SWAP` | **75** | **WATCH** | 16.8 | 16.7 | 66.2% | 13.3 | 68.2% | 0.8% |

## Analyst consensus (12-month price target) — most upside

| Rank | Company | OKX | Price | Analyst mean target | Gap | Analysts | Currency |
|---:|---|---|---:|---:|---:|---:|---|
| 1 | Cerebras Systems Inc. | `CBRS` | 110.82 | 282.55 | **155.0%** | 11 | USD |
| 2 | Hyperliquid Strategies Inc | `PURR` | 8.78 | 22.32 | **154.3%** | 4 | USD |
| 3 | CoreWeave, Inc. | `CRWV` | 54.23 | 135.82 | **150.4%** | 38 | USD |
| 4 | SK hynix | `SKHYNIX` | 1277000.00 | 3096288.00 | **142.5%** | 38 | KRW |
| 5 | Applied Optoelectronics, Inc. | `AAOI` | 67.51 | 160.00 | **137.0%** | 5 | USD |
| 6 | SamsungElec | `SAMSUNG` | 215500.00 | 478905.62 | **122.2%** | 36 | KRW |
| 7 | IonQ, Inc. | `IONQ` | 31.27 | 64.06 | **104.9%** | 14 | USD |
| 8 | BitMine Immersion Technologies, | `BMNR` | 22.40 | 45.87 | **104.8%** | 3 | USD |
| 9 | Rocket Lab Corporation | `RKLB` | 52.60 | 102.15 | **94.2%** | 20 | USD |
| 10 | Credo Technology Group Holding  | `CRDO` | 147.29 | 284.05 | **92.8%** | 19 | USD |
| 11 | Coherent Corp. | `COHR` | 209.29 | 394.79 | **88.6%** | 24 | USD |
| 12 | AST SpaceMobile, Inc. | `ASTS` | 39.79 | 74.68 | **87.7%** | 12 | USD |
| 13 | Oracle Corporation | `ORCL` | 126.16 | 236.54 | **87.5%** | 41 | USD |
| 14 | Applovin Corporation | `APP` | 260.25 | 476.85 | **83.2%** | 31 | USD |
| 15 | SOFTBANK GROUP CORP | `SOFTBANK` | 4276.00 | 7782.47 | **82.0%** | 18 | JPY |

## Analyst consensus (12-month price target) — most downside

| Rank | Company | OKX | Price | Analyst mean target | Gap | Analysts | Currency |
|---:|---|---|---:|---:|---:|---:|---|
| 1 | Moderna, Inc. | `MRNA` | 200.10 | 135.05 | **-32.5%** | 19 | USD |
| 2 | Apple Inc. | `AAPL` | 347.73 | 329.25 | **-5.3%** | 39 | USD |

Price/target uses the underlying Yahoo Finance share quote, not the OKX derivative. Minimum 3 analysts; unreliable price scales and missing coverage excluded. Targets are analyst opinions, not guaranteed forecasts.

## All OKX companies — our ratio + LONG/SHORT scores

| Company | OKX | P/S | EV/S | Op margin | Fwd P/E | EPS +1y | Rev +1y | FCF yield | LONG | SHORT |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Rocket Lab Corporation | `RKLB` | 43.7 | 38.1 | -24.6% | 914.9 | 66.8% | 38.2% | -0.7% | **0** | **100 CORE** |
| USA Rare Earth, Inc. | `USAR` | 265.9 | 58.2 | -795.6% | 311.0 | 105.3% | 870.1% | -8.1% | **0** | **100 CORE** |
| Taiwan Semiconductor Manufactur | `TSM` | 0.4 | 2.9 | 58.7% | 17.9 | 33.6% | 37.5% | 55.4% | **90 CORE** | **10** |
| IonQ, Inc. | `IONQ` | 54.5 | 40.0 | -408.2% | -23.3 | 21.3% | 77.6% | -0.7% | **0** | **88 CORE** |
| Applovin Corporation | `APP` | 12.8 | 12.8 | 77.7% | 12.7 | 27.1% | 26.0% | 3.7% | **83 CORE** | **10** |
| Sandisk Corporation | `SNDK` | 8.8 | 8.7 | 78.5% | 4.6 | 24.0% | 18.9% | 4.3% | **82 CORE** | **10** |
| Okta, Inc. | `OKTA` | 12.1 | 11.4 | 13.3% | 48.7 | 11.4% | 10.0% | 2.8% | **8** | **80 CORE** |
| AST SpaceMobile, Inc. | `ASTS` | 134.3 | 113.9 | -544.6% | -30.9 | 44.3% | 264.2% | -11.6% | **0** | **80 WATCH** |
| Nebius Group N.V. | `NBIS` | 29.7 | 33.7 | -0.2% | -44.1 | -191.4% | 266.0% | -23.9% | **0** | **80 WATCH** |
| Tesla, Inc. | `TSLA` | 14.2 | 13.9 | 2.6% | 172.0 | 22.5% | 13.5% | 0.3% | **12** | **78 WATCH** |
| Corning Incorporated | `GLW` | 6.3 | 6.7 | 15.6% | 28.1 | 33.6% | 20.0% | 0.7% | **77 WATCH** | **13** |
| Applied Materials, Inc. | `AMAT` | 9.7 | 9.6 | 33.7% | 20.4 | 44.6% | 35.3% | 1.0% | **77 WATCH** | **3** |
| Robinhood Markets, Inc. | `HOOD` | 17.3 | 17.1 | 43.9% | 27.8 | 36.5% | 29.3% | — | **77 WATCH** | **5** |
| Credo Technology Group Holding  | `CRDO` | 17.4 | 16.9 | 25.2% | 15.2 | 53.9% | 55.0% | 0.9% | **75 WATCH** | **28** |
| NVIDIA Corporation | `NVDA` | 16.8 | 16.7 | 66.2% | 13.3 | 70.9% | 68.2% | 0.8% | **75 WATCH** | **18** |
| Broadcom Inc. | `AVGO` | 17.2 | 17.6 | 54.3% | 16.6 | 66.7% | 64.3% | 2.0% | **75 WATCH** | **28** |
| Micron Technology, Inc. | `MU` | 7.5 | 7.2 | 80.7% | 4.2 | 17.2% | 15.7% | 2.9% | **75 CORE** | **30** |
| Western Digital Corporation | `WDC` | 8.9 | 8.9 | 47.7% | 8.7 | 59.1% | 36.9% | 2.1% | **75 WATCH** | **18** |
| Cerebras Systems Inc. | `CBRS` | 38.7 | 29.2 | -265.0% | 87.0 | 371.3% | 232.7% | — | **0** | **75 WATCH** |
| Moderna, Inc. | `MRNA` | 35.9 | 34.1 | -557.9% | -44.2 | 42.6% | 15.8% | 0.4% | **0** | **72 WATCH** |
| Advanced Micro Devices, Inc. | `AMD` | 20.4 | 20.2 | 17.2% | 32.8 | 107.7% | 74.9% | 1.0% | **70 WATCH** | **13** |
| Oracle Corporation | `ORCL` | 5.3 | 7.2 | 35.6% | 11.5 | 35.0% | 45.7% | -12.0% | **70 WATCH** | **10** |
| Marvell Technology, Inc. | `MRVL` | 21.7 | 21.3 | 16.7% | 31.2 | 73.7% | 63.3% | 1.2% | **70 WATCH** | **13** |
| XIAOMI-W | `XIAOMI` | 1.6 | 1.4 | 4.0% | 17.8 | 36.8% | 19.7% | -1.3% | **70 WATCH** | **10** |
| Adobe Inc. | `ADBE` | 4.0 | 4.0 | 34.8% | 9.6 | 12.4% | 9.1% | 9.1% | **65 WATCH** | **30** |
| Coherent Corp. | `COHR` | 5.8 | 6.0 | 11.8% | 15.0 | 48.3% | 38.3% | -1.6% | **60 WATCH** | **35** |
| Microsoft Corporation | `MSFT` | 11.7 | 11.9 | 45.1% | 22.1 | 20.0% | 19.7% | 0.4% | **59 WATCH** | **23** |
| Apple Inc. | `AAPL` | 10.9 | 10.9 | 32.6% | 36.4 | 8.2% | 10.4% | 2.1% | **5** | **58** |
| Coca-Cola Company (The) | `KO` | 8.0 | 8.6 | 34.9% | 26.3 | 6.7% | -0.1% | 1.3% | **0** | **58** |
| Meta Platforms, Inc. | `META` | 6.8 | 6.9 | 35.4% | 18.5 | 16.3% | 21.4% | 1.0% | **57 WATCH** | **38** |
| AXT Inc | `AXT` | 27.2 | 24.7 | 21.9% | 23.1 | 159.2% | 111.3% | -1.3% | **52** | **35** |
| Super Micro Computer, Inc. | `SMCI` | 0.5 | 0.7 | 13.4% | 5.9 | 19.7% | 16.3% | -38.7% | **52** | **45** |
| Lumentum Holdings Inc. | `LITE` | 22.7 | 22.2 | 28.0% | 21.1 | 64.9% | 57.2% | 0.3% | **0** | **51** |
| Netflix, Inc. | `NFLX` | 5.5 | 5.6 | 34.6% | 17.5 | 5.1% | 10.8% | 9.3% | **35** | **50** |
| IREN LIMITED | `IREN` | 14.3 | 16.6 | -102.5% | -6.3 | -16.4% | 164.0% | -41.9% | **0** | **50** |
| Palantir Technologies Inc. | `PLTR` | 76.8 | 75.3 | 47.1% | 83.7 | 45.6% | 50.4% | 0.5% | **33** | **48** |
| Intel Corporation | `INTC` | 8.1 | 8.3 | 12.2% | 41.2 | 38.1% | 15.2% | 1.1% | **10** | **48** |
| Bloom Energy Corporation | `BE` | 14.9 | 15.0 | 18.5% | 39.1 | 62.7% | 55.7% | -0.0% | **45** | **35** |
| SK hynix | `SKHYNIX` | 4.9 | 4.4 | 76.3% | 2.7 | 31.9% | 54.3% | 6.0% | **45** | **5** |
| SK hynix | `SKHY` | 4.9 | 4.4 | 76.3% | 2.7 | 31.9% | 54.3% | 6.0% | **45** | **5** |
| SamsungElec | `SAMSUNG` | 2.9 | 2.6 | 52.2% | 3.0 | 51.5% | 38.3% | 5.0% | **45** | **10** |
| Arm Holdings plc | `ARM` | 43.6 | 42.9 | 7.6% | 68.6 | 37.5% | 36.4% | 0.6% | **43** | **33** |
| Circle Internet Group, Inc. | `CRCL` | 7.5 | 6.9 | 4.9% | 58.1 | 30.0% | 26.7% | 0.9% | **43** | **33** |
| Coinbase Global, Inc. | `COIN` | 7.2 | 6.8 | -13.9% | 53.5 | 283.2% | 30.1% | 6.2% | **20** | **40** |
| SOFTBANK GROUP CORP | `SOFTBANK` | 3.0 | 6.4 | -11.6% | 14.5 | -14.5% | 6.9% | -9.0% | **0** | **40** |
| CoreWeave, Inc. | `CRWV` | 3.9 | 10.0 | -1.9% | -28.4 | 11.4% | 105.6% | -30.4% | **0** | **40** |
| Dell Technologies Inc. | `DELL` | 1.9 | 2.1 | 12.0% | 15.3 | 9.6% | 18.4% | 2.1% | **33** | **38** |
| Amazon.com, Inc. | `AMZN` | 3.4 | 3.6 | 13.7% | 23.8 | -18.2% | 14.6% | 0.1% | **0** | **38** |
| Fluence Energy, Inc. | `FLNC` | 0.4 | 0.4 | -8.9% | -12.4 | 60.4% | 26.9% | 0.2% | **5** | **28** |
| Hyperliquid Strategies Inc | `PURR` | 258.3 | 169.0 | 9595.1% | 23.7 | 51.0% | 31.4% | — | **25** | **10** |
| Strategy Inc | `MSTR` | 124.1 | 150.2 | -6808.1% | 3.0 | 168.2% | 2.2% | -36.5% | **25** | **25** |
| BitMine Immersion Technologies, | `BMNR` | 220.8 | 215.3 | 8.4% | 23.8 | 103.2% | 421.8% | -3.8% | **25** | **25** |
| QUALCOMM Incorporated | `QCOM` | 4.3 | 4.4 | 18.5% | 17.3 | -2.8% | 4.7% | 5.5% | **25** | **15** |
| Applied Optoelectronics, Inc. | `AAOI` | 9.6 | 9.2 | -12.9% | 14.7 | 576.8% | 156.5% | -15.5% | **10** | **25** |
| Alphabet Inc. | `GOOGL` | 8.8 | 8.6 | 34.0% | 20.8 | -26.6% | 25.3% | 0.6% | **12** | **23** |

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
