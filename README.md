# OKX Long / Short Fundamental Scanner

Hourly scanner restricted to public companies exposed by the **OKX EEA TradFi / Stock Perpetual API universe**.

**Last scan:** 2026-10-30 05:57 UTC  
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
| 1 | Taiwan Semiconductor Manufactur | TSM | 0.0% | 3.2% | 1.6% | 88 | -1 | **87** | **CORE** | yes |
| 2 | Marvell Technology, Inc. | MRVL | 0.0% | -4.5% | -2.2% | 84 | +2 | **86** | **CORE** | yes |
| 3 | Applovin Corporation | APP | -0.0% | -2.1% | -1.0% | 82 | +1 | **83** | **CORE** | yes |
| 4 | NVIDIA Corporation | NVDA | -0.0% | 1.3% | 0.6% | 82 | -1 | **81** | **CORE** | yes |
| 5 | Robinhood Markets, Inc. | HOOD | 0.0% | -3.7% | -1.8% | 80 | +1 | **81** | **CORE** | yes |
| 6 | Sandisk Corporation | SNDK | -0.0% | 7.4% | 3.7% | 82 | -3 | **79** | **CORE** | yes |
| 7 | Broadcom Inc. | AVGO | 0.0% | 7.2% | 3.6% | 82 | -3 | **79** | **CORE** | yes |
| 8 | Corning Incorporated | GLW | -0.0% | 4.2% | 2.1% | 80 | -2 | **78** | **CORE** | yes |
| 9 | Credo Technology Group Holding  | CRDO | 0.0% | 12.2% | 6.1% | 82 | -5 | **77** | **CORE** | yes |
| 10 | Applied Materials, Inc. | AMAT | -0.0% | 11.8% | 5.9% | 81 | -5 | **76** | **CORE** | yes |

## Final model + Price Timing — SHORT

| Rank | Company | OKX | 24h | 7d | 50/50 move | Base SHORT | Timing adj. | Final | Signal | Prev. SHORT? |
|---:|---|---|---:|---:|---:|---:|---:|---:|---|---|
| 1 | USA Rare Earth, Inc. | USAR | -0.0% | 12.8% | 6.4% | 100 | +5 | **100** | **CORE** | yes |
| 2 | Rocket Lab Corporation | RKLB | 0.0% | 12.4% | 6.2% | 100 | +5 | **100** | **CORE** | yes |
| 3 | IonQ, Inc. | IONQ | 0.0% | 1.4% | 0.7% | 88 | +1 | **89** | **CORE** | yes |
| 4 | Nebius Group N.V. | NBIS | -0.0% | 8.3% | 4.2% | 84 | +3 | **87** | **CORE** | yes |
| 5 | Cerebras Systems Inc. | CBRS | -0.0% | 3.9% | 2.0% | 82 | +2 | **84** | **CORE** | yes |
| 6 | AST SpaceMobile, Inc. | ASTS | 0.0% | 8.2% | 4.1% | 80 | +3 | **83** | **CORE** | yes |
| 7 | Moderna, Inc. | MRNA | 0.0% | 11.3% | 5.7% | 72 | +5 | **77** | **CORE** | yes |
| 8 | Lumentum Holdings Inc. | LITE | -0.0% | 21.6% | 10.8% | 59 | +9 | **68** | **WATCH** | yes |
| 9 | Okta, Inc. | OKTA | -0.0% | 4.1% | 2.1% | 61 | +2 | **63** | **WATCH** | yes |
| 10 | IREN LIMITED | IREN | 0.0% | 5.4% | 2.7% | 60 | +2 | **62** | **WATCH** | yes |

## Combined model — LONG

Weighted score: **70% fundamental + 30% P/E trend**.

| Rank | Company | OKX | Fundamental LONG | P/E trend LONG | Combined | Signal |
|---:|---|---|---:|---:|---:|---|
| 1 | Taiwan Semiconductor Manufactur | `TSM` | 90 | 85 | **88** | **CORE** |
| 2 | Marvell Technology, Inc. | `MRVL` | 77 | 100 | **84** | **CORE** |
| 3 | Applovin Corporation | `APP` | 83 | 80 | **82** | **CORE** |
| 4 | Sandisk Corporation | `SNDK` | 82 | 82 | **82** | **CORE** |
| 5 | NVIDIA Corporation | `NVDA` | 75 | 100 | **82** | **CORE** |
| 6 | Broadcom Inc. | `AVGO` | 75 | 100 | **82** | **CORE** |
| 7 | Credo Technology Group Holding  | `CRDO` | 75 | 100 | **82** | **CORE** |
| 8 | Applied Materials, Inc. | `AMAT` | 77 | 91 | **81** | **CORE** |
| 9 | Robinhood Markets, Inc. | `HOOD` | 77 | 86 | **80** | **CORE** |
| 10 | Corning Incorporated | `GLW` | 77 | 86 | **80** | **CORE** |

