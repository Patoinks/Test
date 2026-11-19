# OKX Long / Short Fundamental Scanner

Hourly scanner restricted to public companies exposed by the **OKX EEA TradFi / Stock Perpetual API universe**.

**Last scan:** 2026-11-19 03:37 UTC  
**Availability scope:** user-confirmed OKX EEA Stock Futures / X-Perp  
**OKX stock/ETF markets in configured universe:** 72  
**Public companies analysed:** 55  
**SHORT CORE:** 3  
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
| 1 | Marvell Technology, Inc. | MRVL | -2.2% | -13.8% | -8.0% | 90 | +6 | **96** | **CORE** | yes |
| 2 | QUALCOMM Incorporated | QCOM | -4.1% | -9.5% | -6.8% | 89 | +5 | **94** | **CORE** | yes |
| 3 | Taiwan Semiconductor Manufactur | TSM | 0.8% | -12.3% | -5.7% | 88 | +5 | **93** | **CORE** | yes |
| 4 | AXT Inc | AXT | -2.2% | -24.2% | -13.2% | 82 | +11 | **93** | **CORE** | yes |
| 5 | Sandisk Corporation | SNDK | -2.6% | — | — | 90 | +0 | **90** | **CORE** | yes |
| 6 | NVIDIA Corporation | NVDA | -2.9% | -13.1% | -8.0% | 82 | +6 | **88** | **CORE** | yes |
| 7 | Credo Technology Group Holding  | CRDO | -0.8% | -13.1% | -6.9% | 82 | +6 | **88** | **CORE** | yes |
| 8 | Robinhood Markets, Inc. | HOOD | -0.0% | -18.2% | -9.1% | 80 | +7 | **87** | **CORE** | yes |
| 9 | Western Digital Corporation | WDC | 1.7% | -8.0% | -3.2% | 82 | +3 | **85** | **CORE** | yes |
| 10 | Applovin Corporation | APP | -2.0% | -3.4% | -2.7% | 82 | +2 | **84** | **CORE** | yes |

## Final model + Price Timing — SHORT

| Rank | Company | OKX | 24h | 7d | 50/50 move | Base SHORT | Timing adj. | Final | Signal | Prev. SHORT? |
|---:|---|---|---:|---:|---:|---:|---:|---:|---|---|
| 1 | Rocket Lab Corporation | RKLB | -3.6% | -19.8% | -11.7% | 100 | -9 | **91** | **CORE** | yes |
| 2 | Moderna, Inc. | MRNA | -4.8% | -20.9% | -12.9% | 94 | -10 | **84** | **CORE** | yes |
| 3 | USA Rare Earth, Inc. | USAR | -1.1% | -20.6% | -10.9% | 86 | -9 | **77** | **CORE** | yes |
| 4 | Okta, Inc. | OKTA | 12.1% | 7.3% | 9.7% | 60 | +8 | **68** | **WATCH** | yes |
| 5 | AST SpaceMobile, Inc. | ASTS | -7.6% | -30.4% | -19.0% | 80 | -15 | **65** | **WATCH** | yes |
| 6 | Cerebras Systems Inc. | CBRS | -9.6% | -6.9% | -8.2% | 71 | -7 | **64** | **WATCH** | yes |
| 7 | Tesla, Inc. | TSLA | 0.9% | -1.8% | -0.4% | 59 | +0 | **59** | **WATCH** | yes |

## Combined model — LONG

Weighted score: **70% fundamental + 30% P/E trend**.

| Rank | Company | OKX | Fundamental LONG | P/E trend LONG | Combined | Signal |
|---:|---|---|---:|---:|---:|---|
| 1 | Sandisk Corporation | `SNDK` | 90 | 90 | **90** | **CORE** |
| 2 | Marvell Technology, Inc. | `MRVL` | 85 | 100 | **90** | **CORE** |
| 3 | QUALCOMM Incorporated | `QCOM` | 100 | 62 | **89** | **CORE** |
| 4 | Taiwan Semiconductor Manufactur | `TSM` | 90 | 85 | **88** | **CORE** |
| 5 | Western Digital Corporation | `WDC` | 83 | 80 | **82** | **CORE** |
| 6 | Applovin Corporation | `APP` | 83 | 80 | **82** | **CORE** |
| 7 | AXT Inc | `AXT` | 75 | 100 | **82** | **CORE** |
| 8 | NVIDIA Corporation | `NVDA` | 75 | 100 | **82** | **CORE** |
| 9 | Credo Technology Group Holding  | `CRDO` | 75 | 100 | **82** | **CORE** |
| 10 | Broadcom Inc. | `AVGO` | 75 | 100 | **82** | **CORE** |

