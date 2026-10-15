# OKX Long / Short Fundamental Scanner

Hourly scanner restricted to public companies exposed by the **OKX EEA TradFi / Stock Perpetual API universe**.

**Last scan:** 2026-10-15 01:32 UTC  
**Availability scope:** user-confirmed OKX EEA Stock Futures / X-Perp  
**OKX stock/ETF markets in configured universe:** 72  
**Public companies analysed:** 55  
**SHORT CORE:** 5  
**LONG CORE:** 4

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
| 1 | Taiwan Semiconductor Manufactur | TSM | -3.4% | -8.9% | -6.2% | 88 | +5 | **93** | **CORE** | yes |
| 2 | Credo Technology Group Holding  | CRDO | -9.6% | -18.5% | -14.1% | 82 | +11 | **93** | **CORE** | yes |
| 3 | Applied Materials, Inc. | AMAT | -3.8% | -14.2% | -9.0% | 81 | +7 | **88** | **CORE** | yes |
| 4 | Marvell Technology, Inc. | MRVL | -8.7% | -13.8% | -11.3% | 79 | +9 | **88** | **CORE** | yes |
| 5 | Broadcom Inc. | AVGO | -3.1% | -8.0% | -5.6% | 82 | +4 | **86** | **CORE** | yes |
| 6 | Applovin Corporation | APP | -3.7% | -6.8% | -5.2% | 82 | +4 | **86** | **CORE** | yes |
| 7 | NVIDIA Corporation | NVDA | -3.2% | -6.8% | -5.0% | 82 | +4 | **86** | **CORE** | yes |
| 8 | Robinhood Markets, Inc. | HOOD | -8.5% | -7.7% | -8.1% | 80 | +6 | **86** | **CORE** | yes |
| 9 | Advanced Micro Devices, Inc. | AMD | -5.7% | -11.6% | -8.7% | 79 | +7 | **86** | **CORE** | yes |
| 10 | Corning Incorporated | GLW | -5.2% | -13.7% | -9.4% | 78 | +8 | **86** | **CORE** | yes |

## Final model + Price Timing — SHORT

| Rank | Company | OKX | 24h | 7d | 50/50 move | Base SHORT | Timing adj. | Final | Signal | Prev. SHORT? |
|---:|---|---|---:|---:|---:|---:|---:|---:|---|---|
| 1 | Rocket Lab Corporation | RKLB | -7.8% | -17.7% | -12.8% | 100 | -10 | **90** | **CORE** | yes |
| 2 | USA Rare Earth, Inc. | USAR | -8.5% | -22.0% | -15.3% | 100 | -12 | **88** | **CORE** | yes |
| 3 | Moderna, Inc. | MRNA | 4.6% | 15.2% | 9.9% | 80 | +8 | **88** | **CORE** | yes |
| 4 | Cerebras Systems Inc. | CBRS | -5.1% | -19.2% | -12.1% | 92 | -10 | **82** | **CORE** | yes |
| 5 | IonQ, Inc. | IONQ | -9.5% | -24.0% | -16.8% | 88 | -13 | **75** | **CORE** | yes |
| 6 | Nebius Group N.V. | NBIS | -10.1% | -21.6% | -15.8% | 84 | -13 | **71** | **WATCH** | yes |
| 7 | AST SpaceMobile, Inc. | ASTS | -10.5% | -30.5% | -20.5% | 80 | -16 | **64** | **WATCH** | yes |
| 8 | Okta, Inc. | OKTA | -6.5% | -2.8% | -4.6% | 60 | -4 | **56** | **WATCH** | yes |

## Combined model — LONG

Weighted score: **70% fundamental + 30% P/E trend**.

| Rank | Company | OKX | Fundamental LONG | P/E trend LONG | Combined | Signal |
|---:|---|---|---:|---:|---:|---|
| 1 | Taiwan Semiconductor Manufactur | `TSM` | 90 | 85 | **88** | **CORE** |
| 2 | Applovin Corporation | `APP` | 83 | 80 | **82** | **CORE** |
| 3 | Credo Technology Group Holding  | `CRDO` | 75 | 100 | **82** | **CORE** |
| 4 | NVIDIA Corporation | `NVDA` | 75 | 100 | **82** | **CORE** |
| 5 | Broadcom Inc. | `AVGO` | 75 | 100 | **82** | **CORE** |
| 6 | Applied Materials, Inc. | `AMAT` | 77 | 91 | **81** | **CORE** |
| 7 | Robinhood Markets, Inc. | `HOOD` | 77 | 86 | **80** | **CORE** |
| 8 | Marvell Technology, Inc. | `MRVL` | 70 | 100 | **79** | **CORE** |
| 9 | Advanced Micro Devices, Inc. | `AMD` | 70 | 100 | **79** | **CORE** |
| 10 | Corning Incorporated | `GLW` | 70 | 96 | **78** | **CORE** |

