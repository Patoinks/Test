# OKX Long / Short Fundamental Scanner

Hourly scanner restricted to public companies exposed by the **OKX EEA TradFi / Stock Perpetual API universe**.

**Last scan:** 2026-11-16 22:15 UTC  
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
| 1 | Sandisk Corporation | SNDK | -8.6% | -8.7% | -8.7% | 90 | +7 | **97** | **CORE** | yes |
| 2 | Marvell Technology, Inc. | MRVL | -7.3% | -6.0% | -6.6% | 90 | +5 | **95** | **CORE** | yes |
| 3 | Taiwan Semiconductor Manufactur | TSM | -6.3% | -3.9% | -5.1% | 88 | +4 | **92** | **CORE** | yes |
| 4 | AXT Inc | AXT | -8.1% | -10.4% | -9.2% | 82 | +7 | **89** | **CORE** | yes |
| 5 | Credo Technology Group Holding  | CRDO | -8.2% | -9.2% | -8.7% | 82 | +7 | **89** | **CORE** | yes |
| 6 | NVIDIA Corporation | NVDA | -4.1% | -12.6% | -8.4% | 82 | +7 | **89** | **CORE** | yes |
| 7 | Robinhood Markets, Inc. | HOOD | -7.4% | -13.5% | -10.5% | 80 | +8 | **88** | **CORE** | yes |
| 8 | QUALCOMM Incorporated | QCOM | -2.3% | -1.7% | -2.0% | 85 | +2 | **87** | **CORE** | yes |
| 9 | Advanced Micro Devices, Inc. | AMD | -5.6% | -0.8% | -3.2% | 84 | +3 | **87** | **CORE** | yes |
| 10 | Corning Incorporated | GLW | -6.9% | -8.4% | -7.7% | 80 | +6 | **86** | **CORE** | yes |

## Final model + Price Timing — SHORT

| Rank | Company | OKX | 24h | 7d | 50/50 move | Base SHORT | Timing adj. | Final | Signal | Prev. SHORT? |
|---:|---|---|---:|---:|---:|---:|---:|---:|---|---|
| 1 | Rocket Lab Corporation | RKLB | -6.8% | -2.5% | -4.6% | 100 | -4 | **96** | **CORE** | yes |
| 2 | Moderna, Inc. | MRNA | -3.6% | -20.0% | -11.8% | 94 | -9 | **85** | **CORE** | yes |
| 3 | USA Rare Earth, Inc. | USAR | -12.6% | -18.6% | -15.6% | 86 | -12 | **74** | **WATCH** | yes |
| 4 | Cerebras Systems Inc. | CBRS | -7.1% | 4.4% | -1.3% | 75 | -1 | **74** | **WATCH** | yes |
| 5 | AST SpaceMobile, Inc. | ASTS | -12.3% | -22.5% | -17.4% | 80 | -14 | **66** | **WATCH** | yes |
| 6 | IonQ, Inc. | IONQ | -8.4% | -25.2% | -16.8% | 79 | -13 | **66** | **WATCH** | yes |
| 7 | Tesla, Inc. | TSLA | -2.7% | 0.4% | -1.1% | 59 | -1 | **58** | **WATCH** | yes |

## Combined model — LONG

Weighted score: **70% fundamental + 30% P/E trend**.

| Rank | Company | OKX | Fundamental LONG | P/E trend LONG | Combined | Signal |
|---:|---|---|---:|---:|---:|---|
| 1 | Sandisk Corporation | `SNDK` | 90 | 90 | **90** | **CORE** |
| 2 | Marvell Technology, Inc. | `MRVL` | 85 | 100 | **90** | **CORE** |
| 3 | Taiwan Semiconductor Manufactur | `TSM` | 90 | 85 | **88** | **CORE** |
| 4 | QUALCOMM Incorporated | `QCOM` | 100 | 50 | **85** | **CORE** |
| 5 | Advanced Micro Devices, Inc. | `AMD` | 77 | 100 | **84** | **CORE** |
| 6 | Western Digital Corporation | `WDC` | 83 | 80 | **82** | **CORE** |
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
| 5 | IonQ, Inc. | `IONQ` | 79 | 0 | **79** | **WATCH** |
| 6 | Cerebras Systems Inc. | `CBRS` | 75 | 0 | **75** | **WATCH** |
| 7 | Tesla, Inc. | `TSLA` | 78 | 15 | **59** | **WATCH** |

