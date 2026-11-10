# OKX Long / Short Fundamental Scanner

Hourly scanner restricted to public companies exposed by the **OKX EEA TradFi / Stock Perpetual API universe**.

**Last scan:** 2026-11-10 10:00 UTC  
**Availability scope:** user-confirmed OKX EEA Stock Futures / X-Perp  
**OKX stock/ETF markets in configured universe:** 72  
**Public companies analysed:** 55  
**SHORT CORE:** 5  
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
| 1 | Sandisk Corporation | SNDK | -0.0% | -21.3% | -10.7% | 90 | +9 | **99** | **CORE** | yes |
| 2 | Taiwan Semiconductor Manufactur | TSM | 0.0% | -4.0% | -2.0% | 88 | +2 | **90** | **CORE** | yes |
| 3 | Applied Materials, Inc. | AMAT | 0.0% | -3.0% | -1.5% | 88 | +1 | **89** | **CORE** | yes |
| 4 | Western Digital Corporation | WDC | 0.0% | -16.6% | -8.3% | 82 | +7 | **89** | **CORE** | yes |
| 5 | AXT Inc | AXT | 0.0% | -16.4% | -8.2% | 82 | +7 | **89** | **CORE** | yes |
| 6 | Marvell Technology, Inc. | MRVL | -0.0% | -10.1% | -5.1% | 84 | +4 | **88** | **CORE** | yes |
| 7 | NVIDIA Corporation | NVDA | 0.0% | -13.6% | -6.8% | 82 | +5 | **87** | **CORE** | yes |
| 8 | Credo Technology Group Holding  | CRDO | 0.0% | -11.9% | -6.0% | 82 | +5 | **87** | **CORE** | yes |
| 9 | Broadcom Inc. | AVGO | -0.0% | -3.8% | -1.9% | 82 | +2 | **84** | **CORE** | yes |
| 10 | QUALCOMM Incorporated | QCOM | -0.0% | 4.3% | 2.1% | 85 | -2 | **83** | **CORE** | yes |

## Final model + Price Timing — SHORT

| Rank | Company | OKX | 24h | 7d | 50/50 move | Base SHORT | Timing adj. | Final | Signal | Prev. SHORT? |
|---:|---|---|---:|---:|---:|---:|---:|---:|---|---|
| 1 | Rocket Lab Corporation | RKLB | -0.0% | 8.1% | 4.1% | 100 | +3 | **100** | **CORE** | yes |
| 2 | USA Rare Earth, Inc. | USAR | -0.0% | 0.6% | 0.3% | 100 | +0 | **100** | **CORE** | yes |
| 3 | Moderna, Inc. | MRNA | 0.0% | 17.8% | 8.9% | 85 | +7 | **92** | **CORE** | yes |
| 4 | IonQ, Inc. | IONQ | -0.0% | 17.8% | 8.9% | 82 | +7 | **89** | **CORE** | yes |
| 5 | AST SpaceMobile, Inc. | ASTS | 0.0% | -0.7% | -0.3% | 80 | +0 | **80** | **CORE** | yes |
| 6 | Nebius Group N.V. | NBIS | 0.0% | -6.7% | -3.4% | 80 | -3 | **77** | **CORE** | yes |
| 7 | Cerebras Systems Inc. | CBRS | 0.0% | -1.1% | -0.6% | 71 | +0 | **71** | **WATCH** | yes |
| 8 | IREN LIMITED | IREN | 0.0% | -12.5% | -6.2% | 74 | -5 | **69** | **WATCH** | yes |
| 9 | Okta, Inc. | OKTA | -0.0% | -6.4% | -3.2% | 60 | -3 | **57** | **WATCH** | yes |
| 10 | Tesla, Inc. | TSLA | 0.0% | -5.1% | -2.6% | 59 | -2 | **57** | **WATCH** | yes |

## Combined model — LONG

Weighted score: **70% fundamental + 30% P/E trend**.