## Combined model — SHORT

Weighted score: **70% fundamental + 30% P/E trend**.

| Rank | Company | OKX | Fundamental SHORT | P/E trend SHORT | Combined | Signal |
|---:|---|---|---:|---:|---:|---|
| 1 | Rocket Lab Corporation | `RKLB` | 100 | 0 | **100** | **CORE** |
| 2 | Moderna, Inc. | `MRNA` | 94 | 0 | **94** | **WATCH** |
| 3 | USA Rare Earth, Inc. | `USAR` | 86 | 0 | **86** | **CORE** |
| 4 | AST SpaceMobile, Inc. | `ASTS` | 80 | 0 | **80** | **WATCH** |
| 5 | Cerebras Systems Inc. | `CBRS` | 71 | 0 | **71** | **WATCH** |
| 6 | IonQ, Inc. | `IONQ` | 67 | 0 | **67** | **WATCH** |
| 7 | Okta, Inc. | `OKTA` | 80 | 13 | **60** | **WATCH** |
| 8 | Tesla, Inc. | `TSLA` | 78 | 15 | **59** | **WATCH** |

## P/E Compression + Growth — LONG

| Rank | Company | OKX | Trail P/E | Fwd P/E | P/E change | EPS +1y | Rev +1y | Rev trend | LONG score | Signal |
|---:|---|---|---:|---:|---:|---:|---:|---|---:|---|
| 1 | Marvell Technology, Inc. | `MRVL` | 47.9 | 19.7 | -58.8% | 74.7% | 64.3% | accelerating | **100** | **CORE** |
| 2 | AXT Inc | `AXT` | 74.2 | 14.0 | -81.2% | 116.3% | 115.9% | decelerating | **100** | **CORE** |
| 3 | NVIDIA Corporation | `NVDA` | 19.7 | 9.1 | -53.7% | 71.4% | 70.0% | decelerating | **100** | **CORE** |
| 4 | Credo Technology Group Holding  | `CRDO` | 43.6 | 12.7 | -71.0% | 53.9% | 55.0% | decelerating | **100** | **CORE** |
| 5 | Broadcom Inc. | `AVGO` | 45.2 | 18.2 | -59.7% | 66.4% | 65.1% | decelerating | **100** | **CORE** |
| 6 | Advanced Micro Devices, Inc. | `AMD` | 113.3 | 30.1 | -73.5% | 118.2% | 83.6% | accelerating | **100** | **CORE** |
| 7 | Coherent Corp. | `COHR` | 43.6 | 13.5 | -69.1% | 51.7% | 39.9% | decelerating | **100** | **CORE** |
| 8 | Bloom Energy Corporation | `BE` | 103.6 | 32.1 | -69.0% | 62.7% | 56.4% | decelerating | **96** | **CORE** |
| 9 | Oracle Corporation | `ORCL` | 18.0 | 10.3 | -42.9% | 35.7% | 45.7% | accelerating | **95** | **CORE** |
| 10 | Arm Holdings plc | `ARM` | 210.1 | 59.2 | -71.8% | 36.2% | 37.2% | accelerating | **95** | **CORE** |

## P/E Expansion + Weakening — SHORT

| Rank | Company | OKX | Trail P/E | Fwd P/E | P/E change | EPS +1y | Rev +1y | Rev trend | SHORT score | Signal |
|---:|---|---|---:|---:|---:|---:|---:|---|---:|---|
| 1 | Hyperliquid Strategies Inc | `PURR` | 3.4 | 38.8 | 1051.2% | -79.8% | 22.8% | decelerating | **80** | **CORE** |
| 2 | Alphabet Inc. | `GOOGL` | 14.7 | 18.5 | 25.2% | -23.8% | 27.4% | accelerating | **50** | **WATCH** |

