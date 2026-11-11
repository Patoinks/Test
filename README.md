# OKX Long / Short Fundamental Scanner

Hourly scanner restricted to public companies exposed by the **OKX EEA TradFi / Stock Perpetual API universe**.

**Last scan:** 2026-11-11 06:39 UTC  
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
| 1 | Sandisk Corporation | SNDK | 0.0% | -17.1% | -8.6% | 90 | +7 | **97** | **CORE** | yes |
| 2 | AXT Inc | AXT | -0.0% | -17.3% | -8.7% | 82 | +7 | **89** | **CORE** | yes |
| 3 | Taiwan Semiconductor Manufactur | TSM | -0.0% | 0.2% | 0.1% | 88 | +0 | **88** | **CORE** | yes |
| 4 | NVIDIA Corporation | NVDA | 0.0% | -15.6% | -7.8% | 82 | +6 | **88** | **CORE** | yes |
| 5 | Western Digital Corporation | WDC | -0.0% | -10.7% | -5.3% | 82 | +4 | **86** | **CORE** | yes |
| 6 | QUALCOMM Incorporated | QCOM | 0.0% | 0.2% | 0.1% | 85 | +0 | **85** | **CORE** | yes |
| 7 | Marvell Technology, Inc. | MRVL | 0.0% | -3.4% | -1.7% | 84 | +1 | **85** | **CORE** | yes |
| 8 | Credo Technology Group Holding  | CRDO | -0.0% | -4.9% | -2.5% | 82 | +2 | **84** | **CORE** | yes |
| 9 | Robinhood Markets, Inc. | HOOD | -0.0% | -7.0% | -3.5% | 80 | +3 | **83** | **CORE** | yes |
| 10 | Advanced Micro Devices, Inc. | AMD | -0.0% | 5.4% | 2.7% | 84 | -2 | **82** | **CORE** | yes |

## Final model + Price Timing — SHORT

| Rank | Company | OKX | 24h | 7d | 50/50 move | Base SHORT | Timing adj. | Final | Signal | Prev. SHORT? |
|---:|---|---|---:|---:|---:|---:|---:|---:|---|---|
| 1 | Rocket Lab Corporation | RKLB | 0.0% | 19.7% | 9.9% | 100 | +8 | **100** | **CORE** | yes |
| 2 | USA Rare Earth, Inc. | USAR | -0.0% | -3.4% | -1.7% | 100 | -1 | **99** | **CORE** | yes |
| 3 | IonQ, Inc. | IONQ | -0.0% | 18.4% | 9.2% | 82 | +7 | **89** | **CORE** | yes |
| 4 | Moderna, Inc. | MRNA | -0.0% | -2.9% | -1.5% | 82 | -1 | **81** | **CORE** | yes |
| 5 | AST SpaceMobile, Inc. | ASTS | 0.0% | -5.4% | -2.7% | 80 | -2 | **78** | **CORE** | yes |
| 6 | Nebius Group N.V. | NBIS | 0.0% | -5.3% | -2.7% | 76 | -2 | **74** | **WATCH** | yes |
| 7 | Cerebras Systems Inc. | CBRS | -0.0% | 2.0% | 1.0% | 71 | +1 | **72** | **WATCH** | yes |
| 8 | Tesla, Inc. | TSLA | 0.0% | -1.4% | -0.7% | 59 | -1 | **58** | **WATCH** | yes |
| 9 | Okta, Inc. | OKTA | -0.0% | -6.6% | -3.3% | 60 | -3 | **57** | **WATCH** | yes |
| 10 | IREN LIMITED | IREN | 0.0% | -9.1% | -4.6% | 59 | -4 | **55** | **WATCH** | no |

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
| 7 | AXT Inc | `AXT` | 75 | 100 | **82** | **CORE** |
| 8 | NVIDIA Corporation | `NVDA` | 75 | 100 | **82** | **CORE** |
| 9 | Credo Technology Group Holding  | `CRDO` | 75 | 100 | **82** | **CORE** |
| 10 | Broadcom Inc. | `AVGO` | 75 | 100 | **82** | **CORE** |

## Combined model — SHORT

Weighted score: **70% fundamental + 30% P/E trend**.

