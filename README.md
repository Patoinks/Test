# OKX Long / Short Fundamental Scanner

Hourly scanner restricted to public companies exposed by the **OKX EEA TradFi / Stock Perpetual API universe**.

**Last scan:** 2026-11-11 22:45 UTC  
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
| 1 | Sandisk Corporation | SNDK | 13.7% | -5.8% | 4.0% | 90 | -3 | **87** | **CORE** | yes |
| 2 | NVIDIA Corporation | NVDA | 2.9% | -13.2% | -5.2% | 82 | +4 | **86** | **CORE** | yes |
| 3 | Taiwan Semiconductor Manufactur | TSM | 4.3% | 4.4% | 4.4% | 88 | -3 | **85** | **CORE** | yes |
| 4 | QUALCOMM Incorporated | QCOM | 1.8% | 2.0% | 1.9% | 85 | -1 | **84** | **CORE** | yes |
| 5 | Robinhood Markets, Inc. | HOOD | 4.0% | -3.2% | 0.4% | 80 | +0 | **80** | **CORE** | yes |
| 6 | Marvell Technology, Inc. | MRVL | 9.3% | 5.6% | 7.5% | 84 | -6 | **78** | **CORE** | yes |
| 7 | Broadcom Inc. | AVGO | 4.0% | 6.1% | 5.0% | 82 | -4 | **78** | **CORE** | yes |
| 8 | Credo Technology Group Holding  | CRDO | 8.9% | 3.6% | 6.3% | 82 | -5 | **77** | **CORE** | yes |
| 9 | Applied Materials, Inc. | AMAT | 6.1% | 7.0% | 6.5% | 81 | -5 | **76** | **CORE** | yes |
| 10 | Corning Incorporated | GLW | 7.4% | 1.4% | 4.4% | 80 | -4 | **76** | **CORE** | yes |

## Final model + Price Timing — SHORT

| Rank | Company | OKX | 24h | 7d | 50/50 move | Base SHORT | Timing adj. | Final | Signal | Prev. SHORT? |
|---:|---|---|---:|---:|---:|---:|---:|---:|---|---|
| 1 | Rocket Lab Corporation | RKLB | 5.5% | 26.3% | 15.9% | 100 | +13 | **100** | **CORE** | yes |
| 2 | USA Rare Earth, Inc. | USAR | 4.4% | 0.8% | 2.6% | 100 | +2 | **100** | **CORE** | yes |
| 3 | Moderna, Inc. | MRNA | -0.9% | -3.8% | -2.3% | 94 | -2 | **92** | **CORE** | yes |
| 4 | Nebius Group N.V. | NBIS | 15.4% | 9.3% | 12.4% | 80 | +10 | **90** | **CORE** | yes |
| 5 | IonQ, Inc. | IONQ | -2.7% | 15.3% | 6.3% | 82 | +5 | **87** | **CORE** | yes |
| 6 | AST SpaceMobile, Inc. | ASTS | 8.7% | 2.8% | 5.8% | 80 | +5 | **85** | **CORE** | yes |
| 7 | Cerebras Systems Inc. | CBRS | 7.9% | 10.0% | 9.0% | 71 | +7 | **78** | **CORE** | yes |
| 8 | IREN LIMITED | IREN | 5.6% | -4.0% | 0.8% | 74 | +1 | **75** | **CORE** | yes |
| 9 | Tesla, Inc. | TSLA | 2.9% | 1.5% | 2.2% | 59 | +2 | **61** | **WATCH** | yes |
| 10 | Okta, Inc. | OKTA | 2.2% | -4.6% | -1.2% | 60 | -1 | **59** | **WATCH** | yes |

## Combined model — LONG

Weighted score: **70% fundamental + 30% P/E trend**.

| Rank | Company | OKX | Fundamental LONG | P/E trend LONG | Combined | Signal |
|---:|---|---|---:|---:|---:|---|
| 1 | Sandisk Corporation | `SNDK` | 90 | 90 | **90** | **CORE** |
| 2 | Taiwan Semiconductor Manufactur | `TSM` | 90 | 85 | **88** | **CORE** |
| 3 | QUALCOMM Incorporated | `QCOM` | 100 | 50 | **85** | **CORE** |
| 4 | Marvell Technology, Inc. | `MRVL` | 77 | 100 | **84** | **CORE** |
| 5 | NVIDIA Corporation | `NVDA` | 75 | 100 | **82** | **CORE** |
| 6 | Broadcom Inc. | `AVGO` | 75 | 100 | **82** | **CORE** |
| 7 | Credo Technology Group Holding  | `CRDO` | 75 | 100 | **82** | **CORE** |
| 8 | AXT Inc | `AXT` | 75 | 100 | **82** | **CORE** |
| 9 | Applied Materials, Inc. | `AMAT` | 77 | 91 | **81** | **CORE** |
| 10 | Robinhood Markets, Inc. | `HOOD` | 77 | 86 | **80** | **CORE** |

