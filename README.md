# OKX Long / Short Fundamental Scanner

Hourly scanner restricted to public companies exposed by the **OKX EEA TradFi / Stock Perpetual API universe**.

**Last scan:** 2026-11-14 19:16 UTC  
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
| 1 | Sandisk Corporation | SNDK | -0.0% | 6.0% | 3.0% | 90 | -2 | **88** | **CORE** | yes |
| 2 | NVIDIA Corporation | NVDA | -0.0% | -12.7% | -6.4% | 82 | +5 | **87** | **CORE** | yes |
| 3 | Taiwan Semiconductor Manufactur | TSM | -0.0% | 6.2% | 3.1% | 88 | -2 | **86** | **CORE** | yes |
| 4 | QUALCOMM Incorporated | QCOM | -0.0% | 4.3% | 2.1% | 85 | -2 | **83** | **CORE** | yes |
| 5 | Robinhood Markets, Inc. | HOOD | -0.0% | -3.8% | -1.9% | 80 | +2 | **82** | **CORE** | yes |
| 6 | Marvell Technology, Inc. | MRVL | 0.0% | 11.0% | 5.5% | 84 | -4 | **80** | **CORE** | yes |
| 7 | AXT Inc | AXT | -0.0% | 7.6% | 3.8% | 82 | -3 | **79** | **CORE** | yes |
| 8 | Credo Technology Group Holding  | CRDO | 0.0% | 9.1% | 4.6% | 82 | -4 | **78** | **CORE** | yes |
| 9 | Corning Incorporated | GLW | -0.0% | 7.5% | 3.7% | 80 | -3 | **77** | **CORE** | yes |
| 10 | Applovin Corporation | APP | -0.0% | 4.6% | 2.3% | 79 | -2 | **77** | **CORE** | yes |

## Final model + Price Timing — SHORT

| Rank | Company | OKX | 24h | 7d | 50/50 move | Base SHORT | Timing adj. | Final | Signal | Prev. SHORT? |
|---:|---|---|---:|---:|---:|---:|---:|---:|---|---|
| 1 | Rocket Lab Corporation | RKLB | 0.0% | 15.9% | 8.0% | 100 | +6 | **100** | **CORE** | yes |
| 2 | Moderna, Inc. | MRNA | 0.0% | -12.1% | -6.1% | 94 | -5 | **89** | **CORE** | yes |
| 3 | USA Rare Earth, Inc. | USAR | 0.0% | -0.8% | -0.4% | 86 | +0 | **86** | **CORE** | yes |
| 4 | Cerebras Systems Inc. | CBRS | -0.0% | 21.2% | 10.6% | 75 | +8 | **83** | **CORE** | yes |
| 5 | AST SpaceMobile, Inc. | ASTS | 0.0% | 0.8% | 0.4% | 80 | +0 | **80** | **CORE** | yes |
| 6 | IonQ, Inc. | IONQ | 0.0% | -11.5% | -5.7% | 79 | -5 | **74** | **WATCH** | yes |
| 7 | Okta, Inc. | OKTA | 0.0% | 8.4% | 4.2% | 60 | +3 | **63** | **WATCH** | yes |
| 8 | Tesla, Inc. | TSLA | -0.0% | 8.9% | 4.5% | 59 | +4 | **63** | **WATCH** | yes |
| 9 | Nebius Group N.V. | NBIS | 0.0% | -10.5% | -5.3% | 60 | -4 | **56** | **WATCH** | yes |

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
| 6 | Cerebras Systems Inc. | `CBRS` | 75 | 0 | **75** | **WATCH** |
| 7 | Okta, Inc. | `OKTA` | 80 | 13 | **60** | **WATCH** |
| 8 | Tesla, Inc. | `TSLA` | 78 | 15 | **59** | **WATCH** |

## P/E Compression + Growth — LONG

