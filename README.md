# OKX Long / Short Fundamental Scanner

Hourly scanner restricted to public companies exposed by the **OKX EEA TradFi / Stock Perpetual API universe**.

**Last scan:** 2026-10-09 09:16 UTC  
**Availability scope:** user-confirmed OKX EEA Stock Futures / X-Perp  
**OKX stock/ETF markets in configured universe:** 72  
**Public companies analysed:** 55  
**SHORT CORE:** 6  
**LONG CORE:** 3

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
| 1 | Taiwan Semiconductor Manufactur | TSM | 0.0% | -3.1% | -1.6% | 82 | +1 | **83** | **CORE** | yes |
| 2 | NVIDIA Corporation | NVDA | 0.0% | -1.5% | -0.7% | 82 | +1 | **83** | **CORE** | yes |
| 3 | Applied Materials, Inc. | AMAT | -0.0% | -5.6% | -2.8% | 81 | +2 | **83** | **CORE** | yes |
| 4 | Broadcom Inc. | AVGO | -0.0% | 1.4% | 0.7% | 82 | -1 | **81** | **CORE** | yes |
| 5 | Applovin Corporation | APP | 0.0% | 4.4% | 2.2% | 82 | -2 | **80** | **CORE** | yes |
| 6 | Advanced Micro Devices, Inc. | AMD | 0.0% | -2.1% | -1.0% | 79 | +1 | **80** | **CORE** | yes |
| 7 | Oracle Corporation | ORCL | -0.0% | -4.6% | -2.3% | 78 | +2 | **80** | **CORE** | yes |
| 8 | Sandisk Corporation | SNDK | 0.0% | -6.4% | -3.2% | 77 | +3 | **80** | **CORE** | yes |
| 9 | Marvell Technology, Inc. | MRVL | -0.0% | 0.9% | 0.4% | 79 | +0 | **79** | **CORE** | yes |
| 10 | Credo Technology Group Holding  | CRDO | -0.0% | -3.1% | -1.6% | 76 | +1 | **77** | **CORE** | yes |

## Final model + Price Timing — SHORT

| Rank | Company | OKX | 24h | 7d | 50/50 move | Base SHORT | Timing adj. | Final | Signal | Prev. SHORT? |
|---:|---|---|---:|---:|---:|---:|---:|---:|---|---|
| 1 | Cerebras Systems Inc. | CBRS | 0.0% | 0.9% | 0.4% | 98 | +0 | **98** | **CORE** | yes |
| 2 | Rocket Lab Corporation | RKLB | -0.0% | -7.5% | -3.7% | 100 | -3 | **97** | **CORE** | yes |
| 3 | USA Rare Earth, Inc. | USAR | -0.0% | -7.1% | -3.5% | 100 | -3 | **97** | **CORE** | yes |
| 4 | IonQ, Inc. | IONQ | -0.0% | -9.9% | -4.9% | 91 | -4 | **87** | **CORE** | yes |
| 5 | Nebius Group N.V. | NBIS | -0.0% | -9.5% | -4.8% | 90 | -4 | **86** | **CORE** | yes |
| 6 | AST SpaceMobile, Inc. | ASTS | -0.0% | -2.6% | -1.3% | 80 | -1 | **79** | **CORE** | yes |
| 7 | Moderna, Inc. | MRNA | 0.0% | 3.7% | 1.8% | 72 | +1 | **73** | **WATCH** | yes |
| 8 | Lumentum Holdings Inc. | LITE | 0.0% | -3.4% | -1.7% | 67 | -1 | **66** | **WATCH** | yes |
| 9 | Okta, Inc. | OKTA | -0.0% | 4.1% | 2.1% | 61 | +2 | **63** | **WATCH** | yes |
| 10 | IREN LIMITED | IREN | 0.0% | -14.5% | -7.2% | 64 | -6 | **58** | **WATCH** | yes |

## Combined model — LONG

Weighted score: **70% fundamental + 30% P/E trend**.

