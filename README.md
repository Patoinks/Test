# OKX Long / Short Fundamental Scanner

Hourly scanner restricted to public companies exposed by the **OKX EEA TradFi / Stock Perpetual API universe**.

**Last scan:** 2026-11-25 17:22 UTC  
**Availability scope:** user-confirmed OKX EEA Stock Futures / X-Perp  
**OKX stock/ETF markets in configured universe:** 72  
**Public companies analysed:** 55  
**SHORT CORE:** 2  
**LONG CORE:** 8

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
| 1 | Sandisk Corporation | SNDK | -26.0% | -28.0% | -27.0% | 90 | +20 | **100** | **CORE** | yes |
| 2 | Marvell Technology, Inc. | MRVL | -6.2% | -15.2% | -10.7% | 90 | +9 | **99** | **CORE** | yes |
| 3 | Advanced Micro Devices, Inc. | AMD | -5.8% | -26.6% | -16.2% | 84 | +13 | **97** | **CORE** | yes |
| 4 | Taiwan Semiconductor Manufactur | TSM | -5.1% | -8.6% | -6.9% | 88 | +6 | **94** | **CORE** | yes |
| 5 | Credo Technology Group Holding  | CRDO | -6.2% | -18.8% | -12.5% | 82 | +10 | **92** | **CORE** | yes |
| 6 | Robinhood Markets, Inc. | HOOD | -3.4% | -8.3% | -5.8% | 86 | +5 | **91** | **CORE** | yes |
| 7 | AXT Inc | AXT | -6.0% | -16.6% | -11.3% | 82 | +9 | **91** | **CORE** | yes |
| 8 | Broadcom Inc. | AVGO | -4.2% | -18.5% | -11.3% | 82 | +9 | **91** | **CORE** | yes |
| 9 | NVIDIA Corporation | NVDA | -6.5% | -3.8% | -5.2% | 85 | +4 | **89** | **CORE** | yes |
| 10 | Western Digital Corporation | WDC | -6.7% | -11.3% | -9.0% | 82 | +7 | **89** | **CORE** | yes |

## Final model + Price Timing — SHORT

| Rank | Company | OKX | 24h | 7d | 50/50 move | Base SHORT | Timing adj. | Final | Signal | Prev. SHORT? |
|---:|---|---|---:|---:|---:|---:|---:|---:|---|---|
| 1 | Moderna, Inc. | MRNA | -3.1% | 11.9% | 4.4% | 94 | +4 | **98** | **CORE** | yes |
| 2 | Rocket Lab Corporation | RKLB | -2.8% | -15.8% | -9.3% | 100 | -7 | **93** | **CORE** | yes |
| 3 | USA Rare Earth, Inc. | USAR | -5.4% | -3.7% | -4.5% | 86 | -4 | **82** | **CORE** | yes |
| 4 | AST SpaceMobile, Inc. | ASTS | 4.2% | -3.6% | 0.3% | 80 | +0 | **80** | **CORE** | yes |
| 5 | IonQ, Inc. | IONQ | -1.1% | -5.7% | -3.4% | 67 | -3 | **64** | **WATCH** | yes |
| 6 | Cerebras Systems Inc. | CBRS | -2.3% | -7.9% | -5.1% | 67 | -4 | **63** | **WATCH** | yes |
| 7 | Okta, Inc. | OKTA | -2.6% | -1.4% | -2.0% | 60 | -2 | **58** | **WATCH** | yes |
| 8 | Tesla, Inc. | TSLA | -4.3% | -4.0% | -4.1% | 59 | -3 | **56** | **WATCH** | yes |

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
| 8 | Western Digital Corporation | `WDC` | 83 | 80 | **82** | **CORE** |
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
| 5 | IonQ, Inc. | `IONQ` | 67 | 0 | **67** | **WATCH** |
| 6 | Cerebras Systems Inc. | `CBRS` | 67 | 0 | **67** | **WATCH** |
| 7 | Okta, Inc. | `OKTA` | 80 | 13 | **60** | **WATCH** |
| 8 | Tesla, Inc. | `TSLA` | 78 | 15 | **59** | **WATCH** |

