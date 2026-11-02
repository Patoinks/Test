# OKX Long / Short Fundamental Scanner

Hourly scanner restricted to public companies exposed by the **OKX EEA TradFi / Stock Perpetual API universe**.

**Last scan:** 2026-11-02 23:54 UTC  
**Availability scope:** user-confirmed OKX EEA Stock Futures / X-Perp  
**OKX stock/ETF markets in configured universe:** 72  
**Public companies analysed:** 55  
**SHORT CORE:** 3  
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
| 1 | Marvell Technology, Inc. | MRVL | -12.7% | -26.7% | -19.7% | 84 | +16 | **100** | **CORE** | yes |
| 2 | Sandisk Corporation | SNDK | -6.6% | -14.4% | -10.5% | 90 | +8 | **98** | **CORE** | yes |
| 3 | AXT Inc | AXT | -12.5% | -14.3% | -13.4% | 82 | +11 | **93** | **CORE** | yes |
| 4 | Applovin Corporation | APP | 0.2% | -12.2% | -6.0% | 87 | +5 | **92** | **CORE** | yes |
| 5 | Advanced Micro Devices, Inc. | AMD | -7.5% | -12.1% | -9.8% | 84 | +8 | **92** | **CORE** | yes |
| 6 | Taiwan Semiconductor Manufactur | TSM | -1.8% | -6.1% | -4.0% | 88 | +3 | **91** | **CORE** | yes |
| 7 | Credo Technology Group Holding  | CRDO | -7.3% | -7.4% | -7.3% | 82 | +6 | **88** | **CORE** | yes |
| 8 | NVIDIA Corporation | NVDA | -1.3% | -6.5% | -3.9% | 82 | +3 | **85** | **CORE** | yes |
| 9 | Applied Materials, Inc. | AMAT | -4.0% | -3.4% | -3.7% | 81 | +3 | **84** | **CORE** | yes |
| 10 | Robinhood Markets, Inc. | HOOD | -1.4% | -9.7% | -5.5% | 80 | +4 | **84** | **CORE** | yes |

## Final model + Price Timing — SHORT

| Rank | Company | OKX | 24h | 7d | 50/50 move | Base SHORT | Timing adj. | Final | Signal | Prev. SHORT? |
|---:|---|---|---:|---:|---:|---:|---:|---:|---|---|
| 1 | USA Rare Earth, Inc. | USAR | -8.0% | -0.6% | -4.3% | 100 | -3 | **97** | **CORE** | yes |
| 2 | Rocket Lab Corporation | RKLB | -4.9% | -3.3% | -4.1% | 100 | -3 | **97** | **CORE** | yes |
| 3 | IonQ, Inc. | IONQ | -6.2% | -8.4% | -7.3% | 82 | -6 | **76** | **CORE** | yes |
| 4 | Moderna, Inc. | MRNA | -0.4% | 11.1% | 5.3% | 72 | +4 | **76** | **CORE** | yes |
| 5 | Nebius Group N.V. | NBIS | -8.3% | -7.8% | -8.0% | 80 | -6 | **74** | **WATCH** | yes |
| 6 | AST SpaceMobile, Inc. | ASTS | -11.3% | -7.9% | -9.6% | 80 | -8 | **72** | **WATCH** | yes |
| 7 | Cerebras Systems Inc. | CBRS | -11.7% | -11.1% | -11.4% | 75 | -9 | **66** | **WATCH** | yes |
| 8 | Tesla, Inc. | TSLA | 1.0% | 3.1% | 2.1% | 59 | +2 | **61** | **WATCH** | yes |

## Combined model — LONG

Weighted score: **70% fundamental + 30% P/E trend**.

| Rank | Company | OKX | Fundamental LONG | P/E trend LONG | Combined | Signal |
|---:|---|---|---:|---:|---:|---|
| 1 | Sandisk Corporation | `SNDK` | 90 | 90 | **90** | **CORE** |
| 2 | Taiwan Semiconductor Manufactur | `TSM` | 90 | 85 | **88** | **CORE** |
| 3 | Applovin Corporation | `APP` | 90 | 80 | **87** | **CORE** |
| 4 | Marvell Technology, Inc. | `MRVL` | 77 | 100 | **84** | **CORE** |
| 5 | Advanced Micro Devices, Inc. | `AMD` | 77 | 100 | **84** | **CORE** |
| 6 | AXT Inc | `AXT` | 75 | 100 | **82** | **CORE** |
| 7 | Credo Technology Group Holding  | `CRDO` | 75 | 100 | **82** | **CORE** |
| 8 | NVIDIA Corporation | `NVDA` | 75 | 100 | **82** | **CORE** |
| 9 | Broadcom Inc. | `AVGO` | 75 | 100 | **82** | **CORE** |
| 10 | Applied Materials, Inc. | `AMAT` | 77 | 91 | **81** | **CORE** |