## P/E Compression + Growth — LONG

| Rank | Company | OKX | Trail P/E | Fwd P/E | P/E change | EPS +1y | Rev +1y | Rev trend | LONG score | Signal |
|---:|---|---|---:|---:|---:|---:|---:|---|---:|---|
| 1 | Marvell Technology, Inc. | `MRVL` | 47.8 | 19.7 | -58.8% | 74.2% | 63.9% | accelerating | **100** | **CORE** |
| 2 | NVIDIA Corporation | `NVDA` | 19.7 | 9.9 | -50.1% | 69.8% | 67.2% | decelerating | **100** | **CORE** |
| 3 | AXT Inc | `AXT` | 78.5 | 15.1 | -80.8% | 116.3% | 115.9% | decelerating | **100** | **CORE** |
| 4 | Credo Technology Group Holding  | `CRDO` | 42.8 | 12.4 | -71.0% | 53.9% | 55.0% | decelerating | **100** | **CORE** |
| 5 | Advanced Micro Devices, Inc. | `AMD` | 107.8 | 28.6 | -73.5% | 118.2% | 83.6% | accelerating | **100** | **CORE** |
| 6 | Broadcom Inc. | `AVGO` | 42.6 | 17.1 | -59.8% | 66.4% | 65.1% | decelerating | **100** | **CORE** |
| 7 | Coherent Corp. | `COHR` | 42.1 | 12.9 | -69.4% | 51.7% | 39.4% | decelerating | **100** | **CORE** |
| 8 | Bloom Energy Corporation | `BE` | 112.9 | 33.3 | -70.5% | 62.7% | 56.4% | decelerating | **96** | **CORE** |
| 9 | Oracle Corporation | `ORCL` | 18.7 | 10.8 | -42.3% | 35.7% | 45.7% | accelerating | **95** | **CORE** |
| 10 | Arm Holdings plc | `ARM` | 201.2 | 56.9 | -71.7% | 35.6% | 37.3% | accelerating | **95** | **CORE** |

## P/E Expansion + Weakening — SHORT

| Rank | Company | OKX | Trail P/E | Fwd P/E | P/E change | EPS +1y | Rev +1y | Rev trend | SHORT score | Signal |
|---:|---|---|---:|---:|---:|---:|---:|---|---:|---|
| 1 | Hyperliquid Strategies Inc | `PURR` | 3.5 | 40.5 | 1051.2% | -79.8% | 22.8% | decelerating | **80** | **CORE** |
| 2 | Alphabet Inc. | `GOOGL` | 14.8 | 18.7 | 26.1% | -23.8% | 27.2% | accelerating | **50** | **WATCH** |

## Top SHORT candidates

| Rank | Company | OKX market | SHORT score | Signal | P/S | EV/S | Op margin | Fwd P/E | Rev +1y | FCF yield |
|---:|---|---|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Rocket Lab Corporation | `RKLB-USDT-SWAP` | **100** | **CORE** | 43.8 | 39.0 | -27.6% | 801.5 | 37.0% | -0.6% |
| 2 | Moderna, Inc. | `MRNA-USDT-SWAP` | **94** | **WATCH** | 34.5 | 35.4 | -80.8% | -51.7 | 10.8% | -0.7% |
| 3 | USA Rare Earth, Inc. | `USAR-USDT-SWAP` | **86** | **CORE** | 165.6 | 163.5 | -984.3% | 30.3 | 1007.2% | -9.6% |
| 4 | AST SpaceMobile, Inc. | `ASTS-USDT-SWAP` | **80** | **WATCH** | 78.0 | 80.9 | -393.3% | -18.3 | 252.7% | -17.0% |
| 5 | IonQ, Inc. | `IONQ-USDT-SWAP` | **79** | **WATCH** | 32.3 | 30.5 | -306.3% | -18.6 | 71.2% | -1.0% |
| 6 | Cerebras Systems Inc. | `CBRS-USDT-SWAP` | **75** | **WATCH** | 32.5 | 27.1 | -99.3% | 54.3 | 217.9% | — |
| 7 | Circle Internet Group, Inc. | `CRCL-USDT-SWAP` | **63** | **CORE** | 4.9 | 4.7 | 11.3% | 40.5 | 24.1% | 1.8% |
| 8 | Okta, Inc. | `OKTA-USDT-SWAP` | **60** | **WATCH** | 10.1 | 9.7 | 7.7% | 40.7 | 10.1% | 3.3% |
| 9 | Hyperliquid Strategies Inc | `PURR-USDT-SWAP` | **25** | **WATCH** | 106.5 | 99.3 | 6252.0% | 40.5 | 22.8% | — |

