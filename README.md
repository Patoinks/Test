# OKX Long / Short Fundamental Scanner

Hourly scanner restricted to public companies exposed by the **OKX EEA TradFi / Stock Perpetual API universe**.

**Last scan:** 2026-10-06 03:05 UTC  
**Availability scope:** user-confirmed OKX EEA Stock Futures / X-Perp  
**OKX stock/ETF markets in configured universe:** 69  
**Public companies analysed:** 54  
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
| 1 | Applovin Corporation | APP | 5.1% | -8.5% | -1.7% | 82 | +1 | **83** | **CORE** | yes |
| 2 | Broadcom Inc. | AVGO | 2.1% | 3.7% | 2.9% | 82 | -2 | **80** | **CORE** | yes |
| 3 | Taiwan Semiconductor Manufactur | TSM | 2.8% | 7.3% | 5.0% | 82 | -4 | **78** | **CORE** | yes |
| 4 | Sandisk Corporation | SNDK | -0.9% | -0.5% | -0.7% | 77 | +1 | **78** | **CORE** | yes |
| 5 | NVIDIA Corporation | NVDA | 2.1% | 4.4% | 3.3% | 80 | -3 | **77** | **CORE** | yes |
| 6 | Applied Materials, Inc. | AMAT | 0.4% | 11.4% | 5.9% | 81 | -5 | **76** | **CORE** | yes |
| 7 | Oracle Corporation | ORCL | 0.1% | 7.5% | 3.8% | 78 | -3 | **75** | **CORE** | yes |
| 8 | Advanced Micro Devices, Inc. | AMD | -0.3% | 3.9% | 1.8% | 76 | -1 | **75** | **CORE** | yes |
| 9 | Robinhood Markets, Inc. | HOOD | 1.2% | -2.0% | -0.4% | 75 | +0 | **75** | **CORE** | yes |
| 10 | Credo Technology Group Holding  | CRDO | -2.8% | 10.3% | 3.7% | 76 | -3 | **73** | **WATCH** | yes |

## Final model + Price Timing — SHORT

| Rank | Company | OKX | 24h | 7d | 50/50 move | Base SHORT | Timing adj. | Final | Signal | Prev. SHORT? |
|---:|---|---|---:|---:|---:|---:|---:|---:|---|---|
| 1 | Cerebras Systems Inc. | CBRS | 9.1% | -7.7% | 0.7% | 100 | +1 | **100** | **CORE** | yes |
| 2 | Rocket Lab Corporation | RKLB | -1.2% | 1.1% | -0.0% | 100 | +0 | **100** | **CORE** | yes |
| 3 | USA Rare Earth, Inc. | USAR | 0.4% | -5.3% | -2.4% | 100 | -2 | **98** | **CORE** | yes |
| 4 | IonQ, Inc. | IONQ | -1.8% | -3.6% | -2.7% | 91 | -2 | **89** | **CORE** | yes |
| 5 | Nebius Group N.V. | NBIS | -4.2% | 0.3% | -2.0% | 90 | -2 | **88** | **CORE** | yes |
| 6 | AST SpaceMobile, Inc. | ASTS | -0.0% | -4.2% | -2.1% | 80 | -2 | **78** | **CORE** | yes |
| 7 | Moderna, Inc. | MRNA | 6.9% | 3.0% | 5.0% | 72 | +4 | **76** | **CORE** | yes |
| 8 | Lumentum Holdings Inc. | LITE | 0.6% | 18.5% | 9.5% | 67 | +8 | **75** | **CORE** | yes |
| 9 | IREN LIMITED | IREN | -3.1% | -3.0% | -3.0% | 72 | -2 | **70** | **WATCH** | yes |
| 10 | Okta, Inc. | OKTA | 3.2% | 8.0% | 5.6% | 60 | +4 | **64** | **WATCH** | yes |

## Combined model — LONG

Weighted score: **70% fundamental + 30% P/E trend**.