## P/E Compression + Growth — LONG

| Rank | Company | OKX | Trail P/E | Fwd P/E | P/E change | EPS +1y | Rev +1y | Rev trend | LONG score | Signal |
|---:|---|---|---:|---:|---:|---:|---:|---|---:|---|
| 1 | Marvell Technology, Inc. | `MRVL` | 40.6 | 16.7 | -58.8% | 74.9% | 63.9% | accelerating | **100** | **CORE** |
| 2 | Advanced Micro Devices, Inc. | `AMD` | 83.2 | 22.1 | -73.5% | 117.9% | 83.4% | accelerating | **100** | **CORE** |
| 3 | Credo Technology Group Holding  | `CRDO` | 35.4 | 10.3 | -71.0% | 53.9% | 55.0% | decelerating | **100** | **CORE** |
| 4 | AXT Inc | `AXT` | 60.6 | 11.7 | -80.8% | 116.3% | 111.5% | decelerating | **100** | **CORE** |
| 5 | Broadcom Inc. | `AVGO` | 36.9 | 14.9 | -59.6% | 65.9% | 64.8% | decelerating | **100** | **CORE** |
| 6 | Coherent Corp. | `COHR` | 38.2 | 11.7 | -69.3% | 52.1% | 39.1% | decelerating | **100** | **CORE** |
| 7 | Bloom Energy Corporation | `BE` | 87.4 | 26.9 | -69.2% | 63.8% | 58.8% | decelerating | **96** | **CORE** |
| 8 | Oracle Corporation | `ORCL` | 16.2 | 9.3 | -42.3% | 35.7% | 45.7% | accelerating | **95** | **CORE** |
| 9 | Arm Holdings plc | `ARM` | 178.5 | 50.3 | -71.8% | 36.2% | 37.2% | accelerating | **95** | **CORE** |
| 10 | Sandisk Corporation | `SNDK` | 4.5 | 1.9 | -56.4% | 26.1% | 23.7% | decelerating | **90** | **CORE** |

## P/E Expansion + Weakening — SHORT

| Rank | Company | OKX | Trail P/E | Fwd P/E | P/E change | EPS +1y | Rev +1y | Rev trend | SHORT score | Signal |
|---:|---|---|---:|---:|---:|---:|---:|---|---:|---|
| 1 | Hyperliquid Strategies Inc | `PURR` | 3.1 | 35.4 | 1051.2% | -79.8% | 22.8% | decelerating | **80** | **CORE** |
| 2 | Alphabet Inc. | `GOOGL` | 14.1 | 17.7 | 25.2% | -23.8% | 27.4% | accelerating | **50** | **WATCH** |

## Top SHORT candidates

| Rank | Company | OKX market | SHORT score | Signal | P/S | EV/S | Op margin | Fwd P/E | Rev +1y | FCF yield |
|---:|---|---|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Rocket Lab Corporation | `RKLB-USDT-SWAP` | **100** | **WATCH** | 34.1 | 27.9 | -27.6% | 624.5 | 36.6% | -0.7% |
| 2 | Moderna, Inc. | `MRNA-USDT-SWAP` | **94** | **WATCH** | 35.3 | 36.1 | -80.8% | -52.6 | 11.3% | -0.7% |
| 3 | USA Rare Earth, Inc. | `USAR-USDT-SWAP` | **86** | **CORE** | 146.7 | 129.2 | -984.3% | 26.9 | 1039.1% | -10.8% |
| 4 | Okta, Inc. | `OKTA-USDT-SWAP` | **80** | **CORE** | 11.0 | 10.5 | 7.7% | 44.1 | 10.1% | 3.1% |
| 5 | AST SpaceMobile, Inc. | `ASTS-USDT-SWAP` | **80** | **WATCH** | 68.9 | 62.0 | -393.3% | -15.7 | 252.7% | -19.2% |
| 6 | IonQ, Inc. | `IONQ-USDT-SWAP` | **67** | **WATCH** | 26.9 | 23.1 | -306.3% | -15.6 | 71.2% | -1.2% |
| 7 | Cerebras Systems Inc. | `CBRS-USDT-SWAP` | **67** | **WATCH** | 27.9 | 20.7 | -99.3% | 46.7 | 214.4% | — |

