# OKX Long / Short Fundamental Scanner

Hourly scanner restricted to public companies exposed by the **OKX EEA TradFi / Stock Perpetual API universe**.

**Last scan:** 2026-11-13 01:54 UTC  
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
| 1 | NVIDIA Corporation | NVDA | -4.3% | -8.5% | -6.4% | 82 | +5 | **87** | **CORE** | yes |
| 2 | Sandisk Corporation | SNDK | -4.1% | 16.2% | 6.1% | 90 | -5 | **85** | **CORE** | yes |
| 3 | Taiwan Semiconductor Manufactur | TSM | -1.9% | 14.8% | 6.5% | 88 | -5 | **83** | **CORE** | yes |
| 4 | QUALCOMM Incorporated | QCOM | 0.3% | 13.0% | 6.7% | 85 | -5 | **80** | **CORE** | yes |
| 5 | Robinhood Markets, Inc. | HOOD | -3.8% | 3.8% | -0.0% | 80 | +0 | **80** | **CORE** | yes |
| 6 | AXT Inc | AXT | -7.3% | 18.6% | 5.6% | 82 | -5 | **77** | **CORE** | yes |
| 7 | Marvell Technology, Inc. | MRVL | -2.6% | 23.1% | 10.3% | 84 | -8 | **76** | **CORE** | yes |
| 8 | Applovin Corporation | APP | -2.7% | 10.6% | 3.9% | 79 | -3 | **76** | **CORE** | yes |
| 9 | Applied Materials, Inc. | AMAT | -3.6% | 19.3% | 7.9% | 80 | -6 | **74** | **WATCH** | yes |
| 10 | Corning Incorporated | GLW | -0.8% | 15.5% | 7.4% | 80 | -6 | **74** | **WATCH** | yes |

## Final model + Price Timing — SHORT

| Rank | Company | OKX | 24h | 7d | 50/50 move | Base SHORT | Timing adj. | Final | Signal | Prev. SHORT? |
|---:|---|---|---:|---:|---:|---:|---:|---:|---|---|
| 1 | Rocket Lab Corporation | RKLB | -3.1% | 39.3% | 18.1% | 100 | +14 | **100** | **CORE** | yes |
| 2 | Moderna, Inc. | MRNA | -7.0% | -4.2% | -5.6% | 94 | -4 | **90** | **CORE** | yes |
| 3 | USA Rare Earth, Inc. | USAR | -2.4% | 8.8% | 3.2% | 86 | +3 | **89** | **CORE** | yes |
| 4 | AST SpaceMobile, Inc. | ASTS | -5.8% | 14.2% | 4.2% | 80 | +3 | **83** | **CORE** | yes |
| 5 | IonQ, Inc. | IONQ | -9.4% | 16.8% | 3.7% | 79 | +3 | **82** | **CORE** | yes |
| 6 | Cerebras Systems Inc. | CBRS | -3.3% | 19.6% | 8.2% | 71 | +7 | **78** | **CORE** | yes |
| 7 | Nebius Group N.V. | NBIS | -16.8% | 6.9% | -5.0% | 72 | -4 | **68** | **WATCH** | yes |
| 8 | Tesla, Inc. | TSLA | 1.7% | 15.6% | 8.7% | 59 | +7 | **66** | **WATCH** | yes |
| 9 | Okta, Inc. | OKTA | 0.2% | 6.6% | 3.4% | 60 | +3 | **63** | **WATCH** | yes |
| 10 | IREN LIMITED | IREN | -6.5% | 8.0% | 0.8% | 59 | +1 | **60** | **WATCH** | yes |

## Combined model — LONG

Weighted score: **70% fundamental + 30% P/E trend**.

| Rank | Company | OKX | Fundamental LONG | P/E trend LONG | Combined | Signal |
|---:|---|---|---:|---:|---:|---|
| 1 | Sandisk Corporation | `SNDK` | 90 | 90 | **90** | **CORE** |
| 2 | Taiwan Semiconductor Manufactur | `TSM` | 90 | 85 | **88** | **CORE** |
| 3 | QUALCOMM Incorporated | `QCOM` | 100 | 50 | **85** | **CORE** |
| 4 | Marvell Technology, Inc. | `MRVL` | 77 | 100 | **84** | **CORE** |
| 5 | NVIDIA Corporation | `NVDA` | 75 | 100 | **82** | **CORE** |
| 6 | AXT Inc | `AXT` | 75 | 100 | **82** | **CORE** |
| 7 | Credo Technology Group Holding  | `CRDO` | 75 | 100 | **82** | **CORE** |
| 8 | Broadcom Inc. | `AVGO` | 75 | 100 | **82** | **CORE** |
| 9 | Robinhood Markets, Inc. | `HOOD` | 77 | 86 | **80** | **CORE** |
| 10 | Corning Incorporated | `GLW` | 77 | 86 | **80** | **CORE** |