| Rank | Company | OKX | Fundamental LONG | P/E trend LONG | Combined | Signal |
|---:|---|---|---:|---:|---:|---|
| 1 | Applovin Corporation | `APP` | 83 | 80 | **82** | **CORE** |
| 2 | Taiwan Semiconductor Manufactur | `TSM` | 82 | 81 | **82** | **CORE** |
| 3 | Broadcom Inc. | `AVGO` | 75 | 100 | **82** | **CORE** |
| 4 | Applied Materials, Inc. | `AMAT` | 77 | 91 | **81** | **CORE** |
| 5 | NVIDIA Corporation | `NVDA` | 75 | 90 | **80** | **CORE** |
| 6 | Oracle Corporation | `ORCL` | 70 | 95 | **78** | **CORE** |
| 7 | Sandisk Corporation | `SNDK` | 75 | 82 | **77** | **CORE** |
| 8 | Credo Technology Group Holding  | `CRDO` | 67 | 96 | **76** | **CORE** |
| 9 | Advanced Micro Devices, Inc. | `AMD` | 65 | 100 | **76** | **CORE** |
| 10 | Marvell Technology, Inc. | `MRVL` | 65 | 100 | **76** | **CORE** |

## Combined model — SHORT

Weighted score: **70% fundamental + 30% P/E trend**.

| Rank | Company | OKX | Fundamental SHORT | P/E trend SHORT | Combined | Signal |
|---:|---|---|---:|---:|---:|---|
| 1 | Cerebras Systems Inc. | `CBRS` | 100 | 0 | **100** | **CORE** |
| 2 | Rocket Lab Corporation | `RKLB` | 100 | 0 | **100** | **CORE** |
| 3 | USA Rare Earth, Inc. | `USAR` | 100 | 0 | **100** | **CORE** |
| 4 | IonQ, Inc. | `IONQ` | 91 | 0 | **91** | **CORE** |
| 5 | Nebius Group N.V. | `NBIS` | 90 | 0 | **90** | **CORE** |
| 6 | AST SpaceMobile, Inc. | `ASTS` | 80 | 0 | **80** | **WATCH** |
| 7 | Moderna, Inc. | `MRNA` | 72 | 0 | **72** | **WATCH** |
| 8 | IREN LIMITED | `IREN` | 72 | 0 | **72** | **WATCH** |
| 9 | Lumentum Holdings Inc. | `LITE` | 67 | 0 | **67** | **WATCH** |
| 10 | Okta, Inc. | `OKTA` | 80 | 13 | **60** | **WATCH** |

## P/E Compression + Growth — LONG

| Rank | Company | OKX | Trail P/E | Fwd P/E | P/E change | EPS +1y | Rev +1y | Rev trend | LONG score | Signal |
|---:|---|---|---:|---:|---:|---:|---:|---|---:|---|
| 1 | Broadcom Inc. | `AVGO` | 46.3 | 18.7 | -59.6% | 66.4% | 64.1% | decelerating | **100** | **CORE** |
| 2 | Advanced Micro Devices, Inc. | `AMD` | 161.2 | 40.2 | -75.1% | 107.2% | 74.5% | accelerating | **100** | **CORE** |
| 3 | Marvell Technology, Inc. | `MRVL` | 89.2 | 40.2 | -55.0% | 60.3% | 50.9% | accelerating | **100** | **CORE** |
| 4 | Credo Technology Group Holding  | `CRDO` | 75.3 | 21.9 | -70.9% | 53.7% | 54.8% | decelerating | **96** | **CORE** |
| 5 | Oracle Corporation | `ORCL` | 22.3 | 13.0 | -42.0% | 35.1% | 45.6% | accelerating | **95** | **CORE** |
| 6 | Corning Incorporated | `GLW` | 73.1 | 36.5 | -50.1% | 33.0% | 19.3% | accelerating | **92** | **CORE** |
| 7 | AXT Inc | `AXT` | 2166.5 | 38.5 | -98.2% | 159.2% | 111.3% | decelerating | **92** | **CORE** |
| 8 | Applied Materials, Inc. | `AMAT` | 46.8 | 29.4 | -37.2% | 44.4% | 34.8% | accelerating | **91** | **CORE** |
| 9 | Coherent Corp. | `COHR` | 81.0 | 23.8 | -70.7% | 49.1% | 38.8% | decelerating | **91** | **CORE** |
| 10 | NVIDIA Corporation | `NVDA` | 30.2 | 15.1 | -49.9% | 69.7% | 67.0% | decelerating | **90** | **CORE** |

