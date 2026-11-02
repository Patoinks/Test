# OKX Long / Short Fundamental Scanner

Hourly scanner restricted to public companies exposed by the **OKX EEA TradFi / Stock Perpetual API universe**.

**Last scan:** 2026-11-02 17:10 UTC  
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
| 1 | Marvell Technology, Inc. | MRVL | -8.9% | -23.5% | -16.2% | 84 | +13 | **97** | **CORE** | yes |
| 2 | Sandisk Corporation | SNDK | -2.5% | -10.6% | -6.6% | 90 | +5 | **95** | **CORE** | yes |
| 3 | Taiwan Semiconductor Manufactur | TSM | 0.0% | -4.3% | -2.1% | 88 | +2 | **90** | **CORE** | yes |
| 4 | Credo Technology Group Holding  | CRDO | -2.8% | -2.9% | -2.9% | 82 | +2 | **84** | **CORE** | yes |
| 5 | Applovin Corporation | APP | 4.1% | -8.7% | -2.3% | 82 | +2 | **84** | **CORE** | yes |
| 6 | NVIDIA Corporation | NVDA | 1.0% | -4.3% | -1.6% | 82 | +1 | **83** | **CORE** | yes |
| 7 | Advanced Micro Devices, Inc. | AMD | -3.1% | -7.9% | -5.5% | 79 | +4 | **83** | **CORE** | yes |
| 8 | Robinhood Markets, Inc. | HOOD | 1.5% | -7.1% | -2.8% | 80 | +2 | **82** | **CORE** | yes |
| 9 | Oracle Corporation | ORCL | -6.6% | -3.2% | -4.9% | 78 | +4 | **82** | **CORE** | yes |
| 10 | Broadcom Inc. | AVGO | 1.3% | 0.3% | 0.8% | 82 | -1 | **81** | **CORE** | yes |

## Final model + Price Timing — SHORT

| Rank | Company | OKX | 24h | 7d | 50/50 move | Base SHORT | Timing adj. | Final | Signal | Prev. SHORT? |
|---:|---|---|---:|---:|---:|---:|---:|---:|---|---|
| 1 | USA Rare Earth, Inc. | USAR | -2.1% | 5.7% | 1.8% | 100 | +1 | **100** | **CORE** | yes |
| 2 | Rocket Lab Corporation | RKLB | -2.2% | -0.5% | -1.3% | 100 | -1 | **99** | **CORE** | yes |
| 3 | Moderna, Inc. | MRNA | 2.2% | 13.9% | 8.0% | 80 | +6 | **86** | **CORE** | yes |
| 4 | IonQ, Inc. | IONQ | -1.8% | -4.1% | -2.9% | 85 | -2 | **83** | **CORE** | yes |
| 5 | AST SpaceMobile, Inc. | ASTS | -4.7% | -1.1% | -2.9% | 80 | -2 | **78** | **CORE** | yes |
| 6 | Nebius Group N.V. | NBIS | -3.5% | -3.0% | -3.2% | 80 | -3 | **77** | **CORE** | yes |
| 7 | Cerebras Systems Inc. | CBRS | -9.7% | -9.0% | -9.4% | 75 | -7 | **68** | **WATCH** | yes |
| 8 | Tesla, Inc. | TSLA | 3.1% | 5.2% | 4.2% | 59 | +3 | **62** | **WATCH** | yes |

## Combined model — LONG

Weighted score: **70% fundamental + 30% P/E trend**.

| Rank | Company | OKX | Fundamental LONG | P/E trend LONG | Combined | Signal |
|---:|---|---|---:|---:|---:|---|
| 1 | Sandisk Corporation | `SNDK` | 90 | 90 | **90** | **CORE** |
| 2 | Taiwan Semiconductor Manufactur | `TSM` | 90 | 85 | **88** | **CORE** |
| 3 | Marvell Technology, Inc. | `MRVL` | 77 | 100 | **84** | **CORE** |
| 4 | Applovin Corporation | `APP` | 83 | 80 | **82** | **CORE** |
| 5 | Credo Technology Group Holding  | `CRDO` | 75 | 100 | **82** | **CORE** |
| 6 | NVIDIA Corporation | `NVDA` | 75 | 100 | **82** | **CORE** |
| 7 | Broadcom Inc. | `AVGO` | 75 | 100 | **82** | **CORE** |
| 8 | Applied Materials, Inc. | `AMAT` | 77 | 91 | **81** | **CORE** |
| 9 | Robinhood Markets, Inc. | `HOOD` | 77 | 86 | **80** | **CORE** |
| 10 | Corning Incorporated | `GLW` | 77 | 86 | **80** | **CORE** |