## Top LONG candidates

| Rank | Company | OKX market | LONG score | Signal | P/S | EV/S | Op margin | Fwd P/E | Rev +1y | FCF yield |
|---:|---|---|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | QUALCOMM Incorporated | `QCOM-USDT-SWAP` | **100** | **CORE** | 4.2 | 4.5 | 20.8% | 13.8 | 15.5% | 5.1% |
| 2 | Taiwan Semiconductor Manufactur | `TSM-USDT-SWAP` | **90** | **CORE** | 0.4 | 2.7 | 58.0% | 16.0 | 37.8% | 62.1% |
| 3 | Sandisk Corporation | `SNDK-USDT-SWAP` | **90** | **CORE** | 4.0 | 4.2 | 72.7% | 2.8 | 23.7% | 9.8% |
| 4 | Marvell Technology, Inc. | `MRVL-USDT-SWAP` | **85** | **WATCH** | 13.8 | 14.7 | 16.8% | 19.7 | 63.9% | 1.8% |
| 5 | Applovin Corporation | `APP-USDT-SWAP` | **83** | **CORE** | 18.1 | 17.9 | 77.8% | 19.9 | 25.4% | 2.7% |
| 6 | Western Digital Corporation | `WDC-USDT-SWAP` | **83** | **CORE** | 7.3 | 7.6 | 40.9% | 7.0 | 40.5% | 2.6% |
| 7 | Corning Incorporated | `GLW-USDT-SWAP` | **77** | **WATCH** | 5.2 | 6.0 | 16.8% | 23.4 | 21.2% | 1.0% |
| 8 | Robinhood Markets, Inc. | `HOOD-USDT-SWAP` | **77** | **WATCH** | 12.8 | 13.4 | 45.7% | 21.1 | 29.4% | — |
| 9 | Advanced Micro Devices, Inc. | `AMD-USDT-SWAP` | **77** | **WATCH** | 18.2 | 19.1 | 17.8% | 28.6 | 83.6% | 0.9% |
| 10 | Dell Technologies Inc. | `DELL-USDT-SWAP` | **75** | **CORE** | 1.3 | 1.6 | 9.9% | 10.5 | 19.6% | 3.0% |

## Analyst consensus (12-month price target) — most upside

