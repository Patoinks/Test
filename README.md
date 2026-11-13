# OKX Long / Short Fundamental Scanner

Hourly scanner restricted to public companies exposed by the **OKX EEA TradFi / Stock Perpetual API universe**.

**Last scan:** 2026-11-13 17:50 UTC  
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
| 1 | Sandisk Corporation | SNDK | -7.9% | 3.4% | -2.3% | 90 | +2 | **92** | **CORE** | yes |
| 2 | NVIDIA Corporation | NVDA | -3.2% | -13.8% | -8.5% | 82 | +7 | **89** | **CORE** | yes |
| 3 | Taiwan Semiconductor Manufactur | TSM | -2.3% | 5.6% | 1.6% | 88 | -1 | **87** | **CORE** | yes |
| 4 | QUALCOMM Incorporated | QCOM | -3.1% | 3.8% | 0.3% | 85 | +0 | **85** | **CORE** | yes |
| 5 | AXT Inc | AXT | -7.8% | 3.3% | -2.2% | 82 | +2 | **84** | **CORE** | yes |
| 6 | Marvell Technology, Inc. | MRVL | -6.1% | 9.3% | 1.6% | 84 | -1 | **83** | **CORE** | yes |
| 7 | Robinhood Markets, Inc. | HOOD | -3.8% | -3.3% | -3.5% | 80 | +3 | **83** | **CORE** | yes |
| 8 | Advanced Micro Devices, Inc. | AMD | -10.6% | 16.5% | 2.9% | 84 | -2 | **82** | **CORE** | yes |
| 9 | Credo Technology Group Holding  | CRDO | -6.9% | 8.0% | 0.5% | 82 | +0 | **82** | **CORE** | yes |
| 10 | Western Digital Corporation | WDC | -6.4% | 10.5% | 2.1% | 82 | -2 | **80** | **CORE** | yes |

## Final model + Price Timing — SHORT

| Rank | Company | OKX | 24h | 7d | 50/50 move | Base SHORT | Timing adj. | Final | Signal | Prev. SHORT? |
|---:|---|---|---:|---:|---:|---:|---:|---:|---|---|
| 1 | Rocket Lab Corporation | RKLB | -4.9% | 14.9% | 5.0% | 100 | +4 | **100** | **CORE** | yes |
| 2 | Moderna, Inc. | MRNA | -2.8% | -11.6% | -7.2% | 94 | -6 | **88** | **CORE** | yes |
| 3 | USA Rare Earth, Inc. | USAR | -0.9% | -2.8% | -1.9% | 86 | -1 | **85** | **CORE** | yes |
| 4 | Cerebras Systems Inc. | CBRS | 11.2% | 21.2% | 16.2% | 71 | +13 | **84** | **CORE** | yes |
| 5 | AST SpaceMobile, Inc. | ASTS | -6.1% | 0.2% | -2.9% | 80 | -2 | **78** | **CORE** | yes |
| 6 | IonQ, Inc. | IONQ | -6.5% | -11.6% | -9.0% | 79 | -7 | **72** | **WATCH** | yes |
| 7 | Okta, Inc. | OKTA | -0.5% | 7.7% | 3.6% | 60 | +3 | **63** | **WATCH** | yes |
| 8 | Tesla, Inc. | TSLA | -1.7% | 9.1% | 3.7% | 59 | +3 | **62** | **WATCH** | yes |

## Combined model — LONG

Weighted score: **70% fundamental + 30% P/E trend**.

| Rank | Company | OKX | Fundamental LONG | P/E trend LONG | Combined | Signal |
|---:|---|---|---:|---:|---:|---|
| 1 | Sandisk Corporation | `SNDK` | 90 | 90 | **90** | **CORE** |
| 2 | Taiwan Semiconductor Manufactur | `TSM` | 90 | 85 | **88** | **CORE** |
| 3 | QUALCOMM Incorporated | `QCOM` | 100 | 50 | **85** | **CORE** |
| 4 | Marvell Technology, Inc. | `MRVL` | 77 | 100 | **84** | **CORE** |
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
| 6 | Cerebras Systems Inc. | `CBRS` | 71 | 0 | **71** | **WATCH** |
| 7 | Okta, Inc. | `OKTA` | 80 | 13 | **60** | **WATCH** |
| 8 | Tesla, Inc. | `TSLA` | 78 | 15 | **59** | **WATCH** |

