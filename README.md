# OKX Long / Short Fundamental Scanner

Hourly scanner restricted to public companies exposed by the **OKX EEA TradFi / Stock Perpetual API universe**.

**Last scan:** 2026-10-30 23:00 UTC  
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
| 1 | Applovin Corporation | APP | -10.4% | -12.2% | -11.3% | 87 | +9 | **96** | **CORE** | yes |
| 2 | Marvell Technology, Inc. | MRVL | -10.0% | -14.1% | -12.1% | 84 | +10 | **94** | **CORE** | yes |
| 3 | Taiwan Semiconductor Manufactur | TSM | -5.9% | -3.0% | -4.5% | 88 | +4 | **92** | **CORE** | yes |
| 4 | Sandisk Corporation | SNDK | -13.5% | -7.0% | -10.3% | 82 | +8 | **90** | **CORE** | yes |
| 5 | Robinhood Markets, Inc. | HOOD | -7.2% | -10.6% | -8.9% | 80 | +7 | **87** | **CORE** | yes |
| 6 | NVIDIA Corporation | NVDA | -4.2% | -3.0% | -3.6% | 82 | +3 | **85** | **CORE** | yes |
| 7 | Credo Technology Group Holding  | CRDO | -8.7% | 2.5% | -3.1% | 82 | +2 | **84** | **CORE** | yes |
| 8 | Broadcom Inc. | AVGO | -5.5% | 1.4% | -2.1% | 82 | +2 | **84** | **CORE** | yes |
| 9 | Advanced Micro Devices, Inc. | AMD | -10.9% | -2.3% | -6.6% | 79 | +5 | **84** | **CORE** | yes |
| 10 | Applied Materials, Inc. | AMAT | -7.5% | 3.4% | -2.0% | 81 | +2 | **83** | **CORE** | yes |

## Final model + Price Timing — SHORT

| Rank | Company | OKX | 24h | 7d | 50/50 move | Base SHORT | Timing adj. | Final | Signal | Prev. SHORT? |
|---:|---|---|---:|---:|---:|---:|---:|---:|---|---|
| 1 | Rocket Lab Corporation | RKLB | -7.4% | 4.0% | -1.7% | 100 | -1 | **99** | **CORE** | yes |
| 2 | USA Rare Earth, Inc. | USAR | -8.6% | 3.1% | -2.7% | 100 | -2 | **98** | **CORE** | yes |
| 3 | IonQ, Inc. | IONQ | -5.3% | -3.9% | -4.6% | 85 | -4 | **81** | **CORE** | yes |
| 4 | Nebius Group N.V. | NBIS | -10.4% | -2.9% | -6.6% | 84 | -5 | **79** | **CORE** | yes |
| 5 | AST SpaceMobile, Inc. | ASTS | -4.9% | 3.0% | -1.0% | 80 | -1 | **79** | **CORE** | yes |
| 6 | Cerebras Systems Inc. | CBRS | -5.2% | -1.5% | -3.3% | 79 | -3 | **76** | **CORE** | yes |
| 7 | Moderna, Inc. | MRNA | -0.5% | 10.8% | 5.2% | 72 | +4 | **76** | **CORE** | yes |
| 8 | Tesla, Inc. | TSLA | -0.9% | 7.4% | 3.3% | 59 | +3 | **62** | **WATCH** | yes |
| 9 | Lumentum Holdings Inc. | LITE | -8.6% | 11.2% | 1.3% | 59 | +1 | **60** | **WATCH** | no |
| 10 | Okta, Inc. | OKTA | -6.1% | -2.3% | -4.2% | 60 | -3 | **57** | **WATCH** | yes |

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
| 6 | Cerebras Systems Inc. | `CBRS` | 79 | 0 | **79** | **WATCH** |
| 7 | Moderna, Inc. | `MRNA` | 72 | 0 | **72** | **WATCH** |
| 8 | Okta, Inc. | `OKTA` | 80 | 13 | **60** | **WATCH** |
| 9 | Tesla, Inc. | `TSLA` | 78 | 15 | **59** | **WATCH** |