## Top LONG candidates

| Rank | Company | OKX market | LONG score | Signal | P/S | EV/S | Op margin | Fwd P/E | Rev +1y | FCF yield |
|---:|---|---|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | QUALCOMM Incorporated | `QCOM-USDT-SWAP` | **100** | **CORE** | 4.1 | 4.3 | 20.8% | 13.4 | 15.4% | 5.2% |
| 2 | Taiwan Semiconductor Manufactur | `TSM-USDT-SWAP` | **90** | **CORE** | 0.3 | 2.3 | 58.0% | 14.2 | 37.9% | 60.7% |
| 3 | Sandisk Corporation | `SNDK-USDT-SWAP` | **90** | **CORE** | 2.7 | 2.9 | 72.7% | 1.9 | 23.7% | 14.1% |
| 4 | Robinhood Markets, Inc. | `HOOD-USDT-SWAP` | **85** | **WATCH** | 11.2 | 11.2 | 45.7% | 18.6 | 29.4% | — |
| 5 | Marvell Technology, Inc. | `MRVL-USDT-SWAP` | **85** | **WATCH** | 11.8 | 12.4 | 16.8% | 16.7 | 63.9% | 2.2% |
| 6 | Applovin Corporation | `APP-USDT-SWAP` | **83** | **CORE** | 16.3 | 16.6 | 77.8% | 17.9 | 25.7% | 3.0% |
| 7 | NVIDIA Corporation | `NVDA-USDT-SWAP` | **83** | **CORE** | 9.7 | 10.2 | 66.1% | 8.7 | 71.4% | 2.8% |
| 8 | Western Digital Corporation | `WDC-USDT-SWAP` | **83** | **CORE** | 6.6 | 7.1 | 40.9% | 6.4 | 39.6% | 2.9% |
| 9 | Corning Incorporated | `GLW-USDT-SWAP` | **77** | **WATCH** | 4.7 | 5.4 | 16.8% | 21.2 | 21.2% | 1.0% |
| 10 | Advanced Micro Devices, Inc. | `AMD-USDT-SWAP` | **77** | **WATCH** | 14.2 | 14.8 | 17.8% | 22.1 | 83.4% | 1.1% |

## Analyst consensus (12-month price target) — most upside

| Rank | Company | OKX | Price | Analyst mean target | Gap | Analysts | Currency |
|---:|---|---|---:|---:|---:|---:|---|
| 1 | SK hynix | `SKHYNIX` | 1030000.00 | 2977665.20 | **189.1%** | 39 | KRW |
| 2 | CoreWeave, Inc. | `CRWV` | 39.84 | 114.55 | **187.5%** | 38 | USD |
| 3 | Nebius Group N.V. | `NBIS` | 80.89 | 231.60 | **186.3%** | 20 | USD |
| 4 | AXT Inc | `AXT` | 29.69 | 82.77 | **178.8%** | 7 | USD |
| 5 | Credo Technology Group Holding  | `CRDO` | 99.84 | 274.31 | **174.7%** | 19 | USD |
| 6 | SamsungElec | `SAMSUNG` | 170700.00 | 459028.56 | **168.9%** | 35 | KRW |
| 7 | Micron Technology, Inc. | `MU` | 569.79 | 1529.69 | **168.5%** | 45 | USD |
| 8 | SOFTBANK GROUP CORP | `SOFTBANK` | 2696.50 | 6953.47 | **157.9%** | 18 | JPY |
| 9 | AST SpaceMobile, Inc. | `ASTS` | 24.58 | 63.35 | **157.7%** | 12 | USD |
| 10 | IonQ, Inc. | `IONQ` | 22.14 | 54.27 | **145.1%** | 14 | USD |
| 11 | Marvell Technology, Inc. | `MRVL` | 123.47 | 301.02 | **143.8%** | 40 | USD |
| 12 | Cerebras Systems Inc. | `CBRS` | 86.72 | 210.18 | **142.4%** | 11 | USD |
| 13 | Western Digital Corporation | `WDC` | 255.50 | 600.46 | **135.0%** | 24 | USD |
| 14 | Lumentum Holdings Inc. | `LITE` | 451.30 | 1048.34 | **132.3%** | 26 | USD |
| 15 | Oracle Corporation | `ORCL` | 103.15 | 236.18 | **129.0%** | 40 | USD |