## Combined model — SHORT

Weighted score: **70% fundamental + 30% P/E trend**.

| Rank | Company | OKX | Fundamental SHORT | P/E trend SHORT | Combined | Signal |
|---:|---|---|---:|---:|---:|---|
| 1 | Rocket Lab Corporation | `RKLB` | 100 | 0 | **100** | **CORE** |
| 2 | USA Rare Earth, Inc. | `USAR` | 100 | 0 | **100** | **CORE** |
| 3 | IonQ, Inc. | `IONQ` | 88 | 0 | **88** | **CORE** |
| 4 | Nebius Group N.V. | `NBIS` | 84 | 0 | **84** | **WATCH** |
| 5 | Cerebras Systems Inc. | `CBRS` | 82 | 0 | **82** | **WATCH** |
| 6 | AST SpaceMobile, Inc. | `ASTS` | 80 | 0 | **80** | **WATCH** |
| 7 | Moderna, Inc. | `MRNA` | 72 | 0 | **72** | **WATCH** |
| 8 | Okta, Inc. | `OKTA` | 80 | 18 | **61** | **WATCH** |
| 9 | Tesla, Inc. | `TSLA` | 78 | 15 | **59** | **WATCH** |

## P/E Compression + Growth — LONG

| Rank | Company | OKX | Trail P/E | Fwd P/E | P/E change | EPS +1y | Rev +1y | Rev trend | LONG score | Signal |
|---:|---|---|---:|---:|---:|---:|---:|---|---:|---|
| 1 | Marvell Technology, Inc. | `MRVL` | 82.7 | 29.8 | -64.0% | 73.6% | 63.3% | accelerating | **100** | **CORE** |
| 2 | NVIDIA Corporation | `NVDA` | 27.0 | 13.4 | -50.3% | 70.9% | 68.2% | decelerating | **100** | **CORE** |
| 3 | Broadcom Inc. | `AVGO` | 44.1 | 17.7 | -59.8% | 66.9% | 64.4% | decelerating | **100** | **CORE** |
| 4 | Credo Technology Group Holding  | `CRDO` | 58.6 | 17.0 | -71.0% | 53.9% | 55.0% | decelerating | **100** | **CORE** |
| 5 | Advanced Micro Devices, Inc. | `AMD` | 144.5 | 35.6 | -75.4% | 108.3% | 75.1% | accelerating | **100** | **CORE** |
| 6 | AXT Inc | `AXT` | 1522.0 | 27.1 | -98.2% | 159.2% | 111.3% | decelerating | **96** | **CORE** |
| 7 | Oracle Corporation | `ORCL` | 21.9 | 12.6 | -42.2% | 35.4% | 45.7% | accelerating | **95** | **CORE** |
| 8 | Coherent Corp. | `COHR` | 57.6 | 17.1 | -70.4% | 48.0% | 38.1% | decelerating | **95** | **CORE** |
| 9 | Arm Holdings plc | `ARM` | 235.8 | 74.6 | -68.4% | 37.5% | 36.4% | accelerating | **95** | **CORE** |
| 10 | Bloom Energy Corporation | `BE` | 134.7 | 41.9 | -68.9% | 62.7% | 56.0% | decelerating | **92** | **CORE** |

## P/E Expansion + Weakening — SHORT

| Rank | Company | OKX | Trail P/E | Fwd P/E | P/E change | EPS +1y | Rev +1y | Rev trend | SHORT score | Signal |
|---:|---|---|---:|---:|---:|---:|---:|---|---:|---|
| 1 | SOFTBANK GROUP CORP | `SOFTBANK` | 5.2 | 15.1 | 191.0% | -14.5% | 7.0% | decelerating | **86** | **CORE** |
| 2 | Hyperliquid Strategies Inc | `PURR` | 3.8 | 33.2 | 767.6% | 51.0% | 31.4% | decelerating | **55** | **WATCH** |
| 3 | Amazon.com, Inc. | `AMZN` | 19.6 | 23.3 | 18.9% | -18.3% | 14.6% | decelerating | **52** | **WATCH** |
| 4 | Alphabet Inc. | `GOOGL` | 14.8 | 18.7 | 26.5% | -24.2% | 26.6% | accelerating | **50** | **WATCH** |