## P/E Expansion + Weakening — SHORT

| Rank | Company | OKX | Trail P/E | Fwd P/E | P/E change | EPS +1y | Rev +1y | Rev trend | SHORT score | Signal |
|---:|---|---|---:|---:|---:|---:|---:|---|---:|---|
| 1 | SOFTBANK GROUP CORP | `SOFTBANK` | 7.0 | 21.4 | 204.2% | -39.0% | 6.9% | decelerating | **86** | **CORE** |
| 2 | Alphabet Inc. | `GOOGL` | 17.4 | 23.0 | 32.2% | -27.6% | 23.3% | decelerating | **70** | **CORE** |
| 3 | Hyperliquid Strategies Inc | `PURI` | 4.0 | 34.9 | 767.6% | 51.0% | 33.4% | decelerating | **55** | **WATCH** |
| 4 | Amazon.com, Inc. | `AMZN` | 20.2 | 24.0 | 18.7% | -18.4% | 14.4% | decelerating | **52** | **WATCH** |

## Top SHORT candidates

| Rank | Company | OKX market | SHORT score | Signal | P/S | EV/S | Op margin | Fwd P/E | Rev +1y | FCF yield |
|---:|---|---|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Rocket Lab Corporation | `RKLB-USDT-SWAP` | **100** | **CORE** | 60.7 | 54.0 | -24.6% | 1352.5 | 41.6% | -0.5% |
| 2 | USA Rare Earth, Inc. | `USAR-USDT-SWAP` | **100** | **CORE** | 389.0 | 138.5 | -795.6% | 455.0 | 870.1% | -5.5% |
| 3 | Cerebras Systems Inc. | `CBRS-USDT-SWAP` | **100** | **CORE** | 63.4 | 53.9 | -265.0% | 142.5 | 232.7% | — |
| 4 | IonQ, Inc. | `IONQ-USDT-SWAP` | **91** | **CORE** | 70.6 | 58.1 | -408.2% | -33.2 | 79.0% | -0.5% |
| 5 | Nebius Group N.V. | `NBIS-USDT-SWAP` | **90** | **CORE** | 43.6 | 48.6 | -0.2% | -66.6 | 268.8% | -16.3% |
| 6 | Okta, Inc. | `OKTA-USDT-SWAP` | **80** | **CORE** | 12.4 | 11.7 | 13.3% | 49.9 | 10.0% | 2.7% |
| 7 | AST SpaceMobile, Inc. | `ASTS-USDT-SWAP` | **80** | **WATCH** | 197.3 | 162.4 | -544.6% | -45.4 | 259.9% | -7.9% |
| 8 | IREN LIMITED | `IREN-USDT-SWAP` | **72** | **WATCH** | 22.6 | 25.3 | -102.5% | -10.2 | 160.9% | -26.5% |
| 9 | Moderna, Inc. | `MRNA-USDT-SWAP` | **72** | **WATCH** | 36.4 | 34.7 | -557.9% | -45.7 | 15.8% | 0.4% |
| 10 | Lumentum Holdings Inc. | `LITE-USDT-SWAP` | **67** | **WATCH** | 32.5 | 32.1 | 28.0% | 30.7 | 55.5% | 0.2% |

## Top LONG candidates