## P/E Compression + Growth — LONG

| Rank | Company | OKX | Trail P/E | Fwd P/E | P/E change | EPS +1y | Rev +1y | Rev trend | LONG score | Signal |
|---:|---|---|---:|---:|---:|---:|---:|---|---:|---|
| 1 | NVIDIA Corporation | `NVDA` | 20.3 | 10.1 | -50.1% | 70.0% | 67.3% | decelerating | **100** | **CORE** |
| 2 | AXT Inc | `AXT` | 82.0 | 15.8 | -80.8% | 116.3% | 115.9% | decelerating | **100** | **CORE** |
| 3 | Marvell Technology, Inc. | `MRVL` | 50.8 | 21.0 | -58.6% | 74.2% | 63.9% | accelerating | **100** | **CORE** |
| 4 | Advanced Micro Devices, Inc. | `AMD` | 111.8 | 29.6 | -73.5% | 118.8% | 83.6% | accelerating | **100** | **CORE** |
| 5 | Credo Technology Group Holding  | `CRDO` | 46.1 | 13.4 | -71.0% | 53.9% | 55.0% | decelerating | **100** | **CORE** |
| 6 | Broadcom Inc. | `AVGO` | 44.1 | 17.7 | -59.8% | 66.9% | 65.6% | decelerating | **100** | **CORE** |
| 7 | Coherent Corp. | `COHR` | 44.1 | 13.5 | -69.4% | 51.7% | 39.9% | decelerating | **100** | **CORE** |
| 8 | Oracle Corporation | `ORCL` | 19.5 | 11.2 | -42.3% | 35.7% | 45.7% | accelerating | **95** | **CORE** |
| 9 | Arm Holdings plc | `ARM` | 216.7 | 61.3 | -71.7% | 35.6% | 37.3% | accelerating | **95** | **CORE** |
| 10 | Bloom Energy Corporation | `BE` | 115.8 | 35.9 | -69.0% | 62.7% | 56.4% | decelerating | **92** | **CORE** |

## P/E Expansion + Weakening — SHORT

| Rank | Company | OKX | Trail P/E | Fwd P/E | P/E change | EPS +1y | Rev +1y | Rev trend | SHORT score | Signal |
|---:|---|---|---:|---:|---:|---:|---:|---|---:|---|
| 1 | Hyperliquid Strategies Inc | `PURR` | 3.7 | 43.1 | 1051.2% | -79.8% | 22.8% | decelerating | **80** | **CORE** |
| 2 | Alphabet Inc. | `GOOGL` | 15.4 | 19.1 | 24.1% | -23.5% | 27.6% | accelerating | **50** | **WATCH** |

## Top SHORT candidates

| Rank | Company | OKX market | SHORT score | Signal | P/S | EV/S | Op margin | Fwd P/E | Rev +1y | FCF yield |
|---:|---|---|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Rocket Lab Corporation | `RKLB-USDT-SWAP` | **100** | **CORE** | 46.5 | 40.8 | -27.6% | 851.6 | 37.0% | -0.5% |
| 2 | Moderna, Inc. | `MRNA-USDT-SWAP` | **94** | **WATCH** | 36.0 | 36.7 | -80.8% | -54.5 | 10.6% | -0.6% |
| 3 | USA Rare Earth, Inc. | `USAR-USDT-SWAP` | **86** | **CORE** | 185.5 | 98.4 | -1476.1% | -11.7 | 1031.4% | -10.3% |
| 4 | Okta, Inc. | `OKTA-USDT-SWAP` | **80** | **CORE** | 10.3 | 9.7 | 7.7% | 41.5 | 10.1% | 3.3% |
| 5 | AST SpaceMobile, Inc. | `ASTS-USDT-SWAP` | **80** | **WATCH** | 88.5 | 84.9 | -393.3% | -20.8 | 252.7% | -15.0% |
| 6 | IonQ, Inc. | `IONQ-USDT-SWAP` | **79** | **WATCH** | 35.2 | 32.8 | -306.3% | -20.3 | 71.2% | -0.9% |
| 7 | Cerebras Systems Inc. | `CBRS-USDT-SWAP` | **71** | **WATCH** | 34.2 | 23.6 | -99.3% | 82.7 | 228.6% | — |
| 8 | Circle Internet Group, Inc. | `CRCL-USDT-SWAP` | **63** | **CORE** | 5.3 | 4.8 | 11.3% | 44.0 | 24.1% | 1.6% |
| 9 | Hyperliquid Strategies Inc | `PURR-USDT-SWAP` | **25** | **WATCH** | 113.3 | 100.6 | 6252.0% | 43.1 | 22.8% | — |

