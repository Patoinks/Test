# OKX Long / Short Fundamental Scanner

Hourly scanner restricted to public companies exposed by the **OKX EEA TradFi / Stock Perpetual API universe**.

**Last scan:** 2026-10-22 13:52 UTC  
**Availability scope:** user-confirmed OKX EEA Stock Futures / X-Perp  
**OKX stock/ETF markets in configured universe:** 72  
**Public companies analysed:** 55  
**SHORT CORE:** 4  
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
| 1 | Taiwan Semiconductor Manufactur | TSM | -3.4% | -1.2% | -2.3% | 88 | +2 | **90** | **CORE** | yes |
| 2 | Corning Incorporated | GLW | -5.9% | -8.3% | -7.1% | 83 | +6 | **89** | **CORE** | yes |
| 3 | Applied Materials, Inc. | AMAT | -5.7% | -10.3% | -8.0% | 81 | +6 | **87** | **CORE** | yes |
| 4 | Credo Technology Group Holding  | CRDO | -6.3% | -4.3% | -5.3% | 82 | +4 | **86** | **CORE** | yes |
| 5 | Sandisk Corporation | SNDK | -3.7% | -4.9% | -4.3% | 82 | +3 | **85** | **CORE** | yes |
| 6 | Broadcom Inc. | AVGO | -2.7% | -4.6% | -3.7% | 82 | +3 | **85** | **CORE** | yes |
| 7 | Applovin Corporation | APP | -0.7% | -4.8% | -2.8% | 82 | +2 | **84** | **CORE** | yes |
| 8 | Advanced Micro Devices, Inc. | AMD | -5.4% | -7.0% | -6.2% | 79 | +5 | **84** | **CORE** | yes |
| 9 | NVIDIA Corporation | NVDA | -2.7% | -0.6% | -1.7% | 82 | +1 | **83** | **CORE** | yes |
| 10 | Marvell Technology, Inc. | MRVL | -5.1% | -3.8% | -4.4% | 79 | +4 | **83** | **CORE** | yes |

## Final model + Price Timing — SHORT

| Rank | Company | OKX | 24h | 7d | 50/50 move | Base SHORT | Timing adj. | Final | Signal | Prev. SHORT? |
|---:|---|---|---:|---:|---:|---:|---:|---:|---|---|
| 1 | Rocket Lab Corporation | RKLB | -3.9% | -6.7% | -5.3% | 100 | -4 | **96** | **CORE** | yes |
| 2 | USA Rare Earth, Inc. | USAR | -4.0% | -11.5% | -7.7% | 100 | -6 | **94** | **CORE** | yes |
| 3 | IonQ, Inc. | IONQ | -2.4% | -8.3% | -5.4% | 88 | -4 | **84** | **CORE** | yes |
| 4 | Moderna, Inc. | MRNA | -3.3% | 0.5% | -1.4% | 80 | -1 | **79** | **CORE** | yes |
| 5 | Nebius Group N.V. | NBIS | -7.2% | -15.5% | -11.3% | 84 | -9 | **75** | **CORE** | yes |
| 6 | AST SpaceMobile, Inc. | ASTS | -4.4% | -12.0% | -8.2% | 80 | -7 | **73** | **WATCH** | yes |
| 7 | Cerebras Systems Inc. | CBRS | -6.8% | -22.6% | -14.7% | 79 | -12 | **67** | **WATCH** | yes |
| 8 | Tesla, Inc. | TSLA | -0.6% | 6.0% | 2.7% | 59 | +2 | **61** | **WATCH** | no |
| 9 | Okta, Inc. | OKTA | -1.0% | -1.0% | -1.0% | 60 | -1 | **59** | **WATCH** | yes |

## Combined model — LONG

Weighted score: **70% fundamental + 30% P/E trend**.

| Rank | Company | OKX | Fundamental LONG | P/E trend LONG | Combined | Signal |
|---:|---|---|---:|---:|---:|---|
| 1 | Taiwan Semiconductor Manufactur | `TSM` | 90 | 85 | **88** | **CORE** |
| 2 | Corning Incorporated | `GLW` | 77 | 96 | **83** | **CORE** |
| 3 | Applovin Corporation | `APP` | 83 | 80 | **82** | **CORE** |
| 4 | Sandisk Corporation | `SNDK` | 82 | 82 | **82** | **CORE** |
| 5 | Credo Technology Group Holding  | `CRDO` | 75 | 100 | **82** | **CORE** |
| 6 | Broadcom Inc. | `AVGO` | 75 | 100 | **82** | **CORE** |
| 7 | NVIDIA Corporation | `NVDA` | 75 | 100 | **82** | **CORE** |
| 8 | Applied Materials, Inc. | `AMAT` | 77 | 91 | **81** | **CORE** |
| 9 | Robinhood Markets, Inc. | `HOOD` | 77 | 86 | **80** | **CORE** |
| 10 | Advanced Micro Devices, Inc. | `AMD` | 70 | 100 | **79** | **CORE** |

