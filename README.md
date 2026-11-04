# OKX Long / Short Fundamental Scanner

Hourly scanner restricted to public companies exposed by the **OKX EEA TradFi / Stock Perpetual API universe**.

**Last scan:** 2026-11-04 09:25 UTC  
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
| 1 | Sandisk Corporation | SNDK | -0.0% | -19.8% | -9.9% | 90 | +8 | **98** | **CORE** | yes |
| 2 | Marvell Technology, Inc. | MRVL | -0.0% | -31.7% | -15.8% | 84 | +13 | **97** | **CORE** | yes |
| 3 | Taiwan Semiconductor Manufactur | TSM | 0.0% | -7.9% | -3.9% | 88 | +3 | **91** | **CORE** | yes |
| 4 | Advanced Micro Devices, Inc. | AMD | 0.0% | -16.3% | -8.2% | 84 | +7 | **91** | **CORE** | yes |
| 5 | Credo Technology Group Holding  | CRDO | -0.0% | -13.1% | -6.6% | 82 | +5 | **87** | **CORE** | yes |
| 6 | Applovin Corporation | APP | 0.0% | -5.6% | -2.8% | 82 | +2 | **84** | **CORE** | yes |
| 7 | Broadcom Inc. | AVGO | -0.0% | -5.6% | -2.8% | 82 | +2 | **84** | **CORE** | yes |
| 8 | NVIDIA Corporation | NVDA | -0.0% | -4.0% | -2.0% | 82 | +2 | **84** | **CORE** | yes |
| 9 | Applied Materials, Inc. | AMAT | -0.0% | -8.2% | -4.1% | 81 | +3 | **84** | **CORE** | yes |
| 10 | AXT Inc | AXT | -0.0% | -20.3% | -10.1% | 76 | +8 | **84** | **CORE** | yes |

## Final model + Price Timing — SHORT

| Rank | Company | OKX | 24h | 7d | 50/50 move | Base SHORT | Timing adj. | Final | Signal | Prev. SHORT? |
|---:|---|---|---:|---:|---:|---:|---:|---:|---|---|
| 1 | Rocket Lab Corporation | RKLB | -0.0% | -7.1% | -3.6% | 100 | -3 | **97** | **CORE** | yes |
| 2 | USA Rare Earth, Inc. | USAR | -0.0% | -16.9% | -8.4% | 100 | -7 | **93** | **CORE** | yes |
| 3 | Moderna, Inc. | MRNA | -0.0% | 6.7% | 3.3% | 80 | +3 | **83** | **CORE** | yes |
| 4 | IonQ, Inc. | IONQ | 0.0% | -7.5% | -3.8% | 85 | -3 | **82** | **CORE** | yes |
| 5 | Nebius Group N.V. | NBIS | 0.0% | -16.8% | -8.4% | 84 | -7 | **77** | **CORE** | yes |
| 6 | AST SpaceMobile, Inc. | ASTS | -0.0% | -12.2% | -6.1% | 80 | -5 | **75** | **CORE** | yes |
| 7 | Cerebras Systems Inc. | CBRS | 0.0% | -13.1% | -6.5% | 71 | -5 | **66** | **WATCH** | yes |
| 8 | Tesla, Inc. | TSLA | 0.0% | -1.4% | -0.7% | 59 | -1 | **58** | **WATCH** | yes |

## Combined model — LONG

Weighted score: **70% fundamental + 30% P/E trend**.

| Rank | Company | OKX | Fundamental LONG | P/E trend LONG | Combined | Signal |
|---:|---|---|---:|---:|---:|---|
| 1 | Sandisk Corporation | `SNDK` | 90 | 90 | **90** | **CORE** |
| 2 | Taiwan Semiconductor Manufactur | `TSM` | 90 | 85 | **88** | **CORE** |
| 3 | Marvell Technology, Inc. | `MRVL` | 77 | 100 | **84** | **CORE** |
| 4 | Advanced Micro Devices, Inc. | `AMD` | 77 | 100 | **84** | **CORE** |
| 5 | Applovin Corporation | `APP` | 83 | 80 | **82** | **CORE** |
| 6 | Credo Technology Group Holding  | `CRDO` | 75 | 100 | **82** | **CORE** |
| 7 | NVIDIA Corporation | `NVDA` | 75 | 100 | **82** | **CORE** |
| 8 | Broadcom Inc. | `AVGO` | 75 | 100 | **82** | **CORE** |
| 9 | Applied Materials, Inc. | `AMAT` | 77 | 91 | **81** | **CORE** |
| 10 | Robinhood Markets, Inc. | `HOOD` | 77 | 86 | **80** | **CORE** |

