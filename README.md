# OKX Long / Short Fundamental Scanner

Hourly scanner restricted to public companies exposed by the **OKX EEA TradFi / Stock Perpetual API universe**.

**Last scan:** 2026-11-22 00:24 UTC  
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
| 1 | Marvell Technology, Inc. | MRVL | 0.0% | -22.0% | -11.0% | 90 | +9 | **99** | **CORE** | yes |
| 2 | Taiwan Semiconductor Manufactur | TSM | 0.0% | -20.1% | -10.0% | 88 | +8 | **96** | **CORE** | yes |
| 3 | Robinhood Markets, Inc. | HOOD | 0.0% | -20.2% | -10.1% | 86 | +8 | **94** | **CORE** | yes |
| 4 | NVIDIA Corporation | NVDA | 0.0% | -22.9% | -11.5% | 85 | +9 | **94** | **CORE** | yes |
| 5 | AXT Inc | AXT | 0.0% | -26.9% | -13.5% | 82 | +11 | **93** | **CORE** | yes |
| 6 | Sandisk Corporation | SNDK | -16.1% | -28.4% | -22.2% | 75 | +18 | **93** | **CORE** | yes |
| 7 | Advanced Micro Devices, Inc. | AMD | -0.0% | -20.5% | -10.3% | 84 | +8 | **92** | **CORE** | yes |
| 8 | Credo Technology Group Holding  | CRDO | -0.0% | -24.1% | -12.0% | 82 | +10 | **92** | **CORE** | yes |
| 9 | Micron Technology, Inc. | MU | -0.0% | -23.6% | -11.8% | 82 | +9 | **91** | **CORE** | yes |
| 10 | QUALCOMM Incorporated | QCOM | -0.0% | -13.1% | -6.5% | 85 | +5 | **90** | **CORE** | yes |

## Final model + Price Timing — SHORT

| Rank | Company | OKX | 24h | 7d | 50/50 move | Base SHORT | Timing adj. | Final | Signal | Prev. SHORT? |
|---:|---|---|---:|---:|---:|---:|---:|---:|---|---|
| 1 | Rocket Lab Corporation | RKLB | 0.0% | -26.2% | -13.1% | 100 | -10 | **90** | **CORE** | yes |
| 2 | Moderna, Inc. | MRNA | 0.0% | -12.7% | -6.4% | 94 | -5 | **89** | **CORE** | yes |
| 3 | USA Rare Earth, Inc. | USAR | 0.0% | -23.2% | -11.6% | 86 | -9 | **77** | **CORE** | yes |
| 4 | AST SpaceMobile, Inc. | ASTS | -0.0% | -28.6% | -14.3% | 80 | -11 | **69** | **WATCH** | yes |
| 5 | Okta, Inc. | OKTA | -0.0% | 4.7% | 2.3% | 60 | +2 | **62** | **WATCH** | yes |
| 6 | IonQ, Inc. | IONQ | 0.0% | -28.3% | -14.1% | 67 | -11 | **56** | **WATCH** | yes |

## Combined model — LONG

Weighted score: **70% fundamental + 30% P/E trend**.

| Rank | Company | OKX | Fundamental LONG | P/E trend LONG | Combined | Signal |
|---:|---|---|---:|---:|---:|---|
| 1 | Marvell Technology, Inc. | `MRVL` | 85 | 100 | **90** | **CORE** |
| 2 | Taiwan Semiconductor Manufactur | `TSM` | 90 | 85 | **88** | **CORE** |
| 3 | Robinhood Markets, Inc. | `HOOD` | 85 | 90 | **86** | **CORE** |
| 4 | QUALCOMM Incorporated | `QCOM` | 100 | 50 | **85** | **CORE** |
| 5 | NVIDIA Corporation | `NVDA` | 83 | 90 | **85** | **CORE** |
| 6 | Advanced Micro Devices, Inc. | `AMD` | 77 | 100 | **84** | **CORE** |
| 7 | Western Digital Corporation | `WDC` | 83 | 80 | **82** | **CORE** |
| 8 | Micron Technology, Inc. | `MU` | 82 | 82 | **82** | **CORE** |
| 9 | AXT Inc | `AXT` | 75 | 100 | **82** | **CORE** |
| 10 | Credo Technology Group Holding  | `CRDO` | 75 | 100 | **82** | **CORE** |