## Combined model — SHORT

Weighted score: **70% fundamental + 30% P/E trend**.

| Rank | Company | OKX | Fundamental SHORT | P/E trend SHORT | Combined | Signal |
|---:|---|---|---:|---:|---:|---|
| 1 | Rocket Lab Corporation | `RKLB` | 100 | 0 | **100** | **CORE** |
| 2 | USA Rare Earth, Inc. | `USAR` | 100 | 0 | **100** | **CORE** |
| 3 | IonQ, Inc. | `IONQ` | 88 | 0 | **88** | **CORE** |
| 4 | Nebius Group N.V. | `NBIS` | 84 | 0 | **84** | **WATCH** |
| 5 | Moderna, Inc. | `MRNA` | 80 | 0 | **80** | **WATCH** |
| 6 | AST SpaceMobile, Inc. | `ASTS` | 80 | 0 | **80** | **WATCH** |
| 7 | Cerebras Systems Inc. | `CBRS` | 79 | 0 | **79** | **WATCH** |
| 8 | Okta, Inc. | `OKTA` | 80 | 13 | **60** | **WATCH** |
| 9 | Tesla, Inc. | `TSLA` | 78 | 15 | **59** | **WATCH** |

## P/E Compression + Growth — LONG

| Rank | Company | OKX | Trail P/E | Fwd P/E | P/E change | EPS +1y | Rev +1y | Rev trend | LONG score | Signal |
|---:|---|---|---:|---:|---:|---:|---:|---|---:|---|
| 1 | Credo Technology Group Holding  | `CRDO` | 60.6 | 17.6 | -71.0% | 53.9% | 55.0% | decelerating | **100** | **CORE** |
| 2 | Broadcom Inc. | `AVGO` | 42.0 | 16.9 | -59.6% | 66.4% | 64.1% | decelerating | **100** | **CORE** |
| 3 | Advanced Micro Devices, Inc. | `AMD` | 133.4 | 33.2 | -75.1% | 107.7% | 74.9% | accelerating | **100** | **CORE** |
| 4 | NVIDIA Corporation | `NVDA` | 27.3 | 13.6 | -50.3% | 70.9% | 68.2% | decelerating | **100** | **CORE** |
| 5 | Marvell Technology, Inc. | `MRVL` | 76.4 | 31.7 | -58.5% | 73.7% | 63.3% | accelerating | **100** | **CORE** |
| 6 | Corning Incorporated | `GLW` | 58.3 | 28.9 | -50.4% | 33.6% | 20.0% | accelerating | **96** | **CORE** |
| 7 | AXT Inc | `AXT` | 1364.9 | 24.3 | -98.2% | 159.2% | 111.3% | decelerating | **96** | **CORE** |
| 8 | Oracle Corporation | `ORCL` | 19.8 | 11.5 | -42.0% | 35.1% | 45.7% | accelerating | **95** | **CORE** |
| 9 | Coherent Corp. | `COHR` | 52.5 | 15.5 | -70.4% | 48.3% | 38.3% | decelerating | **95** | **CORE** |
| 10 | Arm Holdings plc | `ARM` | 221.9 | 70.2 | -68.4% | 37.5% | 36.4% | accelerating | **95** | **CORE** |

## P/E Expansion + Weakening — SHORT

| Rank | Company | OKX | Trail P/E | Fwd P/E | P/E change | EPS +1y | Rev +1y | Rev trend | SHORT score | Signal |
|---:|---|---|---:|---:|---:|---:|---:|---|---:|---|
| 1 | SOFTBANK GROUP CORP | `SOFTBANK` | 5.0 | 14.6 | 191.0% | -14.5% | 6.9% | decelerating | **86** | **CORE** |
| 2 | Hyperliquid Strategies Inc | `PURR` | 2.8 | 24.0 | 767.6% | 51.0% | 31.4% | decelerating | **55** | **WATCH** |
| 3 | Amazon.com, Inc. | `AMZN` | 20.3 | 24.1 | 19.0% | -18.2% | 14.6% | decelerating | **52** | **WATCH** |
| 4 | Alphabet Inc. | `GOOGL` | 16.4 | 21.3 | 29.9% | -26.6% | 25.3% | accelerating | **50** | **WATCH** |

