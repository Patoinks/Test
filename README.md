# OKX Long / Short Fundamental Scanner

Hourly scanner restricted to public companies exposed by the **OKX EEA TradFi / Stock Perpetual API universe**.

**Last scan:** 2026-11-12 20:53 UTC  
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
| 1 | NVIDIA Corporation | NVDA | -4.5% | -8.7% | -6.6% | 82 | +5 | **87** | **CORE** | yes |
| 2 | Sandisk Corporation | SNDK | -4.1% | 16.3% | 6.1% | 90 | -5 | **85** | **CORE** | yes |
| 3 | Taiwan Semiconductor Manufactur | TSM | -1.9% | 14.9% | 6.5% | 88 | -5 | **83** | **CORE** | yes |
| 4 | QUALCOMM Incorporated | QCOM | 0.1% | 12.7% | 6.4% | 85 | -5 | **80** | **CORE** | yes |
| 5 | Robinhood Markets, Inc. | HOOD | -3.5% | 4.1% | 0.3% | 80 | +0 | **80** | **CORE** | yes |
| 6 | AXT Inc | AXT | -8.0% | 17.7% | 4.9% | 82 | -4 | **78** | **CORE** | yes |
| 7 | Marvell Technology, Inc. | MRVL | -2.6% | 23.2% | 10.3% | 84 | -8 | **76** | **CORE** | yes |
| 8 | Applovin Corporation | APP | -2.5% | 10.8% | 4.1% | 79 | -3 | **76** | **CORE** | yes |
| 9 | Applied Materials, Inc. | AMAT | -3.8% | 19.0% | 7.6% | 81 | -6 | **75** | **CORE** | yes |
| 10 | Corning Incorporated | GLW | -1.1% | 15.1% | 7.0% | 80 | -6 | **74** | **WATCH** | yes |

## Final model + Price Timing — SHORT

| Rank | Company | OKX | 24h | 7d | 50/50 move | Base SHORT | Timing adj. | Final | Signal | Prev. SHORT? |
|---:|---|---|---:|---:|---:|---:|---:|---:|---|---|
| 1 | Rocket Lab Corporation | RKLB | -3.2% | 39.2% | 18.0% | 100 | +14 | **100** | **CORE** | yes |
| 2 | Moderna, Inc. | MRNA | -7.4% | -4.6% | -6.0% | 94 | -5 | **89** | **CORE** | yes |
| 3 | USA Rare Earth, Inc. | USAR | -1.6% | 9.6% | 4.0% | 86 | +3 | **89** | **CORE** | yes |
| 4 | AST SpaceMobile, Inc. | ASTS | -5.2% | 14.9% | 4.8% | 80 | +4 | **84** | **CORE** | yes |
| 5 | IonQ, Inc. | IONQ | -9.5% | 16.6% | 3.5% | 79 | +3 | **82** | **CORE** | yes |
| 6 | Cerebras Systems Inc. | CBRS | -3.2% | 19.7% | 8.2% | 75 | +7 | **82** | **CORE** | yes |
| 7 | Nebius Group N.V. | NBIS | -17.3% | 6.3% | -5.5% | 80 | -4 | **76** | **CORE** | yes |
| 8 | Tesla, Inc. | TSLA | 1.5% | 15.5% | 8.5% | 59 | +7 | **66** | **WATCH** | yes |
| 9 | Okta, Inc. | OKTA | 0.1% | 6.6% | 3.3% | 60 | +3 | **63** | **WATCH** | yes |
| 10 | IREN LIMITED | IREN | -7.3% | 7.1% | -0.1% | 59 | +0 | **59** | **WATCH** | yes |

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
| 9 | Applied Materials, Inc. | `AMAT` | 77 | 91 | **81** | **CORE** |
| 10 | Robinhood Markets, Inc. | `HOOD` | 77 | 86 | **80** | **CORE** |

## Combined model — SHORT

Weighted score: **70% fundamental + 30% P/E trend**.