## Combined model — SHORT

Weighted score: **70% fundamental + 30% P/E trend**.

| Rank | Company | OKX | Fundamental SHORT | P/E trend SHORT | Combined | Signal |
|---:|---|---|---:|---:|---:|---|
| 1 | USA Rare Earth, Inc. | `USAR` | 100 | 0 | **100** | **CORE** |
| 2 | Rocket Lab Corporation | `RKLB` | 100 | 0 | **100** | **CORE** |
| 3 | IonQ, Inc. | `IONQ` | 85 | 0 | **85** | **CORE** |
| 4 | Moderna, Inc. | `MRNA` | 80 | 0 | **80** | **WATCH** |
| 5 | AST SpaceMobile, Inc. | `ASTS` | 80 | 0 | **80** | **WATCH** |
| 6 | Nebius Group N.V. | `NBIS` | 80 | 0 | **80** | **WATCH** |
| 7 | Cerebras Systems Inc. | `CBRS` | 75 | 0 | **75** | **WATCH** |
| 8 | Okta, Inc. | `OKTA` | 80 | 13 | **60** | **WATCH** |
| 9 | Tesla, Inc. | `TSLA` | 78 | 15 | **59** | **WATCH** |

## P/E Compression + Growth — LONG

| Rank | Company | OKX | Trail P/E | Fwd P/E | P/E change | EPS +1y | Rev +1y | Rev trend | LONG score | Signal |
|---:|---|---|---:|---:|---:|---:|---:|---|---:|---|
| 1 | Marvell Technology, Inc. | `MRVL` | 58.9 | 24.4 | -58.5% | 73.6% | 63.3% | accelerating | **100** | **CORE** |
| 2 | Credo Technology Group Holding  | `CRDO` | 52.0 | 15.1 | -71.0% | 53.9% | 55.0% | decelerating | **100** | **CORE** |
| 3 | NVIDIA Corporation | `NVDA` | 26.1 | 13.0 | -50.3% | 70.9% | 68.2% | decelerating | **100** | **CORE** |
| 4 | Advanced Micro Devices, Inc. | `AMD` | 124.8 | 30.6 | -75.5% | 110.0% | 75.8% | accelerating | **100** | **CORE** |
| 5 | Broadcom Inc. | `AVGO` | 42.2 | 17.0 | -59.8% | 66.9% | 64.4% | decelerating | **100** | **CORE** |
| 6 | AXT Inc | `AXT` | 109.9 | 20.3 | -81.5% | 125.3% | 115.8% | decelerating | **96** | **CORE** |
| 7 | Oracle Corporation | `ORCL` | 19.1 | 11.0 | -42.4% | 35.6% | 45.7% | accelerating | **95** | **CORE** |
| 8 | Coherent Corp. | `COHR` | 50.4 | 14.9 | -70.5% | 48.0% | 38.1% | decelerating | **95** | **CORE** |
| 9 | Arm Holdings plc | `ARM` | 210.1 | 66.7 | -68.3% | 37.5% | 36.5% | accelerating | **95** | **CORE** |
| 10 | Bloom Energy Corporation | `BE` | 123.8 | 38.4 | -69.0% | 63.0% | 56.4% | decelerating | **92** | **CORE** |

## P/E Expansion + Weakening — SHORT

| Rank | Company | OKX | Trail P/E | Fwd P/E | P/E change | EPS +1y | Rev +1y | Rev trend | SHORT score | Signal |
|---:|---|---|---:|---:|---:|---:|---:|---|---:|---|
| 1 | SOFTBANK GROUP CORP | `SOFTBANK` | 5.1 | 14.9 | 191.0% | -14.5% | 7.0% | decelerating | **86** | **CORE** |
| 2 | Hyperliquid Strategies Inc | `PURR` | 3.2 | 27.7 | 767.6% | 51.0% | 31.4% | decelerating | **55** | **WATCH** |
| 3 | Amazon.com, Inc. | `AMZN` | 20.3 | 23.0 | 13.3% | -16.8% | 14.6% | decelerating | **52** | **WATCH** |
| 4 | Alphabet Inc. | `GOOGL` | 14.8 | 18.7 | 26.3% | -24.7% | 27.0% | accelerating | **50** | **WATCH** |

