# OKX Long / Short Fundamental Scanner

Hourly scanner restricted to public companies exposed by the **OKX EEA TradFi / Stock Perpetual API universe**.

**Last scan:** 2026-11-17 04:37 UTC  
**Availability scope:** user-confirmed OKX EEA Stock Futures / X-Perp  
**OKX stock/ETF markets in configured universe:** 72  
**Public companies analysed:** 55  
**SHORT CORE:** 4  
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
| 1 | Sandisk Corporation | SNDK | -8.6% | -8.7% | -8.7% | 90 | +7 | **97** | **CORE** | yes |
| 2 | Marvell Technology, Inc. | MRVL | -7.3% | -6.0% | -6.6% | 90 | +5 | **95** | **CORE** | yes |
| 3 | Taiwan Semiconductor Manufactur | TSM | -6.3% | -3.9% | -5.1% | 88 | +4 | **92** | **CORE** | yes |
| 4 | AXT Inc | AXT | -8.1% | -10.4% | -9.2% | 82 | +7 | **89** | **CORE** | yes |
| 5 | Credo Technology Group Holding  | CRDO | -8.2% | -9.2% | -8.7% | 82 | +7 | **89** | **CORE** | yes |
| 6 | NVIDIA Corporation | NVDA | -4.1% | -12.6% | -8.4% | 82 | +7 | **89** | **CORE** | yes |
| 7 | Western Digital Corporation | WDC | -5.0% | -3.1% | -4.0% | 85 | +3 | **88** | **CORE** | yes |
| 8 | Robinhood Markets, Inc. | HOOD | -7.4% | -13.5% | -10.5% | 80 | +8 | **88** | **CORE** | yes |
| 9 | QUALCOMM Incorporated | QCOM | -2.3% | -1.7% | -2.0% | 85 | +2 | **87** | **CORE** | yes |
| 10 | Advanced Micro Devices, Inc. | AMD | -5.6% | -0.8% | -3.2% | 84 | +3 | **87** | **CORE** | yes |

## Final model + Price Timing — SHORT

| Rank | Company | OKX | 24h | 7d | 50/50 move | Base SHORT | Timing adj. | Final | Signal | Prev. SHORT? |
|---:|---|---|---:|---:|---:|---:|---:|---:|---|---|
| 1 | Rocket Lab Corporation | RKLB | -6.8% | -2.5% | -4.6% | 100 | -4 | **96** | **CORE** | yes |
| 2 | Moderna, Inc. | MRNA | -3.6% | -20.0% | -11.8% | 94 | -9 | **85** | **CORE** | yes |
| 3 | USA Rare Earth, Inc. | USAR | -12.6% | -18.6% | -15.6% | 86 | -12 | **74** | **WATCH** | yes |
| 4 | Cerebras Systems Inc. | CBRS | -7.1% | 4.4% | -1.3% | 71 | -1 | **70** | **WATCH** | yes |
| 5 | AST SpaceMobile, Inc. | ASTS | -12.3% | -22.5% | -17.4% | 80 | -14 | **66** | **WATCH** | yes |
| 6 | IonQ, Inc. | IONQ | -8.4% | -25.2% | -16.8% | 75 | -13 | **62** | **WATCH** | yes |
| 7 | Okta, Inc. | OKTA | -2.5% | 0.4% | -1.1% | 60 | -1 | **59** | **WATCH** | no |
| 8 | Tesla, Inc. | TSLA | -2.7% | 0.4% | -1.1% | 59 | -1 | **58** | **WATCH** | yes |

## Combined model — LONG

Weighted score: **70% fundamental + 30% P/E trend**.