## Combined model — SHORT

Weighted score: **70% fundamental + 30% P/E trend**.

| Rank | Company | OKX | Fundamental SHORT | P/E trend SHORT | Combined | Signal |
|---:|---|---|---:|---:|---:|---|
| 1 | Rocket Lab Corporation | `RKLB` | 100 | 0 | **100** | **CORE** |
| 2 | USA Rare Earth, Inc. | `USAR` | 100 | 0 | **100** | **CORE** |
| 3 | Cerebras Systems Inc. | `CBRS` | 92 | 0 | **92** | **CORE** |
| 4 | IonQ, Inc. | `IONQ` | 88 | 0 | **88** | **CORE** |
| 5 | Nebius Group N.V. | `NBIS` | 84 | 0 | **84** | **WATCH** |
| 6 | Moderna, Inc. | `MRNA` | 80 | 0 | **80** | **WATCH** |
| 7 | AST SpaceMobile, Inc. | `ASTS` | 80 | 0 | **80** | **WATCH** |
| 8 | Okta, Inc. | `OKTA` | 80 | 13 | **60** | **WATCH** |

## P/E Compression + Growth — LONG

| Rank | Company | OKX | Trail P/E | Fwd P/E | P/E change | EPS +1y | Rev +1y | Rev trend | LONG score | Signal |
|---:|---|---|---:|---:|---:|---:|---:|---|---:|---|
| 1 | Credo Technology Group Holding  | `CRDO` | 63.6 | 18.5 | -70.9% | 53.7% | 54.8% | decelerating | **100** | **CORE** |
| 2 | Marvell Technology, Inc. | `MRVL` | 80.7 | 33.6 | -58.3% | 72.9% | 63.2% | accelerating | **100** | **CORE** |
| 3 | NVIDIA Corporation | `NVDA` | 28.0 | 13.9 | -50.3% | 70.9% | 68.2% | decelerating | **100** | **CORE** |
| 4 | Advanced Micro Devices, Inc. | `AMD` | 145.6 | 36.3 | -75.1% | 107.2% | 74.6% | accelerating | **100** | **CORE** |
| 5 | Broadcom Inc. | `AVGO` | 43.4 | 17.9 | -58.9% | 66.4% | 64.1% | decelerating | **100** | **CORE** |
| 6 | Corning Incorporated | `GLW` | 64.6 | 32.2 | -50.1% | 33.0% | 19.6% | accelerating | **96** | **CORE** |
| 7 | AXT Inc | `AXT` | 1539.8 | 27.4 | -98.2% | 159.2% | 111.3% | decelerating | **96** | **CORE** |
| 8 | Oracle Corporation | `ORCL` | 20.5 | 11.9 | -42.0% | 35.1% | 45.7% | accelerating | **95** | **CORE** |
| 9 | Coherent Corp. | `COHR` | 63.9 | 18.7 | -70.7% | 49.2% | 38.9% | decelerating | **95** | **CORE** |
| 10 | Arm Holdings plc | `ARM` | 245.4 | 77.7 | -68.3% | 37.5% | 36.2% | accelerating | **95** | **CORE** |

## P/E Expansion + Weakening — SHORT

| Rank | Company | OKX | Trail P/E | Fwd P/E | P/E change | EPS +1y | Rev +1y | Rev trend | SHORT score | Signal |
|---:|---|---|---:|---:|---:|---:|---:|---|---:|---|
| 1 | SOFTBANK GROUP CORP | `SOFTBANK` | 5.6 | 16.4 | 193.2% | -14.5% | 6.9% | decelerating | **86** | **CORE** |
| 2 | Alphabet Inc. | `GOOGL` | 17.4 | 22.8 | 30.7% | -26.9% | 24.1% | accelerating | **60** | **WATCH** |
| 3 | Hyperliquid Strategies Inc | `PURR` | 3.0 | 25.6 | 767.6% | 51.0% | 31.4% | decelerating | **55** | **WATCH** |
| 4 | Amazon.com, Inc. | `AMZN` | 20.4 | 24.3 | 18.9% | -18.3% | 14.5% | decelerating | **52** | **WATCH** |