## Top SHORT candidates

| Rank | Company | OKX market | SHORT score | Signal | P/S | EV/S | Op margin | Fwd P/E | Rev +1y | FCF yield |
|---:|---|---|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Rocket Lab Corporation | `RKLB-USDT-SWAP` | **100** | **CORE** | 44.5 | 39.8 | -24.6% | 931.4 | 38.7% | -0.7% |
| 2 | USA Rare Earth, Inc. | `USAR-USDT-SWAP` | **100** | **CORE** | 268.4 | 63.6 | -795.6% | 314.0 | 870.1% | -8.0% |
| 3 | IonQ, Inc. | `IONQ-USDT-SWAP` | **85** | **CORE** | 51.4 | 38.1 | -408.2% | -22.0 | 77.6% | -0.7% |
| 4 | Nebius Group N.V. | `NBIS-USDT-SWAP` | **80** | **WATCH** | 29.8 | 32.8 | -0.2% | -41.3 | 266.0% | -23.8% |
| 5 | Okta, Inc. | `OKTA-USDT-SWAP` | **80** | **CORE** | 11.3 | 11.1 | 13.3% | 45.2 | 10.1% | 3.0% |
| 6 | AST SpaceMobile, Inc. | `ASTS-USDT-SWAP` | **80** | **WATCH** | 131.7 | 117.0 | -544.6% | -26.9 | 264.2% | -11.8% |
| 7 | Moderna, Inc. | `MRNA-USDT-SWAP` | **80** | **WATCH** | 40.6 | 38.0 | -557.9% | -49.4 | 16.3% | 0.3% |
| 8 | Tesla, Inc. | `TSLA-USDT-SWAP` | **78** | **WATCH** | 15.7 | 15.0 | 5.4% | 190.9 | 13.5% | 0.3% |
| 9 | Cerebras Systems Inc. | `CBRS-USDT-SWAP` | **75** | **WATCH** | 34.4 | 28.7 | -265.0% | 77.1 | 232.7% | — |

## Top LONG candidates

| Rank | Company | OKX market | LONG score | Signal | P/S | EV/S | Op margin | Fwd P/E | Rev +1y | FCF yield |
|---:|---|---|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Taiwan Semiconductor Manufactur | `TSM-USDT-SWAP` | **90** | **CORE** | 0.4 | 2.8 | 58.7% | 17.4 | 37.6% | 57.1% |
| 2 | Sandisk Corporation | `SNDK-USDT-SWAP` | **90** | **CORE** | 5.5 | 5.5 | 79.6% | 3.9 | 22.5% | 7.0% |
| 3 | Applovin Corporation | `APP-USDT-SWAP` | **83** | **CORE** | 11.7 | 11.3 | 77.7% | 11.9 | 24.9% | 4.0% |
| 4 | Corning Incorporated | `GLW-USDT-SWAP` | **77** | **WATCH** | 6.1 | 6.4 | 18.9% | 28.0 | 21.1% | 0.8% |
| 5 | Robinhood Markets, Inc. | `HOOD-USDT-SWAP` | **77** | **WATCH** | 15.3 | 14.6 | 48.1% | 25.5 | 29.2% | — |
| 6 | Applied Materials, Inc. | `AMAT-USDT-SWAP` | **77** | **WATCH** | 10.1 | 10.0 | 33.7% | 21.1 | 35.4% | 1.0% |
| 7 | Marvell Technology, Inc. | `MRVL-USDT-SWAP` | **77** | **WATCH** | 17.0 | 18.4 | 16.7% | 24.4 | 63.3% | 1.5% |
| 8 | Credo Technology Group Holding  | `CRDO-USDT-SWAP` | **75** | **WATCH** | 17.3 | 17.4 | 25.2% | 15.1 | 55.0% | 0.9% |
| 9 | Broadcom Inc. | `AVGO-USDT-SWAP` | **75** | **WATCH** | 17.7 | 17.9 | 54.3% | 17.0 | 64.4% | 1.9% |
| 10 | Micron Technology, Inc. | `MU-USDT-SWAP` | **75** | **CORE** | 7.3 | 7.2 | 80.7% | 4.1 | 16.0% | 3.0% |