## P/E Compression + Growth — LONG

| Rank | Company | OKX | Trail P/E | Fwd P/E | P/E change | EPS +1y | Rev +1y | Rev trend | LONG score | Signal |
|---:|---|---|---:|---:|---:|---:|---:|---|---:|---|
| 1 | Marvell Technology, Inc. | `MRVL` | 64.6 | 26.8 | -58.5% | 73.6% | 63.3% | accelerating | **100** | **CORE** |
| 2 | NVIDIA Corporation | `NVDA` | 25.9 | 12.9 | -50.3% | 70.9% | 68.2% | decelerating | **100** | **CORE** |
| 3 | Advanced Micro Devices, Inc. | `AMD` | 128.8 | 31.7 | -75.4% | 108.6% | 75.1% | accelerating | **100** | **CORE** |
| 4 | Broadcom Inc. | `AVGO` | 41.6 | 16.8 | -59.8% | 66.9% | 64.4% | decelerating | **100** | **CORE** |
| 5 | Credo Technology Group Holding  | `CRDO` | 53.5 | 15.5 | -71.0% | 53.9% | 55.0% | decelerating | **100** | **CORE** |
| 6 | AXT Inc | `AXT` | 1376.5 | 24.7 | -98.2% | 159.2% | 111.3% | decelerating | **96** | **CORE** |
| 7 | Oracle Corporation | `ORCL` | 20.5 | 11.8 | -42.2% | 35.5% | 45.7% | accelerating | **95** | **CORE** |
| 8 | Coherent Corp. | `COHR` | 51.0 | 15.1 | -70.4% | 48.0% | 38.1% | decelerating | **95** | **CORE** |
| 9 | Arm Holdings plc | `ARM` | 212.3 | 67.2 | -68.4% | 37.5% | 36.4% | accelerating | **95** | **CORE** |
| 10 | Bloom Energy Corporation | `BE` | 123.1 | 38.2 | -69.0% | 62.7% | 56.0% | decelerating | **92** | **CORE** |

## P/E Expansion + Weakening — SHORT

| Rank | Company | OKX | Trail P/E | Fwd P/E | P/E change | EPS +1y | Rev +1y | Rev trend | SHORT score | Signal |
|---:|---|---|---:|---:|---:|---:|---:|---|---:|---|
| 1 | SOFTBANK GROUP CORP | `SOFTBANK` | 5.5 | 15.2 | 173.6% | -14.5% | 7.0% | decelerating | **86** | **CORE** |
| 2 | Hyperliquid Strategies Inc | `PURR` | 3.4 | 29.8 | 767.6% | 51.0% | 31.4% | decelerating | **55** | **WATCH** |
| 3 | Amazon.com, Inc. | `AMZN` | 19.3 | 22.8 | 17.7% | -18.3% | 14.6% | decelerating | **52** | **WATCH** |
| 4 | Alphabet Inc. | `GOOGL` | 14.6 | 18.5 | 26.5% | -24.7% | 27.1% | accelerating | **50** | **WATCH** |

## Top SHORT candidates

