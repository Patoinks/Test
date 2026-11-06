# OKX Long / Short Fundamental Scanner

Hourly scanner restricted to public companies exposed by the **OKX EEA TradFi / Stock Perpetual API universe**.

**Last scan:** 2026-11-06 02:32 UTC  
**Availability scope:** user-confirmed OKX EEA Stock Futures / X-Perp  
**OKX stock/ETF markets in configured universe:** 72  
**Public companies analysed:** 55  
**SHORT CORE:** 1  
**LONG CORE:** 7

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
| 1 | Sandisk Corporation | SNDK | -22.3% | -39.4% | -30.8% | 90 | +20 | **100** | **CORE** | yes |
| 2 | Marvell Technology, Inc. | MRVL | -16.4% | -38.8% | -27.6% | 90 | +20 | **100** | **CORE** | yes |
| 3 | Applied Materials, Inc. | AMAT | -13.6% | -24.3% | -18.9% | 88 | +15 | **100** | **CORE** | yes |
| 4 | Taiwan Semiconductor Manufactur | TSM | -10.8% | -18.2% | -14.5% | 88 | +12 | **100** | **CORE** | yes |
| 5 | Advanced Micro Devices, Inc. | AMD | -17.3% | -28.6% | -22.9% | 84 | +18 | **100** | **CORE** | yes |
| 6 | AXT Inc | AXT | -22.8% | -39.7% | -31.2% | 82 | +20 | **100** | **CORE** | yes |
| 7 | Western Digital Corporation | WDC | -17.4% | -32.3% | -24.8% | 82 | +20 | **100** | **CORE** | yes |
| 8 | Credo Technology Group Holding  | CRDO | -17.7% | -32.0% | -24.9% | 82 | +20 | **100** | **CORE** | yes |
| 9 | QUALCOMM Incorporated | QCOM | -9.5% | -15.5% | -12.5% | 89 | +10 | **99** | **CORE** | yes |
| 10 | Micron Technology, Inc. | MU | -17.5% | -29.7% | -23.6% | 77 | +19 | **96** | **CORE** | yes |

## Final model + Price Timing — SHORT

| Rank | Company | OKX | 24h | 7d | 50/50 move | Base SHORT | Timing adj. | Final | Signal | Prev. SHORT? |
|---:|---|---|---:|---:|---:|---:|---:|---:|---|---|
| 1 | Rocket Lab Corporation | RKLB | -12.2% | -22.2% | -17.2% | 100 | -14 | **86** | **CORE** | yes |
| 2 | USA Rare Earth, Inc. | USAR | -9.5% | -29.5% | -19.5% | 100 | -16 | **84** | **CORE** | yes |
| 3 | Moderna, Inc. | MRNA | -6.5% | 8.4% | 0.9% | 80 | +1 | **81** | **CORE** | yes |
| 4 | IonQ, Inc. | IONQ | -10.5% | -16.7% | -13.6% | 82 | -11 | **71** | **WATCH** | yes |
| 5 | AST SpaceMobile, Inc. | ASTS | -15.2% | -29.9% | -22.5% | 80 | -18 | **62** | **WATCH** | yes |

## Combined model — LONG

Weighted score: **70% fundamental + 30% P/E trend**.

| Rank | Company | OKX | Fundamental LONG | P/E trend LONG | Combined | Signal |
|---:|---|---|---:|---:|---:|---|
| 1 | Sandisk Corporation | `SNDK` | 90 | 90 | **90** | **CORE** |
| 2 | Marvell Technology, Inc. | `MRVL` | 85 | 100 | **90** | **CORE** |
| 3 | QUALCOMM Incorporated | `QCOM` | 100 | 62 | **89** | **CORE** |
| 4 | Taiwan Semiconductor Manufactur | `TSM` | 90 | 85 | **88** | **CORE** |
| 5 | Applied Materials, Inc. | `AMAT` | 85 | 95 | **88** | **CORE** |
| 6 | Advanced Micro Devices, Inc. | `AMD` | 77 | 100 | **84** | **CORE** |
| 7 | Western Digital Corporation | `WDC` | 83 | 80 | **82** | **CORE** |
| 8 | AXT Inc | `AXT` | 75 | 100 | **82** | **CORE** |
| 9 | Credo Technology Group Holding  | `CRDO` | 75 | 100 | **82** | **CORE** |
| 10 | NVIDIA Corporation | `NVDA` | 75 | 100 | **82** | **CORE** |