## Analyst consensus (12-month price target) — most upside

| Rank | Company | OKX | Price | Analyst mean target | Gap | Analysts | Currency |
|---:|---|---|---:|---:|---:|---:|---|
| 1 | Cerebras Systems Inc. | `CBRS` | 98.60 | 282.55 | **186.6%** | 11 | USD |
| 2 | CoreWeave, Inc. | `CRWV` | 52.63 | 134.58 | **155.7%** | 38 | USD |
| 3 | Applied Optoelectronics, Inc. | `AAOI` | 66.86 | 156.00 | **133.3%** | 5 | USD |
| 4 | BitMine Immersion Technologies, | `BMNR` | 20.38 | 45.87 | **125.1%** | 3 | USD |
| 5 | Hyperliquid Strategies Inc | `PURR` | 10.23 | 22.32 | **118.1%** | 4 | USD |
| 6 | IonQ, Inc. | `IONQ` | 29.50 | 64.06 | **117.1%** | 14 | USD |
| 7 | SK hynix | `SKHYNIX` | 1472000.00 | 3157408.80 | **114.5%** | 39 | KRW |
| 8 | SamsungElec | `SAMSUNG` | 229000.00 | 480102.94 | **109.7%** | 35 | KRW |
| 9 | Credo Technology Group Holding  | `CRDO` | 146.74 | 284.05 | **93.6%** | 19 | USD |
| 10 | Oracle Corporation | `ORCL` | 122.01 | 235.56 | **93.1%** | 41 | USD |
| 11 | AST SpaceMobile, Inc. | `ASTS` | 39.02 | 74.68 | **91.4%** | 12 | USD |
| 12 | Rocket Lab Corporation | `RKLB` | 53.55 | 102.15 | **90.8%** | 20 | USD |
| 13 | Marvell Technology, Inc. | `MRVL` | 178.87 | 340.56 | **90.4%** | 44 | USD |
| 14 | Nebius Group N.V. | `NBIS` | 148.72 | 281.00 | **88.9%** | 20 | USD |
| 15 | Applovin Corporation | `APP` | 237.96 | 448.43 | **88.4%** | 31 | USD |

## Analyst consensus (12-month price target) — most downside

| Rank | Company | OKX | Price | Analyst mean target | Gap | Analysts | Currency |
|---:|---|---|---:|---:|---:|---:|---|
| 1 | Moderna, Inc. | `MRNA` | 226.49 | 138.37 | **-38.9%** | 19 | USD |
| 2 | Apple Inc. | `AAPL` | 338.25 | 332.39 | **-1.7%** | 38 | USD |

Price/target uses the underlying Yahoo Finance share quote, not the OKX derivative. Minimum 3 analysts; unreliable price scales and missing coverage excluded. Targets are analyst opinions, not guaranteed forecasts.

## All OKX companies — our ratio + LONG/SHORT scores