## Top SHORT candidates

| Rank | Company | OKX market | SHORT score | Signal | P/S | EV/S | Op margin | Fwd P/E | Rev +1y | FCF yield |
|---:|---|---|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Rocket Lab Corporation | `RKLB-USDT-SWAP` | **100** | **CORE** | 40.5 | 32.9 | -27.6% | 741.4 | 37.0% | -0.6% |
| 2 | Moderna, Inc. | `MRNA-USDT-SWAP` | **94** | **WATCH** | 31.5 | 31.2 | -80.8% | -47.0 | 11.3% | -0.7% |
| 3 | USA Rare Earth, Inc. | `USAR-USDT-SWAP` | **86** | **CORE** | 152.3 | 126.4 | -984.3% | 27.9 | 1039.1% | -10.4% |
| 4 | Okta, Inc. | `OKTA-USDT-SWAP` | **80** | **CORE** | 11.1 | 10.4 | 7.7% | 44.7 | 10.1% | 3.0% |
| 5 | AST SpaceMobile, Inc. | `ASTS-USDT-SWAP` | **80** | **WATCH** | 69.6 | 65.9 | -393.3% | -16.3 | 252.7% | -19.0% |
| 6 | Cerebras Systems Inc. | `CBRS-USDT-SWAP` | **71** | **WATCH** | 30.3 | 22.5 | -99.3% | 50.7 | 217.9% | — |
| 7 | IonQ, Inc. | `IONQ-USDT-SWAP` | **67** | **WATCH** | 28.6 | 24.4 | -306.3% | -16.5 | 71.2% | -1.1% |

## Top LONG candidates

| Rank | Company | OKX market | LONG score | Signal | P/S | EV/S | Op margin | Fwd P/E | Rev +1y | FCF yield |
|---:|---|---|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | QUALCOMM Incorporated | `QCOM-USDT-SWAP` | **100** | **CORE** | 4.0 | 4.2 | 20.8% | 13.1 | 15.4% | 5.3% |
| 2 | Taiwan Semiconductor Manufactur | `TSM-USDT-SWAP` | **90** | **CORE** | 0.4 | 2.5 | 58.0% | 15.5 | 37.8% | 55.4% |
| 3 | Sandisk Corporation | `SNDK-USDT-SWAP` | **90** | **CORE** | 3.8 | 3.6 | 72.7% | 2.7 | 23.7% | 10.2% |
| 4 | Marvell Technology, Inc. | `MRVL-USDT-SWAP` | **85** | **WATCH** | 13.9 | 13.6 | 16.8% | 19.7 | 64.3% | 1.8% |
| 5 | Applovin Corporation | `APP-USDT-SWAP` | **83** | **CORE** | 17.0 | 17.1 | 77.8% | 18.7 | 25.4% | 2.9% |
| 6 | Western Digital Corporation | `WDC-USDT-SWAP` | **83** | **CORE** | 7.4 | 7.4 | 40.9% | 7.1 | 40.5% | 2.5% |
| 7 | Corning Incorporated | `GLW-USDT-SWAP` | **77** | **WATCH** | 5.3 | 5.7 | 16.8% | 23.8 | 21.2% | 0.9% |
| 8 | Robinhood Markets, Inc. | `HOOD-USDT-SWAP` | **77** | **WATCH** | 12.3 | 11.8 | 45.7% | 20.3 | 29.4% | — |
| 9 | Dell Technologies Inc. | `DELL-USDT-SWAP` | **75** | **CORE** | 1.3 | 1.5 | 9.9% | 10.2 | 19.7% | 3.0% |
| 10 | Applied Materials, Inc. | `AMAT-USDT-SWAP` | **75** | **WATCH** | 8.1 | 8.0 | 32.9% | 14.3 | 20.8% | 0.9% |

## Analyst consensus (12-month price target) — most upside

