# OKX Long / Short Fundamental Scanner

Hourly scanner restricted to public companies exposed by the **OKX EEA TradFi / Stock Perpetual API universe**.

**Last scan:** 2026-10-28 13:08 UTC  
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
| 1 | Taiwan Semiconductor Manufactur | TSM | 0.0% | 1.2% | 0.6% | 88 | +0 | **88** | **CORE** | yes |
| 2 | Credo Technology Group Holding  | CRDO | 0.0% | -8.1% | -4.1% | 82 | +3 | **85** | **CORE** | yes |
| 3 | Sandisk Corporation | SNDK | 0.0% | -5.3% | -2.7% | 82 | +2 | **84** | **CORE** | yes |
| 4 | NVIDIA Corporation | NVDA | -0.0% | -1.8% | -0.9% | 82 | +1 | **83** | **CORE** | yes |
| 5 | Applovin Corporation | APP | -0.0% | -1.9% | -0.9% | 82 | +1 | **83** | **CORE** | yes |
| 6 | Robinhood Markets, Inc. | HOOD | 0.0% | -7.2% | -3.6% | 80 | +3 | **83** | **CORE** | yes |
| 7 | Corning Incorporated | GLW | -0.0% | -6.4% | -3.2% | 80 | +3 | **83** | **CORE** | yes |
| 8 | Applied Materials, Inc. | AMAT | 0.0% | -3.2% | -1.6% | 81 | +1 | **82** | **CORE** | yes |
| 9 | Broadcom Inc. | AVGO | 0.0% | 1.3% | 0.7% | 82 | -1 | **81** | **CORE** | yes |
| 10 | Marvell Technology, Inc. | MRVL | -0.0% | -0.5% | -0.2% | 79 | +0 | **79** | **CORE** | yes |

## Final model + Price Timing — SHORT

| Rank | Company | OKX | 24h | 7d | 50/50 move | Base SHORT | Timing adj. | Final | Signal | Prev. SHORT? |
|---:|---|---|---:|---:|---:|---:|---:|---:|---|---|
| 1 | Rocket Lab Corporation | RKLB | -0.0% | 8.6% | 4.3% | 100 | +3 | **100** | **CORE** | yes |
| 2 | USA Rare Earth, Inc. | USAR | 0.0% | 1.7% | 0.8% | 100 | +1 | **100** | **CORE** | yes |
| 3 | IonQ, Inc. | IONQ | -0.0% | 2.1% | 1.0% | 88 | +1 | **89** | **CORE** | yes |
| 4 | Nebius Group N.V. | NBIS | -0.0% | -0.6% | -0.3% | 84 | +0 | **84** | **CORE** | yes |
| 5 | Cerebras Systems Inc. | CBRS | 0.0% | 1.1% | 0.6% | 82 | +0 | **82** | **CORE** | yes |
| 6 | AST SpaceMobile, Inc. | ASTS | 0.0% | 2.6% | 1.3% | 80 | +1 | **81** | **CORE** | yes |
| 7 | Moderna, Inc. | MRNA | -0.0% | -15.4% | -7.7% | 72 | -6 | **66** | **WATCH** | yes |
| 8 | Okta, Inc. | OKTA | -0.0% | 8.4% | 4.2% | 61 | +3 | **64** | **WATCH** | yes |
| 9 | Tesla, Inc. | TSLA | 0.0% | 5.4% | 2.7% | 59 | +2 | **61** | **WATCH** | yes |
| 10 | Lumentum Holdings Inc. | LITE | 0.0% | 1.8% | 0.9% | 59 | +1 | **60** | **WATCH** | yes |

## Combined model — LONG

Weighted score: **70% fundamental + 30% P/E trend**.