| Rank | Company | OKX | Fundamental LONG | P/E trend LONG | Combined | Signal |
|---:|---|---|---:|---:|---:|---|
| 1 | Sandisk Corporation | `SNDK` | 90 | 90 | **90** | **CORE** |
| 2 | Taiwan Semiconductor Manufactur | `TSM` | 90 | 85 | **88** | **CORE** |
| 3 | Applied Materials, Inc. | `AMAT` | 85 | 95 | **88** | **CORE** |
| 4 | QUALCOMM Incorporated | `QCOM` | 100 | 50 | **85** | **CORE** |
| 5 | Marvell Technology, Inc. | `MRVL` | 77 | 100 | **84** | **CORE** |
| 6 | Advanced Micro Devices, Inc. | `AMD` | 77 | 100 | **84** | **CORE** |
| 7 | Western Digital Corporation | `WDC` | 83 | 80 | **82** | **CORE** |
| 8 | AXT Inc | `AXT` | 75 | 100 | **82** | **CORE** |
| 9 | NVIDIA Corporation | `NVDA` | 75 | 100 | **82** | **CORE** |
| 10 | Credo Technology Group Holding  | `CRDO` | 75 | 100 | **82** | **CORE** |

## Combined model — SHORT

Weighted score: **70% fundamental + 30% P/E trend**.

| Rank | Company | OKX | Fundamental SHORT | P/E trend SHORT | Combined | Signal |
|---:|---|---|---:|---:|---:|---|
| 1 | Rocket Lab Corporation | `RKLB` | 100 | 0 | **100** | **CORE** |
| 2 | USA Rare Earth, Inc. | `USAR` | 100 | 0 | **100** | **CORE** |
| 3 | Moderna, Inc. | `MRNA` | 85 | 0 | **85** | **CORE** |
| 4 | IonQ, Inc. | `IONQ` | 82 | 0 | **82** | **WATCH** |
| 5 | AST SpaceMobile, Inc. | `ASTS` | 80 | 0 | **80** | **WATCH** |
| 6 | Nebius Group N.V. | `NBIS` | 80 | 0 | **80** | **WATCH** |
| 7 | IREN LIMITED | `IREN` | 74 | 0 | **74** | **WATCH** |
| 8 | Cerebras Systems Inc. | `CBRS` | 71 | 0 | **71** | **WATCH** |
| 9 | Okta, Inc. | `OKTA` | 80 | 13 | **60** | **WATCH** |
| 10 | Tesla, Inc. | `TSLA` | 78 | 15 | **59** | **WATCH** |

## P/E Compression + Growth — LONG

| Rank | Company | OKX | Trail P/E | Fwd P/E | P/E change | EPS +1y | Rev +1y | Rev trend | LONG score | Signal |
|---:|---|---|---:|---:|---:|---:|---:|---|---:|---|
| 1 | AXT Inc | `AXT` | 87.6 | 16.8 | -80.8% | 116.3% | 115.9% | decelerating | **100** | **CORE** |
| 2 | Marvell Technology, Inc. | `MRVL` | 50.9 | 21.0 | -58.6% | 74.2% | 63.9% | accelerating | **100** | **CORE** |
| 3 | NVIDIA Corporation | `NVDA` | 22.6 | 11.2 | -50.3% | 71.0% | 68.0% | decelerating | **100** | **CORE** |
| 4 | Credo Technology Group Holding  | `CRDO` | 47.1 | 13.7 | -71.0% | 53.9% | 55.0% | decelerating | **100** | **CORE** |
| 5 | Broadcom Inc. | `AVGO` | 40.8 | 16.4 | -59.8% | 66.9% | 65.6% | decelerating | **100** | **CORE** |
| 6 | Advanced Micro Devices, Inc. | `AMD` | 108.7 | 28.8 | -73.5% | 118.8% | 83.5% | accelerating | **100** | **CORE** |
| 7 | Coherent Corp. | `COHR` | 46.6 | 14.3 | -69.4% | 51.7% | 40.0% | decelerating | **100** | **CORE** |
| 8 | Applied Materials, Inc. | `AMAT` | 32.0 | 20.0 | -37.5% | 45.0% | 35.4% | accelerating | **95** | **CORE** |
| 9 | Oracle Corporation | `ORCL` | 18.8 | 10.8 | -42.3% | 35.7% | 45.7% | accelerating | **95** | **CORE** |
| 10 | Arm Holdings plc | `ARM` | 214.1 | 60.5 | -71.7% | 35.6% | 37.2% | accelerating | **95** | **CORE** |

## P/E Expansion + Weakening — SHORT

| Rank | Company | OKX | Trail P/E | Fwd P/E | P/E change | EPS +1y | Rev +1y | Rev trend | SHORT score | Signal |
|---:|---|---|---:|---:|---:|---:|---:|---|---:|---|
| 1 | SOFTBANK GROUP CORP | `SOFTBANK` | 4.5 | 13.1 | 191.0% | -14.5% | 7.0% | decelerating | **86** | **CORE** |
| 2 | Hyperliquid Strategies Inc | `PURR` | 3.8 | 26.2 | 594.1% | -66.6% | 22.8% | decelerating | **80** | **CORE** |
| 3 | Alphabet Inc. | `GOOGL` | 15.0 | 18.7 | 24.1% | -23.4% | 27.6% | accelerating | **50** | **WATCH** |

