# OKX Long / Short Fundamental Scanner

Hourly scanner restricted to public companies exposed by the **OKX EEA TradFi / Stock Perpetual API universe**.

**Last scan:** 2026-10-26 14:21 UTC  
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
| 1 | Taiwan Semiconductor Manufactur | TSM | 0.9% | 0.4% | 0.6% | 88 | -1 | **87** | **CORE** | yes |
| 2 | Credo Technology Group Holding  | CRDO | 0.8% | -14.1% | -6.7% | 82 | +5 | **87** | **CORE** | yes |
| 3 | Corning Incorporated | GLW | 0.4% | -6.4% | -3.0% | 83 | +2 | **85** | **CORE** | yes |
| 4 | Sandisk Corporation | SNDK | 0.8% | -9.0% | -4.1% | 82 | +3 | **85** | **CORE** | yes |
| 5 | Applovin Corporation | APP | -0.1% | -3.4% | -1.7% | 82 | +1 | **83** | **CORE** | yes |
| 6 | Applied Materials, Inc. | AMAT | 1.4% | -7.4% | -3.0% | 81 | +2 | **83** | **CORE** | yes |
| 7 | NVIDIA Corporation | NVDA | 1.9% | -0.9% | 0.5% | 82 | +0 | **82** | **CORE** | yes |
| 8 | Broadcom Inc. | AVGO | 1.4% | -2.5% | -0.6% | 82 | +0 | **82** | **CORE** | yes |
| 9 | Robinhood Markets, Inc. | HOOD | -2.1% | -3.6% | -2.9% | 80 | +2 | **82** | **CORE** | yes |
| 10 | Marvell Technology, Inc. | MRVL | -0.2% | -3.8% | -2.0% | 79 | +2 | **81** | **CORE** | yes |

## Final model + Price Timing — SHORT

| Rank | Company | OKX | 24h | 7d | 50/50 move | Base SHORT | Timing adj. | Final | Signal | Prev. SHORT? |
|---:|---|---|---:|---:|---:|---:|---:|---:|---|---|
| 1 | Rocket Lab Corporation | RKLB | 2.2% | 4.6% | 3.4% | 100 | +3 | **100** | **CORE** | yes |
| 2 | USA Rare Earth, Inc. | USAR | -2.0% | -9.4% | -5.7% | 100 | -5 | **95** | **CORE** | yes |
| 3 | IonQ, Inc. | IONQ | -2.0% | -0.4% | -1.2% | 88 | -1 | **87** | **CORE** | yes |
| 4 | Nebius Group N.V. | NBIS | -2.8% | -9.4% | -6.1% | 84 | -5 | **79** | **CORE** | yes |
| 5 | AST SpaceMobile, Inc. | ASTS | -0.4% | -5.3% | -2.9% | 80 | -2 | **78** | **CORE** | yes |
| 6 | Cerebras Systems Inc. | CBRS | -2.1% | -10.1% | -6.1% | 75 | -5 | **70** | **WATCH** | yes |
| 7 | Moderna, Inc. | MRNA | 1.3% | -10.7% | -4.7% | 72 | -4 | **68** | **WATCH** | yes |
| 8 | Okta, Inc. | OKTA | 2.9% | 15.4% | 9.1% | 61 | +7 | **68** | **WATCH** | yes |
| 9 | Tesla, Inc. | TSLA | 6.1% | 7.3% | 6.7% | 59 | +5 | **64** | **WATCH** | yes |

## Combined model — LONG

Weighted score: **70% fundamental + 30% P/E trend**.

| Rank | Company | OKX | Fundamental LONG | P/E trend LONG | Combined | Signal |
|---:|---|---|---:|---:|---:|---|
| 1 | Taiwan Semiconductor Manufactur | `TSM` | 90 | 85 | **88** | **CORE** |
| 2 | Corning Incorporated | `GLW` | 77 | 96 | **83** | **CORE** |
| 3 | Applovin Corporation | `APP` | 83 | 80 | **82** | **CORE** |
| 4 | Sandisk Corporation | `SNDK` | 82 | 82 | **82** | **CORE** |
| 5 | Credo Technology Group Holding  | `CRDO` | 75 | 100 | **82** | **CORE** |
| 6 | NVIDIA Corporation | `NVDA` | 75 | 100 | **82** | **CORE** |
| 7 | Broadcom Inc. | `AVGO` | 75 | 100 | **82** | **CORE** |
| 8 | Applied Materials, Inc. | `AMAT` | 77 | 91 | **81** | **CORE** |
| 9 | Robinhood Markets, Inc. | `HOOD` | 77 | 86 | **80** | **CORE** |
| 10 | Marvell Technology, Inc. | `MRVL` | 70 | 100 | **79** | **CORE** |