## Combined model — SHORT

Weighted score: **70% fundamental + 30% P/E trend**.

| Rank | Company | OKX | Fundamental SHORT | P/E trend SHORT | Combined | Signal |
|---:|---|---|---:|---:|---:|---|
| 1 | Rocket Lab Corporation | `RKLB` | 100 | 0 | **100** | **CORE** |
| 2 | USA Rare Earth, Inc. | `USAR` | 100 | 0 | **100** | **CORE** |
| 3 | IonQ, Inc. | `IONQ` | 82 | 0 | **82** | **WATCH** |
| 4 | Nebius Group N.V. | `NBIS` | 80 | 0 | **80** | **WATCH** |
| 5 | AST SpaceMobile, Inc. | `ASTS` | 80 | 0 | **80** | **WATCH** |
| 6 | Cerebras Systems Inc. | `CBRS` | 75 | 0 | **75** | **WATCH** |
| 7 | Moderna, Inc. | `MRNA` | 72 | 0 | **72** | **WATCH** |
| 8 | Okta, Inc. | `OKTA` | 80 | 13 | **60** | **WATCH** |
| 9 | Tesla, Inc. | `TSLA` | 78 | 15 | **59** | **WATCH** |

## P/E Compression + Growth — LONG

| Rank | Company | OKX | Trail P/E | Fwd P/E | P/E change | EPS +1y | Rev +1y | Rev trend | LONG score | Signal |
|---:|---|---|---:|---:|---:|---:|---:|---|---:|---|
| 1 | Marvell Technology, Inc. | `MRVL` | 56.4 | 23.4 | -58.5% | 74.2% | 63.7% | accelerating | **100** | **CORE** |
| 2 | AXT Inc | `AXT` | 98.4 | 18.2 | -81.5% | 125.3% | 115.8% | decelerating | **100** | **CORE** |
| 3 | Advanced Micro Devices, Inc. | `AMD` | 119.1 | 29.2 | -75.5% | 110.1% | 75.8% | accelerating | **100** | **CORE** |
| 4 | Credo Technology Group Holding  | `CRDO` | 49.7 | 14.4 | -71.0% | 53.9% | 55.0% | decelerating | **100** | **CORE** |
| 5 | NVIDIA Corporation | `NVDA` | 25.5 | 12.7 | -50.3% | 70.9% | 68.2% | decelerating | **100** | **CORE** |
| 6 | Broadcom Inc. | `AVGO` | 41.2 | 16.6 | -59.8% | 66.9% | 64.4% | decelerating | **100** | **CORE** |
| 7 | Oracle Corporation | `ORCL` | 18.7 | 10.8 | -42.4% | 36.1% | 45.9% | accelerating | **95** | **CORE** |
| 8 | Coherent Corp. | `COHR` | 48.5 | 14.3 | -70.5% | 48.4% | 38.6% | decelerating | **95** | **CORE** |
| 9 | Arm Holdings plc | `ARM` | 202.9 | 64.4 | -68.3% | 36.9% | 36.5% | accelerating | **95** | **CORE** |
| 10 | Bloom Energy Corporation | `BE` | 118.9 | 37.0 | -68.9% | 63.0% | 56.4% | decelerating | **92** | **CORE** |

## P/E Expansion + Weakening — SHORT

| Rank | Company | OKX | Trail P/E | Fwd P/E | P/E change | EPS +1y | Rev +1y | Rev trend | SHORT score | Signal |
|---:|---|---|---:|---:|---:|---:|---:|---|---:|---|
| 1 | SOFTBANK GROUP CORP | `SOFTBANK` | 5.2 | 14.9 | 186.3% | -14.5% | 7.0% | decelerating | **86** | **CORE** |
| 2 | Hyperliquid Strategies Inc | `PURR` | 3.0 | 26.2 | 767.6% | 51.0% | 31.4% | decelerating | **55** | **WATCH** |
| 3 | Amazon.com, Inc. | `AMZN` | 19.9 | 22.5 | 13.3% | -16.7% | 14.6% | decelerating | **52** | **WATCH** |
| 4 | Alphabet Inc. | `GOOGL` | 14.6 | 18.4 | 26.1% | -24.9% | 27.0% | accelerating | **50** | **WATCH** |

