# OKX Long / Short Fundamental Scanner

Hourly scanner restricted to public companies exposed by the **OKX EEA TradFi / Stock Perpetual API universe**.

**Last scan:** 2026-11-06 18:04 UTC  
**Availability scope:** user-confirmed OKX EEA Stock Futures / X-Perp  
**OKX stock/ETF markets in configured universe:** 72  
**Public companies analysed:** 55  
**SHORT CORE:** 2  
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
| 1 | Marvell Technology, Inc. | MRVL | 1.8% | -30.8% | -14.5% | 90 | +12 | **100** | **CORE** | yes |
| 2 | Sandisk Corporation | SNDK | 1.7% | -28.7% | -13.5% | 90 | +11 | **100** | **CORE** | yes |
| 3 | Western Digital Corporation | WDC | -2.6% | -28.8% | -15.7% | 82 | +13 | **95** | **CORE** | yes |
| 4 | AXT Inc | AXT | 1.6% | -32.2% | -15.3% | 82 | +12 | **94** | **CORE** | yes |
| 5 | Applied Materials, Inc. | AMAT | 3.7% | -15.1% | -5.7% | 88 | +5 | **93** | **CORE** | yes |
| 6 | Taiwan Semiconductor Manufactur | TSM | 4.9% | -8.8% | -1.9% | 88 | +2 | **90** | **CORE** | yes |
| 7 | Credo Technology Group Holding  | CRDO | 3.0% | -23.4% | -10.2% | 82 | +8 | **90** | **CORE** | yes |
| 8 | Advanced Micro Devices, Inc. | AMD | 7.8% | -13.7% | -2.9% | 84 | +2 | **86** | **CORE** | yes |
| 9 | Broadcom Inc. | AVGO | -0.2% | -10.7% | -5.4% | 82 | +4 | **86** | **CORE** | yes |
| 10 | NVIDIA Corporation | NVDA | 2.4% | -9.1% | -3.4% | 82 | +3 | **85** | **CORE** | yes |

## Final model + Price Timing — SHORT

| Rank | Company | OKX | 24h | 7d | 50/50 move | Base SHORT | Timing adj. | Final | Signal | Prev. SHORT? |
|---:|---|---|---:|---:|---:|---:|---:|---:|---|---|
| 1 | Rocket Lab Corporation | RKLB | 10.4% | -7.3% | 1.6% | 100 | +1 | **100** | **CORE** | yes |
| 2 | USA Rare Earth, Inc. | USAR | 8.4% | -16.4% | -4.0% | 100 | -3 | **97** | **CORE** | yes |
| 3 | Moderna, Inc. | MRNA | 6.8% | 16.3% | 11.6% | 80 | +9 | **89** | **CORE** | yes |
| 4 | IonQ, Inc. | IONQ | 15.8% | 1.9% | 8.8% | 75 | +7 | **82** | **CORE** | yes |
| 5 | AST SpaceMobile, Inc. | ASTS | 4.2% | -23.2% | -9.5% | 80 | -8 | **72** | **WATCH** | yes |
| 6 | Nebius Group N.V. | NBIS | 4.2% | -18.6% | -7.2% | 76 | -6 | **70** | **WATCH** | yes |
| 7 | Tesla, Inc. | TSLA | 4.4% | -10.3% | -2.9% | 59 | -2 | **57** | **WATCH** | no |
| 8 | Cerebras Systems Inc. | CBRS | 4.9% | -21.5% | -8.3% | 63 | -7 | **56** | **WATCH** | no |

## Combined model — LONG

Weighted score: **70% fundamental + 30% P/E trend**.

| Rank | Company | OKX | Fundamental LONG | P/E trend LONG | Combined | Signal |
|---:|---|---|---:|---:|---:|---|
| 1 | Sandisk Corporation | `SNDK` | 90 | 90 | **90** | **CORE** |
| 2 | Marvell Technology, Inc. | `MRVL` | 85 | 100 | **90** | **CORE** |
| 3 | Taiwan Semiconductor Manufactur | `TSM` | 90 | 85 | **88** | **CORE** |
| 4 | Applied Materials, Inc. | `AMAT` | 85 | 95 | **88** | **CORE** |
| 5 | QUALCOMM Incorporated | `QCOM` | 100 | 50 | **85** | **CORE** |
| 6 | Advanced Micro Devices, Inc. | `AMD` | 77 | 100 | **84** | **CORE** |
| 7 | Western Digital Corporation | `WDC` | 83 | 80 | **82** | **CORE** |
| 8 | AXT Inc | `AXT` | 75 | 100 | **82** | **CORE** |
| 9 | Credo Technology Group Holding  | `CRDO` | 75 | 100 | **82** | **CORE** |
| 10 | Broadcom Inc. | `AVGO` | 75 | 100 | **82** | **CORE** |