| Rank | Company | OKX | Fundamental LONG | P/E trend LONG | Combined | Signal |
|---:|---|---|---:|---:|---:|---|
| 1 | Sandisk Corporation | `SNDK` | 90 | 90 | **90** | **CORE** |
| 2 | Marvell Technology, Inc. | `MRVL` | 85 | 100 | **90** | **CORE** |
| 3 | Taiwan Semiconductor Manufactur | `TSM` | 90 | 85 | **88** | **CORE** |
| 4 | QUALCOMM Incorporated | `QCOM` | 100 | 50 | **85** | **CORE** |
| 5 | Western Digital Corporation | `WDC` | 83 | 90 | **85** | **CORE** |
| 6 | Advanced Micro Devices, Inc. | `AMD` | 77 | 100 | **84** | **CORE** |
| 7 | NVIDIA Corporation | `NVDA` | 75 | 100 | **82** | **CORE** |
| 8 | AXT Inc | `AXT` | 75 | 100 | **82** | **CORE** |
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
| 5 | IonQ, Inc. | `IONQ` | 75 | 0 | **75** | **WATCH** |
| 6 | Cerebras Systems Inc. | `CBRS` | 71 | 0 | **71** | **WATCH** |
| 7 | Okta, Inc. | `OKTA` | 80 | 13 | **60** | **WATCH** |
| 8 | Tesla, Inc. | `TSLA` | 78 | 15 | **59** | **WATCH** |

## P/E Compression + Growth — LONG

| Rank | Company | OKX | Trail P/E | Fwd P/E | P/E change | EPS +1y | Rev +1y | Rev trend | LONG score | Signal |
|---:|---|---|---:|---:|---:|---:|---:|---|---:|---|
| 1 | Marvell Technology, Inc. | `MRVL` | 51.5 | 19.7 | -61.7% | 74.7% | 64.3% | accelerating | **100** | **CORE** |
| 2 | NVIDIA Corporation | `NVDA` | 20.6 | 9.9 | -52.2% | 69.8% | 67.2% | decelerating | **100** | **CORE** |
| 3 | AXT Inc | `AXT` | 85.5 | 15.1 | -82.3% | 116.3% | 115.9% | decelerating | **100** | **CORE** |
| 4 | Credo Technology Group Holding  | `CRDO` | 46.6 | 12.4 | -73.3% | 53.9% | 55.0% | decelerating | **100** | **CORE** |
| 5 | Advanced Micro Devices, Inc. | `AMD` | 114.1 | 28.6 | -74.9% | 118.2% | 83.6% | accelerating | **100** | **CORE** |
| 6 | Broadcom Inc. | `AVGO` | 42.6 | 17.2 | -59.7% | 66.4% | 65.1% | decelerating | **100** | **CORE** |
| 7 | Coherent Corp. | `COHR` | 45.2 | 12.9 | -71.5% | 51.7% | 39.4% | decelerating | **100** | **CORE** |
| 8 | Bloom Energy Corporation | `BE` | 116.6 | 33.3 | -71.4% | 62.7% | 56.4% | decelerating | **96** | **CORE** |
| 9 | Oracle Corporation | `ORCL` | 18.7 | 10.8 | -42.3% | 35.7% | 45.7% | accelerating | **95** | **CORE** |
| 10 | Arm Holdings plc | `ARM` | 218.8 | 56.7 | -74.1% | 36.2% | 37.2% | accelerating | **95** | **CORE** |

## P/E Expansion + Weakening — SHORT

| Rank | Company | OKX | Trail P/E | Fwd P/E | P/E change | EPS +1y | Rev +1y | Rev trend | SHORT score | Signal |
|---:|---|---|---:|---:|---:|---:|---:|---|---:|---|
| 1 | Hyperliquid Strategies Inc | `PURR` | 3.7 | 40.5 | 997.6% | -79.8% | 22.8% | decelerating | **80** | **CORE** |
| 2 | Alphabet Inc. | `GOOGL` | 15.4 | 18.7 | 21.0% | -23.8% | 27.2% | accelerating | **50** | **WATCH** |

## Top SHORT candidates