## Combined model — SHORT

Weighted score: **70% fundamental + 30% P/E trend**.

| Rank | Company | OKX | Fundamental SHORT | P/E trend SHORT | Combined | Signal |
|---:|---|---|---:|---:|---:|---|
| 1 | Rocket Lab Corporation | `RKLB` | 100 | 0 | **100** | **CORE** |
| 2 | USA Rare Earth, Inc. | `USAR` | 100 | 0 | **100** | **CORE** |
| 3 | IonQ, Inc. | `IONQ` | 88 | 0 | **88** | **CORE** |
| 4 | Nebius Group N.V. | `NBIS` | 84 | 0 | **84** | **WATCH** |
| 5 | AST SpaceMobile, Inc. | `ASTS` | 80 | 0 | **80** | **WATCH** |
| 6 | Cerebras Systems Inc. | `CBRS` | 75 | 0 | **75** | **WATCH** |
| 7 | Moderna, Inc. | `MRNA` | 72 | 0 | **72** | **WATCH** |
| 8 | Okta, Inc. | `OKTA` | 80 | 18 | **61** | **WATCH** |
| 9 | Tesla, Inc. | `TSLA` | 78 | 15 | **59** | **WATCH** |

## P/E Compression + Growth — LONG

| Rank | Company | OKX | Trail P/E | Fwd P/E | P/E change | EPS +1y | Rev +1y | Rev trend | LONG score | Signal |
|---:|---|---|---:|---:|---:|---:|---:|---|---:|---|
| 1 | Credo Technology Group Holding  | `CRDO` | 52.6 | 15.3 | -71.0% | 53.9% | 55.0% | decelerating | **100** | **CORE** |
| 2 | NVIDIA Corporation | `NVDA` | 27.2 | 13.5 | -50.3% | 70.9% | 68.2% | decelerating | **100** | **CORE** |
| 3 | Broadcom Inc. | `AVGO` | 41.6 | 16.8 | -59.7% | 66.7% | 64.3% | decelerating | **100** | **CORE** |
| 4 | Marvell Technology, Inc. | `MRVL` | 75.0 | 31.1 | -58.5% | 73.7% | 63.3% | accelerating | **100** | **CORE** |
| 5 | Advanced Micro Devices, Inc. | `AMD` | 132.5 | 32.9 | -75.1% | 107.7% | 74.9% | accelerating | **100** | **CORE** |
| 6 | Corning Incorporated | `GLW` | 57.0 | 28.3 | -50.4% | 33.6% | 20.0% | accelerating | **96** | **CORE** |
| 7 | AXT Inc | `AXT` | 1345.1 | 23.9 | -98.2% | 159.2% | 111.3% | decelerating | **96** | **CORE** |
| 8 | Oracle Corporation | `ORCL` | 19.8 | 11.5 | -41.9% | 35.0% | 45.7% | accelerating | **95** | **CORE** |
| 9 | Coherent Corp. | `COHR` | 51.7 | 15.3 | -70.4% | 48.3% | 38.3% | decelerating | **95** | **CORE** |
| 10 | Arm Holdings plc | `ARM` | 222.1 | 70.2 | -68.4% | 37.5% | 36.4% | accelerating | **95** | **CORE** |

## P/E Expansion + Weakening — SHORT

| Rank | Company | OKX | Trail P/E | Fwd P/E | P/E change | EPS +1y | Rev +1y | Rev trend | SHORT score | Signal |
|---:|---|---|---:|---:|---:|---:|---:|---|---:|---|
| 1 | SOFTBANK GROUP CORP | `SOFTBANK` | 5.0 | 14.4 | 191.0% | -14.5% | 6.9% | decelerating | **86** | **CORE** |
| 2 | Hyperliquid Strategies Inc | `PURR` | 2.8 | 24.5 | 767.6% | 51.0% | 31.4% | decelerating | **55** | **WATCH** |
| 3 | Amazon.com, Inc. | `AMZN` | 20.1 | 24.0 | 19.2% | -18.2% | 14.6% | decelerating | **52** | **WATCH** |
| 4 | Alphabet Inc. | `GOOGL` | 16.1 | 20.9 | 29.8% | -26.6% | 25.3% | accelerating | **50** | **WATCH** |

