# OKX Long / Short Fundamental Scanner

Hourly scanner restricted to public companies exposed by the **OKX EEA TradFi / Stock Perpetual API universe**.

**Last scan:** 2026-11-28 03:58 UTC  
**Availability scope:** user-confirmed OKX EEA Stock Futures / X-Perp  
**OKX stock/ETF markets in configured universe:** 72  
**Public companies analysed:** 55  
**SHORT CORE:** 2  
**LONG CORE:** 6

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
| 1 | Sandisk Corporation | SNDK | -9.6% | -9.6% | -9.6% | 90 | +8 | **98** | **CORE** | yes |
| 2 | Taiwan Semiconductor Manufactur | TSM | 3.2% | 10.9% | 7.0% | 88 | -6 | **82** | **CORE** | yes |
| 3 | Advanced Micro Devices, Inc. | AMD | 4.6% | 0.0% | 2.3% | 84 | -2 | **82** | **CORE** | yes |
| 4 | Marvell Technology, Inc. | MRVL | 7.3% | 14.9% | 11.1% | 90 | -9 | **81** | **CORE** | yes |
| 5 | Robinhood Markets, Inc. | HOOD | 3.3% | 9.2% | 6.3% | 86 | -5 | **81** | **CORE** | yes |
| 6 | Broadcom Inc. | AVGO | 3.8% | 2.6% | 3.2% | 82 | -3 | **79** | **CORE** | yes |
| 7 | NVIDIA Corporation | NVDA | 0.8% | 19.9% | 10.3% | 85 | -8 | **77** | **CORE** | yes |
| 8 | QUALCOMM Incorporated | QCOM | 6.3% | 19.6% | 12.9% | 85 | -10 | **75** | **CORE** | yes |
| 9 | Corning Incorporated | GLW | 4.8% | 11.3% | 8.1% | 80 | -6 | **74** | **WATCH** | yes |
| 10 | Oracle Corporation | ORCL | 3.1% | 5.9% | 4.5% | 78 | -4 | **74** | **WATCH** | yes |

## Final model + Price Timing — SHORT

| Rank | Company | OKX | 24h | 7d | 50/50 move | Base SHORT | Timing adj. | Final | Signal | Prev. SHORT? |
|---:|---|---|---:|---:|---:|---:|---:|---:|---|---|
| 1 | Rocket Lab Corporation | RKLB | 8.2% | 12.0% | 10.1% | 100 | +8 | **100** | **CORE** | yes |
| 2 | Moderna, Inc. | MRNA | 3.5% | 17.3% | 10.4% | 94 | +8 | **100** | **CORE** | yes |
| 3 | USA Rare Earth, Inc. | USAR | 1.7% | 6.9% | 4.3% | 86 | +3 | **89** | **CORE** | yes |
| 4 | AST SpaceMobile, Inc. | ASTS | 3.2% | 15.4% | 9.3% | 80 | +7 | **87** | **CORE** | yes |
| 5 | IonQ, Inc. | IONQ | 6.1% | 20.5% | 13.3% | 75 | +11 | **86** | **CORE** | yes |
| 6 | Cerebras Systems Inc. | CBRS | 5.1% | 14.0% | 9.5% | 71 | +8 | **79** | **CORE** | yes |
| 7 | Tesla, Inc. | TSLA | 5.2% | 15.7% | 10.4% | 59 | +8 | **67** | **WATCH** | yes |
| 8 | Okta, Inc. | OKTA | 2.8% | 8.4% | 5.6% | 60 | +4 | **64** | **WATCH** | yes |
| 9 | IREN LIMITED | IREN | 5.9% | 15.1% | 10.5% | 55 | +8 | **63** | **WATCH** | yes |

## Combined model — LONG

Weighted score: **70% fundamental + 30% P/E trend**.