## Combined model — SHORT

Weighted score: **70% fundamental + 30% P/E trend**.

| Rank | Company | OKX | Fundamental SHORT | P/E trend SHORT | Combined | Signal |
|---:|---|---|---:|---:|---:|---|
| 1 | Rocket Lab Corporation | `RKLB` | 100 | 0 | **100** | **WATCH** |
| 2 | Moderna, Inc. | `MRNA` | 94 | 0 | **94** | **WATCH** |
| 3 | USA Rare Earth, Inc. | `USAR` | 86 | 0 | **86** | **CORE** |
| 4 | AST SpaceMobile, Inc. | `ASTS` | 80 | 0 | **80** | **WATCH** |
| 5 | IonQ, Inc. | `IONQ` | 67 | 0 | **67** | **WATCH** |
| 6 | Okta, Inc. | `OKTA` | 80 | 13 | **60** | **WATCH** |
| 7 | Tesla, Inc. | `TSLA` | 78 | 15 | **59** | **WATCH** |

## P/E Compression + Growth — LONG

| Rank | Company | OKX | Trail P/E | Fwd P/E | P/E change | EPS +1y | Rev +1y | Rev trend | LONG score | Signal |
|---:|---|---|---:|---:|---:|---:|---:|---|---:|---|
| 1 | Marvell Technology, Inc. | `MRVL` | 40.2 | 16.6 | -58.8% | 74.7% | 64.3% | accelerating | **100** | **CORE** |
| 2 | AXT Inc | `AXT` | 62.4 | 12.0 | -80.8% | 116.3% | 111.5% | decelerating | **100** | **CORE** |
| 3 | Advanced Micro Devices, Inc. | `AMD` | 90.7 | 24.1 | -73.5% | 118.2% | 83.6% | accelerating | **100** | **CORE** |
| 4 | Credo Technology Group Holding  | `CRDO` | 35.4 | 10.3 | -71.0% | 53.9% | 55.0% | decelerating | **100** | **CORE** |
| 5 | Broadcom Inc. | `AVGO` | 38.9 | 15.7 | -59.7% | 66.1% | 65.0% | decelerating | **100** | **CORE** |
| 6 | Coherent Corp. | `COHR` | 38.8 | 11.9 | -69.4% | 52.1% | 39.1% | decelerating | **100** | **CORE** |
| 7 | Arm Holdings plc | `ARM` | 174.9 | 49.3 | -71.8% | 36.2% | 37.2% | accelerating | **97** | **CORE** |
| 8 | Bloom Energy Corporation | `BE` | 86.3 | 26.7 | -69.0% | 62.4% | 56.4% | decelerating | **96** | **CORE** |
| 9 | Oracle Corporation | `ORCL` | 15.9 | 9.2 | -42.3% | 35.7% | 45.7% | accelerating | **95** | **CORE** |
| 10 | NVIDIA Corporation | `NVDA` | 13.5 | 7.6 | -43.9% | 71.7% | 71.2% | decelerating | **90** | **CORE** |

## P/E Expansion + Weakening — SHORT

| Rank | Company | OKX | Trail P/E | Fwd P/E | P/E change | EPS +1y | Rev +1y | Rev trend | SHORT score | Signal |
|---:|---|---|---:|---:|---:|---:|---:|---|---:|---|
| 1 | Hyperliquid Strategies Inc | `PURR` | 3.2 | 36.5 | 1051.2% | -79.8% | 22.8% | decelerating | **80** | **CORE** |
| 2 | Sandisk Corporation | `SNDK` | 0.1 | 2.2 | 2473.0% | 26.1% | 23.7% | decelerating | **55** | **WATCH** |
| 3 | Alphabet Inc. | `GOOGL` | 13.9 | 17.3 | 25.2% | -23.8% | 27.4% | accelerating | **50** | **WATCH** |

## Top SHORT candidates

