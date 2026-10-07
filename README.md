# OKX Long / Short Fundamental Scanner

Hourly scanner restricted to public companies exposed by the **OKX EEA TradFi / Stock Perpetual API universe**.

**Last scan:** 2026-10-07 16:36 UTC  
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
| 1 | Applovin Corporation | APP | -1.1% | -5.0% | -3.1% | 82 | +2 | **84** | **CORE** | yes |
| 2 | NVIDIA Corporation | NVDA | -0.9% | 3.8% | 1.5% | 82 | -1 | **81** | **CORE** | yes |
| 3 | Taiwan Semiconductor Manufactur | TSM | -2.0% | 3.6% | 0.8% | 82 | -1 | **81** | **CORE** | yes |
| 4 | Applied Materials, Inc. | AMAT | -1.6% | 2.0% | 0.2% | 81 | +0 | **81** | **CORE** | yes |
| 5 | Broadcom Inc. | AVGO | -0.6% | 6.4% | 2.9% | 82 | -2 | **80** | **CORE** | yes |
| 6 | Marvell Technology, Inc. | MRVL | — | — | — | 79 | +0 | **79** | **CORE** | yes |
| 7 | Western Digital Corporation | WDC | -1.8% | -11.2% | -6.5% | 74 | +5 | **79** | **CORE** | yes |
| 8 | Robinhood Markets, Inc. | HOOD | -2.6% | -3.0% | -2.8% | 75 | +2 | **77** | **CORE** | yes |
| 9 | Oracle Corporation | ORCL | -0.5% | 4.9% | 2.2% | 78 | -2 | **76** | **CORE** | yes |
| 10 | Sandisk Corporation | SNDK | 3.5% | -1.2% | 1.1% | 77 | -1 | **76** | **CORE** | yes |

## Final model + Price Timing — SHORT

| Rank | Company | OKX | 24h | 7d | 50/50 move | Base SHORT | Timing adj. | Final | Signal | Prev. SHORT? |
|---:|---|---|---:|---:|---:|---:|---:|---:|---|---|
| 1 | Cerebras Systems Inc. | CBRS | -2.0% | -2.3% | -2.1% | 100 | -2 | **98** | **CORE** | yes |
| 2 | Rocket Lab Corporation | RKLB | -5.6% | 1.7% | -2.0% | 100 | -2 | **98** | **CORE** | yes |
| 3 | USA Rare Earth, Inc. | USAR | -4.2% | -6.5% | -5.4% | 100 | -4 | **96** | **CORE** | yes |
| 4 | Nebius Group N.V. | NBIS | -6.0% | -0.4% | -3.2% | 93 | -3 | **90** | **CORE** | yes |
| 5 | IonQ, Inc. | IONQ | -5.5% | -6.7% | -6.1% | 91 | -5 | **86** | **CORE** | yes |
| 6 | AST SpaceMobile, Inc. | ASTS | -6.1% | 0.7% | -2.7% | 80 | -2 | **78** | **CORE** | yes |
| 7 | Moderna, Inc. | MRNA | 2.4% | -0.3% | 1.1% | 72 | +1 | **73** | **WATCH** | yes |
| 8 | Lumentum Holdings Inc. | LITE | -2.7% | 13.5% | 5.4% | 67 | +4 | **71** | **WATCH** | yes |
| 9 | IREN LIMITED | IREN | -6.5% | -5.6% | -6.1% | 72 | -5 | **67** | **WATCH** | yes |
| 10 | Okta, Inc. | OKTA | -0.5% | 4.0% | 1.7% | 60 | +1 | **61** | **WATCH** | yes |

## Combined model — LONG

Weighted score: **70% fundamental + 30% P/E trend**.

