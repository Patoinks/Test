# OKX Long / Short Fundamental Scanner

Hourly scanner restricted to public companies exposed by the **OKX EEA TradFi / Stock Perpetual API universe**.

**Last scan:** 2026-11-05 06:57 UTC  
**Availability scope:** user-confirmed OKX EEA Stock Futures / X-Perp  
**OKX stock/ETF markets in configured universe:** 72  
**Public companies analysed:** 55  
**SHORT CORE:** 4  
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
| 1 | Sandisk Corporation | SNDK | -0.0% | -22.0% | -11.0% | 90 | +9 | **99** | **CORE** | yes |
| 2 | Marvell Technology, Inc. | MRVL | -0.0% | -26.8% | -13.4% | 84 | +11 | **95** | **CORE** | yes |
| 3 | Applied Materials, Inc. | AMAT | 0.0% | -12.4% | -6.2% | 88 | +5 | **93** | **CORE** | yes |
| 4 | QUALCOMM Incorporated | QCOM | -0.0% | -6.6% | -3.3% | 89 | +3 | **92** | **CORE** | no |
| 5 | Taiwan Semiconductor Manufactur | TSM | 0.0% | -8.4% | -4.2% | 88 | +3 | **91** | **CORE** | yes |
| 6 | AXT Inc | AXT | -0.0% | -21.9% | -11.0% | 82 | +9 | **91** | **CORE** | yes |
| 7 | Credo Technology Group Holding  | CRDO | 0.0% | -17.4% | -8.7% | 82 | +7 | **89** | **CORE** | yes |
| 8 | NVIDIA Corporation | NVDA | -0.0% | -6.3% | -3.2% | 82 | +3 | **85** | **CORE** | yes |
| 9 | Broadcom Inc. | AVGO | -0.0% | -5.7% | -2.8% | 82 | +2 | **84** | **CORE** | yes |
| 10 | Advanced Micro Devices, Inc. | AMD | 0.0% | -13.7% | -6.9% | 79 | +5 | **84** | **CORE** | yes |

## Final model + Price Timing — SHORT

| Rank | Company | OKX | 24h | 7d | 50/50 move | Base SHORT | Timing adj. | Final | Signal | Prev. SHORT? |
|---:|---|---|---:|---:|---:|---:|---:|---:|---|---|
| 1 | Rocket Lab Corporation | RKLB | 0.0% | -11.4% | -5.7% | 100 | -5 | **95** | **CORE** | yes |
| 2 | USA Rare Earth, Inc. | USAR | 0.0% | -22.1% | -11.0% | 100 | -9 | **91** | **CORE** | yes |
| 3 | Moderna, Inc. | MRNA | -0.0% | 16.0% | 8.0% | 80 | +6 | **86** | **CORE** | yes |
| 4 | IonQ, Inc. | IONQ | -0.0% | -6.9% | -3.4% | 85 | -3 | **82** | **CORE** | yes |
| 5 | Nebius Group N.V. | NBIS | -0.0% | -17.7% | -8.9% | 80 | -7 | **73** | **WATCH** | yes |
| 6 | AST SpaceMobile, Inc. | ASTS | 0.0% | -17.3% | -8.6% | 80 | -7 | **73** | **WATCH** | yes |
| 7 | Cerebras Systems Inc. | CBRS | 0.0% | -20.2% | -10.1% | 71 | -8 | **63** | **WATCH** | yes |
| 8 | Tesla, Inc. | TSLA | -0.0% | -4.5% | -2.2% | 59 | -2 | **57** | **WATCH** | yes |

## Combined model — LONG

Weighted score: **70% fundamental + 30% P/E trend**.

| Rank | Company | OKX | Fundamental LONG | P/E trend LONG | Combined | Signal |
|---:|---|---|---:|---:|---:|---|
| 1 | Sandisk Corporation | `SNDK` | 90 | 90 | **90** | **CORE** |
| 2 | QUALCOMM Incorporated | `QCOM` | 100 | 62 | **89** | **CORE** |
| 3 | Taiwan Semiconductor Manufactur | `TSM` | 90 | 85 | **88** | **CORE** |
| 4 | Applied Materials, Inc. | `AMAT` | 85 | 95 | **88** | **CORE** |
| 5 | Marvell Technology, Inc. | `MRVL` | 77 | 100 | **84** | **CORE** |
| 6 | AXT Inc | `AXT` | 75 | 100 | **82** | **CORE** |
| 7 | Credo Technology Group Holding  | `CRDO` | 75 | 100 | **82** | **CORE** |
| 8 | NVIDIA Corporation | `NVDA` | 75 | 100 | **82** | **CORE** |
| 9 | Broadcom Inc. | `AVGO` | 75 | 100 | **82** | **CORE** |
| 10 | Corning Incorporated | `GLW` | 77 | 86 | **80** | **CORE** |