## Combined model — SHORT

Weighted score: **70% fundamental + 30% P/E trend**.

| Rank | Company | OKX | Fundamental SHORT | P/E trend SHORT | Combined | Signal |
|---:|---|---|---:|---:|---:|---|
| 1 | Rocket Lab Corporation | `RKLB` | 100 | 0 | **100** | **WATCH** |
| 2 | USA Rare Earth, Inc. | `USAR` | 100 | 0 | **100** | **CORE** |
| 3 | IonQ, Inc. | `IONQ` | 82 | 0 | **82** | **WATCH** |
| 4 | Moderna, Inc. | `MRNA` | 80 | 0 | **80** | **WATCH** |
| 5 | AST SpaceMobile, Inc. | `ASTS` | 80 | 0 | **80** | **WATCH** |
| 6 | Nebius Group N.V. | `NBIS` | 72 | 0 | **72** | **WATCH** |
| 7 | Tesla, Inc. | `TSLA` | 78 | 15 | **59** | **WATCH** |

## P/E Compression + Growth — LONG

| Rank | Company | OKX | Trail P/E | Fwd P/E | P/E change | EPS +1y | Rev +1y | Rev trend | LONG score | Signal |
|---:|---|---|---:|---:|---:|---:|---:|---|---:|---|
| 1 | Advanced Micro Devices, Inc. | `AMD` | 86.4 | 24.8 | -71.3% | 102.2% | 77.4% | accelerating | **100** | **CORE** |
| 2 | AXT Inc | `AXT` | 74.9 | 14.4 | -80.8% | 116.3% | 115.9% | decelerating | **100** | **CORE** |
| 3 | Credo Technology Group Holding  | `CRDO` | 39.8 | 11.6 | -71.0% | 53.9% | 55.0% | decelerating | **100** | **CORE** |
| 4 | Marvell Technology, Inc. | `MRVL` | 43.9 | 18.2 | -58.6% | 73.9% | 63.7% | accelerating | **100** | **CORE** |
| 5 | NVIDIA Corporation | `NVDA` | 23.0 | 11.4 | -50.3% | 70.9% | 68.2% | decelerating | **100** | **CORE** |
| 6 | Broadcom Inc. | `AVGO` | 37.2 | 15.0 | -59.8% | 66.9% | 64.4% | decelerating | **100** | **CORE** |
| 7 | Bloom Energy Corporation | `BE` | 101.5 | 31.5 | -69.0% | 62.7% | 56.4% | decelerating | **96** | **CORE** |
| 8 | Applied Materials, Inc. | `AMAT` | 27.5 | 17.2 | -37.5% | 45.0% | 35.4% | accelerating | **95** | **CORE** |
| 9 | Oracle Corporation | `ORCL` | 18.1 | 10.4 | -42.3% | 35.8% | 45.7% | accelerating | **95** | **CORE** |
| 10 | Coherent Corp. | `COHR` | 35.1 | 12.2 | -65.4% | 48.4% | 38.6% | decelerating | **95** | **CORE** |

## P/E Expansion + Weakening — SHORT

| Rank | Company | OKX | Trail P/E | Fwd P/E | P/E change | EPS +1y | Rev +1y | Rev trend | SHORT score | Signal |
|---:|---|---|---:|---:|---:|---:|---:|---|---:|---|
| 1 | SOFTBANK GROUP CORP | `SOFTBANK` | 4.5 | 12.2 | 171.3% | -14.5% | 7.0% | decelerating | **86** | **CORE** |
| 2 | Hyperliquid Strategies Inc | `PURR` | 2.7 | 23.7 | 767.6% | 51.0% | 31.4% | decelerating | **55** | **WATCH** |
| 3 | Amazon.com, Inc. | `AMZN` | 21.0 | 23.8 | 13.3% | -16.7% | 15.6% | decelerating | **52** | **WATCH** |
| 4 | Alphabet Inc. | `GOOGL` | 14.8 | 18.2 | 23.6% | -24.1% | 27.0% | accelerating | **50** | **WATCH** |