## Top LONG candidates

| Rank | Company | OKX market | LONG score | Signal | P/S | EV/S | Op margin | Fwd P/E | Rev +1y | FCF yield |
|---:|---|---|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | QUALCOMM Incorporated | `QCOM-USDT-SWAP` | **100** | **CORE** | 4.3 | 4.6 | 20.8% | 14.1 | 15.5% | 5.0% |
| 2 | Taiwan Semiconductor Manufactur | `TSM-USDT-SWAP` | **90** | **CORE** | 0.4 | 2.8 | 58.0% | 16.9 | 37.8% | 58.5% |
| 3 | Sandisk Corporation | `SNDK-USDT-SWAP` | **90** | **CORE** | 4.2 | 4.4 | 72.7% | 3.0 | 23.7% | 9.2% |
| 4 | Applovin Corporation | `APP-USDT-SWAP` | **83** | **CORE** | 17.9 | 17.2 | 77.8% | 19.7 | 25.4% | 2.7% |
| 5 | Western Digital Corporation | `WDC-USDT-SWAP` | **83** | **CORE** | 7.5 | 8.0 | 40.9% | 7.2 | 40.5% | 2.5% |
| 6 | Corning Incorporated | `GLW-USDT-SWAP` | **77** | **WATCH** | 5.5 | 6.2 | 16.8% | 24.8 | 21.2% | 0.9% |
| 7 | Robinhood Markets, Inc. | `HOOD-USDT-SWAP` | **77** | **WATCH** | 13.9 | 14.0 | 45.7% | 22.9 | 29.2% | — |
| 8 | Marvell Technology, Inc. | `MRVL-USDT-SWAP` | **77** | **WATCH** | 14.7 | 15.4 | 16.8% | 21.0 | 63.9% | 1.7% |
| 9 | Advanced Micro Devices, Inc. | `AMD-USDT-SWAP` | **77** | **WATCH** | 18.9 | 21.0 | 17.8% | 29.6 | 83.6% | 0.9% |
| 10 | Dell Technologies Inc. | `DELL-USDT-SWAP` | **75** | **CORE** | 1.4 | 1.7 | 9.9% | 11.2 | 20.3% | 2.8% |

## Analyst consensus (12-month price target) — most upside

