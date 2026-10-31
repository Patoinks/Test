# OKX Long / Short Fundamental Scanner

Hourly scanner restricted to public companies exposed by the **OKX EEA TradFi / Stock Perpetual API universe**.

**Last scan:** 2026-10-31 15:46 UTC  
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
| 1 | Applovin Corporation | APP | 0.0% | -12.2% | -6.1% | 87 | +5 | **92** | **CORE** | yes |
| 2 | Marvell Technology, Inc. | MRVL | 0.0% | -14.1% | -7.0% | 84 | +6 | **90** | **CORE** | yes |
| 3 | Taiwan Semiconductor Manufactur | TSM | -0.0% | -3.0% | -1.5% | 88 | +1 | **89** | **CORE** | yes |
| 4 | Sandisk Corporation | SNDK | -0.0% | -7.0% | -3.5% | 82 | +3 | **85** | **CORE** | yes |
| 5 | Robinhood Markets, Inc. | HOOD | 0.0% | -10.6% | -5.3% | 80 | +4 | **84** | **CORE** | yes |
| 6 | NVIDIA Corporation | NVDA | 0.0% | -3.0% | -1.5% | 82 | +1 | **83** | **CORE** | yes |
| 7 | Credo Technology Group Holding  | CRDO | -0.0% | 2.5% | 1.3% | 82 | -1 | **81** | **CORE** | yes |
| 8 | Broadcom Inc. | AVGO | 0.0% | 1.4% | 0.7% | 82 | -1 | **81** | **CORE** | yes |
| 9 | Applied Materials, Inc. | AMAT | 0.0% | 3.4% | 1.7% | 81 | -1 | **80** | **CORE** | yes |
| 10 | Corning Incorporated | GLW | 0.0% | -0.3% | -0.2% | 80 | +0 | **80** | **CORE** | yes |

## Final model + Price Timing — SHORT

| Rank | Company | OKX | 24h | 7d | 50/50 move | Base SHORT | Timing adj. | Final | Signal | Prev. SHORT? |
|---:|---|---|---:|---:|---:|---:|---:|---:|---|---|
| 1 | Rocket Lab Corporation | RKLB | 0.0% | 4.0% | 2.0% | 100 | +2 | **100** | **CORE** | yes |
| 2 | USA Rare Earth, Inc. | USAR | 0.0% | 3.1% | 1.6% | 100 | +1 | **100** | **CORE** | yes |
| 3 | IonQ, Inc. | IONQ | -0.0% | -3.9% | -2.0% | 85 | -2 | **83** | **CORE** | yes |
| 4 | Nebius Group N.V. | NBIS | 0.0% | -2.9% | -1.4% | 84 | -1 | **83** | **CORE** | yes |
| 5 | AST SpaceMobile, Inc. | ASTS | -0.0% | 3.0% | 1.5% | 80 | +1 | **81** | **CORE** | yes |
| 6 | Moderna, Inc. | MRNA | -0.0% | 10.8% | 5.4% | 72 | +4 | **76** | **CORE** | yes |
| 7 | Cerebras Systems Inc. | CBRS | -0.0% | -1.5% | -0.7% | 75 | -1 | **74** | **WATCH** | yes |
| 8 | Tesla, Inc. | TSLA | 0.0% | 7.4% | 3.7% | 59 | +3 | **62** | **WATCH** | yes |
| 9 | Okta, Inc. | OKTA | -0.0% | -2.3% | -1.1% | 60 | -1 | **59** | **WATCH** | yes |
| 10 | Lumentum Holdings Inc. | LITE | -0.0% | 11.2% | 5.6% | 55 | +4 | **59** | **WATCH** | yes |

## Combined model — LONG

Weighted score: **70% fundamental + 30% P/E trend**.