## Top SHORT candidates

| Rank | Company | OKX market | SHORT score | Signal | P/S | EV/S | Op margin | Fwd P/E | Rev +1y | FCF yield |
|---:|---|---|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Rocket Lab Corporation | `RKLB-USDT-SWAP` | **100** | **WATCH** | 38.2 | 33.0 | -24.6% | 800.0 | 38.7% | -0.9% |
| 2 | USA Rare Earth, Inc. | `USAR-USDT-SWAP` | **100** | **CORE** | 211.4 | 22.7 | -795.6% | 247.3 | 870.1% | -10.2% |
| 3 | IonQ, Inc. | `IONQ-USDT-SWAP` | **82** | **WATCH** | 46.0 | 32.5 | -408.2% | -19.7 | 77.6% | -0.8% |
| 4 | AST SpaceMobile, Inc. | `ASTS-USDT-SWAP` | **80** | **WATCH** | 101.9 | 89.0 | -544.6% | -20.8 | 264.2% | -15.3% |
| 5 | Moderna, Inc. | `MRNA-USDT-SWAP` | **80** | **WATCH** | 43.3 | 41.5 | -557.9% | -52.7 | 16.3% | 0.3% |
| 6 | Tesla, Inc. | `TSLA-USDT-SWAP` | **78** | **WATCH** | 13.1 | 12.8 | 5.4% | 159.2 | 13.5% | 0.4% |
| 7 | Nebius Group N.V. | `NBIS-USDT-SWAP` | **72** | **WATCH** | 22.6 | 25.9 | -0.2% | -33.5 | 266.0% | -31.5% |

## Top LONG candidates

| Rank | Company | OKX market | LONG score | Signal | P/S | EV/S | Op margin | Fwd P/E | Rev +1y | FCF yield |
|---:|---|---|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | QUALCOMM Incorporated | `QCOM-USDT-SWAP` | **100** | **CORE** | 3.8 | 4.3 | 18.5% | 12.2 | 15.7% | 6.1% |
| 2 | Taiwan Semiconductor Manufactur | `TSM-USDT-SWAP` | **90** | **CORE** | 0.4 | 2.3 | 58.7% | 15.1 | 37.8% | 65.7% |
| 3 | Sandisk Corporation | `SNDK-USDT-SWAP` | **90** | **CORE** | 4.0 | 3.8 | 79.6% | 2.8 | 22.3% | 9.8% |
| 4 | Applied Materials, Inc. | `AMAT-USDT-SWAP` | **85** | **WATCH** | 8.2 | 8.2 | 33.7% | 17.2 | 35.4% | 1.2% |
| 5 | Marvell Technology, Inc. | `MRVL-USDT-SWAP` | **85** | **WATCH** | 12.7 | 12.5 | 16.7% | 18.2 | 63.7% | 2.0% |
| 6 | Applovin Corporation | `APP-USDT-SWAP` | **83** | **CORE** | 17.5 | 13.4 | 77.7% | 17.8 | 24.9% | 2.7% |
| 7 | Western Digital Corporation | `WDC-USDT-SWAP` | **83** | **CORE** | 6.9 | 6.9 | 47.7% | 6.6 | 40.5% | 2.7% |
| 8 | Corning Incorporated | `GLW-USDT-SWAP` | **77** | **WATCH** | 5.0 | 5.4 | 18.9% | 22.9 | 21.1% | 1.0% |
| 9 | Robinhood Markets, Inc. | `HOOD-USDT-SWAP` | **77** | **WATCH** | 13.9 | 13.5 | 48.1% | 23.0 | 29.2% | — |
| 10 | Advanced Micro Devices, Inc. | `AMD-USDT-SWAP` | **77** | **WATCH** | 14.6 | 14.4 | 21.2% | 24.8 | 77.4% | 1.1% |

## Analyst consensus (12-month price target) — most upside

