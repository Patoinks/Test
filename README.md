# OKX Long / Short Fundamental Scanner

Hourly scanner restricted to public companies represented in the **OKX TradFi / Stock Perpetual** universe.

**Last scan:** 2026-09-29 14:07 UTC  
**OKX TradFi/RWA instruments discovered:** 108  
**Public companies analysed:** 101  
**SHORT CORE:** 2  
**LONG CORE:** 12

## Our ratio

**Our ratio = Forward P/E ÷ expected EPS growth (%)**. It is PEG-like: lower can indicate more growth per unit of valuation; very high can indicate expensive valuation relative to expected growth.

### SHORT CORE

`Forward P/E > 40` + `Our ratio > 2.5` + `EPS growth < 20%`.

### LONG CORE

`Forward P/E <= 35` + `Our ratio <= 1.5` + `EPS growth >= 15%` + `Revenue growth >= 8%` + `FCF yield >= 2.5%`.

Scores are 0-100 heuristics. Revenue acceleration helps LONG and penalizes SHORT; deceleration does the opposite. Funding is shown separately because it affects the cost/carry of holding an OKX perpetual.

## Top SHORT candidates

| Rank | Company | OKX perp | SHORT score | Signal | Our ratio | Fwd P/E | EPS +1y | Rev +1y | FCF yield | Funding ann. |
|---:|---|---|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Okta, Inc. | `OKTA-USDT-SWAP` | **90** | **CORE** | 4.02 | 46.0 | 11.4% | 10.0% | 2.9% | 0.0% |
| 2 | Twilio Inc. | `TWLO-USDT-SWAP` | **85** | **CORE** | 2.88 | 41.8 | 14.5% | 11.5% | 2.2% | 0.0% |
| 3 | Tesla, Inc. | `TSLA-USDT-SWAP` | **60** | **WATCH** | 6.97 | 163.6 | 23.5% | 13.8% | 0.3% | 29.5% |

## Top LONG candidates

| Rank | Company | OKX perp | LONG score | Signal | Our ratio | Fwd P/E | EPS +1y | Rev +1y | FCF yield | Funding ann. |
|---:|---|---|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | ON Semiconductor Corporation | `ON-USDT-SWAP` | **95** | **CORE** | 0.41 | 17.0 | 41.4% | 13.1% | 5.5% | 0.0% |
| 2 | DraftKings Inc. | `DKNG-USDT-SWAP` | **95** | **CORE** | 0.14 | 12.3 | 88.4% | 13.3% | 4.5% | 0.0% |
| 3 | SK hynix | `SKHY-USDT-SWAP` | **90** | **CORE** | 0.11 | 3.7 | 33.4% | 54.1% | 4.5% | 0.0% |
| 4 | POP MART | `POPMART-USDT-SWAP` | **85** | **CORE** | 0.58 | 12.6 | 21.5% | 17.2% | 2.9% | 0.0% |
| 5 | Applovin Corporation | `APP-USDT-SWAP` | **83** | **CORE** | 0.53 | 14.7 | 27.7% | 26.7% | 3.1% | 21.9% |
| 6 | Taiwan Semiconductor Manufactur | `TSM-USDT-SWAP` | **82** | **CORE** | 0.70 | 20.6 | 29.5% | 34.5% | 31.2% | 0.0% |
| 7 | Hewlett Packard Enterprise Comp | `HPE-USDT-SWAP` | **82** | **CORE** | 0.66 | 13.4 | 20.2% | 17.1% | 5.8% | 0.0% |
| 8 | Bending Spoons S.p.A. | `BSP-USDT-SWAP` | **80** | **WATCH** | 0.42 | 17.0 | 40.3% | 45.6% | — | 0.0% |
| 9 | Coinbase Global, Inc. | `COIN-USDT-SWAP` | **80** | **WATCH** | 0.28 | 67.9 | 239.9% | 29.5% | 5.3% | 0.0% |
| 10 | Take-Two Interactive Software,  | `TTWO-USDT-SWAP` | **78** | **CORE** | 0.10 | 19.6 | 187.0% | 8.8% | 3.3% | 0.0% |

## All OKX companies — our ratio + LONG/SHORT scores