| Rank | Company | OKX | Fundamental LONG | P/E trend LONG | Combined | Signal |
|---:|---|---|---:|---:|---:|---|
| 1 | Applovin Corporation | `APP` | 83 | 80 | **82** | **CORE** |
| 2 | Taiwan Semiconductor Manufactur | `TSM` | 82 | 81 | **82** | **CORE** |
| 3 | NVIDIA Corporation | `NVDA` | 75 | 100 | **82** | **CORE** |
| 4 | Broadcom Inc. | `AVGO` | 75 | 100 | **82** | **CORE** |
| 5 | Applied Materials, Inc. | `AMAT` | 77 | 91 | **81** | **CORE** |
| 6 | Advanced Micro Devices, Inc. | `AMD` | 70 | 100 | **79** | **CORE** |
| 7 | Marvell Technology, Inc. | `MRVL` | 70 | 100 | **79** | **CORE** |
| 8 | Oracle Corporation | `ORCL` | 70 | 95 | **78** | **CORE** |
| 9 | Sandisk Corporation | `SNDK` | 75 | 82 | **77** | **CORE** |
| 10 | Credo Technology Group Holding  | `CRDO` | 67 | 96 | **76** | **CORE** |

## Combined model — SHORT

Weighted score: **70% fundamental + 30% P/E trend**.

| Rank | Company | OKX | Fundamental SHORT | P/E trend SHORT | Combined | Signal |
|---:|---|---|---:|---:|---:|---|
| 1 | Rocket Lab Corporation | `RKLB` | 100 | 0 | **100** | **CORE** |
| 2 | USA Rare Earth, Inc. | `USAR` | 100 | 0 | **100** | **CORE** |
| 3 | Cerebras Systems Inc. | `CBRS` | 98 | 0 | **98** | **CORE** |
| 4 | IonQ, Inc. | `IONQ` | 91 | 0 | **91** | **CORE** |
| 5 | Nebius Group N.V. | `NBIS` | 90 | 0 | **90** | **CORE** |
| 6 | AST SpaceMobile, Inc. | `ASTS` | 80 | 0 | **80** | **WATCH** |
| 7 | Moderna, Inc. | `MRNA` | 72 | 0 | **72** | **WATCH** |
| 8 | Lumentum Holdings Inc. | `LITE` | 67 | 0 | **67** | **WATCH** |
| 9 | Okta, Inc. | `OKTA` | 80 | 18 | **61** | **WATCH** |

## P/E Compression + Growth — LONG

| Rank | Company | OKX | Trail P/E | Fwd P/E | P/E change | EPS +1y | Rev +1y | Rev trend | LONG score | Signal |
|---:|---|---|---:|---:|---:|---:|---:|---|---:|---|
| 1 | NVIDIA Corporation | `NVDA` | 29.1 | 14.5 | -50.3% | 70.9% | 68.2% | decelerating | **100** | **CORE** |
| 2 | Broadcom Inc. | `AVGO` | 46.0 | 18.6 | -59.6% | 66.4% | 64.1% | decelerating | **100** | **CORE** |
| 3 | Advanced Micro Devices, Inc. | `AMD` | 158.3 | 39.5 | -75.1% | 107.2% | 74.6% | accelerating | **100** | **CORE** |
| 4 | Marvell Technology, Inc. | `MRVL` | 90.3 | 37.7 | -58.3% | 72.6% | 63.1% | accelerating | **100** | **CORE** |
| 5 | Credo Technology Group Holding  | `CRDO` | 75.1 | 21.9 | -70.9% | 53.7% | 54.8% | decelerating | **96** | **CORE** |
| 6 | Corning Incorporated | `GLW` | 70.1 | 35.0 | -50.1% | 33.0% | 19.6% | accelerating | **96** | **CORE** |
| 7 | AXT Inc | `AXT` | 1791.5 | 31.8 | -98.2% | 159.2% | 111.3% | decelerating | **96** | **CORE** |
| 8 | Oracle Corporation | `ORCL` | 21.3 | 12.3 | -42.0% | 35.1% | 45.7% | accelerating | **95** | **CORE** |
| 9 | Applied Materials, Inc. | `AMAT` | 44.0 | 27.6 | -37.3% | 44.5% | 34.9% | accelerating | **91** | **CORE** |
| 10 | Coherent Corp. | `COHR` | 73.4 | 21.5 | -70.7% | 49.1% | 38.8% | decelerating | **91** | **CORE** |

## P/E Expansion + Weakening — SHORT

| Rank | Company | OKX | Trail P/E | Fwd P/E | P/E change | EPS +1y | Rev +1y | Rev trend | SHORT score | Signal |
|---:|---|---|---:|---:|---:|---:|---:|---|---:|---|
| 1 | SOFTBANK GROUP CORP | `SOFTBANK` | 6.8 | 19.7 | 191.0% | -14.5% | 6.9% | decelerating | **86** | **CORE** |
| 2 | Alphabet Inc. | `GOOGL` | 17.5 | 23.1 | 32.2% | -27.4% | 23.3% | decelerating | **70** | **CORE** |
| 3 | Hyperliquid Strategies Inc | `PURR` | 3.5 | 30.5 | 767.6% | 51.0% | 31.4% | decelerating | **55** | **WATCH** |
| 4 | Amazon.com, Inc. | `AMZN` | 20.4 | 24.3 | 18.8% | -18.4% | 14.5% | decelerating | **52** | **WATCH** |