| Rank | Company | OKX | Trail P/E | Fwd P/E | P/E change | EPS +1y | Rev +1y | Rev trend | LONG score | Signal |
|---:|---|---|---:|---:|---:|---:|---:|---|---:|---|
| 1 | NVIDIA Corporation | `NVDA` | 20.6 | 10.3 | -50.1% | 70.0% | 67.2% | decelerating | **100** | **CORE** |
| 2 | Marvell Technology, Inc. | `MRVL` | 51.6 | 21.3 | -58.6% | 74.2% | 63.9% | accelerating | **100** | **CORE** |
| 3 | AXT Inc | `AXT` | 85.4 | 16.4 | -80.8% | 116.3% | 115.9% | decelerating | **100** | **CORE** |
| 4 | Credo Technology Group Holding  | `CRDO` | 46.6 | 13.5 | -71.0% | 53.9% | 55.0% | decelerating | **100** | **CORE** |
| 5 | Broadcom Inc. | `AVGO` | 44.3 | 17.9 | -59.7% | 66.4% | 65.1% | decelerating | **100** | **CORE** |
| 6 | Advanced Micro Devices, Inc. | `AMD` | 114.1 | 30.2 | -73.5% | 118.8% | 83.6% | accelerating | **100** | **CORE** |
| 7 | Coherent Corp. | `COHR` | 45.2 | 13.8 | -69.4% | 51.7% | 39.9% | decelerating | **100** | **CORE** |
| 8 | Oracle Corporation | `ORCL` | 19.6 | 11.3 | -42.3% | 35.7% | 45.7% | accelerating | **95** | **CORE** |
| 9 | Arm Holdings plc | `ARM` | 219.0 | 62.0 | -71.7% | 35.6% | 37.3% | accelerating | **95** | **CORE** |
| 10 | Bloom Energy Corporation | `BE` | 116.4 | 36.1 | -69.0% | 62.7% | 56.4% | decelerating | **92** | **CORE** |

## P/E Expansion + Weakening — SHORT

| Rank | Company | OKX | Trail P/E | Fwd P/E | P/E change | EPS +1y | Rev +1y | Rev trend | SHORT score | Signal |
|---:|---|---|---:|---:|---:|---:|---:|---|---:|---|
| 1 | Hyperliquid Strategies Inc | `PURR` | 3.7 | 42.4 | 1051.2% | -79.8% | 22.8% | decelerating | **80** | **CORE** |
| 2 | Alphabet Inc. | `GOOGL` | 15.4 | 19.2 | 24.1% | -23.5% | 27.6% | accelerating | **50** | **WATCH** |

## Top SHORT candidates

| Rank | Company | OKX market | SHORT score | Signal | P/S | EV/S | Op margin | Fwd P/E | Rev +1y | FCF yield |
|---:|---|---|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Rocket Lab Corporation | `RKLB-USDT-SWAP` | **100** | **CORE** | 47.0 | 39.0 | -27.6% | 859.6 | 37.0% | -0.5% |
| 2 | Moderna, Inc. | `MRNA-USDT-SWAP` | **94** | **WATCH** | 35.8 | 35.4 | -80.8% | -51.7 | 8.8% | -0.6% |
| 3 | USA Rare Earth, Inc. | `USAR-USDT-SWAP` | **86** | **CORE** | 189.5 | 163.5 | -984.3% | -11.9 | 1031.4% | -8.3% |
| 4 | Okta, Inc. | `OKTA-USDT-SWAP` | **80** | **CORE** | 10.4 | 9.7 | 7.7% | 41.8 | 10.1% | 3.2% |
| 5 | AST SpaceMobile, Inc. | `ASTS-USDT-SWAP` | **80** | **WATCH** | 89.0 | 80.9 | -393.3% | -20.9 | 252.7% | -14.9% |
| 6 | IonQ, Inc. | `IONQ-USDT-SWAP` | **79** | **WATCH** | 35.3 | 30.5 | -306.3% | -20.3 | 71.2% | -0.9% |
| 7 | Cerebras Systems Inc. | `CBRS-USDT-SWAP` | **75** | **WATCH** | 35.0 | 27.1 | -99.3% | 61.1 | 216.5% | — |
| 8 | Circle Internet Group, Inc. | `CRCL-USDT-SWAP` | **63** | **CORE** | 5.3 | 4.7 | 11.3% | 43.7 | 24.1% | 1.6% |
| 9 | Hyperliquid Strategies Inc | `PURR-USDT-SWAP` | **25** | **WATCH** | 111.5 | 99.3 | 6252.0% | 42.4 | 22.8% | — |