| Rank | Company | OKX | Fundamental SHORT | P/E trend SHORT | Combined | Signal |
|---:|---|---|---:|---:|---:|---|
| 1 | Rocket Lab Corporation | `RKLB` | 100 | 0 | **100** | **CORE** |
| 2 | Moderna, Inc. | `MRNA` | 94 | 0 | **94** | **WATCH** |
| 3 | USA Rare Earth, Inc. | `USAR` | 86 | 0 | **86** | **CORE** |
| 4 | AST SpaceMobile, Inc. | `ASTS` | 80 | 0 | **80** | **WATCH** |
| 5 | Nebius Group N.V. | `NBIS` | 80 | 0 | **80** | **WATCH** |
| 6 | IonQ, Inc. | `IONQ` | 79 | 0 | **79** | **WATCH** |
| 7 | Cerebras Systems Inc. | `CBRS` | 75 | 0 | **75** | **WATCH** |
| 8 | Okta, Inc. | `OKTA` | 80 | 13 | **60** | **WATCH** |
| 9 | Tesla, Inc. | `TSLA` | 78 | 15 | **59** | **WATCH** |

## P/E Compression + Growth — LONG

| Rank | Company | OKX | Trail P/E | Fwd P/E | P/E change | EPS +1y | Rev +1y | Rev trend | LONG score | Signal |
|---:|---|---|---:|---:|---:|---:|---:|---|---:|---|
| 1 | NVIDIA Corporation | `NVDA` | 21.0 | 10.4 | -50.3% | 70.9% | 68.0% | decelerating | **100** | **CORE** |
| 2 | AXT Inc | `AXT` | 88.2 | 17.0 | -80.8% | 116.3% | 115.9% | decelerating | **100** | **CORE** |
| 3 | Marvell Technology, Inc. | `MRVL` | 54.1 | 22.4 | -58.6% | 74.2% | 63.9% | accelerating | **100** | **CORE** |
| 4 | Credo Technology Group Holding  | `CRDO` | 49.6 | 14.4 | -71.0% | 53.9% | 55.0% | decelerating | **100** | **CORE** |
| 5 | Broadcom Inc. | `AVGO` | 46.3 | 18.6 | -59.8% | 66.9% | 65.6% | decelerating | **100** | **CORE** |
| 6 | Advanced Micro Devices, Inc. | `AMD` | 124.2 | 32.9 | -73.5% | 118.8% | 83.5% | accelerating | **100** | **CORE** |
| 7 | Coherent Corp. | `COHR` | 48.1 | 14.7 | -69.4% | 51.7% | 39.9% | decelerating | **100** | **CORE** |
| 8 | Oracle Corporation | `ORCL` | 19.9 | 11.5 | -42.3% | 35.7% | 45.7% | accelerating | **95** | **CORE** |
| 9 | Arm Holdings plc | `ARM` | 229.5 | 64.9 | -71.7% | 35.5% | 37.3% | accelerating | **95** | **CORE** |
| 10 | Bloom Energy Corporation | `BE` | 122.4 | 37.9 | -69.0% | 62.7% | 56.4% | decelerating | **92** | **CORE** |

## P/E Expansion + Weakening — SHORT

| Rank | Company | OKX | Trail P/E | Fwd P/E | P/E change | EPS +1y | Rev +1y | Rev trend | SHORT score | Signal |
|---:|---|---|---:|---:|---:|---:|---:|---|---:|---|
| 1 | Hyperliquid Strategies Inc | `PURR` | 3.8 | 43.2 | 1051.2% | -79.8% | 22.8% | decelerating | **80** | **CORE** |
| 2 | Alphabet Inc. | `GOOGL` | 15.6 | 19.3 | 24.1% | -23.5% | 27.6% | accelerating | **50** | **WATCH** |

## Top SHORT candidates