| Rank | Company | OKX | Fundamental LONG | P/E trend LONG | Combined | Signal |
|---:|---|---|---:|---:|---:|---|
| 1 | Sandisk Corporation | `SNDK` | 90 | 90 | **90** | **CORE** |
| 2 | Marvell Technology, Inc. | `MRVL` | 85 | 100 | **90** | **CORE** |
| 3 | Taiwan Semiconductor Manufactur | `TSM` | 90 | 85 | **88** | **CORE** |
| 4 | Robinhood Markets, Inc. | `HOOD` | 85 | 90 | **86** | **CORE** |
| 5 | QUALCOMM Incorporated | `QCOM` | 100 | 50 | **85** | **CORE** |
| 6 | NVIDIA Corporation | `NVDA` | 83 | 90 | **85** | **CORE** |
| 7 | Advanced Micro Devices, Inc. | `AMD` | 77 | 100 | **84** | **CORE** |
| 8 | Broadcom Inc. | `AVGO` | 75 | 100 | **82** | **CORE** |
| 9 | Credo Technology Group Holding  | `CRDO` | 75 | 100 | **82** | **CORE** |
| 10 | AXT Inc | `AXT` | 75 | 100 | **82** | **CORE** |

## Combined model — SHORT

Weighted score: **70% fundamental + 30% P/E trend**.

| Rank | Company | OKX | Fundamental SHORT | P/E trend SHORT | Combined | Signal |
|---:|---|---|---:|---:|---:|---|
| 1 | Rocket Lab Corporation | `RKLB` | 100 | 0 | **100** | **WATCH** |
| 2 | Moderna, Inc. | `MRNA` | 94 | 0 | **94** | **WATCH** |
| 3 | USA Rare Earth, Inc. | `USAR` | 86 | 0 | **86** | **CORE** |
| 4 | AST SpaceMobile, Inc. | `ASTS` | 80 | 0 | **80** | **WATCH** |
| 5 | IonQ, Inc. | `IONQ` | 75 | 0 | **75** | **WATCH** |
| 6 | Cerebras Systems Inc. | `CBRS` | 71 | 0 | **71** | **WATCH** |
| 7 | Okta, Inc. | `OKTA` | 80 | 13 | **60** | **WATCH** |
| 8 | Tesla, Inc. | `TSLA` | 78 | 15 | **59** | **WATCH** |

## P/E Compression + Growth — LONG

| Rank | Company | OKX | Trail P/E | Fwd P/E | P/E change | EPS +1y | Rev +1y | Rev trend | LONG score | Signal |
|---:|---|---|---:|---:|---:|---:|---:|---|---:|---|
| 1 | Advanced Micro Devices, Inc. | `AMD` | 90.7 | 24.1 | -73.4% | 117.7% | 83.3% | accelerating | **100** | **CORE** |
| 2 | Marvell Technology, Inc. | `MRVL` | 46.2 | 19.1 | -58.8% | 75.3% | 64.2% | accelerating | **100** | **CORE** |
| 3 | Broadcom Inc. | `AVGO` | 39.9 | 16.2 | -59.5% | 65.8% | 64.9% | decelerating | **100** | **CORE** |
| 4 | Credo Technology Group Holding  | `CRDO` | 41.0 | 11.9 | -71.0% | 53.9% | 55.0% | decelerating | **100** | **CORE** |
| 5 | AXT Inc | `AXT` | 74.2 | 14.3 | -80.8% | 116.3% | 111.5% | decelerating | **100** | **CORE** |
| 6 | Coherent Corp. | `COHR` | 46.3 | 14.2 | -69.3% | 51.8% | 38.8% | decelerating | **100** | **CORE** |
| 7 | Bloom Energy Corporation | `BE` | 98.8 | 30.4 | -69.2% | 63.8% | 58.8% | decelerating | **96** | **CORE** |
| 8 | Oracle Corporation | `ORCL` | 16.8 | 9.7 | -42.3% | 35.7% | 45.7% | accelerating | **95** | **CORE** |
| 9 | Arm Holdings plc | `ARM` | 197.2 | 55.6 | -71.8% | 36.5% | 37.3% | accelerating | **95** | **CORE** |
| 10 | Sandisk Corporation | `SNDK` | 5.5 | 2.4 | -56.3% | 25.7% | 23.4% | decelerating | **90** | **CORE** |

## P/E Expansion + Weakening — SHORT

| Rank | Company | OKX | Trail P/E | Fwd P/E | P/E change | EPS +1y | Rev +1y | Rev trend | SHORT score | Signal |
|---:|---|---|---:|---:|---:|---:|---:|---|---:|---|
| 1 | Hyperliquid Strategies Inc | `PURR` | 3.3 | 38.0 | 1051.2% | -79.8% | 22.8% | decelerating | **80** | **CORE** |
| 2 | Alphabet Inc. | `GOOGL` | 14.4 | 18.0 | 25.2% | -23.8% | 27.4% | accelerating | **50** | **WATCH** |