| Rank | Company | OKX | Fundamental LONG | P/E trend LONG | Combined | Signal |
|---:|---|---|---:|---:|---:|---|
| 1 | Applovin Corporation | `APP` | 83 | 80 | **82** | **CORE** |
| 2 | Taiwan Semiconductor Manufactur | `TSM` | 82 | 81 | **82** | **CORE** |
| 3 | NVIDIA Corporation | `NVDA` | 75 | 100 | **82** | **CORE** |
| 4 | Broadcom Inc. | `AVGO` | 75 | 100 | **82** | **CORE** |
| 5 | Applied Materials, Inc. | `AMAT` | 77 | 91 | **81** | **CORE** |
| 6 | Marvell Technology, Inc. | `MRVL` | 70 | 100 | **79** | **CORE** |
| 7 | Oracle Corporation | `ORCL` | 70 | 95 | **78** | **CORE** |
| 8 | Sandisk Corporation | `SNDK` | 75 | 82 | **77** | **CORE** |
| 9 | Credo Technology Group Holding  | `CRDO` | 67 | 96 | **76** | **CORE** |
| 10 | Advanced Micro Devices, Inc. | `AMD` | 65 | 100 | **76** | **CORE** |

## Combined model — SHORT

Weighted score: **70% fundamental + 30% P/E trend**.

| Rank | Company | OKX | Fundamental SHORT | P/E trend SHORT | Combined | Signal |
|---:|---|---|---:|---:|---:|---|
| 1 | Cerebras Systems Inc. | `CBRS` | 100 | 0 | **100** | **CORE** |
| 2 | Rocket Lab Corporation | `RKLB` | 100 | 0 | **100** | **CORE** |
| 3 | USA Rare Earth, Inc. | `USAR` | 100 | 0 | **100** | **CORE** |
| 4 | Nebius Group N.V. | `NBIS` | 93 | 0 | **93** | **CORE** |
| 5 | IonQ, Inc. | `IONQ` | 91 | 0 | **91** | **CORE** |
| 6 | AST SpaceMobile, Inc. | `ASTS` | 80 | 0 | **80** | **WATCH** |
| 7 | Moderna, Inc. | `MRNA` | 72 | 0 | **72** | **WATCH** |
| 8 | IREN LIMITED | `IREN` | 72 | 0 | **72** | **WATCH** |
| 9 | Lumentum Holdings Inc. | `LITE` | 67 | 0 | **67** | **WATCH** |
| 10 | Okta, Inc. | `OKTA` | 80 | 13 | **60** | **WATCH** |

## P/E Compression + Growth — LONG

| Rank | Company | OKX | Trail P/E | Fwd P/E | P/E change | EPS +1y | Rev +1y | Rev trend | LONG score | Signal |
|---:|---|---|---:|---:|---:|---:|---:|---|---:|---|
| 1 | NVIDIA Corporation | `NVDA` | 30.0 | 14.9 | -50.3% | 70.9% | 68.2% | decelerating | **100** | **CORE** |
| 2 | Broadcom Inc. | `AVGO` | 46.0 | 19.3 | -58.1% | 66.4% | 64.1% | decelerating | **100** | **CORE** |
| 3 | Marvell Technology, Inc. | `MRVL` | 92.6 | 39.2 | -57.7% | 70.9% | 62.7% | accelerating | **100** | **CORE** |
| 4 | Advanced Micro Devices, Inc. | `AMD` | 163.8 | 40.8 | -75.1% | 107.2% | 74.6% | accelerating | **100** | **CORE** |
| 5 | Credo Technology Group Holding  | `CRDO` | 75.7 | 22.0 | -70.9% | 53.7% | 54.8% | decelerating | **96** | **CORE** |
| 6 | Oracle Corporation | `ORCL` | 22.6 | 13.1 | -42.0% | 35.1% | 45.6% | accelerating | **95** | **CORE** |
| 7 | Corning Incorporated | `GLW` | 75.9 | 37.9 | -50.1% | 33.0% | 19.3% | accelerating | **92** | **CORE** |
| 8 | AXT Inc | `AXT` | 2033.0 | 36.1 | -98.2% | 159.2% | 111.3% | decelerating | **92** | **CORE** |
| 9 | Applied Materials, Inc. | `AMAT` | 45.0 | 28.2 | -37.2% | 44.4% | 34.8% | accelerating | **91** | **CORE** |
| 10 | Coherent Corp. | `COHR` | 78.9 | 23.2 | -70.7% | 49.1% | 38.8% | decelerating | **91** | **CORE** |

## P/E Expansion + Weakening — SHORT