| Rank | Company | OKX market | SHORT score | Signal | P/S | EV/S | Op margin | Fwd P/E | Rev +1y | FCF yield |
|---:|---|---|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Rocket Lab Corporation | `RKLB-USDT-SWAP` | **100** | **CORE** | 45.5 | 43.2 | -24.6% | 952.0 | 38.2% | -0.7% |
| 2 | USA Rare Earth, Inc. | `USAR-USDT-SWAP` | **100** | **CORE** | 274.1 | 80.3 | -795.6% | 320.7 | 870.1% | -7.9% |
| 3 | IonQ, Inc. | `IONQ-USDT-SWAP` | **85** | **CORE** | 52.3 | 38.1 | -408.2% | -22.3 | 77.6% | -0.7% |
| 4 | Nebius Group N.V. | `NBIS-USDT-SWAP` | **84** | **WATCH** | 30.9 | 36.4 | -0.2% | -42.8 | 266.0% | -22.9% |
| 5 | Okta, Inc. | `OKTA-USDT-SWAP` | **80** | **CORE** | 11.8 | 11.9 | 13.3% | 47.6 | 10.1% | 2.9% |
| 6 | AST SpaceMobile, Inc. | `ASTS-USDT-SWAP` | **80** | **WATCH** | 138.3 | 122.5 | -544.6% | -28.2 | 264.2% | -11.3% |
| 7 | Cerebras Systems Inc. | `CBRS-USDT-SWAP` | **79** | **WATCH** | 38.1 | 30.7 | -265.0% | 85.7 | 232.7% | — |
| 8 | Tesla, Inc. | `TSLA-USDT-SWAP` | **78** | **WATCH** | 15.3 | 15.1 | 5.4% | 185.5 | 13.4% | 0.3% |
| 9 | Moderna, Inc. | `MRNA-USDT-SWAP` | **72** | **WATCH** | 39.7 | 38.2 | -557.9% | -48.4 | 16.3% | 0.3% |

## Top LONG candidates

| Rank | Company | OKX market | LONG score | Signal | P/S | EV/S | Op margin | Fwd P/E | Rev +1y | FCF yield |
|---:|---|---|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Taiwan Semiconductor Manufactur | `TSM-USDT-SWAP` | **90** | **CORE** | 0.4 | 2.8 | 58.7% | 17.4 | 37.6% | 57.1% |
| 2 | Applovin Corporation | `APP-USDT-SWAP` | **90** | **CORE** | 11.2 | 11.3 | 77.7% | 11.1 | 25.1% | 4.1% |
| 3 | Sandisk Corporation | `SNDK-USDT-SWAP` | **82** | **CORE** | 8.2 | 9.4 | 78.5% | 4.2 | 18.6% | 4.6% |
| 4 | Corning Incorporated | `GLW-USDT-SWAP` | **77** | **WATCH** | 6.0 | 6.9 | 19.0% | 27.3 | 21.1% | 1.0% |
| 5 | Robinhood Markets, Inc. | `HOOD-USDT-SWAP` | **77** | **WATCH** | 15.1 | 14.8 | 48.1% | 25.1 | 29.0% | — |
| 6 | Applied Materials, Inc. | `AMAT-USDT-SWAP` | **77** | **WATCH** | 10.0 | 10.0 | 33.7% | 21.0 | 35.3% | 1.0% |
| 7 | Marvell Technology, Inc. | `MRVL-USDT-SWAP` | **77** | **WATCH** | 18.7 | 20.4 | 16.7% | 26.8 | 63.3% | 1.4% |
| 8 | Credo Technology Group Holding  | `CRDO-USDT-SWAP` | **75** | **WATCH** | 17.8 | 19.1 | 25.2% | 15.5 | 55.0% | 0.9% |
| 9 | Broadcom Inc. | `AVGO-USDT-SWAP` | **75** | **WATCH** | 17.5 | 18.9 | 54.3% | 16.8 | 64.4% | 2.0% |
| 10 | Micron Technology, Inc. | `MU-USDT-SWAP` | **75** | **CORE** | 7.5 | 7.2 | 80.7% | 4.3 | 16.0% | 2.9% |

## Analyst consensus (12-month price target) — most upside