| Rank | Company | OKX | Price | Analyst mean target | Gap | Analysts | Currency |
|---:|---|---|---:|---:|---:|---:|---|
| 1 | SK hynix | `SKHYNIX` | 1216000.00 | 3097152.20 | **154.7%** | 39 | KRW |
| 2 | Hyperliquid Strategies Inc | `PURR` | 8.84 | 22.50 | **154.5%** | 4 | USD |
| 3 | Sandisk Corporation | `SNDK` | 863.28 | 2047.38 | **137.2%** | 24 | USD |
| 4 | Nebius Group N.V. | `NBIS` | 116.40 | 271.20 | **133.0%** | 20 | USD |
| 5 | SamsungElec | `SAMSUNG` | 206000.00 | 475628.56 | **130.9%** | 35 | KRW |
| 6 | CoreWeave, Inc. | `CRWV` | 52.06 | 120.08 | **130.6%** | 38 | USD |
| 7 | AXT Inc | `AXT` | 40.16 | 91.50 | **127.8%** | 6 | USD |
| 8 | Applied Optoelectronics, Inc. | `AAOI` | 48.93 | 109.00 | **122.8%** | 5 | USD |
| 9 | Cerebras Systems Inc. | `CBRS` | 108.68 | 239.73 | **120.6%** | 11 | USD |
| 10 | Credo Technology Group Holding  | `CRDO` | 130.12 | 284.05 | **118.3%** | 19 | USD |
| 11 | Strategy Inc | `MSTR` | 110.60 | 233.27 | **110.9%** | 15 | USD |
| 12 | Western Digital Corporation | `WDC` | 291.39 | 613.38 | **110.5%** | 24 | USD |
| 13 | SOFTBANK GROUP CORP | `SOFTBANK` | 3547.00 | 7396.25 | **108.5%** | 18 | JPY |
| 14 | Micron Technology, Inc. | `MU` | 764.42 | 1561.91 | **104.3%** | 45 | USD |
| 15 | Marvell Technology, Inc. | `MRVL` | 154.37 | 310.32 | **101.0%** | 40 | USD |

## Analyst consensus (12-month price target) — most downside

| Rank | Company | OKX | Price | Analyst mean target | Gap | Analysts | Currency |
|---:|---|---|---:|---:|---:|---:|---|
| 1 | Moderna, Inc. | `MRNA` | 224.82 | 158.47 | **-29.5%** | 19 | USD |
| 2 | Apple Inc. | `AAPL` | 357.89 | 344.62 | **-3.7%** | 40 | USD |
| 3 | Coca-Cola Company (The) | `KO` | 99.12 | 98.43 | **-0.7%** | 23 | USD |

Price/target uses the underlying Yahoo Finance share quote, not the OKX derivative. Minimum 3 analysts; unreliable price scales and missing coverage excluded. Targets are analyst opinions, not guaranteed forecasts.

## All OKX companies — our ratio + LONG/SHORT scores