## Combined model — SHORT

Weighted score: **70% fundamental + 30% P/E trend**.

| Rank | Company | OKX | Fundamental SHORT | P/E trend SHORT | Combined | Signal |
|---:|---|---|---:|---:|---:|---|
| 1 | Rocket Lab Corporation | `RKLB` | 100 | 0 | **100** | **CORE** |
| 2 | USA Rare Earth, Inc. | `USAR` | 100 | 0 | **100** | **CORE** |
| 3 | Moderna, Inc. | `MRNA` | 94 | 0 | **94** | **WATCH** |
| 4 | IonQ, Inc. | `IONQ` | 82 | 0 | **82** | **WATCH** |
| 5 | Nebius Group N.V. | `NBIS` | 80 | 0 | **80** | **WATCH** |
| 6 | AST SpaceMobile, Inc. | `ASTS` | 80 | 0 | **80** | **WATCH** |
| 7 | IREN LIMITED | `IREN` | 74 | 0 | **74** | **WATCH** |
| 8 | Cerebras Systems Inc. | `CBRS` | 71 | 0 | **71** | **WATCH** |
| 9 | Circle Internet Group, Inc. | `CRCL` | 73 | 32 | **61** | **WATCH** |
| 10 | Okta, Inc. | `OKTA` | 80 | 13 | **60** | **WATCH** |

## P/E Compression + Growth — LONG

| Rank | Company | OKX | Trail P/E | Fwd P/E | P/E change | EPS +1y | Rev +1y | Rev trend | LONG score | Signal |
|---:|---|---|---:|---:|---:|---:|---:|---|---:|---|
| 1 | NVIDIA Corporation | `NVDA` | 22.0 | 10.9 | -50.3% | 70.8% | 67.8% | decelerating | **100** | **CORE** |
| 2 | Broadcom Inc. | `AVGO` | 44.1 | 17.7 | -59.8% | 66.9% | 65.6% | decelerating | **100** | **CORE** |
| 3 | Marvell Technology, Inc. | `MRVL` | 55.5 | 23.0 | -58.6% | 74.2% | 63.9% | accelerating | **100** | **CORE** |
| 4 | Credo Technology Group Holding  | `CRDO` | 50.1 | 14.6 | -71.0% | 53.9% | 55.0% | decelerating | **100** | **CORE** |
| 5 | AXT Inc | `AXT` | 95.9 | 18.4 | -80.8% | 116.3% | 115.9% | decelerating | **100** | **CORE** |
| 6 | Advanced Micro Devices, Inc. | `AMD` | 118.1 | 31.3 | -73.5% | 118.8% | 83.5% | accelerating | **100** | **CORE** |
| 7 | Coherent Corp. | `COHR` | 48.6 | 14.9 | -69.4% | 51.7% | 39.9% | decelerating | **100** | **CORE** |
| 8 | Oracle Corporation | `ORCL` | 20.1 | 11.6 | -42.3% | 35.7% | 45.7% | accelerating | **95** | **CORE** |
| 9 | Arm Holdings plc | `ARM` | 233.7 | 66.2 | -71.7% | 35.5% | 37.2% | accelerating | **95** | **CORE** |
| 10 | Bloom Energy Corporation | `BE` | 127.0 | 39.3 | -69.0% | 62.7% | 56.4% | decelerating | **92** | **CORE** |

## P/E Expansion + Weakening — SHORT

| Rank | Company | OKX | Trail P/E | Fwd P/E | P/E change | EPS +1y | Rev +1y | Rev trend | SHORT score | Signal |
|---:|---|---|---:|---:|---:|---:|---:|---|---:|---|
| 1 | Hyperliquid Strategies Inc | `PURR` | 3.9 | 44.6 | 1051.2% | -79.8% | 22.8% | decelerating | **80** | **CORE** |
| 2 | SOFTBANK GROUP CORP | `SOFTBANK` | 4.5 | 13.1 | 189.7% | 85.8% | 6.1% | decelerating | **61** | **WATCH** |
| 3 | Alphabet Inc. | `GOOGL` | 15.3 | 19.0 | 24.1% | -23.5% | 27.6% | accelerating | **50** | **WATCH** |