## Top SHORT candidates

| Rank | Company | OKX market | SHORT score | Signal | P/S | EV/S | Op margin | Fwd P/E | Rev +1y | FCF yield |
|---:|---|---|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Rocket Lab Corporation | `RKLB-USDT-SWAP` | **100** | **WATCH** | 38.8 | 31.4 | -27.6% | 710.8 | 36.5% | -0.6% |
| 2 | Moderna, Inc. | `MRNA-USDT-SWAP` | **94** | **WATCH** | 36.6 | 36.3 | -80.8% | -54.6 | 11.3% | -0.6% |
| 3 | USA Rare Earth, Inc. | `USAR-USDT-SWAP` | **86** | **CORE** | 155.7 | 129.7 | -984.3% | 28.5 | 872.0% | -10.2% |
| 4 | Okta, Inc. | `OKTA-USDT-SWAP` | **80** | **CORE** | 11.8 | 11.1 | 7.7% | 47.4 | 10.1% | 2.9% |
| 5 | AST SpaceMobile, Inc. | `ASTS-USDT-SWAP` | **80** | **WATCH** | 75.3 | 68.8 | -393.3% | -19.7 | 241.4% | -17.6% |
| 6 | IonQ, Inc. | `IONQ-USDT-SWAP` | **75** | **WATCH** | 30.4 | 26.1 | -306.3% | -17.6 | 71.2% | -1.0% |
| 7 | Cerebras Systems Inc. | `CBRS-USDT-SWAP` | **71** | **WATCH** | 30.3 | 22.5 | -99.3% | 50.7 | 214.4% | — |

## Top LONG candidates

| Rank | Company | OKX market | LONG score | Signal | P/S | EV/S | Op margin | Fwd P/E | Rev +1y | FCF yield |
|---:|---|---|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | QUALCOMM Incorporated | `QCOM-USDT-SWAP` | **100** | **CORE** | 4.4 | 4.6 | 20.8% | 14.7 | 15.4% | 4.7% |
| 2 | Taiwan Semiconductor Manufactur | `TSM-USDT-SWAP` | **90** | **CORE** | 0.4 | 2.4 | 58.0% | 15.1 | 38.1% | 56.9% |
| 3 | Sandisk Corporation | `SNDK-USDT-SWAP` | **90** | **CORE** | 3.4 | 3.2 | 72.7% | 2.4 | 23.4% | 11.6% |
| 4 | Robinhood Markets, Inc. | `HOOD-USDT-SWAP` | **85** | **WATCH** | 12.0 | 11.6 | 45.7% | 19.9 | 29.4% | — |
| 5 | Marvell Technology, Inc. | `MRVL-USDT-SWAP` | **85** | **WATCH** | 13.4 | 13.2 | 16.8% | 19.1 | 64.2% | 1.9% |
| 6 | Applovin Corporation | `APP-USDT-SWAP` | **83** | **CORE** | 17.4 | 17.4 | 77.8% | 19.1 | 25.7% | 2.8% |
| 7 | NVIDIA Corporation | `NVDA-USDT-SWAP` | **83** | **CORE** | 10.0 | 9.9 | 66.1% | 9.1 | 71.4% | 2.7% |
| 8 | Corning Incorporated | `GLW-USDT-SWAP` | **77** | **WATCH** | 5.1 | 5.5 | 16.8% | 23.1 | 21.2% | 1.0% |
| 9 | Advanced Micro Devices, Inc. | `AMD-USDT-SWAP` | **77** | **WATCH** | 15.5 | 15.2 | 17.8% | 24.1 | 83.3% | 1.0% |
| 10 | Applied Materials, Inc. | `AMAT-USDT-SWAP` | **75** | **WATCH** | 7.4 | 7.3 | 32.9% | 13.0 | 21.2% | 1.0% |

## Analyst consensus (12-month price target) — most upside