## Top SHORT candidates

| Rank | Company | OKX market | SHORT score | Signal | P/S | EV/S | Op margin | Fwd P/E | Rev +1y | FCF yield |
|---:|---|---|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Rocket Lab Corporation | `RKLB-USDT-SWAP` | **100** | **CORE** | 44.7 | 38.1 | -24.6% | 934.9 | 38.2% | -0.7% |
| 2 | USA Rare Earth, Inc. | `USAR-USDT-SWAP` | **100** | **CORE** | 260.5 | 58.2 | -795.6% | 304.7 | 870.1% | -8.3% |
| 3 | IonQ, Inc. | `IONQ-USDT-SWAP` | **88** | **CORE** | 53.4 | 40.0 | -408.2% | -22.8 | 77.6% | -0.7% |
| 4 | Nebius Group N.V. | `NBIS-USDT-SWAP` | **84** | **WATCH** | 30.9 | 33.7 | -0.2% | -42.9 | 266.0% | -22.9% |
| 5 | Okta, Inc. | `OKTA-USDT-SWAP` | **80** | **CORE** | 12.5 | 11.4 | 13.3% | 50.1 | 10.1% | 2.7% |
| 6 | AST SpaceMobile, Inc. | `ASTS-USDT-SWAP` | **80** | **WATCH** | 133.8 | 113.9 | -544.6% | -30.8 | 264.2% | -11.7% |
| 7 | Tesla, Inc. | `TSLA-USDT-SWAP` | **78** | **WATCH** | 15.1 | 13.9 | 2.6% | 181.5 | 13.5% | 0.3% |
| 8 | Cerebras Systems Inc. | `CBRS-USDT-SWAP` | **75** | **WATCH** | 37.9 | 29.2 | -265.0% | 85.2 | 232.7% | — |
| 9 | Moderna, Inc. | `MRNA-USDT-SWAP` | **72** | **WATCH** | 36.3 | 34.1 | -557.9% | -44.4 | 16.3% | 0.4% |

## Top LONG candidates

| Rank | Company | OKX market | LONG score | Signal | P/S | EV/S | Op margin | Fwd P/E | Rev +1y | FCF yield |
|---:|---|---|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Taiwan Semiconductor Manufactur | `TSM-USDT-SWAP` | **90** | **CORE** | 0.4 | 2.9 | 58.7% | 18.0 | 37.5% | 55.0% |
| 2 | Applovin Corporation | `APP-USDT-SWAP` | **83** | **CORE** | 12.8 | 12.8 | 77.7% | 12.7 | 25.7% | 3.6% |
| 3 | Sandisk Corporation | `SNDK-USDT-SWAP` | **82** | **CORE** | 8.9 | 8.7 | 78.5% | 4.7 | 18.9% | 4.3% |
| 4 | Corning Incorporated | `GLW-USDT-SWAP` | **77** | **WATCH** | 6.3 | 6.7 | 15.6% | 28.3 | 20.0% | 0.7% |
| 5 | Robinhood Markets, Inc. | `HOOD-USDT-SWAP` | **77** | **WATCH** | 17.0 | 17.1 | 43.9% | 27.2 | 29.3% | — |
| 6 | Applied Materials, Inc. | `AMAT-USDT-SWAP` | **77** | **WATCH** | 9.8 | 9.6 | 33.7% | 20.7 | 35.3% | 1.0% |
| 7 | Credo Technology Group Holding  | `CRDO-USDT-SWAP` | **75** | **WATCH** | 17.5 | 16.9 | 25.2% | 15.3 | 55.0% | 0.9% |
| 8 | Broadcom Inc. | `AVGO-USDT-SWAP` | **75** | **WATCH** | 17.5 | 17.6 | 54.3% | 16.8 | 64.3% | 2.0% |
| 9 | Micron Technology, Inc. | `MU-USDT-SWAP` | **75** | **CORE** | 7.6 | 7.2 | 80.7% | 4.3 | 15.7% | 2.9% |
| 10 | NVIDIA Corporation | `NVDA-USDT-SWAP` | **75** | **WATCH** | 17.1 | 16.7 | 66.2% | 13.5 | 68.2% | 0.8% |