## Top SHORT candidates

| Rank | Company | OKX market | SHORT score | Signal | P/S | EV/S | Op margin | Fwd P/E | Rev +1y | FCF yield |
|---:|---|---|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Rocket Lab Corporation | `RKLB-USDT-SWAP` | **100** | **CORE** | 43.3 | 39.8 | -24.6% | 905.7 | 38.7% | -0.8% |
| 2 | USA Rare Earth, Inc. | `USAR-USDT-SWAP` | **100** | **CORE** | 252.3 | 63.6 | -795.6% | 295.2 | 870.1% | -8.5% |
| 3 | IonQ, Inc. | `IONQ-USDT-SWAP` | **82** | **WATCH** | 49.1 | 38.1 | -408.2% | -21.0 | 77.6% | -0.7% |
| 4 | Nebius Group N.V. | `NBIS-USDT-SWAP` | **80** | **WATCH** | 26.5 | 32.8 | -0.2% | -39.3 | 266.0% | -26.8% |
| 5 | Okta, Inc. | `OKTA-USDT-SWAP` | **80** | **CORE** | 10.5 | 11.1 | 13.3% | 42.2 | 10.1% | 3.2% |
| 6 | AST SpaceMobile, Inc. | `ASTS-USDT-SWAP` | **80** | **WATCH** | 122.6 | 117.0 | -544.6% | -25.0 | 264.2% | -12.7% |
| 7 | Tesla, Inc. | `TSLA-USDT-SWAP` | **78** | **WATCH** | 15.4 | 15.0 | 5.4% | 187.0 | 13.5% | 0.3% |
| 8 | Cerebras Systems Inc. | `CBRS-USDT-SWAP` | **75** | **WATCH** | 33.6 | 28.7 | -265.0% | 75.3 | 233.1% | — |
| 9 | Moderna, Inc. | `MRNA-USDT-SWAP` | **72** | **WATCH** | 39.6 | 38.0 | -557.9% | -48.2 | 16.3% | 0.3% |
| 10 | Circle Internet Group, Inc. | `CRCL-USDT-SWAP` | **33** | **WATCH** | 6.3 | 5.7 | 4.9% | 48.8 | 27.4% | 1.1% |

## Top LONG candidates

| Rank | Company | OKX market | LONG score | Signal | P/S | EV/S | Op margin | Fwd P/E | Rev +1y | FCF yield |
|---:|---|---|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Taiwan Semiconductor Manufactur | `TSM-USDT-SWAP` | **90** | **CORE** | 0.4 | 2.8 | 58.7% | 17.0 | 37.6% | 58.2% |
| 2 | Applovin Corporation | `APP-USDT-SWAP` | **90** | **CORE** | 11.2 | 11.3 | 77.7% | 11.4 | 24.9% | 4.2% |
| 3 | Sandisk Corporation | `SNDK-USDT-SWAP` | **90** | **CORE** | 5.3 | 5.5 | 79.6% | 3.7 | 22.3% | 7.3% |
| 4 | Corning Incorporated | `GLW-USDT-SWAP` | **77** | **WATCH** | 6.0 | 6.4 | 18.9% | 27.2 | 21.1% | 0.8% |
| 5 | Robinhood Markets, Inc. | `HOOD-USDT-SWAP` | **77** | **WATCH** | 14.9 | 14.6 | 48.1% | 24.8 | 29.2% | — |
| 6 | Applied Materials, Inc. | `AMAT-USDT-SWAP` | **77** | **WATCH** | 9.6 | 10.0 | 33.7% | 20.2 | 35.4% | 1.0% |
| 7 | Marvell Technology, Inc. | `MRVL-USDT-SWAP` | **77** | **WATCH** | 16.3 | 18.4 | 16.7% | 23.4 | 63.7% | 1.6% |
| 8 | Advanced Micro Devices, Inc. | `AMD-USDT-SWAP` | **77** | **WATCH** | 18.5 | 19.7 | 17.2% | 29.2 | 75.8% | 1.2% |
| 9 | Credo Technology Group Holding  | `CRDO-USDT-SWAP` | **75** | **WATCH** | 16.5 | 17.4 | 25.2% | 14.4 | 55.0% | 0.9% |
| 10 | Broadcom Inc. | `AVGO-USDT-SWAP` | **75** | **WATCH** | 17.3 | 17.9 | 54.3% | 16.6 | 64.4% | 2.0% |