| Rank | Company | OKX market | SHORT score | Signal | P/S | EV/S | Op margin | Fwd P/E | Rev +1y | FCF yield |
|---:|---|---|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Rocket Lab Corporation | `RKLB-USDT-SWAP` | **100** | **CORE** | 48.8 | 42.3 | -27.6% | 908.3 | 37.6% | -0.5% |
| 2 | Moderna, Inc. | `MRNA-USDT-SWAP` | **94** | **WATCH** | 36.9 | 39.5 | -80.8% | -55.8 | 10.6% | -0.6% |
| 3 | USA Rare Earth, Inc. | `USAR-USDT-SWAP` | **86** | **CORE** | 188.7 | 101.9 | -1476.1% | 13.7 | 1245.4% | -10.1% |
| 4 | Nebius Group N.V. | `NBIS-USDT-SWAP` | **80** | **WATCH** | 25.7 | 32.9 | -37.4% | -36.8 | 267.0% | -27.6% |
| 5 | Okta, Inc. | `OKTA-USDT-SWAP` | **80** | **CORE** | 10.4 | 9.6 | 7.7% | 41.7 | 10.1% | 3.3% |
| 6 | AST SpaceMobile, Inc. | `ASTS-USDT-SWAP` | **80** | **WATCH** | 94.7 | 89.4 | -393.3% | -22.2 | 249.8% | -14.0% |
| 7 | IonQ, Inc. | `IONQ-USDT-SWAP` | **79** | **WATCH** | 37.6 | 36.4 | -306.3% | -21.9 | 70.7% | -0.8% |
| 8 | Cerebras Systems Inc. | `CBRS-USDT-SWAP` | **75** | **WATCH** | 34.1 | 25.8 | -81.2% | 76.5 | 233.1% | — |
| 9 | Circle Internet Group, Inc. | `CRCL-USDT-SWAP` | **63** | **CORE** | 5.4 | 5.1 | 11.3% | 44.9 | 24.1% | 1.6% |
| 10 | Hyperliquid Strategies Inc | `PURR-USDT-SWAP` | **25** | **WATCH** | 113.5 | 105.0 | 6252.0% | 43.2 | 22.8% | — |

## Top LONG candidates

| Rank | Company | OKX market | LONG score | Signal | P/S | EV/S | Op margin | Fwd P/E | Rev +1y | FCF yield |
|---:|---|---|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | QUALCOMM Incorporated | `QCOM-USDT-SWAP` | **100** | **CORE** | 4.4 | 4.6 | 20.8% | 14.5 | 15.6% | 4.8% |
| 2 | Taiwan Semiconductor Manufactur | `TSM-USDT-SWAP` | **90** | **CORE** | 0.4 | 2.8 | 58.0% | 17.3 | 37.8% | 57.2% |
| 3 | Sandisk Corporation | `SNDK-USDT-SWAP` | **90** | **CORE** | 4.6 | 4.6 | 72.7% | 3.2 | 23.7% | 8.4% |
| 4 | Applovin Corporation | `APP-USDT-SWAP` | **83** | **CORE** | 17.2 | 17.7 | 77.8% | 18.9 | 25.2% | 2.8% |
| 5 | Corning Incorporated | `GLW-USDT-SWAP` | **77** | **WATCH** | 5.8 | 6.3 | 16.8% | 26.2 | 21.2% | 0.8% |
| 6 | Robinhood Markets, Inc. | `HOOD-USDT-SWAP` | **77** | **WATCH** | 14.5 | 14.6 | 45.7% | 23.9 | 29.2% | — |
| 7 | Applied Materials, Inc. | `AMAT-USDT-SWAP` | **77** | **WATCH** | 9.8 | 10.1 | 31.2% | 20.4 | 35.8% | 1.0% |
| 8 | Marvell Technology, Inc. | `MRVL-USDT-SWAP` | **77** | **WATCH** | 15.7 | 15.8 | 16.8% | 22.4 | 63.9% | 1.6% |
| 9 | Dell Technologies Inc. | `DELL-USDT-SWAP` | **75** | **CORE** | 1.6 | 1.7 | 9.9% | 12.2 | 19.5% | 2.6% |
| 10 | Broadcom Inc. | `AVGO-USDT-SWAP` | **75** | **WATCH** | 19.4 | 18.9 | 48.8% | 18.6 | 65.6% | 1.8% |

## Analyst consensus (12-month price target) — most upside