## Top SHORT candidates

| Rank | Company | OKX market | SHORT score | Signal | P/S | EV/S | Op margin | Fwd P/E | Rev +1y | FCF yield |
|---:|---|---|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Rocket Lab Corporation | `RKLB-USDT-SWAP` | **100** | **CORE** | 56.9 | 50.4 | -24.6% | 1161.7 | 41.9% | -0.6% |
| 2 | USA Rare Earth, Inc. | `USAR-USDT-SWAP` | **100** | **CORE** | 359.9 | 119.5 | -795.6% | 421.0 | 870.1% | -6.0% |
| 3 | Cerebras Systems Inc. | `CBRS-USDT-SWAP` | **98** | **CORE** | 58.6 | 49.2 | -265.0% | 131.8 | 232.7% | — |
| 4 | IonQ, Inc. | `IONQ-USDT-SWAP` | **91** | **CORE** | 64.8 | 52.7 | -408.2% | -30.5 | 79.0% | -0.5% |
| 5 | Nebius Group N.V. | `NBIS-USDT-SWAP` | **90** | **CORE** | 44.1 | 46.0 | -0.2% | -61.8 | 268.0% | -16.1% |
| 6 | Okta, Inc. | `OKTA-USDT-SWAP` | **80** | **CORE** | 12.5 | 11.8 | 13.3% | 50.3 | 10.0% | 2.7% |
| 7 | AST SpaceMobile, Inc. | `ASTS-USDT-SWAP` | **80** | **WATCH** | 192.2 | 158.5 | -544.6% | -44.2 | 259.9% | -8.1% |
| 8 | Moderna, Inc. | `MRNA-USDT-SWAP` | **72** | **WATCH** | 35.3 | 33.6 | -557.9% | -44.3 | 15.8% | 0.4% |
| 9 | Lumentum Holdings Inc. | `LITE-USDT-SWAP` | **67** | **WATCH** | 31.5 | 30.9 | 28.0% | 29.5 | 55.7% | 0.2% |
| 10 | Tesla, Inc. | `TSLA-USDT-SWAP` | **63** | **WATCH** | 14.3 | 14.0 | 1.4% | 174.8 | 13.4% | 0.3% |

## Top LONG candidates

| Rank | Company | OKX market | LONG score | Signal | P/S | EV/S | Op margin | Fwd P/E | Rev +1y | FCF yield |
|---:|---|---|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Applovin Corporation | `APP-USDT-SWAP` | **83** | **CORE** | 13.8 | 13.8 | 77.7% | 13.5 | 26.4% | 3.4% |
| 2 | Taiwan Semiconductor Manufactur | `TSM-USDT-SWAP` | **82** | **CORE** | 0.5 | 3.7 | 60.3% | 20.9 | 35.3% | 30.8% |
| 3 | Applied Materials, Inc. | `AMAT-USDT-SWAP` | **77** | **WATCH** | 13.1 | 13.1 | 33.7% | 27.6 | 34.9% | 0.8% |
| 4 | Broadcom Inc. | `AVGO-USDT-SWAP` | **75** | **WATCH** | 19.3 | 19.7 | 54.3% | 18.6 | 64.1% | 1.8% |
| 5 | Sandisk Corporation | `SNDK-USDT-SWAP` | **75** | **CORE** | 11.5 | 11.4 | 78.5% | 6.0 | 18.9% | 3.3% |
| 6 | Western Digital Corporation | `WDC-USDT-SWAP` | **75** | **WATCH** | 11.4 | 10.9 | 43.6% | 12.3 | 36.9% | 1.5% |
| 7 | NVIDIA Corporation | `NVDA-USDT-SWAP` | **75** | **WATCH** | 18.4 | 18.3 | 66.2% | 14.5 | 68.2% | 0.8% |
| 8 | Robinhood Markets, Inc. | `HOOD-USDT-SWAP` | **70** | **WATCH** | 19.5 | 19.3 | 43.9% | 31.1 | 28.6% | — |
| 9 | Marvell Technology, Inc. | `MRVL-USDT-SWAP` | **70** | **WATCH** | 26.1 | 25.6 | 16.7% | 37.7 | 63.1% | 1.0% |
| 10 | XIAOMI-W | `XIAOMI-USDT-SWAP` | **70** | **WATCH** | 1.5 | 1.2 | 4.0% | 16.9 | 22.6% | -1.3% |