## Top SHORT candidates

| Rank | Company | OKX market | SHORT score | Signal | P/S | EV/S | Op margin | Fwd P/E | Rev +1y | FCF yield |
|---:|---|---|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Rocket Lab Corporation | `RKLB-USDT-SWAP` | **100** | **CORE** | 42.9 | 38.9 | -24.6% | 897.0 | 38.2% | -0.8% |
| 2 | USA Rare Earth, Inc. | `USAR-USDT-SWAP` | **100** | **CORE** | 279.8 | 74.9 | -795.6% | 327.3 | 870.1% | -7.7% |
| 3 | IonQ, Inc. | `IONQ-USDT-SWAP` | **88** | **CORE** | 51.8 | 41.6 | -408.2% | -23.4 | 77.6% | -0.7% |
| 4 | Nebius Group N.V. | `NBIS-USDT-SWAP` | **84** | **WATCH** | 32.0 | 36.3 | -0.2% | -44.3 | 266.0% | -22.2% |
| 5 | Okta, Inc. | `OKTA-USDT-SWAP` | **80** | **CORE** | 11.7 | 11.1 | 13.3% | 47.2 | 10.0% | 2.9% |
| 6 | AST SpaceMobile, Inc. | `ASTS-USDT-SWAP` | **80** | **WATCH** | 132.0 | 116.8 | -544.6% | -30.4 | 247.3% | -11.8% |
| 7 | Moderna, Inc. | `MRNA-USDT-SWAP` | **80** | **WATCH** | 42.6 | 42.3 | -557.9% | -53.8 | 15.8% | 0.3% |
| 8 | Cerebras Systems Inc. | `CBRS-USDT-SWAP` | **79** | **WATCH** | 38.4 | 31.7 | -265.0% | 86.4 | 232.7% | — |
| 9 | Tesla, Inc. | `TSLA-USDT-SWAP` | **78** | **WATCH** | 14.6 | 14.5 | 1.4% | 176.5 | 13.1% | 0.3% |

## Top LONG candidates

| Rank | Company | OKX market | LONG score | Signal | P/S | EV/S | Op margin | Fwd P/E | Rev +1y | FCF yield |
|---:|---|---|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Taiwan Semiconductor Manufactur | `TSM-USDT-SWAP` | **90** | **CORE** | 0.4 | 3.0 | 58.7% | 17.8 | 37.5% | 55.6% |
| 2 | Applovin Corporation | `APP-USDT-SWAP` | **83** | **CORE** | 13.1 | 13.2 | 77.7% | 13.0 | 26.0% | 3.6% |
| 3 | Sandisk Corporation | `SNDK-USDT-SWAP` | **82** | **CORE** | 9.5 | 9.7 | 78.5% | 5.0 | 18.9% | 4.0% |
| 4 | Corning Incorporated | `GLW-USDT-SWAP` | **77** | **WATCH** | 6.4 | 7.3 | 15.6% | 28.9 | 20.0% | 0.7% |
| 5 | Robinhood Markets, Inc. | `HOOD-USDT-SWAP` | **77** | **WATCH** | 18.2 | 18.4 | 43.9% | 29.2 | 29.3% | — |
| 6 | Applied Materials, Inc. | `AMAT-USDT-SWAP` | **77** | **WATCH** | 9.9 | 10.5 | 33.7% | 20.9 | 35.3% | 1.0% |
| 7 | Credo Technology Group Holding  | `CRDO-USDT-SWAP` | **75** | **WATCH** | 20.2 | 21.1 | 25.2% | 17.6 | 55.0% | 0.8% |
| 8 | Broadcom Inc. | `AVGO-USDT-SWAP` | **75** | **WATCH** | 17.6 | 18.5 | 54.3% | 16.9 | 64.1% | 2.0% |
| 9 | Micron Technology, Inc. | `MU-USDT-SWAP` | **75** | **CORE** | 7.6 | 7.5 | 80.7% | 4.3 | 15.6% | 2.9% |
| 10 | NVIDIA Corporation | `NVDA-USDT-SWAP` | **75** | **WATCH** | 17.2 | 17.6 | 66.2% | 13.6 | 68.2% | 0.8% |