| Rank | Company | OKX market | SHORT score | Signal | P/S | EV/S | Op margin | Fwd P/E | Rev +1y | FCF yield |
|---:|---|---|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Rocket Lab Corporation | `RKLB-USDT-SWAP` | **100** | **CORE** | 43.8 | 36.0 | -27.6% | 801.5 | 37.0% | -0.6% |
| 2 | Moderna, Inc. | `MRNA-USDT-SWAP` | **94** | **WATCH** | 34.5 | 34.1 | -80.8% | -51.4 | 11.3% | -0.7% |
| 3 | USA Rare Earth, Inc. | `USAR-USDT-SWAP` | **86** | **CORE** | 165.6 | 139.3 | -984.3% | 30.3 | 1039.1% | -9.6% |
| 4 | Okta, Inc. | `OKTA-USDT-SWAP` | **80** | **CORE** | 10.1 | 9.4 | 7.7% | 40.7 | 10.1% | 3.3% |
| 5 | AST SpaceMobile, Inc. | `ASTS-USDT-SWAP` | **80** | **WATCH** | 78.0 | 72.4 | -393.3% | -18.3 | 252.7% | -17.0% |
| 6 | IonQ, Inc. | `IONQ-USDT-SWAP` | **75** | **WATCH** | 32.3 | 27.8 | -306.3% | -18.6 | 71.2% | -1.0% |
| 7 | Cerebras Systems Inc. | `CBRS-USDT-SWAP` | **71** | **WATCH** | 32.5 | 24.7 | -99.3% | 54.3 | 217.9% | — |
| 8 | Circle Internet Group, Inc. | `CRCL-USDT-SWAP` | **63** | **CORE** | 4.9 | 4.3 | 11.3% | 40.5 | 24.1% | 1.8% |
| 9 | Hyperliquid Strategies Inc | `PURR-USDT-SWAP` | **25** | **WATCH** | 106.5 | 94.3 | 6252.0% | 40.5 | 22.8% | — |

## Top LONG candidates

| Rank | Company | OKX market | LONG score | Signal | P/S | EV/S | Op margin | Fwd P/E | Rev +1y | FCF yield |
|---:|---|---|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | QUALCOMM Incorporated | `QCOM-USDT-SWAP` | **100** | **CORE** | 4.2 | 4.4 | 20.8% | 13.8 | 15.5% | 5.1% |
| 2 | Taiwan Semiconductor Manufactur | `TSM-USDT-SWAP` | **90** | **CORE** | 0.4 | 2.5 | 58.0% | 16.0 | 37.8% | 62.1% |
| 3 | Sandisk Corporation | `SNDK-USDT-SWAP` | **90** | **CORE** | 4.0 | 3.8 | 72.7% | 2.8 | 23.7% | 9.8% |
| 4 | Marvell Technology, Inc. | `MRVL-USDT-SWAP` | **85** | **WATCH** | 13.8 | 13.6 | 16.8% | 19.7 | 64.3% | 1.8% |
| 5 | Applovin Corporation | `APP-USDT-SWAP` | **83** | **CORE** | 18.1 | 18.1 | 77.8% | 19.9 | 25.4% | 2.7% |
| 6 | Western Digital Corporation | `WDC-USDT-SWAP` | **83** | **CORE** | 7.3 | 7.2 | 40.9% | 7.0 | 40.5% | 2.6% |
| 7 | Corning Incorporated | `GLW-USDT-SWAP` | **77** | **WATCH** | 5.2 | 5.6 | 16.8% | 23.3 | 21.2% | 1.0% |
| 8 | Robinhood Markets, Inc. | `HOOD-USDT-SWAP` | **77** | **WATCH** | 12.8 | 12.3 | 45.7% | 21.1 | 29.4% | — |
| 9 | Advanced Micro Devices, Inc. | `AMD-USDT-SWAP` | **77** | **WATCH** | 18.2 | 18.1 | 17.8% | 28.6 | 83.6% | 0.9% |
| 10 | Dell Technologies Inc. | `DELL-USDT-SWAP` | **75** | **CORE** | 1.3 | 1.5 | 9.9% | 10.5 | 19.7% | 3.0% |

## Analyst consensus (12-month price target) — most upside