## Top SHORT candidates

| Rank | Company | OKX market | SHORT score | Signal | P/S | EV/S | Op margin | Fwd P/E | Rev +1y | FCF yield |
|---:|---|---|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Rocket Lab Corporation | `RKLB-USDT-SWAP` | **100** | **CORE** | 50.5 | 39.9 | -27.6% | 972.4 | 37.6% | -0.5% |
| 2 | USA Rare Earth, Inc. | `USAR-USDT-SWAP` | **100** | **CORE** | 191.8 | 95.7 | -1476.1% | 275.5 | 954.6% | -9.9% |
| 3 | Moderna, Inc. | `MRNA-USDT-SWAP` | **94** | **WATCH** | 39.9 | 39.8 | -80.8% | -59.3 | 10.6% | -0.6% |
| 4 | IonQ, Inc. | `IONQ-USDT-SWAP` | **82** | **WATCH** | 41.6 | 37.5 | -306.3% | -24.3 | 70.7% | -0.8% |
| 5 | Nebius Group N.V. | `NBIS-USDT-SWAP` | **80** | **WATCH** | 31.0 | 28.7 | -37.4% | -44.5 | 267.0% | -22.9% |
| 6 | Okta, Inc. | `OKTA-USDT-SWAP` | **80** | **CORE** | 10.4 | 9.4 | 7.7% | 41.6 | 10.1% | 3.3% |
| 7 | AST SpaceMobile, Inc. | `ASTS-USDT-SWAP` | **80** | **WATCH** | 100.0 | 83.2 | -393.3% | -23.5 | 249.8% | -13.2% |
| 8 | IREN LIMITED | `IREN-USDT-SWAP` | **74** | **WATCH** | 12.7 | 21.7 | -72.9% | 77.2 | 206.6% | -99.3% |
| 9 | Circle Internet Group, Inc. | `CRCL-USDT-SWAP` | **73** | **CORE** | 5.7 | 4.9 | 11.3% | 47.1 | 24.1% | 1.5% |
| 10 | Cerebras Systems Inc. | `CBRS-USDT-SWAP` | **71** | **WATCH** | 35.3 | 23.2 | -81.2% | 79.0 | 233.1% | — |

## Top LONG candidates

| Rank | Company | OKX market | LONG score | Signal | P/S | EV/S | Op margin | Fwd P/E | Rev +1y | FCF yield |
|---:|---|---|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | QUALCOMM Incorporated | `QCOM-USDT-SWAP` | **100** | **CORE** | 4.4 | 4.5 | 20.8% | 14.5 | 15.6% | 4.8% |
| 2 | Taiwan Semiconductor Manufactur | `TSM-USDT-SWAP` | **90** | **CORE** | 0.4 | 2.7 | 58.0% | 17.7 | 37.8% | 56.1% |
| 3 | Sandisk Corporation | `SNDK-USDT-SWAP` | **90** | **CORE** | 4.8 | 4.1 | 72.7% | 3.4 | 23.7% | 8.1% |
| 4 | Applovin Corporation | `APP-USDT-SWAP` | **83** | **CORE** | 17.6 | 17.3 | 77.8% | 19.4 | 24.8% | 2.8% |
| 5 | Corning Incorporated | `GLW-USDT-SWAP` | **77** | **WATCH** | 5.9 | 5.9 | 16.8% | 26.5 | 21.2% | 0.8% |
| 6 | Robinhood Markets, Inc. | `HOOD-USDT-SWAP` | **77** | **WATCH** | 15.0 | 14.0 | 45.7% | 24.8 | 29.2% | — |
| 7 | Applied Materials, Inc. | `AMAT-USDT-SWAP` | **77** | **WATCH** | 10.2 | 9.5 | 31.2% | 21.2 | 35.7% | 1.0% |
| 8 | Marvell Technology, Inc. | `MRVL-USDT-SWAP` | **77** | **WATCH** | 16.1 | 14.5 | 16.8% | 23.0 | 63.9% | 1.6% |
| 9 | Dell Technologies Inc. | `DELL-USDT-SWAP` | **75** | **CORE** | 1.6 | 1.6 | 9.9% | 12.3 | 19.5% | 2.5% |
| 10 | Credo Technology Group Holding  | `CRDO-USDT-SWAP` | **75** | **WATCH** | 16.7 | 14.9 | 31.7% | 14.6 | 55.0% | 0.9% |