## Combined model — SHORT

Weighted score: **70% fundamental + 30% P/E trend**.

| Rank | Company | OKX | Fundamental SHORT | P/E trend SHORT | Combined | Signal |
|---:|---|---|---:|---:|---:|---|
| 1 | Rocket Lab Corporation | `RKLB` | 100 | 0 | **100** | **CORE** |
| 2 | Moderna, Inc. | `MRNA` | 94 | 0 | **94** | **WATCH** |
| 3 | USA Rare Earth, Inc. | `USAR` | 86 | 0 | **86** | **CORE** |
| 4 | AST SpaceMobile, Inc. | `ASTS` | 80 | 0 | **80** | **WATCH** |
| 5 | IonQ, Inc. | `IONQ` | 79 | 0 | **79** | **WATCH** |
| 6 | Nebius Group N.V. | `NBIS` | 72 | 0 | **72** | **WATCH** |
| 7 | Cerebras Systems Inc. | `CBRS` | 71 | 0 | **71** | **WATCH** |
| 8 | Okta, Inc. | `OKTA` | 80 | 13 | **60** | **WATCH** |
| 9 | Tesla, Inc. | `TSLA` | 78 | 15 | **59** | **WATCH** |

## P/E Compression + Growth — LONG

| Rank | Company | OKX | Trail P/E | Fwd P/E | P/E change | EPS +1y | Rev +1y | Rev trend | LONG score | Signal |
|---:|---|---|---:|---:|---:|---:|---:|---|---:|---|
| 1 | NVIDIA Corporation | `NVDA` | 21.0 | 10.5 | -50.1% | 70.9% | 68.0% | decelerating | **100** | **CORE** |
| 2 | AXT Inc | `AXT` | 88.9 | 17.1 | -80.8% | 116.3% | 115.9% | decelerating | **100** | **CORE** |
| 3 | Marvell Technology, Inc. | `MRVL` | 54.1 | 22.4 | -58.6% | 74.2% | 63.9% | accelerating | **100** | **CORE** |
| 4 | Credo Technology Group Holding  | `CRDO` | 49.6 | 14.4 | -71.0% | 53.9% | 55.0% | decelerating | **100** | **CORE** |
| 5 | Broadcom Inc. | `AVGO` | 46.5 | 18.7 | -59.8% | 66.9% | 65.6% | decelerating | **100** | **CORE** |
| 6 | Advanced Micro Devices, Inc. | `AMD` | 125.1 | 33.1 | -73.5% | 118.8% | 83.5% | accelerating | **100** | **CORE** |
| 7 | Coherent Corp. | `COHR` | 48.0 | 14.7 | -69.4% | 51.7% | 39.9% | decelerating | **100** | **CORE** |
| 8 | Oracle Corporation | `ORCL` | 19.9 | 11.5 | -42.3% | 35.7% | 45.7% | accelerating | **95** | **CORE** |
| 9 | Arm Holdings plc | `ARM` | 229.6 | 65.0 | -71.7% | 35.5% | 37.3% | accelerating | **95** | **CORE** |
| 10 | Bloom Energy Corporation | `BE` | 122.4 | 37.9 | -69.0% | 62.7% | 56.4% | decelerating | **92** | **CORE** |

## P/E Expansion + Weakening — SHORT

| Rank | Company | OKX | Trail P/E | Fwd P/E | P/E change | EPS +1y | Rev +1y | Rev trend | SHORT score | Signal |
|---:|---|---|---:|---:|---:|---:|---:|---|---:|---|
| 1 | Hyperliquid Strategies Inc | `PURR` | 3.7 | 43.0 | 1051.2% | -79.8% | 22.8% | decelerating | **80** | **CORE** |
| 2 | Alphabet Inc. | `GOOGL` | 15.6 | 19.4 | 24.1% | -23.5% | 27.6% | accelerating | **50** | **WATCH** |