| Rank | Company | OKX | Fundamental LONG | P/E trend LONG | Combined | Signal |
|---:|---|---|---:|---:|---:|---|
| 1 | Taiwan Semiconductor Manufactur | `TSM` | 90 | 85 | **88** | **CORE** |
| 2 | Applovin Corporation | `APP` | 83 | 80 | **82** | **CORE** |
| 3 | Sandisk Corporation | `SNDK` | 82 | 82 | **82** | **CORE** |
| 4 | Credo Technology Group Holding  | `CRDO` | 75 | 100 | **82** | **CORE** |
| 5 | NVIDIA Corporation | `NVDA` | 75 | 100 | **82** | **CORE** |
| 6 | Broadcom Inc. | `AVGO` | 75 | 100 | **82** | **CORE** |
| 7 | Applied Materials, Inc. | `AMAT` | 77 | 91 | **81** | **CORE** |
| 8 | Robinhood Markets, Inc. | `HOOD` | 77 | 86 | **80** | **CORE** |
| 9 | Corning Incorporated | `GLW` | 77 | 86 | **80** | **CORE** |
| 10 | Marvell Technology, Inc. | `MRVL` | 70 | 100 | **79** | **CORE** |

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
| 1 | Credo Technology Group Holding  | `CRDO` | 59.4 | 17.2 | -71.0% | 53.9% | 55.0% | decelerating | **100** | **CORE** |
| 2 | NVIDIA Corporation | `NVDA` | 27.6 | 13.7 | -50.3% | 70.9% | 68.2% | decelerating | **100** | **CORE** |
| 3 | Broadcom Inc. | `AVGO` | 43.7 | 17.6 | -59.7% | 66.9% | 64.4% | decelerating | **100** | **CORE** |
| 4 | Marvell Technology, Inc. | `MRVL` | 80.1 | 33.2 | -58.5% | 73.7% | 63.3% | accelerating | **100** | **CORE** |
| 5 | Advanced Micro Devices, Inc. | `AMD` | 142.9 | 35.6 | -75.1% | 107.6% | 74.9% | accelerating | **100** | **CORE** |
| 6 | AXT Inc | `AXT` | 1455.8 | 25.9 | -98.2% | 159.2% | 111.3% | decelerating | **96** | **CORE** |
| 7 | Oracle Corporation | `ORCL` | 20.5 | 11.9 | -42.0% | 35.0% | 45.7% | accelerating | **95** | **CORE** |
| 8 | Coherent Corp. | `COHR` | 57.2 | 17.0 | -70.4% | 48.2% | 38.1% | decelerating | **95** | **CORE** |
| 9 | Arm Holdings plc | `ARM` | 233.6 | 73.9 | -68.4% | 37.5% | 36.4% | accelerating | **95** | **CORE** |
| 10 | Bloom Energy Corporation | `BE` | 287.5 | 44.2 | -84.6% | 62.7% | 56.0% | decelerating | **92** | **CORE** |

## P/E Expansion + Weakening — SHORT

| Rank | Company | OKX | Trail P/E | Fwd P/E | P/E change | EPS +1y | Rev +1y | Rev trend | SHORT score | Signal |
|---:|---|---|---:|---:|---:|---:|---:|---|---:|---|
| 1 | SOFTBANK GROUP CORP | `SOFTBANK` | 5.4 | 15.9 | 191.0% | -14.5% | 6.9% | decelerating | **86** | **CORE** |
| 2 | Hyperliquid Strategies Inc | `PURR` | 3.1 | 26.6 | 767.6% | 51.0% | 31.4% | decelerating | **55** | **WATCH** |
| 3 | Amazon.com, Inc. | `AMZN` | 20.4 | 24.3 | 19.1% | -18.3% | 14.6% | decelerating | **52** | **WATCH** |
| 4 | Alphabet Inc. | `GOOGL` | 16.1 | 20.9 | 29.8% | -26.4% | 25.5% | accelerating | **50** | **WATCH** |

## Top SHORT candidates

