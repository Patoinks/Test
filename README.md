# OKX Long / Short Fundamental Scanner

Hourly scanner restricted to public companies exposed by the **OKX EEA TradFi / Stock Perpetual API universe**.

**Last scan:** 2026-10-09 21:44 UTC  
**Availability scope:** user-confirmed OKX EEA Stock Futures / X-Perp  
**OKX stock/ETF markets in configured universe:** 72  
**Public companies analysed:** 55  
**SHORT CORE:** 6  
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
| 1 | Taiwan Semiconductor Manufactur | TSM | -1.0% | -4.1% | -2.6% | 82 | +2 | **84** | **CORE** | yes |
| 2 | Applied Materials, Inc. | AMAT | -0.5% | -6.1% | -3.3% | 81 | +3 | **84** | **CORE** | yes |
| 3 | NVIDIA Corporation | NVDA | -0.5% | -2.0% | -1.3% | 82 | +1 | **83** | **CORE** | yes |
| 4 | Applovin Corporation | APP | -1.1% | 3.3% | 1.1% | 82 | -1 | **81** | **CORE** | yes |
| 5 | Broadcom Inc. | AVGO | 0.4% | 1.8% | 1.1% | 82 | -1 | **81** | **CORE** | yes |
| 6 | Advanced Micro Devices, Inc. | AMD | -2.0% | -4.1% | -3.0% | 79 | +2 | **81** | **CORE** | yes |
| 7 | Sandisk Corporation | SNDK | -1.7% | -8.0% | -4.9% | 77 | +4 | **81** | **CORE** | yes |
| 8 | Micron Technology, Inc. | MU | -0.7% | -4.3% | -2.5% | 77 | +2 | **79** | **CORE** | yes |
| 9 | Marvell Technology, Inc. | MRVL | 0.2% | 1.1% | 0.7% | 79 | -1 | **78** | **CORE** | yes |
| 10 | Oracle Corporation | ORCL | 4.2% | -0.6% | 1.8% | 78 | -1 | **77** | **CORE** | yes |

## Final model + Price Timing — SHORT

| Rank | Company | OKX | 24h | 7d | 50/50 move | Base SHORT | Timing adj. | Final | Signal | Prev. SHORT? |
|---:|---|---|---:|---:|---:|---:|---:|---:|---|---|
| 1 | Rocket Lab Corporation | RKLB | -0.3% | -7.7% | -4.0% | 100 | -3 | **97** | **CORE** | yes |
| 2 | USA Rare Earth, Inc. | USAR | -0.6% | -7.6% | -4.1% | 100 | -3 | **97** | **CORE** | yes |
| 3 | Cerebras Systems Inc. | CBRS | -2.2% | -1.4% | -1.8% | 98 | -1 | **97** | **CORE** | yes |
| 4 | Moderna, Inc. | MRNA | 14.2% | 18.4% | 16.3% | 80 | +13 | **93** | **CORE** | yes |
| 5 | IonQ, Inc. | IONQ | 1.1% | -8.9% | -3.9% | 91 | -3 | **88** | **CORE** | yes |
| 6 | Nebius Group N.V. | NBIS | 0.6% | -9.0% | -4.2% | 90 | -3 | **87** | **CORE** | yes |
| 7 | AST SpaceMobile, Inc. | ASTS | -10.5% | -12.8% | -11.6% | 80 | -9 | **71** | **WATCH** | yes |
| 8 | Lumentum Holdings Inc. | LITE | 5.2% | 1.7% | 3.4% | 67 | +3 | **70** | **WATCH** | yes |
| 9 | Okta, Inc. | OKTA | 5.4% | 9.8% | 7.6% | 61 | +6 | **67** | **WATCH** | yes |
| 10 | IREN LIMITED | IREN | -1.5% | -15.7% | -8.6% | 64 | -7 | **57** | **WATCH** | yes |

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
| 10 | Micron Technology, Inc. | `MU` | 75 | 82 | **77** | **CORE** |

## Combined model — SHORT

Weighted score: **70% fundamental + 30% P/E trend**.