| Rank | Company | OKX | Trail P/E | Fwd P/E | P/E change | EPS +1y | Rev +1y | Rev trend | SHORT score | Signal |
|---:|---|---|---:|---:|---:|---:|---:|---|---:|---|
| 1 | SOFTBANK GROUP CORP | `SOFTBANK` | 7.2 | 21.4 | 195.5% | -14.5% | 6.9% | decelerating | **86** | **CORE** |
| 2 | Alphabet Inc. | `GOOGL` | 17.4 | 23.0 | 32.2% | -27.6% | 23.3% | decelerating | **70** | **CORE** |
| 3 | Hyperliquid Strategies Inc | `PURI` | 3.7 | 32.0 | 767.6% | 51.0% | 31.4% | decelerating | **55** | **WATCH** |
| 4 | Amazon.com, Inc. | `AMZN` | 20.8 | 24.7 | 18.8% | -18.4% | 14.5% | decelerating | **52** | **WATCH** |

## Top SHORT candidates

| Rank | Company | OKX market | SHORT score | Signal | P/S | EV/S | Op margin | Fwd P/E | Rev +1y | FCF yield |
|---:|---|---|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Rocket Lab Corporation | `RKLB-USDT-SWAP` | **100** | **CORE** | 58.9 | 55.6 | -24.6% | 1312.2 | 41.6% | -0.6% |
| 2 | USA Rare Earth, Inc. | `USAR-USDT-SWAP` | **100** | **CORE** | 375.0 | 140.2 | -795.6% | 438.7 | 870.1% | -5.8% |
| 3 | Cerebras Systems Inc. | `CBRS-USDT-SWAP` | **100** | **CORE** | 60.6 | 52.4 | -265.0% | 136.3 | 232.7% | — |
| 4 | Nebius Group N.V. | `NBIS-USDT-SWAP` | **93** | **CORE** | 47.1 | 52.1 | -0.2% | -67.3 | 268.8% | -15.1% |
| 5 | IonQ, Inc. | `IONQ-USDT-SWAP` | **91** | **CORE** | 67.2 | 58.6 | -408.2% | -31.6 | 79.0% | -0.5% |
| 6 | Okta, Inc. | `OKTA-USDT-SWAP` | **80** | **CORE** | 12.4 | 11.7 | 13.3% | 49.7 | 10.0% | 2.7% |
| 7 | AST SpaceMobile, Inc. | `ASTS-USDT-SWAP` | **80** | **WATCH** | 200.1 | 174.6 | -544.6% | -46.1 | 259.9% | -7.8% |
| 8 | IREN LIMITED | `IREN-USDT-SWAP` | **72** | **WATCH** | 21.5 | 25.8 | -102.5% | -9.7 | 160.9% | -27.8% |
| 9 | Moderna, Inc. | `MRNA-USDT-SWAP` | **72** | **WATCH** | 34.4 | 31.9 | -557.9% | -43.1 | 15.8% | 0.4% |
| 10 | Lumentum Holdings Inc. | `LITE-USDT-SWAP` | **67** | **WATCH** | 32.8 | 33.4 | 28.0% | 31.0 | 55.5% | 0.2% |

## Top LONG candidates