## Top SHORT candidates

| Rank | Company | OKX market | SHORT score | Signal | P/S | EV/S | Op margin | Fwd P/E | Rev +1y | FCF yield |
|---:|---|---|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Rocket Lab Corporation | `RKLB-USDT-SWAP` | **100** | **CORE** | 49.1 | 43.2 | -24.6% | 1028.0 | 38.2% | -0.7% |
| 2 | USA Rare Earth, Inc. | `USAR-USDT-SWAP` | **100** | **CORE** | 299.8 | 80.3 | -795.6% | 350.7 | 870.1% | -7.2% |
| 3 | IonQ, Inc. | `IONQ-USDT-SWAP` | **88** | **CORE** | 55.3 | 40.7 | -408.2% | -23.6 | 77.6% | -0.6% |
| 4 | Nebius Group N.V. | `NBIS-USDT-SWAP` | **84** | **WATCH** | 32.2 | 36.4 | -0.2% | -47.8 | 266.0% | -22.0% |
| 5 | Cerebras Systems Inc. | `CBRS-USDT-SWAP` | **82** | **WATCH** | 40.2 | 30.7 | -265.0% | 90.4 | 232.7% | — |
| 6 | Okta, Inc. | `OKTA-USDT-SWAP` | **80** | **CORE** | 12.6 | 11.9 | 13.3% | 50.7 | 10.1% | 2.7% |
| 7 | AST SpaceMobile, Inc. | `ASTS-USDT-SWAP` | **80** | **WATCH** | 145.4 | 122.5 | -544.6% | -33.5 | 264.2% | -10.7% |
| 8 | Tesla, Inc. | `TSLA-USDT-SWAP` | **78** | **WATCH** | 15.4 | 15.1 | 5.4% | 187.1 | 13.5% | 0.3% |
| 9 | Moderna, Inc. | `MRNA-USDT-SWAP` | **72** | **WATCH** | 39.9 | 38.2 | -557.9% | -48.6 | 16.3% | 0.3% |

## Top LONG candidates

| Rank | Company | OKX market | LONG score | Signal | P/S | EV/S | Op margin | Fwd P/E | Rev +1y | FCF yield |
|---:|---|---|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Taiwan Semiconductor Manufactur | `TSM-USDT-SWAP` | **90** | **CORE** | 0.5 | 3.0 | 58.7% | 18.5 | 37.6% | 53.7% |
| 2 | Applovin Corporation | `APP-USDT-SWAP` | **83** | **CORE** | 12.5 | 12.6 | 77.7% | 12.4 | 25.1% | 3.7% |
| 3 | Sandisk Corporation | `SNDK-USDT-SWAP` | **82** | **CORE** | 9.5 | 9.4 | 78.5% | 5.0 | 18.6% | 4.0% |
| 4 | Corning Incorporated | `GLW-USDT-SWAP` | **77** | **WATCH** | 6.3 | 6.9 | 18.8% | 28.5 | 21.1% | 0.8% |
| 5 | Robinhood Markets, Inc. | `HOOD-USDT-SWAP` | **77** | **WATCH** | — | — | 0.0% | 27.0 | 29.0% | — |
| 6 | Applied Materials, Inc. | `AMAT-USDT-SWAP` | **77** | **WATCH** | 10.9 | 10.8 | 33.7% | 22.7 | 35.3% | 0.9% |
| 7 | Marvell Technology, Inc. | `MRVL-USDT-SWAP` | **77** | **WATCH** | 20.8 | 20.4 | 16.7% | 29.8 | 63.3% | 1.2% |
| 8 | Credo Technology Group Holding  | `CRDO-USDT-SWAP` | **75** | **WATCH** | 19.5 | 19.1 | 25.2% | 17.0 | 55.0% | 0.8% |
| 9 | Broadcom Inc. | `AVGO-USDT-SWAP` | **75** | **WATCH** | 18.5 | 18.9 | 54.3% | 17.7 | 64.4% | 1.9% |
| 10 | Micron Technology, Inc. | `MU-USDT-SWAP` | **75** | **CORE** | 7.9 | 7.6 | 80.7% | 4.5 | 16.0% | 2.8% |