## Analyst consensus (12-month price target) — most downside

| Rank | Company | OKX | Price | Analyst mean target | Gap | Analysts | Currency |
|---:|---|---|---:|---:|---:|---:|---|
| 1 | Moderna, Inc. | `MRNA` | 220.24 | 163.74 | **-25.7%** | 19 | USD |
| 2 | Apple Inc. | `AAPL` | 352.14 | 345.63 | **-1.8%** | 39 | USD |

Price/target uses the underlying Yahoo Finance share quote, not the OKX derivative. Minimum 3 analysts; unreliable price scales and missing coverage excluded. Targets are analyst opinions, not guaranteed forecasts.

## All OKX companies — our ratio + LONG/SHORT scores

| Company | OKX | P/S | EV/S | Op margin | Fwd P/E | EPS +1y | Rev +1y | FCF yield | LONG | SHORT |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| QUALCOMM Incorporated | `QCOM` | 4.1 | 4.3 | 20.8% | 13.4 | 26.6% | 15.4% | 5.2% | **100 CORE** | **0** |
| Rocket Lab Corporation | `RKLB` | 34.1 | 27.9 | -27.6% | 624.5 | 77.8% | 36.6% | -0.7% | **0** | **100 WATCH** |
| Moderna, Inc. | `MRNA` | 35.3 | 36.1 | -80.8% | -52.6 | 39.0% | 11.3% | -0.7% | **0** | **94 WATCH** |
| Sandisk Corporation | `SNDK` | 2.7 | 2.9 | 72.7% | 1.9 | 26.1% | 23.7% | 14.1% | **90 CORE** | **10** |
| Taiwan Semiconductor Manufactur | `TSM` | 0.3 | 2.3 | 58.0% | 14.2 | 33.6% | 37.9% | 60.7% | **90 CORE** | **10** |
| USA Rare Earth, Inc. | `USAR` | 146.7 | 129.2 | -984.3% | 26.9 | 125.8% | 1039.1% | -10.8% | **0** | **86 CORE** |
| Marvell Technology, Inc. | `MRVL` | 11.8 | 12.4 | 16.8% | 16.7 | 74.9% | 63.9% | 2.2% | **85 WATCH** | **13** |
| Robinhood Markets, Inc. | `HOOD` | 11.2 | 11.2 | 45.7% | 18.6 | 39.7% | 29.4% | — | **85 WATCH** | **0** |
| NVIDIA Corporation | `NVDA` | 9.7 | 10.2 | 66.1% | 8.7 | 71.7% | 71.4% | 2.8% | **83 CORE** | **10** |
| Western Digital Corporation | `WDC` | 6.6 | 7.1 | 40.9% | 6.4 | 61.7% | 39.6% | 2.9% | **83 CORE** | **10** |
| Applovin Corporation | `APP` | 16.3 | 16.6 | 77.8% | 17.9 | 27.6% | 25.7% | 3.0% | **83 CORE** | **10** |
| Okta, Inc. | `OKTA` | 11.0 | 10.5 | 7.7% | 44.1 | 11.5% | 10.1% | 3.1% | **8** | **80 CORE** |
| AST SpaceMobile, Inc. | `ASTS` | 68.9 | 62.0 | -393.3% | -15.7 | 28.1% | 252.7% | -19.2% | **0** | **80 WATCH** |
| Tesla, Inc. | `TSLA` | 14.1 | 14.4 | 3.0% | 170.6 | 25.2% | 13.4% | 0.3% | **20** | **78** |
| Advanced Micro Devices, Inc. | `AMD` | 14.2 | 14.8 | 17.8% | 22.1 | 117.9% | 83.4% | 1.1% | **77 WATCH** | **13** |
| Micron Technology, Inc. | `MU` | 4.8 | 5.1 | 74.6% | 2.8 | 16.4% | 14.9% | 4.5% | **77 CORE** | **30** |
| Corning Incorporated | `GLW` | 4.7 | 5.4 | 16.8% | 21.2 | 34.8% | 21.2% | 1.0% | **77 WATCH** | **3** |
| Credo Technology Group Holding  | `CRDO` | 11.8 | 12.1 | 31.7% | 10.3 | 53.9% | 55.0% | 1.3% | **75 WATCH** | **18** |
| AXT Inc | `AXT` | 11.4 | 9.8 | 19.6% | 11.7 | 116.3% | 111.5% | 1.0% | **75 WATCH** | **28** |
| Broadcom Inc. | `AVGO` | 15.5 | 16.5 | 48.8% | 14.9 | 65.9% | 64.8% | 2.2% | **75 WATCH** | **18** |
| Applied Materials, Inc. | `AMAT` | 6.9 | 7.4 | 32.9% | 12.3 | 27.2% | 20.4% | 1.1% | **75 WATCH** | **18** |
| Dell Technologies Inc. | `DELL` | 1.2 | 1.4 | 9.9% | 9.3 | 17.9% | 19.7% | 3.3% | **75 CORE** | **30** |
| Oracle Corporation | `ORCL` | 4.5 | 6.5 | 34.3% | 9.3 | 35.7% | 45.7% | -14.3% | **70 WATCH** | **10** |
| XIAOMI-W | `XIAOMI` | 1.6 | 1.4 | 3.3% | 18.2 | 42.0% | 19.1% | -5.4% | **70 WATCH** | **10** |
| Microsoft Corporation | `MSFT` | 10.4 | 10.8 | 47.1% | 20.1 | 21.0% | 20.7% | 0.1% | **69 WATCH** | **3** |
| IonQ, Inc. | `IONQ` | 26.9 | 23.1 | -306.3% | -15.6 | -41.0% | 71.2% | -1.2% | **0** | **67 WATCH** |
| Cerebras Systems Inc. | `CBRS` | 27.9 | 20.7 | -99.3% | 46.7 | 543.0% | 214.4% | — | **0** | **67 WATCH** |
| Adobe Inc. | `ADBE` | 3.5 | 3.5 | 36.3% | 8.6 | 12.0% | 9.1% | 10.2% | **65 WATCH** | **30** |
| Coherent Corp. | `COHR` | 4.6 | 5.3 | 14.1% | 11.7 | 52.1% | 39.1% | -4.6% | **60 WATCH** | **25** |
| Apple Inc. | `AAPL` | 10.7 | 10.8 | 33.0% | 33.3 | 12.4% | 8.1% | 2.1% | **5** | **58** |
| Coca-Cola Company (The) | `KO` | 8.3 | 8.8 | 32.2% | 27.8 | 5.5% | -3.0% | 1.0% | **0** | **58** |
| Meta Platforms, Inc. | `META` | 6.3 | 6.4 | 37.8% | 16.7 | 16.3% | 21.9% | 1.1% | **57 WATCH** | **38** |
| Arm Holdings plc | `ARM` | 30.4 | 31.1 | 17.0% | 50.3 | 36.2% | 37.2% | 0.7% | **55 WATCH** | **33** |
| IREN LIMITED | `IREN` | 7.4 | 17.5 | -72.9% | 45.0 | 116.3% | 200.8% | — | **0** | **55** |
| Bloom Energy Corporation | `BE` | 11.1 | 12.2 | 14.3% | 26.9 | 63.8% | 58.8% | -0.0% | **52** | **35** |
| Netflix, Inc. | `NFLX` | 4.8 | 5.0 | 31.3% | 15.5 | 5.4% | 10.7% | 10.6% | **35** | **50** |
| Palantir Technologies Inc. | `PLTR` | 52.8 | 51.9 | 45.6% | 62.9 | 49.2% | 53.7% | 0.7% | **45** | **48** |
| SamsungElec | `SAMSUNG` | 1.9 | 1.6 | 46.1% | 2.2 | 62.7% | 40.9% | 10.6% | **45** | **10** |
| Super Micro Computer, Inc. | `SMCI` | 0.3 | 0.4 | 8.3% | 3.2 | 6.5% | 11.3% | -56.1% | **35** | **45** |
| Circle Internet Group, Inc. | `CRCL` | 3.9 | 3.5 | 11.3% | 32.1 | 0.5% | 24.1% | 2.2% | **20** | **43** |
| Nebius Group N.V. | `NBIS` | 10.8 | 15.6 | -18.7% | -26.6 | -1706.3% | 289.8% | -86.1% | **0** | **40** |
| CoreWeave, Inc. | `CRWV` | 2.2 | 8.7 | -0.5% | -22.4 | 23.4% | 106.9% | -88.7% | **0** | **40** |
| SOFTBANK GROUP CORP | `SOFTBANK` | 1.9 | 5.4 | -6.3% | 9.1 | 156.6% | 6.0% | -6.7% | **0** | **40** |
| Coinbase Global, Inc. | `COIN` | 4.9 | 4.6 | 0.1% | 41.6 | 1001.9% | 25.7% | 13.9% | **35** | **25** |
| Fluence Energy, Inc. | `FLNC` | 0.4 | 0.3 | -14.8% | -8.3 | 100.8% | 30.4% | -55.8% | **0** | **35** |
| SK hynix | `SKHYNIX` | 2.7 | 2.4 | 74.5% | 1.9 | 49.0% | 60.6% | — | **30** | **5** |
| Lumentum Holdings Inc. | `LITE` | 10.9 | 11.7 | 23.4% | 11.2 | 60.9% | 58.5% | 0.3% | **30** | **23** |
| SK hynix | `SKHY` | 2.7 | 2.4 | 74.5% | 1.9 | 49.0% | 60.6% | — | **30** | **5** |
| Alphabet Inc. | `GOOGL` | 7.0 | 7.1 | 33.3% | 17.7 | -23.8% | 27.4% | -0.0% | **5** | **30** |
| Amazon.com, Inc. | `AMZN` | 3.3 | 3.7 | 13.1% | 22.3 | -16.6% | 15.8% | -1.3% | **0** | **30** |
| Intel Corporation | `INTC` | 4.6 | 5.1 | 10.3% | 28.8 | 20.4% | 12.0% | 0.3% | **12** | **28** |
| BitMine Immersion Technologies, | `BMNR` | 63.3 | 64.0 | -216.3% | 13.4 | 105.7% | 197.6% | -1.3% | **25** | **25** |
| Strategy Inc | `MSTR` | 64.3 | 94.3 | -1100.1% | 4.3 | 417.1% | 3.1% | -10.2% | **25** | **25** |
| Applied Optoelectronics, Inc. | `AAOI` | 4.3 | 4.3 | -6.8% | 10.4 | 383.4% | 135.1% | -41.2% | **10** | **25** |
| Hyperliquid Strategies Inc | `PURR` | 92.9 | 87.0 | 6252.0% | 35.4 | -79.8% | 22.8% | — | **0** | **25** |

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