## Analyst consensus (12-month price target) — most upside

| Rank | Company | OKX | Price | Analyst mean target | Gap | Analysts | Currency |
|---:|---|---|---:|---:|---:|---:|---|
| 1 | Cerebras Systems Inc. | `CBRS` | 110.01 | 282.55 | **156.8%** | 11 | USD |
| 2 | SK hynix | `SKHYNIX` | 1223000.00 | 3096288.00 | **153.2%** | 38 | KRW |
| 3 | Hyperliquid Strategies Inc | `PURR` | 8.87 | 22.32 | **151.8%** | 4 | USD |
| 4 | CoreWeave, Inc. | `CRWV` | 58.47 | 138.34 | **136.6%** | 38 | USD |
| 5 | Applied Optoelectronics, Inc. | `AAOI` | 71.12 | 160.00 | **125.0%** | 5 | USD |
| 6 | SamsungElec | `SAMSUNG` | 214500.00 | 478905.62 | **123.3%** | 36 | KRW |
| 7 | IonQ, Inc. | `IONQ` | 31.49 | 64.06 | **103.4%** | 14 | USD |
| 8 | BitMine Immersion Technologies, | `BMNR` | 22.79 | 45.87 | **101.3%** | 3 | USD |
| 9 | Rocket Lab Corporation | `RKLB` | 51.57 | 102.15 | **98.1%** | 20 | USD |
| 10 | AST SpaceMobile, Inc. | `ASTS` | 39.12 | 74.28 | **89.9%** | 12 | USD |
| 11 | Oracle Corporation | `ORCL` | 126.44 | 237.36 | **87.7%** | 41 | USD |
| 12 | Coherent Corp. | `COHR` | 216.25 | 394.79 | **82.6%** | 24 | USD |
| 13 | Western Digital Corporation | `WDC` | 360.50 | 654.00 | **81.4%** | 24 | USD |
| 14 | SOFTBANK GROUP CORP | `SOFTBANK` | 4305.00 | 7782.47 | **80.8%** | 18 | JPY |
| 15 | Applovin Corporation | `APP` | 265.94 | 476.85 | **79.3%** | 31 | USD |

## Analyst consensus (12-month price target) — most downside

| Rank | Company | OKX | Price | Analyst mean target | Gap | Analysts | Currency |
|---:|---|---|---:|---:|---:|---:|---|
| 1 | Moderna, Inc. | `MRNA` | 237.68 | 130.58 | **-45.1%** | 19 | USD |
| 2 | Apple Inc. | `AAPL` | 345.35 | 328.35 | **-4.9%** | 39 | USD |

Price/target uses the underlying Yahoo Finance share quote, not the OKX derivative. Minimum 3 analysts; unreliable price scales and missing coverage excluded. Targets are analyst opinions, not guaranteed forecasts.

## All OKX companies — our ratio + LONG/SHORT scores