| Rank | Company | OKX market | SHORT score | Signal | P/S | EV/S | Op margin | Fwd P/E | Rev +1y | FCF yield |
|---:|---|---|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Rocket Lab Corporation | `RKLB-USDT-SWAP` | **100** | **CORE** | 48.5 | 42.5 | -24.6% | 1014.3 | 38.2% | -0.7% |
| 2 | USA Rare Earth, Inc. | `USAR-USDT-SWAP` | **100** | **CORE** | 296.4 | 78.1 | -795.6% | 346.7 | 870.1% | -7.3% |
| 3 | IonQ, Inc. | `IONQ-USDT-SWAP` | **88** | **CORE** | 57.4 | 42.6 | -408.2% | -24.5 | 77.6% | -0.6% |
| 4 | Nebius Group N.V. | `NBIS-USDT-SWAP` | **84** | **WATCH** | 31.9 | 36.1 | -0.2% | -47.4 | 266.0% | -22.2% |
| 5 | Cerebras Systems Inc. | `CBRS-USDT-SWAP` | **82** | **WATCH** | 41.6 | 32.2 | -265.0% | 93.7 | 232.7% | — |
| 6 | Okta, Inc. | `OKTA-USDT-SWAP` | **80** | **CORE** | 12.9 | 12.1 | 13.3% | 51.6 | 10.1% | 2.6% |
| 7 | AST SpaceMobile, Inc. | `ASTS-USDT-SWAP` | **80** | **WATCH** | 141.6 | 119.6 | -544.6% | -32.6 | 264.2% | -11.0% |
| 8 | Tesla, Inc. | `TSLA-USDT-SWAP` | **78** | **WATCH** | 15.6 | 15.3 | 5.4% | 189.0 | 13.5% | 0.3% |
| 9 | Moderna, Inc. | `MRNA-USDT-SWAP` | **72** | **WATCH** | 37.3 | 35.5 | -557.9% | -45.5 | 16.3% | 0.4% |

## Top LONG candidates

| Rank | Company | OKX market | LONG score | Signal | P/S | EV/S | Op margin | Fwd P/E | Rev +1y | FCF yield |
|---:|---|---|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Taiwan Semiconductor Manufactur | `TSM-USDT-SWAP` | **90** | **CORE** | 0.5 | 3.0 | 58.7% | 18.7 | 37.6% | 53.1% |
| 2 | Applovin Corporation | `APP-USDT-SWAP` | **83** | **CORE** | 12.9 | 12.9 | 77.7% | 12.8 | 25.7% | 3.6% |
| 3 | Sandisk Corporation | `SNDK-USDT-SWAP` | **82** | **CORE** | 9.3 | 9.2 | 78.5% | 4.9 | 18.9% | 4.1% |
| 4 | Corning Incorporated | `GLW-USDT-SWAP` | **77** | **WATCH** | 6.1 | 6.8 | 18.8% | 28.4 | 20.7% | 0.8% |
| 5 | Robinhood Markets, Inc. | `HOOD-USDT-SWAP` | **77** | **WATCH** | 17.2 | 17.1 | 43.9% | 28.1 | 28.8% | — |
| 6 | Applied Materials, Inc. | `AMAT-USDT-SWAP` | **77** | **WATCH** | 10.2 | 10.1 | 33.7% | 21.4 | 35.3% | 1.0% |
| 7 | Credo Technology Group Holding  | `CRDO-USDT-SWAP` | **75** | **WATCH** | 19.8 | 19.3 | 25.2% | 17.2 | 55.0% | 0.8% |
| 8 | Broadcom Inc. | `AVGO-USDT-SWAP` | **75** | **WATCH** | 18.3 | 18.7 | 54.3% | 17.6 | 64.4% | 1.9% |
| 9 | Micron Technology, Inc. | `MU-USDT-SWAP` | **75** | **CORE** | 7.9 | 7.6 | 80.7% | 4.5 | 15.7% | 2.8% |
| 10 | NVIDIA Corporation | `NVDA-USDT-SWAP` | **75** | **WATCH** | 17.4 | 17.3 | 66.2% | 13.7 | 68.2% | 0.8% |

## Analyst consensus (12-month price target) — most upside