## Analyst consensus (12-month price target) — most upside

| Rank | Company | OKX | Price | Analyst mean target | Gap | Analysts | Currency |
|---:|---|---|---:|---:|---:|---:|---|
| 1 | Cerebras Systems Inc. | `CBRS` | 108.48 | 282.55 | **160.5%** | 11 | USD |
| 2 | CoreWeave, Inc. | `CRWV` | 55.08 | 135.82 | **146.6%** | 38 | USD |
| 3 | Hyperliquid Strategies Inc | `PURR` | 9.07 | 22.32 | **146.1%** | 4 | USD |
| 4 | SK hynix | `SKHYNIX` | 1275000.00 | 3096288.00 | **142.8%** | 38 | KRW |
| 5 | Applied Optoelectronics, Inc. | `AAOI` | 68.20 | 160.00 | **134.6%** | 5 | USD |
| 6 | SamsungElec | `SAMSUNG` | 213000.00 | 478905.62 | **124.8%** | 36 | KRW |
| 7 | BitMine Immersion Technologies, | `BMNR` | 21.86 | 45.87 | **109.8%** | 3 | USD |
| 8 | IonQ, Inc. | `IONQ` | 30.66 | 64.06 | **109.0%** | 14 | USD |
| 9 | Credo Technology Group Holding  | `CRDO` | 148.40 | 284.05 | **91.4%** | 19 | USD |
| 10 | Rocket Lab Corporation | `RKLB` | 53.74 | 102.15 | **90.1%** | 20 | USD |
| 11 | AST SpaceMobile, Inc. | `ASTS` | 39.63 | 74.68 | **88.5%** | 12 | USD |
| 12 | Oracle Corporation | `ORCL` | 126.56 | 236.54 | **86.9%** | 41 | USD |
| 13 | Coherent Corp. | `COHR` | 212.91 | 394.79 | **85.4%** | 24 | USD |
| 14 | SOFTBANK GROUP CORP | `SOFTBANK` | 4263.00 | 7782.47 | **82.6%** | 18 | JPY |
| 15 | Nebius Group N.V. | `NBIS` | 154.24 | 281.00 | **82.2%** | 20 | USD |

## Analyst consensus (12-month price target) — most downside

| Rank | Company | OKX | Price | Analyst mean target | Gap | Analysts | Currency |
|---:|---|---|---:|---:|---:|---:|---|
| 1 | Moderna, Inc. | `MRNA` | 202.69 | 138.37 | **-31.7%** | 19 | USD |
| 2 | Apple Inc. | `AAPL` | 345.20 | 329.25 | **-4.6%** | 39 | USD |
| 3 | Okta, Inc. | `OKTA` | 219.20 | 214.72 | **-2.0%** | 43 | USD |

Price/target uses the underlying Yahoo Finance share quote, not the OKX derivative. Minimum 3 analysts; unreliable price scales and missing coverage excluded. Targets are analyst opinions, not guaranteed forecasts.

## All OKX companies — our ratio + LONG/SHORT scores