## Top SHORT candidates

| Rank | Company | OKX market | SHORT score | Signal | P/S | EV/S | Op margin | Fwd P/E | Rev +1y | FCF yield |
|---:|---|---|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Rocket Lab Corporation | `RKLB-USDT-SWAP` | **100** | **CORE** | 48.9 | 40.8 | -27.6% | 895.1 | 37.6% | -0.5% |
| 2 | Moderna, Inc. | `MRNA-USDT-SWAP` | **94** | **WATCH** | 37.1 | 36.7 | -80.8% | -56.0 | 10.6% | -0.6% |
| 3 | USA Rare Earth, Inc. | `USAR-USDT-SWAP` | **86** | **CORE** | 187.3 | 98.4 | -1476.1% | -11.8 | 1245.4% | -10.2% |
| 4 | Okta, Inc. | `OKTA-USDT-SWAP` | **80** | **CORE** | 10.4 | 9.7 | 7.7% | 41.7 | 10.1% | 3.3% |
| 5 | AST SpaceMobile, Inc. | `ASTS-USDT-SWAP` | **80** | **WATCH** | 94.2 | 84.9 | -393.3% | -22.1 | 249.8% | -14.1% |
| 6 | IonQ, Inc. | `IONQ-USDT-SWAP` | **79** | **WATCH** | 37.7 | 32.8 | -306.3% | -22.0 | 70.7% | -0.8% |
| 7 | Nebius Group N.V. | `NBIS-USDT-SWAP` | **72** | **WATCH** | 24.1 | 27.6 | -37.4% | -37.0 | 267.0% | -29.4% |
| 8 | Cerebras Systems Inc. | `CBRS-USDT-SWAP` | **71** | **WATCH** | 34.1 | 24.7 | -81.2% | 76.4 | 233.1% | — |
| 9 | Circle Internet Group, Inc. | `CRCL-USDT-SWAP` | **63** | **CORE** | 5.4 | 4.9 | 11.3% | 44.8 | 24.1% | 1.6% |
| 10 | Hyperliquid Strategies Inc | `PURR-USDT-SWAP` | **25** | **WATCH** | 112.9 | 100.6 | 6252.0% | 43.0 | 22.8% | — |

## Top LONG candidates

| Rank | Company | OKX market | LONG score | Signal | P/S | EV/S | Op margin | Fwd P/E | Rev +1y | FCF yield |
|---:|---|---|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | QUALCOMM Incorporated | `QCOM-USDT-SWAP` | **100** | **CORE** | 4.4 | 4.6 | 20.8% | 14.5 | 15.6% | 4.8% |
| 2 | Taiwan Semiconductor Manufactur | `TSM-USDT-SWAP` | **90** | **CORE** | 0.4 | 2.8 | 58.0% | 17.3 | 37.8% | 57.2% |
| 3 | Sandisk Corporation | `SNDK-USDT-SWAP` | **90** | **CORE** | 4.6 | 4.4 | 72.7% | 3.2 | 23.7% | 8.4% |
| 4 | Applovin Corporation | `APP-USDT-SWAP` | **83** | **CORE** | 17.1 | 17.2 | 77.8% | 18.9 | 25.2% | 2.9% |
| 5 | Corning Incorporated | `GLW-USDT-SWAP` | **77** | **WATCH** | 5.8 | 6.2 | 16.8% | 26.3 | 21.2% | 0.8% |
| 6 | Robinhood Markets, Inc. | `HOOD-USDT-SWAP` | **77** | **WATCH** | 14.4 | 14.0 | 45.7% | 23.8 | 29.2% | — |
| 7 | Marvell Technology, Inc. | `MRVL-USDT-SWAP` | **77** | **WATCH** | 15.7 | 15.4 | 16.8% | 22.4 | 63.9% | 1.6% |
| 8 | Dell Technologies Inc. | `DELL-USDT-SWAP` | **75** | **CORE** | 1.6 | 1.7 | 9.9% | 12.2 | 19.5% | 2.6% |
| 9 | Applied Materials, Inc. | `AMAT-USDT-SWAP` | **75** | **WATCH** | 9.8 | 9.7 | 31.2% | 15.8 | 21.0% | 1.0% |
| 10 | Broadcom Inc. | `AVGO-USDT-SWAP` | **75** | **WATCH** | 19.5 | 19.9 | 48.8% | 18.7 | 65.6% | 1.8% |