| Rank | Company | OKX | Price | Analyst mean target | Gap | Analysts | Currency |
|---:|---|---|---:|---:|---:|---:|---|
| 1 | SK hynix | `SKHYNIX` | 1120000.00 | 3056126.80 | **172.9%** | 39 | KRW |
| 2 | Hyperliquid Strategies Inc | `PURR` | 8.31 | 22.50 | **170.8%** | 4 | USD |
| 3 | Sandisk Corporation | `SNDK` | 809.11 | 2047.38 | **153.0%** | 24 | USD |
| 4 | SamsungElec | `SAMSUNG` | 196800.00 | 475628.56 | **141.7%** | 35 | KRW |
| 5 | Applied Optoelectronics, Inc. | `AAOI` | 45.16 | 109.00 | **141.4%** | 5 | USD |
| 6 | AXT Inc | `AXT` | 38.46 | 91.50 | **137.9%** | 6 | USD |
| 7 | CoreWeave, Inc. | `CRWV` | 49.88 | 115.34 | **131.2%** | 38 | USD |
| 8 | Credo Technology Group Holding  | `CRDO` | 120.71 | 277.47 | **129.9%** | 19 | USD |
| 9 | Strategy Inc | `MSTR` | 103.03 | 233.27 | **126.4%** | 15 | USD |
| 10 | AST SpaceMobile, Inc. | `ASTS` | 28.58 | 63.35 | **121.7%** | 12 | USD |
| 11 | Nebius Group N.V. | `NBIS` | 107.13 | 234.50 | **118.9%** | 20 | USD |
| 12 | Western Digital Corporation | `WDC` | 280.93 | 613.38 | **118.3%** | 24 | USD |
| 13 | Micron Technology, Inc. | `MU` | 719.02 | 1561.91 | **117.2%** | 45 | USD |
| 14 | Marvell Technology, Inc. | `MRVL` | 145.36 | 310.32 | **113.5%** | 40 | USD |
| 15 | SOFTBANK GROUP CORP | `SOFTBANK` | 3416.00 | 7229.58 | **111.6%** | 18 | JPY |

## Analyst consensus (12-month price target) — most downside

| Rank | Company | OKX | Price | Analyst mean target | Gap | Analysts | Currency |
|---:|---|---|---:|---:|---:|---:|---|
| 1 | Moderna, Inc. | `MRNA` | 215.27 | 158.47 | **-26.4%** | 19 | USD |
| 2 | Apple Inc. | `AAPL` | 352.78 | 345.63 | **-2.0%** | 39 | USD |
| 3 | Coca-Cola Company (The) | `KO` | 99.48 | 98.43 | **-1.1%** | 23 | USD |

Price/target uses the underlying Yahoo Finance share quote, not the OKX derivative. Minimum 3 analysts; unreliable price scales and missing coverage excluded. Targets are analyst opinions, not guaranteed forecasts.

## All OKX companies — our ratio + LONG/SHORT scores