| Company | OKX | P/S | EV/S | Op margin | Fwd P/E | EPS +1y | Rev +1y | FCF yield | LONG | SHORT |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| QUALCOMM Incorporated | `QCOM` | 4.3 | 4.6 | 20.8% | 14.1 | 27.3% | 15.5% | 5.0% | **100 CORE** | **0** |
| Rocket Lab Corporation | `RKLB` | 46.5 | 40.8 | -27.6% | 851.6 | 75.3% | 37.0% | -0.5% | **0** | **100 CORE** |
| Moderna, Inc. | `MRNA` | 36.0 | 36.7 | -80.8% | -54.5 | 40.6% | 10.6% | -0.6% | **0** | **94 WATCH** |
| Sandisk Corporation | `SNDK` | 4.2 | 4.4 | 72.7% | 3.0 | 27.1% | 23.7% | 9.2% | **90 CORE** | **10** |
| Taiwan Semiconductor Manufactur | `TSM` | 0.4 | 2.8 | 58.0% | 16.9 | 33.6% | 37.8% | 58.5% | **90 CORE** | **10** |
| USA Rare Earth, Inc. | `USAR` | 185.5 | 98.4 | -1476.1% | -11.7 | 45.1% | 1031.4% | -10.3% | **0** | **86 CORE** |
| Western Digital Corporation | `WDC` | 7.5 | 8.0 | 40.9% | 7.2 | 63.4% | 40.5% | 2.5% | **83 CORE** | **10** |
| Applovin Corporation | `APP` | 17.9 | 17.2 | 77.8% | 19.7 | 27.4% | 25.4% | 2.7% | **83 CORE** | **10** |
| Okta, Inc. | `OKTA` | 10.3 | 9.7 | 7.7% | 41.5 | 11.4% | 10.1% | 3.3% | **8** | **80 CORE** |
| AST SpaceMobile, Inc. | `ASTS` | 88.5 | 84.9 | -393.3% | -20.8 | 28.8% | 252.7% | -15.0% | **0** | **80 WATCH** |
| IonQ, Inc. | `IONQ` | 35.2 | 32.8 | -306.3% | -20.3 | -41.0% | 71.2% | -0.9% | **0** | **79 WATCH** |
| Tesla, Inc. | `TSLA` | 14.9 | 14.9 | 3.0% | 181.0 | 25.2% | 13.5% | 0.3% | **20** | **78** |
| Robinhood Markets, Inc. | `HOOD` | 13.9 | 14.0 | 45.7% | 22.9 | 39.7% | 29.2% | — | **77 WATCH** | **0** |
| Marvell Technology, Inc. | `MRVL` | 14.7 | 15.4 | 16.8% | 21.0 | 74.2% | 63.9% | 1.7% | **77 WATCH** | **13** |
| Advanced Micro Devices, Inc. | `AMD` | 18.9 | 21.0 | 17.8% | 29.6 | 118.8% | 83.6% | 0.9% | **77 WATCH** | **13** |
| Corning Incorporated | `GLW` | 5.5 | 6.2 | 16.8% | 24.8 | 34.6% | 21.2% | 0.9% | **77 WATCH** | **13** |
| NVIDIA Corporation | `NVDA` | 12.8 | 13.1 | 65.2% | 10.1 | 70.0% | 67.3% | 1.1% | **75 WATCH** | **18** |
| AXT Inc | `AXT` | 15.4 | 14.4 | 19.6% | 15.8 | 116.3% | 115.9% | — | **75 WATCH** | **20** |
| Credo Technology Group Holding  | `CRDO` | 15.4 | 16.1 | 31.7% | 13.4 | 53.9% | 55.0% | 1.0% | **75 WATCH** | **28** |
| Broadcom Inc. | `AVGO` | 18.5 | 19.9 | 48.8% | 17.7 | 66.9% | 65.6% | 1.9% | **75 WATCH** | **28** |
| Dell Technologies Inc. | `DELL` | 1.4 | 1.7 | 9.9% | 11.2 | 17.9% | 20.3% | 2.8% | **75 CORE** | **30** |
| Micron Technology, Inc. | `MU` | 6.5 | 6.5 | 74.6% | 3.7 | 17.7% | 16.0% | 3.4% | **75 CORE** | **30** |
| Applied Materials, Inc. | `AMAT` | 8.4 | 8.7 | 32.9% | 14.8 | 28.1% | 20.3% | 0.6% | **75 WATCH** | **18** |
| Cerebras Systems Inc. | `CBRS` | 34.2 | 23.6 | -99.3% | 82.7 | 373.2% | 228.6% | — | **0** | **71 WATCH** |
| Oracle Corporation | `ORCL` | 5.4 | 7.3 | 34.3% | 11.2 | 35.7% | 45.7% | -11.8% | **70 WATCH** | **10** |
| XIAOMI-W | `XIAOMI` | 1.7 | 1.5 | 4.7% | 19.6 | 39.5% | 19.2% | -1.2% | **70 WATCH** | **10** |
| Adobe Inc. | `ADBE` | 3.6 | 3.6 | 36.3% | 8.8 | 12.0% | 9.1% | 9.9% | **65 WATCH** | **30** |
| Circle Internet Group, Inc. | `CRCL` | 5.3 | 4.8 | 11.3% | 44.0 | 0.5% | 24.1% | 1.6% | **15** | **63 CORE** |
| Nebius Group N.V. | `NBIS` | 21.8 | 27.6 | -37.4% | -39.8 | -10709.8% | 273.5% | -32.5% | **0** | **62** |
| Coherent Corp. | `COHR` | 5.3 | 6.2 | 14.1% | 13.5 | 51.7% | 39.9% | -4.0% | **60 WATCH** | **35** |
| Microsoft Corporation | `MSFT` | 11.2 | 11.4 | 47.1% | 21.7 | 20.9% | 20.5% | 0.1% | **59 WATCH** | **3** |
| IREN LIMITED | `IREN` | 10.9 | 21.5 | -72.9% | 66.2 | 116.3% | 199.7% | — | **0** | **59** |
| Apple Inc. | `AAPL` | 10.9 | 10.8 | 33.0% | 33.9 | 12.3% | 8.1% | 2.0% | **5** | **58** |
| Coca-Cola Company (The) | `KO` | 8.4 | 8.8 | 32.2% | 28.1 | 5.7% | -3.1% | 1.0% | **0** | **58** |
| Meta Platforms, Inc. | `META` | 6.7 | 6.7 | 37.8% | 17.9 | 16.7% | 21.7% | 1.0% | **57 WATCH** | **38** |
| Netflix, Inc. | `NFLX` | 5.1 | 5.4 | 31.3% | 16.5 | 5.1% | 10.7% | 9.9% | **35** | **50** |
| Palantir Technologies Inc. | `PLTR` | 55.5 | 55.3 | 45.6% | 66.3 | 49.2% | 53.5% | 0.7% | **45** | **48** |
| Bloom Energy Corporation | `BE` | 14.8 | 15.7 | 14.3% | 35.9 | 62.7% | 56.4% | -0.0% | **45** | **35** |
| SamsungElec | `SAMSUNG` | 2.3 | 1.9 | 46.1% | 2.7 | 62.3% | 40.9% | 6.2% | **45** | **10** |
| Super Micro Computer, Inc. | `SMCI` | 0.3 | 0.4 | 8.3% | 3.8 | 6.5% | 11.3% | -46.9% | **35** | **45** |
| Arm Holdings plc | `ARM` | 36.9 | 38.6 | 17.0% | 61.3 | 35.6% | 37.3% | 0.6% | **43** | **33** |
| CoreWeave, Inc. | `CRWV` | 2.9 | 9.5 | -0.5% | -30.3 | 13.9% | 107.4% | -67.8% | **0** | **40** |
| SOFTBANK GROUP CORP | `SOFTBANK` | 2.4 | 6.0 | -6.3% | 12.0 | 339.8% | 6.3% | -5.1% | **0** | **40** |
| Coinbase Global, Inc. | `COIN` | 6.3 | 6.0 | 0.1% | 53.2 | 815.7% | 27.1% | 10.8% | **35** | **25** |
| SK hynix | `SKHYNIX` | 3.2 | 2.9 | 74.5% | 2.3 | 48.7% | 60.4% | — | **30** | **5** |
| Lumentum Holdings Inc. | `LITE` | 14.3 | 15.0 | 23.4% | 14.7 | 60.9% | 57.9% | 0.3% | **30** | **23** |
| SK hynix | `SKHY` | 3.2 | 2.9 | 74.5% | 2.3 | 48.7% | 60.4% | — | **30** | **5** |
| Alphabet Inc. | `GOOGL` | 7.7 | 7.6 | 33.3% | 19.1 | -23.5% | 27.6% | -0.0% | **5** | **30** |
| Amazon.com, Inc. | `AMZN` | 3.6 | 3.9 | 13.1% | 24.3 | -16.6% | 15.7% | -1.2% | **0** | **30** |
| Intel Corporation | `INTC` | 5.2 | 5.6 | 10.3% | 32.8 | 20.4% | 12.0% | 0.3% | **5** | **28** |
| Fluence Energy, Inc. | `FLNC` | 0.3 | 0.3 | -4.2% | -8.7 | 59.3% | 25.4% | 0.3% | **5** | **28** |
| Strategy Inc | `MSTR` | 94.6 | 125.7 | -1100.1% | 6.4 | 380.1% | 3.2% | -6.9% | **25** | **25** |
| BitMine Immersion Technologies, | `BMNR` | 88.5 | 90.4 | -216.3% | 18.8 | 105.8% | 58.9% | -0.9% | **25** | **25** |
| Applied Optoelectronics, Inc. | `AAOI` | 5.9 | 6.1 | -6.8% | 13.0 | 439.3% | 135.1% | -29.5% | **10** | **25** |
| Hyperliquid Strategies Inc | `PURR` | 113.3 | 100.6 | 6252.0% | 43.1 | -79.8% | 22.8% | — | **0** | **25 WATCH** |

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