| Rank | Company | OKX | Fundamental SHORT | P/E trend SHORT | Combined | Signal |
|---:|---|---|---:|---:|---:|---|
| 1 | Rocket Lab Corporation | `RKLB` | 100 | 0 | **100** | **CORE** |
| 2 | USA Rare Earth, Inc. | `USAR` | 100 | 0 | **100** | **CORE** |
| 3 | Cerebras Systems Inc. | `CBRS` | 98 | 0 | **98** | **CORE** |
| 4 | IonQ, Inc. | `IONQ` | 91 | 0 | **91** | **CORE** |
| 5 | Nebius Group N.V. | `NBIS` | 90 | 0 | **90** | **CORE** |
| 6 | Moderna, Inc. | `MRNA` | 80 | 0 | **80** | **WATCH** |
| 7 | AST SpaceMobile, Inc. | `ASTS` | 80 | 0 | **80** | **WATCH** |
| 8 | Lumentum Holdings Inc. | `LITE` | 67 | 0 | **67** | **WATCH** |
| 9 | Okta, Inc. | `OKTA` | 80 | 18 | **61** | **WATCH** |

## P/E Compression + Growth — LONG

| Rank | Company | OKX | Trail P/E | Fwd P/E | P/E change | EPS +1y | Rev +1y | Rev trend | LONG score | Signal |
|---:|---|---|---:|---:|---:|---:|---:|---|---:|---|
| 1 | NVIDIA Corporation | `NVDA` | 29.0 | 14.4 | -50.3% | 70.9% | 68.2% | decelerating | **100** | **CORE** |
| 2 | Advanced Micro Devices, Inc. | `AMD` | 155.1 | 38.7 | -75.1% | 107.2% | 74.6% | accelerating | **100** | **CORE** |
| 3 | Broadcom Inc. | `AVGO` | 46.2 | 18.6 | -59.6% | 66.4% | 64.1% | decelerating | **100** | **CORE** |
| 4 | Marvell Technology, Inc. | `MRVL` | 90.6 | 37.8 | -58.3% | 72.6% | 63.0% | accelerating | **100** | **CORE** |
| 5 | Credo Technology Group Holding  | `CRDO` | 76.8 | 22.3 | -70.9% | 53.7% | 54.8% | decelerating | **96** | **CORE** |
| 6 | AXT Inc | `AXT` | 1711.5 | 30.4 | -98.2% | 159.2% | 111.3% | decelerating | **96** | **CORE** |
| 7 | Oracle Corporation | `ORCL` | 22.2 | 12.9 | -42.0% | 35.1% | 45.7% | accelerating | **95** | **CORE** |
| 8 | Corning Incorporated | `GLW` | 71.9 | 35.8 | -50.1% | 33.0% | 19.6% | accelerating | **92** | **CORE** |
| 9 | Applied Materials, Inc. | `AMAT` | 43.7 | 27.4 | -37.3% | 44.5% | 34.9% | accelerating | **91** | **CORE** |
| 10 | Coherent Corp. | `COHR` | 75.9 | 22.3 | -70.7% | 49.1% | 38.8% | decelerating | **91** | **CORE** |

## P/E Expansion + Weakening — SHORT

| Rank | Company | OKX | Trail P/E | Fwd P/E | P/E change | EPS +1y | Rev +1y | Rev trend | SHORT score | Signal |
|---:|---|---|---:|---:|---:|---:|---:|---|---:|---|
| 1 | SOFTBANK GROUP CORP | `SOFTBANK` | 7.0 | 19.7 | 179.5% | -14.5% | 6.9% | decelerating | **86** | **CORE** |
| 2 | Alphabet Inc. | `GOOGL` | 17.6 | 23.3 | 32.2% | -27.4% | 23.5% | decelerating | **70** | **CORE** |
| 3 | Hyperliquid Strategies Inc | `PURR` | 3.5 | 30.0 | 767.6% | 51.0% | 31.4% | decelerating | **55** | **WATCH** |
| 4 | Amazon.com, Inc. | `AMZN` | 21.1 | 25.1 | 18.8% | -18.4% | 14.5% | decelerating | **52** | **WATCH** |

## Top SHORT candidates