| Rank | Company | OKX | Price | Analyst mean target | Gap | Analysts | Currency |
|---:|---|---|---:|---:|---:|---:|---|
| 1 | Hyperliquid Strategies Inc | `PURR` | 7.80 | 22.50 | **188.5%** | 4 | USD |
| 2 | Sandisk Corporation | `SNDK` | 85.36 | 244.96 | **187.0%** | 24 | USD |
| 3 | Strategy Inc | `MSTR` | 81.62 | 233.27 | **185.8%** | 15 | USD |
| 4 | Applied Optoelectronics, Inc. | `AAOI` | 40.90 | 109.00 | **166.5%** | 5 | USD |
| 5 | SK hynix | `SKHYNIX` | 1110000.00 | 2957152.20 | **166.4%** | 39 | KRW |
| 6 | CoreWeave, Inc. | `CRWV` | 44.15 | 114.45 | **159.2%** | 38 | USD |
| 7 | Nebius Group N.V. | `NBIS` | 89.46 | 231.60 | **158.9%** | 20 | USD |
| 8 | SamsungElec | `SAMSUNG` | 179100.00 | 455166.66 | **154.1%** | 36 | KRW |
| 9 | Micron Technology, Inc. | `MU` | 646.95 | 1529.69 | **136.4%** | 45 | USD |
| 10 | Credo Technology Group Holding  | `CRDO` | 115.57 | 269.05 | **132.8%** | 19 | USD |
| 11 | AXT Inc | `AXT` | 36.37 | 82.77 | **127.6%** | 7 | USD |
| 12 | SOFTBANK GROUP CORP | `SOFTBANK` | 2984.50 | 6667.36 | **123.4%** | 18 | JPY |
| 13 | Cerebras Systems Inc. | `CBRS` | 94.24 | 210.18 | **123.0%** | 11 | USD |
| 14 | Oracle Corporation | `ORCL` | 107.13 | 236.18 | **120.5%** | 40 | USD |
| 15 | IonQ, Inc. | `IONQ` | 24.97 | 54.27 | **117.4%** | 14 | USD |

## Analyst consensus (12-month price target) — most downside

| Rank | Company | OKX | Price | Analyst mean target | Gap | Analysts | Currency |
|---:|---|---|---:|---:|---:|---:|---|
| 1 | Moderna, Inc. | `MRNA` | 228.64 | 163.74 | **-28.4%** | 19 | USD |
| 2 | Apple Inc. | `AAPL` | 358.54 | 345.63 | **-3.6%** | 39 | USD |

Price/target uses the underlying Yahoo Finance share quote, not the OKX derivative. Minimum 3 analysts; unreliable price scales and missing coverage excluded. Targets are analyst opinions, not guaranteed forecasts.

## All OKX companies — our ratio + LONG/SHORT scores