## Top SHORT candidates

| Rank | Company | OKX market | SHORT score | Signal | P/S | EV/S | Op margin | Fwd P/E | Rev +1y | FCF yield |
|---:|---|---|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Rocket Lab Corporation | `RKLB-USDT-SWAP` | **100** | **CORE** | 42.7 | 37.1 | -29.6% | 1023.8 | 39.6% | -0.6% |
| 2 | USA Rare Earth, Inc. | `USAR-USDT-SWAP` | **100** | **CORE** | 203.3 | 70.4 | -4711.6% | 292.0 | 870.1% | -9.5% |
| 3 | Moderna, Inc. | `MRNA-USDT-SWAP` | **85** | **CORE** | 43.1 | 42.7 | 10.4% | -62.9 | 11.6% | -0.5% |
| 4 | IonQ, Inc. | `IONQ-USDT-SWAP` | **82** | **WATCH** | 43.2 | 37.9 | -226.5% | -25.2 | 70.7% | -0.7% |
| 5 | Nebius Group N.V. | `NBIS-USDT-SWAP` | **80** | **WATCH** | 26.5 | 30.2 | -0.2% | -40.7 | 267.0% | -26.8% |
| 6 | Okta, Inc. | `OKTA-USDT-SWAP` | **80** | **CORE** | 10.1 | 9.4 | 13.3% | 40.6 | 10.1% | 3.3% |
| 7 | AST SpaceMobile, Inc. | `ASTS-USDT-SWAP` | **80** | **WATCH** | 100.5 | 89.9 | -398.5% | -25.4 | 264.2% | -14.1% |
| 8 | IREN LIMITED | `IREN-USDT-SWAP` | **74** | **WATCH** | 13.1 | 22.7 | -82.5% | 79.3 | 206.6% | -96.6% |
| 9 | Circle Internet Group, Inc. | `CRCL-USDT-SWAP` | **73** | **CORE** | 5.7 | 5.2 | 24.1% | 42.9 | 24.1% | 1.5% |
| 10 | Cerebras Systems Inc. | `CBRS-USDT-SWAP` | **71** | **WATCH** | 33.7 | 24.3 | -265.0% | 75.6 | 233.1% | — |

## Top LONG candidates

| Rank | Company | OKX market | LONG score | Signal | P/S | EV/S | Op margin | Fwd P/E | Rev +1y | FCF yield |
|---:|---|---|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | QUALCOMM Incorporated | `QCOM-USDT-SWAP` | **100** | **CORE** | 4.3 | 4.4 | 15.4% | 14.0 | 15.6% | 5.0% |
| 2 | Taiwan Semiconductor Manufactur | `TSM-USDT-SWAP` | **90** | **CORE** | 0.4 | 2.6 | 58.7% | 16.6 | 37.8% | 59.7% |
| 3 | Sandisk Corporation | `SNDK-USDT-SWAP` | **90** | **CORE** | 4.4 | 4.2 | 79.6% | 3.1 | 23.7% | 8.9% |
| 4 | Applied Materials, Inc. | `AMAT-USDT-SWAP` | **85** | **WATCH** | 9.5 | 9.5 | 33.7% | 20.0 | 35.4% | 1.0% |
| 5 | Applovin Corporation | `APP-USDT-SWAP` | **83** | **CORE** | 17.9 | 17.9 | 78.2% | 19.7 | 25.1% | 2.7% |
| 6 | Western Digital Corporation | `WDC-USDT-SWAP` | **83** | **CORE** | 7.5 | 7.5 | 47.7% | 7.2 | 40.5% | 2.5% |
| 7 | Corning Incorporated | `GLW-USDT-SWAP` | **77** | **WATCH** | 5.6 | 6.0 | 18.9% | 25.6 | 21.0% | 0.9% |
| 8 | Robinhood Markets, Inc. | `HOOD-USDT-SWAP` | **77** | **WATCH** | 14.8 | 14.3 | 48.1% | 24.4 | 29.2% | — |
| 9 | Marvell Technology, Inc. | `MRVL-USDT-SWAP` | **77** | **WATCH** | 14.7 | 14.5 | 16.7% | 21.0 | 63.9% | 1.7% |
| 10 | Advanced Micro Devices, Inc. | `AMD-USDT-SWAP` | **77** | **WATCH** | 18.4 | 18.2 | 21.2% | 28.8 | 83.5% | 0.9% |