| Rank | Company | OKX market | SHORT score | Signal | P/S | EV/S | Op margin | Fwd P/E | Rev +1y | FCF yield |
|---:|---|---|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Rocket Lab Corporation | `RKLB-USDT-SWAP` | **100** | **CORE** | 56.7 | 50.4 | -24.6% | 1158.5 | 41.2% | -0.6% |
| 2 | USA Rare Earth, Inc. | `USAR-USDT-SWAP` | **100** | **CORE** | 357.9 | 119.5 | -795.6% | 418.7 | 870.1% | -6.0% |
| 3 | Cerebras Systems Inc. | `CBRS-USDT-SWAP` | **98** | **CORE** | 57.3 | 49.2 | -265.0% | 128.9 | 232.7% | — |
| 4 | IonQ, Inc. | `IONQ-USDT-SWAP` | **91** | **CORE** | 65.6 | 52.7 | -408.2% | -30.9 | 79.0% | -0.5% |
| 5 | Nebius Group N.V. | `NBIS-USDT-SWAP` | **90** | **CORE** | 44.4 | 46.0 | -0.2% | -62.1 | 268.0% | -16.0% |
| 6 | Okta, Inc. | `OKTA-USDT-SWAP` | **80** | **CORE** | 13.2 | 11.8 | 13.3% | 53.0 | 10.0% | 2.6% |
| 7 | AST SpaceMobile, Inc. | `ASTS-USDT-SWAP` | **80** | **WATCH** | 172.0 | 158.5 | -544.6% | -39.6 | 259.9% | -9.1% |
| 8 | Moderna, Inc. | `MRNA-USDT-SWAP` | **80** | **WATCH** | 40.3 | 33.6 | -557.9% | -50.7 | 16.1% | 0.3% |
| 9 | Lumentum Holdings Inc. | `LITE-USDT-SWAP` | **67** | **WATCH** | 33.2 | 30.9 | 28.0% | 31.0 | 55.7% | 0.2% |
| 10 | Tesla, Inc. | `TSLA-USDT-SWAP` | **63** | **WATCH** | 14.6 | 14.0 | 1.4% | 178.4 | 13.8% | 0.3% |

## Top LONG candidates

| Rank | Company | OKX market | LONG score | Signal | P/S | EV/S | Op margin | Fwd P/E | Rev +1y | FCF yield |
|---:|---|---|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Applovin Corporation | `APP-USDT-SWAP` | **83** | **CORE** | 13.6 | 13.8 | 77.7% | 13.3 | 26.4% | 3.4% |
| 2 | Taiwan Semiconductor Manufactur | `TSM-USDT-SWAP` | **82** | **CORE** | 0.5 | 3.7 | 60.3% | 20.7 | 35.3% | 31.1% |
| 3 | Applied Materials, Inc. | `AMAT-USDT-SWAP` | **77** | **WATCH** | 13.0 | 13.1 | 33.7% | 27.4 | 34.9% | 0.8% |
| 4 | Micron Technology, Inc. | `MU-USDT-SWAP` | **75** | **CORE** | 8.7 | 8.5 | 80.7% | 5.0 | 16.5% | 2.5% |
| 5 | Broadcom Inc. | `AVGO-USDT-SWAP` | **75** | **WATCH** | 19.4 | 19.7 | 54.3% | 18.6 | 64.1% | 1.8% |
| 6 | Sandisk Corporation | `SNDK-USDT-SWAP` | **75** | **CORE** | 11.3 | 11.4 | 78.5% | 5.9 | 18.9% | 3.4% |
| 7 | Western Digital Corporation | `WDC-USDT-SWAP` | **75** | **WATCH** | 11.5 | 10.9 | 43.6% | 12.4 | 36.9% | 1.5% |
| 8 | NVIDIA Corporation | `NVDA-USDT-SWAP` | **75** | **WATCH** | 18.3 | 18.3 | 66.2% | 14.4 | 68.2% | 0.8% |
| 9 | Robinhood Markets, Inc. | `HOOD-USDT-SWAP` | **70** | **WATCH** | 19.9 | 19.3 | 43.9% | 31.7 | 28.9% | — |
| 10 | Marvell Technology, Inc. | `MRVL-USDT-SWAP` | **70** | **WATCH** | 26.2 | 25.6 | 16.7% | 37.8 | 63.0% | 1.0% |

## Analyst consensus (12-month price target) — most upside