## Analyst consensus (12-month price target) — most upside

| Rank | Company | OKX | Price | Analyst mean target | Gap | Analysts | Currency |
|---:|---|---|---:|---:|---:|---:|---|
| 1 | IREN LIMITED | `IREN` | 20.84 | 56.69 | **172.0%** | 19 | USD |
| 2 | Hyperliquid Strategies Inc | `PURR` | 9.15 | 22.50 | **145.9%** | 4 | USD |
| 3 | SK hynix | `SKHYNIX` | 1277000.00 | 3100998.50 | **142.8%** | 39 | KRW |
| 4 | Cerebras Systems Inc. | `CBRS` | 101.08 | 245.18 | **142.6%** | 11 | USD |
| 5 | SamsungElec | `SAMSUNG` | 206000.00 | 475628.56 | **130.9%** | 35 | KRW |
| 6 | Sandisk Corporation | `SNDK` | 977.69 | 2047.38 | **109.4%** | 24 | USD |
| 7 | CoreWeave, Inc. | `CRWV` | 60.77 | 125.46 | **106.4%** | 37 | USD |
| 8 | SOFTBANK GROUP CORP | `SOFTBANK` | 3855.00 | 7757.69 | **101.2%** | 18 | JPY |
| 9 | Credo Technology Group Holding  | `CRDO` | 141.41 | 284.05 | **100.9%** | 19 | USD |
| 10 | Western Digital Corporation | `WDC` | 313.31 | 613.38 | **95.8%** | 24 | USD |
| 11 | Applied Optoelectronics, Inc. | `AAOI` | 55.86 | 109.00 | **95.1%** | 5 | USD |
| 12 | AXT Inc | `AXT` | 46.97 | 91.50 | **94.8%** | 6 | USD |
| 13 | Micron Technology, Inc. | `MU` | 811.30 | 1561.91 | **92.5%** | 45 | USD |
| 14 | Strategy Inc | `MSTR` | 122.35 | 233.27 | **90.7%** | 15 | USD |
| 15 | Marvell Technology, Inc. | `MRVL` | 168.80 | 310.94 | **84.2%** | 40 | USD |

## Analyst consensus (12-month price target) — most downside

| Rank | Company | OKX | Price | Analyst mean target | Gap | Analysts | Currency |
|---:|---|---|---:|---:|---:|---:|---|
| 1 | Moderna, Inc. | `MRNA` | 248.69 | 158.47 | **-36.3%** | 19 | USD |
| 2 | Apple Inc. | `AAPL` | 355.63 | 344.62 | **-3.1%** | 40 | USD |

Price/target uses the underlying Yahoo Finance share quote, not the OKX derivative. Minimum 3 analysts; unreliable price scales and missing coverage excluded. Targets are analyst opinions, not guaranteed forecasts.

## All OKX companies — our ratio + LONG/SHORT scores