| Rank | Company | OKX | Price | Analyst mean target | Gap | Analysts | Currency |
|---:|---|---|---:|---:|---:|---:|---|
| 1 | Hyperliquid Strategies Inc | `PURR` | 7.95 | 22.50 | **183.0%** | 4 | USD |
| 2 | SK hynix | `SKHYNIX` | 1123000.00 | 3056126.80 | **172.1%** | 39 | KRW |
| 3 | Applied Optoelectronics, Inc. | `AAOI` | 40.79 | 109.00 | **167.2%** | 5 | USD |
| 4 | Sandisk Corporation | `SNDK` | 776.22 | 2047.38 | **163.8%** | 24 | USD |
| 5 | Strategy Inc | `MSTR` | 90.32 | 233.27 | **158.3%** | 15 | USD |
| 6 | AXT Inc | `AXT` | 35.61 | 89.33 | **150.9%** | 6 | USD |
| 7 | AST SpaceMobile, Inc. | `ASTS` | 25.49 | 63.35 | **148.5%** | 12 | USD |
| 8 | SamsungElec | `SAMSUNG` | 190800.00 | 467638.88 | **145.1%** | 36 | KRW |
| 9 | CoreWeave, Inc. | `CRWV` | 47.83 | 115.34 | **141.2%** | 38 | USD |
| 10 | IonQ, Inc. | `IONQ` | 23.48 | 54.27 | **131.2%** | 14 | USD |
| 11 | Credo Technology Group Holding  | `CRDO` | 122.94 | 277.47 | **125.7%** | 19 | USD |
| 12 | Cerebras Systems Inc. | `CBRS` | 94.15 | 210.18 | **123.2%** | 11 | USD |
| 13 | Micron Technology, Inc. | `MU` | 705.27 | 1561.91 | **121.5%** | 45 | USD |
| 14 | Nebius Group N.V. | `NBIS` | 106.96 | 234.50 | **119.2%** | 20 | USD |
| 15 | Marvell Technology, Inc. | `MRVL` | 145.54 | 310.89 | **113.6%** | 40 | USD |

## Analyst consensus (12-month price target) — most downside

| Rank | Company | OKX | Price | Analyst mean target | Gap | Analysts | Currency |
|---:|---|---|---:|---:|---:|---:|---|
| 1 | Moderna, Inc. | `MRNA` | 196.79 | 165.32 | **-16.0%** | 19 | USD |
| 2 | Apple Inc. | `AAPL` | 352.45 | 345.63 | **-1.9%** | 39 | USD |

Price/target uses the underlying Yahoo Finance share quote, not the OKX derivative. Minimum 3 analysts; unreliable price scales and missing coverage excluded. Targets are analyst opinions, not guaranteed forecasts.

## All OKX companies — our ratio + LONG/SHORT scores