| Company | OKX | P/S | EV/S | Op margin | Fwd P/E | EPS +1y | Rev +1y | FCF yield | LONG | SHORT |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| QUALCOMM Incorporated | `QCOM` | 4.4 | 4.6 | 20.8% | 14.7 | 26.6% | 15.4% | 4.7% | **100 CORE** | **0** |
| Rocket Lab Corporation | `RKLB` | 38.8 | 31.4 | -27.6% | 710.8 | 77.8% | 36.5% | -0.6% | **0** | **100 WATCH** |
| Moderna, Inc. | `MRNA` | 36.6 | 36.3 | -80.8% | -54.6 | 39.0% | 11.3% | -0.6% | **0** | **94 WATCH** |
| Sandisk Corporation | `SNDK` | 3.4 | 3.2 | 72.7% | 2.4 | 25.7% | 23.4% | 11.6% | **90 CORE** | **10** |
| Taiwan Semiconductor Manufactur | `TSM` | 0.4 | 2.4 | 58.0% | 15.1 | 33.8% | 38.1% | 56.9% | **90 CORE** | **10** |
| USA Rare Earth, Inc. | `USAR` | 155.7 | 129.7 | -984.3% | 28.5 | 77.7% | 872.0% | -10.2% | **0** | **86 CORE** |
| Robinhood Markets, Inc. | `HOOD` | 12.0 | 11.6 | 45.7% | 19.9 | 39.9% | 29.4% | — | **85 WATCH** | **0** |
| Marvell Technology, Inc. | `MRVL` | 13.4 | 13.2 | 16.8% | 19.1 | 75.3% | 64.2% | 1.9% | **85 WATCH** | **13** |
| NVIDIA Corporation | `NVDA` | 10.0 | 9.9 | 66.1% | 9.1 | 71.7% | 71.4% | 2.7% | **83 CORE** | **10** |
| Applovin Corporation | `APP` | 17.4 | 17.4 | 77.8% | 19.1 | 27.6% | 25.7% | 2.8% | **83 CORE** | **10** |
| Okta, Inc. | `OKTA` | 11.8 | 11.1 | 7.7% | 47.4 | 11.5% | 10.1% | 2.9% | **8** | **80 CORE** |
| AST SpaceMobile, Inc. | `ASTS` | 75.3 | 68.8 | -393.3% | -19.7 | 24.2% | 241.4% | -17.6% | **0** | **80 WATCH** |
| Tesla, Inc. | `TSLA` | 15.3 | 15.0 | 3.4% | 184.9 | 25.2% | 13.4% | 0.3% | **20** | **78** |
| Advanced Micro Devices, Inc. | `AMD` | 15.5 | 15.2 | 17.8% | 24.1 | 117.7% | 83.3% | 1.0% | **77 WATCH** | **13** |
| Corning Incorporated | `GLW` | 5.1 | 5.5 | 16.8% | 23.1 | 34.8% | 21.2% | 1.0% | **77 WATCH** | **13** |
| Broadcom Inc. | `AVGO` | 16.7 | 17.1 | 48.8% | 16.2 | 65.8% | 64.9% | 2.1% | **75 WATCH** | **18** |
| Credo Technology Group Holding  | `CRDO` | 13.7 | 13.2 | 31.7% | 11.9 | 53.9% | 55.0% | 1.1% | **75 WATCH** | **28** |
| Applied Materials, Inc. | `AMAT` | 7.4 | 7.3 | 32.9% | 13.0 | 28.5% | 21.2% | 1.0% | **75 WATCH** | **18** |
| AXT Inc | `AXT` | 14.0 | 11.6 | 19.6% | 14.3 | 116.3% | 111.5% | 0.8% | **75 WATCH** | **28** |
| Western Digital Corporation | `WDC` | 7.6 | 7.5 | 40.9% | 7.3 | 61.3% | 39.3% | 2.5% | **75 WATCH** | **18** |
| IonQ, Inc. | `IONQ` | 30.4 | 26.1 | -306.3% | -17.6 | -41.0% | 71.2% | -1.0% | **0** | **75 WATCH** |
| Cerebras Systems Inc. | `CBRS` | 30.3 | 22.5 | -99.3% | 50.7 | 543.0% | 214.4% | — | **0** | **71 WATCH** |
| Oracle Corporation | `ORCL` | 4.7 | 6.4 | 34.3% | 9.7 | 35.7% | 45.7% | -13.7% | **70 WATCH** | **10** |
| XIAOMI-W | `XIAOMI` | 1.7 | 1.5 | 3.3% | 19.1 | 39.3% | 15.8% | -5.0% | **70 WATCH** | **10** |
| Micron Technology, Inc. | `MU` | 5.5 | 5.2 | 74.6% | 3.2 | 17.1% | 14.9% | 4.0% | **70 CORE** | **30** |
| Microsoft Corporation | `MSFT` | 10.6 | 10.8 | 47.1% | 20.4 | 21.0% | 20.7% | 0.1% | **69 WATCH** | **3** |
| Adobe Inc. | `ADBE` | 3.5 | 3.6 | 36.3% | 8.6 | 12.0% | 9.1% | 10.2% | **65 WATCH** | **30** |
| Coherent Corp. | `COHR` | 5.6 | 5.9 | 14.1% | 14.2 | 51.8% | 38.8% | -3.8% | **60 WATCH** | **35** |
| Apple Inc. | `AAPL` | 10.9 | 11.0 | 33.0% | 33.9 | 12.4% | 8.1% | 2.0% | **5** | **58** |
| Coca-Cola Company (The) | `KO` | 8.2 | 8.8 | 32.2% | 27.6 | 5.5% | -3.0% | 1.0% | **0** | **58** |
| Meta Platforms, Inc. | `META` | 6.7 | 6.8 | 37.8% | 17.6 | 16.3% | 21.9% | 1.0% | **57 WATCH** | **38** |
| IREN LIMITED | `IREN` | 8.3 | 17.9 | -72.9% | 50.4 | 116.3% | 200.8% | — | **0** | **55** |
| Netflix, Inc. | `NFLX` | 5.0 | 5.2 | 31.3% | 16.2 | 5.4% | 10.7% | 10.2% | **35** | **50** |
| Fluence Energy, Inc. | `FLNC` | 0.4 | 0.4 | -14.8% | -9.8 | 86.7% | 24.3% | -47.4% | **0** | **50** |
| Palantir Technologies Inc. | `PLTR` | 56.9 | 55.5 | 45.6% | 67.7 | 49.3% | 54.1% | 0.6% | **45** | **48** |
| Bloom Energy Corporation | `BE` | 12.6 | 12.7 | 14.3% | 30.4 | 63.8% | 58.8% | -0.0% | **45** | **35** |
| SamsungElec | `SAMSUNG` | 2.0 | 1.6 | 46.1% | 2.3 | 62.9% | 41.0% | 10.1% | **45** | **10** |
| Super Micro Computer, Inc. | `SMCI` | 0.3 | 0.4 | 8.3% | 3.4 | 6.5% | 11.3% | -52.3% | **35** | **45** |
| Dell Technologies Inc. | `DELL` | 1.1 | 1.3 | 11.2% | 10.4 | 7.6% | 21.2% | -0.2% | **30** | **45** |
| Arm Holdings plc | `ARM` | 33.6 | 33.0 | 17.0% | 55.6 | 36.5% | 37.3% | 0.6% | **43** | **33** |
| Circle Internet Group, Inc. | `CRCL` | 4.2 | 3.6 | 11.3% | 34.8 | 3.6% | 24.2% | 2.1% | **20** | **43** |
| Nebius Group N.V. | `NBIS` | 12.0 | 15.9 | -18.7% | -29.4 | -1706.3% | 289.8% | -77.8% | **0** | **40** |
| CoreWeave, Inc. | `CRWV` | 2.5 | 8.8 | -0.5% | -24.8 | 24.0% | 106.9% | -80.0% | **0** | **40** |
| SOFTBANK GROUP CORP | `SOFTBANK` | 2.1 | 5.6 | -6.3% | 10.1 | 160.7% | 5.8% | -6.1% | **0** | **40** |
| Coinbase Global, Inc. | `COIN` | 5.2 | 4.9 | 0.1% | 42.0 | 1061.9% | 25.0% | 13.0% | **35** | **25** |
| SK hynix | `SKHYNIX` | 2.9 | 2.6 | 74.5% | 2.1 | 49.5% | 60.8% | — | **30** | **5** |
| Lumentum Holdings Inc. | `LITE` | 12.5 | 12.3 | 23.4% | 12.9 | 60.4% | 58.5% | 0.3% | **30** | **23** |
| SK hynix | `SKHY` | 2.9 | 2.6 | 74.5% | 2.1 | 49.5% | 60.8% | — | **30** | **5** |
| Alphabet Inc. | `GOOGL` | 7.2 | 7.0 | 33.3% | 18.0 | -23.8% | 27.4% | -0.0% | **5** | **30** |
| Amazon.com, Inc. | `AMZN` | 3.4 | 3.7 | 13.1% | 23.3 | -16.6% | 15.8% | -1.3% | **0** | **30** |
| Intel Corporation | `INTC` | 5.1 | 5.3 | 10.3% | 32.1 | 20.4% | 11.9% | 0.3% | **5** | **28** |
| Strategy Inc | `MSTR` | 70.1 | 97.8 | -1100.1% | 4.7 | 417.1% | 3.1% | -9.3% | **25** | **25** |
| BitMine Immersion Technologies, | `BMNR` | 69.7 | 67.5 | -216.3% | 14.8 | 105.7% | 197.6% | -1.2% | **25** | **25** |
| Applied Optoelectronics, Inc. | `AAOI` | 5.0 | 4.6 | -6.8% | 12.2 | 383.4% | 135.1% | -35.3% | **10** | **25** |
| Hyperliquid Strategies Inc | `PURR` | 100.0 | 87.8 | 6252.0% | 38.0 | -79.8% | 22.8% | — | **0** | **25** |

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