## Combined model — SHORT

Weighted score: **70% fundamental + 30% P/E trend**.

| Rank | Company | OKX | Fundamental SHORT | P/E trend SHORT | Combined | Signal |
|---:|---|---|---:|---:|---:|---|
| 1 | Rocket Lab Corporation | `RKLB` | 100 | 0 | **100** | **CORE** |
| 2 | USA Rare Earth, Inc. | `USAR` | 100 | 0 | **100** | **CORE** |
| 3 | IonQ, Inc. | `IONQ` | 85 | 0 | **85** | **CORE** |
| 4 | Nebius Group N.V. | `NBIS` | 84 | 0 | **84** | **WATCH** |
| 5 | Moderna, Inc. | `MRNA` | 80 | 0 | **80** | **WATCH** |
| 6 | AST SpaceMobile, Inc. | `ASTS` | 80 | 0 | **80** | **WATCH** |
| 7 | Cerebras Systems Inc. | `CBRS` | 71 | 0 | **71** | **WATCH** |
| 8 | Okta, Inc. | `OKTA` | 80 | 13 | **60** | **WATCH** |
| 9 | Tesla, Inc. | `TSLA` | 78 | 15 | **59** | **WATCH** |

## P/E Compression + Growth — LONG

| Rank | Company | OKX | Trail P/E | Fwd P/E | P/E change | EPS +1y | Rev +1y | Rev trend | LONG score | Signal |
|---:|---|---|---:|---:|---:|---:|---:|---|---:|---|
| 1 | Marvell Technology, Inc. | `MRVL` | 56.6 | 23.4 | -58.6% | 73.9% | 63.7% | accelerating | **100** | **CORE** |
| 2 | Advanced Micro Devices, Inc. | `AMD` | 123.4 | 29.7 | -75.9% | 110.7% | 76.3% | accelerating | **100** | **CORE** |
| 3 | Credo Technology Group Holding  | `CRDO` | 53.5 | 15.5 | -71.0% | 53.9% | 55.0% | decelerating | **100** | **CORE** |
| 4 | NVIDIA Corporation | `NVDA` | 26.1 | 13.0 | -50.3% | 70.9% | 68.2% | decelerating | **100** | **CORE** |
| 5 | Broadcom Inc. | `AVGO` | 41.2 | 17.1 | -58.5% | 66.9% | 64.4% | decelerating | **100** | **CORE** |
| 6 | AXT Inc | `AXT` | 104.8 | 20.1 | -80.8% | 125.3% | 115.8% | decelerating | **96** | **CORE** |
| 7 | Oracle Corporation | `ORCL` | 19.8 | 11.4 | -42.3% | 36.1% | 46.0% | accelerating | **95** | **CORE** |
| 8 | Coherent Corp. | `COHR` | 50.4 | 14.9 | -70.5% | 48.4% | 38.6% | decelerating | **95** | **CORE** |
| 9 | Arm Holdings plc | `ARM` | 208.8 | 66.2 | -68.3% | 36.9% | 36.5% | accelerating | **95** | **CORE** |
| 10 | Bloom Energy Corporation | `BE` | 129.7 | 40.2 | -69.0% | 63.0% | 56.4% | decelerating | **92** | **CORE** |

## P/E Expansion + Weakening — SHORT

| Rank | Company | OKX | Trail P/E | Fwd P/E | P/E change | EPS +1y | Rev +1y | Rev trend | SHORT score | Signal |
|---:|---|---|---:|---:|---:|---:|---:|---|---:|---|
| 1 | SOFTBANK GROUP CORP | `SOFTBANK` | 5.0 | 14.5 | 191.0% | -14.5% | 7.0% | decelerating | **86** | **CORE** |
| 2 | Hyperliquid Strategies Inc | `PURR` | 3.2 | 27.5 | 767.6% | 51.0% | 31.4% | decelerating | **55** | **WATCH** |
| 3 | Amazon.com, Inc. | `AMZN` | 20.3 | 23.0 | 13.3% | -16.7% | 14.6% | decelerating | **52** | **WATCH** |
| 4 | Alphabet Inc. | `GOOGL` | 14.6 | 18.1 | 23.6% | -24.3% | 27.0% | accelerating | **50** | **WATCH** |