## Analyst consensus (12-month price target) — most upside

| Rank | Company | OKX | Price | Analyst mean target | Gap | Analysts | Currency |
|---:|---|---|---:|---:|---:|---:|---|
| 1 | USA Rare Earth, Inc. | `USAR` | 12.63 | 35.56 | **181.5%** | 9 | USD |
| 2 | IREN LIMITED | `IREN` | 35.71 | 78.14 | **118.8%** | 18 | USD |
| 3 | Hyperliquid Strategies Inc | `PURR` | 11.30 | 22.32 | **97.6%** | 4 | USD |
| 4 | BitMine Immersion Technologies, | `BMNR` | 24.04 | 45.87 | **90.8%** | 3 | USD |
| 5 | SK hynix | `SKHYNIX` | 1681000.00 | 3141024.80 | **86.9%** | 38 | KRW |
| 6 | SamsungElec | `SAMSUNG` | 262000.00 | 478905.62 | **82.8%** | 36 | KRW |
| 7 | Oracle Corporation | `ORCL` | 135.69 | 237.97 | **75.4%** | 41 | USD |
| 8 | Applovin Corporation | `APP` | 280.12 | 490.08 | **75.0%** | 31 | USD |
| 9 | Cerebras Systems Inc. | `CBRS` | 167.92 | 291.64 | **73.7%** | 11 | USD |
| 10 | CoreWeave, Inc. | `CRWV` | 81.58 | 141.47 | **73.4%** | 38 | USD |
| 11 | Western Digital Corporation | `WDC` | 393.31 | 670.79 | **70.6%** | 24 | USD |
| 12 | IonQ, Inc. | `IONQ` | 39.45 | 66.63 | **68.9%** | 14 | USD |
| 13 | Rocket Lab Corporation | `RKLB` | 68.40 | 109.15 | **59.6%** | 20 | USD |
| 14 | Strategy Inc | `MSTR` | 151.47 | 237.80 | **57.0%** | 15 | USD |
| 15 | Applied Optoelectronics, Inc. | `AAOI` | 105.90 | 163.40 | **54.3%** | 5 | USD |

## Analyst consensus (12-month price target) — most downside

| Rank | Company | OKX | Price | Analyst mean target | Gap | Analysts | Currency |
|---:|---|---|---:|---:|---:|---:|---|
| 1 | Moderna, Inc. | `MRNA` | 197.00 | 121.00 | **-38.6%** | 18 | USD |
| 2 | Apple Inc. | `AAPL` | 340.42 | 328.09 | **-3.6%** | 39 | USD |
| 3 | Okta, Inc. | `OKTA` | 220.21 | 212.25 | **-3.6%** | 43 | USD |
| 4 | Super Micro Computer, Inc. | `SMCI` | 42.77 | 42.27 | **-1.2%** | 15 | USD |

Price/target uses the underlying Yahoo Finance share quote, not the OKX derivative. Minimum 3 analysts; unreliable price scales and missing coverage excluded. Targets are analyst opinions, not guaranteed forecasts.

## All OKX companies — our ratio + LONG/SHORT scores