| Rank | Company | OKX | Price | Analyst mean target | Gap | Analysts | Currency |
|---:|---|---|---:|---:|---:|---:|---|
| 1 | IREN LIMITED | `IREN` | 19.31 | 56.69 | **193.5%** | 19 | USD |
| 2 | Hyperliquid Strategies Inc | `PURR` | 8.86 | 22.50 | **154.1%** | 4 | USD |
| 3 | Cerebras Systems Inc. | `CBRS` | 97.82 | 245.18 | **150.6%** | 11 | USD |
| 4 | SK hynix | `SKHYNIX` | 1254000.00 | 3097152.20 | **147.0%** | 39 | KRW |
| 5 | SamsungElec | `SAMSUNG` | 208000.00 | 475628.56 | **128.7%** | 35 | KRW |
| 6 | Sandisk Corporation | `SNDK` | 937.58 | 2047.38 | **118.4%** | 24 | USD |
| 7 | Nebius Group N.V. | `NBIS` | 127.97 | 278.05 | **117.3%** | 20 | USD |
| 8 | CoreWeave, Inc. | `CRWV` | 56.60 | 121.26 | **114.2%** | 38 | USD |
| 9 | AXT Inc | `AXT` | 43.23 | 91.50 | **111.7%** | 6 | USD |
| 10 | Applied Optoelectronics, Inc. | `AAOI` | 52.93 | 109.00 | **105.9%** | 5 | USD |
| 11 | SOFTBANK GROUP CORP | `SOFTBANK` | 3738.00 | 7656.31 | **104.8%** | 18 | JPY |
| 12 | Credo Technology Group Holding  | `CRDO` | 140.01 | 284.05 | **102.9%** | 19 | USD |
| 13 | Strategy Inc | `MSTR` | 115.26 | 233.27 | **102.4%** | 15 | USD |
| 14 | Western Digital Corporation | `WDC` | 310.12 | 613.38 | **97.8%** | 24 | USD |
| 15 | Micron Technology, Inc. | `MU` | 797.79 | 1561.91 | **95.8%** | 45 | USD |

## Analyst consensus (12-month price target) — most downside

| Rank | Company | OKX | Price | Analyst mean target | Gap | Analysts | Currency |
|---:|---|---|---:|---:|---:|---:|---|
| 1 | Moderna, Inc. | `MRNA` | 230.26 | 158.47 | **-31.2%** | 19 | USD |
| 2 | Apple Inc. | `AAPL` | 354.56 | 344.62 | **-2.8%** | 40 | USD |

Price/target uses the underlying Yahoo Finance share quote, not the OKX derivative. Minimum 3 analysts; unreliable price scales and missing coverage excluded. Targets are analyst opinions, not guaranteed forecasts.

## All OKX companies — our ratio + LONG/SHORT scores