## Combined model — SHORT

Weighted score: **70% fundamental + 30% P/E trend**.

| Rank | Company | OKX | Fundamental SHORT | P/E trend SHORT | Combined | Signal |
|---:|---|---|---:|---:|---:|---|
| 1 | Rocket Lab Corporation | `RKLB` | 100 | 0 | **100** | **CORE** |
| 2 | USA Rare Earth, Inc. | `USAR` | 100 | 0 | **100** | **CORE** |
| 3 | Moderna, Inc. | `MRNA` | 80 | 0 | **80** | **WATCH** |
| 4 | AST SpaceMobile, Inc. | `ASTS` | 80 | 0 | **80** | **WATCH** |
| 5 | Nebius Group N.V. | `NBIS` | 76 | 0 | **76** | **WATCH** |
| 6 | IonQ, Inc. | `IONQ` | 75 | 0 | **75** | **WATCH** |
| 7 | Tesla, Inc. | `TSLA` | 78 | 15 | **59** | **WATCH** |

## P/E Compression + Growth — LONG

| Rank | Company | OKX | Trail P/E | Fwd P/E | P/E change | EPS +1y | Rev +1y | Rev trend | LONG score | Signal |
|---:|---|---|---:|---:|---:|---:|---:|---|---:|---|
| 1 | Marvell Technology, Inc. | `MRVL` | 44.7 | 18.5 | -58.6% | 73.9% | 63.7% | accelerating | **100** | **CORE** |
| 2 | AXT Inc | `AXT` | 76.1 | 14.6 | -80.8% | 116.3% | 115.9% | decelerating | **100** | **CORE** |
| 3 | Credo Technology Group Holding  | `CRDO` | 41.0 | 11.9 | -71.0% | 53.9% | 55.0% | decelerating | **100** | **CORE** |
| 4 | Advanced Micro Devices, Inc. | `AMD` | 93.1 | 26.0 | -72.1% | 108.0% | 79.4% | accelerating | **100** | **CORE** |
| 5 | Broadcom Inc. | `AVGO` | 37.2 | 15.0 | -59.8% | 66.9% | 64.4% | decelerating | **100** | **CORE** |
| 6 | NVIDIA Corporation | `NVDA` | 23.5 | 11.7 | -50.3% | 70.9% | 68.2% | decelerating | **100** | **CORE** |
| 7 | Bloom Energy Corporation | `BE` | 103.3 | 32.0 | -69.0% | 62.7% | 56.4% | decelerating | **96** | **CORE** |
| 8 | Applied Materials, Inc. | `AMAT` | 28.6 | 17.8 | -37.5% | 45.0% | 35.4% | accelerating | **95** | **CORE** |
| 9 | Oracle Corporation | `ORCL` | 17.7 | 10.2 | -42.3% | 35.8% | 45.7% | accelerating | **95** | **CORE** |
| 10 | Coherent Corp. | `COHR` | 39.0 | 13.5 | -65.4% | 48.4% | 38.6% | decelerating | **95** | **CORE** |

## P/E Expansion + Weakening — SHORT

| Rank | Company | OKX | Trail P/E | Fwd P/E | P/E change | EPS +1y | Rev +1y | Rev trend | SHORT score | Signal |
|---:|---|---|---:|---:|---:|---:|---:|---|---:|---|
| 1 | SOFTBANK GROUP CORP | `SOFTBANK` | 4.1 | 12.0 | 191.0% | -14.5% | 7.0% | decelerating | **86** | **CORE** |
| 2 | Hyperliquid Strategies Inc | `PURR` | 2.7 | 23.6 | 767.6% | 51.0% | 31.4% | decelerating | **55** | **WATCH** |
| 3 | Amazon.com, Inc. | `AMZN` | 21.1 | 24.0 | 13.4% | -16.7% | 15.6% | decelerating | **52** | **WATCH** |
| 4 | Alphabet Inc. | `GOOGL` | 14.9 | 18.4 | 23.6% | -24.1% | 27.0% | accelerating | **50** | **WATCH** |