## Top LONG candidates

| Rank | Company | OKX market | LONG score | Signal | P/S | EV/S | Op margin | Fwd P/E | Rev +1y | FCF yield |
|---:|---|---|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | QUALCOMM Incorporated | `QCOM-USDT-SWAP` | **100** | **CORE** | 4.3 | 4.5 | 20.8% | 14.1 | 15.5% | 4.9% |
| 2 | Taiwan Semiconductor Manufactur | `TSM-USDT-SWAP` | **90** | **CORE** | 0.4 | 2.7 | 58.0% | 17.1 | 37.8% | 58.2% |
| 3 | Sandisk Corporation | `SNDK-USDT-SWAP` | **90** | **CORE** | 4.3 | 4.2 | 72.7% | 3.1 | 23.7% | 8.9% |
| 4 | Applovin Corporation | `APP-USDT-SWAP` | **83** | **CORE** | 17.8 | 17.9 | 77.8% | 19.6 | 25.4% | 2.7% |
| 5 | Corning Incorporated | `GLW-USDT-SWAP` | **77** | **WATCH** | 5.5 | 6.0 | 16.8% | 25.1 | 21.2% | 0.9% |
| 6 | Robinhood Markets, Inc. | `HOOD-USDT-SWAP` | **77** | **WATCH** | 13.8 | 13.4 | 45.7% | 22.8 | 29.2% | — |
| 7 | Marvell Technology, Inc. | `MRVL-USDT-SWAP` | **77** | **WATCH** | 14.9 | 14.7 | 16.8% | 21.3 | 63.9% | 1.7% |
| 8 | Dell Technologies Inc. | `DELL-USDT-SWAP` | **75** | **CORE** | 1.4 | 1.6 | 9.9% | 11.3 | 20.3% | 2.8% |
| 9 | Applied Materials, Inc. | `AMAT-USDT-SWAP` | **75** | **WATCH** | 8.5 | 8.4 | 32.9% | 15.1 | 20.4% | 0.9% |
| 10 | Broadcom Inc. | `AVGO-USDT-SWAP` | **75** | **WATCH** | 18.6 | 19.0 | 48.8% | 17.9 | 65.1% | 1.8% |

## Analyst consensus (12-month price target) — most upside

| Rank | Company | OKX | Price | Analyst mean target | Gap | Analysts | Currency |
|---:|---|---|---:|---:|---:|---:|---|
| 1 | Hyperliquid Strategies Inc | `PURR` | 8.70 | 22.50 | **158.6%** | 4 | USD |
| 2 | SK hynix | `SKHYNIX` | 1216000.00 | 3097152.20 | **154.7%** | 39 | KRW |
| 3 | Sandisk Corporation | `SNDK` | 885.01 | 2047.38 | **131.3%** | 24 | USD |
| 4 | SamsungElec | `SAMSUNG` | 206000.00 | 475628.56 | **130.9%** | 35 | KRW |
| 5 | Nebius Group N.V. | `NBIS` | 115.88 | 257.20 | **122.0%** | 20 | USD |
| 6 | AXT Inc | `AXT` | 41.84 | 91.50 | **118.7%** | 6 | USD |
| 7 | Applied Optoelectronics, Inc. | `AAOI` | 49.89 | 109.00 | **118.5%** | 5 | USD |
| 8 | CoreWeave, Inc. | `CRWV` | 53.13 | 115.47 | **117.3%** | 38 | USD |
| 9 | Credo Technology Group Holding  | `CRDO` | 131.51 | 284.05 | **116.0%** | 19 | USD |
| 10 | Strategy Inc | `MSTR` | 111.62 | 233.27 | **109.0%** | 15 | USD |
| 11 | SOFTBANK GROUP CORP | `SOFTBANK` | 3547.00 | 7385.14 | **108.2%** | 18 | JPY |
| 12 | Cerebras Systems Inc. | `CBRS` | 108.72 | 225.64 | **107.5%** | 11 | USD |
| 13 | Western Digital Corporation | `WDC` | 295.65 | 613.38 | **107.5%** | 24 | USD |
| 14 | Micron Technology, Inc. | `MU` | 778.31 | 1561.91 | **100.7%** | 45 | USD |
| 15 | Marvell Technology, Inc. | `MRVL` | 156.76 | 310.32 | **98.0%** | 40 | USD |