| Company | OKX | P/S | EV/S | Op margin | Fwd P/E | EPS +1y | Rev +1y | FCF yield | LONG | SHORT |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| QUALCOMM Incorporated | `QCOM` | 4.4 | 4.5 | 20.8% | 14.5 | 27.3% | 15.6% | 4.8% | **100 CORE** | **0** |
| Rocket Lab Corporation | `RKLB` | 50.5 | 39.9 | -27.6% | 972.4 | 74.6% | 37.6% | -0.5% | **0** | **100 CORE** |
| USA Rare Earth, Inc. | `USAR` | 191.8 | 95.7 | -1476.1% | 275.5 | 105.3% | 954.6% | -9.9% | **0** | **100 CORE** |
| Moderna, Inc. | `MRNA` | 39.9 | 39.8 | -80.8% | -59.3 | 41.1% | 10.6% | -0.6% | **0** | **94 WATCH** |
| Sandisk Corporation | `SNDK` | 4.8 | 4.1 | 72.7% | 3.4 | 27.1% | 23.7% | 8.1% | **90 CORE** | **10** |
| Taiwan Semiconductor Manufactur | `TSM` | 0.4 | 2.7 | 58.0% | 17.7 | 33.6% | 37.8% | 56.1% | **90 CORE** | **10** |
| Applovin Corporation | `APP` | 17.6 | 17.3 | 77.8% | 19.4 | 26.1% | 24.8% | 2.8% | **83 CORE** | **10** |
| IonQ, Inc. | `IONQ` | 41.6 | 37.5 | -306.3% | -24.3 | -39.3% | 70.7% | -0.8% | **0** | **82 WATCH** |
| Okta, Inc. | `OKTA` | 10.4 | 9.4 | 7.7% | 41.6 | 11.4% | 10.1% | 3.3% | **8** | **80 CORE** |
| Nebius Group N.V. | `NBIS` | 31.0 | 28.7 | -37.4% | -44.5 | -191.4% | 267.0% | -22.9% | **0** | **80 WATCH** |
| AST SpaceMobile, Inc. | `ASTS` | 100.0 | 83.2 | -393.3% | -23.5 | 28.8% | 249.8% | -13.2% | **0** | **80 WATCH** |
| Tesla, Inc. | `TSLA` | 14.9 | 14.2 | 3.0% | 181.0 | 25.2% | 13.5% | 0.3% | **20** | **78** |
| Robinhood Markets, Inc. | `HOOD` | 15.0 | 14.0 | 45.7% | 24.8 | 39.7% | 29.2% | — | **77 WATCH** | **0** |
| Marvell Technology, Inc. | `MRVL` | 16.1 | 14.5 | 16.8% | 23.0 | 74.2% | 63.9% | 1.6% | **77 WATCH** | **13** |
| Corning Incorporated | `GLW` | 5.9 | 5.9 | 16.8% | 26.5 | 34.6% | 21.2% | 0.8% | **77 WATCH** | **13** |
| Applied Materials, Inc. | `AMAT` | 10.2 | 9.5 | 31.2% | 21.2 | 45.5% | 35.7% | 1.0% | **77 WATCH** | **3** |
| NVIDIA Corporation | `NVDA` | 13.8 | 13.4 | 65.2% | 10.9 | 70.8% | 67.8% | 1.0% | **75 WATCH** | **18** |
| Broadcom Inc. | `AVGO` | 18.5 | 18.2 | 48.8% | 17.7 | 66.9% | 65.6% | 1.9% | **75 WATCH** | **28** |
| Credo Technology Group Holding  | `CRDO` | 16.7 | 14.9 | 31.7% | 14.6 | 53.9% | 55.0% | 0.9% | **75 WATCH** | **28** |
| AXT Inc | `AXT` | 18.0 | 12.8 | 19.6% | 18.4 | 116.3% | 115.9% | — | **75 WATCH** | **20** |
| Western Digital Corporation | `WDC` | 8.1 | 7.4 | 40.9% | 7.8 | 63.4% | 40.5% | 2.3% | **75 WATCH** | **18** |
| Micron Technology, Inc. | `MU` | 6.9 | 5.9 | 74.6% | 3.9 | 17.7% | 16.0% | 3.2% | **75 CORE** | **30** |
| Dell Technologies Inc. | `DELL` | 1.6 | 1.6 | 9.9% | 12.3 | 16.8% | 19.5% | 2.5% | **75 CORE** | **30** |
| IREN LIMITED | `IREN` | 12.7 | 21.7 | -72.9% | 77.2 | 116.3% | 206.6% | -99.3% | **0** | **74 WATCH** |
| Circle Internet Group, Inc. | `CRCL` | 5.7 | 4.9 | 11.3% | 47.1 | 0.5% | 24.1% | 1.5% | **15** | **73 CORE** |
| Cerebras Systems Inc. | `CBRS` | 35.3 | 23.2 | -81.2% | 79.0 | 370.9% | 233.1% | — | **0** | **71 WATCH** |
| Oracle Corporation | `ORCL` | 5.6 | 6.9 | 34.3% | 11.6 | 35.7% | 45.7% | -11.5% | **70 WATCH** | **10** |
| Advanced Micro Devices, Inc. | `AMD` | 20.0 | 18.5 | 17.8% | 31.3 | 118.8% | 83.5% | 0.8% | **70 WATCH** | **13** |
| Adobe Inc. | `ADBE` | 3.6 | 3.6 | 36.3% | 8.7 | 12.0% | 9.1% | 10.1% | **65 WATCH** | **30** |
| XIAOMI-W | `XIAOMI` | 1.8 | 1.6 | 4.7% | 20.4 | 39.5% | 19.2% | -1.1% | **62 WATCH** | **10** |
| Coherent Corp. | `COHR` | 5.8 | 5.7 | 14.1% | 14.9 | 51.7% | 39.9% | -3.6% | **60 WATCH** | **35** |
| Microsoft Corporation | `MSFT` | 11.2 | 11.6 | 47.1% | 21.5 | 20.9% | 20.5% | 0.1% | **59 WATCH** | **3** |
| Coca-Cola Company (The) | `KO` | 8.2 | 8.7 | 32.2% | 27.6 | 5.7% | -3.1% | 1.0% | **0** | **58** |
| Meta Platforms, Inc. | `META` | 6.7 | 6.9 | 37.8% | 17.7 | 16.7% | 21.7% | 1.0% | **57 WATCH** | **38** |
| Netflix, Inc. | `NFLX` | 5.3 | 5.4 | 31.3% | 17.1 | 5.1% | 10.7% | 9.6% | **35** | **50** |
| Palantir Technologies Inc. | `PLTR` | 57.0 | 54.4 | 45.6% | 67.9 | 49.2% | 53.5% | 0.6% | **45** | **48** |
| Bloom Energy Corporation | `BE` | 16.2 | 14.4 | 14.3% | 39.3 | 62.7% | 56.4% | -0.0% | **45** | **35** |
| SamsungElec | `SAMSUNG` | 2.3 | 1.9 | 46.1% | 2.7 | 62.3% | 40.9% | 6.2% | **45** | **10** |
| Super Micro Computer, Inc. | `SMCI` | 0.4 | 0.5 | 8.3% | 4.4 | 6.5% | 11.3% | -40.8% | **35** | **45** |
| Arm Holdings plc | `ARM` | 39.8 | 35.0 | 17.0% | 66.2 | 35.5% | 37.2% | 0.5% | **43** | **33** |
| SOFTBANK GROUP CORP | `SOFTBANK` | 2.6 | 6.2 | -6.3% | 13.1 | 85.8% | 6.1% | -4.7% | **0** | **40** |
| CoreWeave, Inc. | `CRWV` | 3.4 | 9.0 | -0.5% | -33.4 | 9.8% | 107.0% | -58.8% | **0** | **40** |
| Apple Inc. | `AAPL` | 10.8 | 10.7 | 33.0% | 33.7 | 19.7% | 8.2% | 2.0% | **25** | **38** |
| Coinbase Global, Inc. | `COIN` | 6.6 | 6.1 | 0.1% | 56.4 | 782.5% | 27.1% | 10.2% | **35** | **25** |
| Lumentum Holdings Inc. | `LITE` | 15.7 | 14.0 | 23.4% | 16.1 | 60.9% | 57.9% | 0.2% | **20** | **33** |
| SK hynix | `SKHYNIX` | 3.3 | 3.1 | 74.5% | 2.4 | 49.0% | 60.4% | — | **30** | **5** |
| SK hynix | `SKHY` | 3.3 | 3.1 | 74.5% | 2.4 | 49.0% | 60.4% | — | **30** | **5** |
| Alphabet Inc. | `GOOGL` | 7.7 | 7.3 | 33.3% | 19.0 | -23.5% | 27.6% | -0.0% | **5** | **30** |
| Amazon.com, Inc. | `AMZN` | 3.6 | 3.9 | 13.1% | 24.4 | -16.6% | 15.8% | -1.2% | **0** | **30** |
| Intel Corporation | `INTC` | 5.5 | 5.4 | 10.3% | 34.9 | 20.4% | 12.0% | 0.2% | **5** | **28** |
| Fluence Energy, Inc. | `FLNC` | 0.4 | 0.3 | -4.2% | -9.6 | 59.3% | 25.4% | 0.2% | **5** | **28** |
| Strategy Inc | `MSTR` | 104.6 | 131.4 | -1100.1% | 7.1 | 380.1% | 3.2% | -6.3% | **25** | **25** |
| BitMine Immersion Technologies, | `BMNR` | 189.7 | 172.7 | -481.9% | 20.5 | 84.2% | 58.9% | -4.5% | **25** | **25** |
| Applied Optoelectronics, Inc. | `AAOI` | 6.8 | 5.5 | -6.8% | 14.6 | 454.1% | 135.1% | -25.8% | **10** | **25** |
| Hyperliquid Strategies Inc | `PURR` | 117.3 | 99.9 | 6252.0% | 44.6 | -79.8% | 22.8% | — | **0** | **25 WATCH** |

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