| Rank | Company | OKX market | SHORT score | Signal | P/S | EV/S | Op margin | Fwd P/E | Rev +1y | FCF yield |
|---:|---|---|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Rocket Lab Corporation | `RKLB-USDT-SWAP` | **100** | **WATCH** | 34.7 | 27.5 | -27.6% | 634.5 | 37.0% | -0.7% |
| 2 | Moderna, Inc. | `MRNA-USDT-SWAP` | **94** | **WATCH** | 31.2 | 30.9 | -80.8% | -46.6 | 11.3% | -0.7% |
| 3 | USA Rare Earth, Inc. | `USAR-USDT-SWAP` | **86** | **CORE** | 145.6 | 119.6 | -984.3% | 26.7 | 1039.1% | -10.9% |
| 4 | Okta, Inc. | `OKTA-USDT-SWAP` | **80** | **CORE** | 10.9 | 10.2 | 7.7% | 43.7 | 10.1% | 3.1% |
| 5 | AST SpaceMobile, Inc. | `ASTS-USDT-SWAP` | **80** | **WATCH** | 65.3 | 61.3 | -393.3% | -17.1 | 252.7% | -20.3% |
| 6 | IonQ, Inc. | `IONQ-USDT-SWAP` | **67** | **WATCH** | 25.2 | 21.2 | -306.3% | -14.6 | 71.2% | -1.3% |

## Top LONG candidates

| Rank | Company | OKX market | LONG score | Signal | P/S | EV/S | Op margin | Fwd P/E | Rev +1y | FCF yield |
|---:|---|---|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | QUALCOMM Incorporated | `QCOM-USDT-SWAP` | **100** | **CORE** | 3.7 | 3.9 | 20.8% | 12.3 | 15.4% | 5.7% |
| 2 | Taiwan Semiconductor Manufactur | `TSM-USDT-SWAP` | **90** | **CORE** | 0.3 | 2.1 | 58.0% | 13.6 | 37.9% | 63.1% |
| 3 | Sandisk Corporation | `SNDK-USDT-SWAP` | **90** | **CORE** | 3.1 | 2.9 | 72.7% | 2.2 | 23.7% | 12.5% |
| 4 | Robinhood Markets, Inc. | `HOOD-USDT-SWAP` | **85** | **WATCH** | 11.0 | 10.6 | 45.7% | 18.2 | 29.4% | — |
| 5 | Marvell Technology, Inc. | `MRVL-USDT-SWAP` | **85** | **WATCH** | 11.6 | 11.5 | 16.8% | 16.6 | 64.3% | 2.2% |
| 6 | Applovin Corporation | `APP-USDT-SWAP` | **83** | **CORE** | 15.2 | 15.2 | 77.8% | 16.7 | 25.5% | 3.2% |
| 7 | NVIDIA Corporation | `NVDA-USDT-SWAP` | **83** | **CORE** | 8.4 | 8.2 | 66.1% | 7.6 | 71.2% | 3.3% |
| 8 | Western Digital Corporation | `WDC-USDT-SWAP` | **83** | **CORE** | 6.7 | 6.7 | 40.9% | 6.5 | 40.5% | 2.8% |
| 9 | Micron Technology, Inc. | `MU-USDT-SWAP` | **82** | **CORE** | 5.1 | 4.8 | 74.6% | 2.8 | 16.2% | 4.3% |
| 10 | Corning Incorporated | `GLW-USDT-SWAP` | **77** | **WATCH** | 4.6 | 5.0 | 16.8% | 20.7 | 21.2% | 1.1% |

## Analyst consensus (12-month price target) — most upside