| Rank | Company | OKX market | LONG score | Signal | P/S | EV/S | Op margin | Fwd P/E | Rev +1y | FCF yield |
|---:|---|---|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Applovin Corporation | `APP-USDT-SWAP` | **83** | **CORE** | 13.8 | 13.9 | 77.7% | 13.4 | 26.6% | 3.4% |
| 2 | Taiwan Semiconductor Manufactur | `TSM-USDT-SWAP` | **82** | **CORE** | 0.6 | 4.0 | 60.3% | 22.2 | 34.8% | 29.0% |
| 3 | Applied Materials, Inc. | `AMAT-USDT-SWAP` | **77** | **WATCH** | 14.0 | 13.9 | 33.7% | 29.4 | 34.8% | 0.7% |
| 4 | Broadcom Inc. | `AVGO-USDT-SWAP` | **75** | **WATCH** | 19.4 | 19.8 | 54.3% | 18.7 | 64.1% | 1.8% |
| 5 | Sandisk Corporation | `SNDK-USDT-SWAP` | **75** | **CORE** | 12.3 | 12.1 | 78.5% | 6.5 | 18.3% | 3.1% |
| 6 | Western Digital Corporation | `WDC-USDT-SWAP` | **75** | **WATCH** | 12.3 | 12.3 | 43.6% | 13.9 | 36.8% | 1.4% |
| 7 | NVIDIA Corporation | `NVDA-USDT-SWAP` | **75** | **WATCH** | 19.0 | 18.9 | 66.2% | 15.1 | 67.0% | 0.7% |
| 8 | Robinhood Markets, Inc. | `HOOD-USDT-SWAP` | **70** | **WATCH** | 20.8 | 20.6 | 43.9% | 33.2 | 28.3% | — |
| 9 | XIAOMI-W | `XIAOMI-USDT-SWAP` | **70** | **WATCH** | 1.4 | 1.2 | 4.0% | 15.7 | 24.1% | -1.4% |
| 10 | Oracle Corporation | `ORCL-USDT-SWAP` | **70** | **WATCH** | 6.0 | 7.9 | 35.6% | 13.0 | 45.6% | -10.6% |

## All OKX companies — our ratio + LONG/SHORT scores