| Rank | Company | OKX | Price | Analyst mean target | Gap | Analysts | Currency |
|---:|---|---|---:|---:|---:|---:|---|
| 1 | USA Rare Earth, Inc. | `USAR` | 12.56 | 35.56 | **183.1%** | 9 | USD |
| 2 | IREN LIMITED | `IREN` | 35.19 | 78.14 | **122.0%** | 18 | USD |
| 3 | Hyperliquid Strategies Inc | `PURR` | 11.11 | 22.32 | **100.9%** | 4 | USD |
| 4 | BitMine Immersion Technologies, | `BMNR` | 24.03 | 45.87 | **90.9%** | 3 | USD |
| 5 | SK hynix | `SKHYNIX` | 1681000.00 | 3141024.80 | **86.9%** | 38 | KRW |
| 6 | SamsungElec | `SAMSUNG` | 262000.00 | 478905.62 | **82.8%** | 36 | KRW |
| 7 | Cerebras Systems Inc. | `CBRS` | 164.17 | 291.64 | **77.6%** | 11 | USD |
| 8 | Applovin Corporation | `APP` | 277.04 | 487.66 | **76.0%** | 31 | USD |
| 9 | CoreWeave, Inc. | `CRWV` | 82.08 | 141.47 | **72.4%** | 38 | USD |
| 10 | Western Digital Corporation | `WDC` | 397.28 | 670.79 | **68.8%** | 24 | USD |
| 11 | Oracle Corporation | `ORCL` | 141.40 | 237.97 | **68.3%** | 41 | USD |
| 12 | IonQ, Inc. | `IONQ` | 39.89 | 66.63 | **67.0%** | 14 | USD |
| 13 | Rocket Lab Corporation | `RKLB` | 68.21 | 106.57 | **56.2%** | 21 | USD |
| 14 | Strategy Inc | `MSTR` | 154.34 | 237.80 | **54.1%** | 15 | USD |
| 15 | AST SpaceMobile, Inc. | `ASTS` | 50.97 | 77.94 | **52.9%** | 12 | USD |

## Analyst consensus (12-month price target) — most downside

| Rank | Company | OKX | Price | Analyst mean target | Gap | Analysts | Currency |
|---:|---|---|---:|---:|---:|---:|---|
| 1 | Moderna, Inc. | `MRNA` | 225.00 | 122.67 | **-45.5%** | 18 | USD |
| 2 | Okta, Inc. | `OKTA` | 232.13 | 212.60 | **-8.4%** | 43 | USD |
| 3 | Palantir Technologies Inc. | `PLTR` | 209.05 | 203.35 | **-2.7%** | 26 | USD |
| 4 | Apple Inc. | `AAPL` | 336.64 | 328.09 | **-2.5%** | 39 | USD |
| 5 | Dell Technologies Inc. | `DELL` | 586.06 | 585.96 | **-0.0%** | 25 | USD |

Price/target uses the underlying Yahoo Finance share quote, not the OKX derivative. Minimum 3 analysts; unreliable price scales and missing coverage excluded. Targets are analyst opinions, not guaranteed forecasts.

## All OKX companies — our ratio + LONG/SHORT scores