| Rank | Company | OKX | Price | Analyst mean target | Gap | Analysts | Currency |
|---:|---|---|---:|---:|---:|---:|---|
| 1 | Strategy Inc | `MSTR` | 77.80 | 233.27 | **199.8%** | 15 | USD |
| 2 | CoreWeave, Inc. | `CRWV` | 39.51 | 115.08 | **191.3%** | 38 | USD |
| 3 | Nebius Group N.V. | `NBIS` | 81.31 | 231.60 | **184.8%** | 20 | USD |
| 4 | Credo Technology Group Holding  | `CRDO` | 99.86 | 274.31 | **174.7%** | 19 | USD |
| 5 | SK hynix | `SKHYNIX` | 1113000.00 | 3056126.80 | **174.6%** | 39 | KRW |
| 6 | AST SpaceMobile, Inc. | `ASTS` | 23.27 | 63.35 | **172.2%** | 12 | USD |
| 7 | AXT Inc | `AXT` | 30.57 | 82.77 | **170.8%** | 7 | USD |
| 8 | Micron Technology, Inc. | `MU` | 594.51 | 1561.91 | **162.7%** | 45 | USD |
| 9 | IonQ, Inc. | `IONQ` | 20.72 | 54.27 | **161.9%** | 14 | USD |
| 10 | SamsungElec | `SAMSUNG` | 183100.00 | 471857.16 | **157.7%** | 35 | KRW |
| 11 | Cerebras Systems Inc. | `CBRS` | 82.67 | 210.18 | **154.2%** | 11 | USD |
| 12 | Marvell Technology, Inc. | `MRVL` | 122.28 | 309.14 | **152.8%** | 40 | USD |
| 13 | Western Digital Corporation | `WDC` | 261.11 | 613.38 | **134.9%** | 24 | USD |
| 14 | SOFTBANK GROUP CORP | `SOFTBANK` | 3025.00 | 7064.58 | **133.5%** | 18 | JPY |
| 15 | Oracle Corporation | `ORCL` | 101.19 | 236.18 | **133.4%** | 40 | USD |

## Analyst consensus (12-month price target) — most downside

| Rank | Company | OKX | Price | Analyst mean target | Gap | Analysts | Currency |
|---:|---|---|---:|---:|---:|---:|---|
| 1 | Moderna, Inc. | `MRNA` | 195.00 | 164.53 | **-15.6%** | 19 | USD |

Price/target uses the underlying Yahoo Finance share quote, not the OKX derivative. Minimum 3 analysts; unreliable price scales and missing coverage excluded. Targets are analyst opinions, not guaranteed forecasts.

## All OKX companies — our ratio + LONG/SHORT scores