## Analyst consensus (12-month price target) — most upside

| Rank | Company | OKX | Price | Analyst mean target | Gap | Analysts | Currency |
|---:|---|---|---:|---:|---:|---:|---|
| 1 | Cerebras Systems Inc. | `CBRS` | 96.36 | 275.27 | **185.7%** | 11 | USD |
| 2 | CoreWeave, Inc. | `CRWV` | 50.15 | 134.58 | **168.4%** | 38 | USD |
| 3 | Applied Optoelectronics, Inc. | `AAOI` | 62.50 | 156.00 | **149.6%** | 5 | USD |
| 4 | BitMine Immersion Technologies, | `BMNR` | 19.54 | 45.87 | **134.7%** | 3 | USD |
| 5 | Hyperliquid Strategies Inc | `PURR` | 9.71 | 22.32 | **129.9%** | 4 | USD |
| 6 | IonQ, Inc. | `IONQ` | 28.17 | 64.06 | **127.4%** | 14 | USD |
| 7 | SK hynix | `SKHYNIX` | 1472000.00 | 3157408.80 | **114.5%** | 39 | KRW |
| 8 | SamsungElec | `SAMSUNG` | 229000.00 | 480102.94 | **109.7%** | 35 | KRW |
| 9 | AST SpaceMobile, Inc. | `ASTS` | 36.33 | 74.68 | **105.6%** | 12 | USD |
| 10 | Credo Technology Group Holding  | `CRDO` | 140.02 | 284.05 | **102.9%** | 19 | USD |
| 11 | Nebius Group N.V. | `NBIS` | 141.39 | 281.00 | **98.7%** | 20 | USD |
| 12 | Oracle Corporation | `ORCL` | 119.22 | 234.10 | **96.4%** | 39 | USD |
| 13 | Rocket Lab Corporation | `RKLB` | 52.07 | 102.15 | **96.2%** | 20 | USD |
| 14 | Applovin Corporation | `APP` | 228.85 | 448.43 | **96.0%** | 31 | USD |
| 15 | Marvell Technology, Inc. | `MRVL` | 171.41 | 333.09 | **94.3%** | 41 | USD |

## Analyst consensus (12-month price target) — most downside

| Rank | Company | OKX | Price | Analyst mean target | Gap | Analysts | Currency |
|---:|---|---|---:|---:|---:|---:|---|
| 1 | Moderna, Inc. | `MRNA` | 220.83 | 138.37 | **-37.3%** | 19 | USD |
| 2 | Apple Inc. | `AAPL` | 338.32 | 332.39 | **-1.8%** | 38 | USD |

Price/target uses the underlying Yahoo Finance share quote, not the OKX derivative. Minimum 3 analysts; unreliable price scales and missing coverage excluded. Targets are analyst opinions, not guaranteed forecasts.

## All OKX companies — our ratio + LONG/SHORT scores