| Company | OKX | P/S | EV/S | Op margin | Fwd P/E | EPS +1y | Rev +1y | FCF yield | LONG | SHORT |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Rocket Lab Corporation | `RKLB` | 44.7 | 38.1 | -24.6% | 934.9 | 66.8% | 38.2% | -0.7% | **0** | **100 CORE** |
| USA Rare Earth, Inc. | `USAR` | 260.5 | 58.2 | -795.6% | 304.7 | 105.3% | 870.1% | -8.3% | **0** | **100 CORE** |
| Taiwan Semiconductor Manufactur | `TSM` | 0.4 | 2.9 | 58.7% | 18.0 | 33.6% | 37.5% | 55.0% | **90 CORE** | **10** |
| IonQ, Inc. | `IONQ` | 53.4 | 40.0 | -408.2% | -22.8 | 21.3% | 77.6% | -0.7% | **0** | **88 CORE** |
| Nebius Group N.V. | `NBIS` | 30.9 | 33.7 | -0.2% | -42.9 | -191.4% | 266.0% | -22.9% | **0** | **84 WATCH** |
| Applovin Corporation | `APP` | 12.8 | 12.8 | 77.7% | 12.7 | 26.8% | 25.7% | 3.6% | **83 CORE** | **10** |
| Sandisk Corporation | `SNDK` | 8.9 | 8.7 | 78.5% | 4.7 | 24.0% | 18.9% | 4.3% | **82 CORE** | **10** |
| Okta, Inc. | `OKTA` | 12.5 | 11.4 | 13.3% | 50.1 | 11.4% | 10.1% | 2.7% | **8** | **80 CORE** |
| AST SpaceMobile, Inc. | `ASTS` | 133.8 | 113.9 | -544.6% | -30.8 | 44.3% | 264.2% | -11.7% | **0** | **80 WATCH** |
| Tesla, Inc. | `TSLA` | 15.1 | 13.9 | 2.6% | 181.5 | 22.5% | 13.5% | 0.3% | **12** | **78 WATCH** |
| Corning Incorporated | `GLW` | 6.3 | 6.7 | 15.6% | 28.3 | 33.6% | 20.0% | 0.7% | **77 WATCH** | **13** |
| Applied Materials, Inc. | `AMAT` | 9.8 | 9.6 | 33.7% | 20.7 | 44.6% | 35.3% | 1.0% | **77 WATCH** | **3** |
| Robinhood Markets, Inc. | `HOOD` | 17.0 | 17.1 | 43.9% | 27.2 | 36.5% | 29.3% | — | **77 WATCH** | **5** |
| Credo Technology Group Holding  | `CRDO` | 17.5 | 16.9 | 25.2% | 15.3 | 53.9% | 55.0% | 0.9% | **75 WATCH** | **28** |
| NVIDIA Corporation | `NVDA` | 17.1 | 16.7 | 66.2% | 13.5 | 70.9% | 68.2% | 0.8% | **75 WATCH** | **18** |
| Broadcom Inc. | `AVGO` | 17.5 | 17.6 | 54.3% | 16.8 | 66.7% | 64.3% | 2.0% | **75 WATCH** | **28** |
| Micron Technology, Inc. | `MU` | 7.6 | 7.2 | 80.7% | 4.3 | 17.2% | 15.7% | 2.9% | **75 CORE** | **30** |
| Western Digital Corporation | `WDC` | 9.0 | 8.9 | 47.7% | 8.8 | 59.1% | 36.9% | 2.1% | **75 WATCH** | **18** |
| Cerebras Systems Inc. | `CBRS` | 37.9 | 29.2 | -265.0% | 85.2 | 371.3% | 232.7% | — | **0** | **75 WATCH** |
| Moderna, Inc. | `MRNA` | 36.3 | 34.1 | -557.9% | -44.4 | 42.5% | 16.3% | 0.4% | **0** | **72 WATCH** |
| Marvell Technology, Inc. | `MRVL` | 21.7 | 21.3 | 16.7% | 31.1 | 73.7% | 63.3% | 1.2% | **70 WATCH** | **13** |
| Advanced Micro Devices, Inc. | `AMD` | 20.5 | 20.2 | 17.2% | 32.9 | 107.7% | 74.9% | 1.0% | **70 WATCH** | **13** |
| Oracle Corporation | `ORCL` | 5.3 | 7.2 | 35.6% | 11.5 | 35.0% | 45.7% | -12.0% | **70 WATCH** | **10** |
| XIAOMI-W | `XIAOMI` | 1.6 | 1.4 | 4.0% | 17.8 | 36.8% | 19.7% | -1.3% | **70 WATCH** | **10** |
| Adobe Inc. | `ADBE` | 3.9 | 4.0 | 34.8% | 9.5 | 12.4% | 9.1% | 9.2% | **65 WATCH** | **30** |
| Coherent Corp. | `COHR` | 5.9 | 6.0 | 11.8% | 15.3 | 48.3% | 38.3% | -1.6% | **60 WATCH** | **35** |
| Microsoft Corporation | `MSFT` | 11.8 | 11.9 | 45.1% | 22.2 | 20.0% | 19.7% | 0.4% | **59 WATCH** | **23** |
| Apple Inc. | `AAPL` | 10.8 | 10.9 | 32.6% | 36.1 | 8.2% | 10.4% | 2.1% | **5** | **58** |
| Coca-Cola Company (The) | `KO` | 7.9 | 8.6 | 34.9% | 26.2 | 6.7% | -0.1% | 1.3% | **0** | **58** |
| Meta Platforms, Inc. | `META` | 6.7 | 6.9 | 35.4% | 18.2 | 16.4% | 21.5% | 1.0% | **57 WATCH** | **38** |
| AXT Inc | `AXT` | 28.1 | 24.7 | 21.9% | 23.9 | 159.2% | 111.3% | -1.3% | **52** | **35** |
| Super Micro Computer, Inc. | `SMCI` | 0.6 | 0.7 | 13.4% | 5.9 | 19.7% | 16.3% | -38.0% | **52** | **45** |
| Lumentum Holdings Inc. | `LITE` | 23.8 | 22.2 | 28.0% | 22.1 | 64.9% | 57.2% | 0.3% | **0** | **51** |
| Netflix, Inc. | `NFLX` | 5.5 | 5.6 | 34.6% | 17.3 | 5.1% | 10.8% | 9.4% | **35** | **50** |
| IREN LIMITED | `IREN` | 14.2 | 16.6 | -102.5% | -6.2 | -16.4% | 164.0% | -42.0% | **0** | **50** |
| Palantir Technologies Inc. | `PLTR` | 76.8 | 75.3 | 47.1% | 83.6 | 45.6% | 50.4% | 0.5% | **33** | **48** |
| Intel Corporation | `INTC` | 8.1 | 8.3 | 12.2% | 41.1 | 38.1% | 15.2% | 1.1% | **10** | **48** |
| Bloom Energy Corporation | `BE` | 15.5 | 15.0 | 18.5% | 37.9 | 62.7% | 55.7% | -0.0% | **45** | **35** |
| SK hynix | `SKHYNIX` | 4.9 | 4.4 | 76.3% | 2.7 | 31.9% | 54.3% | 6.0% | **45** | **5** |
| SK hynix | `SKHY` | 4.9 | 4.4 | 76.3% | 2.7 | 31.9% | 54.3% | 6.0% | **45** | **5** |
| SamsungElec | `SAMSUNG` | 2.9 | 2.6 | 52.2% | 2.9 | 51.5% | 38.3% | 5.0% | **45** | **10** |
| Arm Holdings plc | `ARM` | 44.6 | 42.9 | 7.6% | 70.2 | 37.5% | 36.4% | 0.6% | **43** | **33** |
| Circle Internet Group, Inc. | `CRCL` | 7.0 | 6.9 | 4.9% | 54.4 | 30.0% | 26.7% | 1.0% | **43** | **33** |
| Coinbase Global, Inc. | `COIN` | 7.0 | 6.8 | -13.9% | 52.1 | 283.2% | 30.1% | 6.3% | **20** | **40** |
| SOFTBANK GROUP CORP | `SOFTBANK` | 3.0 | 6.4 | -11.6% | 14.4 | -14.5% | 6.9% | -9.0% | **0** | **40** |
| CoreWeave, Inc. | `CRWV` | 4.0 | 10.0 | -1.9% | -27.9 | 11.4% | 105.6% | -29.9% | **0** | **40** |
| Dell Technologies Inc. | `DELL` | 1.9 | 2.1 | 12.0% | 15.4 | 9.6% | 18.4% | 2.1% | **33** | **38** |
| Amazon.com, Inc. | `AMZN` | 3.5 | 3.6 | 13.7% | 24.0 | -18.2% | 14.6% | 0.1% | **0** | **38** |
| Fluence Energy, Inc. | `FLNC` | 0.4 | 0.4 | -8.9% | -12.3 | 60.4% | 26.9% | 0.2% | **5** | **28** |
| Hyperliquid Strategies Inc | `PURR` | 266.8 | 169.0 | 9595.1% | 24.5 | 51.0% | 31.4% | — | **25** | **10** |
| BitMine Immersion Technologies, | `BMNR` | 215.5 | 215.3 | 8.4% | 23.3 | 103.2% | 421.8% | -3.9% | **25** | **25** |
| Strategy Inc | `MSTR` | 120.6 | 150.2 | -6808.1% | 6.0 | 168.2% | 2.2% | -37.6% | **25** | **25** |
| QUALCOMM Incorporated | `QCOM` | 4.3 | 4.4 | 18.5% | 17.3 | -2.8% | 4.7% | 5.4% | **25** | **15** |
| Applied Optoelectronics, Inc. | `AAOI` | 9.7 | 9.2 | -12.9% | 14.8 | 576.8% | 156.5% | -15.3% | **10** | **25** |
| Alphabet Inc. | `GOOGL` | 8.8 | 8.6 | 34.0% | 20.9 | -26.6% | 25.3% | 0.6% | **12** | **23** |

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