| Rank | Company | OKX market | LONG score | Signal | P/S | EV/S | Op margin | Fwd P/E | Rev +1y | FCF yield |
|---:|---|---|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Applovin Corporation | `APP-USDT-SWAP` | **83** | **CORE** | 13.6 | 13.7 | 77.7% | 13.1 | 26.6% | 3.4% |
| 2 | Taiwan Semiconductor Manufactur | `TSM-USDT-SWAP` | **82** | **CORE** | 0.6 | 4.0 | 60.3% | 21.6 | 35.0% | 29.8% |
| 3 | Applied Materials, Inc. | `AMAT-USDT-SWAP` | **77** | **WATCH** | 13.4 | 13.6 | 33.7% | 28.2 | 34.8% | 0.7% |
| 4 | Broadcom Inc. | `AVGO-USDT-SWAP` | **75** | **WATCH** | 20.0 | 20.5 | 54.3% | 19.3 | 64.1% | 1.7% |
| 5 | Sandisk Corporation | `SNDK-USDT-SWAP` | **75** | **CORE** | 12.4 | 11.8 | 78.5% | 6.5 | 18.8% | 3.1% |
| 6 | Western Digital Corporation | `WDC-USDT-SWAP` | **75** | **WATCH** | 11.7 | 11.4 | 43.6% | 12.7 | 36.9% | 1.5% |
| 7 | NVIDIA Corporation | `NVDA-USDT-SWAP` | **75** | **WATCH** | 18.9 | 19.0 | 66.2% | 14.9 | 68.2% | 0.7% |
| 8 | Robinhood Markets, Inc. | `HOOD-USDT-SWAP` | **70** | **WATCH** | 19.9 | 20.2 | 43.9% | 31.7 | 28.6% | — |
| 9 | Marvell Technology, Inc. | `MRVL-USDT-SWAP` | **70** | **WATCH** | 26.8 | 26.8 | 16.7% | 39.2 | 62.7% | 1.0% |
| 10 | XIAOMI-W | `XIAOMI-USDT-SWAP` | **70** | **WATCH** | 1.4 | 1.2 | 4.0% | 15.6 | 24.1% | -1.4% |

## All OKX companies — our ratio + LONG/SHORT scores