| Company | OKX | P/S | EV/S | Op margin | Fwd P/E | EPS +1y | Rev +1y | FCF yield | LONG | SHORT |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| QUALCOMM Incorporated | `QCOM` | 4.0 | 4.2 | 20.8% | 13.1 | 26.6% | 15.4% | 5.3% | **100 CORE** | **0** |
| Rocket Lab Corporation | `RKLB` | 40.5 | 32.9 | -27.6% | 741.4 | 75.7% | 37.0% | -0.6% | **0** | **100 CORE** |
| Moderna, Inc. | `MRNA` | 31.5 | 31.2 | -80.8% | -47.0 | 39.0% | 11.3% | -0.7% | **0** | **94 WATCH** |
| Taiwan Semiconductor Manufactur | `TSM` | 0.4 | 2.5 | 58.0% | 15.5 | 33.6% | 37.8% | 55.4% | **90 CORE** | **10** |
| Sandisk Corporation | `SNDK` | 3.8 | 3.6 | 72.7% | 2.7 | 27.1% | 23.7% | 10.2% | **90 CORE** | **10** |
| USA Rare Earth, Inc. | `USAR` | 152.3 | 126.4 | -984.3% | 27.9 | 125.8% | 1039.1% | -10.4% | **0** | **86 CORE** |
| Marvell Technology, Inc. | `MRVL` | 13.9 | 13.6 | 16.8% | 19.7 | 74.7% | 64.3% | 1.8% | **85 WATCH** | **13** |
| Western Digital Corporation | `WDC` | 7.4 | 7.4 | 40.9% | 7.1 | 63.4% | 40.5% | 2.5% | **83 CORE** | **10** |
| Applovin Corporation | `APP` | 17.0 | 17.1 | 77.8% | 18.7 | 27.4% | 25.4% | 2.9% | **83 CORE** | **10** |
| Okta, Inc. | `OKTA` | 11.1 | 10.4 | 7.7% | 44.7 | 11.4% | 10.1% | 3.0% | **8** | **80 CORE** |
| AST SpaceMobile, Inc. | `ASTS` | 69.6 | 65.9 | -393.3% | -16.3 | 28.1% | 252.7% | -19.0% | **0** | **80 WATCH** |
| Tesla, Inc. | `TSLA` | 14.6 | 14.4 | 3.0% | 177.7 | 25.2% | 13.5% | 0.3% | **20** | **78** |
| Robinhood Markets, Inc. | `HOOD` | 12.3 | 11.8 | 45.7% | 20.3 | 39.7% | 29.4% | — | **77 WATCH** | **0** |
| Corning Incorporated | `GLW` | 5.3 | 5.7 | 16.8% | 23.8 | 34.8% | 21.2% | 0.9% | **77 WATCH** | **13** |
| AXT Inc | `AXT` | 13.7 | 11.4 | 19.6% | 14.0 | 116.3% | 115.9% | 0.8% | **75 WATCH** | **28** |
| NVIDIA Corporation | `NVDA` | 12.0 | 12.3 | 65.2% | 9.1 | 71.4% | 70.0% | 1.1% | **75 WATCH** | **18** |
| Credo Technology Group Holding  | `CRDO` | 14.5 | 14.1 | 31.7% | 12.7 | 53.9% | 55.0% | 1.1% | **75 WATCH** | **28** |
| Micron Technology, Inc. | `MU` | 6.0 | 5.7 | 74.6% | 3.4 | 17.7% | 16.0% | 3.7% | **75 CORE** | **30** |
| Dell Technologies Inc. | `DELL` | 1.3 | 1.5 | 9.9% | 10.2 | 17.9% | 19.7% | 3.0% | **75 CORE** | **30** |
| Broadcom Inc. | `AVGO` | 19.0 | 19.4 | 48.8% | 18.2 | 66.4% | 65.1% | 1.8% | **75 WATCH** | **28** |
| Applied Materials, Inc. | `AMAT` | 8.1 | 8.0 | 32.9% | 14.3 | 27.7% | 20.8% | 0.9% | **75 WATCH** | **18** |
| Cerebras Systems Inc. | `CBRS` | 30.3 | 22.5 | -99.3% | 50.7 | 543.3% | 217.9% | — | **0** | **71 WATCH** |
| Oracle Corporation | `ORCL` | 4.9 | 6.7 | 34.3% | 10.3 | 35.7% | 45.7% | -12.9% | **70 WATCH** | **10** |
| Advanced Micro Devices, Inc. | `AMD` | 19.3 | 19.0 | 17.8% | 30.1 | 118.2% | 83.6% | 0.8% | **70 WATCH** | **13** |
| XIAOMI-W | `XIAOMI` | 1.7 | 1.6 | 4.7% | 19.6 | 38.7% | 19.0% | -1.2% | **70 WATCH** | **10** |
| IonQ, Inc. | `IONQ` | 28.6 | 24.4 | -306.3% | -16.5 | -41.0% | 71.2% | -1.1% | **0** | **67 WATCH** |
| Adobe Inc. | `ADBE` | 3.4 | 3.4 | 36.3% | 8.3 | 12.0% | 9.1% | 10.6% | **65 WATCH** | **30** |
| Coherent Corp. | `COHR` | 5.3 | 5.7 | 14.1% | 13.5 | 51.7% | 39.9% | -4.0% | **60 WATCH** | **35** |
| Microsoft Corporation | `MSFT` | 10.9 | 11.1 | 47.1% | 21.0 | 20.9% | 20.5% | 0.1% | **59 WATCH** | **3** |
| Apple Inc. | `AAPL` | 10.7 | 10.8 | 33.0% | 33.3 | 12.4% | 8.1% | 2.1% | **5** | **58** |
| Coca-Cola Company (The) | `KO` | 8.3 | 8.8 | 32.2% | 27.8 | 5.5% | -3.1% | 1.0% | **0** | **58** |
| Meta Platforms, Inc. | `META` | 6.5 | 6.7 | 37.8% | 17.3 | 16.6% | 21.8% | 1.1% | **57 WATCH** | **38** |
| IREN LIMITED | `IREN` | 9.3 | 18.9 | -72.9% | 56.4 | 116.3% | 199.7% | — | **0** | **55** |
| Netflix, Inc. | `NFLX` | 4.9 | 5.1 | 31.3% | 15.9 | 5.1% | 10.7% | 10.4% | **35** | **50** |
| Palantir Technologies Inc. | `PLTR` | 51.8 | 50.4 | 45.6% | 61.7 | 49.2% | 53.7% | 0.7% | **45** | **48** |
| Bloom Energy Corporation | `BE` | 13.2 | 13.3 | 14.3% | 32.1 | 62.7% | 56.4% | -0.0% | **45** | **35** |
| SamsungElec | `SAMSUNG` | 2.1 | 1.8 | 46.1% | 2.5 | 63.5% | 41.2% | 6.7% | **45** | **10** |
| Super Micro Computer, Inc. | `SMCI` | 0.3 | 0.4 | 8.3% | 3.5 | 6.5% | 11.3% | -51.0% | **35** | **45** |
| Arm Holdings plc | `ARM` | 35.8 | 35.2 | 17.0% | 59.2 | 36.2% | 37.2% | 0.6% | **43** | **33** |
| Circle Internet Group, Inc. | `CRCL` | 4.5 | 4.0 | 11.3% | 37.4 | 0.5% | 24.1% | 1.9% | **20** | **43** |
| Nebius Group N.V. | `NBIS` | 14.3 | 18.3 | -18.7% | -35.1 | -1706.3% | 290.9% | -65.1% | **0** | **40** |
| CoreWeave, Inc. | `CRWV` | 2.7 | 9.0 | -0.5% | -27.0 | 23.4% | 106.6% | -73.9% | **0** | **40** |
| SOFTBANK GROUP CORP | `SOFTBANK` | 2.4 | 5.9 | -6.3% | 11.7 | 208.4% | 6.0% | -5.2% | **0** | **40** |
| Coinbase Global, Inc. | `COIN` | 5.4 | 5.0 | 0.1% | 45.0 | 866.1% | 26.2% | 12.6% | **35** | **25** |
| SK hynix | `SKHYNIX` | 2.9 | 2.7 | 74.5% | 2.1 | 49.4% | 60.5% | — | **30** | **5** |
| Lumentum Holdings Inc. | `LITE` | 13.4 | 13.2 | 23.4% | 13.7 | 60.9% | 57.9% | 0.3% | **30** | **23** |
| SK hynix | `SKHY` | 2.9 | 2.7 | 74.5% | 2.1 | 49.4% | 60.5% | — | **30** | **5** |
| Alphabet Inc. | `GOOGL` | 7.4 | 7.2 | 33.3% | 18.5 | -23.8% | 27.4% | -0.0% | **5** | **30** |
| Amazon.com, Inc. | `AMZN` | 3.6 | 3.9 | 13.1% | 24.5 | -16.7% | 15.7% | -1.2% | **0** | **30** |
| Intel Corporation | `INTC` | 4.9 | 5.1 | 10.3% | 30.5 | 20.4% | 12.0% | 0.3% | **5** | **28** |
| Fluence Energy, Inc. | `FLNC` | 0.3 | 0.3 | -4.2% | -7.6 | 59.3% | 25.4% | 0.3% | **5** | **28** |
| BitMine Immersion Technologies, | `BMNR` | 77.6 | 75.5 | -216.3% | 16.5 | 105.7% | 197.6% | -1.0% | **25** | **25** |
| Strategy Inc | `MSTR` | 77.2 | 105.2 | -1100.1% | 5.2 | 417.1% | 3.1% | -8.5% | **25** | **25** |
| Applied Optoelectronics, Inc. | `AAOI` | 5.0 | 4.6 | -6.8% | 10.9 | 439.3% | 135.1% | -35.4% | **10** | **25** |
| Hyperliquid Strategies Inc | `PURR` | 101.9 | 89.7 | 6252.0% | 38.8 | -79.8% | 22.8% | — | **0** | **25** |

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