## Top SHORT candidates

| Rank | Company | OKX market | SHORT score | Signal | P/S | EV/S | Op margin | Fwd P/E | Rev +1y | FCF yield |
|---:|---|---|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Rocket Lab Corporation | `RKLB-USDT-SWAP` | **100** | **CORE** | 49.2 | 43.2 | -24.6% | 910.6 | 41.3% | -0.7% |
| 2 | USA Rare Earth, Inc. | `USAR-USDT-SWAP` | **100** | **CORE** | 294.1 | 76.6 | -795.6% | 344.0 | 870.1% | -7.3% |
| 3 | Cerebras Systems Inc. | `CBRS-USDT-SWAP` | **92** | **CORE** | 49.4 | 39.9 | -265.0% | 111.1 | 232.7% | — |
| 4 | IonQ, Inc. | `IONQ-USDT-SWAP` | **88** | **CORE** | 51.6 | 40.2 | -408.2% | -24.3 | 79.0% | -0.7% |
| 5 | Nebius Group N.V. | `NBIS-USDT-SWAP` | **84** | **WATCH** | 37.3 | 39.2 | -0.2% | -52.3 | 268.0% | -19.0% |
| 6 | Okta, Inc. | `OKTA-USDT-SWAP` | **80** | **CORE** | 12.1 | 11.3 | 13.3% | 48.4 | 10.0% | 2.8% |
| 7 | AST SpaceMobile, Inc. | `ASTS-USDT-SWAP` | **80** | **WATCH** | 142.2 | 120.1 | -544.6% | -32.8 | 247.3% | -11.0% |
| 8 | Moderna, Inc. | `MRNA-USDT-SWAP` | **80** | **WATCH** | 40.6 | 38.8 | -557.9% | -51.0 | 16.1% | 0.3% |
| 9 | Tesla, Inc. | `TSLA-USDT-SWAP` | **63** | **WATCH** | 14.0 | 13.7 | 1.4% | 168.4 | 13.6% | 0.3% |

## Top LONG candidates

| Rank | Company | OKX market | LONG score | Signal | P/S | EV/S | Op margin | Fwd P/E | Rev +1y | FCF yield |
|---:|---|---|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Taiwan Semiconductor Manufactur | `TSM-USDT-SWAP` | **90** | **CORE** | 0.5 | 3.5 | 60.3% | 19.3 | 35.9% | 32.8% |
| 2 | Applovin Corporation | `APP-USDT-SWAP` | **83** | **CORE** | 12.9 | 12.9 | 77.7% | 12.8 | 26.0% | 3.6% |
| 3 | Robinhood Markets, Inc. | `HOOD-USDT-SWAP` | **77** | **WATCH** | 18.4 | 18.2 | 43.9% | 29.5 | 29.2% | — |
| 4 | Applied Materials, Inc. | `AMAT-USDT-SWAP` | **77** | **WATCH** | 11.5 | 11.4 | 33.7% | 24.2 | 35.2% | 0.9% |
| 5 | Credo Technology Group Holding  | `CRDO-USDT-SWAP` | **75** | **WATCH** | 21.2 | 20.7 | 25.2% | 18.5 | 54.8% | 0.7% |
| 6 | Broadcom Inc. | `AVGO-USDT-SWAP` | **75** | **WATCH** | 18.5 | 18.9 | 54.3% | 17.9 | 64.1% | 1.9% |
| 7 | Micron Technology, Inc. | `MU-USDT-SWAP` | **75** | **CORE** | 7.8 | 7.5 | 80.7% | 4.4 | 15.7% | 2.8% |
| 8 | Sandisk Corporation | `SNDK-USDT-SWAP` | **75** | **CORE** | 10.0 | 9.9 | 78.5% | 5.3 | 18.9% | 3.8% |
| 9 | NVIDIA Corporation | `NVDA-USDT-SWAP` | **75** | **WATCH** | 17.6 | 17.5 | 66.2% | 13.9 | 68.2% | 0.8% |
| 10 | Western Digital Corporation | `WDC-USDT-SWAP` | **75** | **WATCH** | 10.5 | 10.1 | 43.6% | 11.0 | 37.2% | 1.7% |