## Combined model — SHORT

Weighted score: **70% fundamental + 30% P/E trend**.

| Rank | Company | OKX | Fundamental SHORT | P/E trend SHORT | Combined | Signal |
|---:|---|---|---:|---:|---:|---|
| 1 | Rocket Lab Corporation | `RKLB` | 100 | 0 | **100** | **CORE** |
| 2 | USA Rare Earth, Inc. | `USAR` | 100 | 0 | **100** | **CORE** |
| 3 | IonQ, Inc. | `IONQ` | 85 | 0 | **85** | **CORE** |
| 4 | Moderna, Inc. | `MRNA` | 80 | 0 | **80** | **WATCH** |
| 5 | Nebius Group N.V. | `NBIS` | 80 | 0 | **80** | **WATCH** |
| 6 | AST SpaceMobile, Inc. | `ASTS` | 80 | 0 | **80** | **WATCH** |
| 7 | Cerebras Systems Inc. | `CBRS` | 71 | 0 | **71** | **WATCH** |
| 8 | Okta, Inc. | `OKTA` | 80 | 13 | **60** | **WATCH** |
| 9 | Tesla, Inc. | `TSLA` | 78 | 15 | **59** | **WATCH** |

## P/E Compression + Growth — LONG

| Rank | Company | OKX | Trail P/E | Fwd P/E | P/E change | EPS +1y | Rev +1y | Rev trend | LONG score | Signal |
|---:|---|---|---:|---:|---:|---:|---:|---|---:|---|
| 1 | Marvell Technology, Inc. | `MRVL` | 52.6 | 21.8 | -58.6% | 73.9% | 63.7% | accelerating | **100** | **CORE** |
| 2 | AXT Inc | `AXT` | 97.0 | 18.7 | -80.8% | 116.3% | 115.9% | decelerating | **100** | **CORE** |
| 3 | Credo Technology Group Holding  | `CRDO` | 48.4 | 14.1 | -71.0% | 53.9% | 55.0% | decelerating | **100** | **CORE** |
| 4 | NVIDIA Corporation | `NVDA` | 25.3 | 12.6 | -50.3% | 70.9% | 68.2% | decelerating | **100** | **CORE** |
| 5 | Advanced Micro Devices, Inc. | `AMD` | 104.4 | 30.0 | -71.2% | 101.8% | 77.5% | accelerating | **100** | **CORE** |
| 6 | Broadcom Inc. | `AVGO` | 41.6 | 16.7 | -59.8% | 66.9% | 64.4% | decelerating | **100** | **CORE** |
| 7 | Applied Materials, Inc. | `AMAT` | 31.9 | 19.9 | -37.5% | 45.0% | 35.4% | accelerating | **95** | **CORE** |
| 8 | Oracle Corporation | `ORCL` | 19.4 | 11.2 | -42.3% | 35.8% | 45.7% | accelerating | **95** | **CORE** |
| 9 | Coherent Corp. | `COHR` | 40.4 | 14.0 | -65.4% | 48.4% | 38.6% | decelerating | **95** | **CORE** |
| 10 | Arm Holdings plc | `ARM` | 220.5 | 62.7 | -71.6% | 37.0% | 36.5% | accelerating | **95** | **CORE** |

## P/E Expansion + Weakening — SHORT

| Rank | Company | OKX | Trail P/E | Fwd P/E | P/E change | EPS +1y | Rev +1y | Rev trend | SHORT score | Signal |
|---:|---|---|---:|---:|---:|---:|---:|---|---:|---|
| 1 | SOFTBANK GROUP CORP | `SOFTBANK` | 4.6 | 13.5 | 191.0% | -14.5% | 7.0% | decelerating | **86** | **CORE** |
| 2 | Hyperliquid Strategies Inc | `PURR` | 3.0 | 26.2 | 767.6% | 51.0% | 31.4% | decelerating | **55** | **WATCH** |
| 3 | Amazon.com, Inc. | `AMZN` | 21.5 | 24.4 | 13.3% | -16.7% | 14.6% | decelerating | **52** | **WATCH** |
| 4 | Alphabet Inc. | `GOOGL` | 15.1 | 18.6 | 23.6% | -24.1% | 27.0% | accelerating | **50** | **WATCH** |