| Company | OKX | Our ratio | Fwd P/E | Trail P/E | EPS +1y | Rev +1y | FCF yield | LONG | SHORT | Funding ann. |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| DraftKings Inc. | `DKNG` | 0.14 | 12.3 | — | 88.4% | 13.3% | 4.5% | **95 CORE** | **0** | 0.0% |
| ON Semiconductor Corporation | `ON` | 0.41 | 17.0 | 50.3 | 41.4% | 13.1% | 5.5% | **95 CORE** | **5** | 0.0% |
| SK hynix | `SKHY` | 0.11 | 3.7 | — | 33.4% | 54.1% | 4.5% | **90 CORE** | **10** | 0.0% |
| Okta, Inc. | `OKTA` | 4.02 | 46.0 | 121.4 | 11.4% | 10.0% | 2.9% | **8** | **90 CORE** | 0.0% |
| POP MART | `POPMART` | 0.58 | 12.6 | 13.3 | 21.5% | 17.2% | 2.9% | **85 CORE** | **0** | 0.0% |
| Twilio Inc. | `TWLO` | 2.88 | 41.8 | 39.2 | 14.5% | 11.5% | 2.2% | **0** | **85 CORE** | 0.0% |
| Applovin Corporation | `APP` | 0.53 | 14.7 | 23.8 | 27.7% | 26.7% | 3.1% | **83 CORE** | **10** | 21.9% |
| Hewlett Packard Enterprise Comp | `HPE` | 0.66 | 13.4 | 31.8 | 20.2% | 17.1% | 5.8% | **82 CORE** | **10** | 0.0% |
| Taiwan Semiconductor Manufactur | `TSM` | 0.70 | 20.6 | 33.6 | 29.5% | 34.5% | 31.2% | **82 CORE** | **10** | 0.0% |
| Bending Spoons S.p.A. | `BSP` | 0.42 | 17.0 | 76.0 | 40.3% | 45.6% | — | **80 WATCH** | **15** | 0.0% |
| Coinbase Global, Inc. | `COIN` | 0.28 | 67.9 | — | 239.9% | 29.5% | 5.3% | **80 WATCH** | **15** | 0.0% |
| CrowdStrike Holdings, Inc. | `CRWD` | 5.75 | 160.1 | 8569.0 | 27.9% | 22.6% | 0.8% | **25** | **80** | 0.0% |
| Take-Two Interactive Software,  | `TTWO` | 0.10 | 19.6 | — | 187.0% | 8.8% | 3.3% | **78 CORE** | **10** | 0.0% |
| Applied Materials, Inc. | `AMAT` | 0.62 | 27.4 | 43.7 | 44.3% | 34.8% | 0.8% | **77 WATCH** | **15** | 0.0% |
| Blackstone Inc. | `BX` | 0.63 | 15.3 | 25.6 | 24.4% | 23.9% | — | **77 WATCH** | **0** | -12.9% |
| Broadcom Inc. | `AVGO` | 0.28 | 18.5 | 45.7 | 66.2% | 63.7% | 1.8% | **75 WATCH** | **35** | 28.0% |
| Credo Technology Group Holding  | `CRDO` | 0.37 | 19.9 | 68.3 | 53.9% | 55.0% | 0.7% | **75 WATCH** | **35** | 0.0% |
| Hims & Hers Health, Inc. | `HIMS` | 0.23 | 39.5 | — | 174.8% | 24.6% | 12.5% | **75 WATCH** | **10** | 0.0% |
| LGELECTRONICS | `LGELECTRONICS` | 0.57 | 12.7 | — | 22.3% | 40.6% | 3.2% | **75 CORE** | **10** | 0.0% |
| Micron Technology, Inc. | `MU` | 0.06 | 6.6 | 24.3 | 118.6% | 92.1% | 0.6% | **75 WATCH** | **20** | 7.5% |
| NVIDIA Corporation | `NVDA` | 0.21 | 14.6 | 29.0 | 68.5% | 65.9% | 0.8% | **75 WATCH** | **20** | 15.0% |
| Reddit, Inc. | `RDDT` | 0.48 | 14.9 | 33.6 | 31.4% | 31.8% | 2.4% | **75 WATCH** | **20** | 27.4% |
| Sandisk Corporation | `SNDK` | 0.28 | 6.6 | 23.4 | 23.2% | 18.3% | 3.0% | **75 CORE** | **10** | 19.4% |
| Vertiv Holdings, LLC | `VRT` | 0.77 | 27.7 | 57.0 | 36.0% | 30.1% | 2.8% | **75 CORE** | **25** | 19.1% |
| Western Digital Corporation | `WDC` | 0.25 | 14.3 | 17.0 | 58.0% | 36.8% | 1.4% | **75 WATCH** | **20** | 0.0% |
| ZHONGJI INNOLIGHT | `ZHONGJI` | 0.10 | 12.2 | 44.3 | 122.1% | 99.5% | 0.0% | **75 WATCH** | **35** | 10.5% |
| Intuitive Surgical, Inc. | `ISRG` | 2.77 | 33.7 | 45.7 | 12.2% | 12.8% | 1.8% | **5** | **75** | 0.0% |
| Advanced Micro Devices, Inc. | `AMD` | 0.38 | 39.7 | 164.0 | 105.6% | 73.2% | 0.9% | **70 WATCH** | **15** | 0.0% |
| Robinhood Markets, Inc. | `HOOD` | 0.99 | 33.8 | 51.6 | 34.1% | 27.9% | — | **70 WATCH** | **5** | 6.6% |
| Marvell Technology, Inc. | `MRVL` | 0.63 | 38.5 | 86.6 | 60.7% | 51.3% | 1.0% | **70 WATCH** | **15** | 0.0% |
| Oracle Corporation | `ORCL` | 0.35 | 12.2 | 21.0 | 35.1% | 45.3% | -11.3% | **70 WATCH** | **0** | 66.2% |
| Tower Semiconductor Ltd. | `TSEM` | 0.49 | 35.4 | 92.8 | 72.4% | 37.9% | 0.6% | **70 WATCH** | **15** | 0.0% |
| XIAOMI-W | `XIAOMI` | 0.41 | 16.3 | 17.7 | 39.7% | 24.3% | -1.3% | **70 WATCH** | **0** | 0.0% |
| Ciena Corporation | `CIEN` | 0.39 | 29.7 | 78.5 | 76.5% | 30.7% | 1.3% | **67 WATCH** | **35** | 0.0% |
| Lumentum Holdings Inc. | `LITE` | 0.47 | 28.1 | — | 59.6% | 52.2% | 0.3% | **67 WATCH** | **20** | 14.0% |
| Eli Lilly and Company | `LLY` | 0.87 | 24.9 | 39.7 | 28.6% | 15.4% | 1.1% | **67 WATCH** | **20** | 0.0% |
| Adobe Inc. | `ADBE` | 0.64 | 8.4 | 13.0 | 13.0% | 9.2% | 10.1% | **65 WATCH** | **30** | 24.1% |
| HANMISemi | `HANMI` | 0.89 | 50.4 | — | 56.4% | 55.7% | 0.3% | **65 WATCH** | **25** | 0.0% |
| Snowflake Inc. | `SNOW` | 3.01 | 108.8 | — | 36.2% | 28.5% | 1.5% | **25** | **65** | 0.0% |
| BlackBerry Limited | `BB` | 2.54 | 37.1 | 84.7 | 14.6% | 9.9% | 2.8% | **13** | **65** | 12.8% |
| Rocket Lab Corporation | `RKLB` | 23.01 | 1567.2 | — | 68.1% | 42.2% | -0.6% | **10** | **65** | 0.3% |
| USA Rare Earth, Inc. | `USAR` | 4.48 | 471.8 | — | 105.3% | 870.1% | -5.3% | **10** | **65** | 16.2% |
| Applied Optoelectronics, Inc. | `AAOI` | 0.04 | 21.9 | — | 576.8% | 156.5% | -10.4% | **62 WATCH** | **0** | 0.0% |
| ASML Holding N.V. - New York Re | `ASML` | 0.88 | 30.8 | 62.9 | 35.0% | 27.3% | 1.2% | **60 WATCH** | **35** | 0.0% |
| Cerebras Systems Inc. | `CBRS` | 0.43 | 159.9 | — | 371.3% | 232.7% | — | **60 WATCH** | **25** | 0.0% |
| Corning Incorporated | `GLW` | 1.10 | 36.4 | 73.2 | 33.0% | 19.2% | 0.5% | **60 WATCH** | **15** | 12.5% |
| Space Exploration Technologies  | `SPCX` | 0.02 | 83.6 | — | 5097.3% | 150.7% | — | **60 WATCH** | **25** | 35.9% |
| UnitedHealth Group Incorporated | `UNH` | 1.20 | 16.5 | 24.0 | 13.8% | 2.9% | 7.2% | **60 WATCH** | **10** | 0.0% |
| Astera Labs, Inc. | `ALAB` | 0.96 | 56.2 | 176.2 | 58.6% | 55.8% | 0.1% | **55 WATCH** | **60** | 0.0% |
| Bloom Energy Corporation | `BE` | 0.72 | 59.3 | 374.8 | 82.2% | 65.0% | 0.6% | **55 WATCH** | **60** | 0.0% |
| Arm Holdings plc | `ARM` | 2.60 | 97.4 | 300.4 | 37.4% | 36.2% | 0.4% | **35** | **60** | 28.2% |
| Palantir Technologies Inc. | `PLTR` | 1.80 | 80.1 | 159.0 | 44.4% | 49.7% | 0.5% | **33** | **60** | 0.0% |
| Palo Alto Networks, Inc. | `PANW` | 1.93 | 77.7 | 972.0 | 40.2% | 14.5% | 1.4% | **28** | **60** | — |
| Dell Technologies Inc. | `DELL` | 22.64 | 18.8 | 31.9 | 0.8% | 15.8% | 1.7% | **25** | **60** | 9.4% |
| Tesla, Inc. | `TSLA` | 6.97 | 163.6 | 340.3 | 23.5% | 13.8% | 0.3% | **22** | **60 WATCH** | 29.5% |
| Coca-Cola Company (The) | `KO` | 3.62 | 24.7 | 26.4 | 6.8% | 0.2% | 1.4% | **7** | **60** | 0.0% |
| Apple Inc. | `AAPL` | 4.04 | 34.7 | 38.2 | 8.6% | 10.5% | 2.2% | **5** | **60** | 1.8% |
| Microsoft Corporation | `MSFT` | 1.07 | 21.3 | 28.1 | 19.8% | 19.5% | 0.4% | **59 WATCH** | **20** | 0.0% |
| NAVER | `NAVER` | 0.96 | 13.3 | — | 13.9% | 14.1% | 3.1% | **58 WATCH** | **30** | 0.0% |
| ServiceNow, Inc. | `NOW` | 1.13 | 26.1 | 81.6 | 23.1% | 18.8% | 3.8% | **57 CORE** | **25** | 19.8% |
| Cognex Corporation | `CGNX` | 1.50 | 29.2 | 56.6 | 19.5% | 9.7% | 2.0% | **44** | **55** | 0.0% |
| BitMine Immersion Technologies, | `BMNR` | 0.28 | 28.8 | — | 103.2% | 421.8% | -3.2% | **52** | **20** | 26.8% |
| Coherent Corp. | `COHR` | 0.44 | 21.1 | 71.4 | 48.2% | 38.2% | -1.1% | **52** | **35** | 44.8% |
| Super Micro Computer, Inc. | `SMCI` | 0.35 | 7.9 | 13.3 | 22.8% | 17.3% | -30.4% | **52** | **20** | 0.0% |
| GoPro, Inc. | `GPRO` | -1.37 | -135.5 | — | 98.6% | 35.5% | 21.1% | **50** | **0** | 0.0% |
| Strategy Inc | `MSTR` | 0.02 | 3.2 | — | 156.0% | 2.2% | -36.3% | **50** | **20** | 28.6% |
| Teradyne, Inc. | `TER` | 1.25 | 35.1 | 56.1 | 28.2% | 21.8% | 0.7% | **50** | **35** | 0.0% |
| Netflix, Inc. | `NFLX` | 2.95 | 18.6 | 22.2 | 6.3% | 11.3% | 8.6% | **35** | **50** | 7.5% |
| Zoom Communications, Inc. | `ZM` | 4.13 | 13.8 | 8.3 | 3.3% | 4.2% | 7.8% | **30** | **50** | 0.0% |
| Wendy's Company (The) | `WEN` | 3.61 | 12.5 | 9.8 | 3.5% | -0.5% | 14.0% | **20** | **50** | 0.0% |
| KLA Corporation | `KLAC` | 1.28 | 29.3 | 53.8 | 22.9% | 18.2% | 1.0% | **49** | **35** | 0.0% |
| Lam Research Corporation | `LRCX` | 1.15 | 27.7 | 56.5 | 24.0% | 18.4% | 0.8% | **49** | **35** | 0.0% |
| Intel Corporation | `INTC` | 1.59 | 56.5 | — | 35.6% | 14.2% | 0.8% | **28** | **45** | 22.5% |
| Rockwell Automation, Inc. | `ROK` | 2.32 | 29.0 | 40.3 | 12.5% | 5.7% | 2.7% | **15** | **45** | 0.0% |
| Circle Internet Group, Inc. | `CRCL` | 1.80 | 55.7 | 17.1 | 30.9% | 24.1% | 0.9% | **43** | **25** | 45.0% |
| GameStop Corporation | `GME` | 3.85 | 12.8 | 15.7 | 3.3% | 11.0% | 0.7% | **30** | **40** | 0.0% |
| Meta Platforms, Inc. | `META` | 2.29 | 20.6 | 28.6 | 9.0% | 20.6% | 1.2% | **17** | **40** | 2.8% |
| Alphabet Inc. | `GOOGL` | — | 22.6 | 17.1 | -27.6% | 23.3% | 0.5% | **2** | **40** | 22.4% |
| Amazon.com, Inc. | `AMZN` | — | 23.5 | 19.8 | -18.5% | 14.4% | 0.1% | **0** | **40** | 15.2% |
| CoreWeave, Inc. | `CRWV` | -3.21 | -47.6 | — | 14.8% | 104.0% | -19.0% | **0** | **40** | 0.0% |
| IREN LIMITED | `IREN` | — | -10.5 | — | -16.4% | 158.8% | -25.7% | **0** | **40** | 0.0% |
| Nebius Group N.V. | `NBIS` | — | -68.5 | — | -123.5% | 270.0% | -15.8% | **0** | **40** | 0.0% |
| SOFTBANK GROUP CORP | `SOFTBANK` | — | 20.4 | 6.9 | -39.7% | 7.2% | -6.4% | **0** | **40** | 0.0% |
| Fluence Energy, Inc. | `FLNC` | -0.41 | -29.1 | — | 70.1% | 36.0% | 0.2% | **35** | **0** | 0.0% |
| KIOXIA HOLDINGS CORPORATION | `KIOXIA` | — | — | 17.7 | 36.8% | 30.0% | 3.0% | **33** | **10** | 0.0% |
| International Business Machines | `IBM` | 2.48 | 16.9 | 19.7 | 6.8% | 3.9% | 5.8% | **30** | **30** | 0.0% |
| Cisco Systems, Inc. | `CSCO` | 2.05 | 18.9 | 32.0 | 9.2% | 6.6% | 2.7% | **23** | **30** | 0.0% |
| Salesforce, Inc. | `CRM` | — | 14.2 | 20.7 | -4.5% | 9.7% | 9.5% | **20** | **30** | 0.0% |
| Johnson & Johnson | `JNJ` | 2.30 | 22.1 | 31.1 | 9.6% | 7.4% | 2.6% | **15** | **30** | 0.0% |
| GE Vernova Inc. | `GEV` | — | 38.3 | 27.8 | -19.3% | 13.9% | 6.1% | **5** | **30** | 0.0% |
| ExxonMobil Holdings Corporation | `XOM` | — | 14.5 | 20.5 | -7.4% | -1.2% | 3.1% | **0** | **30** | 0.0% |
| QUALCOMM Incorporated | `QCOM` | — | 18.5 | 21.5 | -2.7% | 4.8% | 5.1% | **25** | **10** | 51.1% |
| Applied Digital Corporation | `APLD` | -0.92 | -51.1 | — | 55.6% | 131.1% | -67.1% | **20** | **0** | 0.0% |
| AST SpaceMobile, Inc. | `ASTS` | -0.92 | -47.6 | — | 51.8% | 285.4% | -7.5% | **20** | **0** | 11.7% |
| Intuitive Machines, Inc. | `LUNR` | -1.37 | -95.9 | — | 70.2% | 28.2% | -3.4% | **10** | **20** | 0.0% |
| Ondas Inc | `ONDS` | -4.16 | -376.8 | — | 90.5% | 87.7% | -1.6% | **10** | **20** | 0.0% |
| Redwire Corporation | `RDW` | -1.20 | -32.5 | — | 27.1% | 18.6% | -0.9% | **10** | **20** | 0.0% |
| Rivian Automotive, Inc. | `RIVN` | -0.76 | -8.5 | — | 11.1% | 58.3% | -7.2% | **0** | **20** | 0.0% |
| SharonAI Holdings, Inc. | `SHAZ` | -0.13 | -6.8 | — | 51.6% | 1195.1% | -11.9% | **15** | **10** | 0.0% |
| AMC Entertainment Holdings, Inc | `AMC` | — | -40.8 | — | — | 4.1% | 4.9% | **10** | **10** | 0.0% |
| RoboStrategy, Inc. | `BOT` | — | — | — | — | — | — | **0** | **0** | 109.6% |

## Files

- `scanner.py` — scanner and scoring logic
- `reports/latest.md` — latest full report
- `data/latest.csv` — latest machine-readable snapshot
- `data/history.csv` — hourly history of **all companies** for later backtests
- `.github/workflows/hourly-okx-scanner.yml` — hourly GitHub Action

## Data

OKX public market data provides the TradFi/perpetual context and funding. Yahoo Finance/yfinance supplies valuation, cash-flow and analyst-growth estimates. Availability can differ by OKX account/jurisdiction.

This is a quantitative research screen, not an automatic trading system. It does not place orders or select leverage.