| Company | OKX | P/S | EV/S | Op margin | Fwd P/E | EPS +1y | Rev +1y | FCF yield | LONG | SHORT |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| USA Rare Earth, Inc. | `USAR` | 268.4 | 63.6 | -795.6% | 314.0 | 105.3% | 870.1% | -8.0% | **0** | **100 CORE** |
| Rocket Lab Corporation | `RKLB` | 44.5 | 39.8 | -24.6% | 931.4 | 66.8% | 38.7% | -0.7% | **0** | **100 CORE** |
| Sandisk Corporation | `SNDK` | 5.5 | 5.5 | 79.6% | 3.9 | 26.5% | 22.5% | 7.0% | **90 CORE** | **10** |
| Taiwan Semiconductor Manufactur | `TSM` | 0.4 | 2.8 | 58.7% | 17.4 | 33.6% | 37.6% | 57.1% | **90 CORE** | **10** |
| IonQ, Inc. | `IONQ` | 51.4 | 38.1 | -408.2% | -22.0 | 21.3% | 77.6% | -0.7% | **0** | **85 CORE** |
| Applovin Corporation | `APP` | 11.7 | 11.3 | 77.7% | 11.9 | 25.7% | 24.9% | 4.0% | **83 CORE** | **10** |
| Okta, Inc. | `OKTA` | 11.3 | 11.1 | 13.3% | 45.2 | 11.4% | 10.1% | 3.0% | **8** | **80 CORE** |
| Moderna, Inc. | `MRNA` | 40.6 | 38.0 | -557.9% | -49.4 | 42.3% | 16.3% | 0.3% | **0** | **80 WATCH** |
| AST SpaceMobile, Inc. | `ASTS` | 131.7 | 117.0 | -544.6% | -26.9 | 44.3% | 264.2% | -11.8% | **0** | **80 WATCH** |
| Nebius Group N.V. | `NBIS` | 29.8 | 32.8 | -0.2% | -41.3 | -191.4% | 266.0% | -23.8% | **0** | **80 WATCH** |
| Tesla, Inc. | `TSLA` | 15.7 | 15.0 | 5.4% | 190.9 | 24.2% | 13.5% | 0.3% | **12** | **78 WATCH** |
| Marvell Technology, Inc. | `MRVL` | 17.0 | 18.4 | 16.7% | 24.4 | 73.6% | 63.3% | 1.5% | **77 WATCH** | **13** |
| Robinhood Markets, Inc. | `HOOD` | 15.3 | 14.6 | 48.1% | 25.5 | 39.5% | 29.2% | — | **77 WATCH** | **0** |
| Applied Materials, Inc. | `AMAT` | 10.1 | 10.0 | 33.7% | 21.1 | 45.0% | 35.4% | 1.0% | **77 WATCH** | **3** |
| Corning Incorporated | `GLW` | 6.1 | 6.4 | 18.9% | 28.0 | 34.1% | 21.1% | 0.8% | **77 WATCH** | **13** |
| Credo Technology Group Holding  | `CRDO` | 17.3 | 17.4 | 25.2% | 15.1 | 53.9% | 55.0% | 0.9% | **75 WATCH** | **28** |
| NVIDIA Corporation | `NVDA` | 16.5 | 16.2 | 66.2% | 13.0 | 70.9% | 68.2% | 0.8% | **75 WATCH** | **18** |
| Broadcom Inc. | `AVGO` | 17.7 | 17.9 | 54.3% | 17.0 | 66.9% | 64.4% | 1.9% | **75 WATCH** | **28** |
| Micron Technology, Inc. | `MU` | 7.3 | 7.2 | 80.7% | 4.1 | 17.7% | 16.0% | 3.0% | **75 CORE** | **30** |
| Western Digital Corporation | `WDC` | 9.0 | 9.4 | 47.7% | 8.6 | 63.4% | 40.5% | 2.1% | **75 WATCH** | **18** |
| Cerebras Systems Inc. | `CBRS` | 34.4 | 28.7 | -265.0% | 77.1 | 371.3% | 232.7% | — | **0** | **75 WATCH** |
| Advanced Micro Devices, Inc. | `AMD` | 19.3 | 19.7 | 17.2% | 30.6 | 110.0% | 75.8% | 1.1% | **70 WATCH** | **13** |
| Oracle Corporation | `ORCL` | 5.2 | 7.4 | 35.6% | 11.0 | 35.6% | 45.7% | -12.4% | **70 WATCH** | **10** |
| XIAOMI-W | `XIAOMI` | 1.7 | 1.4 | 4.0% | 18.8 | 36.0% | 19.5% | -1.2% | **70 WATCH** | **10** |
| AXT Inc | `AXT` | 20.7 | 18.7 | 38.7% | 20.3 | 125.3% | 115.8% | — | **67 WATCH** | **20** |
| Dell Technologies Inc. | `DELL` | 1.7 | 1.9 | 12.0% | 13.7 | 16.2% | 19.2% | 2.3% | **67 WATCH** | **38** |
| Adobe Inc. | `ADBE` | 3.8 | 3.8 | 34.8% | 9.2 | 12.4% | 9.1% | 9.5% | **65 WATCH** | **30** |
| Coherent Corp. | `COHR` | 5.7 | 6.1 | 11.8% | 14.9 | 48.0% | 38.1% | -1.6% | **60 WATCH** | **35** |
| Microsoft Corporation | `MSFT` | 11.2 | 11.4 | 49.8% | 21.6 | 20.9% | 20.2% | 0.1% | **59 WATCH** | **3** |
| Apple Inc. | `AAPL` | 10.6 | 10.8 | 32.6% | 35.4 | 8.3% | 9.9% | 2.2% | **5** | **58** |
| Coca-Cola Company (The) | `KO` | 8.0 | 8.5 | 33.4% | 27.0 | 5.6% | -3.1% | 1.1% | **0** | **58** |
| Meta Platforms, Inc. | `META` | 6.5 | 6.6 | 35.4% | 17.2 | 16.5% | 21.6% | 1.1% | **57 WATCH** | **38** |
| Super Micro Computer, Inc. | `SMCI` | 0.5 | 0.7 | 13.4% | 5.6 | 19.6% | 16.2% | -39.4% | **52** | **45** |
| Lumentum Holdings Inc. | `LITE` | 21.7 | 24.7 | 28.0% | 20.2 | 63.7% | 56.5% | 0.3% | **0** | **51** |
| Netflix, Inc. | `NFLX` | 5.2 | 5.3 | 34.6% | 16.5 | 5.1% | 10.7% | 9.8% | **35** | **50** |
| IREN LIMITED | `IREN` | 13.3 | 16.1 | -102.5% | -5.8 | -16.4% | 164.0% | -44.9% | **0** | **50** |
| Palantir Technologies Inc. | `PLTR` | 71.8 | 70.4 | 47.1% | 78.3 | 45.6% | 50.8% | 0.5% | **33** | **48** |
| Bloom Energy Corporation | `BE` | 15.8 | 15.8 | 18.5% | 38.4 | 63.0% | 56.4% | -0.0% | **45** | **35** |
| SamsungElec | `SAMSUNG` | 2.5 | 2.2 | 55.0% | 3.0 | 63.8% | 39.6% | 5.6% | **45** | **10** |
| Amazon.com, Inc. | `AMZN` | 3.4 | 3.5 | 13.9% | 23.0 | -16.8% | 14.6% | -1.3% | **0** | **45** |
| Arm Holdings plc | `ARM` | 42.2 | 42.0 | 7.6% | 66.7 | 37.5% | 36.5% | 0.6% | **43** | **33** |
| Circle Internet Group, Inc. | `CRCL` | 6.5 | 5.7 | 4.9% | 50.7 | 27.0% | 27.4% | 1.1% | **43** | **33** |
| Coinbase Global, Inc. | `COIN` | 6.8 | 6.6 | -1.4% | 56.6 | 829.2% | 27.1% | 9.9% | **20** | **40** |
| SOFTBANK GROUP CORP | `SOFTBANK` | 3.1 | 6.5 | -11.6% | 14.9 | -14.5% | 7.0% | -8.7% | **0** | **40** |
| CoreWeave, Inc. | `CRWV` | 3.8 | 10.1 | -1.9% | -26.7 | 9.7% | 105.6% | -31.3% | **0** | **40** |
| SK hynix | `SKHYNIX` | 3.9 | 3.6 | 79.7% | 2.8 | 47.0% | 58.5% | — | **30** | **5** |
| SK hynix | `SKHY` | 3.9 | 3.6 | 79.7% | 2.8 | 47.0% | 58.5% | — | **30** | **5** |
| Alphabet Inc. | `GOOGL` | 7.4 | 7.1 | 31.8% | 18.7 | -24.7% | 27.0% | -0.0% | **5** | **30** |
| Intel Corporation | `INTC` | 5.6 | 6.0 | 15.6% | 34.8 | 21.9% | 12.1% | 0.2% | **5** | **28** |
| Fluence Energy, Inc. | `FLNC` | 0.4 | 0.4 | -8.9% | -10.1 | 59.3% | 25.4% | 0.2% | **5** | **28** |
| Hyperliquid Strategies Inc | `PURR` | 301.1 | 215.7 | 9595.1% | 27.7 | 51.0% | 31.4% | — | **25** | **10** |
| Strategy Inc | `MSTR` | 115.0 | 139.4 | 16670.9% | 5.7 | 40.6% | 3.0% | — | **25** | **10** |
| BitMine Immersion Technologies, | `BMNR` | 200.8 | 193.4 | 8.4% | 21.7 | 103.2% | 421.8% | -4.2% | **25** | **25** |
| QUALCOMM Incorporated | `QCOM` | 4.1 | 4.1 | 18.5% | 16.5 | -3.0% | 4.5% | 5.7% | **25** | **15** |
| Applied Optoelectronics, Inc. | `AAOI` | 9.5 | 9.5 | -12.9% | 14.5 | 576.8% | 156.5% | -15.6% | **10** | **25** |

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