## Analyst consensus (12-month price target) — most downside

| Rank | Company | OKX | Price | Analyst mean target | Gap | Analysts | Currency |
|---:|---|---|---:|---:|---:|---:|---|
| 1 | Moderna, Inc. | `MRNA` | 223.37 | 155.50 | **-30.4%** | 18 | USD |
| 2 | Apple Inc. | `AAPL` | 356.27 | 344.62 | **-3.3%** | 40 | USD |
| 3 | Coca-Cola Company (The) | `KO` | 99.25 | 98.43 | **-0.8%** | 23 | USD |

Price/target uses the underlying Yahoo Finance share quote, not the OKX derivative. Minimum 3 analysts; unreliable price scales and missing coverage excluded. Targets are analyst opinions, not guaranteed forecasts.

## All OKX companies — our ratio + LONG/SHORT scores

| Company | OKX | P/S | EV/S | Op margin | Fwd P/E | EPS +1y | Rev +1y | FCF yield | LONG | SHORT |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| QUALCOMM Incorporated | `QCOM` | 4.3 | 4.5 | 20.8% | 14.1 | 27.3% | 15.5% | 4.9% | **100 CORE** | **0** |
| Rocket Lab Corporation | `RKLB` | 47.0 | 39.0 | -27.6% | 859.6 | 75.3% | 37.0% | -0.5% | **0** | **100 CORE** |
| Moderna, Inc. | `MRNA` | 35.8 | 35.4 | -80.8% | -51.7 | 38.3% | 8.8% | -0.6% | **0** | **94 WATCH** |
| Sandisk Corporation | `SNDK` | 4.3 | 4.2 | 72.7% | 3.1 | 27.1% | 23.7% | 8.9% | **90 CORE** | **10** |
| Taiwan Semiconductor Manufactur | `TSM` | 0.4 | 2.7 | 58.0% | 17.1 | 33.6% | 37.8% | 58.2% | **90 CORE** | **10** |
| USA Rare Earth, Inc. | `USAR` | 189.5 | 163.5 | -984.3% | -11.9 | 45.1% | 1031.4% | -8.3% | **0** | **86 CORE** |
| Applovin Corporation | `APP` | 17.8 | 17.9 | 77.8% | 19.6 | 27.4% | 25.4% | 2.7% | **83 CORE** | **10** |
| Okta, Inc. | `OKTA` | 10.4 | 9.7 | 7.7% | 41.8 | 11.4% | 10.1% | 3.2% | **8** | **80 CORE** |
| AST SpaceMobile, Inc. | `ASTS` | 89.0 | 80.9 | -393.3% | -20.9 | 28.1% | 252.7% | -14.9% | **0** | **80 WATCH** |
| IonQ, Inc. | `IONQ` | 35.3 | 30.5 | -306.3% | -20.3 | -41.0% | 71.2% | -0.9% | **0** | **79 WATCH** |
| Tesla, Inc. | `TSLA` | 14.9 | 14.6 | 3.0% | 180.7 | 25.2% | 13.5% | 0.3% | **20** | **78** |
| Robinhood Markets, Inc. | `HOOD` | 13.8 | 13.4 | 45.7% | 22.8 | 39.7% | 29.2% | — | **77 WATCH** | **0** |
| Marvell Technology, Inc. | `MRVL` | 14.9 | 14.7 | 16.8% | 21.3 | 74.2% | 63.9% | 1.7% | **77 WATCH** | **13** |
| Corning Incorporated | `GLW` | 5.5 | 6.0 | 16.8% | 25.1 | 34.6% | 21.2% | 0.9% | **77 WATCH** | **13** |
| NVIDIA Corporation | `NVDA` | 13.0 | 12.9 | 65.2% | 10.3 | 70.0% | 67.2% | 1.1% | **75 WATCH** | **18** |
| AXT Inc | `AXT` | 16.1 | 13.7 | 19.6% | 16.4 | 116.3% | 115.9% | 0.7% | **75 WATCH** | **28** |
| Credo Technology Group Holding  | `CRDO` | 15.5 | 15.1 | 31.7% | 13.5 | 53.9% | 55.0% | 1.0% | **75 WATCH** | **28** |
| Broadcom Inc. | `AVGO` | 18.6 | 19.0 | 48.8% | 17.9 | 66.4% | 65.1% | 1.8% | **75 WATCH** | **28** |
| Micron Technology, Inc. | `MU` | 6.6 | 6.3 | 74.6% | 3.7 | 17.7% | 16.0% | 3.3% | **75 CORE** | **30** |
| Dell Technologies Inc. | `DELL` | 1.4 | 1.6 | 9.9% | 11.3 | 17.9% | 20.3% | 2.8% | **75 CORE** | **30** |
| Western Digital Corporation | `WDC` | 7.6 | 7.6 | 40.9% | 7.3 | 63.4% | 40.5% | 2.5% | **75 WATCH** | **18** |
| Applied Materials, Inc. | `AMAT` | 8.5 | 8.4 | 32.9% | 15.1 | 28.8% | 20.4% | 0.9% | **75 WATCH** | **18** |
| Cerebras Systems Inc. | `CBRS` | 35.0 | 27.1 | -99.3% | 61.1 | 345.0% | 216.5% | — | **0** | **75 WATCH** |
| Oracle Corporation | `ORCL` | 5.4 | 7.2 | 34.3% | 11.3 | 35.7% | 45.7% | -11.7% | **70 WATCH** | **10** |
| Advanced Micro Devices, Inc. | `AMD` | 19.3 | 19.1 | 17.8% | 30.2 | 118.8% | 83.6% | 0.8% | **70 WATCH** | **13** |
| XIAOMI-W | `XIAOMI` | 1.7 | 1.5 | 4.7% | 19.6 | 39.5% | 19.2% | -1.2% | **70 WATCH** | **10** |
| Adobe Inc. | `ADBE` | 3.6 | 3.7 | 36.3% | 8.9 | 12.0% | 9.1% | 9.9% | **65 WATCH** | **30** |
| Circle Internet Group, Inc. | `CRCL` | 5.3 | 4.7 | 11.3% | 43.7 | 0.5% | 24.1% | 1.6% | **15** | **63 CORE** |
| Coherent Corp. | `COHR` | 5.4 | 5.8 | 14.1% | 13.8 | 51.7% | 39.9% | -3.9% | **60 WATCH** | **35** |
| Nebius Group N.V. | `NBIS` | 15.5 | 19.4 | -23.0% | -40.2 | -3529.4% | 283.7% | -59.8% | **0** | **60** |
| Microsoft Corporation | `MSFT` | 11.2 | 11.4 | 47.1% | 21.7 | 20.9% | 20.5% | 0.1% | **59 WATCH** | **3** |
| IREN LIMITED | `IREN` | 11.1 | 20.7 | -72.9% | 67.3 | 116.3% | 199.7% | — | **0** | **59** |
| Apple Inc. | `AAPL` | 10.8 | 10.9 | 33.0% | 33.7 | 12.3% | 8.1% | 2.0% | **5** | **58** |
| Coca-Cola Company (The) | `KO` | 8.4 | 8.9 | 32.2% | 28.1 | 5.7% | -3.1% | 1.0% | **0** | **58** |
| Meta Platforms, Inc. | `META` | 6.8 | 6.9 | 37.8% | 18.0 | 16.7% | 21.7% | 1.0% | **57 WATCH** | **38** |
| Netflix, Inc. | `NFLX` | 5.1 | 5.3 | 31.3% | 16.5 | 5.1% | 10.7% | 10.0% | **35** | **50** |
| Palantir Technologies Inc. | `PLTR` | 55.5 | 54.1 | 45.6% | 66.2 | 49.2% | 53.5% | 0.7% | **45** | **48** |
| Bloom Energy Corporation | `BE` | 14.8 | 14.9 | 14.3% | 36.1 | 62.7% | 56.4% | -0.0% | **45** | **35** |
| SamsungElec | `SAMSUNG` | 2.3 | 1.9 | 46.1% | 2.7 | 62.3% | 40.9% | 6.2% | **45** | **10** |
| Super Micro Computer, Inc. | `SMCI` | 0.3 | 0.4 | 8.3% | 3.9 | 6.5% | 11.3% | -46.3% | **35** | **45** |
| Arm Holdings plc | `ARM` | 37.3 | 36.7 | 17.0% | 62.0 | 35.6% | 37.3% | 0.6% | **43** | **33** |
| CoreWeave, Inc. | `CRWV` | 3.0 | 9.3 | -0.5% | -30.5 | 23.1% | 107.7% | -66.5% | **0** | **40** |
| SOFTBANK GROUP CORP | `SOFTBANK` | 2.4 | 6.0 | -6.3% | 12.0 | 345.5% | 6.7% | -5.1% | **0** | **40** |
| Coinbase Global, Inc. | `COIN` | 6.2 | 5.9 | 0.1% | 52.0 | 825.3% | 26.2% | 10.9% | **35** | **25** |
| SK hynix | `SKHYNIX` | 3.2 | 2.9 | 74.5% | 2.3 | 48.7% | 60.4% | — | **30** | **5** |
| Lumentum Holdings Inc. | `LITE` | 14.5 | 14.3 | 23.4% | 14.9 | 60.9% | 57.9% | 0.3% | **30** | **23** |
| SK hynix | `SKHY` | 3.2 | 2.9 | 74.5% | 2.3 | 48.7% | 60.4% | — | **30** | **5** |
| Alphabet Inc. | `GOOGL` | 7.7 | 7.5 | 33.3% | 19.2 | -23.5% | 27.6% | -0.0% | **5** | **30** |
| Amazon.com, Inc. | `AMZN` | 3.6 | 3.9 | 13.1% | 24.4 | -16.6% | 15.7% | -1.2% | **0** | **30** |
| Intel Corporation | `INTC` | 5.3 | 5.5 | 10.3% | 33.3 | 20.4% | 12.0% | 0.3% | **5** | **28** |
| Fluence Energy, Inc. | `FLNC` | 0.3 | 0.3 | -4.2% | -8.8 | 59.3% | 25.4% | 0.3% | **5** | **28** |
| BitMine Immersion Technologies, | `BMNR` | 88.2 | 86.1 | -216.3% | 18.7 | 105.8% | 58.9% | -0.9% | **25** | **25** |
| Strategy Inc | `MSTR` | 95.4 | 123.4 | -1100.1% | 6.5 | 417.1% | 3.1% | -6.9% | **25** | **25** |
| Applied Optoelectronics, Inc. | `AAOI` | 6.1 | 5.7 | -6.8% | 13.3 | 439.3% | 135.1% | -28.9% | **10** | **25** |
| Hyperliquid Strategies Inc | `PURR` | 111.5 | 99.3 | 6252.0% | 42.4 | -79.8% | 22.8% | — | **0** | **25 WATCH** |

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