## Top SHORT candidates

| Rank | Company | OKX market | SHORT score | Signal | P/S | EV/S | Op margin | Fwd P/E | Rev +1y | FCF yield |
|---:|---|---|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Rocket Lab Corporation | `RKLB-USDT-SWAP` | **100** | **CORE** | 42.2 | 33.0 | -24.6% | 882.9 | 38.7% | -0.8% |
| 2 | USA Rare Earth, Inc. | `USAR-USDT-SWAP` | **100** | **CORE** | 229.2 | 22.7 | -795.6% | 268.1 | 870.1% | -9.4% |
| 3 | AST SpaceMobile, Inc. | `ASTS-USDT-SWAP` | **80** | **WATCH** | 106.2 | 89.0 | -544.6% | -21.7 | 264.2% | -14.7% |
| 4 | Moderna, Inc. | `MRNA-USDT-SWAP` | **80** | **WATCH** | 46.2 | 41.5 | -557.9% | -56.2 | 16.3% | 0.3% |
| 5 | Tesla, Inc. | `TSLA-USDT-SWAP` | **78** | **WATCH** | 13.7 | 12.8 | 5.4% | 166.1 | 13.5% | 0.4% |
| 6 | Nebius Group N.V. | `NBIS-USDT-SWAP` | **76** | **WATCH** | 25.2 | 25.9 | -0.2% | -34.9 | 266.0% | -28.2% |
| 7 | IonQ, Inc. | `IONQ-USDT-SWAP` | **75** | **WATCH** | 34.5 | 27.7 | -249.1% | -22.8 | 77.6% | -3.2% |

## Top LONG candidates

| Rank | Company | OKX market | LONG score | Signal | P/S | EV/S | Op margin | Fwd P/E | Rev +1y | FCF yield |
|---:|---|---|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | QUALCOMM Incorporated | `QCOM-USDT-SWAP` | **100** | **CORE** | 4.0 | 4.1 | 15.4% | 12.9 | 15.3% | 5.2% |
| 2 | Taiwan Semiconductor Manufactur | `TSM-USDT-SWAP` | **90** | **CORE** | 0.4 | 2.3 | 58.7% | 15.8 | 37.8% | 62.6% |
| 3 | Sandisk Corporation | `SNDK-USDT-SWAP` | **90** | **CORE** | 4.0 | 3.8 | 79.6% | 2.8 | 22.3% | 9.6% |
| 4 | Applied Materials, Inc. | `AMAT-USDT-SWAP` | **85** | **WATCH** | 8.5 | 8.2 | 33.7% | 17.8 | 35.4% | 1.2% |
| 5 | Marvell Technology, Inc. | `MRVL-USDT-SWAP` | **85** | **WATCH** | 12.9 | 12.5 | 16.7% | 18.5 | 63.7% | 2.0% |
| 6 | Western Digital Corporation | `WDC-USDT-SWAP` | **83** | **CORE** | 6.7 | 6.9 | 47.7% | 6.4 | 40.5% | 2.8% |
| 7 | Corning Incorporated | `GLW-USDT-SWAP` | **77** | **WATCH** | 5.1 | 5.4 | 18.9% | 23.2 | 21.1% | 1.0% |
| 8 | Robinhood Markets, Inc. | `HOOD-USDT-SWAP` | **77** | **WATCH** | 14.0 | 13.5 | 48.1% | 23.1 | 29.2% | — |
| 9 | Advanced Micro Devices, Inc. | `AMD-USDT-SWAP` | **77** | **WATCH** | 15.7 | 14.5 | 21.2% | 26.0 | 79.4% | 1.0% |
| 10 | Applovin Corporation | `APP-USDT-SWAP` | **75** | **CORE** | 17.0 | 15.6 | 78.2% | 19.5 | 21.9% | 2.9% |

## Analyst consensus (12-month price target) — most upside