| Rank | Company | OKX | Price | Analyst mean target | Gap | Analysts | Currency |
|---:|---|---|---:|---:|---:|---:|---|
| 1 | IREN LIMITED | `IREN` | 27.44 | 77.81 | **183.5%** | 18 | USD |
| 2 | Cerebras Systems Inc. | `CBRS` | 119.31 | 282.55 | **136.8%** | 11 | USD |
| 3 | Hyperliquid Strategies Inc | `PURR` | 9.85 | 22.32 | **126.6%** | 4 | USD |
| 4 | CoreWeave, Inc. | `CRWV` | 59.57 | 134.58 | **125.9%** | 38 | USD |
| 5 | BitMine Immersion Technologies, | `BMNR` | 21.62 | 45.87 | **112.1%** | 3 | USD |
| 6 | SK hynix | `SKHYNIX` | 1487000.00 | 3096288.00 | **108.2%** | 38 | KRW |
| 7 | Applied Optoelectronics, Inc. | `AAOI` | 76.95 | 156.00 | **102.7%** | 5 | USD |
| 8 | SamsungElec | `SAMSUNG` | 242000.00 | 478905.62 | **97.9%** | 36 | KRW |
| 9 | IonQ, Inc. | `IONQ` | 32.95 | 64.06 | **94.4%** | 14 | USD |
| 10 | Oracle Corporation | `ORCL` | 130.53 | 235.80 | **80.7%** | 41 | USD |
| 11 | Applovin Corporation | `APP` | 262.82 | 471.69 | **79.5%** | 31 | USD |
| 12 | AST SpaceMobile, Inc. | `ASTS` | 41.96 | 74.68 | **78.0%** | 12 | USD |
| 13 | Rocket Lab Corporation | `RKLB` | 58.31 | 102.15 | **75.2%** | 20 | USD |
| 14 | Credo Technology Group Holding  | `CRDO` | 167.43 | 284.05 | **69.7%** | 19 | USD |
| 15 | Strategy Inc | `MSTR` | 141.40 | 239.27 | **69.2%** | 15 | USD |

## Analyst consensus (12-month price target) — most downside

| Rank | Company | OKX | Price | Analyst mean target | Gap | Analysts | Currency |
|---:|---|---|---:|---:|---:|---:|---|
| 1 | Moderna, Inc. | `MRNA` | 207.97 | 138.37 | **-33.5%** | 19 | USD |
| 2 | Okta, Inc. | `OKTA` | 226.07 | 214.72 | **-5.0%** | 43 | USD |
| 3 | Apple Inc. | `AAPL` | 347.10 | 330.02 | **-4.9%** | 39 | USD |

Price/target uses the underlying Yahoo Finance share quote, not the OKX derivative. Minimum 3 analysts; unreliable price scales and missing coverage excluded. Targets are analyst opinions, not guaranteed forecasts.

## All OKX companies — our ratio + LONG/SHORT scores