| Company | OKX | P/S | EV/S | Op margin | Fwd P/E | EPS +1y | Rev +1y | FCF yield | LONG | SHORT |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Rocket Lab Corporation | `RKLB` | 56.9 | 50.4 | -24.6% | 1161.7 | 72.7% | 41.9% | -0.6% | **0** | **100 CORE** |
| USA Rare Earth, Inc. | `USAR` | 359.9 | 119.5 | -795.6% | 421.0 | 105.3% | 870.1% | -6.0% | **0** | **100 CORE** |
| Cerebras Systems Inc. | `CBRS` | 58.6 | 49.2 | -265.0% | 131.8 | 371.3% | 232.7% | — | **0** | **98 CORE** |
| IonQ, Inc. | `IONQ` | 64.8 | 52.7 | -408.2% | -30.5 | 18.1% | 79.0% | -0.5% | **0** | **91 CORE** |
| Nebius Group N.V. | `NBIS` | 44.1 | 46.0 | -0.2% | -61.8 | -191.4% | 268.0% | -16.1% | **0** | **90 CORE** |
| Applovin Corporation | `APP` | 13.8 | 13.8 | 77.7% | 13.5 | 27.5% | 26.4% | 3.4% | **83 CORE** | **10** |
| Taiwan Semiconductor Manufactur | `TSM` | 0.5 | 3.7 | 60.3% | 20.9 | 30.0% | 35.3% | 30.8% | **82 CORE** | **10** |
| Okta, Inc. | `OKTA` | 12.5 | 11.8 | 13.3% | 50.3 | 11.4% | 10.0% | 2.7% | **8** | **80 CORE** |
| AST SpaceMobile, Inc. | `ASTS` | 192.2 | 158.5 | -544.6% | -44.2 | 47.7% | 259.9% | -8.1% | **0** | **80 WATCH** |
| Applied Materials, Inc. | `AMAT` | 13.1 | 13.1 | 33.7% | 27.6 | 44.5% | 34.9% | 0.8% | **77 WATCH** | **13** |
| NVIDIA Corporation | `NVDA` | 18.4 | 18.3 | 66.2% | 14.5 | 70.9% | 68.2% | 0.8% | **75 WATCH** | **18** |
| Broadcom Inc. | `AVGO` | 19.3 | 19.7 | 54.3% | 18.6 | 66.4% | 64.1% | 1.8% | **75 WATCH** | **28** |
| Sandisk Corporation | `SNDK` | 11.5 | 11.4 | 78.5% | 6.0 | 24.0% | 18.9% | 3.3% | **75 CORE** | **10** |
| Western Digital Corporation | `WDC` | 11.4 | 10.9 | 43.6% | 12.3 | 58.2% | 36.9% | 1.5% | **75 WATCH** | **18** |
| Moderna, Inc. | `MRNA` | 35.3 | 33.6 | -557.9% | -44.3 | 42.9% | 15.8% | 0.4% | **0** | **72 WATCH** |
| Advanced Micro Devices, Inc. | `AMD` | 24.5 | 24.3 | 17.2% | 39.5 | 107.2% | 74.6% | 0.9% | **70 WATCH** | **13** |
| Oracle Corporation | `ORCL` | 5.7 | 7.6 | 35.6% | 12.3 | 35.1% | 45.7% | -11.1% | **70 WATCH** | **10** |
| Marvell Technology, Inc. | `MRVL` | 26.1 | 25.6 | 16.7% | 37.7 | 72.6% | 63.1% | 1.0% | **70 WATCH** | **13** |
| Robinhood Markets, Inc. | `HOOD` | 19.5 | 19.3 | 43.9% | 31.1 | 35.3% | 28.6% | — | **70 WATCH** | **5** |
| XIAOMI-W | `XIAOMI` | 1.5 | 1.2 | 4.0% | 16.9 | 39.6% | 22.6% | -1.3% | **70 WATCH** | **10** |
| Credo Technology Group Holding  | `CRDO` | 25.0 | 24.6 | 25.2% | 21.9 | 53.7% | 54.8% | 0.6% | **67 WATCH** | **28** |
| Micron Technology, Inc. | `MU` | 8.8 | 8.5 | 80.7% | 5.0 | 17.1% | 16.0% | 2.5% | **67 WATCH** | **38** |
| Lumentum Holdings Inc. | `LITE` | 31.5 | 30.9 | 28.0% | 29.5 | 63.4% | 55.7% | 0.2% | **0** | **67 WATCH** |
| Adobe Inc. | `ADBE` | 3.6 | 3.7 | 34.8% | 8.7 | 13.0% | 9.2% | 10.0% | **65 WATCH** | **30** |
| IREN LIMITED | `IREN` | 19.9 | 22.7 | -102.5% | -9.0 | -16.4% | 160.9% | -30.0% | **0** | **64** |
| Tesla, Inc. | `TSLA` | 14.3 | 14.0 | 1.4% | 174.8 | 23.2% | 13.4% | 0.3% | **22** | **63 WATCH** |
| Corning Incorporated | `GLW` | 7.8 | 8.2 | 15.6% | 35.0 | 33.0% | 19.6% | 0.6% | **60 WATCH** | **13** |
| Microsoft Corporation | `MSFT` | 11.7 | 11.9 | 45.1% | 22.1 | 19.8% | 19.6% | 0.4% | **59 WATCH** | **23** |
| Dell Technologies Inc. | `DELL` | 2.4 | 2.6 | 12.0% | 19.7 | 0.8% | 16.5% | 1.7% | **25** | **58** |
| Coca-Cola Company (The) | `KO` | 7.5 | 8.1 | 34.9% | 24.9 | 6.8% | 0.2% | 1.4% | **7** | **58** |
| Apple Inc. | `AAPL` | 10.6 | 10.7 | 32.6% | 35.5 | 8.6% | 10.5% | 2.2% | **5** | **58** |
| Bloom Energy Corporation | `BE` | 25.8 | 25.9 | 17.1% | 55.2 | 82.6% | 65.0% | 0.7% | **55 WATCH** | **48** |
| Coherent Corp. | `COHR` | 8.3 | 8.6 | 11.8% | 21.5 | 49.1% | 38.8% | -1.1% | **52** | **35** |
| Super Micro Computer, Inc. | `SMCI` | 0.7 | 0.9 | 13.4% | 8.0 | 22.8% | 17.3% | -29.4% | **52** | **25** |
| Netflix, Inc. | `NFLX` | 6.2 | 6.3 | 33.4% | 18.8 | 6.1% | 11.2% | 8.5% | **35** | **50** |
| Palantir Technologies Inc. | `PLTR` | 77.6 | 76.1 | 47.1% | 84.5 | 45.0% | 49.8% | 0.5% | **33** | **48** |
| Intel Corporation | `INTC` | 9.9 | 10.1 | 12.2% | 51.4 | 36.9% | 14.8% | 0.9% | **5** | **48** |
| AXT Inc | `AXT` | 37.4 | 34.7 | 21.9% | 31.8 | 159.2% | 111.3% | -0.9% | **45** | **35** |
| SK hynix | `SKHYNIX` | 6.3 | 6.0 | 76.3% | 3.6 | 32.4% | 54.4% | 4.7% | **45** | **5** |
| SK hynix | `SKHY` | 6.3 | 6.0 | 76.3% | 3.6 | 32.4% | 54.4% | 4.7% | **45** | **5** |
| SamsungElec | `SAMSUNG` | 3.5 | 3.2 | 52.2% | 3.6 | 50.8% | 37.7% | 4.0% | **45** | **10** |
| Circle Internet Group, Inc. | `CRCL` | 7.1 | 6.5 | 4.9% | 57.2 | 30.8% | 24.9% | 1.0% | **43** | **33** |
| Coinbase Global, Inc. | `COIN` | 7.5 | 7.2 | -13.9% | 60.6 | 267.7% | 29.9% | 5.9% | **20** | **40** |
| SOFTBANK GROUP CORP | `SOFTBANK` | 4.1 | 7.7 | -11.6% | 19.7 | -14.5% | 6.9% | -6.6% | **0** | **40** |
| CoreWeave, Inc. | `CRWV` | 5.9 | 12.0 | -1.9% | -45.0 | 15.4% | 104.3% | -20.2% | **0** | **40** |
| Meta Platforms, Inc. | `META` | 8.0 | 8.1 | 34.8% | 20.9 | 9.8% | 20.6% | 1.2% | **17** | **38** |
| Alphabet Inc. | `GOOGL` | 9.6 | 9.3 | 34.0% | 23.1 | -27.4% | 23.3% | 0.5% | **2** | **38** |
| Amazon.com, Inc. | `AMZN` | 3.5 | 3.7 | 13.7% | 24.3 | -18.4% | 14.5% | 0.1% | **0** | **38** |
| Arm Holdings plc | `ARM` | 57.0 | 56.4 | 7.6% | 89.9 | 37.5% | 36.2% | 0.5% | **35** | **33** |
| Applied Optoelectronics, Inc. | `AAOI` | 15.1 | 14.7 | -12.9% | 23.0 | 576.8% | 156.5% | -9.9% | **0** | **35** |
| Fluence Energy, Inc. | `FLNC` | 0.6 | 0.5 | -8.9% | -28.0 | 70.1% | 35.3% | 0.2% | **5** | **28** |
| Hyperliquid Strategies Inc | `PURR` | 332.4 | 221.7 | 9595.1% | 30.5 | 51.0% | 31.4% | — | **25** | **10** |
| BitMine Immersion Technologies, | `BMNR` | 237.0 | 231.4 | 8.4% | 25.6 | 103.2% | 421.8% | -3.6% | **25** | **25** |
| Strategy Inc | `MSTR` | 121.2 | 154.4 | -6808.1% | 3.1 | 157.6% | 2.2% | -37.4% | **25** | **25** |
| QUALCOMM Incorporated | `QCOM` | 4.3 | 4.4 | 18.5% | 17.2 | -2.7% | 4.8% | 5.4% | **25** | **15** |

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