| Company | OKX | P/S | EV/S | Op margin | Fwd P/E | EPS +1y | Rev +1y | FCF yield | LONG | SHORT |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| QUALCOMM Incorporated | `QCOM` | 4.4 | 4.6 | 20.8% | 14.5 | 27.3% | 15.6% | 4.8% | **100 CORE** | **0** |
| Rocket Lab Corporation | `RKLB` | 48.8 | 42.3 | -27.6% | 908.3 | 77.3% | 37.6% | -0.5% | **0** | **100 CORE** |
| Moderna, Inc. | `MRNA` | 36.9 | 39.5 | -80.8% | -55.8 | 41.1% | 10.6% | -0.6% | **0** | **94 WATCH** |
| Sandisk Corporation | `SNDK` | 4.6 | 4.6 | 72.7% | 3.2 | 27.1% | 23.7% | 8.4% | **90 CORE** | **10** |
| Taiwan Semiconductor Manufactur | `TSM` | 0.4 | 2.8 | 58.0% | 17.3 | 33.6% | 37.8% | 57.2% | **90 CORE** | **10** |
| USA Rare Earth, Inc. | `USAR` | 188.7 | 101.9 | -1476.1% | 13.7 | 105.3% | 1245.4% | -10.1% | **0** | **86 CORE** |
| Applovin Corporation | `APP` | 17.2 | 17.7 | 77.8% | 18.9 | 27.4% | 25.2% | 2.8% | **83 CORE** | **10** |
| Okta, Inc. | `OKTA` | 10.4 | 9.6 | 7.7% | 41.7 | 11.4% | 10.1% | 3.3% | **8** | **80 CORE** |
| AST SpaceMobile, Inc. | `ASTS` | 94.7 | 89.4 | -393.3% | -22.2 | 28.8% | 249.8% | -14.0% | **0** | **80 WATCH** |
| Nebius Group N.V. | `NBIS` | 25.7 | 32.9 | -37.4% | -36.8 | -191.4% | 267.0% | -27.6% | **0** | **80 WATCH** |
| IonQ, Inc. | `IONQ` | 37.6 | 36.4 | -306.3% | -21.9 | -39.3% | 70.7% | -0.8% | **0** | **79 WATCH** |
| Tesla, Inc. | `TSLA` | 15.1 | 14.6 | 3.0% | 183.8 | 25.2% | 13.5% | 0.3% | **20** | **78** |
| Robinhood Markets, Inc. | `HOOD` | 14.5 | 14.6 | 45.7% | 23.9 | 39.7% | 29.2% | — | **77 WATCH** | **0** |
| Marvell Technology, Inc. | `MRVL` | 15.7 | 15.8 | 16.8% | 22.4 | 74.2% | 63.9% | 1.6% | **77 WATCH** | **13** |
| Applied Materials, Inc. | `AMAT` | 9.8 | 10.1 | 31.2% | 20.4 | 45.9% | 35.8% | 1.0% | **77 WATCH** | **3** |
| Corning Incorporated | `GLW` | 5.8 | 6.3 | 16.8% | 26.2 | 34.6% | 21.2% | 0.8% | **77 WATCH** | **13** |
| NVIDIA Corporation | `NVDA` | 13.2 | 13.7 | 65.2% | 10.4 | 70.9% | 68.0% | 1.0% | **75 WATCH** | **18** |
| AXT Inc | `AXT` | 16.6 | 15.6 | 19.6% | 17.0 | 116.3% | 115.9% | — | **75 WATCH** | **20** |
| Credo Technology Group Holding  | `CRDO` | 16.5 | 16.2 | 31.7% | 14.4 | 53.9% | 55.0% | 0.9% | **75 WATCH** | **28** |
| Western Digital Corporation | `WDC` | 8.0 | 8.1 | 40.9% | 7.7 | 63.4% | 40.5% | 2.4% | **75 WATCH** | **18** |
| Broadcom Inc. | `AVGO` | 19.4 | 18.9 | 48.8% | 18.6 | 66.9% | 65.6% | 1.8% | **75 WATCH** | **28** |
| Micron Technology, Inc. | `MU` | 6.8 | 6.6 | 74.6% | 3.8 | 17.7% | 16.0% | 3.2% | **75 CORE** | **30** |
| Dell Technologies Inc. | `DELL` | 1.6 | 1.7 | 9.9% | 12.2 | 16.8% | 19.5% | 2.6% | **75 CORE** | **30** |
| Cerebras Systems Inc. | `CBRS` | 34.1 | 25.8 | -81.2% | 76.5 | 370.9% | 233.1% | — | **0** | **75 WATCH** |
| Oracle Corporation | `ORCL` | 5.5 | 7.3 | 34.3% | 11.5 | 35.7% | 45.7% | -11.6% | **70 WATCH** | **10** |
| Advanced Micro Devices, Inc. | `AMD` | 21.0 | 19.8 | 17.8% | 32.9 | 118.8% | 83.5% | 0.8% | **70 WATCH** | **13** |
| Adobe Inc. | `ADBE` | 3.6 | 3.6 | 36.3% | 8.7 | 12.0% | 9.1% | 10.0% | **65 WATCH** | **30** |
| Circle Internet Group, Inc. | `CRCL` | 5.4 | 5.1 | 11.3% | 44.9 | 0.5% | 24.1% | 1.6% | **15** | **63 CORE** |
| XIAOMI-W | `XIAOMI` | 1.8 | 1.6 | 4.7% | 20.3 | 39.5% | 19.2% | -1.1% | **62 WATCH** | **10** |
| Coherent Corp. | `COHR` | 5.8 | 6.2 | 14.1% | 14.7 | 51.7% | 39.9% | -3.7% | **60 WATCH** | **35** |
| Microsoft Corporation | `MSFT` | 11.2 | 11.4 | 47.1% | 21.5 | 20.9% | 20.5% | 0.1% | **59 WATCH** | **3** |
| IREN LIMITED | `IREN` | 11.8 | 22.4 | -72.9% | 71.5 | 116.3% | 199.7% | — | **0** | **59** |
| Apple Inc. | `AAPL` | 10.8 | 10.9 | 33.0% | 33.6 | 12.2% | 8.2% | 2.1% | **5** | **58** |
| Coca-Cola Company (The) | `KO` | 8.2 | 8.8 | 32.2% | 27.6 | 5.7% | -3.1% | 1.0% | **0** | **58** |
| Meta Platforms, Inc. | `META` | 6.6 | 6.8 | 37.8% | 17.4 | 16.7% | 21.7% | 1.1% | **57 WATCH** | **38** |
| Netflix, Inc. | `NFLX` | 5.2 | 5.5 | 31.3% | 16.6 | 5.1% | 10.7% | 9.9% | **35** | **50** |
| Palantir Technologies Inc. | `PLTR` | 56.8 | 55.6 | 45.6% | 67.6 | 49.2% | 53.5% | 0.6% | **45** | **48** |
| Bloom Energy Corporation | `BE` | 15.6 | 16.3 | 14.3% | 37.9 | 62.7% | 56.4% | -0.0% | **45** | **35** |
| SamsungElec | `SAMSUNG` | 2.3 | 2.0 | 46.1% | 2.7 | 62.3% | 40.9% | 6.2% | **45** | **10** |
| Super Micro Computer, Inc. | `SMCI` | 0.3 | 0.5 | 8.3% | 3.9 | 6.5% | 11.3% | -45.7% | **35** | **45** |
| Arm Holdings plc | `ARM` | 39.1 | 39.3 | 17.0% | 64.9 | 35.5% | 37.3% | 0.5% | **43** | **33** |
| Lumentum Holdings Inc. | `LITE` | 15.1 | 15.6 | 23.4% | 15.6 | 60.9% | 57.9% | 0.3% | **10** | **43** |
| CoreWeave, Inc. | `CRWV` | 3.2 | 9.7 | -0.5% | -32.6 | 13.3% | 107.4% | -63.1% | **0** | **40** |
| SOFTBANK GROUP CORP | `SOFTBANK` | 2.6 | 6.1 | -6.1% | 12.7 | 87.5% | 6.3% | -6.5% | **0** | **40** |
| Coinbase Global, Inc. | `COIN` | 6.4 | 6.3 | 0.1% | 54.1 | 782.5% | 27.1% | 10.6% | **35** | **25** |
| SK hynix | `SKHYNIX` | 3.3 | 3.0 | 74.5% | 2.3 | 48.7% | 60.4% | — | **30** | **5** |
| SK hynix | `SKHY` | 3.3 | 3.0 | 74.5% | 2.3 | 48.7% | 60.4% | — | **30** | **5** |
| Alphabet Inc. | `GOOGL` | 7.8 | 7.5 | 33.3% | 19.3 | -23.5% | 27.6% | -0.0% | **5** | **30** |
| Amazon.com, Inc. | `AMZN` | 3.6 | 3.8 | 13.1% | 24.5 | -16.6% | 15.8% | -1.2% | **0** | **30** |
| Intel Corporation | `INTC` | 5.4 | 5.8 | 10.3% | 34.2 | 20.4% | 12.0% | 0.2% | **5** | **28** |
| Fluence Energy, Inc. | `FLNC` | 0.3 | 0.3 | -4.2% | -8.9 | 59.3% | 25.4% | 0.3% | **5** | **28** |
| BitMine Immersion Technologies, | `BMNR` | 93.2 | 96564.2 | -216.6% | 19.8 | 105.8% | 58.9% | -1.4% | **25** | **25** |
| Strategy Inc | `MSTR` | 98.5 | 132.5 | -1100.1% | 6.7 | 380.1% | 3.2% | -6.6% | **25** | **25** |
| Applied Optoelectronics, Inc. | `AAOI` | 6.4 | 6.4 | -6.8% | 14.1 | 439.3% | 135.1% | -27.3% | **10** | **25** |
| Hyperliquid Strategies Inc | `PURR` | 113.5 | 105.0 | 6252.0% | 43.2 | -79.8% | 22.8% | — | **0** | **25 WATCH** |

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