| Rank | Company | OKX | Price | Analyst mean target | Gap | Analysts | Currency |
|---:|---|---|---:|---:|---:|---:|---|
| 1 | SK hynix | `SKHYNIX` | 1112000.00 | 3056126.80 | **174.8%** | 39 | KRW |
| 2 | Hyperliquid Strategies Inc | `PURR` | 8.31 | 22.50 | **170.8%** | 4 | USD |
| 3 | Sandisk Corporation | `SNDK` | 809.11 | 2047.38 | **153.0%** | 24 | USD |
| 4 | SamsungElec | `SAMSUNG` | 190500.00 | 467638.88 | **145.5%** | 36 | KRW |
| 5 | Applied Optoelectronics, Inc. | `AAOI` | 45.16 | 109.00 | **141.4%** | 5 | USD |
| 6 | AXT Inc | `AXT` | 38.46 | 91.50 | **137.9%** | 6 | USD |
| 7 | CoreWeave, Inc. | `CRWV` | 49.88 | 115.34 | **131.2%** | 38 | USD |
| 8 | Credo Technology Group Holding  | `CRDO` | 120.71 | 277.47 | **129.9%** | 19 | USD |
| 9 | Strategy Inc | `MSTR` | 103.03 | 233.27 | **126.4%** | 15 | USD |
| 10 | SOFTBANK GROUP CORP | `SOFTBANK` | 3252.00 | 7229.58 | **122.3%** | 18 | JPY |
| 11 | AST SpaceMobile, Inc. | `ASTS` | 28.58 | 63.35 | **121.7%** | 12 | USD |
| 12 | Nebius Group N.V. | `NBIS` | 107.13 | 234.50 | **118.9%** | 20 | USD |
| 13 | Western Digital Corporation | `WDC` | 280.93 | 613.38 | **118.3%** | 24 | USD |
| 14 | Micron Technology, Inc. | `MU` | 719.02 | 1561.91 | **117.2%** | 45 | USD |
| 15 | Marvell Technology, Inc. | `MRVL` | 145.36 | 310.89 | **113.9%** | 40 | USD |

## Analyst consensus (12-month price target) — most downside

| Rank | Company | OKX | Price | Analyst mean target | Gap | Analysts | Currency |
|---:|---|---|---:|---:|---:|---:|---|
| 1 | Moderna, Inc. | `MRNA` | 215.27 | 159.79 | **-25.8%** | 19 | USD |
| 2 | Apple Inc. | `AAPL` | 352.78 | 345.63 | **-2.0%** | 39 | USD |
| 3 | Coca-Cola Company (The) | `KO` | 99.48 | 98.46 | **-1.0%** | 24 | USD |

Price/target uses the underlying Yahoo Finance share quote, not the OKX derivative. Minimum 3 analysts; unreliable price scales and missing coverage excluded. Targets are analyst opinions, not guaranteed forecasts.

## All OKX companies — our ratio + LONG/SHORT scores