## Top SHORT candidates

| Rank | Company | OKX market | SHORT score | Signal | P/S | EV/S | Op margin | Fwd P/E | Rev +1y | FCF yield |
|---:|---|---|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Rocket Lab Corporation | `RKLB-USDT-SWAP` | **100** | **CORE** | 43.5 | 37.9 | -24.6% | 910.9 | 38.7% | -0.8% |
| 2 | USA Rare Earth, Inc. | `USAR-USDT-SWAP` | **100** | **CORE** | 233.7 | 37.2 | -795.6% | 273.3 | 870.1% | -9.2% |
| 3 | IonQ, Inc. | `IONQ-USDT-SWAP` | **85** | **CORE** | 51.5 | 37.3 | -408.2% | -22.0 | 77.6% | -0.7% |
| 4 | Nebius Group N.V. | `NBIS-USDT-SWAP` | **80** | **WATCH** | 28.4 | 30.2 | -0.2% | -39.3 | 266.0% | -25.0% |
| 5 | Okta, Inc. | `OKTA-USDT-SWAP` | **80** | **CORE** | 10.9 | 10.1 | 13.3% | 43.6 | 10.1% | 3.1% |
| 6 | AST SpaceMobile, Inc. | `ASTS-USDT-SWAP` | **80** | **WATCH** | 120.2 | 103.1 | -544.6% | -24.5 | 264.2% | -13.0% |
| 7 | Moderna, Inc. | `MRNA-USDT-SWAP` | **80** | **WATCH** | 46.3 | 44.6 | -557.9% | -56.4 | 16.3% | 0.3% |
| 8 | Tesla, Inc. | `TSLA-USDT-SWAP` | **78** | **WATCH** | 14.7 | 14.4 | 5.4% | 178.4 | 13.5% | 0.3% |
| 9 | Cerebras Systems Inc. | `CBRS-USDT-SWAP` | **71** | **WATCH** | 32.1 | 22.6 | -265.0% | 71.8 | 233.1% | — |
| 10 | Circle Internet Group, Inc. | `CRCL-USDT-SWAP` | **33** | **WATCH** | 6.7 | 6.0 | 4.9% | 51.5 | 27.3% | 1.1% |

## Top LONG candidates

| Rank | Company | OKX market | LONG score | Signal | P/S | EV/S | Op margin | Fwd P/E | Rev +1y | FCF yield |
|---:|---|---|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | QUALCOMM Incorporated | `QCOM-USDT-SWAP` | **100** | **CORE** | 4.2 | 4.3 | 18.5% | 13.5 | 15.7% | 5.5% |
| 2 | Taiwan Semiconductor Manufactur | `TSM-USDT-SWAP` | **90** | **CORE** | 0.4 | 2.7 | 58.7% | 16.9 | 37.8% | 58.6% |
| 3 | Sandisk Corporation | `SNDK-USDT-SWAP` | **90** | **CORE** | 5.1 | 4.9 | 79.6% | 3.6 | 22.3% | 7.6% |
| 4 | Applied Materials, Inc. | `AMAT-USDT-SWAP` | **85** | **WATCH** | 9.5 | 9.4 | 33.7% | 19.9 | 35.4% | 1.0% |
| 5 | Applovin Corporation | `APP-USDT-SWAP` | **83** | **CORE** | 13.4 | 13.4 | 77.7% | 13.6 | 24.9% | 3.5% |
| 6 | Corning Incorporated | `GLW-USDT-SWAP` | **77** | **WATCH** | 5.8 | 6.2 | 18.9% | 26.2 | 21.1% | 0.9% |
| 7 | Robinhood Markets, Inc. | `HOOD-USDT-SWAP` | **77** | **WATCH** | 15.5 | 15.1 | 48.1% | 25.6 | 29.2% | — |
| 8 | Marvell Technology, Inc. | `MRVL-USDT-SWAP` | **77** | **WATCH** | 15.2 | 15.0 | 16.7% | 21.8 | 63.7% | 1.7% |
| 9 | Dell Technologies Inc. | `DELL-USDT-SWAP` | **75** | **CORE** | 1.6 | 1.7 | 12.0% | 12.3 | 19.5% | 2.5% |
| 10 | Credo Technology Group Holding  | `CRDO-USDT-SWAP` | **75** | **WATCH** | 16.1 | 15.7 | 25.2% | 14.1 | 55.0% | 1.0% |