| Company | OKX | P/S | EV/S | Op margin | Fwd P/E | EPS +1y | Rev +1y | FCF yield | LONG | SHORT |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Rocket Lab Corporation | `RKLB` | 42.9 | 38.9 | -24.6% | 897.0 | 66.8% | 38.2% | -0.8% | **0** | **100 CORE** |
| USA Rare Earth, Inc. | `USAR` | 279.8 | 74.9 | -795.6% | 327.3 | 105.3% | 870.1% | -7.7% | **0** | **100 CORE** |
| Taiwan Semiconductor Manufactur | `TSM` | 0.4 | 3.0 | 58.7% | 17.8 | 33.6% | 37.5% | 55.6% | **90 CORE** | **10** |
| IonQ, Inc. | `IONQ` | 51.8 | 41.6 | -408.2% | -23.4 | 21.3% | 77.6% | -0.7% | **0** | **88 CORE** |
| Nebius Group N.V. | `NBIS` | 32.0 | 36.3 | -0.2% | -44.3 | -191.4% | 266.0% | -22.2% | **0** | **84 WATCH** |
| Applovin Corporation | `APP` | 13.1 | 13.2 | 77.7% | 13.0 | 27.1% | 26.0% | 3.6% | **83 CORE** | **10** |
| Sandisk Corporation | `SNDK` | 9.5 | 9.7 | 78.5% | 5.0 | 24.0% | 18.9% | 4.0% | **82 CORE** | **10** |
| Okta, Inc. | `OKTA` | 11.7 | 11.1 | 13.3% | 47.2 | 11.4% | 10.0% | 2.9% | **8** | **80 CORE** |
| Moderna, Inc. | `MRNA` | 42.6 | 42.3 | -557.9% | -53.8 | 43.2% | 15.8% | 0.3% | **0** | **80 WATCH** |
| AST SpaceMobile, Inc. | `ASTS` | 132.0 | 116.8 | -544.6% | -30.4 | 44.3% | 247.3% | -11.8% | **0** | **80 WATCH** |
| Cerebras Systems Inc. | `CBRS` | 38.4 | 31.7 | -265.0% | 86.4 | 371.3% | 232.7% | — | **0** | **79 WATCH** |
| Tesla, Inc. | `TSLA` | 14.6 | 14.5 | 1.4% | 176.5 | 24.8% | 13.1% | 0.3% | **12** | **78 WATCH** |
| Corning Incorporated | `GLW` | 6.4 | 7.3 | 15.6% | 28.9 | 33.6% | 20.0% | 0.7% | **77 WATCH** | **13** |
| Applied Materials, Inc. | `AMAT` | 9.9 | 10.5 | 33.7% | 20.9 | 44.6% | 35.3% | 1.0% | **77 WATCH** | **3** |
| Robinhood Markets, Inc. | `HOOD` | 18.2 | 18.4 | 43.9% | 29.2 | 36.5% | 29.3% | — | **77 WATCH** | **5** |
| Credo Technology Group Holding  | `CRDO` | 20.2 | 21.1 | 25.2% | 17.6 | 53.9% | 55.0% | 0.8% | **75 WATCH** | **28** |
| Broadcom Inc. | `AVGO` | 17.6 | 18.5 | 54.3% | 16.9 | 66.4% | 64.1% | 2.0% | **75 WATCH** | **28** |
| NVIDIA Corporation | `NVDA` | 17.2 | 17.6 | 66.2% | 13.6 | 70.9% | 68.2% | 0.8% | **75 WATCH** | **18** |
| Micron Technology, Inc. | `MU` | 7.6 | 7.5 | 80.7% | 4.3 | 17.2% | 15.6% | 2.9% | **75 CORE** | **30** |
| Western Digital Corporation | `WDC` | 10.4 | 10.5 | 43.6% | 10.7 | 62.4% | 37.7% | 1.7% | **75 WATCH** | **18** |
| Advanced Micro Devices, Inc. | `AMD` | 20.7 | 21.6 | 17.2% | 33.2 | 107.7% | 74.9% | 1.0% | **70 WATCH** | **13** |
| Marvell Technology, Inc. | `MRVL` | 22.1 | 22.9 | 16.7% | 31.7 | 73.7% | 63.3% | 1.2% | **70 WATCH** | **13** |
| Oracle Corporation | `ORCL` | 5.3 | 7.4 | 35.6% | 11.5 | 35.1% | 45.7% | -12.0% | **70 WATCH** | **10** |
| XIAOMI-W | `XIAOMI` | 1.5 | 1.4 | 4.0% | 16.8 | 39.0% | 21.4% | -1.3% | **70 WATCH** | **10** |
| Adobe Inc. | `ADBE` | 3.9 | 3.9 | 34.8% | 9.5 | 12.4% | 9.1% | 9.2% | **65 WATCH** | **30** |
| Coherent Corp. | `COHR` | 6.0 | 6.8 | 11.8% | 15.5 | 48.3% | 38.3% | -1.5% | **60 WATCH** | **35** |
| Microsoft Corporation | `MSFT` | 11.8 | 12.1 | 45.1% | 22.2 | 20.0% | 19.7% | 0.4% | **59 WATCH** | **23** |
| Apple Inc. | `AAPL` | 10.8 | 10.8 | 32.6% | 36.1 | 8.4% | 10.4% | 2.1% | **5** | **58** |
| Coca-Cola Company (The) | `KO` | 8.1 | 8.6 | 34.9% | 26.7 | 6.7% | -0.1% | 1.3% | **0** | **58** |
| Meta Platforms, Inc. | `META` | 7.3 | 7.9 | 34.8% | 18.6 | 15.1% | 21.1% | 1.3% | **57 WATCH** | **38** |
| Bloom Energy Corporation | `BE` | 21.2 | 22.6 | 17.1% | 45.4 | 82.4% | 62.7% | 0.8% | **55 WATCH** | **48** |
| AXT Inc | `AXT` | 28.5 | 28.3 | 21.9% | 24.3 | 159.2% | 111.3% | -1.2% | **52** | **35** |
| Super Micro Computer, Inc. | `SMCI` | 0.6 | 0.8 | 13.4% | 6.1 | 19.7% | 16.3% | -36.8% | **52** | **45** |
| Lumentum Holdings Inc. | `LITE` | 23.7 | 25.0 | 28.0% | 22.0 | 64.9% | 57.2% | 0.3% | **0** | **51** |
| Netflix, Inc. | `NFLX` | 5.5 | 5.5 | 34.6% | 17.5 | 5.2% | 10.8% | 9.3% | **35** | **50** |
| IREN LIMITED | `IREN` | 14.3 | 18.3 | -102.5% | -6.4 | -16.4% | 164.0% | -41.7% | **0** | **50** |
| Palantir Technologies Inc. | `PLTR` | 78.5 | 77.3 | 47.1% | 85.5 | 45.2% | 50.1% | 0.4% | **33** | **48** |
| Intel Corporation | `INTC` | 8.1 | 8.9 | 12.2% | 41.5 | 38.1% | 15.2% | 1.0% | **10** | **48** |
| SK hynix | `SKHYNIX` | 4.7 | 4.5 | 76.3% | 2.6 | 31.9% | 54.3% | 6.3% | **45** | **5** |
| SK hynix | `SKHY` | 4.7 | 4.5 | 76.3% | 2.6 | 31.9% | 54.3% | 6.3% | **45** | **5** |
| SamsungElec | `SAMSUNG` | 2.9 | 2.7 | 52.2% | 3.0 | 51.4% | 37.7% | 5.0% | **45** | **10** |
| Arm Holdings plc | `ARM` | 44.6 | 46.3 | 7.6% | 70.2 | 37.5% | 36.4% | 0.6% | **43** | **33** |
| Circle Internet Group, Inc. | `CRCL` | 7.5 | 7.2 | 4.9% | 58.0 | 30.0% | 26.7% | 0.9% | **43** | **33** |
| Coinbase Global, Inc. | `COIN` | 7.5 | 7.4 | -13.9% | 56.6 | 266.1% | 30.1% | 5.9% | **20** | **40** |
| SOFTBANK GROUP CORP | `SOFTBANK` | 3.1 | 6.6 | -11.6% | 14.6 | -14.5% | 6.9% | -8.9% | **0** | **40** |
| CoreWeave, Inc. | `CRWV` | 4.2 | 10.6 | -1.9% | -30.8 | 12.6% | 104.7% | -28.2% | **0** | **40** |
| Dell Technologies Inc. | `DELL` | 2.0 | 2.2 | 12.0% | 15.6 | 9.6% | 18.4% | 2.0% | **33** | **38** |
| Amazon.com, Inc. | `AMZN` | 3.5 | 3.8 | 13.7% | 24.1 | -18.2% | 14.6% | 0.1% | **0** | **38** |
| Fluence Energy, Inc. | `FLNC` | 0.4 | 0.4 | -8.9% | -12.9 | 60.4% | 26.9% | 0.2% | **5** | **28** |
| Hyperliquid Strategies Inc | `PURR` | 260.8 | 186.6 | 9595.1% | 24.0 | 51.0% | 31.4% | — | **25** | **10** |
| BitMine Immersion Technologies, | `BMNR` | 224.7 | 230.7 | 8.4% | 24.2 | 103.2% | 421.8% | -3.8% | **25** | **25** |
| Strategy Inc | `MSTR` | 124.2 | 156.0 | -6808.1% | 3.0 | 168.2% | 2.2% | -36.5% | **25** | **25** |
| QUALCOMM Incorporated | `QCOM` | 4.3 | 4.4 | 18.5% | 17.2 | -2.8% | 4.7% | 5.5% | **25** | **15** |
| Applied Optoelectronics, Inc. | `AAOI` | 10.1 | 10.6 | -12.9% | 15.5 | 576.8% | 156.5% | -14.7% | **10** | **25** |
| Alphabet Inc. | `GOOGL` | 9.0 | 8.9 | 34.0% | 21.3 | -26.6% | 25.3% | 0.6% | **12** | **23** |

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