| Company | OKX | P/S | EV/S | Op margin | Fwd P/E | EPS +1y | Rev +1y | FCF yield | LONG | SHORT |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Cerebras Systems Inc. | `CBRS` | 60.6 | 52.4 | -265.0% | 136.3 | 371.3% | 232.7% | — | **0** | **100 CORE** |
| Rocket Lab Corporation | `RKLB` | 58.9 | 55.6 | -24.6% | 1312.2 | 68.1% | 41.6% | -0.6% | **0** | **100 CORE** |
| USA Rare Earth, Inc. | `USAR` | 375.0 | 140.2 | -795.6% | 438.7 | 105.3% | 870.1% | -5.8% | **0** | **100 CORE** |
| Nebius Group N.V. | `NBIS` | 47.1 | 52.1 | -0.2% | -67.3 | -147.8% | 268.8% | -15.1% | **0** | **93 CORE** |
| IonQ, Inc. | `IONQ` | 67.2 | 58.6 | -408.2% | -31.6 | 18.1% | 79.0% | -0.5% | **0** | **91 CORE** |
| Applovin Corporation | `APP` | 13.6 | 13.7 | 77.7% | 13.1 | 27.7% | 26.6% | 3.4% | **83 CORE** | **10** |
| Taiwan Semiconductor Manufactur | `TSM` | 0.6 | 4.0 | 60.3% | 21.6 | 30.0% | 35.0% | 29.8% | **82 CORE** | **10** |
| Okta, Inc. | `OKTA` | 12.4 | 11.7 | 13.3% | 49.7 | 11.4% | 10.0% | 2.7% | **8** | **80 CORE** |
| AST SpaceMobile, Inc. | `ASTS` | 200.1 | 174.6 | -544.6% | -46.1 | 47.7% | 259.9% | -7.8% | **0** | **80 WATCH** |
| Applied Materials, Inc. | `AMAT` | 13.4 | 13.6 | 33.7% | 28.2 | 44.4% | 34.8% | 0.7% | **77 WATCH** | **13** |
| NVIDIA Corporation | `NVDA` | 18.9 | 19.0 | 66.2% | 14.9 | 70.9% | 68.2% | 0.7% | **75 WATCH** | **18** |
| Broadcom Inc. | `AVGO` | 20.0 | 20.5 | 54.3% | 19.3 | 66.4% | 64.1% | 1.7% | **75 WATCH** | **28** |
| Western Digital Corporation | `WDC` | 11.7 | 11.4 | 43.6% | 12.7 | 58.2% | 36.9% | 1.5% | **75 WATCH** | **18** |
| Sandisk Corporation | `SNDK` | 12.4 | 11.8 | 78.5% | 6.5 | 23.7% | 18.8% | 3.1% | **75 CORE** | **10** |
| Moderna, Inc. | `MRNA` | 34.4 | 31.9 | -557.9% | -43.1 | 42.9% | 15.8% | 0.4% | **0** | **72 WATCH** |
| IREN LIMITED | `IREN` | 21.5 | 25.8 | -102.5% | -9.7 | -16.4% | 160.9% | -27.8% | **0** | **72 WATCH** |
| Marvell Technology, Inc. | `MRVL` | 26.8 | 26.8 | 16.7% | 39.2 | 70.9% | 62.7% | 1.0% | **70 WATCH** | **13** |
| Robinhood Markets, Inc. | `HOOD` | 19.9 | 20.2 | 43.9% | 31.7 | 35.3% | 28.6% | — | **70 WATCH** | **5** |
| Oracle Corporation | `ORCL` | 6.1 | 8.0 | 35.6% | 13.1 | 35.1% | 45.6% | -10.5% | **70 WATCH** | **10** |
| XIAOMI-W | `XIAOMI` | 1.4 | 1.2 | 4.0% | 15.6 | 39.6% | 24.1% | -1.4% | **70 WATCH** | **10** |
| Credo Technology Group Holding  | `CRDO` | 25.2 | 25.6 | 25.2% | 22.0 | 53.7% | 54.8% | 0.6% | **67 WATCH** | **28** |
| Micron Technology, Inc. | `MU` | 9.1 | 8.6 | 80.7% | 5.2 | 17.1% | 16.0% | 2.4% | **67 WATCH** | **38** |
| Lumentum Holdings Inc. | `LITE` | 32.8 | 33.4 | 28.0% | 31.0 | 63.3% | 55.5% | 0.2% | **0** | **67 WATCH** |
| Advanced Micro Devices, Inc. | `AMD` | 25.4 | 25.5 | 17.2% | 40.8 | 107.2% | 74.6% | 0.8% | **65 WATCH** | **33** |
| Adobe Inc. | `ADBE` | 3.5 | 3.6 | 34.8% | 8.4 | 13.0% | 9.2% | 10.4% | **65 WATCH** | **30** |
| Tesla, Inc. | `TSLA` | 14.3 | 14.3 | 1.4% | 175.2 | 23.2% | 13.4% | 0.3% | **22** | **63 WATCH** |
| Corning Incorporated | `GLW` | 8.4 | 9.0 | 15.6% | 37.9 | 33.0% | 19.3% | 0.5% | **60 WATCH** | **13** |
| Microsoft Corporation | `MSFT` | 11.8 | 12.0 | 45.1% | 22.3 | 19.8% | 19.6% | 0.4% | **59 WATCH** | **23** |
| Dell Technologies Inc. | `DELL` | 2.4 | 2.6 | 12.0% | 19.9 | 0.8% | 16.5% | 1.6% | **25** | **58** |
| Coca-Cola Company (The) | `KO` | 7.4 | 8.0 | 34.9% | 24.5 | 6.8% | 0.2% | 1.4% | **7** | **58** |
| Apple Inc. | `AAPL` | 10.5 | 10.5 | 32.6% | 35.0 | 8.6% | 10.5% | 2.2% | **5** | **58** |
| Bloom Energy Corporation | `BE` | 27.1 | 28.0 | 17.1% | 58.0 | 82.6% | 65.0% | 0.6% | **55 WATCH** | **48** |
| Arm Holdings plc | `ARM` | 61.6 | 62.0 | 7.6% | 97.1 | 37.5% | 36.2% | 0.4% | **35** | **53** |
| Coherent Corp. | `COHR` | 8.9 | 9.6 | 11.8% | 23.2 | 49.1% | 38.8% | -1.0% | **52** | **35** |
| Super Micro Computer, Inc. | `SMCI` | 0.7 | 0.9 | 13.4% | 8.3 | 22.8% | 17.3% | -28.3% | **52** | **25** |
| Palantir Technologies Inc. | `PLTR` | 75.4 | 73.5 | 47.1% | 82.4 | 44.7% | 49.7% | 0.5% | **33** | **48** |
| Intel Corporation | `INTC` | 10.5 | 10.6 | 12.2% | 54.3 | 36.9% | 14.8% | 0.8% | **5** | **48** |
| AXT Inc | `AXT` | 42.5 | 41.0 | 21.9% | 36.1 | 159.2% | 111.3% | -0.8% | **45** | **35** |
| SK hynix | `SKHYNIX` | 6.5 | 6.1 | 76.3% | 3.7 | 32.9% | 54.3% | 4.6% | **45** | **5** |
| SK hynix | `SKHY` | 6.5 | 6.1 | 76.3% | 3.7 | 32.9% | 54.3% | 4.6% | **45** | **5** |
| Applied Optoelectronics, Inc. | `AAOI` | 17.3 | 18.1 | -12.9% | 26.3 | 576.8% | 156.5% | -8.6% | **0** | **45** |
| Circle Internet Group, Inc. | `CRCL` | 7.1 | 6.8 | 4.9% | 57.4 | 30.6% | 24.7% | 1.0% | **43** | **33** |
| Coinbase Global, Inc. | `COIN` | 7.9 | 7.8 | -13.9% | 63.6 | 254.8% | 29.3% | 5.6% | **20** | **40** |
| SOFTBANK GROUP CORP | `SOFTBANK` | 4.5 | 7.8 | -11.6% | 21.4 | -14.5% | 6.9% | -6.1% | **0** | **40** |
| CoreWeave, Inc. | `CRWV` | 6.4 | 12.7 | -1.9% | -48.5 | 15.4% | 104.1% | -18.7% | **0** | **40** |
| SamsungElec | `SAMSUNG` | 3.6 | 3.3 | 52.2% | 3.8 | 49.5% | 35.2% | 3.9% | **38** | **10** |
| Meta Platforms, Inc. | `META` | 8.1 | 8.3 | 34.8% | 20.8 | 9.5% | 20.6% | 1.2% | **17** | **38** |
| Alphabet Inc. | `GOOGL` | 9.5 | 9.3 | 34.0% | 23.0 | -27.6% | 23.3% | 0.5% | **2** | **38** |
| Amazon.com, Inc. | `AMZN` | 3.6 | 3.7 | 13.7% | 24.7 | -18.4% | 14.5% | 0.1% | **0** | **38** |
| Fluence Energy, Inc. | `FLNC` | 0.6 | 0.5 | -8.9% | -28.3 | 70.1% | 35.3% | 0.2% | **5** | **28** |
| Hyperliquid Strategies Inc | `PURI` | 347.8 | 246.8 | 9595.1% | 32.0 | 51.0% | 31.4% | — | **25** | **10** |
| BitMine Immersion Technologies, | `BMNR` | 241.5 | 252.7 | 8.4% | 26.1 | 103.2% | 421.8% | -3.5% | **25** | **25** |
| Strategy Inc | `MSTR` | 124.4 | 164.5 | -6808.1% | 3.1 | 157.5% | 2.2% | -36.4% | **25** | **25** |
| QUALCOMM Incorporated | `QCOM` | 4.3 | 4.5 | 18.5% | 17.4 | -2.7% | 4.8% | 5.4% | **25** | **15** |