## Top SHORT candidates

| Rank | Company | OKX market | SHORT score | Signal | P/S | EV/S | Op margin | Fwd P/E | Rev +1y | FCF yield |
|---:|---|---|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Rocket Lab Corporation | `RKLB-USDT-SWAP` | **100** | **CORE** | 45.2 | 39.5 | -24.6% | 946.8 | 38.7% | -0.7% |
| 2 | USA Rare Earth, Inc. | `USAR-USDT-SWAP` | **100** | **CORE** | 248.2 | 46.6 | -795.6% | 290.3 | 870.1% | -8.7% |
| 3 | IonQ, Inc. | `IONQ-USDT-SWAP` | **85** | **CORE** | 52.2 | 38.0 | -408.2% | -22.3 | 77.6% | -0.7% |
| 4 | Nebius Group N.V. | `NBIS-USDT-SWAP` | **84** | **WATCH** | 30.4 | 32.3 | -0.2% | -42.1 | 266.0% | -23.3% |
| 5 | Okta, Inc. | `OKTA-USDT-SWAP` | **80** | **CORE** | 10.8 | 10.1 | 13.3% | 43.3 | 10.1% | 3.1% |
| 6 | AST SpaceMobile, Inc. | `ASTS-USDT-SWAP` | **80** | **WATCH** | 125.4 | 107.1 | -544.6% | -25.6 | 264.2% | -12.4% |
| 7 | Moderna, Inc. | `MRNA-USDT-SWAP` | **80** | **WATCH** | 40.9 | 39.2 | -557.9% | -49.8 | 16.3% | 0.3% |
| 8 | Tesla, Inc. | `TSLA-USDT-SWAP` | **78** | **WATCH** | 15.2 | 14.9 | 5.4% | 184.6 | 13.5% | 0.3% |
| 9 | Cerebras Systems Inc. | `CBRS-USDT-SWAP` | **71** | **WATCH** | 34.1 | 24.7 | -265.0% | 76.5 | 233.1% | — |
| 10 | Circle Internet Group, Inc. | `CRCL-USDT-SWAP` | **33** | **WATCH** | 6.6 | 6.0 | 4.9% | 50.9 | 27.3% | 1.1% |

## Top LONG candidates

| Rank | Company | OKX market | LONG score | Signal | P/S | EV/S | Op margin | Fwd P/E | Rev +1y | FCF yield |
|---:|---|---|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Taiwan Semiconductor Manufactur | `TSM-USDT-SWAP` | **90** | **CORE** | 0.4 | 2.7 | 58.7% | 17.3 | 37.8% | 57.3% |
| 2 | Sandisk Corporation | `SNDK-USDT-SWAP` | **90** | **CORE** | 5.5 | 5.4 | 79.6% | 3.9 | 22.3% | 7.0% |
| 3 | Applovin Corporation | `APP-USDT-SWAP` | **83** | **CORE** | 12.1 | 12.1 | 77.7% | 12.3 | 24.9% | 3.9% |
| 4 | Corning Incorporated | `GLW-USDT-SWAP` | **77** | **WATCH** | 6.1 | 6.5 | 18.9% | 27.9 | 21.1% | 0.8% |
| 5 | Robinhood Markets, Inc. | `HOOD-USDT-SWAP` | **77** | **WATCH** | 15.2 | 14.7 | 48.1% | 25.1 | 29.2% | — |
| 6 | Applied Materials, Inc. | `AMAT-USDT-SWAP` | **77** | **WATCH** | 9.8 | 9.8 | 33.7% | 20.6 | 35.4% | 1.0% |
| 7 | Marvell Technology, Inc. | `MRVL-USDT-SWAP` | **77** | **WATCH** | 16.4 | 16.1 | 16.7% | 23.4 | 63.7% | 1.6% |
| 8 | Advanced Micro Devices, Inc. | `AMD-USDT-SWAP` | **77** | **WATCH** | 19.1 | 18.9 | 17.2% | 29.7 | 76.3% | 1.1% |
| 9 | Credo Technology Group Holding  | `CRDO-USDT-SWAP` | **75** | **WATCH** | 17.8 | 17.4 | 25.2% | 15.5 | 55.0% | 0.9% |
| 10 | Broadcom Inc. | `AVGO-USDT-SWAP` | **75** | **WATCH** | 17.8 | 18.2 | 54.3% | 17.1 | 64.4% | 1.9% |