| Rank | Company | OKX | Price | Analyst mean target | Gap | Analysts | Currency |
|---:|---|---|---:|---:|---:|---:|---|
| 1 | CoreWeave, Inc. | `CRWV` | 44.27 | 132.18 | **198.6%** | 38 | USD |
| 2 | SK hynix | `SKHYNIX` | 1132000.00 | 3157408.80 | **178.9%** | 39 | KRW |
| 3 | Hyperliquid Strategies Inc | `PURR` | 8.74 | 22.32 | **155.5%** | 4 | USD |
| 4 | SamsungElec | `SAMSUNG` | 188700.00 | 478771.44 | **153.7%** | 35 | KRW |
| 5 | BitMine Immersion Technologies, | `BMNR` | 18.48 | 45.87 | **148.3%** | 3 | USD |
| 6 | Sandisk Corporation | `SNDK` | 820.33 | 2023.62 | **146.7%** | 24 | USD |
| 7 | AXT Inc | `AXT` | 37.31 | 91.60 | **145.5%** | 5 | USD |
| 8 | Credo Technology Group Holding  | `CRDO` | 115.72 | 284.05 | **145.4%** | 19 | USD |
| 9 | AST SpaceMobile, Inc. | `ASTS` | 31.47 | 74.68 | **137.3%** | 12 | USD |
| 10 | Western Digital Corporation | `WDC` | 260.59 | 613.38 | **135.4%** | 24 | USD |
| 11 | Micron Technology, Inc. | `MU` | 682.24 | 1561.91 | **128.9%** | 45 | USD |
| 12 | Marvell Technology, Inc. | `MRVL` | 135.98 | 311.29 | **128.9%** | 41 | USD |
| 13 | Nebius Group N.V. | `NBIS` | 125.47 | 281.00 | **124.0%** | 20 | USD |
| 14 | SOFTBANK GROUP CORP | `SOFTBANK` | 3549.00 | 7845.25 | **121.1%** | 18 | JPY |
| 15 | Lumentum Holdings Inc. | `LITE` | 521.68 | 1100.15 | **110.9%** | 26 | USD |

## Analyst consensus (12-month price target) — most downside

| Rank | Company | OKX | Price | Analyst mean target | Gap | Analysts | Currency |
|---:|---|---|---:|---:|---:|---:|---|
| 1 | Moderna, Inc. | `MRNA` | 257.90 | 138.37 | **-46.3%** | 19 | USD |
| 2 | Apple Inc. | `AAPL` | 344.12 | 333.28 | **-3.1%** | 38 | USD |

Price/target uses the underlying Yahoo Finance share quote, not the OKX derivative. Minimum 3 analysts; unreliable price scales and missing coverage excluded. Targets are analyst opinions, not guaranteed forecasts.

## All OKX companies — our ratio + LONG/SHORT scores