| Company | OKX | P/S | EV/S | Op margin | Fwd P/E | EPS +1y | Rev +1y | FCF yield | LONG | SHORT |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Rocket Lab Corporation | `RKLB` | 56.7 | 50.4 | -24.6% | 1158.5 | 75.5% | 41.2% | -0.6% | **0** | **100 CORE** |
| USA Rare Earth, Inc. | `USAR` | 357.9 | 119.5 | -795.6% | 418.7 | 105.3% | 870.1% | -6.0% | **0** | **100 CORE** |
| Cerebras Systems Inc. | `CBRS` | 57.3 | 49.2 | -265.0% | 128.9 | 371.3% | 232.7% | — | **0** | **98 CORE** |
| IonQ, Inc. | `IONQ` | 65.6 | 52.7 | -408.2% | -30.9 | 18.1% | 79.0% | -0.5% | **0** | **91 CORE** |
| Nebius Group N.V. | `NBIS` | 44.4 | 46.0 | -0.2% | -62.1 | -191.4% | 268.0% | -16.0% | **0** | **90 CORE** |
| Applovin Corporation | `APP` | 13.6 | 13.8 | 77.7% | 13.3 | 27.5% | 26.4% | 3.4% | **83 CORE** | **10** |
| Taiwan Semiconductor Manufactur | `TSM` | 0.5 | 3.7 | 60.3% | 20.7 | 30.0% | 35.3% | 31.1% | **82 CORE** | **10** |
| Okta, Inc. | `OKTA` | 13.2 | 11.8 | 13.3% | 53.0 | 11.4% | 10.0% | 2.6% | **8** | **80 CORE** |
| Moderna, Inc. | `MRNA` | 40.3 | 33.6 | -557.9% | -50.7 | 43.0% | 16.1% | 0.3% | **0** | **80 WATCH** |
| AST SpaceMobile, Inc. | `ASTS` | 172.0 | 158.5 | -544.6% | -39.6 | 47.7% | 259.9% | -9.1% | **0** | **80 WATCH** |
| Applied Materials, Inc. | `AMAT` | 13.0 | 13.1 | 33.7% | 27.4 | 44.5% | 34.9% | 0.8% | **77 WATCH** | **13** |
| NVIDIA Corporation | `NVDA` | 18.3 | 18.3 | 66.2% | 14.4 | 70.9% | 68.2% | 0.8% | **75 WATCH** | **18** |
| Sandisk Corporation | `SNDK` | 11.3 | 11.4 | 78.5% | 5.9 | 24.0% | 18.9% | 3.4% | **75 CORE** | **10** |
| Broadcom Inc. | `AVGO` | 19.4 | 19.7 | 54.3% | 18.6 | 66.4% | 64.1% | 1.8% | **75 WATCH** | **28** |
| Micron Technology, Inc. | `MU` | 8.7 | 8.5 | 80.7% | 5.0 | 17.1% | 16.5% | 2.5% | **75 CORE** | **30** |
| Western Digital Corporation | `WDC` | 11.5 | 10.9 | 43.6% | 12.4 | 58.2% | 36.9% | 1.5% | **75 WATCH** | **18** |
| Advanced Micro Devices, Inc. | `AMD` | 24.0 | 24.3 | 17.2% | 38.7 | 107.2% | 74.6% | 0.9% | **70 WATCH** | **13** |
| Marvell Technology, Inc. | `MRVL` | 26.2 | 25.6 | 16.7% | 37.8 | 72.6% | 63.0% | 1.0% | **70 WATCH** | **13** |
| Oracle Corporation | `ORCL` | 6.0 | 7.6 | 35.6% | 12.9 | 35.1% | 45.7% | -10.7% | **70 WATCH** | **10** |
| Robinhood Markets, Inc. | `HOOD` | 19.9 | 19.3 | 43.9% | 31.7 | 35.9% | 28.9% | — | **70 WATCH** | **5** |
| XIAOMI-W | `XIAOMI` | 1.5 | 1.3 | 4.0% | 17.0 | 39.1% | 22.6% | -1.3% | **70 WATCH** | **10** |
| Credo Technology Group Holding  | `CRDO` | 25.6 | 24.6 | 25.2% | 22.3 | 53.7% | 54.8% | 0.6% | **67 WATCH** | **28** |
| Lumentum Holdings Inc. | `LITE` | 33.2 | 30.9 | 28.0% | 31.0 | 63.4% | 55.7% | 0.2% | **0** | **67 WATCH** |
| Adobe Inc. | `ADBE` | 3.6 | 3.7 | 34.8% | 8.8 | 13.0% | 9.2% | 9.9% | **65 WATCH** | **30** |
| IREN LIMITED | `IREN` | 19.6 | 22.7 | -102.5% | -8.8 | -16.4% | 160.9% | -30.4% | **0** | **64** |
| Tesla, Inc. | `TSLA` | 14.6 | 14.0 | 1.4% | 178.4 | 24.9% | 13.8% | 0.3% | **22** | **63 WATCH** |
| Corning Incorporated | `GLW` | 8.0 | 8.2 | 15.6% | 35.8 | 33.0% | 19.6% | 0.5% | **60 WATCH** | **13** |
| Microsoft Corporation | `MSFT` | 12.0 | 11.9 | 45.1% | 22.6 | 19.8% | 19.6% | 0.4% | **59 WATCH** | **23** |
| Dell Technologies Inc. | `DELL` | 2.5 | 2.6 | 12.0% | 20.1 | 0.8% | 16.5% | 1.6% | **17** | **58** |
| Coca-Cola Company (The) | `KO` | 7.6 | 8.1 | 34.9% | 25.0 | 6.7% | 0.1% | 1.4% | **7** | **58** |
| Apple Inc. | `AAPL` | 10.5 | 10.7 | 32.6% | 35.1 | 8.6% | 10.5% | 2.2% | **5** | **58** |
| Bloom Energy Corporation | `BE` | 26.5 | 25.9 | 17.1% | 56.8 | 82.6% | 65.0% | 0.6% | **55 WATCH** | **48** |
| Coherent Corp. | `COHR` | 8.6 | 8.6 | 11.8% | 22.3 | 49.1% | 38.8% | -1.1% | **52** | **35** |
| Super Micro Computer, Inc. | `SMCI` | 0.7 | 0.9 | 13.4% | 7.9 | 22.8% | 17.3% | -30.0% | **52** | **25** |
| Netflix, Inc. | `NFLX` | 6.1 | 6.3 | 33.4% | 18.5 | 6.1% | 11.2% | 8.7% | **35** | **50** |
| Palantir Technologies Inc. | `PLTR` | 81.6 | 76.1 | 47.1% | 88.9 | 45.2% | 49.8% | 0.4% | **33** | **48** |
| Intel Corporation | `INTC` | 9.7 | 10.1 | 12.2% | 50.3 | 36.9% | 14.8% | 0.9% | **5** | **48** |
| AXT Inc | `AXT` | 35.8 | 34.7 | 21.9% | 30.4 | 159.2% | 111.3% | -1.0% | **45** | **35** |
| SK hynix | `SKHYNIX` | 6.3 | 6.0 | 76.3% | 3.6 | 32.4% | 54.4% | 4.7% | **45** | **5** |
| SK hynix | `SKHY` | 6.3 | 6.0 | 76.3% | 3.6 | 32.4% | 54.4% | 4.7% | **45** | **5** |
| SamsungElec | `SAMSUNG` | 3.5 | 3.2 | 52.2% | 3.6 | 50.8% | 37.6% | 4.0% | **45** | **10** |
| Circle Internet Group, Inc. | `CRCL` | 7.4 | 6.5 | 4.9% | 59.8 | 31.2% | 25.1% | 1.0% | **43** | **33** |
| Coinbase Global, Inc. | `COIN` | 7.8 | 7.2 | -13.9% | 57.2 | 274.3% | 29.9% | 5.6% | **20** | **40** |
| SOFTBANK GROUP CORP | `SOFTBANK` | 4.1 | 7.5 | -11.6% | 19.7 | -14.5% | 6.9% | -6.6% | **0** | **40** |
| CoreWeave, Inc. | `CRWV` | 6.0 | 12.0 | -1.9% | -45.3 | 15.4% | 104.3% | -20.1% | **0** | **40** |
| Meta Platforms, Inc. | `META` | 8.0 | 8.1 | 34.8% | 20.8 | 9.8% | 20.6% | 1.2% | **17** | **38** |
| Alphabet Inc. | `GOOGL` | 9.6 | 9.3 | 34.0% | 23.3 | -27.4% | 23.5% | 0.5% | **2** | **38** |
| Amazon.com, Inc. | `AMZN` | 3.6 | 3.7 | 13.7% | 25.1 | -18.4% | 14.5% | 0.1% | **0** | **38** |
| Arm Holdings plc | `ARM` | 55.2 | 56.4 | 7.6% | 86.9 | 37.5% | 36.2% | 0.5% | **35** | **33** |
| Applied Optoelectronics, Inc. | `AAOI` | 15.6 | 14.7 | -12.9% | 23.8 | 576.8% | 156.5% | -9.5% | **0** | **35** |
| Fluence Energy, Inc. | `FLNC` | 0.5 | 0.5 | -8.9% | -27.9 | 70.1% | 35.3% | 0.2% | **5** | **28** |
| Hyperliquid Strategies Inc | `PURR` | 326.8 | 221.7 | 9595.1% | 30.0 | 51.0% | 31.4% | — | **25** | **10** |
| BitMine Immersion Technologies, | `BMNR` | 236.9 | 231.4 | 8.4% | 25.6 | 103.2% | 421.8% | -3.6% | **25** | **25** |
| Strategy Inc | `MSTR` | 123.5 | 154.4 | -6808.1% | 3.1 | 157.6% | 2.2% | -36.7% | **25** | **25** |
| QUALCOMM Incorporated | `QCOM` | 4.3 | 4.4 | 18.5% | 17.2 | -2.7% | 4.8% | 5.5% | **25** | **15** |

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