## Analyst consensus (12-month price target) — most upside

| Rank | Company | OKX | Price | Analyst mean target | Gap | Analysts | Currency |
|---:|---|---|---:|---:|---:|---:|---|
| 1 | Cerebras Systems Inc. | `CBRS` | 97.82 | 275.27 | **181.4%** | 11 | USD |
| 2 | CoreWeave, Inc. | `CRWV` | 53.74 | 133.00 | **147.5%** | 38 | USD |
| 3 | Applied Optoelectronics, Inc. | `AAOI` | 63.97 | 156.00 | **143.9%** | 5 | USD |
| 4 | SK hynix | `SKHYNIX` | 1396000.00 | 3157408.80 | **126.2%** | 39 | KRW |
| 5 | BitMine Immersion Technologies, | `BMNR` | 20.53 | 45.87 | **123.4%** | 3 | USD |
| 6 | Hyperliquid Strategies Inc | `PURR` | 10.16 | 22.32 | **119.7%** | 4 | USD |
| 7 | SamsungElec | `SAMSUNG` | 218000.00 | 478771.44 | **119.6%** | 35 | KRW |
| 8 | IonQ, Inc. | `IONQ` | 29.99 | 62.27 | **107.7%** | 14 | USD |
| 9 | AST SpaceMobile, Inc. | `ASTS` | 37.15 | 74.68 | **101.0%** | 12 | USD |
| 10 | Credo Technology Group Holding  | `CRDO` | 150.91 | 284.05 | **88.2%** | 19 | USD |
| 11 | Rocket Lab Corporation | `RKLB` | 54.43 | 102.15 | **87.7%** | 20 | USD |
| 12 | Marvell Technology, Inc. | `MRVL` | 171.97 | 321.87 | **87.2%** | 41 | USD |
| 13 | Coherent Corp. | `COHR` | 207.49 | 387.80 | **86.9%** | 25 | USD |
| 14 | Nebius Group N.V. | `NBIS` | 151.64 | 281.00 | **85.3%** | 20 | USD |
| 15 | Oracle Corporation | `ORCL` | 126.19 | 233.34 | **84.9%** | 38 | USD |

## Analyst consensus (12-month price target) — most downside

| Rank | Company | OKX | Price | Analyst mean target | Gap | Analysts | Currency |
|---:|---|---|---:|---:|---:|---:|---|
| 1 | Moderna, Inc. | `MRNA` | 228.44 | 138.37 | **-39.4%** | 19 | USD |

Price/target uses the underlying Yahoo Finance share quote, not the OKX derivative. Minimum 3 analysts; unreliable price scales and missing coverage excluded. Targets are analyst opinions, not guaranteed forecasts.

## All OKX companies — our ratio + LONG/SHORT scores