| Rank | Company | OKX | Fundamental LONG | P/E trend LONG | Combined | Signal |
|---:|---|---|---:|---:|---:|---|
| 1 | Taiwan Semiconductor Manufactur | `TSM` | 90 | 85 | **88** | **CORE** |
| 2 | Applovin Corporation | `APP` | 90 | 80 | **87** | **CORE** |
| 3 | Marvell Technology, Inc. | `MRVL` | 77 | 100 | **84** | **CORE** |
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
| 3 | IonQ, Inc. | `IONQ` | 85 | 0 | **85** | **CORE** |
| 4 | Nebius Group N.V. | `NBIS` | 84 | 0 | **84** | **WATCH** |
| 5 | AST SpaceMobile, Inc. | `ASTS` | 80 | 0 | **80** | **WATCH** |
| 6 | Cerebras Systems Inc. | `CBRS` | 75 | 0 | **75** | **WATCH** |
| 7 | Moderna, Inc. | `MRNA` | 72 | 0 | **72** | **WATCH** |
| 8 | Okta, Inc. | `OKTA` | 80 | 13 | **60** | **WATCH** |
| 9 | Tesla, Inc. | `TSLA` | 78 | 15 | **59** | **WATCH** |

## P/E Compression + Growth — LONG

| Rank | Company | OKX | Trail P/E | Fwd P/E | P/E change | EPS +1y | Rev +1y | Rev trend | LONG score | Signal |
|---:|---|---|---:|---:|---:|---:|---:|---|---:|---|
| 1 | Marvell Technology, Inc. | `MRVL` | 64.6 | 26.8 | -58.5% | 73.6% | 63.3% | accelerating | **100** | **CORE** |
| 2 | NVIDIA Corporation | `NVDA` | 25.9 | 12.9 | -50.3% | 70.9% | 68.2% | decelerating | **100** | **CORE** |
| 3 | Broadcom Inc. | `AVGO` | 41.6 | 16.8 | -59.8% | 66.9% | 64.4% | decelerating | **100** | **CORE** |
| 4 | Credo Technology Group Holding  | `CRDO` | 53.5 | 15.5 | -71.0% | 53.9% | 55.0% | decelerating | **100** | **CORE** |
| 5 | Advanced Micro Devices, Inc. | `AMD` | 128.8 | 31.7 | -75.4% | 108.8% | 75.1% | accelerating | **100** | **CORE** |
| 6 | AXT Inc | `AXT` | 112.4 | 20.7 | -81.5% | 125.3% | 115.8% | decelerating | **96** | **CORE** |
| 7 | Oracle Corporation | `ORCL` | 20.5 | 11.8 | -42.2% | 35.5% | 45.7% | accelerating | **95** | **CORE** |
| 8 | Coherent Corp. | `COHR` | 51.0 | 15.1 | -70.4% | 48.0% | 38.1% | decelerating | **95** | **CORE** |
| 9 | Arm Holdings plc | `ARM` | 212.3 | 67.2 | -68.4% | 37.5% | 36.4% | accelerating | **95** | **CORE** |
| 10 | Bloom Energy Corporation | `BE` | 123.1 | 38.2 | -69.0% | 63.0% | 56.4% | decelerating | **92** | **CORE** |

## P/E Expansion + Weakening — SHORT

| Rank | Company | OKX | Trail P/E | Fwd P/E | P/E change | EPS +1y | Rev +1y | Rev trend | SHORT score | Signal |
|---:|---|---|---:|---:|---:|---:|---:|---|---:|---|
| 1 | SOFTBANK GROUP CORP | `SOFTBANK` | 5.2 | 15.2 | 191.0% | -14.5% | 7.0% | decelerating | **86** | **CORE** |
| 2 | Hyperliquid Strategies Inc | `PURR` | 3.4 | 29.8 | 767.6% | 51.0% | 31.4% | decelerating | **55** | **WATCH** |
| 3 | Amazon.com, Inc. | `AMZN` | 19.4 | 22.8 | 17.4% | -17.2% | 14.7% | decelerating | **52** | **WATCH** |
| 4 | Alphabet Inc. | `GOOGL` | 14.6 | 18.5 | 26.5% | -24.7% | 27.0% | accelerating | **50** | **WATCH** |

## Top SHORT candidates