| Rank | Company | OKX | Fundamental SHORT | P/E trend SHORT | Combined | Signal |
|---:|---|---|---:|---:|---:|---|
| 1 | Rocket Lab Corporation | `RKLB` | 100 | 0 | **100** | **CORE** |
| 2 | USA Rare Earth, Inc. | `USAR` | 100 | 0 | **100** | **CORE** |
| 3 | IonQ, Inc. | `IONQ` | 82 | 0 | **82** | **WATCH** |
| 4 | Moderna, Inc. | `MRNA` | 82 | 0 | **82** | **WATCH** |
| 5 | AST SpaceMobile, Inc. | `ASTS` | 80 | 0 | **80** | **WATCH** |
| 6 | Nebius Group N.V. | `NBIS` | 76 | 0 | **76** | **WATCH** |
| 7 | Cerebras Systems Inc. | `CBRS` | 71 | 0 | **71** | **WATCH** |
| 8 | Okta, Inc. | `OKTA` | 80 | 13 | **60** | **WATCH** |
| 9 | Tesla, Inc. | `TSLA` | 78 | 15 | **59** | **WATCH** |

## P/E Compression + Growth — LONG

| Rank | Company | OKX | Trail P/E | Fwd P/E | P/E change | EPS +1y | Rev +1y | Rev trend | LONG score | Signal |
|---:|---|---|---:|---:|---:|---:|---:|---|---:|---|
| 1 | AXT Inc | `AXT` | 72.8 | 15.4 | -78.8% | 116.3% | 115.9% | decelerating | **100** | **CORE** |
| 2 | NVIDIA Corporation | `NVDA` | 21.4 | 10.6 | -50.3% | 71.0% | 68.0% | decelerating | **100** | **CORE** |
| 3 | Marvell Technology, Inc. | `MRVL` | 50.8 | 21.0 | -58.6% | 74.2% | 63.9% | accelerating | **100** | **CORE** |
| 4 | Credo Technology Group Holding  | `CRDO` | 46.0 | 13.4 | -71.0% | 53.9% | 55.0% | decelerating | **100** | **CORE** |
| 5 | Advanced Micro Devices, Inc. | `AMD` | 110.1 | 29.1 | -73.5% | 118.8% | 83.5% | accelerating | **100** | **CORE** |
| 6 | Broadcom Inc. | `AVGO` | 42.4 | 17.1 | -59.8% | 66.9% | 65.6% | decelerating | **100** | **CORE** |
| 7 | Coherent Corp. | `COHR` | 44.4 | 13.6 | -69.4% | 51.7% | 39.4% | decelerating | **100** | **CORE** |
| 8 | Bloom Energy Corporation | `BE` | 112.4 | 34.8 | -69.0% | 62.7% | 56.4% | decelerating | **96** | **CORE** |
| 9 | Oracle Corporation | `ORCL` | 18.5 | 10.7 | -42.3% | 35.7% | 45.7% | accelerating | **95** | **CORE** |
| 10 | Arm Holdings plc | `ARM` | 208.6 | 59.0 | -71.7% | 35.5% | 37.2% | accelerating | **95** | **CORE** |

## P/E Expansion + Weakening — SHORT

| Rank | Company | OKX | Trail P/E | Fwd P/E | P/E change | EPS +1y | Rev +1y | Rev trend | SHORT score | Signal |
|---:|---|---|---:|---:|---:|---:|---:|---|---:|---|
| 1 | Hyperliquid Strategies Inc | `PURR` | 3.7 | 42.7 | 1051.2% | -79.8% | 22.8% | decelerating | **80** | **CORE** |
| 2 | SOFTBANK GROUP CORP | `SOFTBANK` | 4.5 | 13.0 | 191.0% | 30.4% | 6.1% | decelerating | **61** | **WATCH** |
| 3 | Alphabet Inc. | `GOOGL` | 15.0 | 18.6 | 24.1% | -23.5% | 27.6% | accelerating | **50** | **WATCH** |

## Top SHORT candidates