## Analyst consensus (12-month price target) — most upside

| Rank | Company | OKX | Price | Analyst mean target | Gap | Analysts | Currency |
|---:|---|---|---:|---:|---:|---:|---|
| 1 | Cerebras Systems Inc. | `CBRS` | 91.85 | 275.27 | **199.7%** | 11 | USD |
| 2 | CoreWeave, Inc. | `CRWV` | 48.42 | 132.18 | **173.0%** | 38 | USD |
| 3 | Applied Optoelectronics, Inc. | `AAOI` | 59.27 | 156.00 | **163.2%** | 5 | USD |
| 4 | SK hynix | `SKHYNIX` | 1264000.00 | 3157408.80 | **149.8%** | 39 | KRW |
| 5 | SamsungElec | `SAMSUNG` | 201500.00 | 478771.44 | **137.6%** | 35 | KRW |
| 6 | Hyperliquid Strategies Inc | `PURR` | 9.69 | 22.32 | **130.4%** | 4 | USD |
| 7 | BitMine Immersion Technologies, | `BMNR` | 21.73 | 45.87 | **111.1%** | 3 | USD |
| 8 | IonQ, Inc. | `IONQ` | 29.54 | 62.27 | **110.8%** | 14 | USD |
| 9 | AST SpaceMobile, Inc. | `ASTS` | 35.62 | 74.68 | **109.7%** | 12 | USD |
| 10 | Credo Technology Group Holding  | `CRDO` | 136.50 | 284.05 | **108.1%** | 19 | USD |
| 11 | Coherent Corp. | `COHR` | 195.09 | 387.80 | **98.8%** | 25 | USD |
| 12 | Nebius Group N.V. | `NBIS` | 141.52 | 281.00 | **98.6%** | 20 | USD |
| 13 | SOFTBANK GROUP CORP | `SOFTBANK` | 3980.00 | 7845.25 | **97.1%** | 18 | JPY |
| 14 | Micron Technology, Inc. | `MU` | 795.23 | 1561.91 | **96.4%** | 45 | USD |
| 15 | Marvell Technology, Inc. | `MRVL` | 159.80 | 313.73 | **96.3%** | 41 | USD |

## Analyst consensus (12-month price target) — most downside

| Rank | Company | OKX | Price | Analyst mean target | Gap | Analysts | Currency |
|---:|---|---|---:|---:|---:|---:|---|
| 1 | Moderna, Inc. | `MRNA` | 258.38 | 138.37 | **-46.4%** | 19 | USD |
| 2 | Apple Inc. | `AAPL` | 349.51 | 333.28 | **-4.6%** | 38 | USD |

Price/target uses the underlying Yahoo Finance share quote, not the OKX derivative. Minimum 3 analysts; unreliable price scales and missing coverage excluded. Targets are analyst opinions, not guaranteed forecasts.

## All OKX companies — our ratio + LONG/SHORT scores