| Rank | Company | OKX market | SHORT score | Signal | P/S | EV/S | Op margin | Fwd P/E | Rev +1y | FCF yield |
|---:|---|---|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Rocket Lab Corporation | `RKLB-USDT-SWAP` | **100** | **CORE** | 45.5 | 39.8 | -24.6% | 952.0 | 38.2% | -0.7% |
| 2 | USA Rare Earth, Inc. | `USAR-USDT-SWAP` | **100** | **CORE** | 274.1 | 63.6 | -795.6% | 320.7 | 870.1% | -7.9% |
| 3 | IonQ, Inc. | `IONQ-USDT-SWAP` | **85** | **CORE** | 52.3 | 38.1 | -408.2% | -22.3 | 77.6% | -0.7% |
| 4 | Nebius Group N.V. | `NBIS-USDT-SWAP` | **84** | **WATCH** | 30.9 | 32.8 | -0.2% | -42.8 | 266.0% | -22.9% |
| 5 | Okta, Inc. | `OKTA-USDT-SWAP` | **80** | **CORE** | 11.8 | 11.1 | 13.3% | 47.6 | 10.1% | 2.9% |
| 6 | AST SpaceMobile, Inc. | `ASTS-USDT-SWAP` | **80** | **WATCH** | 138.3 | 117.0 | -544.6% | -28.2 | 264.2% | -11.3% |
| 7 | Tesla, Inc. | `TSLA-USDT-SWAP` | **78** | **WATCH** | 15.3 | 15.0 | 5.4% | 185.5 | 13.4% | 0.3% |
| 8 | Cerebras Systems Inc. | `CBRS-USDT-SWAP` | **75** | **WATCH** | 38.1 | 28.7 | -265.0% | 85.7 | 232.7% | — |
| 9 | Moderna, Inc. | `MRNA-USDT-SWAP` | **72** | **WATCH** | 39.7 | 38.0 | -557.9% | -48.4 | 16.3% | 0.3% |

## Top LONG candidates

| Rank | Company | OKX market | LONG score | Signal | P/S | EV/S | Op margin | Fwd P/E | Rev +1y | FCF yield |
|---:|---|---|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Taiwan Semiconductor Manufactur | `TSM-USDT-SWAP` | **90** | **CORE** | 0.4 | 2.8 | 58.7% | 17.4 | 37.6% | 57.1% |
| 2 | Applovin Corporation | `APP-USDT-SWAP` | **90** | **CORE** | 11.2 | 11.3 | 77.7% | 11.1 | 25.1% | 4.1% |
| 3 | Sandisk Corporation | `SNDK-USDT-SWAP` | **82** | **CORE** | 5.7 | 5.5 | 79.6% | 4.2 | 19.8% | 6.8% |
| 4 | Corning Incorporated | `GLW-USDT-SWAP` | **77** | **WATCH** | 6.0 | 6.4 | 18.9% | 27.2 | 21.2% | 0.8% |
| 5 | Robinhood Markets, Inc. | `HOOD-USDT-SWAP` | **77** | **WATCH** | 15.1 | 14.6 | 48.1% | 25.1 | 29.0% | — |
| 6 | Applied Materials, Inc. | `AMAT-USDT-SWAP` | **77** | **WATCH** | 10.0 | 10.0 | 33.7% | 21.0 | 35.3% | 1.0% |
| 7 | Marvell Technology, Inc. | `MRVL-USDT-SWAP` | **77** | **WATCH** | 18.7 | 18.4 | 16.7% | 26.8 | 63.3% | 1.4% |
| 8 | Credo Technology Group Holding  | `CRDO-USDT-SWAP` | **75** | **WATCH** | 17.8 | 17.4 | 25.2% | 15.5 | 55.0% | 0.9% |
| 9 | Broadcom Inc. | `AVGO-USDT-SWAP` | **75** | **WATCH** | 17.5 | 17.9 | 54.3% | 16.8 | 64.4% | 2.0% |
| 10 | Micron Technology, Inc. | `MU-USDT-SWAP` | **75** | **CORE** | 7.5 | 7.2 | 80.7% | 4.3 | 16.0% | 2.9% |

## Analyst consensus (12-month price target) — most upside