| Company | OKX | P/S | EV/S | Op margin | Fwd P/E | EPS +1y | Rev +1y | FCF yield | LONG | SHORT |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| QUALCOMM Incorporated | `QCOM` | 4.2 | 4.5 | 20.8% | 13.8 | 27.3% | 15.5% | 5.1% | **100 CORE** | **0** |
| Rocket Lab Corporation | `RKLB` | 43.8 | 39.0 | -27.6% | 801.5 | 78.0% | 37.0% | -0.6% | **0** | **100 CORE** |
| Moderna, Inc. | `MRNA` | 34.5 | 35.4 | -80.8% | -51.7 | 39.9% | 10.8% | -0.7% | **0** | **94 WATCH** |
| Sandisk Corporation | `SNDK` | 4.0 | 4.2 | 72.7% | 2.8 | 27.1% | 23.7% | 9.8% | **90 CORE** | **10** |
| Taiwan Semiconductor Manufactur | `TSM` | 0.4 | 2.7 | 58.0% | 16.0 | 33.6% | 37.8% | 62.1% | **90 CORE** | **10** |
| USA Rare Earth, Inc. | `USAR` | 165.6 | 163.5 | -984.3% | 30.3 | 45.1% | 1007.2% | -9.6% | **0** | **86 CORE** |
| Marvell Technology, Inc. | `MRVL` | 13.8 | 14.7 | 16.8% | 19.7 | 74.2% | 63.9% | 1.8% | **85 WATCH** | **13** |
| Western Digital Corporation | `WDC` | 7.3 | 7.6 | 40.9% | 7.0 | 63.4% | 40.5% | 2.6% | **83 CORE** | **10** |
| Applovin Corporation | `APP` | 18.1 | 17.9 | 77.8% | 19.9 | 27.4% | 25.4% | 2.7% | **83 CORE** | **10** |
| AST SpaceMobile, Inc. | `ASTS` | 78.0 | 80.9 | -393.3% | -18.3 | 28.1% | 252.7% | -17.0% | **0** | **80 WATCH** |
| IonQ, Inc. | `IONQ` | 32.3 | 30.5 | -306.3% | -18.6 | -41.0% | 71.2% | -1.0% | **0** | **79 WATCH** |
| Tesla, Inc. | `TSLA` | 14.5 | 14.6 | 3.0% | 175.9 | 25.2% | 13.5% | 0.3% | **20** | **78** |
| Robinhood Markets, Inc. | `HOOD` | 12.8 | 13.4 | 45.7% | 21.1 | 39.7% | 29.4% | — | **77 WATCH** | **0** |
| Advanced Micro Devices, Inc. | `AMD` | 18.2 | 19.1 | 17.8% | 28.6 | 118.2% | 83.6% | 0.9% | **77 WATCH** | **13** |
| Corning Incorporated | `GLW` | 5.2 | 6.0 | 16.8% | 23.4 | 34.6% | 21.2% | 1.0% | **77 WATCH** | **13** |
| NVIDIA Corporation | `NVDA` | 12.4 | 12.9 | 65.2% | 9.9 | 69.8% | 67.2% | 1.1% | **75 WATCH** | **18** |
| AXT Inc | `AXT` | 14.8 | 13.7 | 19.6% | 15.1 | 116.3% | 115.9% | 0.7% | **75 WATCH** | **28** |
| Credo Technology Group Holding  | `CRDO` | 14.3 | 15.1 | 31.7% | 12.4 | 53.9% | 55.0% | 1.1% | **75 WATCH** | **28** |
| Broadcom Inc. | `AVGO` | 17.9 | 19.0 | 48.8% | 17.1 | 66.4% | 65.1% | 1.9% | **75 WATCH** | **28** |
| Micron Technology, Inc. | `MU` | 6.1 | 6.3 | 74.6% | 3.5 | 17.7% | 16.0% | 3.6% | **75 CORE** | **30** |
| Dell Technologies Inc. | `DELL` | 1.3 | 1.6 | 9.9% | 10.5 | 17.9% | 19.6% | 3.0% | **75 CORE** | **30** |
| Applied Materials, Inc. | `AMAT` | 8.1 | 8.4 | 32.9% | 14.2 | 28.8% | 20.9% | 0.9% | **75 WATCH** | **18** |
| Cerebras Systems Inc. | `CBRS` | 32.5 | 27.1 | -99.3% | 54.3 | 543.3% | 217.9% | — | **0** | **75 WATCH** |
| Oracle Corporation | `ORCL` | 5.2 | 7.2 | 34.3% | 10.8 | 35.7% | 45.7% | -12.3% | **70 WATCH** | **10** |
| XIAOMI-W | `XIAOMI` | 1.7 | 1.5 | 4.7% | 19.7 | 39.5% | 19.2% | -1.2% | **70 WATCH** | **10** |
| Adobe Inc. | `ADBE` | 3.7 | 3.7 | 36.3% | 9.0 | 12.0% | 9.1% | 9.8% | **65 WATCH** | **30** |
| Circle Internet Group, Inc. | `CRCL` | 4.9 | 4.7 | 11.3% | 40.5 | 0.5% | 24.1% | 1.8% | **15** | **63 CORE** |
| Coherent Corp. | `COHR` | 5.1 | 5.8 | 14.1% | 12.9 | 51.7% | 39.4% | -4.2% | **60 WATCH** | **35** |
| Okta, Inc. | `OKTA` | 10.1 | 9.7 | 7.7% | 40.7 | 18.5% | 10.1% | 3.3% | **20** | **60 WATCH** |
| Microsoft Corporation | `MSFT` | 11.1 | 11.4 | 47.1% | 21.4 | 20.9% | 20.5% | 0.1% | **59 WATCH** | **3** |
| IREN LIMITED | `IREN` | 10.0 | 20.7 | -72.9% | 60.7 | 116.3% | 199.7% | — | **0** | **59** |
| Apple Inc. | `AAPL` | 10.7 | 10.9 | 33.0% | 33.4 | 12.4% | 8.1% | 2.1% | **5** | **58** |
| Coca-Cola Company (The) | `KO` | 8.4 | 8.9 | 32.2% | 28.2 | 5.7% | -3.1% | 1.0% | **0** | **58** |
| Meta Platforms, Inc. | `META` | 6.6 | 6.9 | 37.8% | 17.6 | 16.8% | 21.7% | 1.1% | **57 WATCH** | **38** |
| Netflix, Inc. | `NFLX` | 5.0 | 5.3 | 31.3% | 16.1 | 5.1% | 10.7% | 10.2% | **35** | **50** |
| Nebius Group N.V. | `NBIS` | 14.3 | 19.5 | -18.7% | -35.0 | -1750.0% | 288.2% | -65.0% | **0** | **50** |
| Palantir Technologies Inc. | `PLTR` | 53.0 | 54.1 | 45.6% | 63.3 | 49.2% | 53.3% | 0.7% | **45** | **48** |
| Bloom Energy Corporation | `BE` | 13.7 | 14.9 | 14.3% | 33.3 | 62.7% | 56.4% | -0.0% | **45** | **35** |
| SamsungElec | `SAMSUNG` | 2.2 | 1.8 | 46.1% | 2.5 | 62.3% | 40.9% | 6.5% | **45** | **10** |
| Super Micro Computer, Inc. | `SMCI` | 0.3 | 0.4 | 8.3% | 3.6 | 6.5% | 11.3% | -49.7% | **35** | **45** |
| Arm Holdings plc | `ARM` | 34.3 | 36.7 | 17.0% | 56.9 | 35.6% | 37.3% | 0.6% | **43** | **33** |
| CoreWeave, Inc. | `CRWV` | 2.8 | 9.3 | -0.5% | -28.1 | 23.4% | 106.6% | -70.8% | **0** | **40** |
| SOFTBANK GROUP CORP | `SOFTBANK` | 2.3 | 5.9 | -6.3% | 11.6 | 2027.4% | 6.0% | -5.3% | **0** | **40** |
| Coinbase Global, Inc. | `COIN` | 5.8 | 5.9 | 0.1% | 48.8 | 825.3% | 26.2% | 11.6% | **35** | **25** |
| SK hynix | `SKHYNIX` | 2.9 | 2.6 | 74.5% | 2.1 | 49.4% | 60.5% | — | **30** | **5** |
| Lumentum Holdings Inc. | `LITE` | 13.2 | 14.3 | 23.4% | 13.6 | 60.9% | 57.9% | 0.3% | **30** | **23** |
| SK hynix | `SKHY` | 2.9 | 2.6 | 74.5% | 2.1 | 49.4% | 60.5% | — | **30** | **5** |
| Alphabet Inc. | `GOOGL` | 7.4 | 7.5 | 33.3% | 18.7 | -23.8% | 27.2% | -0.0% | **5** | **30** |
| Amazon.com, Inc. | `AMZN` | 3.5 | 3.9 | 13.1% | 23.6 | -16.5% | 15.7% | -1.2% | **0** | **30** |
| Intel Corporation | `INTC` | 4.9 | 5.5 | 10.3% | 31.0 | 20.4% | 12.0% | 0.3% | **5** | **28** |
| Fluence Energy, Inc. | `FLNC` | 0.3 | 0.3 | -4.2% | -8.1 | 59.3% | 25.4% | 0.3% | **5** | **28** |
| Strategy Inc | `MSTR` | 88.1 | 123.4 | -1100.1% | 6.0 | 417.1% | 3.1% | -7.4% | **25** | **25** |
| BitMine Immersion Technologies, | `BMNR` | 81.6 | 86.1 | -216.3% | 17.3 | 110.6% | 87.2% | -1.0% | **25** | **25** |
| Applied Optoelectronics, Inc. | `AAOI` | 5.5 | 5.7 | -6.8% | 12.0 | 439.3% | 135.1% | -31.9% | **10** | **25** |
| Hyperliquid Strategies Inc | `PURR` | 106.5 | 99.3 | 6252.0% | 40.5 | -79.8% | 22.8% | — | **0** | **25 WATCH** |

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