## Analyst consensus (12-month price target) — most upside

| Rank | Company | OKX | Price | Analyst mean target | Gap | Analysts | Currency |
|---:|---|---|---:|---:|---:|---:|---|
| 1 | CoreWeave, Inc. | `CRWV` | 48.98 | 131.53 | **168.5%** | 38 | USD |
| 2 | IREN LIMITED | `IREN` | 21.41 | 56.69 | **164.8%** | 19 | USD |
| 3 | Cerebras Systems Inc. | `CBRS` | 96.70 | 254.27 | **163.0%** | 11 | USD |
| 4 | SK hynix | `SKHYNIX` | 1212000.00 | 3100998.50 | **155.9%** | 39 | KRW |
| 5 | Hyperliquid Strategies Inc | `PURR` | 8.91 | 22.50 | **152.5%** | 4 | USD |
| 6 | SamsungElec | `SAMSUNG` | 198900.00 | 475628.56 | **139.1%** | 35 | KRW |
| 7 | Sandisk Corporation | `SNDK` | 886.51 | 2047.38 | **130.9%** | 24 | USD |
| 8 | Credo Technology Group Holding  | `CRDO` | 132.89 | 284.05 | **113.7%** | 19 | USD |
| 9 | AXT Inc | `AXT` | 42.91 | 91.50 | **113.2%** | 6 | USD |
| 10 | Micron Technology, Inc. | `MU` | 733.15 | 1561.91 | **113.0%** | 45 | USD |
| 11 | Western Digital Corporation | `WDC` | 289.78 | 613.38 | **111.7%** | 24 | USD |
| 12 | Applied Optoelectronics, Inc. | `AAOI` | 52.10 | 109.00 | **109.2%** | 5 | USD |
| 13 | SOFTBANK GROUP CORP | `SOFTBANK` | 3872.00 | 7845.25 | **102.6%** | 18 | JPY |
| 14 | AST SpaceMobile, Inc. | `ASTS` | 36.89 | 74.68 | **102.4%** | 12 | USD |
| 15 | Marvell Technology, Inc. | `MRVL` | 154.60 | 310.94 | **101.1%** | 40 | USD |

## Analyst consensus (12-month price target) — most downside

| Rank | Company | OKX | Price | Analyst mean target | Gap | Analysts | Currency |
|---:|---|---|---:|---:|---:|---:|---|
| 1 | Moderna, Inc. | `MRNA` | 269.00 | 154.47 | **-42.6%** | 19 | USD |
| 2 | Apple Inc. | `AAPL` | 350.69 | 340.77 | **-2.8%** | 40 | USD |

Price/target uses the underlying Yahoo Finance share quote, not the OKX derivative. Minimum 3 analysts; unreliable price scales and missing coverage excluded. Targets are analyst opinions, not guaranteed forecasts.

## All OKX companies — our ratio + LONG/SHORT scores