| Rank | Company | OKX | Price | Analyst mean target | Gap | Analysts | Currency |
|---:|---|---|---:|---:|---:|---:|---|
| 1 | Cerebras Systems Inc. | `CBRS` | 109.18 | 282.55 | **158.8%** | 11 | USD |
| 2 | CoreWeave, Inc. | `CRWV` | 54.87 | 134.58 | **145.3%** | 38 | USD |
| 3 | BitMine Immersion Technologies, | `BMNR` | 20.18 | 45.87 | **127.3%** | 3 | USD |
| 4 | Applied Optoelectronics, Inc. | `AAOI` | 69.05 | 156.00 | **125.9%** | 5 | USD |
| 5 | SK hynix | `SKHYNIX` | 1418000.00 | 3157408.80 | **122.7%** | 39 | KRW |
| 6 | SamsungElec | `SAMSUNG` | 225000.00 | 480102.94 | **113.4%** | 35 | KRW |
| 7 | IonQ, Inc. | `IONQ` | 30.04 | 64.06 | **113.3%** | 14 | USD |
| 8 | Hyperliquid Strategies Inc | `PURR` | 11.01 | 22.32 | **102.8%** | 4 | USD |
| 9 | Applovin Corporation | `APP` | 228.50 | 452.95 | **98.2%** | 31 | USD |
| 10 | Credo Technology Group Holding  | `CRDO` | 150.99 | 284.05 | **88.1%** | 19 | USD |
| 11 | Coherent Corp. | `COHR` | 210.32 | 394.40 | **87.5%** | 25 | USD |
| 12 | Rocket Lab Corporation | `RKLB` | 54.73 | 102.15 | **86.6%** | 20 | USD |
| 13 | Strategy Inc | `MSTR` | 130.51 | 239.27 | **83.3%** | 15 | USD |
| 14 | Sandisk Corporation | `SNDK` | 1150.89 | 2105.29 | **82.9%** | 24 | USD |
| 15 | Nebius Group N.V. | `NBIS` | 154.14 | 281.00 | **82.3%** | 20 | USD |

## Analyst consensus (12-month price target) — most downside

| Rank | Company | OKX | Price | Analyst mean target | Gap | Analysts | Currency |
|---:|---|---|---:|---:|---:|---:|---|
| 1 | Moderna, Inc. | `MRNA` | 221.72 | 138.37 | **-37.6%** | 19 | USD |
| 2 | Apple Inc. | `AAPL` | 344.63 | 332.39 | **-3.6%** | 38 | USD |

Price/target uses the underlying Yahoo Finance share quote, not the OKX derivative. Minimum 3 analysts; unreliable price scales and missing coverage excluded. Targets are analyst opinions, not guaranteed forecasts.

## All OKX companies — our ratio + LONG/SHORT scores