| Company | OKX | P/S | EV/S | Op margin | Fwd P/E | EPS +1y | Rev +1y | FCF yield | LONG | SHORT |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| QUALCOMM Incorporated | `QCOM` | 3.7 | 3.9 | 20.8% | 12.3 | 26.6% | 15.4% | 5.7% | **100 CORE** | **0** |
| Rocket Lab Corporation | `RKLB` | 34.7 | 27.5 | -27.6% | 634.5 | 75.2% | 37.0% | -0.7% | **0** | **100 WATCH** |
| Moderna, Inc. | `MRNA` | 31.2 | 30.9 | -80.8% | -46.6 | 39.0% | 11.3% | -0.7% | **0** | **94 WATCH** |
| Taiwan Semiconductor Manufactur | `TSM` | 0.3 | 2.1 | 58.0% | 13.6 | 33.6% | 37.9% | 63.1% | **90 CORE** | **10** |
| Sandisk Corporation | `SNDK` | 3.1 | 2.9 | 72.7% | 2.2 | 26.1% | 23.7% | 12.5% | **90 CORE** | **10** |
| USA Rare Earth, Inc. | `USAR` | 145.6 | 119.6 | -984.3% | 26.7 | 125.8% | 1039.1% | -10.9% | **0** | **86 CORE** |
| Marvell Technology, Inc. | `MRVL` | 11.6 | 11.5 | 16.8% | 16.6 | 74.7% | 64.3% | 2.2% | **85 WATCH** | **13** |
| Robinhood Markets, Inc. | `HOOD` | 11.0 | 10.6 | 45.7% | 18.2 | 39.8% | 29.4% | — | **85 WATCH** | **0** |
| NVIDIA Corporation | `NVDA` | 8.4 | 8.2 | 66.1% | 7.6 | 71.7% | 71.2% | 3.3% | **83 CORE** | **10** |
| Western Digital Corporation | `WDC` | 6.7 | 6.7 | 40.9% | 6.5 | 63.4% | 40.5% | 2.8% | **83 CORE** | **10** |
| Applovin Corporation | `APP` | 15.2 | 15.2 | 77.8% | 16.7 | 27.4% | 25.5% | 3.2% | **83 CORE** | **10** |
| Micron Technology, Inc. | `MU` | 5.1 | 4.8 | 74.6% | 2.8 | 18.2% | 16.2% | 4.3% | **82 CORE** | **30** |
| Okta, Inc. | `OKTA` | 10.9 | 10.2 | 7.7% | 43.7 | 11.5% | 10.1% | 3.1% | **8** | **80 CORE** |
| AST SpaceMobile, Inc. | `ASTS` | 65.3 | 61.3 | -393.3% | -17.1 | 28.1% | 252.7% | -20.3% | **0** | **80 WATCH** |
| Tesla, Inc. | `TSLA` | 13.2 | 12.9 | 3.0% | 160.2 | 25.2% | 13.5% | 0.4% | **20** | **78** |
| Advanced Micro Devices, Inc. | `AMD` | 15.5 | 15.2 | 17.8% | 24.1 | 118.2% | 83.6% | 1.0% | **77 WATCH** | **13** |
| Corning Incorporated | `GLW` | 4.6 | 5.0 | 16.8% | 20.7 | 34.8% | 21.2% | 1.1% | **77 WATCH** | **3** |
| AXT Inc | `AXT` | 11.8 | 9.5 | 19.6% | 12.0 | 116.3% | 111.5% | 0.9% | **75 WATCH** | **28** |
| Credo Technology Group Holding  | `CRDO` | 11.8 | 11.3 | 31.7% | 10.3 | 53.9% | 55.0% | 1.3% | **75 WATCH** | **18** |
| Broadcom Inc. | `AVGO` | 16.3 | 16.7 | 48.8% | 15.7 | 66.1% | 65.0% | 2.1% | **75 WATCH** | **18** |
| Applied Materials, Inc. | `AMAT` | 7.0 | 6.9 | 32.9% | 12.3 | 27.6% | 20.7% | 1.0% | **75 WATCH** | **18** |
| Dell Technologies Inc. | `DELL` | 1.2 | 1.3 | 9.9% | 9.1 | 17.9% | 19.7% | 3.4% | **75 CORE** | **30** |
| Oracle Corporation | `ORCL` | 4.4 | 6.2 | 34.3% | 9.2 | 35.7% | 45.7% | -14.5% | **70 WATCH** | **10** |
| XIAOMI-W | `XIAOMI` | 1.6 | 1.4 | 4.7% | 19.0 | 38.8% | 19.0% | -1.2% | **70 WATCH** | **10** |
| Microsoft Corporation | `MSFT` | 10.4 | 10.6 | 47.1% | 20.0 | 20.9% | 20.7% | 0.1% | **69 WATCH** | **3** |
| Meta Platforms, Inc. | `META` | 5.9 | 6.1 | 37.8% | 15.7 | 16.6% | 21.8% | 1.2% | **67 WATCH** | **38** |
| IonQ, Inc. | `IONQ` | 25.2 | 21.2 | -306.3% | -14.6 | -41.0% | 71.2% | -1.3% | **0** | **67 WATCH** |
| Adobe Inc. | `ADBE` | 3.3 | 3.3 | 36.3% | 7.9 | 12.0% | 9.1% | 11.0% | **65 WATCH** | **30** |
| Cerebras Systems Inc. | `CBRS` | 26.6 | 18.8 | -99.3% | 44.5 | 543.3% | 215.4% | — | **0** | **63** |
| Coherent Corp. | `COHR` | 4.7 | 5.0 | 14.1% | 11.9 | 52.1% | 39.1% | -4.6% | **60 WATCH** | **25** |
| Apple Inc. | `AAPL` | 10.4 | 10.5 | 33.0% | 32.4 | 12.4% | 8.1% | 2.1% | **5** | **58** |
| Coca-Cola Company (The) | `KO` | 8.2 | 8.7 | 32.2% | 27.4 | 5.5% | -3.1% | 1.0% | **0** | **58** |
| Arm Holdings plc | `ARM` | 29.8 | 29.2 | 17.0% | 49.3 | 36.2% | 37.2% | 0.7% | **55 WATCH** | **33** |
| IREN LIMITED | `IREN` | 7.2 | 16.8 | -72.9% | 43.8 | 116.3% | 199.7% | — | **0** | **55** |
| Bloom Energy Corporation | `BE` | 11.0 | 11.1 | 14.3% | 26.7 | 62.4% | 56.4% | -0.0% | **52** | **35** |
| Netflix, Inc. | `NFLX` | 4.7 | 4.9 | 31.3% | 15.0 | 5.4% | 10.7% | 10.9% | **35** | **50** |
| Palantir Technologies Inc. | `PLTR` | 47.4 | 46.0 | 45.6% | 56.5 | 49.2% | 53.7% | 0.8% | **45** | **48** |
| SamsungElec | `SAMSUNG` | 2.0 | 1.7 | 46.1% | 2.3 | 63.7% | 41.4% | 9.9% | **45** | **10** |
| Super Micro Computer, Inc. | `SMCI` | 0.3 | 0.4 | 8.3% | 3.1 | 6.5% | 11.3% | -57.4% | **35** | **45** |
| Circle Internet Group, Inc. | `CRCL` | 4.0 | 3.5 | 11.3% | 33.3 | 0.5% | 24.1% | 2.1% | **20** | **43** |
| CoreWeave, Inc. | `CRWV` | 2.2 | 8.5 | -0.5% | -22.2 | 23.4% | 106.5% | -89.4% | **0** | **40** |
| SOFTBANK GROUP CORP | `SOFTBANK` | 2.1 | 5.6 | -6.3% | 10.2 | 149.9% | 6.0% | -6.0% | **0** | **40** |
| Coinbase Global, Inc. | `COIN` | 5.0 | 4.6 | 0.1% | 42.5 | 949.6% | 25.9% | 13.6% | **35** | **25** |
| SK hynix | `SKHYNIX` | 2.9 | 2.6 | 74.5% | 2.1 | 49.4% | 60.5% | — | **30** | **5** |
| Lumentum Holdings Inc. | `LITE` | 11.2 | 11.0 | 23.4% | 11.5 | 60.9% | 58.5% | 0.3% | **30** | **23** |
| SK hynix | `SKHY` | 2.9 | 2.6 | 74.5% | 2.1 | 49.4% | 60.5% | — | **30** | **5** |
| Alphabet Inc. | `GOOGL` | 6.9 | 6.7 | 33.3% | 17.3 | -23.8% | 27.4% | -0.0% | **5** | **30** |
| Amazon.com, Inc. | `AMZN` | 3.3 | 3.6 | 13.1% | 22.6 | -16.7% | 15.8% | -1.3% | **0** | **30** |
| Nebius Group N.V. | `NBIS` | 10.9 | 14.8 | -18.7% | -26.7 | -1706.3% | 290.9% | -85.6% | **0** | **30** |
| Intel Corporation | `INTC` | 4.6 | 4.8 | 10.3% | 28.6 | 20.4% | 12.0% | 0.3% | **12** | **28** |
| Fluence Energy, Inc. | `FLNC` | 0.3 | 0.2 | -4.2% | -6.5 | 59.3% | 25.4% | 0.4% | **5** | **28** |
| BitMine Immersion Technologies, | `BMNR` | 65.1 | 63.0 | -216.3% | 13.8 | 105.7% | 197.6% | -1.2% | **25** | **25** |
| Strategy Inc | `MSTR` | 66.5 | 94.5 | -1100.1% | 4.5 | 417.1% | 3.1% | -9.8% | **25** | **25** |
| Applied Optoelectronics, Inc. | `AAOI` | 4.0 | 3.7 | -6.8% | 9.8 | 383.4% | 135.1% | -43.8% | **10** | **25** |
| Hyperliquid Strategies Inc | `PURR` | 95.9 | 83.7 | 6252.0% | 36.5 | -79.8% | 22.8% | — | **0** | **25** |

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