## Analyst consensus (12-month price target) — most upside

| Rank | Company | OKX | Price | Analyst mean target | Gap | Analysts | Currency |
|---:|---|---|---:|---:|---:|---:|---|
| 1 | IREN LIMITED | `IREN` | 30.56 | 78.14 | **155.7%** | 18 | USD |
| 2 | SK hynix | `SKHYNIX` | 1261000.00 | 3141024.80 | **149.1%** | 38 | KRW |
| 3 | Hyperliquid Strategies Inc | `PURR` | 9.47 | 22.32 | **135.7%** | 4 | USD |
| 4 | SamsungElec | `SAMSUNG` | 212500.00 | 478905.62 | **125.4%** | 36 | KRW |
| 5 | CoreWeave, Inc. | `CRWV` | 65.78 | 141.47 | **115.1%** | 38 | USD |
| 6 | IonQ, Inc. | `IONQ` | 31.42 | 66.63 | **112.1%** | 14 | USD |
| 7 | BitMine Immersion Technologies, | `BMNR` | 22.25 | 45.87 | **106.1%** | 3 | USD |
| 8 | Cerebras Systems Inc. | `CBRS` | 141.48 | 291.64 | **106.1%** | 11 | USD |
| 9 | Applied Optoelectronics, Inc. | `AAOI` | 86.22 | 163.40 | **89.5%** | 5 | USD |
| 10 | Western Digital Corporation | `WDC` | 364.10 | 668.50 | **83.6%** | 24 | USD |
| 11 | Applovin Corporation | `APP` | 262.19 | 480.08 | **83.1%** | 31 | USD |
| 12 | Oracle Corporation | `ORCL` | 130.55 | 237.97 | **82.3%** | 41 | USD |
| 13 | Rocket Lab Corporation | `RKLB` | 59.18 | 105.05 | **77.5%** | 19 | USD |
| 14 | AST SpaceMobile, Inc. | `ASTS` | 42.14 | 74.28 | **76.3%** | 12 | USD |
| 15 | Micron Technology, Inc. | `MU` | 914.13 | 1560.57 | **70.7%** | 46 | USD |

## Analyst consensus (12-month price target) — most downside

| Rank | Company | OKX | Price | Analyst mean target | Gap | Analysts | Currency |
|---:|---|---|---:|---:|---:|---:|---|
| 1 | Moderna, Inc. | `MRNA` | 226.30 | 122.67 | **-45.8%** | 18 | USD |
| 2 | Apple Inc. | `AAPL` | 342.96 | 329.38 | **-4.0%** | 39 | USD |

Price/target uses the underlying Yahoo Finance share quote, not the OKX derivative. Minimum 3 analysts; unreliable price scales and missing coverage excluded. Targets are analyst opinions, not guaranteed forecasts.

## All OKX companies — our ratio + LONG/SHORT scores