| Company | OKX | P/S | EV/S | Op margin | Fwd P/E | EPS +1y | Rev +1y | FCF yield | LONG | SHORT |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| QUALCOMM Incorporated | `QCOM` | 4.3 | 4.4 | 15.4% | 14.0 | 27.3% | 15.6% | 5.0% | **100 CORE** | **0** |
| Rocket Lab Corporation | `RKLB` | 42.7 | 37.1 | -29.6% | 1023.8 | 65.7% | 39.6% | -0.6% | **0** | **100 CORE** |
| USA Rare Earth, Inc. | `USAR` | 203.3 | 70.4 | -4711.6% | 292.0 | 105.3% | 870.1% | -9.5% | **0** | **100 CORE** |
| Sandisk Corporation | `SNDK` | 4.4 | 4.2 | 79.6% | 3.1 | 27.1% | 23.7% | 8.9% | **90 CORE** | **10** |
| Taiwan Semiconductor Manufactur | `TSM` | 0.4 | 2.6 | 58.7% | 16.6 | 33.6% | 37.8% | 59.7% | **90 CORE** | **10** |
| Applied Materials, Inc. | `AMAT` | 9.5 | 9.5 | 33.7% | 20.0 | 45.0% | 35.4% | 1.0% | **85 WATCH** | **3** |
| Moderna, Inc. | `MRNA` | 43.1 | 42.7 | 10.4% | -62.9 | 41.5% | 11.6% | -0.5% | **0** | **85 CORE** |
| Western Digital Corporation | `WDC` | 7.5 | 7.5 | 47.7% | 7.2 | 63.4% | 40.5% | 2.5% | **83 CORE** | **10** |
| Applovin Corporation | `APP` | 17.9 | 17.9 | 78.2% | 19.7 | 26.1% | 25.1% | 2.7% | **83 CORE** | **10** |
| IonQ, Inc. | `IONQ` | 43.2 | 37.9 | -226.5% | -25.2 | -39.3% | 70.7% | -0.7% | **0** | **82 WATCH** |
| Okta, Inc. | `OKTA` | 10.1 | 9.4 | 13.3% | 40.6 | 11.4% | 10.1% | 3.3% | **8** | **80 CORE** |
| AST SpaceMobile, Inc. | `ASTS` | 100.5 | 89.9 | -398.5% | -25.4 | 44.3% | 264.2% | -14.1% | **0** | **80 WATCH** |
| Nebius Group N.V. | `NBIS` | 26.5 | 30.2 | -0.2% | -40.7 | -191.4% | 267.0% | -26.8% | **0** | **80 WATCH** |
| Tesla, Inc. | `TSLA` | 14.4 | 14.2 | 5.4% | 175.1 | 25.2% | 13.5% | 0.3% | **20** | **78** |
| Marvell Technology, Inc. | `MRVL` | 14.7 | 14.5 | 16.7% | 21.0 | 74.2% | 63.9% | 1.7% | **77 WATCH** | **13** |
| Corning Incorporated | `GLW` | 5.6 | 6.0 | 18.9% | 25.6 | 34.1% | 21.0% | 0.9% | **77 WATCH** | **13** |
| Advanced Micro Devices, Inc. | `AMD` | 18.4 | 18.2 | 21.2% | 28.8 | 118.8% | 83.5% | 0.9% | **77 WATCH** | **13** |
| Robinhood Markets, Inc. | `HOOD` | 14.8 | 14.3 | 48.1% | 24.4 | 39.7% | 29.2% | — | **77 WATCH** | **0** |
| AXT Inc | `AXT` | 16.5 | 14.1 | 38.7% | 16.8 | 116.3% | 115.9% | — | **75 WATCH** | **20** |
| NVIDIA Corporation | `NVDA` | 14.2 | 14.1 | 66.2% | 11.2 | 71.0% | 68.0% | 1.0% | **75 WATCH** | **18** |
| Credo Technology Group Holding  | `CRDO` | 15.7 | 15.2 | 25.2% | 13.7 | 53.9% | 55.0% | 1.0% | **75 WATCH** | **28** |
| Broadcom Inc. | `AVGO` | 17.1 | 17.5 | 54.3% | 16.4 | 66.9% | 65.6% | 2.0% | **75 WATCH** | **28** |
| Micron Technology, Inc. | `MU` | 6.2 | 5.9 | 80.7% | 3.5 | 17.7% | 16.0% | 3.5% | **75 CORE** | **30** |
| Dell Technologies Inc. | `DELL` | 1.5 | 1.6 | 12.0% | 11.4 | 16.8% | 19.5% | 2.7% | **75 CORE** | **30** |
| IREN LIMITED | `IREN` | 13.1 | 22.7 | -82.5% | 79.3 | 116.3% | 206.6% | -96.6% | **0** | **74 WATCH** |
| Circle Internet Group, Inc. | `CRCL` | 5.7 | 5.2 | 24.1% | 42.9 | 3.2% | 24.1% | 1.5% | **15** | **73 CORE** |
| Cerebras Systems Inc. | `CBRS` | 33.7 | 24.3 | -265.0% | 75.6 | 372.9% | 233.1% | — | **0** | **71 WATCH** |
| Oracle Corporation | `ORCL` | 5.2 | 7.0 | 35.6% | 10.8 | 35.7% | 45.7% | -12.3% | **70 WATCH** | **10** |
| Adobe Inc. | `ADBE` | 3.6 | 3.6 | 34.8% | 8.7 | 12.0% | 9.1% | 10.1% | **65 WATCH** | **30** |
| XIAOMI-W | `XIAOMI` | 1.8 | 1.6 | 4.0% | 20.5 | 39.7% | 19.4% | -1.1% | **62 WATCH** | **10** |
| Coherent Corp. | `COHR` | 5.6 | 6.0 | 16.3% | 14.3 | 51.7% | 40.0% | -3.8% | **60 WATCH** | **35** |
| Microsoft Corporation | `MSFT` | 11.7 | 11.9 | 49.8% | 22.5 | 20.9% | 20.5% | 0.1% | **59 WATCH** | **3** |
| Coca-Cola Company (The) | `KO` | 8.1 | 8.6 | 33.4% | 27.2 | 5.6% | -3.1% | 1.1% | **0** | **58** |
| Meta Platforms, Inc. | `META` | 6.8 | 6.9 | 35.4% | 18.0 | 16.7% | 21.7% | 1.0% | **57 WATCH** | **38** |
| Netflix, Inc. | `NFLX` | 5.3 | 5.5 | 34.6% | 17.0 | 5.1% | 10.7% | 9.7% | **35** | **50** |
| Palantir Technologies Inc. | `PLTR` | 55.9 | 54.5 | 46.9% | 66.7 | 49.2% | 53.5% | 0.7% | **45** | **48** |
| Bloom Energy Corporation | `BE` | 15.0 | 15.1 | 18.5% | 36.4 | 62.7% | 56.4% | -0.0% | **45** | **35** |
| SamsungElec | `SAMSUNG` | 2.2 | 1.8 | 55.0% | 2.6 | 62.3% | 40.9% | 6.5% | **45** | **10** |
| Super Micro Computer, Inc. | `SMCI` | 0.3 | 0.5 | 9.6% | 4.1 | 6.5% | 11.3% | -43.4% | **35** | **45** |
| Arm Holdings plc | `ARM` | 36.5 | 35.9 | 13.9% | 60.5 | 35.6% | 37.2% | 0.6% | **43** | **33** |
| Coinbase Global, Inc. | `COIN` | 6.6 | 6.3 | -1.4% | 56.4 | 782.5% | 27.1% | 10.2% | **20** | **40** |
| SOFTBANK GROUP CORP | `SOFTBANK` | 2.8 | 5.8 | -11.6% | 13.1 | -14.5% | 7.0% | -9.9% | **0** | **40** |
| CoreWeave, Inc. | `CRWV` | 3.6 | 9.6 | -1.9% | -24.1 | 9.3% | 105.4% | -33.6% | **0** | **40** |
| Apple Inc. | `AAPL` | 10.6 | 10.7 | 31.1% | 33.2 | 19.0% | 8.0% | 2.1% | **20** | **38** |
| SK hynix | `SKHYNIX` | 3.2 | 2.7 | 79.7% | 2.3 | 48.2% | 60.4% | — | **30** | **5** |
| Lumentum Holdings Inc. | `LITE` | 14.4 | 14.3 | 28.0% | 14.9 | 60.9% | 57.9% | 0.3% | **30** | **23** |
| SK hynix | `SKHY` | 3.2 | 2.7 | 79.7% | 2.3 | 48.2% | 60.4% | — | **30** | **5** |
| Alphabet Inc. | `GOOGL` | 7.5 | 7.3 | 31.8% | 18.7 | -23.4% | 27.6% | -0.0% | **5** | **30** |
| Amazon.com, Inc. | `AMZN` | 3.6 | 3.9 | 13.9% | 24.5 | -16.6% | 15.8% | -1.2% | **0** | **30** |
| Intel Corporation | `INTC` | 5.3 | 5.5 | 15.6% | 33.2 | 20.4% | 12.0% | 0.3% | **5** | **28** |
| Fluence Energy, Inc. | `FLNC` | 0.4 | 0.3 | -8.9% | -10.2 | 59.3% | 25.4% | 0.2% | **5** | **28** |
| Strategy Inc | `MSTR` | 107.4 | 135.3 | -2.1% | 7.3 | 380.1% | 3.2% | -6.1% | **25** | **25** |
| BitMine Immersion Technologies, | `BMNR` | 183.4 | 177.9 | 8.4% | 19.8 | 103.2% | 421.8% | -4.6% | **25** | **25** |
| Applied Optoelectronics, Inc. | `AAOI` | 6.3 | 6.0 | -0.5% | 13.7 | 454.1% | 135.1% | -27.7% | **10** | **25** |
| Hyperliquid Strategies Inc | `PURR` | 114.2 | 102.0 | 6593.3% | 26.2 | -66.6% | 22.8% | — | **2** | **25** |

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