| Company | OKX | P/S | EV/S | Op margin | Fwd P/E | EPS +1y | Rev +1y | FCF yield | LONG | SHORT |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| QUALCOMM Incorporated | `QCOM` | 4.0 | 4.1 | 15.4% | 12.9 | 26.5% | 15.3% | 5.2% | **100 CORE** | **0** |
| Rocket Lab Corporation | `RKLB` | 42.2 | 33.0 | -24.6% | 882.9 | 66.8% | 38.7% | -0.8% | **0** | **100 CORE** |
| USA Rare Earth, Inc. | `USAR` | 229.2 | 22.7 | -795.6% | 268.1 | 105.3% | 870.1% | -9.4% | **0** | **100 CORE** |
| Sandisk Corporation | `SNDK` | 4.0 | 3.8 | 79.6% | 2.8 | 27.1% | 22.3% | 9.6% | **90 CORE** | **10** |
| Taiwan Semiconductor Manufactur | `TSM` | 0.4 | 2.3 | 58.7% | 15.8 | 33.6% | 37.8% | 62.6% | **90 CORE** | **10** |
| Marvell Technology, Inc. | `MRVL` | 12.9 | 12.5 | 16.7% | 18.5 | 73.9% | 63.7% | 2.0% | **85 WATCH** | **13** |
| Applied Materials, Inc. | `AMAT` | 8.5 | 8.2 | 33.7% | 17.8 | 45.0% | 35.4% | 1.2% | **85 WATCH** | **3** |
| Western Digital Corporation | `WDC` | 6.7 | 6.9 | 47.7% | 6.4 | 63.4% | 40.5% | 2.8% | **83 CORE** | **10** |
| Moderna, Inc. | `MRNA` | 46.2 | 41.5 | -557.9% | -56.2 | 42.3% | 16.3% | 0.3% | **0** | **80 WATCH** |
| AST SpaceMobile, Inc. | `ASTS` | 106.2 | 89.0 | -544.6% | -21.7 | 44.3% | 264.2% | -14.7% | **0** | **80 WATCH** |
| Tesla, Inc. | `TSLA` | 13.7 | 12.8 | 5.4% | 166.1 | 24.2% | 13.5% | 0.4% | **12** | **78 WATCH** |
| Advanced Micro Devices, Inc. | `AMD` | 15.7 | 14.5 | 21.2% | 26.0 | 108.0% | 79.4% | 1.0% | **77 WATCH** | **13** |
| Corning Incorporated | `GLW` | 5.1 | 5.4 | 18.9% | 23.2 | 34.1% | 21.1% | 1.0% | **77 WATCH** | **13** |
| Robinhood Markets, Inc. | `HOOD` | 14.0 | 13.5 | 48.1% | 23.1 | 39.7% | 29.2% | — | **77 WATCH** | **0** |
| Nebius Group N.V. | `NBIS` | 25.2 | 25.9 | -0.2% | -34.9 | -191.4% | 266.0% | -28.2% | **0** | **76 WATCH** |
| AXT Inc | `AXT` | 14.3 | 11.8 | 38.7% | 14.6 | 116.3% | 115.9% | — | **75 WATCH** | **20** |
| Credo Technology Group Holding  | `CRDO` | 13.7 | 12.8 | 25.2% | 11.9 | 53.9% | 55.0% | 1.1% | **75 WATCH** | **28** |
| Broadcom Inc. | `AVGO` | 15.6 | 16.0 | 54.3% | 15.0 | 66.9% | 64.4% | 2.2% | **75 WATCH** | **18** |
| Micron Technology, Inc. | `MU` | 5.8 | 5.3 | 80.7% | 3.3 | 17.7% | 16.2% | 3.8% | **75 CORE** | **30** |
| NVIDIA Corporation | `NVDA` | 14.8 | 14.4 | 66.2% | 11.7 | 70.9% | 68.2% | 0.9% | **75 WATCH** | **18** |
| Dell Technologies Inc. | `DELL` | 1.4 | 1.5 | 12.0% | 10.8 | 16.8% | 19.5% | 2.9% | **75 CORE** | **30** |
| Applovin Corporation | `APP` | 17.0 | 15.6 | 78.2% | 19.5 | 24.3% | 21.9% | 2.9% | **75 CORE** | **10** |
| IonQ, Inc. | `IONQ` | 34.5 | 27.7 | -249.1% | -22.8 | 23.1% | 77.6% | -3.2% | **0** | **75 WATCH** |
| Oracle Corporation | `ORCL` | 4.9 | 6.8 | 35.6% | 10.2 | 35.8% | 45.7% | -13.0% | **70 WATCH** | **10** |
| Adobe Inc. | `ADBE` | 3.6 | 3.7 | 34.8% | 8.8 | 12.1% | 9.1% | 10.0% | **65 WATCH** | **30** |
| Cerebras Systems Inc. | `CBRS` | 29.9 | 19.1 | -265.0% | 67.0 | 372.9% | 233.1% | — | **0** | **63** |
| XIAOMI-W | `XIAOMI` | 1.8 | 1.6 | 4.0% | 20.3 | 37.8% | 19.8% | -1.1% | **62 WATCH** | **10** |
| Coherent Corp. | `COHR` | 4.7 | 4.6 | 16.3% | 13.5 | 48.4% | 38.6% | -4.5% | **60 WATCH** | **25** |
| Okta, Inc. | `OKTA` | 9.8 | 9.0 | 13.3% | 39.4 | 11.4% | 10.1% | 3.4% | **13** | **60** |
| Microsoft Corporation | `MSFT` | 11.4 | 11.7 | 49.8% | 22.1 | 20.9% | 20.3% | 0.1% | **59 WATCH** | **3** |
| Coca-Cola Company (The) | `KO` | 8.1 | 8.6 | 33.4% | 27.3 | 5.6% | -3.1% | 1.1% | **0** | **58** |
| Meta Platforms, Inc. | `META` | 6.5 | 6.5 | 35.4% | 17.3 | 16.5% | 21.6% | 1.1% | **57 WATCH** | **38** |
| Super Micro Computer, Inc. | `SMCI` | 0.3 | 0.5 | 10.3% | 4.6 | 18.0% | 15.9% | -43.9% | **52** | **45** |
| Netflix, Inc. | `NFLX` | 5.3 | 5.6 | 34.6% | 16.9 | 5.1% | 10.7% | 9.7% | **35** | **50** |
| Palantir Technologies Inc. | `PLTR` | 53.0 | 49.8 | 46.9% | 64.4 | 46.2% | 52.5% | 0.7% | **45** | **48** |
| Bloom Energy Corporation | `BE` | 13.2 | 13.0 | 18.5% | 32.0 | 62.7% | 56.4% | -0.0% | **45** | **35** |
| SamsungElec | `SAMSUNG` | 2.1 | 1.8 | 55.0% | 2.5 | 64.7% | 40.1% | 6.8% | **45** | **10** |
| Amazon.com, Inc. | `AMZN` | 3.5 | 3.8 | 13.9% | 24.0 | -16.7% | 15.6% | -1.2% | **0** | **45** |
| Arm Holdings plc | `ARM` | 33.4 | 32.1 | 13.9% | 55.8 | 36.4% | 37.1% | 0.6% | **43** | **33** |
| Coinbase Global, Inc. | `COIN` | 6.4 | 6.3 | -1.4% | 53.7 | 819.3% | 27.1% | 10.5% | **20** | **40** |
| SOFTBANK GROUP CORP | `SOFTBANK` | 2.5 | 5.9 | -11.6% | 12.0 | -14.5% | 7.0% | -10.8% | **0** | **40** |
| CoreWeave, Inc. | `CRWV` | 3.2 | 9.2 | -1.9% | -21.6 | 9.7% | 105.4% | -37.2% | **0** | **40** |
| IREN LIMITED | `IREN` | 12.1 | 20.4 | -84.2% | -5.2 | -16.4% | 164.0% | — | **0** | **39** |
| Apple Inc. | `AAPL` | 10.4 | 10.5 | 31.1% | 32.3 | 19.6% | 8.2% | 2.1% | **25** | **38** |
| Circle Internet Group, Inc. | `CRCL` | 5.6 | 5.3 | 24.1% | 44.5 | 24.9% | 27.3% | 1.5% | **35** | **33** |
| SK hynix | `SKHYNIX` | 3.0 | 2.7 | 79.7% | 2.1 | 47.4% | 58.8% | — | **30** | **5** |
| Lumentum Holdings Inc. | `LITE` | 12.6 | 12.2 | 28.0% | 13.4 | 59.1% | 49.2% | 0.3% | **30** | **28** |
| SK hynix | `SKHY` | 3.0 | 2.7 | 79.7% | 2.1 | 47.4% | 58.8% | — | **30** | **5** |
| Alphabet Inc. | `GOOGL` | 7.4 | 7.2 | 31.8% | 18.4 | -24.1% | 27.0% | -0.0% | **5** | **30** |
| Intel Corporation | `INTC` | 4.9 | 4.9 | 15.6% | 30.8 | 21.1% | 12.0% | 0.3% | **5** | **28** |
| Fluence Energy, Inc. | `FLNC` | 0.4 | 0.3 | -8.9% | -9.7 | 59.3% | 25.4% | 0.2% | **5** | **28** |
| Hyperliquid Strategies Inc | `PURR` | 112.0 | 100.0 | 6593.3% | 23.6 | 51.0% | 31.4% | — | **25** | **10** |
| BitMine Immersion Technologies, | `BMNR` | 182.1 | 181.8 | 8.4% | 19.7 | 103.2% | 421.8% | -4.6% | **25** | **25** |
| Strategy Inc | `MSTR` | 108.1 | 138.4 | -2.1% | 7.6 | 451.5% | 3.4% | -6.1% | **25** | **25** |
| Applied Optoelectronics, Inc. | `AAOI` | 5.4 | 5.4 | -0.5% | 10.4 | 576.8% | 156.5% | -32.5% | **10** | **25** |

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