| Company | OKX | P/S | EV/S | Op margin | Fwd P/E | EPS +1y | Rev +1y | FCF yield | LONG | SHORT |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Rocket Lab Corporation | `RKLB` | 49.2 | 43.2 | -24.6% | 910.6 | 75.5% | 41.3% | -0.7% | **0** | **100 CORE** |
| USA Rare Earth, Inc. | `USAR` | 294.1 | 76.6 | -795.6% | 344.0 | 105.3% | 870.1% | -7.3% | **0** | **100 CORE** |
| Cerebras Systems Inc. | `CBRS` | 49.4 | 39.9 | -265.0% | 111.1 | 371.3% | 232.7% | — | **0** | **92 CORE** |
| Taiwan Semiconductor Manufactur | `TSM` | 0.5 | 3.5 | 60.3% | 19.3 | 30.9% | 35.9% | 32.8% | **90 CORE** | **10** |
| IonQ, Inc. | `IONQ` | 51.6 | 40.2 | -408.2% | -24.3 | 18.1% | 79.0% | -0.7% | **0** | **88 CORE** |
| Nebius Group N.V. | `NBIS` | 37.3 | 39.2 | -0.2% | -52.3 | -191.4% | 268.0% | -19.0% | **0** | **84 WATCH** |
| Applovin Corporation | `APP` | 12.9 | 12.9 | 77.7% | 12.8 | 27.3% | 26.0% | 3.6% | **83 CORE** | **10** |
| Okta, Inc. | `OKTA` | 12.1 | 11.3 | 13.3% | 48.4 | 11.4% | 10.0% | 2.8% | **8** | **80 CORE** |
| Moderna, Inc. | `MRNA` | 40.6 | 38.8 | -557.9% | -51.0 | 43.0% | 16.1% | 0.3% | **0** | **80 WATCH** |
| AST SpaceMobile, Inc. | `ASTS` | 142.2 | 120.1 | -544.6% | -32.8 | 44.3% | 247.3% | -11.0% | **0** | **80 WATCH** |
| Applied Materials, Inc. | `AMAT` | 11.5 | 11.4 | 33.7% | 24.2 | 44.4% | 35.2% | 0.9% | **77 WATCH** | **3** |
| Robinhood Markets, Inc. | `HOOD` | 18.4 | 18.2 | 43.9% | 29.5 | 36.5% | 29.2% | — | **77 WATCH** | **5** |
| Credo Technology Group Holding  | `CRDO` | 21.2 | 20.7 | 25.2% | 18.5 | 53.7% | 54.8% | 0.7% | **75 WATCH** | **28** |
| Sandisk Corporation | `SNDK` | 10.0 | 9.9 | 78.5% | 5.3 | 24.0% | 18.9% | 3.8% | **75 CORE** | **10** |
| NVIDIA Corporation | `NVDA` | 17.6 | 17.5 | 66.2% | 13.9 | 70.9% | 68.2% | 0.8% | **75 WATCH** | **18** |
| Broadcom Inc. | `AVGO` | 18.5 | 18.9 | 54.3% | 17.9 | 66.4% | 64.1% | 1.9% | **75 WATCH** | **28** |
| Micron Technology, Inc. | `MU` | 7.8 | 7.5 | 80.7% | 4.4 | 17.1% | 15.7% | 2.8% | **75 CORE** | **30** |
| Western Digital Corporation | `WDC` | 10.5 | 10.1 | 43.6% | 11.0 | 61.2% | 37.2% | 1.7% | **75 WATCH** | **18** |
| Marvell Technology, Inc. | `MRVL` | 23.3 | 22.9 | 16.7% | 33.6 | 72.9% | 63.2% | 1.1% | **70 WATCH** | **13** |
| Advanced Micro Devices, Inc. | `AMD` | 22.6 | 22.3 | 17.2% | 36.3 | 107.2% | 74.6% | 0.9% | **70 WATCH** | **13** |
| Corning Incorporated | `GLW` | 7.2 | 7.6 | 15.6% | 32.2 | 33.0% | 19.6% | 0.6% | **70 WATCH** | **13** |
| Oracle Corporation | `ORCL` | 5.5 | 7.4 | 35.6% | 11.9 | 35.1% | 45.7% | -11.6% | **70 WATCH** | **10** |
| XIAOMI-W | `XIAOMI` | 1.5 | 1.4 | 4.0% | 17.0 | 38.8% | 22.3% | -1.3% | **70 WATCH** | **10** |
| Adobe Inc. | `ADBE` | 3.6 | 3.7 | 34.8% | 8.7 | 12.4% | 9.1% | 10.0% | **65 WATCH** | **30** |
| Tesla, Inc. | `TSLA` | 14.0 | 13.7 | 1.4% | 168.4 | 24.5% | 13.6% | 0.3% | **22** | **63 WATCH** |
| Coherent Corp. | `COHR` | 7.3 | 7.5 | 11.8% | 18.7 | 49.2% | 38.9% | -1.3% | **60 WATCH** | **35** |
| IREN LIMITED | `IREN` | 17.0 | 19.8 | -102.5% | -7.7 | -16.4% | 160.9% | -35.0% | **0** | **60** |
| Microsoft Corporation | `MSFT` | 11.9 | 12.1 | 45.1% | 22.5 | 19.8% | 19.6% | 0.4% | **59 WATCH** | **23** |
| Lumentum Holdings Inc. | `LITE` | 26.9 | 26.3 | 28.0% | 24.9 | 65.3% | 57.0% | 0.3% | **0** | **59** |
| Coca-Cola Company (The) | `KO` | 7.9 | 8.5 | 34.9% | 26.0 | 6.7% | 0.1% | 1.3% | **7** | **58** |
| Apple Inc. | `AAPL` | 10.7 | 10.8 | 32.6% | 35.8 | 8.6% | 10.5% | 2.2% | **5** | **58** |
| Bloom Energy Corporation | `BE` | 22.6 | 22.7 | 17.1% | 49.1 | 78.9% | 64.4% | 0.8% | **55 WATCH** | **48** |
| AXT Inc | `AXT` | 32.2 | 29.5 | 21.9% | 27.4 | 159.2% | 111.3% | -1.1% | **52** | **35** |
| Super Micro Computer, Inc. | `SMCI` | 0.6 | 0.8 | 13.4% | 6.7 | 22.8% | 17.3% | -35.1% | **52** | **25** |
| Netflix, Inc. | `NFLX` | 6.1 | 6.2 | 33.4% | 18.6 | 5.9% | 11.2% | 8.6% | **35** | **50** |
| Palantir Technologies Inc. | `PLTR` | 78.5 | 77.0 | 47.1% | 85.5 | 45.2% | 50.1% | 0.4% | **33** | **48** |
| Intel Corporation | `INTC` | 9.1 | 9.3 | 12.2% | 46.9 | 37.2% | 14.9% | 0.9% | **5** | **48** |
| SK hynix | `SKHYNIX` | 4.7 | 5.0 | 76.3% | 2.7 | 32.4% | 54.4% | 6.2% | **45** | **5** |
| SK hynix | `SKHY` | 4.7 | 5.0 | 76.3% | 2.7 | 32.4% | 54.4% | 6.2% | **45** | **5** |
| SamsungElec | `SAMSUNG` | 2.9 | 2.8 | 52.2% | 2.9 | 50.9% | 38.0% | 5.0% | **45** | **10** |
| Circle Internet Group, Inc. | `CRCL` | 7.0 | 6.4 | 4.9% | 54.2 | 31.7% | 25.8% | 1.0% | **43** | **33** |
| Coinbase Global, Inc. | `COIN` | 7.5 | 7.2 | -13.9% | 57.4 | 261.1% | 29.8% | 5.8% | **20** | **40** |
| SOFTBANK GROUP CORP | `SOFTBANK` | 3.5 | 7.2 | -11.6% | 16.4 | -14.5% | 6.9% | -7.9% | **0** | **40** |
| CoreWeave, Inc. | `CRWV` | 4.8 | 10.9 | -1.9% | -35.9 | 15.4% | 104.3% | -25.1% | **0** | **40** |
| Dell Technologies Inc. | `DELL` | 2.1 | 2.3 | 12.0% | 17.0 | 9.6% | 18.4% | 1.9% | **33** | **38** |
| Meta Platforms, Inc. | `META` | 8.2 | 8.3 | 34.8% | 21.3 | 10.4% | 20.7% | 1.1% | **17** | **38** |
| Amazon.com, Inc. | `AMZN` | 3.5 | 3.7 | 13.7% | 24.3 | -18.3% | 14.5% | 0.1% | **0** | **38** |
| Arm Holdings plc | `ARM` | 49.3 | 48.6 | 7.6% | 77.7 | 37.5% | 36.2% | 0.5% | **35** | **33** |
| Fluence Energy, Inc. | `FLNC` | 0.5 | 0.4 | -8.9% | -17.9 | 66.2% | 29.9% | 0.2% | **5** | **28** |
| Hyperliquid Strategies Inc | `PURR` | 278.6 | 183.5 | 9595.1% | 25.6 | 51.0% | 31.4% | — | **25** | **10** |
| Strategy Inc | `MSTR` | 121.7 | 148.1 | -6808.1% | 2.9 | 157.6% | 2.2% | -37.2% | **25** | **25** |
| BitMine Immersion Technologies, | `BMNR` | 219.3 | 213.8 | 8.4% | 23.7 | 103.2% | 421.8% | -3.9% | **25** | **25** |
| QUALCOMM Incorporated | `QCOM` | 4.2 | 4.3 | 18.5% | 16.9 | -2.7% | 4.8% | 5.6% | **25** | **15** |
| Applied Optoelectronics, Inc. | `AAOI` | 12.3 | 11.9 | -12.9% | 18.7 | 576.8% | 156.5% | -12.1% | **10** | **25** |
| Alphabet Inc. | `GOOGL` | 9.5 | 9.3 | 34.0% | 22.8 | -26.9% | 24.1% | 0.5% | **12** | **23** |

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