## Analyst consensus (12-month price target) — most upside

| Rank | Company | OKX | Price | Analyst mean target | Gap | Analysts | Currency |
|---:|---|---|---:|---:|---:|---:|---|
| 1 | IREN LIMITED | `IREN` | 26.25 | 76.92 | **193.0%** | 18 | USD |
| 2 | Cerebras Systems Inc. | `CBRS` | 115.16 | 282.55 | **145.4%** | 11 | USD |
| 3 | SK hynix | `SKHYNIX` | 1417000.00 | 3157408.80 | **122.8%** | 39 | KRW |
| 4 | CoreWeave, Inc. | `CRWV` | 60.74 | 134.58 | **121.6%** | 38 | USD |
| 5 | SamsungElec | `SAMSUNG` | 222500.00 | 481160.10 | **116.3%** | 35 | KRW |
| 6 | BitMine Immersion Technologies, | `BMNR` | 21.66 | 45.87 | **111.8%** | 3 | USD |
| 7 | IonQ, Inc. | `IONQ` | 31.72 | 64.06 | **102.0%** | 14 | USD |
| 8 | Applied Optoelectronics, Inc. | `AAOI` | 79.19 | 156.00 | **97.0%** | 5 | USD |
| 9 | Hyperliquid Strategies Inc | `PURR` | 12.29 | 22.32 | **81.7%** | 4 | USD |
| 10 | Applovin Corporation | `APP` | 254.91 | 452.95 | **77.7%** | 31 | USD |
| 11 | SOFTBANK GROUP CORP | `SOFTBANK` | 4471.00 | 7845.25 | **75.5%** | 18 | JPY |
| 12 | AST SpaceMobile, Inc. | `ASTS` | 43.07 | 74.68 | **73.4%** | 12 | USD |
| 13 | Rocket Lab Corporation | `RKLB` | 59.10 | 102.15 | **72.8%** | 20 | USD |
| 14 | Credo Technology Group Holding  | `CRDO` | 165.29 | 284.05 | **71.8%** | 19 | USD |
| 15 | Oracle Corporation | `ORCL` | 139.56 | 235.80 | **69.0%** | 41 | USD |

## Analyst consensus (12-month price target) — most downside

| Rank | Company | OKX | Price | Analyst mean target | Gap | Analysts | Currency |
|---:|---|---|---:|---:|---:|---:|---|
| 1 | Moderna, Inc. | `MRNA` | 222.76 | 138.37 | **-37.9%** | 19 | USD |
| 2 | Apple Inc. | `AAPL` | 348.91 | 332.39 | **-4.7%** | 38 | USD |
| 3 | Okta, Inc. | `OKTA` | 221.86 | 214.72 | **-3.2%** | 43 | USD |

Price/target uses the underlying Yahoo Finance share quote, not the OKX derivative. Minimum 3 analysts; unreliable price scales and missing coverage excluded. Targets are analyst opinions, not guaranteed forecasts.

## All OKX companies — our ratio + LONG/SHORT scores