| Rank | Company | OKX market | SHORT score | Signal | P/S | EV/S | Op margin | Fwd P/E | Rev +1y | FCF yield |
|---:|---|---|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Rocket Lab Corporation | `RKLB-USDT-SWAP` | **100** | **CORE** | 45.5 | 39.9 | -29.6% | 2291.2 | 38.3% | -0.6% |
| 2 | USA Rare Earth, Inc. | `USAR-USDT-SWAP` | **100** | **CORE** | 183.8 | 59.1 | -4711.6% | 264.0 | 933.3% | -10.5% |
| 3 | IonQ, Inc. | `IONQ-USDT-SWAP` | **82** | **WATCH** | 42.7 | 37.5 | -226.5% | -24.9 | 70.7% | -0.7% |
| 4 | Moderna, Inc. | `MRNA-USDT-SWAP` | **82** | **WATCH** | 40.2 | 39.8 | 10.4% | -58.7 | 11.6% | -0.6% |
| 5 | Okta, Inc. | `OKTA-USDT-SWAP` | **80** | **CORE** | 10.1 | 9.4 | 13.3% | 40.7 | 10.1% | 3.3% |
| 6 | AST SpaceMobile, Inc. | `ASTS-USDT-SWAP` | **80** | **WATCH** | 91.8 | 83.2 | -398.5% | -21.6 | 249.8% | -15.5% |
| 7 | Nebius Group N.V. | `NBIS-USDT-SWAP` | **76** | **WATCH** | 26.9 | 28.7 | -0.2% | -38.5 | 267.0% | -26.4% |
| 8 | Cerebras Systems Inc. | `CBRS-USDT-SWAP` | **71** | **WATCH** | 32.7 | 23.2 | -265.0% | 73.2 | 233.1% | — |
| 9 | Circle Internet Group, Inc. | `CRCL-USDT-SWAP` | **63** | **CORE** | 5.5 | 4.9 | 24.1% | 45.6 | 24.1% | 1.6% |
| 10 | Hyperliquid Strategies Inc | `PURR-USDT-SWAP` | **25** | **WATCH** | 112.2 | 99.9 | 6593.3% | 42.7 | 22.8% | — |

## Top LONG candidates

| Rank | Company | OKX market | LONG score | Signal | P/S | EV/S | Op margin | Fwd P/E | Rev +1y | FCF yield |
|---:|---|---|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | QUALCOMM Incorporated | `QCOM-USDT-SWAP` | **100** | **CORE** | 4.3 | 4.5 | 15.4% | 14.2 | 15.6% | 4.9% |
| 2 | Taiwan Semiconductor Manufactur | `TSM-USDT-SWAP` | **90** | **CORE** | 0.4 | 2.7 | 58.7% | 17.0 | 37.8% | 58.5% |
| 3 | Sandisk Corporation | `SNDK-USDT-SWAP` | **90** | **CORE** | 4.2 | 4.1 | 79.6% | 3.0 | 23.7% | 9.2% |
| 4 | Applovin Corporation | `APP-USDT-SWAP` | **83** | **CORE** | 17.2 | 17.3 | 78.2% | 19.0 | 24.8% | 2.8% |
| 5 | Western Digital Corporation | `WDC-USDT-SWAP` | **83** | **CORE** | 7.5 | 7.4 | 47.7% | 7.2 | 40.5% | 2.5% |
| 6 | Corning Incorporated | `GLW-USDT-SWAP` | **77** | **WATCH** | 5.5 | 5.9 | 18.9% | 24.8 | 21.0% | 0.9% |
| 7 | Robinhood Markets, Inc. | `HOOD-USDT-SWAP` | **77** | **WATCH** | 14.4 | 14.0 | 48.1% | 23.8 | 29.2% | — |
| 8 | Applied Materials, Inc. | `AMAT-USDT-SWAP` | **77** | **WATCH** | 9.6 | 9.5 | 33.7% | 20.1 | 35.4% | 1.0% |
| 9 | Marvell Technology, Inc. | `MRVL-USDT-SWAP` | **77** | **WATCH** | 14.7 | 14.5 | 16.7% | 21.0 | 63.9% | 1.7% |
| 10 | Advanced Micro Devices, Inc. | `AMD-USDT-SWAP` | **77** | **WATCH** | 18.6 | 18.5 | 21.2% | 29.1 | 83.5% | 0.9% |

## Analyst consensus (12-month price target) — most upside