| Company | OKX | P/S | EV/S | Op margin | Fwd P/E | EPS +1y | Rev +1y | FCF yield | LONG | SHORT |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Cerebras Systems Inc. | `CBRS` | 63.4 | 53.9 | -265.0% | 142.5 | 371.3% | 232.7% | — | **0** | **100 CORE** |
| Rocket Lab Corporation | `RKLB` | 60.7 | 54.0 | -24.6% | 1352.5 | 68.1% | 41.6% | -0.5% | **0** | **100 CORE** |
| USA Rare Earth, Inc. | `USAR` | 389.0 | 138.5 | -795.6% | 455.0 | 105.3% | 870.1% | -5.5% | **0** | **100 CORE** |
| IonQ, Inc. | `IONQ` | 70.6 | 58.1 | -408.2% | -33.2 | 18.1% | 79.0% | -0.5% | **0** | **91 CORE** |
| Nebius Group N.V. | `NBIS` | 43.6 | 48.6 | -0.2% | -66.6 | -147.8% | 268.8% | -16.3% | **0** | **90 CORE** |
| Applovin Corporation | `APP` | 13.8 | 13.9 | 77.7% | 13.4 | 27.7% | 26.6% | 3.4% | **83 CORE** | **10** |
| Taiwan Semiconductor Manufactur | `TSM` | 0.6 | 4.0 | 60.3% | 22.2 | 30.0% | 34.8% | 29.0% | **82 CORE** | **10** |
| Okta, Inc. | `OKTA` | 12.4 | 11.7 | 13.3% | 49.9 | 11.4% | 10.0% | 2.7% | **8** | **80 CORE** |
| AST SpaceMobile, Inc. | `ASTS` | 197.3 | 162.4 | -544.6% | -45.4 | 47.7% | 259.9% | -7.9% | **0** | **80 WATCH** |
| Applied Materials, Inc. | `AMAT` | 14.0 | 13.9 | 33.7% | 29.4 | 44.4% | 34.8% | 0.7% | **77 WATCH** | **13** |
| Broadcom Inc. | `AVGO` | 19.4 | 19.8 | 54.3% | 18.7 | 66.4% | 64.1% | 1.8% | **75 WATCH** | **28** |
| Sandisk Corporation | `SNDK` | 12.3 | 12.1 | 78.5% | 6.5 | 23.2% | 18.3% | 3.1% | **75 CORE** | **10** |
| NVIDIA Corporation | `NVDA` | 19.0 | 18.9 | 66.2% | 15.1 | 69.7% | 67.0% | 0.7% | **75 WATCH** | **18** |
| Western Digital Corporation | `WDC` | 12.3 | 12.3 | 43.6% | 13.9 | 58.0% | 36.8% | 1.4% | **75 WATCH** | **18** |
| Moderna, Inc. | `MRNA` | 36.4 | 34.7 | -557.9% | -45.7 | 42.9% | 15.8% | 0.4% | **0** | **72 WATCH** |
| IREN LIMITED | `IREN` | 22.6 | 25.3 | -102.5% | -10.2 | -16.4% | 160.9% | -26.5% | **0** | **72 WATCH** |
| Robinhood Markets, Inc. | `HOOD` | 20.8 | 20.6 | 43.9% | 33.2 | 34.6% | 28.3% | — | **70 WATCH** | **5** |
| Oracle Corporation | `ORCL` | 6.0 | 7.9 | 35.6% | 13.0 | 35.1% | 45.6% | -10.6% | **70 WATCH** | **10** |
| XIAOMI-W | `XIAOMI` | 1.4 | 1.2 | 4.0% | 15.7 | 39.6% | 24.1% | -1.4% | **70 WATCH** | **10** |
| Credo Technology Group Holding  | `CRDO` | 25.1 | 24.6 | 25.2% | 21.9 | 53.7% | 54.8% | 0.6% | **67 WATCH** | **28** |
| Lumentum Holdings Inc. | `LITE` | 32.5 | 32.1 | 28.0% | 30.7 | 63.3% | 55.5% | 0.2% | **0** | **67 WATCH** |
| Advanced Micro Devices, Inc. | `AMD` | 25.0 | 24.8 | 17.2% | 40.2 | 107.2% | 74.5% | 0.9% | **65 WATCH** | **33** |
| Marvell Technology, Inc. | `MRVL` | 25.8 | 25.3 | 16.7% | 40.2 | 60.3% | 50.9% | 1.0% | **65 WATCH** | **33** |
| Adobe Inc. | `ADBE` | 3.6 | 3.6 | 34.8% | 8.6 | 13.0% | 9.2% | 10.1% | **65 WATCH** | **30** |
| Tesla, Inc. | `TSLA` | 14.4 | 14.2 | 1.4% | 176.6 | 24.6% | 13.5% | 0.3% | **22** | **63 WATCH** |
| Micron Technology, Inc. | `MU` | 9.0 | 8.7 | 80.7% | 5.1 | 17.2% | 14.3% | 2.4% | **62 WATCH** | **38** |
| Corning Incorporated | `GLW` | 8.1 | 8.5 | 15.6% | 36.5 | 33.0% | 19.3% | 0.5% | **60 WATCH** | **13** |
| Microsoft Corporation | `MSFT` | 11.8 | 11.9 | 45.1% | 22.2 | 19.8% | 19.6% | 0.4% | **59 WATCH** | **23** |
| Dell Technologies Inc. | `DELL` | 2.3 | 2.5 | 12.0% | 19.0 | 0.8% | 16.5% | 1.7% | **25** | **58** |
| Coca-Cola Company (The) | `KO` | 7.4 | 8.0 | 34.9% | 24.5 | 6.8% | 0.3% | 1.4% | **7** | **58** |
| Apple Inc. | `AAPL` | 10.4 | 10.5 | 32.6% | 34.7 | 8.6% | 10.5% | 2.2% | **5** | **58** |
| Bloom Energy Corporation | `BE` | 27.1 | 27.2 | 17.1% | 58.0 | 82.6% | 65.0% | 0.6% | **55 WATCH** | **48** |
| Arm Holdings plc | `ARM` | 62.7 | 62.1 | 7.6% | 98.9 | 37.5% | 36.2% | 0.4% | **35** | **53** |
| Coherent Corp. | `COHR` | 9.2 | 9.4 | 11.8% | 23.8 | 49.1% | 38.8% | -1.0% | **52** | **35** |
| Super Micro Computer, Inc. | `SMCI` | 0.7 | 0.9 | 13.4% | 8.1 | 22.8% | 17.3% | -29.5% | **52** | **25** |
| Palantir Technologies Inc. | `PLTR` | 73.9 | 72.5 | 47.1% | 80.8 | 44.7% | 49.7% | 0.5% | **33** | **48** |
| Intel Corporation | `INTC` | 10.8 | 10.9 | 12.2% | 56.3 | 36.9% | 14.8% | 0.8% | **5** | **48** |
| AXT Inc | `AXT` | 45.3 | 42.4 | 21.9% | 38.5 | 159.2% | 111.3% | -0.8% | **45** | **35** |
| SK hynix | `SKHYNIX` | 6.7 | 6.6 | 76.3% | 3.8 | 33.1% | 54.1% | 4.4% | **45** | **5** |
| SK hynix | `SKHY` | 6.7 | 6.6 | 76.3% | 3.8 | 33.1% | 54.1% | 4.4% | **45** | **5** |
| Applied Optoelectronics, Inc. | `AAOI` | 17.3 | 16.9 | -12.9% | 26.4 | 576.8% | 156.5% | -8.6% | **0** | **45** |
| Coinbase Global, Inc. | `COIN` | 8.2 | 7.9 | -13.9% | 66.5 | 245.9% | 29.3% | 5.4% | **20** | **40** |
| SOFTBANK GROUP CORP | `SOFTBANK` | 4.5 | 8.0 | -11.6% | 21.4 | -39.0% | 6.9% | -6.1% | **0** | **40** |
| CoreWeave, Inc. | `CRWV` | 6.4 | 12.4 | -1.9% | -48.3 | 15.4% | 104.1% | -18.9% | **0** | **40** |
| SamsungElec | `SAMSUNG` | 3.7 | 3.4 | 52.2% | 3.9 | 47.7% | 34.2% | 3.9% | **38** | **10** |
| Meta Platforms, Inc. | `META` | 8.3 | 8.4 | 34.8% | 21.3 | 9.3% | 20.6% | 1.1% | **17** | **38** |
| Alphabet Inc. | `GOOGL` | 9.5 | 9.3 | 34.0% | 23.0 | -27.6% | 23.3% | 0.5% | **2** | **38** |
| Amazon.com, Inc. | `AMZN` | 3.5 | 3.7 | 13.7% | 24.0 | -18.4% | 14.4% | 0.1% | **0** | **38** |
| Circle Internet Group, Inc. | `CRCL` | 7.3 | 6.7 | 4.9% | 59.0 | 29.3% | 23.7% | 1.0% | **35** | **33** |
| Fluence Energy, Inc. | `FLNC` | 0.6 | 0.5 | -8.9% | -28.7 | 70.1% | 35.3% | 0.2% | **5** | **28** |
| Hyperliquid Strategies Inc | `PURI` | 324.9 | 255.6 | 9595.1% | 34.9 | 51.0% | 33.4% | — | **25** | **10** |
| Strategy Inc | `MSTR` | 131.6 | 164.4 | -6808.1% | 3.3 | 157.5% | 2.2% | -34.4% | **25** | **25** |
| BitMine Immersion Technologies, | `BMNR` | 264.1 | 258.6 | 8.4% | 28.5 | 103.2% | 421.8% | -3.2% | **25** | **25** |
| QUALCOMM Incorporated | `QCOM` | 4.4 | 4.5 | 18.5% | 17.7 | -2.7% | 4.8% | 5.3% | **25** | **15** |

## Files

- `scanner.py` — scanner and scoring logic
- `reports/latest.md` — latest full report
- `data/latest.csv` — latest machine-readable snapshot
- `data/history.csv` — hourly history of **all companies** for later backtests
- `.github/workflows/hourly-okx-scanner.yml` — hourly GitHub Action

## Data

The configured universe can be pinned to the exact OKX EEA xStocks/USDC markets confirmed in the user's app. When that allowlist is present it overrides the broader public catalogue. Yahoo Finance/yfinance supplies company valuation, cash-flow and analyst-growth estimates. ETFs can exist in the OKX universe but are excluded from the company-fundamentals ranking.

### Optional account-accurate filter

Add read-only GitHub Actions secrets `OKX_API_KEY`, `OKX_API_SECRET`, and `OKX_API_PASSPHRASE`. The scanner will then query the authenticated OKX EEA account-instruments endpoint and only score contracts available to that account. Do not grant Trade or Withdraw permission for this scanner.

This is a quantitative research screen, not an automatic trading system. It does not place orders or select leverage.