| Company | OKX | P/S | EV/S | Op margin | Fwd P/E | EPS +1y | Rev +1y | FCF yield | LONG | SHORT |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Rocket Lab Corporation | `RKLB` | 43.3 | 39.8 | -24.6% | 905.7 | 66.8% | 38.7% | -0.8% | **0** | **100 CORE** |
| USA Rare Earth, Inc. | `USAR` | 252.3 | 63.6 | -795.6% | 295.2 | 105.3% | 870.1% | -8.5% | **0** | **100 CORE** |
| Sandisk Corporation | `SNDK` | 5.3 | 5.5 | 79.6% | 3.7 | 26.1% | 22.3% | 7.3% | **90 CORE** | **10** |
| Applovin Corporation | `APP` | 11.2 | 11.3 | 77.7% | 11.4 | 25.7% | 24.9% | 4.2% | **90 CORE** | **10** |
| Taiwan Semiconductor Manufactur | `TSM` | 0.4 | 2.8 | 58.7% | 17.0 | 33.6% | 37.6% | 58.2% | **90 CORE** | **10** |
| IonQ, Inc. | `IONQ` | 49.1 | 38.1 | -408.2% | -21.0 | 21.3% | 77.6% | -0.7% | **0** | **82 WATCH** |
| Okta, Inc. | `OKTA` | 10.5 | 11.1 | 13.3% | 42.2 | 11.4% | 10.1% | 3.2% | **8** | **80 CORE** |
| Nebius Group N.V. | `NBIS` | 26.5 | 32.8 | -0.2% | -39.3 | -191.4% | 266.0% | -26.8% | **0** | **80 WATCH** |
| AST SpaceMobile, Inc. | `ASTS` | 122.6 | 117.0 | -544.6% | -25.0 | 44.3% | 264.2% | -12.7% | **0** | **80 WATCH** |
| Tesla, Inc. | `TSLA` | 15.4 | 15.0 | 5.4% | 187.0 | 24.2% | 13.5% | 0.3% | **12** | **78 WATCH** |
| Marvell Technology, Inc. | `MRVL` | 16.3 | 18.4 | 16.7% | 23.4 | 74.2% | 63.7% | 1.6% | **77 WATCH** | **13** |
| Advanced Micro Devices, Inc. | `AMD` | 18.5 | 19.7 | 17.2% | 29.2 | 110.1% | 75.8% | 1.2% | **77 WATCH** | **13** |
| Robinhood Markets, Inc. | `HOOD` | 14.9 | 14.6 | 48.1% | 24.8 | 39.6% | 29.2% | — | **77 WATCH** | **0** |
| Applied Materials, Inc. | `AMAT` | 9.6 | 10.0 | 33.7% | 20.2 | 45.0% | 35.4% | 1.0% | **77 WATCH** | **3** |
| Corning Incorporated | `GLW` | 6.0 | 6.4 | 18.9% | 27.2 | 34.1% | 21.1% | 0.8% | **77 WATCH** | **13** |
| AXT Inc | `AXT` | 18.5 | 18.7 | 38.7% | 18.2 | 125.3% | 115.8% | — | **75 WATCH** | **20** |
| Credo Technology Group Holding  | `CRDO` | 16.5 | 17.4 | 25.2% | 14.4 | 53.9% | 55.0% | 0.9% | **75 WATCH** | **28** |
| NVIDIA Corporation | `NVDA` | 16.1 | 16.2 | 66.2% | 12.7 | 70.9% | 68.2% | 0.9% | **75 WATCH** | **18** |
| Broadcom Inc. | `AVGO` | 17.3 | 17.9 | 54.3% | 16.6 | 66.9% | 64.4% | 2.0% | **75 WATCH** | **28** |
| Micron Technology, Inc. | `MU` | 7.1 | 7.2 | 80.7% | 4.0 | 17.7% | 16.2% | 3.1% | **75 CORE** | **30** |
| Western Digital Corporation | `WDC` | 8.8 | 9.4 | 47.7% | 8.4 | 63.4% | 40.5% | 2.2% | **75 WATCH** | **18** |
| Cerebras Systems Inc. | `CBRS` | 33.6 | 28.7 | -265.0% | 75.3 | 372.9% | 233.1% | — | **0** | **75 WATCH** |
| Moderna, Inc. | `MRNA` | 39.6 | 38.0 | -557.9% | -48.2 | 42.3% | 16.3% | 0.3% | **0** | **72 WATCH** |
| Oracle Corporation | `ORCL` | 5.0 | 7.4 | 35.6% | 10.8 | 36.1% | 45.9% | -12.7% | **70 WATCH** | **10** |
| XIAOMI-W | `XIAOMI` | 1.7 | 1.5 | 4.0% | 18.7 | 36.9% | 19.7% | -1.2% | **70 WATCH** | **10** |
| Microsoft Corporation | `MSFT` | 10.9 | 11.4 | 49.8% | 21.0 | 21.8% | 20.2% | 0.1% | **69 WATCH** | **3** |
| Dell Technologies Inc. | `DELL` | 1.7 | 1.9 | 12.0% | 13.0 | 16.2% | 19.2% | 2.4% | **67 WATCH** | **38** |
| Adobe Inc. | `ADBE` | 3.8 | 3.8 | 34.8% | 9.2 | 12.1% | 9.1% | 9.5% | **65 WATCH** | **30** |
| Coherent Corp. | `COHR` | 5.5 | 6.1 | 11.8% | 14.3 | 48.4% | 38.6% | -1.7% | **60 WATCH** | **35** |
| Apple Inc. | `AAPL` | 10.6 | 10.8 | 32.6% | 35.4 | 12.9% | 8.7% | 2.2% | **5** | **58** |
| Coca-Cola Company (The) | `KO` | 8.1 | 8.5 | 33.4% | 27.2 | 5.6% | -3.1% | 1.1% | **0** | **58** |
| Meta Platforms, Inc. | `META` | 6.4 | 6.6 | 35.4% | 17.0 | 16.5% | 21.6% | 1.1% | **57 WATCH** | **38** |
| Lumentum Holdings Inc. | `LITE` | 20.6 | 24.7 | 28.0% | 18.5 | 49.7% | 47.4% | 0.4% | **2** | **56** |
| Super Micro Computer, Inc. | `SMCI` | 0.5 | 0.7 | 13.4% | 5.4 | 19.6% | 16.2% | -41.9% | **52** | **45** |
| Netflix, Inc. | `NFLX` | 5.2 | 5.3 | 34.6% | 16.5 | 5.1% | 10.7% | 9.8% | **35** | **50** |
| IREN LIMITED | `IREN` | 12.6 | 16.1 | -102.5% | -5.5 | -16.4% | 164.0% | -47.4% | **0** | **50** |
| Palantir Technologies Inc. | `PLTR` | 69.6 | 70.4 | 47.1% | 76.3 | 45.6% | 50.8% | 0.5% | **33** | **48** |
| Bloom Energy Corporation | `BE` | 15.1 | 15.8 | 18.5% | 37.0 | 63.0% | 56.4% | -0.0% | **45** | **35** |
| SamsungElec | `SAMSUNG` | 2.5 | 2.2 | 55.0% | 3.0 | 63.8% | 39.6% | 5.6% | **45** | **10** |
| Amazon.com, Inc. | `AMZN` | 3.3 | 3.5 | 13.9% | 22.5 | -16.7% | 14.6% | -1.3% | **0** | **45** |
| Arm Holdings plc | `ARM` | 40.8 | 42.0 | 7.6% | 64.4 | 36.9% | 36.5% | 0.6% | **43** | **33** |
| Coinbase Global, Inc. | `COIN` | 6.7 | 6.6 | -1.4% | 55.8 | 785.9% | 26.3% | 10.1% | **20** | **40** |
| SOFTBANK GROUP CORP | `SOFTBANK` | 3.1 | 6.5 | -11.6% | 14.9 | -14.5% | 7.0% | -8.7% | **0** | **40** |
| CoreWeave, Inc. | `CRWV` | 3.6 | 10.1 | -1.9% | -25.5 | 9.7% | 105.6% | -32.9% | **0** | **40** |
| Circle Internet Group, Inc. | `CRCL` | 6.3 | 5.7 | 4.9% | 48.8 | 24.1% | 27.4% | 1.1% | **27** | **33 WATCH** |
| SK hynix | `SKHYNIX` | 3.9 | 3.6 | 79.7% | 2.8 | 47.0% | 58.5% | — | **30** | **5** |
| SK hynix | `SKHY` | 3.9 | 3.6 | 79.7% | 2.8 | 47.0% | 58.5% | — | **30** | **5** |
| Alphabet Inc. | `GOOGL` | 7.3 | 7.1 | 31.8% | 18.4 | -24.9% | 27.0% | -0.0% | **5** | **30** |
| Intel Corporation | `INTC` | 5.3 | 6.0 | 15.6% | 33.2 | 21.5% | 12.1% | 0.3% | **5** | **28** |
| Fluence Energy, Inc. | `FLNC` | 0.4 | 0.4 | -8.9% | -9.8 | 59.3% | 25.4% | 0.2% | **5** | **28** |
| Hyperliquid Strategies Inc | `PURR` | 285.6 | 215.7 | 9595.1% | 26.2 | 51.0% | 31.4% | — | **25** | **10** |
| BitMine Immersion Technologies, | `BMNR` | 192.6 | 193.4 | 8.4% | 20.8 | 103.2% | 421.8% | -4.4% | **25** | **25** |
| Strategy Inc | `MSTR` | 111.9 | 139.4 | 16670.9% | 5.5 | 261.1% | 3.0% | — | **25** | **10** |
| QUALCOMM Incorporated | `QCOM` | 3.9 | 4.1 | 18.5% | 15.9 | -3.4% | 4.7% | 5.9% | **25** | **15** |
| Applied Optoelectronics, Inc. | `AAOI` | 8.9 | 9.5 | -12.9% | 13.6 | 576.8% | 156.5% | -16.7% | **10** | **25** |

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