| Rank | Company | OKX | Price | Analyst mean target | Gap | Analysts | Currency |
|---:|---|---|---:|---:|---:|---:|---|
| 1 | IREN LIMITED | `IREN` | 19.73 | 56.69 | **187.3%** | 19 | USD |
| 2 | CoreWeave, Inc. | `CRWV` | 48.73 | 131.53 | **169.9%** | 38 | USD |
| 3 | Cerebras Systems Inc. | `CBRS` | 93.66 | 245.18 | **161.8%** | 11 | USD |
| 4 | Hyperliquid Strategies Inc | `PURR` | 8.75 | 22.50 | **157.1%** | 4 | USD |
| 5 | SK hynix | `SKHYNIX` | 1277000.00 | 3100998.50 | **142.8%** | 39 | KRW |
| 6 | Sandisk Corporation | `SNDK` | 859.99 | 2047.38 | **138.1%** | 24 | USD |
| 7 | AXT Inc | `AXT` | 39.31 | 91.50 | **132.8%** | 6 | USD |
| 8 | SamsungElec | `SAMSUNG` | 206000.00 | 475628.56 | **130.9%** | 35 | KRW |
| 9 | Applied Optoelectronics, Inc. | `AAOI` | 48.32 | 109.00 | **125.6%** | 5 | USD |
| 10 | Credo Technology Group Holding  | `CRDO` | 129.80 | 284.05 | **118.8%** | 19 | USD |
| 11 | Micron Technology, Inc. | `MU` | 725.11 | 1561.91 | **115.4%** | 45 | USD |
| 12 | Western Digital Corporation | `WDC` | 289.20 | 613.38 | **112.1%** | 24 | USD |
| 13 | Nebius Group N.V. | `NBIS` | 134.00 | 278.05 | **107.5%** | 20 | USD |
| 14 | SOFTBANK GROUP CORP | `SOFTBANK` | 3831.00 | 7757.69 | **102.5%** | 18 | JPY |
| 15 | Marvell Technology, Inc. | `MRVL` | 154.39 | 310.94 | **101.4%** | 40 | USD |

## Analyst consensus (12-month price target) — most downside

| Rank | Company | OKX | Price | Analyst mean target | Gap | Analysts | Currency |
|---:|---|---|---:|---:|---:|---:|---|
| 1 | Moderna, Inc. | `MRNA` | 250.83 | 154.47 | **-38.4%** | 19 | USD |
| 2 | Apple Inc. | `AAPL` | 348.51 | 340.77 | **-2.2%** | 40 | USD |

Price/target uses the underlying Yahoo Finance share quote, not the OKX derivative. Minimum 3 analysts; unreliable price scales and missing coverage excluded. Targets are analyst opinions, not guaranteed forecasts.

## All OKX companies — our ratio + LONG/SHORT scores