## Analyst consensus (12-month price target) — most upside

| Rank | Company | OKX | Price | Analyst mean target | Gap | Analysts | Currency |
|---:|---|---|---:|---:|---:|---:|---|
| 1 | IREN LIMITED | `IREN` | 19.48 | 56.69 | **191.0%** | 19 | USD |
| 2 | Hyperliquid Strategies Inc | `PURR` | 8.80 | 22.50 | **155.5%** | 4 | USD |
| 3 | Cerebras Systems Inc. | `CBRS` | 97.75 | 245.18 | **150.8%** | 11 | USD |
| 4 | SK hynix | `SKHYNIX` | 1280000.00 | 3097152.20 | **142.0%** | 39 | KRW |
| 5 | SamsungElec | `SAMSUNG` | 213250.00 | 475628.56 | **123.0%** | 35 | KRW |
| 6 | Sandisk Corporation | `SNDK` | 937.46 | 2047.38 | **118.4%** | 24 | USD |
| 7 | Nebius Group N.V. | `NBIS` | 128.64 | 278.05 | **116.1%** | 20 | USD |
| 8 | CoreWeave, Inc. | `CRWV` | 56.60 | 121.26 | **114.2%** | 38 | USD |
| 9 | SOFTBANK GROUP CORP | `SOFTBANK` | 3632.00 | 7656.31 | **110.8%** | 18 | JPY |
| 10 | AXT Inc | `AXT` | 43.54 | 91.50 | **110.2%** | 6 | USD |
| 11 | Applied Optoelectronics, Inc. | `AAOI` | 52.85 | 109.00 | **106.2%** | 5 | USD |
| 12 | Strategy Inc | `MSTR` | 114.41 | 233.27 | **103.9%** | 15 | USD |
| 13 | Credo Technology Group Holding  | `CRDO` | 139.81 | 284.05 | **103.2%** | 19 | USD |
| 14 | Western Digital Corporation | `WDC` | 311.21 | 613.38 | **97.1%** | 24 | USD |
| 15 | Micron Technology, Inc. | `MU` | 798.44 | 1561.91 | **95.6%** | 45 | USD |

## Analyst consensus (12-month price target) — most downside

| Rank | Company | OKX | Price | Analyst mean target | Gap | Analysts | Currency |
|---:|---|---|---:|---:|---:|---:|---|
| 1 | Moderna, Inc. | `MRNA` | 231.35 | 158.47 | **-31.5%** | 19 | USD |
| 2 | Apple Inc. | `AAPL` | 354.88 | 344.62 | **-2.9%** | 40 | USD |

Price/target uses the underlying Yahoo Finance share quote, not the OKX derivative. Minimum 3 analysts; unreliable price scales and missing coverage excluded. Targets are analyst opinions, not guaranteed forecasts.

## All OKX companies — our ratio + LONG/SHORT scores