| Company | OKX | P/S | EV/S | Op margin | Fwd P/E | EPS +1y | Rev +1y | FCF yield | LONG | SHORT |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| QUALCOMM Incorporated | `QCOM` | 4.2 | 4.3 | 18.5% | 13.5 | 26.5% | 15.7% | 5.5% | **100 CORE** | **0** |
| Rocket Lab Corporation | `RKLB` | 43.5 | 37.9 | -24.6% | 910.9 | 66.8% | 38.7% | -0.8% | **0** | **100 CORE** |
| USA Rare Earth, Inc. | `USAR` | 233.7 | 37.2 | -795.6% | 273.3 | 105.3% | 870.1% | -9.2% | **0** | **100 CORE** |
| Sandisk Corporation | `SNDK` | 5.1 | 4.9 | 79.6% | 3.6 | 26.1% | 22.3% | 7.6% | **90 CORE** | **10** |
| Taiwan Semiconductor Manufactur | `TSM` | 0.4 | 2.7 | 58.7% | 16.9 | 34.0% | 37.8% | 58.6% | **90 CORE** | **10** |
| Applied Materials, Inc. | `AMAT` | 9.5 | 9.4 | 33.7% | 19.9 | 45.0% | 35.4% | 1.0% | **85 WATCH** | **3** |
| IonQ, Inc. | `IONQ` | 51.5 | 37.3 | -408.2% | -22.0 | 23.1% | 77.6% | -0.7% | **0** | **85 CORE** |
| Applovin Corporation | `APP` | 13.4 | 13.4 | 77.7% | 13.6 | 25.5% | 24.9% | 3.5% | **83 CORE** | **10** |
| Okta, Inc. | `OKTA` | 10.9 | 10.1 | 13.3% | 43.6 | 11.4% | 10.1% | 3.1% | **8** | **80 CORE** |
| Moderna, Inc. | `MRNA` | 46.3 | 44.6 | -557.9% | -56.4 | 42.3% | 16.3% | 0.3% | **0** | **80 WATCH** |
| Nebius Group N.V. | `NBIS` | 28.4 | 30.2 | -0.2% | -39.3 | -191.4% | 266.0% | -25.0% | **0** | **80 WATCH** |
| AST SpaceMobile, Inc. | `ASTS` | 120.2 | 103.1 | -544.6% | -24.5 | 44.3% | 264.2% | -13.0% | **0** | **80 WATCH** |
| Tesla, Inc. | `TSLA` | 14.7 | 14.4 | 5.4% | 178.4 | 24.2% | 13.5% | 0.3% | **12** | **78 WATCH** |
| Marvell Technology, Inc. | `MRVL` | 15.2 | 15.0 | 16.7% | 21.8 | 73.9% | 63.7% | 1.7% | **77 WATCH** | **13** |
| Corning Incorporated | `GLW` | 5.8 | 6.2 | 18.9% | 26.2 | 34.1% | 21.1% | 0.9% | **77 WATCH** | **13** |
| Robinhood Markets, Inc. | `HOOD` | 15.5 | 15.1 | 48.1% | 25.6 | 39.7% | 29.2% | — | **77 WATCH** | **5** |
| AXT Inc | `AXT` | 18.2 | 15.9 | 38.7% | 18.7 | 116.3% | 115.9% | — | **75 WATCH** | **20** |
| Credo Technology Group Holding  | `CRDO` | 16.1 | 15.7 | 25.2% | 14.1 | 53.9% | 55.0% | 1.0% | **75 WATCH** | **28** |
| NVIDIA Corporation | `NVDA` | 16.0 | 15.8 | 66.2% | 12.6 | 70.9% | 68.2% | 0.9% | **75 WATCH** | **18** |
| Broadcom Inc. | `AVGO` | 17.4 | 17.8 | 54.3% | 16.7 | 66.9% | 64.4% | 2.0% | **75 WATCH** | **28** |
| Micron Technology, Inc. | `MU` | 6.8 | 6.5 | 80.7% | 3.8 | 17.7% | 16.2% | 3.2% | **75 CORE** | **30** |
| Western Digital Corporation | `WDC` | 8.4 | 8.3 | 47.7% | 8.0 | 63.4% | 40.5% | 2.3% | **75 WATCH** | **18** |
| Dell Technologies Inc. | `DELL` | 1.6 | 1.7 | 12.0% | 12.3 | 16.8% | 19.5% | 2.5% | **75 CORE** | **30** |
| Cerebras Systems Inc. | `CBRS` | 32.1 | 22.6 | -265.0% | 71.8 | 372.9% | 233.1% | — | **0** | **71 WATCH** |
| Advanced Micro Devices, Inc. | `AMD` | 19.3 | 18.9 | 17.2% | 30.0 | 101.8% | 77.5% | 1.1% | **70 WATCH** | **13** |
| Oracle Corporation | `ORCL` | 5.2 | 7.1 | 35.6% | 11.2 | 35.8% | 45.7% | -12.2% | **70 WATCH** | **10** |
| Adobe Inc. | `ADBE` | 3.7 | 3.8 | 34.8% | 9.1 | 12.1% | 9.1% | 9.7% | **65 WATCH** | **30** |
| XIAOMI-W | `XIAOMI` | 1.8 | 1.5 | 4.0% | 20.9 | 37.8% | 19.8% | -1.1% | **62 WATCH** | **10** |
| Coherent Corp. | `COHR` | 5.4 | 5.6 | 11.8% | 14.0 | 48.4% | 38.6% | -1.7% | **60 WATCH** | **35** |
| Microsoft Corporation | `MSFT` | 11.9 | 12.1 | 49.8% | 23.0 | 20.9% | 20.2% | 0.1% | **59 WATCH** | **3** |
| Coca-Cola Company (The) | `KO` | 8.1 | 8.6 | 33.4% | 27.2 | 5.6% | -3.1% | 1.1% | **0** | **58** |
| Meta Platforms, Inc. | `META` | 6.7 | 6.8 | 35.4% | 17.7 | 16.5% | 21.6% | 1.0% | **57 WATCH** | **38** |
| Super Micro Computer, Inc. | `SMCI` | 0.5 | 0.7 | 13.4% | 5.1 | 18.0% | 15.9% | -42.4% | **52** | **45** |
| Netflix, Inc. | `NFLX` | 5.6 | 5.7 | 34.6% | 17.6 | 5.1% | 10.7% | 9.2% | **35** | **50** |
| Palantir Technologies Inc. | `PLTR` | 56.8 | 55.3 | 46.9% | 69.2 | 46.1% | 52.1% | 0.6% | **33** | **48** |
| Bloom Energy Corporation | `BE` | 15.5 | 15.6 | 18.5% | 37.6 | 62.7% | 56.4% | -0.0% | **45** | **35** |
| SamsungElec | `SAMSUNG` | 2.2 | 2.1 | 55.0% | 2.7 | 64.7% | 40.1% | 6.4% | **45** | **10** |
| Amazon.com, Inc. | `AMZN` | 3.6 | 3.8 | 13.9% | 24.4 | -16.7% | 14.6% | -1.2% | **0** | **45** |
| Arm Holdings plc | `ARM` | 39.7 | 39.1 | 7.6% | 62.7 | 37.0% | 36.5% | 0.7% | **43** | **33** |
| Coinbase Global, Inc. | `COIN` | 7.4 | 7.0 | -1.4% | 61.3 | 819.3% | 27.1% | 9.2% | **20** | **40** |
| Lumentum Holdings Inc. | `LITE` | 15.2 | 15.0 | 28.0% | 16.1 | 57.1% | 49.2% | — | **10** | **40** |
| SOFTBANK GROUP CORP | `SOFTBANK` | 2.8 | 6.4 | -11.6% | 13.5 | -14.5% | 7.0% | -9.6% | **0** | **40** |
| IREN LIMITED | `IREN` | 12.4 | 14.8 | -102.5% | -5.5 | -16.4% | 164.0% | -48.0% | **0** | **40** |
| CoreWeave, Inc. | `CRWV` | 3.5 | 9.6 | -1.9% | -24.6 | 9.7% | 105.6% | -34.0% | **0** | **40** |
| Apple Inc. | `AAPL` | 10.6 | 10.7 | 31.1% | 32.8 | 19.6% | 8.2% | 2.1% | **25** | **38** |
| Circle Internet Group, Inc. | `CRCL` | 6.7 | 6.0 | 4.9% | 51.5 | 24.9% | 27.3% | 1.1% | **27** | **33 WATCH** |
| SK hynix | `SKHYNIX` | 3.3 | 3.4 | 79.7% | 2.4 | 47.4% | 58.8% | — | **30** | **5** |
| SK hynix | `SKHY` | 3.3 | 3.4 | 79.7% | 2.4 | 47.4% | 58.8% | — | **30** | **5** |
| Alphabet Inc. | `GOOGL` | 7.5 | 7.3 | 31.8% | 18.6 | -24.1% | 27.0% | -0.0% | **5** | **30** |
| Intel Corporation | `INTC` | 5.2 | 5.4 | 15.6% | 32.4 | 21.0% | 12.0% | 0.3% | **5** | **28** |
| Fluence Energy, Inc. | `FLNC` | 0.4 | 0.4 | -8.9% | -11.4 | 59.3% | 25.4% | 0.2% | **5** | **28** |
| Hyperliquid Strategies Inc | `PURR` | 285.0 | 188.1 | 9595.1% | 26.2 | 51.0% | 31.4% | — | **25** | **10** |
| BitMine Immersion Technologies, | `BMNR` | 214.2 | 208.7 | 8.4% | 23.1 | 103.2% | 421.8% | -4.0% | **25** | **25** |
| Strategy Inc | `MSTR` | 121.9 | 149.7 | -2.1% | 8.6 | 481.5% | 3.4% | -5.4% | **25** | **25** |
| Applied Optoelectronics, Inc. | `AAOI` | 8.4 | 8.1 | -12.9% | 12.9 | 576.8% | 156.5% | -17.6% | **10** | **25** |

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