| Rank | Company | OKX | Price | Analyst mean target | Gap | Analysts | Currency |
|---:|---|---|---:|---:|---:|---:|---|
| 1 | SK hynix | `SKHYNIX` | 1172000.00 | 3157408.80 | **169.4%** | 39 | KRW |
| 2 | Hyperliquid Strategies Inc | `PURR` | 8.76 | 22.32 | **154.9%** | 4 | USD |
| 3 | Credo Technology Group Holding  | `CRDO` | 112.33 | 284.05 | **152.9%** | 19 | USD |
| 4 | Sandisk Corporation | `SNDK` | 806.43 | 2023.62 | **150.9%** | 24 | USD |
| 5 | AXT Inc | `AXT` | 36.72 | 91.60 | **149.5%** | 5 | USD |
| 6 | SamsungElec | `SAMSUNG` | 192000.00 | 478771.44 | **149.4%** | 35 | KRW |
| 7 | AST SpaceMobile, Inc. | `ASTS` | 30.20 | 74.68 | **147.3%** | 12 | USD |
| 8 | BitMine Immersion Technologies, | `BMNR` | 19.00 | 45.87 | **141.4%** | 3 | USD |
| 9 | Micron Technology, Inc. | `MU` | 656.39 | 1561.91 | **138.0%** | 45 | USD |
| 10 | IonQ, Inc. | `IONQ` | 26.43 | 62.27 | **135.6%** | 14 | USD |
| 11 | Marvell Technology, Inc. | `MRVL` | 133.55 | 313.73 | **134.9%** | 41 | USD |
| 12 | Nebius Group N.V. | `NBIS` | 120.37 | 281.00 | **133.4%** | 20 | USD |
| 13 | Western Digital Corporation | `WDC` | 267.63 | 613.38 | **129.2%** | 24 | USD |
| 14 | Coherent Corp. | `COHR` | 169.76 | 387.80 | **128.4%** | 25 | USD |
| 15 | Rocket Lab Corporation | `RKLB` | 45.99 | 102.15 | **122.1%** | 20 | USD |

## Analyst consensus (12-month price target) — most downside

| Rank | Company | OKX | Price | Analyst mean target | Gap | Analysts | Currency |
|---:|---|---|---:|---:|---:|---:|---|
| 1 | Moderna, Inc. | `MRNA` | 241.46 | 138.37 | **-42.7%** | 19 | USD |
| 2 | Apple Inc. | `AAPL` | 344.17 | 333.28 | **-3.2%** | 38 | USD |

Price/target uses the underlying Yahoo Finance share quote, not the OKX derivative. Minimum 3 analysts; unreliable price scales and missing coverage excluded. Targets are analyst opinions, not guaranteed forecasts.

## All OKX companies — our ratio + LONG/SHORT scores