| Rank | Company | OKX | Price | Analyst mean target | Gap | Analysts | Currency |
|---:|---|---|---:|---:|---:|---:|---|
| 1 | Cerebras Systems Inc. | `CBRS` | 109.18 | 282.55 | **158.8%** | 11 | USD |
| 2 | CoreWeave, Inc. | `CRWV` | 54.87 | 134.58 | **145.3%** | 38 | USD |
| 3 | BitMine Immersion Technologies, | `BMNR` | 20.18 | 45.87 | **127.3%** | 3 | USD |
| 4 | Applied Optoelectronics, Inc. | `AAOI` | 69.05 | 156.00 | **125.9%** | 5 | USD |
| 5 | SK hynix | `SKHYNIX` | 1418000.00 | 3157408.80 | **122.7%** | 39 | KRW |
| 6 | SamsungElec | `SAMSUNG` | 225000.00 | 482017.22 | **114.2%** | 35 | KRW |
| 7 | IonQ, Inc. | `IONQ` | 30.04 | 64.06 | **113.3%** | 14 | USD |
| 8 | Hyperliquid Strategies Inc | `PURR` | 11.01 | 22.32 | **102.8%** | 4 | USD |
| 9 | Applovin Corporation | `APP` | 228.50 | 452.95 | **98.2%** | 31 | USD |
| 10 | Credo Technology Group Holding  | `CRDO` | 150.99 | 284.05 | **88.1%** | 19 | USD |
| 11 | Coherent Corp. | `COHR` | 210.32 | 394.40 | **87.5%** | 25 | USD |
| 12 | Rocket Lab Corporation | `RKLB` | 54.73 | 102.15 | **86.6%** | 20 | USD |
| 13 | Sandisk Corporation | `SNDK` | 1150.89 | 2143.83 | **86.3%** | 24 | USD |
| 14 | Strategy Inc | `MSTR` | 130.51 | 239.27 | **83.3%** | 15 | USD |
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
| Rocket Lab Corporation | `RKLB` | 45.5 | 43.2 | -24.6% | 952.0 | 66.8% | 38.2% | -0.7% | **0** | **100 CORE** |
| USA Rare Earth, Inc. | `USAR` | 274.1 | 80.3 | -795.6% | 320.7 | 105.3% | 870.1% | -7.9% | **0** | **100 CORE** |
| Applovin Corporation | `APP` | 11.2 | 11.3 | 77.7% | 11.1 | 25.9% | 25.1% | 4.1% | **90 CORE** | **10** |
| Taiwan Semiconductor Manufactur | `TSM` | 0.4 | 2.8 | 58.7% | 17.4 | 33.6% | 37.6% | 57.1% | **90 CORE** | **10** |
| IonQ, Inc. | `IONQ` | 52.3 | 38.1 | -408.2% | -22.3 | 21.3% | 77.6% | -0.7% | **0** | **85 CORE** |
| Nebius Group N.V. | `NBIS` | 30.9 | 36.4 | -0.2% | -42.8 | -191.4% | 266.0% | -22.9% | **0** | **84 WATCH** |
| Sandisk Corporation | `SNDK` | 8.2 | 9.4 | 78.5% | 4.2 | 23.6% | 18.6% | 4.6% | **82 CORE** | **10** |
| Okta, Inc. | `OKTA` | 11.8 | 11.9 | 13.3% | 47.6 | 11.4% | 10.1% | 2.9% | **8** | **80 CORE** |
| AST SpaceMobile, Inc. | `ASTS` | 138.3 | 122.5 | -544.6% | -28.2 | 44.3% | 264.2% | -11.3% | **0** | **80 WATCH** |
| Cerebras Systems Inc. | `CBRS` | 38.1 | 30.7 | -265.0% | 85.7 | 371.3% | 232.7% | — | **0** | **79 WATCH** |
| Tesla, Inc. | `TSLA` | 15.3 | 15.1 | 5.4% | 185.5 | 23.8% | 13.4% | 0.3% | **12** | **78 WATCH** |
| Marvell Technology, Inc. | `MRVL` | 18.7 | 20.4 | 16.7% | 26.8 | 73.6% | 63.3% | 1.4% | **77 WATCH** | **13** |
| Robinhood Markets, Inc. | `HOOD` | 15.1 | 14.8 | 48.1% | 25.1 | 41.0% | 29.0% | — | **77 WATCH** | **0** |
| Applied Materials, Inc. | `AMAT` | 10.0 | 10.0 | 33.7% | 21.0 | 45.0% | 35.3% | 1.0% | **77 WATCH** | **3** |
| Corning Incorporated | `GLW` | 6.0 | 6.9 | 19.0% | 27.3 | 34.0% | 21.1% | 1.0% | **77 WATCH** | **13** |
| NVIDIA Corporation | `NVDA` | 16.3 | 16.2 | 66.2% | 12.9 | 70.9% | 68.2% | 0.8% | **75 WATCH** | **18** |
| Broadcom Inc. | `AVGO` | 17.5 | 18.9 | 54.3% | 16.8 | 66.9% | 64.4% | 2.0% | **75 WATCH** | **28** |
| Credo Technology Group Holding  | `CRDO` | 17.8 | 19.1 | 25.2% | 15.5 | 53.9% | 55.0% | 0.9% | **75 WATCH** | **28** |
| Micron Technology, Inc. | `MU` | 7.5 | 7.2 | 80.7% | 4.3 | 17.7% | 16.0% | 2.9% | **75 CORE** | **30** |
| Western Digital Corporation | `WDC` | 9.5 | 9.4 | 47.7% | 9.1 | 63.4% | 40.5% | 2.0% | **75 WATCH** | **18** |
| Moderna, Inc. | `MRNA` | 39.7 | 38.2 | -557.9% | -48.4 | 42.3% | 16.3% | 0.3% | **0** | **72 WATCH** |
| Advanced Micro Devices, Inc. | `AMD` | 20.0 | 22.2 | 17.2% | 31.7 | 108.6% | 75.1% | 1.1% | **70 WATCH** | **13** |
| Oracle Corporation | `ORCL` | 5.5 | 7.4 | 35.6% | 11.8 | 35.5% | 45.7% | -11.6% | **70 WATCH** | **10** |
| XIAOMI-W | `XIAOMI` | 1.6 | 1.4 | 4.0% | 17.5 | 36.8% | 19.7% | -1.3% | **70 WATCH** | **10** |
| Dell Technologies Inc. | `DELL` | 1.8 | 2.2 | 12.0% | 14.0 | 16.2% | 19.2% | 2.2% | **67 WATCH** | **38** |
| Adobe Inc. | `ADBE` | 3.8 | 3.8 | 34.8% | 9.1 | 12.4% | 9.1% | 9.6% | **65 WATCH** | **30** |
| Coherent Corp. | `COHR` | 5.8 | 6.1 | 11.8% | 15.1 | 48.0% | 38.1% | -1.6% | **60 WATCH** | **35** |
| Microsoft Corporation | `MSFT` | 11.2 | 11.3 | 49.8% | 21.6 | 20.5% | 20.0% | 0.4% | **59 WATCH** | **3** |
| Lumentum Holdings Inc. | `LITE` | 25.3 | 27.0 | 28.0% | 23.5 | 63.7% | 56.5% | 0.3% | **0** | **59** |
| Apple Inc. | `AAPL` | 10.8 | 11.0 | 32.6% | 36.0 | 8.2% | 10.3% | 2.1% | **5** | **58** |
| Coca-Cola Company (The) | `KO` | 7.9 | 8.4 | 33.4% | 26.7 | 5.6% | -3.2% | 1.1% | **0** | **58** |
| Meta Platforms, Inc. | `META` | 6.5 | 6.7 | 35.4% | 17.3 | 16.5% | 21.6% | 1.1% | **57 WATCH** | **38** |
| AXT Inc | `AXT` | 28.8 | 26.2 | 21.9% | 24.7 | 159.2% | 111.3% | -1.2% | **52** | **35** |
| Super Micro Computer, Inc. | `SMCI` | 0.6 | 0.7 | 13.4% | 5.8 | 19.7% | 16.3% | -38.1% | **52** | **45** |
| Netflix, Inc. | `NFLX` | 5.2 | 5.3 | 34.6% | 16.5 | 5.1% | 10.7% | 9.9% | **35** | **50** |
| IREN LIMITED | `IREN` | 13.7 | 17.4 | -102.5% | -6.0 | -16.4% | 164.0% | -43.5% | **0** | **50** |
| Palantir Technologies Inc. | `PLTR` | 71.9 | 75.2 | 47.1% | 78.3 | 45.6% | 50.8% | 0.5% | **33** | **48** |
| Bloom Energy Corporation | `BE` | 15.7 | 17.2 | 18.5% | 38.2 | 62.7% | 56.0% | -0.0% | **45** | **35** |
| SK hynix | `SKHYNIX` | 5.3 | 5.4 | 76.3% | 2.7 | 47.0% | 58.5% | 5.6% | **45** | **5** |
| SK hynix | `SKHY` | 5.3 | 5.4 | 76.3% | 2.7 | 47.0% | 58.5% | 5.6% | **45** | **5** |
| SamsungElec | `SAMSUNG` | 3.0 | 2.8 | 52.2% | 3.0 | 61.3% | 40.0% | 4.7% | **45** | **10** |
| Arm Holdings plc | `ARM` | 42.7 | 46.7 | 7.6% | 67.2 | 37.5% | 36.4% | 0.6% | **43** | **33** |
| Circle Internet Group, Inc. | `CRCL` | 6.3 | 6.4 | 4.9% | 49.1 | 27.0% | 27.4% | 1.1% | **43** | **33** |
| Coinbase Global, Inc. | `COIN` | 6.3 | 6.7 | -13.9% | 47.6 | 278.9% | 29.9% | 7.0% | **20** | **40** |
| SOFTBANK GROUP CORP | `SOFTBANK` | 3.2 | 6.5 | -11.6% | 15.2 | -14.5% | 7.0% | -8.6% | **0** | **40** |
| CoreWeave, Inc. | `CRWV` | 4.0 | 10.1 | -1.9% | -27.9 | 9.7% | 105.6% | -30.0% | **0** | **40** |
| Amazon.com, Inc. | `AMZN` | 3.3 | 3.6 | 13.7% | 22.8 | -18.3% | 14.6% | 0.1% | **0** | **38** |
| Intel Corporation | `INTC` | 6.1 | 8.8 | 12.2% | 31.3 | 42.0% | 15.2% | 1.4% | **15** | **28** |
| Fluence Energy, Inc. | `FLNC` | 0.4 | 0.4 | -8.9% | -10.8 | 59.3% | 25.4% | 0.2% | **5** | **28** |
| Hyperliquid Strategies Inc | `PURR` | 323.9 | 216.1 | 9595.1% | 29.8 | 51.0% | 31.4% | — | **25** | **10** |
| Strategy Inc | `MSTR` | 110.9 | 146.8 | -6808.1% | 5.5 | 168.0% | 2.5% | -40.9% | **25** | **25** |
| BitMine Immersion Technologies, | `BMNR` | 198.9 | 208.0 | 8.4% | 21.5 | 103.2% | 421.8% | -4.3% | **25** | **25** |
| QUALCOMM Incorporated | `QCOM` | 4.0 | 4.6 | 18.5% | 16.2 | -2.8% | 4.6% | 5.8% | **25** | **15** |
| Applied Optoelectronics, Inc. | `AAOI` | 9.8 | 10.9 | -12.9% | 15.0 | 576.8% | 156.5% | -15.1% | **10** | **25** |
| Alphabet Inc. | `GOOGL` | 7.3 | 7.2 | 31.8% | 18.5 | -24.7% | 27.1% | 0.2% | **20** | **23** |

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