| Company | OKX | P/S | EV/S | Op margin | Fwd P/E | EPS +1y | Rev +1y | FCF yield | LONG | SHORT |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| QUALCOMM Incorporated | `QCOM` | 4.4 | 4.6 | 20.8% | 14.5 | 27.3% | 15.6% | 4.8% | **100 CORE** | **0** |
| Rocket Lab Corporation | `RKLB` | 48.9 | 40.8 | -27.6% | 895.1 | 77.3% | 37.6% | -0.5% | **0** | **100 CORE** |
| Moderna, Inc. | `MRNA` | 37.1 | 36.7 | -80.8% | -56.0 | 41.1% | 10.6% | -0.6% | **0** | **94 WATCH** |
| Sandisk Corporation | `SNDK` | 4.6 | 4.4 | 72.7% | 3.2 | 27.1% | 23.7% | 8.4% | **90 CORE** | **10** |
| Taiwan Semiconductor Manufactur | `TSM` | 0.4 | 2.8 | 58.0% | 17.3 | 33.6% | 37.8% | 57.2% | **90 CORE** | **10** |
| USA Rare Earth, Inc. | `USAR` | 187.3 | 98.4 | -1476.1% | -11.8 | 105.3% | 1245.4% | -10.2% | **0** | **86 CORE** |
| Applovin Corporation | `APP` | 17.1 | 17.2 | 77.8% | 18.9 | 27.4% | 25.2% | 2.9% | **83 CORE** | **10** |
| Okta, Inc. | `OKTA` | 10.4 | 9.7 | 7.7% | 41.7 | 11.4% | 10.1% | 3.3% | **8** | **80 CORE** |
| AST SpaceMobile, Inc. | `ASTS` | 94.2 | 84.9 | -393.3% | -22.1 | 28.8% | 249.8% | -14.1% | **0** | **80 WATCH** |
| IonQ, Inc. | `IONQ` | 37.7 | 32.8 | -306.3% | -22.0 | -39.3% | 70.7% | -0.8% | **0** | **79 WATCH** |
| Tesla, Inc. | `TSLA` | 15.2 | 14.9 | 3.0% | 184.1 | 25.2% | 13.5% | 0.3% | **20** | **78** |
| Robinhood Markets, Inc. | `HOOD` | 14.4 | 14.0 | 45.7% | 23.8 | 39.7% | 29.2% | — | **77 WATCH** | **0** |
| Marvell Technology, Inc. | `MRVL` | 15.7 | 15.4 | 16.8% | 22.4 | 74.2% | 63.9% | 1.6% | **77 WATCH** | **13** |
| Corning Incorporated | `GLW` | 5.8 | 6.2 | 16.8% | 26.3 | 34.6% | 21.2% | 0.8% | **77 WATCH** | **13** |
| NVIDIA Corporation | `NVDA` | 13.2 | 13.1 | 65.2% | 10.5 | 70.9% | 68.0% | 1.0% | **75 WATCH** | **18** |
| AXT Inc | `AXT` | 16.7 | 14.4 | 19.6% | 17.1 | 116.3% | 115.9% | — | **75 WATCH** | **20** |
| Applied Materials, Inc. | `AMAT` | 9.8 | 9.7 | 31.2% | 15.8 | 28.8% | 21.0% | 1.0% | **75 WATCH** | **18** |
| Credo Technology Group Holding  | `CRDO` | 16.5 | 16.1 | 31.7% | 14.4 | 53.9% | 55.0% | 0.9% | **75 WATCH** | **28** |
| Western Digital Corporation | `WDC` | 8.0 | 8.0 | 40.9% | 7.7 | 63.4% | 40.5% | 2.3% | **75 WATCH** | **18** |
| Broadcom Inc. | `AVGO` | 19.5 | 19.9 | 48.8% | 18.7 | 66.9% | 65.6% | 1.8% | **75 WATCH** | **28** |
| Micron Technology, Inc. | `MU` | 6.8 | 6.5 | 74.6% | 3.8 | 17.7% | 16.0% | 3.2% | **75 CORE** | **30** |
| Dell Technologies Inc. | `DELL` | 1.6 | 1.7 | 9.9% | 12.2 | 16.8% | 19.5% | 2.6% | **75 CORE** | **30** |
| Nebius Group N.V. | `NBIS` | 24.1 | 27.6 | -37.4% | -37.0 | -191.4% | 267.0% | -29.4% | **0** | **72 WATCH** |
| Cerebras Systems Inc. | `CBRS` | 34.1 | 24.7 | -81.2% | 76.4 | 370.9% | 233.1% | — | **0** | **71 WATCH** |
| Oracle Corporation | `ORCL` | 5.5 | 7.3 | 34.3% | 11.5 | 35.7% | 45.7% | -11.6% | **70 WATCH** | **10** |
| Advanced Micro Devices, Inc. | `AMD` | 21.1 | 21.0 | 17.8% | 33.1 | 118.8% | 83.5% | 0.8% | **70 WATCH** | **13** |
| Adobe Inc. | `ADBE` | 3.6 | 3.6 | 36.3% | 8.7 | 12.0% | 9.1% | 10.1% | **65 WATCH** | **30** |
| Circle Internet Group, Inc. | `CRCL` | 5.4 | 4.9 | 11.3% | 44.8 | 0.5% | 24.1% | 1.6% | **15** | **63 CORE** |
| XIAOMI-W | `XIAOMI` | 1.7 | 1.6 | 4.7% | 20.2 | 39.5% | 19.2% | -1.1% | **62 WATCH** | **10** |
| Coherent Corp. | `COHR` | 5.8 | 6.2 | 14.1% | 14.7 | 51.7% | 39.9% | -3.7% | **60 WATCH** | **35** |
| Microsoft Corporation | `MSFT` | 11.2 | 11.4 | 47.1% | 21.6 | 20.9% | 20.5% | 0.1% | **59 WATCH** | **3** |
| IREN LIMITED | `IREN` | 11.9 | 21.5 | -72.9% | 72.1 | 116.3% | 199.7% | — | **0** | **59** |
| Apple Inc. | `AAPL` | 10.8 | 10.9 | 33.0% | 33.7 | 12.2% | 8.2% | 2.0% | **5** | **58** |
| Coca-Cola Company (The) | `KO` | 8.2 | 8.8 | 32.2% | 27.6 | 5.7% | -3.1% | 1.0% | **0** | **58** |
| Meta Platforms, Inc. | `META` | 6.6 | 6.7 | 37.8% | 17.5 | 16.7% | 21.7% | 1.1% | **57 WATCH** | **38** |
| Netflix, Inc. | `NFLX` | 5.2 | 5.4 | 31.3% | 16.6 | 5.1% | 10.7% | 9.9% | **35** | **50** |
| Palantir Technologies Inc. | `PLTR` | 56.7 | 55.3 | 45.6% | 67.7 | 49.2% | 53.5% | 0.6% | **45** | **48** |
| Bloom Energy Corporation | `BE` | 15.6 | 15.7 | 14.3% | 37.9 | 62.7% | 56.4% | -0.0% | **45** | **35** |
| SamsungElec | `SAMSUNG` | 2.3 | 2.0 | 46.1% | 2.8 | 62.3% | 40.9% | 6.0% | **45** | **10** |
| Super Micro Computer, Inc. | `SMCI` | 0.3 | 0.4 | 8.3% | 3.9 | 6.5% | 11.3% | -46.0% | **35** | **45** |
| Arm Holdings plc | `ARM` | 39.1 | 38.6 | 17.0% | 65.0 | 35.5% | 37.3% | 0.5% | **43** | **33** |
| CoreWeave, Inc. | `CRWV` | 3.2 | 9.5 | -0.5% | -32.6 | 13.3% | 107.4% | -63.1% | **0** | **40** |
| SOFTBANK GROUP CORP | `SOFTBANK` | 2.5 | 6.1 | -6.1% | 12.3 | 87.5% | 6.3% | -6.7% | **0** | **40** |
| Coinbase Global, Inc. | `COIN` | 6.4 | 6.0 | 0.1% | 53.9 | 782.5% | 27.1% | 10.6% | **35** | **25** |
| Lumentum Holdings Inc. | `LITE` | 15.1 | 15.0 | 23.4% | 15.6 | 60.9% | 57.9% | 0.3% | **20** | **33** |
| SK hynix | `SKHYNIX` | 3.4 | 3.0 | 74.5% | 2.4 | 48.7% | 60.4% | — | **30** | **5** |
| SK hynix | `SKHY` | 3.4 | 3.0 | 74.5% | 2.4 | 48.7% | 60.4% | — | **30** | **5** |
| Alphabet Inc. | `GOOGL` | 7.8 | 7.6 | 33.3% | 19.4 | -23.5% | 27.6% | -0.0% | **5** | **30** |
| Amazon.com, Inc. | `AMZN` | 3.6 | 3.9 | 13.1% | 24.5 | -16.6% | 15.8% | -1.2% | **0** | **30** |
| Intel Corporation | `INTC` | 5.4 | 5.6 | 10.3% | 34.2 | 20.4% | 12.0% | 0.2% | **5** | **28** |
| Fluence Energy, Inc. | `FLNC` | 0.4 | 0.3 | -4.2% | -8.9 | 59.3% | 25.4% | 0.3% | **5** | **28** |
| BitMine Immersion Technologies, | `BMNR` | 92.6 | 92674.4 | -216.6% | 19.6 | 105.8% | 58.9% | -1.4% | **25** | **25** |
| Strategy Inc | `MSTR` | 97.8 | 125.7 | -1100.1% | 6.6 | 380.1% | 3.2% | -6.7% | **25** | **25** |
| Applied Optoelectronics, Inc. | `AAOI` | 6.4 | 6.1 | -6.8% | 14.1 | 439.3% | 135.1% | -27.3% | **10** | **25** |
| Hyperliquid Strategies Inc | `PURR` | 112.9 | 100.6 | 6252.0% | 43.0 | -79.8% | 22.8% | — | **0** | **25 WATCH** |

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