| Company | OKX | P/S | EV/S | Op margin | Fwd P/E | EPS +1y | Rev +1y | FCF yield | LONG | SHORT |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| QUALCOMM Incorporated | `QCOM` | 3.8 | 4.3 | 18.5% | 12.2 | 26.5% | 15.7% | 6.1% | **100 CORE** | **0** |
| Rocket Lab Corporation | `RKLB` | 38.2 | 33.0 | -24.6% | 800.0 | 66.8% | 38.7% | -0.9% | **0** | **100 WATCH** |
| USA Rare Earth, Inc. | `USAR` | 211.4 | 22.7 | -795.6% | 247.3 | 105.3% | 870.1% | -10.2% | **0** | **100 CORE** |
| Sandisk Corporation | `SNDK` | 4.0 | 3.8 | 79.6% | 2.8 | 26.1% | 22.3% | 9.8% | **90 CORE** | **10** |
| Taiwan Semiconductor Manufactur | `TSM` | 0.4 | 2.3 | 58.7% | 15.1 | 33.6% | 37.8% | 65.7% | **90 CORE** | **10** |
| Marvell Technology, Inc. | `MRVL` | 12.7 | 12.5 | 16.7% | 18.2 | 73.9% | 63.7% | 2.0% | **85 WATCH** | **13** |
| Applied Materials, Inc. | `AMAT` | 8.2 | 8.2 | 33.7% | 17.2 | 45.0% | 35.4% | 1.2% | **85 WATCH** | **3** |
| Western Digital Corporation | `WDC` | 6.9 | 6.9 | 47.7% | 6.6 | 63.4% | 40.5% | 2.7% | **83 CORE** | **10** |
| Applovin Corporation | `APP` | 17.5 | 13.4 | 77.7% | 17.8 | 25.5% | 24.9% | 2.7% | **83 CORE** | **10** |
| IonQ, Inc. | `IONQ` | 46.0 | 32.5 | -408.2% | -19.7 | 23.1% | 77.6% | -0.8% | **0** | **82 WATCH** |
| Moderna, Inc. | `MRNA` | 43.3 | 41.5 | -557.9% | -52.7 | 42.3% | 16.3% | 0.3% | **0** | **80 WATCH** |
| AST SpaceMobile, Inc. | `ASTS` | 101.9 | 89.0 | -544.6% | -20.8 | 44.3% | 264.2% | -15.3% | **0** | **80 WATCH** |
| Tesla, Inc. | `TSLA` | 13.1 | 12.8 | 5.4% | 159.2 | 24.2% | 13.5% | 0.4% | **12** | **78 WATCH** |
| Advanced Micro Devices, Inc. | `AMD` | 14.6 | 14.4 | 21.2% | 24.8 | 102.2% | 77.4% | 1.1% | **77 WATCH** | **13** |
| Corning Incorporated | `GLW` | 5.0 | 5.4 | 18.9% | 22.9 | 34.1% | 21.1% | 1.0% | **77 WATCH** | **13** |
| Robinhood Markets, Inc. | `HOOD` | 13.9 | 13.5 | 48.1% | 23.0 | 39.7% | 29.2% | — | **77 WATCH** | **0** |
| AXT Inc | `AXT` | 14.1 | 11.8 | 38.7% | 14.4 | 116.3% | 115.9% | — | **75 WATCH** | **20** |
| Credo Technology Group Holding  | `CRDO` | 13.3 | 12.8 | 25.2% | 11.6 | 53.9% | 55.0% | 1.2% | **75 WATCH** | **18** |
| Micron Technology, Inc. | `MU` | 5.6 | 5.3 | 80.7% | 3.2 | 17.7% | 16.2% | 3.9% | **75 CORE** | **30** |
| Dell Technologies Inc. | `DELL` | 1.3 | 1.5 | 12.0% | 10.5 | 16.8% | 19.5% | 3.0% | **75 CORE** | **30** |
| NVIDIA Corporation | `NVDA` | 14.5 | 14.4 | 66.2% | 11.4 | 70.9% | 68.2% | 1.0% | **75 WATCH** | **18** |
| Broadcom Inc. | `AVGO` | 15.6 | 16.0 | 54.3% | 15.0 | 66.9% | 64.4% | 2.2% | **75 WATCH** | **18** |
| Nebius Group N.V. | `NBIS` | 22.6 | 25.9 | -0.2% | -33.5 | -191.4% | 266.0% | -31.5% | **0** | **72 WATCH** |
| Oracle Corporation | `ORCL` | 5.0 | 6.8 | 35.6% | 10.4 | 35.8% | 45.7% | -12.8% | **70 WATCH** | **10** |
| Adobe Inc. | `ADBE` | 3.7 | 3.7 | 34.8% | 9.0 | 12.1% | 9.1% | 9.7% | **65 WATCH** | **30** |
| Cerebras Systems Inc. | `CBRS` | 28.5 | 19.0 | -265.0% | 63.9 | 372.9% | 233.1% | — | **0** | **63** |
| XIAOMI-W | `XIAOMI` | 1.8 | 1.7 | 4.0% | 21.1 | 37.8% | 19.8% | -1.1% | **62 WATCH** | **10** |
| Coherent Corp. | `COHR` | 4.7 | 5.6 | 11.8% | 12.2 | 48.4% | 38.6% | -1.9% | **60 WATCH** | **25** |
| Okta, Inc. | `OKTA` | 9.7 | 9.0 | 13.3% | 39.1 | 11.4% | 10.1% | 3.5% | **13** | **60** |
| Microsoft Corporation | `MSFT` | 11.5 | 11.7 | 49.8% | 22.2 | 20.9% | 20.2% | 0.1% | **59 WATCH** | **3** |
| Coca-Cola Company (The) | `KO` | 8.1 | 8.6 | 33.4% | 27.1 | 5.6% | -3.1% | 1.1% | **0** | **58** |
| Meta Platforms, Inc. | `META` | 6.4 | 6.5 | 35.4% | 17.0 | 16.5% | 21.6% | 1.1% | **57 WATCH** | **38** |
| Arm Holdings plc | `ARM` | 34.5 | 39.1 | 7.6% | 54.5 | 37.0% | 36.5% | 0.7% | **55 WATCH** | **33** |
| Super Micro Computer, Inc. | `SMCI` | 0.3 | 0.5 | 10.3% | 4.7 | 18.0% | 15.9% | -46.0% | **52** | **45** |
| Netflix, Inc. | `NFLX` | 5.5 | 5.6 | 34.6% | 17.4 | 5.1% | 10.7% | 9.3% | **35** | **50** |
| Palantir Technologies Inc. | `PLTR` | 51.2 | 49.8 | 46.9% | 62.3 | 46.2% | 52.5% | 0.7% | **45** | **48** |
| Bloom Energy Corporation | `BE` | 12.9 | 13.0 | 18.5% | 31.5 | 62.7% | 56.4% | -0.0% | **45** | **35** |
| SamsungElec | `SAMSUNG` | 2.1 | 1.9 | 55.0% | 2.5 | 64.7% | 40.1% | 6.7% | **45** | **10** |
| Amazon.com, Inc. | `AMZN` | 3.5 | 3.8 | 13.9% | 23.8 | -16.7% | 15.6% | -1.2% | **0** | **45** |
| Coinbase Global, Inc. | `COIN` | 6.7 | 6.3 | -1.4% | 55.4 | 819.3% | 27.1% | 10.2% | **20** | **40** |
| SOFTBANK GROUP CORP | `SOFTBANK` | 2.6 | 6.2 | -11.6% | 12.2 | -14.5% | 7.0% | -10.7% | **0** | **40** |
| IREN LIMITED | `IREN` | 10.3 | 12.8 | -102.5% | -4.5 | -16.4% | 164.0% | -57.8% | **0** | **40** |
| CoreWeave, Inc. | `CRWV` | 3.2 | 9.2 | -1.9% | -21.7 | 9.7% | 105.4% | -37.7% | **0** | **40** |
| Apple Inc. | `AAPL` | 10.4 | 10.5 | 31.1% | 32.3 | 19.6% | 8.2% | 2.1% | **25** | **38** |
| Circle Internet Group, Inc. | `CRCL` | 5.9 | 5.3 | 24.1% | 47.0 | 24.9% | 27.3% | — | **35** | **25** |
| SK hynix | `SKHYNIX` | 3.1 | 3.0 | 79.7% | 2.2 | 47.4% | 58.8% | — | **30** | **5** |
| Lumentum Holdings Inc. | `LITE` | 12.3 | 12.2 | 28.0% | 13.1 | 57.1% | 49.2% | — | **30** | **20** |
| SK hynix | `SKHY` | 3.1 | 3.0 | 79.7% | 2.2 | 47.4% | 58.8% | — | **30** | **5** |
| Alphabet Inc. | `GOOGL` | 7.4 | 7.2 | 31.8% | 18.2 | -24.1% | 27.0% | -0.0% | **5** | **30** |
| Intel Corporation | `INTC` | 4.6 | 4.8 | 15.6% | 29.0 | 21.0% | 12.0% | 0.3% | **12** | **28** |
| Fluence Energy, Inc. | `FLNC` | 0.4 | 0.3 | -8.9% | -9.6 | 59.3% | 25.4% | 0.2% | **5** | **28** |
| Hyperliquid Strategies Inc | `PURR` | 257.7 | 168.6 | 9595.1% | 23.7 | 51.0% | 31.4% | — | **25** | **10** |
| BitMine Immersion Technologies, | `BMNR` | 187.3 | 181.8 | 8.4% | 20.2 | 103.2% | 421.8% | -4.5% | **25** | **25** |
| Strategy Inc | `MSTR` | 110.5 | 138.6 | -2.1% | 7.8 | 481.5% | 3.4% | -5.9% | **25** | **25** |
| Applied Optoelectronics, Inc. | `AAOI` | 6.7 | 6.3 | -12.9% | 10.2 | 576.8% | 156.5% | -22.3% | **10** | **25** |

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