| Company | OKX | P/S | EV/S | Op margin | Fwd P/E | EPS +1y | Rev +1y | FCF yield | LONG | SHORT |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| QUALCOMM Incorporated | `QCOM` | 4.2 | 4.4 | 20.8% | 13.8 | 27.3% | 15.5% | 5.1% | **100 CORE** | **0** |
| Rocket Lab Corporation | `RKLB` | 43.8 | 36.0 | -27.6% | 801.5 | 75.7% | 37.0% | -0.6% | **0** | **100 CORE** |
| Moderna, Inc. | `MRNA` | 34.5 | 34.1 | -80.8% | -51.4 | 39.0% | 11.3% | -0.7% | **0** | **94 WATCH** |
| Sandisk Corporation | `SNDK` | 4.0 | 3.8 | 72.7% | 2.8 | 27.1% | 23.7% | 9.8% | **90 CORE** | **10** |
| Taiwan Semiconductor Manufactur | `TSM` | 0.4 | 2.5 | 58.0% | 16.0 | 33.6% | 37.8% | 62.1% | **90 CORE** | **10** |
| USA Rare Earth, Inc. | `USAR` | 165.6 | 139.3 | -984.3% | 30.3 | 125.8% | 1039.1% | -9.6% | **0** | **86 CORE** |
| Marvell Technology, Inc. | `MRVL` | 13.8 | 13.6 | 16.8% | 19.7 | 74.7% | 64.3% | 1.8% | **85 WATCH** | **13** |
| Western Digital Corporation | `WDC` | 7.3 | 7.2 | 40.9% | 7.0 | 63.4% | 40.5% | 2.6% | **83 CORE** | **10** |
| Applovin Corporation | `APP` | 18.1 | 18.1 | 77.8% | 19.9 | 27.4% | 25.4% | 2.7% | **83 CORE** | **10** |
| Okta, Inc. | `OKTA` | 10.1 | 9.4 | 7.7% | 40.7 | 11.4% | 10.1% | 3.3% | **8** | **80 CORE** |
| AST SpaceMobile, Inc. | `ASTS` | 78.0 | 72.4 | -393.3% | -18.3 | 28.1% | 252.7% | -17.0% | **0** | **80 WATCH** |
| Tesla, Inc. | `TSLA` | 14.5 | 14.2 | 3.0% | 175.9 | 25.2% | 13.5% | 0.3% | **20** | **78** |
| Robinhood Markets, Inc. | `HOOD` | 12.8 | 12.3 | 45.7% | 21.1 | 39.7% | 29.4% | — | **77 WATCH** | **0** |
| Advanced Micro Devices, Inc. | `AMD` | 18.2 | 18.1 | 17.8% | 28.6 | 118.2% | 83.6% | 0.9% | **77 WATCH** | **13** |
| Corning Incorporated | `GLW` | 5.2 | 5.6 | 16.8% | 23.3 | 34.8% | 21.2% | 1.0% | **77 WATCH** | **13** |
| NVIDIA Corporation | `NVDA` | 12.4 | 12.3 | 65.2% | 9.9 | 69.8% | 67.2% | 1.1% | **75 WATCH** | **18** |
| AXT Inc | `AXT` | 14.8 | 12.4 | 19.6% | 15.1 | 116.3% | 115.9% | 0.7% | **75 WATCH** | **28** |
| Credo Technology Group Holding  | `CRDO` | 14.3 | 13.8 | 31.7% | 12.4 | 53.9% | 55.0% | 1.1% | **75 WATCH** | **28** |
| Applied Materials, Inc. | `AMAT` | 8.1 | 8.0 | 32.9% | 14.2 | 27.7% | 20.8% | 0.9% | **75 WATCH** | **18** |
| Broadcom Inc. | `AVGO` | 17.9 | 18.3 | 48.8% | 17.2 | 66.4% | 65.1% | 1.9% | **75 WATCH** | **28** |
| Micron Technology, Inc. | `MU` | 6.1 | 5.8 | 74.6% | 3.5 | 17.7% | 16.0% | 3.6% | **75 CORE** | **30** |
| Dell Technologies Inc. | `DELL` | 1.3 | 1.5 | 9.9% | 10.5 | 17.9% | 19.7% | 3.0% | **75 CORE** | **30** |
| IonQ, Inc. | `IONQ` | 32.3 | 27.8 | -306.3% | -18.6 | -41.0% | 71.2% | -1.0% | **0** | **75 WATCH** |
| Cerebras Systems Inc. | `CBRS` | 32.5 | 24.7 | -99.3% | 54.3 | 543.3% | 217.9% | — | **0** | **71 WATCH** |
| Oracle Corporation | `ORCL` | 5.2 | 6.9 | 34.3% | 10.8 | 35.7% | 45.7% | -12.3% | **70 WATCH** | **10** |
| Adobe Inc. | `ADBE` | 3.7 | 3.7 | 36.3% | 9.0 | 12.0% | 9.1% | 9.8% | **65 WATCH** | **30** |
| Circle Internet Group, Inc. | `CRCL` | 4.9 | 4.3 | 11.3% | 40.5 | 0.5% | 24.1% | 1.8% | **15** | **63 CORE** |
| XIAOMI-W | `XIAOMI` | 1.8 | 1.5 | 4.7% | 20.5 | 39.5% | 19.2% | -1.1% | **62 WATCH** | **10** |
| Coherent Corp. | `COHR` | 5.1 | 5.4 | 14.1% | 12.9 | 51.7% | 39.4% | -4.2% | **60 WATCH** | **35** |
| Microsoft Corporation | `MSFT` | 11.1 | 11.3 | 47.1% | 21.4 | 20.9% | 20.5% | 0.1% | **59 WATCH** | **3** |
| Apple Inc. | `AAPL` | 10.7 | 10.8 | 33.0% | 33.4 | 12.4% | 8.1% | 2.1% | **5** | **58** |
| Coca-Cola Company (The) | `KO` | 8.4 | 8.9 | 32.2% | 28.2 | 5.7% | -3.1% | 1.0% | **0** | **58** |
| Meta Platforms, Inc. | `META` | 6.6 | 6.8 | 37.8% | 17.6 | 16.6% | 21.8% | 1.1% | **57 WATCH** | **38** |
| IREN LIMITED | `IREN` | 10.0 | 19.6 | -72.9% | 60.7 | 116.3% | 199.7% | — | **0** | **55** |
| Netflix, Inc. | `NFLX` | 5.0 | 5.2 | 31.3% | 16.1 | 5.1% | 10.7% | 10.2% | **35** | **50** |
| Nebius Group N.V. | `NBIS` | 14.3 | 18.3 | -18.7% | -35.0 | -1706.3% | 288.2% | -65.0% | **0** | **50** |
| Palantir Technologies Inc. | `PLTR` | 53.0 | 51.6 | 45.6% | 63.2 | 49.2% | 53.3% | 0.7% | **45** | **48** |
| Bloom Energy Corporation | `BE` | 13.7 | 13.8 | 14.3% | 33.3 | 62.7% | 56.4% | -0.0% | **45** | **35** |
| SamsungElec | `SAMSUNG` | 2.1 | 1.8 | 46.1% | 2.4 | 63.5% | 41.2% | 6.8% | **45** | **10** |
| Super Micro Computer, Inc. | `SMCI` | 0.3 | 0.4 | 8.3% | 3.6 | 6.5% | 11.3% | -49.7% | **35** | **45** |
| Arm Holdings plc | `ARM` | 34.3 | 33.7 | 17.0% | 56.7 | 36.2% | 37.2% | 0.6% | **43** | **33** |
| CoreWeave, Inc. | `CRWV` | 2.8 | 9.1 | -0.5% | -28.1 | 23.4% | 106.6% | -70.8% | **0** | **40** |
| SOFTBANK GROUP CORP | `SOFTBANK` | 2.2 | 5.9 | -6.3% | 11.0 | 208.4% | 6.0% | -5.6% | **0** | **40** |
| Coinbase Global, Inc. | `COIN` | 5.8 | 5.5 | 0.1% | 48.8 | 866.1% | 26.2% | 11.6% | **35** | **25** |
| SK hynix | `SKHYNIX` | 2.9 | 2.6 | 74.5% | 2.1 | 49.4% | 60.5% | — | **30** | **5** |
| Lumentum Holdings Inc. | `LITE` | 13.2 | 13.1 | 23.4% | 13.6 | 60.9% | 57.9% | 0.3% | **30** | **23** |
| SK hynix | `SKHY` | 2.9 | 2.6 | 74.5% | 2.1 | 49.4% | 60.5% | — | **30** | **5** |
| Alphabet Inc. | `GOOGL` | 7.4 | 7.2 | 33.3% | 18.7 | -23.8% | 27.2% | -0.0% | **5** | **30** |
| Amazon.com, Inc. | `AMZN` | 3.5 | 3.7 | 13.1% | 23.6 | -16.5% | 15.7% | -1.2% | **0** | **30** |
| Intel Corporation | `INTC` | 4.9 | 5.1 | 10.3% | 31.0 | 20.4% | 12.0% | 0.3% | **5** | **28** |
| Fluence Energy, Inc. | `FLNC` | 0.3 | 0.3 | -4.2% | -8.1 | 59.3% | 25.4% | 0.3% | **5** | **28** |
| Strategy Inc | `MSTR` | 88.1 | 116.0 | -1100.1% | 6.0 | 417.1% | 3.1% | -7.4% | **25** | **25** |
| BitMine Immersion Technologies, | `BMNR` | 81.6 | 79.4 | -216.3% | 17.3 | 105.7% | 197.6% | -1.0% | **25** | **25** |
| Applied Optoelectronics, Inc. | `AAOI` | 5.5 | 5.1 | -6.8% | 12.0 | 439.3% | 135.1% | -31.9% | **10** | **25** |
| Hyperliquid Strategies Inc | `PURR` | 106.5 | 94.3 | 6252.0% | 40.5 | -79.8% | 22.8% | — | **0** | **25 WATCH** |

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