| Company | OKX | P/S | EV/S | Op margin | Fwd P/E | EPS +1y | Rev +1y | FCF yield | LONG | SHORT |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Rocket Lab Corporation | `RKLB` | 45.5 | 39.8 | -24.6% | 952.0 | 66.8% | 38.2% | -0.7% | **0** | **100 CORE** |
| USA Rare Earth, Inc. | `USAR` | 274.1 | 63.6 | -795.6% | 320.7 | 105.3% | 870.1% | -7.9% | **0** | **100 CORE** |
| Applovin Corporation | `APP` | 11.2 | 11.3 | 77.7% | 11.1 | 25.9% | 25.1% | 4.1% | **90 CORE** | **10** |
| Taiwan Semiconductor Manufactur | `TSM` | 0.4 | 2.8 | 58.7% | 17.4 | 33.6% | 37.6% | 57.1% | **90 CORE** | **10** |
| IonQ, Inc. | `IONQ` | 52.3 | 38.1 | -408.2% | -22.3 | 21.3% | 77.6% | -0.7% | **0** | **85 CORE** |
| Nebius Group N.V. | `NBIS` | 30.9 | 32.8 | -0.2% | -42.8 | -191.4% | 266.0% | -22.9% | **0** | **84 WATCH** |
| Sandisk Corporation | `SNDK` | 5.7 | 5.5 | 79.6% | 4.2 | 22.4% | 19.8% | 6.8% | **82 CORE** | **10** |
| Okta, Inc. | `OKTA` | 11.8 | 11.1 | 13.3% | 47.6 | 11.4% | 10.1% | 2.9% | **8** | **80 CORE** |
| AST SpaceMobile, Inc. | `ASTS` | 138.3 | 117.0 | -544.6% | -28.2 | 44.3% | 264.2% | -11.3% | **0** | **80 WATCH** |
| Tesla, Inc. | `TSLA` | 15.3 | 15.0 | 5.4% | 185.5 | 23.8% | 13.4% | 0.3% | **12** | **78 WATCH** |
| Marvell Technology, Inc. | `MRVL` | 18.7 | 18.4 | 16.7% | 26.8 | 73.6% | 63.3% | 1.4% | **77 WATCH** | **13** |
| Robinhood Markets, Inc. | `HOOD` | 15.1 | 14.6 | 48.1% | 25.1 | 41.0% | 29.0% | — | **77 WATCH** | **0** |
| Corning Incorporated | `GLW` | 6.0 | 6.4 | 18.9% | 27.2 | 34.0% | 21.2% | 0.8% | **77 WATCH** | **13** |
| Applied Materials, Inc. | `AMAT` | 10.0 | 10.0 | 33.7% | 21.0 | 45.0% | 35.3% | 1.0% | **77 WATCH** | **3** |
| NVIDIA Corporation | `NVDA` | 16.3 | 16.2 | 66.2% | 12.9 | 70.9% | 68.2% | 0.8% | **75 WATCH** | **18** |
| Broadcom Inc. | `AVGO` | 17.5 | 17.9 | 54.3% | 16.8 | 66.9% | 64.4% | 2.0% | **75 WATCH** | **28** |
| Credo Technology Group Holding  | `CRDO` | 17.8 | 17.4 | 25.2% | 15.5 | 53.9% | 55.0% | 0.9% | **75 WATCH** | **28** |
| Micron Technology, Inc. | `MU` | 7.5 | 7.2 | 80.7% | 4.3 | 17.7% | 16.0% | 2.9% | **75 CORE** | **30** |
| Western Digital Corporation | `WDC` | 9.5 | 9.4 | 47.7% | 9.1 | 63.4% | 40.5% | 2.0% | **75 WATCH** | **18** |
| Cerebras Systems Inc. | `CBRS` | 38.1 | 28.7 | -265.0% | 85.7 | 371.3% | 232.7% | — | **0** | **75 WATCH** |
| Moderna, Inc. | `MRNA` | 39.7 | 38.0 | -557.9% | -48.4 | 42.3% | 16.3% | 0.3% | **0** | **72 WATCH** |
| Advanced Micro Devices, Inc. | `AMD` | 20.0 | 19.7 | 17.2% | 31.7 | 108.8% | 75.1% | 1.1% | **70 WATCH** | **13** |
| Oracle Corporation | `ORCL` | 5.5 | 7.4 | 35.6% | 11.8 | 35.5% | 45.7% | -11.6% | **70 WATCH** | **10** |
| XIAOMI-W | `XIAOMI` | 1.6 | 1.4 | 4.0% | 17.5 | 36.8% | 19.7% | -1.3% | **70 WATCH** | **10** |
| AXT Inc | `AXT` | 21.1 | 18.7 | 38.7% | 20.7 | 125.3% | 115.8% | — | **67 WATCH** | **20** |
| Dell Technologies Inc. | `DELL` | 1.8 | 1.9 | 12.0% | 14.0 | 16.2% | 19.2% | 2.2% | **67 WATCH** | **38** |
| Adobe Inc. | `ADBE` | 3.8 | 3.8 | 34.8% | 9.1 | 12.4% | 9.1% | 9.6% | **65 WATCH** | **30** |
| Coherent Corp. | `COHR` | 5.8 | 6.1 | 11.8% | 15.1 | 48.0% | 38.1% | -1.6% | **60 WATCH** | **35** |
| Microsoft Corporation | `MSFT` | 11.2 | 11.4 | 49.8% | 21.6 | 20.6% | 19.9% | 0.1% | **59 WATCH** | **3** |
| Apple Inc. | `AAPL` | 10.8 | 10.8 | 32.6% | 36.1 | 8.2% | 9.9% | 2.1% | **5** | **58** |
| Coca-Cola Company (The) | `KO` | 7.9 | 8.5 | 33.4% | 26.7 | 5.6% | -3.0% | 1.1% | **0** | **58** |
| Meta Platforms, Inc. | `META` | 6.5 | 6.6 | 35.4% | 17.3 | 16.5% | 21.6% | 1.1% | **57 WATCH** | **38** |
| Lumentum Holdings Inc. | `LITE` | 25.3 | 24.7 | 28.0% | 23.5 | 63.7% | 56.5% | 0.3% | **0** | **55** |
| Super Micro Computer, Inc. | `SMCI` | 0.6 | 0.7 | 13.4% | 5.8 | 19.6% | 16.2% | -38.1% | **52** | **45** |
| Netflix, Inc. | `NFLX` | 5.2 | 5.3 | 34.6% | 16.5 | 5.1% | 10.7% | 9.9% | **35** | **50** |
| IREN LIMITED | `IREN` | 13.7 | 16.1 | -102.5% | -6.0 | -16.4% | 164.0% | -43.5% | **0** | **50** |
| Palantir Technologies Inc. | `PLTR` | 71.9 | 70.4 | 47.1% | 78.3 | 45.6% | 50.8% | 0.5% | **33** | **48** |
| Bloom Energy Corporation | `BE` | 15.7 | 15.8 | 18.5% | 38.2 | 63.0% | 56.4% | -0.0% | **45** | **35** |
| SamsungElec | `SAMSUNG` | 2.5 | 2.2 | 55.0% | 3.0 | 61.8% | 39.5% | 5.7% | **45** | **10** |
| Amazon.com, Inc. | `AMZN` | 3.3 | 3.5 | 13.9% | 22.8 | -17.2% | 14.7% | -0.4% | **0** | **45** |
| Arm Holdings plc | `ARM` | 42.7 | 42.0 | 7.6% | 67.2 | 37.5% | 36.4% | 0.6% | **43** | **33** |
| Circle Internet Group, Inc. | `CRCL` | 6.3 | 5.7 | 4.9% | 49.1 | 27.0% | 27.4% | 1.1% | **43** | **33** |
| Coinbase Global, Inc. | `COIN` | 7.0 | 6.6 | -1.4% | 48.8 | 274.3% | 29.1% | 9.7% | **20** | **40** |
| SOFTBANK GROUP CORP | `SOFTBANK` | 3.2 | 6.5 | -11.6% | 15.2 | -14.5% | 7.0% | -8.6% | **0** | **40** |
| CoreWeave, Inc. | `CRWV` | 4.0 | 10.1 | -1.9% | -27.9 | 9.7% | 105.6% | -30.0% | **0** | **40** |
| SK hynix | `SKHYNIX` | 3.7 | 3.4 | 79.7% | 2.7 | 47.0% | 58.5% | — | **30** | **5** |
| SK hynix | `SKHY` | 3.7 | 3.4 | 79.7% | 2.7 | 47.0% | 58.5% | — | **30** | **5** |
| Alphabet Inc. | `GOOGL` | 7.3 | 7.1 | 31.8% | 18.5 | -24.7% | 27.0% | -0.0% | **5** | **30** |
| Intel Corporation | `INTC` | 5.8 | 6.0 | 15.6% | 31.3 | 41.6% | 14.2% | 0.2% | **10** | **28** |
| Fluence Energy, Inc. | `FLNC` | 0.4 | 0.4 | -8.9% | -10.8 | 59.3% | 25.4% | 0.2% | **5** | **28** |
| Hyperliquid Strategies Inc | `PURR` | 323.9 | 215.7 | 9595.1% | 29.8 | 51.0% | 31.4% | — | **25** | **10** |
| Strategy Inc | `MSTR` | 111.7 | 139.4 | 16670.9% | 5.5 | 168.0% | 2.7% | — | **25** | **10** |
| BitMine Immersion Technologies, | `BMNR` | 198.9 | 193.4 | 8.4% | 21.5 | 103.2% | 421.8% | -4.3% | **25** | **25** |
| QUALCOMM Incorporated | `QCOM` | 4.0 | 4.1 | 18.5% | 16.2 | -2.8% | 4.6% | 5.8% | **25** | **15** |
| Applied Optoelectronics, Inc. | `AAOI` | 9.8 | 9.5 | -12.9% | 15.0 | 576.8% | 156.5% | -15.1% | **10** | **25** |

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