| Company | OKX | P/S | EV/S | Op margin | Fwd P/E | EPS +1y | Rev +1y | FCF yield | LONG | SHORT |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Rocket Lab Corporation | `RKLB` | 49.1 | 43.2 | -24.6% | 1028.0 | 66.8% | 38.2% | -0.7% | **0** | **100 CORE** |
| USA Rare Earth, Inc. | `USAR` | 299.8 | 80.3 | -795.6% | 350.7 | 105.3% | 870.1% | -7.2% | **0** | **100 CORE** |
| Taiwan Semiconductor Manufactur | `TSM` | 0.5 | 3.0 | 58.7% | 18.5 | 33.6% | 37.6% | 53.7% | **90 CORE** | **10** |
| IonQ, Inc. | `IONQ` | 55.3 | 40.7 | -408.2% | -23.6 | 21.3% | 77.6% | -0.6% | **0** | **88 CORE** |
| Nebius Group N.V. | `NBIS` | 32.2 | 36.4 | -0.2% | -47.8 | -191.4% | 266.0% | -22.0% | **0** | **84 WATCH** |
| Applovin Corporation | `APP` | 12.5 | 12.6 | 77.7% | 12.4 | 25.9% | 25.1% | 3.7% | **83 CORE** | **10** |
| Sandisk Corporation | `SNDK` | 9.5 | 9.4 | 78.5% | 5.0 | 23.6% | 18.6% | 4.0% | **82 CORE** | **10** |
| Cerebras Systems Inc. | `CBRS` | 40.2 | 30.7 | -265.0% | 90.4 | 371.3% | 232.7% | — | **0** | **82 WATCH** |
| Okta, Inc. | `OKTA` | 12.6 | 11.9 | 13.3% | 50.7 | 11.4% | 10.1% | 2.7% | **8** | **80 CORE** |
| AST SpaceMobile, Inc. | `ASTS` | 145.4 | 122.5 | -544.6% | -33.5 | 44.3% | 264.2% | -10.7% | **0** | **80 WATCH** |
| Tesla, Inc. | `TSLA` | 15.4 | 15.1 | 5.4% | 187.1 | 23.8% | 13.5% | 0.3% | **12** | **78 WATCH** |
| Marvell Technology, Inc. | `MRVL` | 20.8 | 20.4 | 16.7% | 29.8 | 73.6% | 63.3% | 1.2% | **77 WATCH** | **13** |
| Robinhood Markets, Inc. | `HOOD` | — | — | 0.0% | 27.0 | 41.3% | 29.0% | — | **77 WATCH** | **5** |
| Corning Incorporated | `GLW` | 6.3 | 6.9 | 18.8% | 28.5 | 34.0% | 21.1% | 0.8% | **77 WATCH** | **13** |
| Applied Materials, Inc. | `AMAT` | 10.9 | 10.8 | 33.7% | 22.7 | 45.0% | 35.3% | 0.9% | **77 WATCH** | **3** |
| NVIDIA Corporation | `NVDA` | 17.0 | 16.9 | 66.2% | 13.4 | 70.9% | 68.2% | 0.8% | **75 WATCH** | **18** |
| Broadcom Inc. | `AVGO` | 18.5 | 18.9 | 54.3% | 17.7 | 66.9% | 64.4% | 1.9% | **75 WATCH** | **28** |
| Credo Technology Group Holding  | `CRDO` | 19.5 | 19.1 | 25.2% | 17.0 | 53.9% | 55.0% | 0.8% | **75 WATCH** | **28** |
| Micron Technology, Inc. | `MU` | 7.9 | 7.6 | 80.7% | 4.5 | 17.7% | 16.0% | 2.8% | **75 CORE** | **30** |
| Western Digital Corporation | `WDC` | 10.2 | 10.2 | 47.7% | 9.8 | 63.4% | 40.5% | 1.8% | **75 WATCH** | **18** |
| Moderna, Inc. | `MRNA` | 39.9 | 38.2 | -557.9% | -48.6 | 42.3% | 16.3% | 0.3% | **0** | **72 WATCH** |
| Advanced Micro Devices, Inc. | `AMD` | 22.4 | 22.2 | 17.2% | 35.6 | 108.3% | 75.1% | 1.0% | **70 WATCH** | **13** |
| Oracle Corporation | `ORCL` | 5.9 | 7.8 | 35.6% | 12.6 | 35.4% | 45.7% | -10.8% | **70 WATCH** | **10** |
| XIAOMI-W | `XIAOMI` | 1.6 | 1.3 | 4.0% | 17.6 | 36.8% | 19.7% | -1.3% | **70 WATCH** | **10** |
| Apple Inc. | `AAPL` | 10.9 | 11.0 | 32.6% | 36.5 | 8.4% | 10.4% | 2.1% | **5** | **68** |
| Dell Technologies Inc. | `DELL` | 2.0 | 2.2 | 12.0% | 15.7 | 16.2% | 19.2% | 2.0% | **67 WATCH** | **38** |
| Adobe Inc. | `ADBE` | 3.7 | 3.8 | 34.8% | 9.0 | 12.4% | 9.1% | 9.7% | **65 WATCH** | **30** |
| Coherent Corp. | `COHR` | 6.6 | 6.8 | 11.8% | 17.1 | 48.0% | 38.1% | -1.4% | **60 WATCH** | **35** |
| IREN LIMITED | `IREN` | 15.0 | 17.4 | -102.5% | -6.6 | -16.4% | 164.0% | -39.7% | **0** | **60** |
| Microsoft Corporation | `MSFT` | 11.9 | 12.0 | 45.1% | 22.4 | 19.9% | 19.7% | 0.4% | **59 WATCH** | **23** |
| Lumentum Holdings Inc. | `LITE` | 27.6 | 27.0 | 28.0% | 25.7 | 63.9% | 56.5% | 0.3% | **0** | **59** |
| Coca-Cola Company (The) | `KO` | 7.8 | 8.4 | 33.4% | 26.3 | 5.6% | -3.0% | 1.1% | **0** | **58** |
| Meta Platforms, Inc. | `META` | 6.6 | 6.7 | 35.4% | 17.5 | 16.4% | 21.6% | 1.1% | **57 WATCH** | **38** |
| Bloom Energy Corporation | `BE` | 17.2 | 17.2 | 18.5% | 41.9 | 62.7% | 56.0% | -0.0% | **40** | **55** |
| AXT Inc | `AXT` | 31.8 | 29.2 | 21.9% | 27.1 | 159.2% | 111.3% | -1.1% | **52** | **35** |
| Super Micro Computer, Inc. | `SMCI` | 0.6 | 0.7 | 13.4% | 6.2 | 19.7% | 16.3% | -37.0% | **52** | **45** |
| Netflix, Inc. | `NFLX` | 5.2 | 5.3 | 34.6% | 16.5 | 5.1% | 10.7% | 9.9% | **35** | **50** |
| Palantir Technologies Inc. | `PLTR` | 76.7 | 75.2 | 47.1% | 84.1 | 45.2% | 50.5% | 0.5% | **33** | **48** |
| Intel Corporation | `INTC` | 8.5 | 8.8 | 12.2% | 42.6 | 40.8% | 15.4% | 1.0% | **10** | **48** |
| SK hynix | `SKHYNIX` | 5.3 | 5.4 | 76.3% | 2.7 | 47.0% | 58.5% | 5.6% | **45** | **5** |
| SK hynix | `SKHY` | 5.3 | 5.4 | 76.3% | 2.7 | 47.0% | 58.5% | 5.6% | **45** | **5** |
| SamsungElec | `SAMSUNG` | 3.0 | 2.8 | 52.2% | 3.1 | 51.5% | 41.5% | 4.8% | **45** | **10** |
| Arm Holdings plc | `ARM` | 47.4 | 46.7 | 7.6% | 74.6 | 37.5% | 36.4% | 0.5% | **43** | **33** |
| Coinbase Global, Inc. | `COIN` | 7.0 | 6.7 | -13.9% | 53.2 | 278.9% | 29.9% | 6.3% | **20** | **40** |
| SOFTBANK GROUP CORP | `SOFTBANK` | 3.2 | 6.7 | -11.6% | 15.1 | -14.5% | 7.0% | -8.6% | **0** | **40** |
| CoreWeave, Inc. | `CRWV` | 4.4 | 10.5 | -1.9% | -30.9 | 9.7% | 105.6% | -27.1% | **0** | **40** |
| Amazon.com, Inc. | `AMZN` | 3.4 | 3.6 | 13.7% | 23.3 | -18.3% | 14.6% | 0.1% | **0** | **38** |
| Circle Internet Group, Inc. | `CRCL` | 7.0 | 6.4 | 4.9% | 54.2 | 27.0% | 27.4% | 1.0% | **35** | **33** |
| Fluence Energy, Inc. | `FLNC` | 0.5 | 0.4 | -8.9% | -11.5 | 59.3% | 25.4% | 0.2% | **5** | **28** |
| Hyperliquid Strategies Inc | `PURR` | 361.5 | 242.4 | 9595.1% | 33.2 | 51.0% | 31.4% | — | **25** | **10** |
| Strategy Inc | `MSTR` | 120.4 | 146.8 | -6808.1% | 6.0 | 168.0% | 2.5% | -37.7% | **25** | **25** |
| BitMine Immersion Technologies, | `BMNR` | 213.5 | 208.0 | 8.4% | 23.0 | 103.2% | 421.8% | -4.0% | **25** | **25** |
| QUALCOMM Incorporated | `QCOM` | 4.5 | 4.6 | 18.5% | 18.2 | -2.8% | 4.6% | 5.2% | **25** | **15** |
| Applied Optoelectronics, Inc. | `AAOI` | 11.3 | 10.9 | -12.9% | 17.2 | 576.8% | 156.5% | -13.2% | **10** | **25** |
| Alphabet Inc. | `GOOGL` | 7.8 | 8.7 | 34.0% | 18.7 | -24.2% | 26.6% | 0.7% | **20** | **23** |

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