## Files

- `scanner.py` — scanner and scoring logic
- `hk_btc_correlation.py` — BTC/Hong Kong correlation scanner
- `reports/latest.md` — latest full report
- `reports/hk_btc_latest.md` — BTC vs Hang Seng/HSTECH/Xiaomi correlation report
- `data/latest.csv` — latest machine-readable snapshot
- `data/history.csv` — hourly history of **all companies** for later backtests
- `data/hk_btc_history.csv` — rolling BTC/Hong Kong correlation history
- `.github/workflows/hourly-okx-scanner.yml` — hourly GitHub Action

## Data

The configured universe can be pinned to the exact OKX EEA xStocks/USDC markets confirmed in the user's app. When that allowlist is present it overrides the broader public catalogue. Yahoo Finance/yfinance supplies company valuation, cash-flow and analyst-growth estimates. ETFs can exist in the OKX universe but are excluded from the company-fundamentals ranking.

### Optional account-accurate filter

Add read-only GitHub Actions secrets `OKX_API_KEY`, `OKX_API_SECRET`, and `OKX_API_PASSPHRASE`. The scanner will then query the authenticated OKX EEA account-instruments endpoint and only score contracts available to that account. Do not grant Trade or Withdraw permission for this scanner.

This is a quantitative research screen, not an automatic trading system. It does not place orders or select leverage.