| Company | OKX | P/S | EV/S | Op margin | Fwd P/E | EPS +1y | Rev +1y | FCF yield | LONG | SHORT |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| QUALCOMM Incorporated | `QCOM` | 4.3 | 4.5 | 15.4% | 14.2 | 27.3% | 15.6% | 4.9% | **100 CORE** | **0** |
| Rocket Lab Corporation | `RKLB` | 45.5 | 39.9 | -29.6% | 2291.2 | 71.7% | 38.3% | -0.6% | **0** | **100 CORE** |
| USA Rare Earth, Inc. | `USAR` | 183.8 | 59.1 | -4711.6% | 264.0 | 105.3% | 933.3% | -10.5% | **0** | **100 CORE** |
| Sandisk Corporation | `SNDK` | 4.2 | 4.1 | 79.6% | 3.0 | 27.1% | 23.7% | 9.2% | **90 CORE** | **10** |
| Taiwan Semiconductor Manufactur | `TSM` | 0.4 | 2.7 | 58.7% | 17.0 | 33.6% | 37.8% | 58.5% | **90 CORE** | **10** |
| Western Digital Corporation | `WDC` | 7.5 | 7.4 | 47.7% | 7.2 | 63.4% | 40.5% | 2.5% | **83 CORE** | **10** |
| Applovin Corporation | `APP` | 17.2 | 17.3 | 78.2% | 19.0 | 26.1% | 24.8% | 2.8% | **83 CORE** | **10** |
| IonQ, Inc. | `IONQ` | 42.7 | 37.5 | -226.5% | -24.9 | -39.3% | 70.7% | -0.7% | **0** | **82 WATCH** |
| Moderna, Inc. | `MRNA` | 40.2 | 39.8 | 10.4% | -58.7 | 41.5% | 11.6% | -0.6% | **0** | **82 WATCH** |
| Okta, Inc. | `OKTA` | 10.1 | 9.4 | 13.3% | 40.7 | 11.4% | 10.1% | 3.3% | **8** | **80 CORE** |
| AST SpaceMobile, Inc. | `ASTS` | 91.8 | 83.2 | -398.5% | -21.6 | 28.8% | 249.8% | -15.5% | **0** | **80 WATCH** |
| Tesla, Inc. | `TSLA` | 14.5 | 14.2 | 5.4% | 175.9 | 25.2% | 13.5% | 0.3% | **20** | **78** |
| Marvell Technology, Inc. | `MRVL` | 14.7 | 14.5 | 16.7% | 21.0 | 74.2% | 63.9% | 1.7% | **77 WATCH** | **13** |
| Robinhood Markets, Inc. | `HOOD` | 14.4 | 14.0 | 48.1% | 23.8 | 39.7% | 29.2% | — | **77 WATCH** | **0** |
| Advanced Micro Devices, Inc. | `AMD` | 18.6 | 18.5 | 21.2% | 29.1 | 118.8% | 83.5% | 0.9% | **77 WATCH** | **13** |
| Corning Incorporated | `GLW` | 5.5 | 5.9 | 18.9% | 24.8 | 34.1% | 21.0% | 0.9% | **77 WATCH** | **13** |
| Applied Materials, Inc. | `AMAT` | 9.6 | 9.5 | 33.7% | 20.1 | 45.0% | 35.4% | 1.0% | **77 WATCH** | **3** |
| Nebius Group N.V. | `NBIS` | 26.9 | 28.7 | -0.2% | -38.5 | -191.4% | 267.0% | -26.4% | **0** | **76 WATCH** |
| AXT Inc | `AXT` | 15.1 | 12.8 | 38.7% | 15.4 | 116.3% | 115.9% | — | **75 WATCH** | **20** |
| NVIDIA Corporation | `NVDA` | 13.5 | 13.4 | 66.2% | 10.6 | 71.0% | 68.0% | 1.0% | **75 WATCH** | **18** |
| Credo Technology Group Holding  | `CRDO` | 15.3 | 14.9 | 25.2% | 13.4 | 53.9% | 55.0% | 1.0% | **75 WATCH** | **28** |
| Micron Technology, Inc. | `MU` | 6.2 | 5.9 | 80.7% | 3.5 | 17.7% | 16.0% | 3.6% | **75 CORE** | **30** |
| Broadcom Inc. | `AVGO` | 17.8 | 18.2 | 54.3% | 17.1 | 66.9% | 65.6% | 1.9% | **75 WATCH** | **28** |
| Dell Technologies Inc. | `DELL` | 1.4 | 1.6 | 12.0% | 11.0 | 16.8% | 19.5% | 2.8% | **75 CORE** | **30** |
| Cerebras Systems Inc. | `CBRS` | 32.7 | 23.2 | -265.0% | 73.2 | 370.9% | 233.1% | — | **0** | **71 WATCH** |
| Oracle Corporation | `ORCL` | 5.1 | 6.9 | 35.6% | 10.7 | 35.7% | 45.7% | -12.5% | **70 WATCH** | **10** |
| Adobe Inc. | `ADBE` | 3.5 | 3.6 | 34.8% | 8.6 | 12.0% | 9.1% | 10.1% | **65 WATCH** | **30** |
| Circle Internet Group, Inc. | `CRCL` | 5.5 | 4.9 | 24.1% | 45.6 | 0.5% | 24.1% | 1.6% | **15** | **63 CORE** |
| XIAOMI-W | `XIAOMI` | 1.8 | 1.6 | 4.0% | 20.5 | 39.7% | 19.4% | -1.1% | **62 WATCH** | **10** |
| Coherent Corp. | `COHR` | 5.3 | 5.7 | 16.3% | 13.6 | 51.7% | 39.4% | -4.0% | **60 WATCH** | **35** |
| Microsoft Corporation | `MSFT` | 11.4 | 11.6 | 49.8% | 22.0 | 20.9% | 20.5% | 0.1% | **59 WATCH** | **3** |
| IREN LIMITED | `IREN` | 12.0 | 21.7 | -82.5% | 73.1 | 116.3% | 206.6% | — | **0** | **59** |
| Coca-Cola Company (The) | `KO` | 8.2 | 8.7 | 33.4% | 27.5 | 5.7% | -3.1% | 1.0% | **0** | **58** |
| Meta Platforms, Inc. | `META` | 6.8 | 6.9 | 35.4% | 18.0 | 16.7% | 21.7% | 1.0% | **57 WATCH** | **38** |
| Netflix, Inc. | `NFLX` | 5.2 | 5.4 | 34.6% | 16.8 | 5.1% | 10.7% | 9.8% | **35** | **50** |
| Palantir Technologies Inc. | `PLTR` | 55.8 | 54.4 | 46.9% | 66.5 | 49.2% | 53.5% | 0.7% | **45** | **48** |
| Bloom Energy Corporation | `BE` | 14.3 | 14.4 | 18.5% | 34.8 | 62.7% | 56.4% | -0.0% | **45** | **35** |
| SamsungElec | `SAMSUNG` | 2.3 | 1.9 | 55.0% | 2.7 | 62.3% | 40.9% | 6.2% | **45** | **10** |
| Super Micro Computer, Inc. | `SMCI` | 0.3 | 0.5 | 9.6% | 4.0 | 6.5% | 11.3% | -44.7% | **35** | **45** |
| Arm Holdings plc | `ARM` | 35.5 | 35.0 | 13.9% | 59.0 | 35.5% | 37.2% | 0.6% | **43** | **33** |
| Coinbase Global, Inc. | `COIN` | 6.4 | 6.1 | -1.4% | 54.7 | 782.5% | 27.1% | 10.5% | **20** | **40** |
| SOFTBANK GROUP CORP | `SOFTBANK` | 2.7 | 6.1 | -11.6% | 13.0 | 30.4% | 6.1% | -10.0% | **0** | **40** |
| CoreWeave, Inc. | `CRWV` | 3.5 | 9.6 | -1.9% | -24.0 | 9.3% | 105.4% | -33.8% | **0** | **40** |
| Apple Inc. | `AAPL` | 10.6 | 10.7 | 31.1% | 33.0 | 19.0% | 8.0% | 2.1% | **20** | **38** |
| SK hynix | `SKHYNIX` | 3.3 | 2.9 | 79.7% | 2.4 | 49.0% | 60.4% | — | **30** | **5** |
| Lumentum Holdings Inc. | `LITE` | 14.2 | 14.0 | 28.0% | 14.6 | 60.9% | 57.9% | 0.3% | **30** | **23** |
| SK hynix | `SKHY` | 3.3 | 2.9 | 79.7% | 2.4 | 49.0% | 60.4% | — | **30** | **5** |
| Alphabet Inc. | `GOOGL` | 7.5 | 7.3 | 31.8% | 18.6 | -23.5% | 27.6% | -0.0% | **5** | **30** |
| Amazon.com, Inc. | `AMZN` | 3.7 | 3.9 | 13.9% | 24.8 | -16.6% | 15.8% | -1.2% | **0** | **30** |
| Intel Corporation | `INTC` | 5.2 | 5.4 | 15.6% | 32.5 | 20.4% | 12.0% | 0.3% | **5** | **28** |
| Fluence Energy, Inc. | `FLNC` | 0.4 | 0.3 | -8.9% | -9.3 | 59.3% | 25.4% | 0.3% | **5** | **28** |
| BitMine Immersion Technologies, | `BMNR` | 178.2 | 172.7 | 8.4% | 19.2 | 103.2% | 421.8% | -4.8% | **25** | **25** |
| Strategy Inc | `MSTR` | 103.5 | 131.4 | -2.1% | 7.0 | 380.1% | 3.2% | -6.3% | **25** | **25** |
| Applied Optoelectronics, Inc. | `AAOI` | 5.9 | 5.5 | -0.5% | 12.6 | 454.1% | 135.1% | -29.9% | **10** | **25** |
| Hyperliquid Strategies Inc | `PURR` | 112.2 | 99.9 | 6593.3% | 42.7 | -79.8% | 22.8% | — | **0** | **25 WATCH** |

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