| Company | OKX | P/S | EV/S | Op margin | Fwd P/E | EPS +1y | Rev +1y | FCF yield | LONG | SHORT |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Rocket Lab Corporation | `RKLB` | 48.5 | 42.5 | -24.6% | 1014.3 | 66.8% | 38.2% | -0.7% | **0** | **100 CORE** |
| USA Rare Earth, Inc. | `USAR` | 296.4 | 78.1 | -795.6% | 346.7 | 105.3% | 870.1% | -7.3% | **0** | **100 CORE** |
| Taiwan Semiconductor Manufactur | `TSM` | 0.5 | 3.0 | 58.7% | 18.7 | 33.6% | 37.6% | 53.1% | **90 CORE** | **10** |
| IonQ, Inc. | `IONQ` | 57.4 | 42.6 | -408.2% | -24.5 | 21.3% | 77.6% | -0.6% | **0** | **88 CORE** |
| Nebius Group N.V. | `NBIS` | 31.9 | 36.1 | -0.2% | -47.4 | -191.4% | 266.0% | -22.2% | **0** | **84 WATCH** |
| Applovin Corporation | `APP` | 12.9 | 12.9 | 77.7% | 12.8 | 26.8% | 25.7% | 3.6% | **83 CORE** | **10** |
| Sandisk Corporation | `SNDK` | 9.3 | 9.2 | 78.5% | 4.9 | 24.0% | 18.9% | 4.1% | **82 CORE** | **10** |
| Cerebras Systems Inc. | `CBRS` | 41.6 | 32.2 | -265.0% | 93.7 | 371.3% | 232.7% | — | **0** | **82 WATCH** |
| Okta, Inc. | `OKTA` | 12.9 | 12.1 | 13.3% | 51.6 | 11.4% | 10.1% | 2.6% | **8** | **80 CORE** |
| AST SpaceMobile, Inc. | `ASTS` | 141.6 | 119.6 | -544.6% | -32.6 | 44.3% | 264.2% | -11.0% | **0** | **80 WATCH** |
| Tesla, Inc. | `TSLA` | 15.6 | 15.3 | 5.4% | 189.0 | 23.8% | 13.5% | 0.3% | **12** | **78 WATCH** |
| Robinhood Markets, Inc. | `HOOD` | 17.2 | 17.1 | 43.9% | 28.1 | 36.5% | 28.8% | — | **77 WATCH** | **5** |
| Corning Incorporated | `GLW` | 6.1 | 6.8 | 18.8% | 28.4 | 33.4% | 20.7% | 0.8% | **77 WATCH** | **13** |
| Applied Materials, Inc. | `AMAT` | 10.2 | 10.1 | 33.7% | 21.4 | 44.6% | 35.3% | 1.0% | **77 WATCH** | **3** |
| Credo Technology Group Holding  | `CRDO` | 19.8 | 19.3 | 25.2% | 17.2 | 53.9% | 55.0% | 0.8% | **75 WATCH** | **28** |
| NVIDIA Corporation | `NVDA` | 17.4 | 17.3 | 66.2% | 13.7 | 70.9% | 68.2% | 0.8% | **75 WATCH** | **18** |
| Broadcom Inc. | `AVGO` | 18.3 | 18.7 | 54.3% | 17.6 | 66.9% | 64.4% | 1.9% | **75 WATCH** | **28** |
| Micron Technology, Inc. | `MU` | 7.9 | 7.6 | 80.7% | 4.5 | 17.2% | 15.7% | 2.8% | **75 CORE** | **30** |
| Western Digital Corporation | `WDC` | 9.8 | 9.8 | 47.7% | 9.4 | 63.4% | 40.5% | 1.9% | **75 WATCH** | **18** |
| Moderna, Inc. | `MRNA` | 37.3 | 35.5 | -557.9% | -45.5 | 42.5% | 16.3% | 0.4% | **0** | **72 WATCH** |
| Marvell Technology, Inc. | `MRVL` | 23.2 | 22.7 | 16.7% | 33.2 | 73.7% | 63.3% | 1.1% | **70 WATCH** | **13** |
| Advanced Micro Devices, Inc. | `AMD` | 22.1 | 21.9 | 17.2% | 35.6 | 107.6% | 74.9% | 1.0% | **70 WATCH** | **13** |
| Oracle Corporation | `ORCL` | 5.5 | 7.4 | 35.6% | 11.9 | 35.0% | 45.7% | -11.6% | **70 WATCH** | **10** |
| XIAOMI-W | `XIAOMI` | 1.5 | 1.3 | 4.0% | 17.0 | 36.8% | 19.7% | -1.3% | **70 WATCH** | **10** |
| Adobe Inc. | `ADBE` | 3.7 | 3.8 | 34.8% | 9.0 | 12.4% | 9.1% | 9.7% | **65 WATCH** | **30** |
| Coherent Corp. | `COHR` | 6.5 | 6.8 | 11.8% | 17.0 | 48.2% | 38.1% | -1.4% | **60 WATCH** | **35** |
| IREN LIMITED | `IREN` | 15.7 | 18.0 | -102.5% | -6.9 | -16.4% | 164.0% | -38.0% | **0** | **60** |
| Microsoft Corporation | `MSFT` | 11.9 | 12.0 | 45.1% | 22.4 | 19.9% | 19.7% | 0.4% | **59 WATCH** | **23** |
| Lumentum Holdings Inc. | `LITE` | 26.0 | 25.4 | 28.0% | 24.3 | 63.9% | 57.6% | 0.3% | **0** | **59** |
| Apple Inc. | `AAPL` | 10.9 | 10.9 | 32.6% | 36.3 | 8.4% | 10.4% | 2.1% | **5** | **58** |
| Coca-Cola Company (The) | `KO` | 7.7 | 8.2 | 33.4% | 25.9 | 5.7% | -2.2% | 1.1% | **0** | **58** |
| Dell Technologies Inc. | `DELL` | 2.1 | 2.3 | 12.0% | 16.6 | 16.2% | 19.2% | 1.9% | **57 WATCH** | **38** |
| Meta Platforms, Inc. | `META` | 6.7 | 6.7 | 35.4% | 17.6 | 16.4% | 21.6% | 1.0% | **57 WATCH** | **38** |
| Bloom Energy Corporation | `BE` | 16.9 | 17.0 | 18.5% | 44.2 | 62.7% | 56.0% | -0.0% | **40** | **55** |
| AXT Inc | `AXT` | 30.4 | 27.8 | 21.9% | 25.9 | 159.2% | 111.3% | -1.2% | **52** | **35** |
| Super Micro Computer, Inc. | `SMCI` | 0.6 | 0.7 | 13.4% | 6.3 | 19.7% | 16.3% | -36.3% | **52** | **45** |
| Netflix, Inc. | `NFLX` | 5.2 | 5.3 | 34.6% | 16.6 | 5.1% | 10.7% | 9.8% | **35** | **50** |
| Palantir Technologies Inc. | `PLTR` | 77.6 | 76.1 | 47.1% | 84.5 | 44.7% | 50.4% | 0.5% | **33** | **48** |
| Intel Corporation | `INTC` | 8.7 | 8.9 | 12.2% | 43.1 | 41.6% | 15.8% | 1.0% | **10** | **48** |
| SK hynix | `SKHYNIX` | 5.5 | 4.7 | 76.3% | 3.2 | 31.6% | 54.3% | 5.3% | **45** | **5** |
| SK hynix | `SKHY` | 5.5 | 4.7 | 76.3% | 3.2 | 31.6% | 54.3% | 5.3% | **45** | **5** |
| SamsungElec | `SAMSUNG` | 3.2 | 2.7 | 52.2% | 3.3 | 51.5% | 38.3% | 4.4% | **45** | **10** |
| Arm Holdings plc | `ARM` | 46.9 | 46.3 | 7.6% | 73.9 | 37.5% | 36.4% | 0.6% | **43** | **33** |
| Coinbase Global, Inc. | `COIN` | 7.0 | 6.7 | -13.9% | 52.4 | 283.2% | 30.0% | 6.3% | **20** | **40** |
| SOFTBANK GROUP CORP | `SOFTBANK` | 3.3 | 6.5 | -11.6% | 15.9 | -14.5% | 6.9% | -8.2% | **0** | **40** |
| CoreWeave, Inc. | `CRWV` | 4.3 | 10.4 | -1.9% | -30.3 | 9.7% | 105.6% | -27.7% | **0** | **40** |
| Amazon.com, Inc. | `AMZN` | 3.5 | 3.7 | 13.7% | 24.3 | -18.3% | 14.6% | 0.1% | **0** | **38** |
| Circle Internet Group, Inc. | `CRCL` | 7.1 | 6.5 | 4.9% | 55.2 | 27.1% | 26.7% | 1.0% | **35** | **33** |
| Fluence Energy, Inc. | `FLNC` | 0.4 | 0.4 | -8.9% | -11.3 | 59.3% | 25.4% | 0.2% | **5** | **28** |
| Hyperliquid Strategies Inc | `PURR` | 289.7 | 191.4 | 9595.1% | 26.6 | 51.0% | 31.4% | — | **25** | **10** |
| BitMine Immersion Technologies, | `BMNR` | 213.1 | 207.6 | 8.4% | 23.0 | 103.2% | 421.8% | -4.0% | **25** | **25** |
| Strategy Inc | `MSTR` | 120.2 | 146.7 | -6808.1% | 6.0 | 168.0% | 2.5% | -37.7% | **25** | **25** |
| QUALCOMM Incorporated | `QCOM` | 4.5 | 4.5 | 18.5% | 18.1 | -2.8% | 4.6% | 5.2% | **25** | **15** |
| Applied Optoelectronics, Inc. | `AAOI` | 11.0 | 10.6 | -12.9% | 16.7 | 576.8% | 156.5% | -13.6% | **10** | **25** |
| Alphabet Inc. | `GOOGL` | 8.8 | 8.6 | 34.0% | 20.9 | -26.4% | 25.5% | 0.6% | **12** | **23** |

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