| Company | OKX | P/S | EV/S | Op margin | Fwd P/E | EPS +1y | Rev +1y | FCF yield | LONG | SHORT |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Rocket Lab Corporation | `RKLB` | 45.2 | 39.5 | -24.6% | 946.8 | 66.8% | 38.7% | -0.7% | **0** | **100 CORE** |
| USA Rare Earth, Inc. | `USAR` | 248.2 | 46.6 | -795.6% | 290.3 | 105.3% | 870.1% | -8.7% | **0** | **100 CORE** |
| Sandisk Corporation | `SNDK` | 5.5 | 5.4 | 79.6% | 3.9 | 26.1% | 22.3% | 7.0% | **90 CORE** | **10** |
| Taiwan Semiconductor Manufactur | `TSM` | 0.4 | 2.7 | 58.7% | 17.3 | 34.0% | 37.8% | 57.3% | **90 CORE** | **10** |
| IonQ, Inc. | `IONQ` | 52.2 | 38.0 | -408.2% | -22.3 | 23.1% | 77.6% | -0.7% | **0** | **85 CORE** |
| Nebius Group N.V. | `NBIS` | 30.4 | 32.3 | -0.2% | -42.1 | -191.4% | 266.0% | -23.3% | **0** | **84 WATCH** |
| Applovin Corporation | `APP` | 12.1 | 12.1 | 77.7% | 12.3 | 25.7% | 24.9% | 3.9% | **83 CORE** | **10** |
| Okta, Inc. | `OKTA` | 10.8 | 10.1 | 13.3% | 43.3 | 11.4% | 10.1% | 3.1% | **8** | **80 CORE** |
| Moderna, Inc. | `MRNA` | 40.9 | 39.2 | -557.9% | -49.8 | 42.3% | 16.3% | 0.3% | **0** | **80 WATCH** |
| AST SpaceMobile, Inc. | `ASTS` | 125.4 | 107.1 | -544.6% | -25.6 | 44.3% | 264.2% | -12.4% | **0** | **80 WATCH** |
| Tesla, Inc. | `TSLA` | 15.2 | 14.9 | 5.4% | 184.6 | 24.2% | 13.5% | 0.3% | **12** | **78 WATCH** |
| Marvell Technology, Inc. | `MRVL` | 16.4 | 16.1 | 16.7% | 23.4 | 73.9% | 63.7% | 1.6% | **77 WATCH** | **13** |
| Advanced Micro Devices, Inc. | `AMD` | 19.1 | 18.9 | 17.2% | 29.7 | 110.7% | 76.3% | 1.1% | **77 WATCH** | **13** |
| Applied Materials, Inc. | `AMAT` | 9.8 | 9.8 | 33.7% | 20.6 | 45.0% | 35.4% | 1.0% | **77 WATCH** | **3** |
| Robinhood Markets, Inc. | `HOOD` | 15.2 | 14.7 | 48.1% | 25.1 | 39.6% | 29.2% | — | **77 WATCH** | **0** |
| Corning Incorporated | `GLW` | 6.1 | 6.5 | 18.9% | 27.9 | 34.1% | 21.1% | 0.8% | **77 WATCH** | **13** |
| Credo Technology Group Holding  | `CRDO` | 17.8 | 17.4 | 25.2% | 15.5 | 53.9% | 55.0% | 0.9% | **75 WATCH** | **28** |
| NVIDIA Corporation | `NVDA` | 16.5 | 16.4 | 66.2% | 13.0 | 70.9% | 68.2% | 0.8% | **75 WATCH** | **18** |
| Broadcom Inc. | `AVGO` | 17.8 | 18.2 | 54.3% | 17.1 | 66.9% | 64.4% | 1.9% | **75 WATCH** | **28** |
| Micron Technology, Inc. | `MU` | 7.3 | 7.0 | 80.7% | 4.1 | 17.7% | 16.2% | 3.0% | **75 CORE** | **30** |
| Western Digital Corporation | `WDC` | 9.0 | 9.0 | 47.7% | 8.6 | 63.4% | 40.5% | 2.1% | **75 WATCH** | **18** |
| Cerebras Systems Inc. | `CBRS` | 34.1 | 24.7 | -265.0% | 76.5 | 372.9% | 233.1% | — | **0** | **71 WATCH** |
| Oracle Corporation | `ORCL` | 5.3 | 7.2 | 35.6% | 11.4 | 36.1% | 46.0% | -12.0% | **70 WATCH** | **10** |
| XIAOMI-W | `XIAOMI` | 1.7 | 1.5 | 4.0% | 19.3 | 37.8% | 19.8% | -1.2% | **70 WATCH** | **10** |
| AXT Inc | `AXT` | 19.7 | 17.3 | 38.7% | 20.1 | 125.3% | 115.8% | — | **67 WATCH** | **20** |
| Dell Technologies Inc. | `DELL` | 1.7 | 1.9 | 12.0% | 13.5 | 16.2% | 19.5% | 2.3% | **67 WATCH** | **38** |
| Adobe Inc. | `ADBE` | 3.7 | 3.7 | 34.8% | 9.0 | 12.1% | 9.1% | 9.8% | **65 WATCH** | **30** |
| Coherent Corp. | `COHR` | 5.7 | 6.0 | 11.8% | 14.9 | 48.4% | 38.6% | -1.6% | **60 WATCH** | **35** |
| Microsoft Corporation | `MSFT` | 11.2 | 11.4 | 49.8% | 21.5 | 20.9% | 20.2% | 0.1% | **59 WATCH** | **3** |
| Coca-Cola Company (The) | `KO` | 8.0 | 8.5 | 33.4% | 26.9 | 5.6% | -3.1% | 1.1% | **0** | **58** |
| Meta Platforms, Inc. | `META` | 6.6 | 6.7 | 35.4% | 17.5 | 16.5% | 21.6% | 1.1% | **57 WATCH** | **38** |
| Bloom Energy Corporation | `BE` | 16.5 | 16.6 | 18.5% | 40.2 | 63.0% | 56.4% | -0.0% | **40** | **55** |
| Super Micro Computer, Inc. | `SMCI` | 0.5 | 0.7 | 13.4% | 5.4 | 19.6% | 16.2% | -40.0% | **52** | **45** |
| Netflix, Inc. | `NFLX` | 5.3 | 5.4 | 34.6% | 16.8 | 5.1% | 10.7% | 9.6% | **35** | **50** |
| IREN LIMITED | `IREN` | 14.0 | 16.4 | -102.5% | -6.1 | -16.4% | 164.0% | -42.6% | **0** | **50** |
| Palantir Technologies Inc. | `PLTR` | 68.5 | 68.1 | 47.1% | 70.7 | 45.3% | 51.9% | 0.5% | **33** | **48** |
| SamsungElec | `SAMSUNG` | 2.4 | 2.1 | 55.0% | 2.9 | 64.7% | 40.1% | 5.9% | **45** | **10** |
| Amazon.com, Inc. | `AMZN` | 3.4 | 3.6 | 13.9% | 23.0 | -16.7% | 14.6% | -1.3% | **0** | **45** |
| Arm Holdings plc | `ARM` | 41.9 | 41.3 | 7.6% | 66.2 | 36.9% | 36.5% | 0.6% | **43** | **33** |
| Coinbase Global, Inc. | `COIN` | 7.1 | 6.7 | -1.4% | 58.9 | 785.9% | 26.4% | 9.6% | **20** | **40** |
| Lumentum Holdings Inc. | `LITE` | 16.5 | 16.3 | 28.0% | 17.4 | 52.9% | 48.9% | — | **10** | **40** |
| SOFTBANK GROUP CORP | `SOFTBANK` | 3.0 | 6.5 | -11.6% | 14.5 | -14.5% | 7.0% | -9.0% | **0** | **40** |
| CoreWeave, Inc. | `CRWV` | 3.9 | 10.0 | -1.9% | -27.3 | 9.7% | 105.6% | -30.7% | **0** | **40** |
| Apple Inc. | `AAPL` | 10.4 | 10.6 | 32.6% | 31.2 | 19.9% | 8.7% | 2.2% | **25** | **38** |
| Circle Internet Group, Inc. | `CRCL` | 6.6 | 6.0 | 4.9% | 50.9 | 24.9% | 27.3% | 1.1% | **27** | **33 WATCH** |
| SK hynix | `SKHYNIX` | 3.7 | 3.4 | 79.7% | 2.6 | 47.4% | 58.8% | — | **30** | **5** |
| SK hynix | `SKHY` | 3.7 | 3.4 | 79.7% | 2.6 | 47.4% | 58.8% | — | **30** | **5** |
| Alphabet Inc. | `GOOGL` | 7.3 | 7.1 | 31.8% | 18.1 | -24.3% | 27.0% | -0.0% | **5** | **30** |
| Intel Corporation | `INTC` | 5.4 | 5.6 | 15.6% | 33.7 | 21.1% | 12.0% | 0.3% | **5** | **28** |
| Fluence Energy, Inc. | `FLNC` | 0.4 | 0.3 | -8.9% | -10.4 | 59.3% | 25.4% | 0.2% | **5** | **28** |
| Hyperliquid Strategies Inc | `PURR` | 298.9 | 197.9 | 9595.1% | 27.5 | 51.0% | 31.4% | — | **25** | **10** |
| Strategy Inc | `MSTR` | 116.0 | 143.7 | 16670.9% | 8.2 | 481.5% | 3.3% | — | **25** | **10** |
| BitMine Immersion Technologies, | `BMNR` | 202.4 | 196.8 | 8.4% | 21.8 | 103.2% | 421.8% | -4.2% | **25** | **25** |
| QUALCOMM Incorporated | `QCOM` | 4.0 | 4.1 | 18.5% | 16.2 | -3.5% | 4.5% | 5.8% | **25** | **15** |
| Applied Optoelectronics, Inc. | `AAOI` | 9.1 | 8.7 | -12.9% | 13.9 | 576.8% | 156.5% | -16.3% | **10** | **25** |

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
