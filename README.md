# OKX Long / Short Fundamental Scanner

Hourly scanner restricted to public companies represented in the **OKX TradFi / Stock Perpetual** universe.

**Last scan:** 2026-09-29 07:00 UTC  
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
| 1 | Okta, Inc. | `OKTA-USDT-SWAP` | **90** | **CORE** | 4.04 | 46.2 | 11.4% | 10.0% | 2.9% | 0.0% |
| 2 | Twilio Inc. | `TWLO-USDT-SWAP` | **85** | **CORE** | 2.91 | 42.3 | 14.5% | 11.5% | 2.2% | 0.0% |
| 3 | Tesla, Inc. | `TSLA-USDT-SWAP` | **60** | **WATCH** | 7.04 | 165.3 | 23.5% | 13.8% | 0.3% | 19.7% |

## Top LONG candidates

| Rank | Company | OKX perp | LONG score | Signal | Our ratio | Fwd P/E | EPS +1y | Rev +1y | FCF yield | Funding ann. |
|---:|---|---|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | ON Semiconductor Corporation | `ON-USDT-SWAP` | **95** | **CORE** | 0.40 | 16.7 | 41.4% | 13.1% | 5.6% | 0.0% |
| 2 | DraftKings Inc. | `DKNG-USDT-SWAP` | **95** | **CORE** | 0.14 | 12.5 | 88.4% | 13.3% | 4.4% | 0.0% |
| 3 | SK hynix | `SKHY-USDT-SWAP` | **90** | **CORE** | 0.11 | 3.7 | 33.4% | 54.1% | 4.5% | 0.0% |
| 4 | POP MART | `POPMART-USDT-SWAP` | **85** | **CORE** | 0.58 | 12.6 | 21.5% | 17.2% | 2.9% | 0.0% |
| 5 | Applovin Corporation | `APP-USDT-SWAP` | **83** | **CORE** | 0.53 | 14.7 | 27.7% | 26.7% | 3.1% | 48.6% |
| 6 | Taiwan Semiconductor Manufactur | `TSM-USDT-SWAP` | **82** | **CORE** | 0.70 | 20.7 | 29.5% | 34.5% | 31.1% | 0.0% |
| 7 | Hewlett Packard Enterprise Comp | `HPE-USDT-SWAP` | **82** | **CORE** | 0.67 | 13.6 | 20.2% | 17.1% | 5.7% | 0.0% |
| 8 | Bending Spoons S.p.A. | `BSP-USDT-SWAP` | **80** | **WATCH** | 0.41 | 16.6 | 40.3% | 45.6% | — | 0.0% |
| 9 | Coinbase Global, Inc. | `COIN-USDT-SWAP` | **80** | **WATCH** | 0.28 | 67.6 | 239.9% | 29.5% | 5.3% | 0.0% |
| 10 | Take-Two Interactive Software,  | `TTWO-USDT-SWAP` | **78** | **CORE** | 0.11 | 19.7 | 187.0% | 8.8% | 3.3% | 8.4% |

## All OKX companies — our ratio + LONG/SHORT scores

| Company | OKX | Our ratio | Fwd P/E | Trail P/E | EPS +1y | Rev +1y | FCF yield | LONG | SHORT | Funding ann. |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| DraftKings Inc. | `DKNG` | 0.14 | 12.5 | — | 88.4% | 13.3% | 4.4% | **95 CORE** | **0** | 0.0% |
| ON Semiconductor Corporation | `ON` | 0.40 | 16.7 | 49.4 | 41.4% | 13.1% | 5.6% | **95 CORE** | **5** | 0.0% |
| SK hynix | `SKHY` | 0.11 | 3.7 | — | 33.4% | 54.1% | 4.5% | **90 CORE** | **10** | 0.0% |
| Okta, Inc. | `OKTA` | 4.04 | 46.2 | 121.8 | 11.4% | 10.0% | 2.9% | **8** | **90 CORE** | 0.0% |
| POP MART | `POPMART` | 0.58 | 12.6 | 13.3 | 21.5% | 17.2% | 2.9% | **85 CORE** | **0** | 0.0% |
| Twilio Inc. | `TWLO` | 2.91 | 42.3 | 39.6 | 14.5% | 11.5% | 2.2% | **0** | **85 CORE** | 0.0% |
| Applovin Corporation | `APP` | 0.53 | 14.7 | 23.9 | 27.7% | 26.7% | 3.1% | **83 CORE** | **10** | 48.6% |
| Hewlett Packard Enterprise Comp | `HPE` | 0.67 | 13.6 | 32.5 | 20.2% | 17.1% | 5.7% | **82 CORE** | **10** | 0.0% |
| Taiwan Semiconductor Manufactur | `TSM` | 0.70 | 20.7 | 33.5 | 29.5% | 34.5% | 31.1% | **82 CORE** | **10** | 0.0% |
| Bending Spoons S.p.A. | `BSP` | 0.41 | 16.6 | 76.3 | 40.3% | 45.6% | — | **80 WATCH** | **15** | 0.0% |
| Coinbase Global, Inc. | `COIN` | 0.28 | 67.6 | — | 239.9% | 29.5% | 5.3% | **80 WATCH** | **15** | 0.0% |
| CrowdStrike Holdings, Inc. | `CRWD` | 5.80 | 161.4 | 8641.7 | 27.9% | 22.6% | 0.8% | **25** | **80** | 0.0% |
| Take-Two Interactive Software,  | `TTWO` | 0.11 | 19.7 | — | 187.0% | 8.8% | 3.3% | **78 CORE** | **10** | 8.4% |
| Applied Materials, Inc. | `AMAT` | 0.59 | 26.4 | 41.9 | 44.3% | 34.8% | 0.8% | **77 WATCH** | **15** | 0.0% |
| Blackstone Inc. | `BX` | 0.63 | 15.3 | 25.7 | 24.4% | 23.9% | — | **77 WATCH** | **0** | 12.4% |
| Broadcom Inc. | `AVGO` | 0.27 | 18.0 | 44.5 | 66.2% | 63.7% | 1.8% | **75 WATCH** | **35** | 18.6% |
| Credo Technology Group Holding  | `CRDO` | 0.37 | 19.9 | 74.1 | 53.9% | 55.0% | 0.7% | **75 WATCH** | **35** | 0.0% |
| Hims & Hers Health, Inc. | `HIMS` | 0.22 | 39.0 | — | 174.8% | 24.6% | 12.7% | **75 WATCH** | **10** | 0.0% |
| LGELECTRONICS | `LGELECTRONICS` | 0.57 | 12.7 | — | 22.3% | 40.6% | 3.2% | **75 CORE** | **10** | 49.3% |
| Micron Technology, Inc. | `MU` | 0.06 | 6.5 | 24.4 | 118.6% | 92.1% | 0.6% | **75 WATCH** | **20** | 0.0% |
| NVIDIA Corporation | `NVDA` | 0.21 | 14.6 | 28.5 | 68.5% | 65.9% | 0.8% | **75 WATCH** | **20** | 0.0% |
| Reddit, Inc. | `RDDT` | 0.47 | 14.8 | 33.3 | 31.4% | 31.8% | 2.5% | **75 WATCH** | **20** | 0.0% |
| Sandisk Corporation | `SNDK` | 0.28 | 6.5 | 24.1 | 23.2% | 18.3% | 3.1% | **75 CORE** | **10** | 0.3% |
| Western Digital Corporation | `WDC` | 0.25 | 14.3 | 17.0 | 58.0% | 36.8% | 1.4% | **75 WATCH** | **20** | 0.0% |
| Vertiv Holdings, LLC | `VRT` | 0.74 | 26.8 | 55.1 | 36.0% | 30.1% | 2.9% | **75 CORE** | **25** | 96.3% |
| ZHONGJI INNOLIGHT | `ZHONGJI` | 0.10 | 12.2 | 44.4 | 122.1% | 99.5% | 0.0% | **75 WATCH** | **35** | 75.0% |
| Intuitive Surgical, Inc. | `ISRG` | 2.82 | 34.3 | 46.5 | 12.2% | 12.8% | 1.8% | **5** | **75** | 0.0% |
| Advanced Micro Devices, Inc. | `AMD` | 0.37 | 39.0 | 155.5 | 105.6% | 73.2% | 0.9% | **70 WATCH** | **15** | 0.0% |
| Robinhood Markets, Inc. | `HOOD` | 0.98 | 33.5 | 52.9 | 34.1% | 27.9% | — | **70 WATCH** | **5** | 0.0% |
| Marvell Technology, Inc. | `MRVL` | 0.61 | 37.2 | 83.7 | 60.7% | 51.3% | 1.1% | **70 WATCH** | **15** | 0.0% |
| Oracle Corporation | `ORCL` | 0.34 | 12.1 | 21.5 | 35.1% | 45.3% | -11.4% | **70 WATCH** | **0** | 27.5% |
| Tower Semiconductor Ltd. | `TSEM` | 0.47 | 34.0 | 90.8 | 72.4% | 37.9% | 0.7% | **70 WATCH** | **15** | 0.0% |
| XIAOMI-W | `XIAOMI` | 0.41 | 16.4 | 17.8 | 39.7% | 24.3% | -1.3% | **70 WATCH** | **0** | 171.8% |
| Ciena Corporation | `CIEN` | 0.38 | 29.2 | 77.2 | 76.5% | 30.7% | 1.3% | **67 WATCH** | **35** | 0.0% |
| Lumentum Holdings Inc. | `LITE` | 0.45 | 26.5 | — | 59.6% | 52.2% | 0.3% | **67 WATCH** | **20** | 0.0% |
| Eli Lilly and Company | `LLY` | 0.87 | 24.9 | 39.7 | 28.6% | 15.4% | 1.0% | **67 WATCH** | **20** | 0.0% |
| Adobe Inc. | `ADBE` | 0.64 | 8.3 | 13.1 | 13.0% | 9.2% | 10.2% | **65 WATCH** | **30** | 30.2% |
| HANMISemi | `HANMI` | 0.89 | 50.4 | — | 56.4% | 55.7% | 0.3% | **65 WATCH** | **25** | -559.2% |
| Snowflake Inc. | `SNOW` | 3.01 | 108.9 | — | 36.2% | 28.5% | 1.5% | **25** | **65** | 0.0% |
| BlackBerry Limited | `BB` | 2.64 | 38.5 | 88.0 | 14.6% | 9.9% | 2.7% | **13** | **65** | 8.1% |
| Rocket Lab Corporation | `RKLB` | 23.26 | 1584.5 | — | 68.1% | 42.2% | -0.5% | **10** | **65** | 0.0% |
| USA Rare Earth, Inc. | `USAR` | 4.56 | 480.5 | — | 105.3% | 870.1% | -5.2% | **10** | **65** | 8.3% |
| Applied Optoelectronics, Inc. | `AAOI` | 0.04 | 21.0 | — | 576.8% | 156.5% | -10.8% | **62 WATCH** | **0** | 43.8% |
| ASML Holding N.V. - New York Re | `ASML` | 0.86 | 30.1 | 60.2 | 35.0% | 27.3% | 1.2% | **60 WATCH** | **35** | 0.0% |
| Cerebras Systems Inc. | `CBRS` | 0.42 | 154.5 | — | 371.3% | 232.7% | — | **60 WATCH** | **25** | 45.6% |
| Corning Incorporated | `GLW` | 1.05 | 34.7 | 72.5 | 33.0% | 19.2% | 0.6% | **60 WATCH** | **15** | 6.6% |
| Space Exploration Technologies  | `SPCX` | 0.02 | 83.5 | — | 5097.3% | 150.7% | — | **60 WATCH** | **25** | 6.3% |
| UnitedHealth Group Incorporated | `UNH` | 1.21 | 16.7 | 24.2 | 13.8% | 2.9% | 7.2% | **60 WATCH** | **10** | 0.0% |
| Astera Labs, Inc. | `ALAB` | 0.94 | 54.9 | 178.3 | 58.6% | 55.8% | 0.2% | **55 WATCH** | **60** | 0.0% |
| Bloom Energy Corporation | `BE` | 0.65 | 53.3 | 337.0 | 82.2% | 65.0% | 0.7% | **55 WATCH** | **60** | 0.0% |
| Palantir Technologies Inc. | `PLTR` | 1.82 | 80.7 | 160.2 | 44.4% | 49.7% | 0.5% | **33** | **60** | 0.0% |
| Palo Alto Networks, Inc. | `PANW` | 2.00 | 80.4 | 911.8 | 40.2% | 14.5% | 1.3% | **28** | **60** | — |
| Dell Technologies Inc. | `DELL` | 22.49 | 18.7 | 32.8 | 0.8% | 15.8% | 1.7% | **25** | **60** | 0.0% |
| Tesla, Inc. | `TSLA` | 7.04 | 165.3 | 343.7 | 23.5% | 13.8% | 0.3% | **22** | **60 WATCH** | 19.7% |
| Coca-Cola Company (The) | `KO` | 3.63 | 24.7 | 26.4 | 6.8% | 0.2% | 1.4% | **7** | **60** | 0.0% |
| Apple Inc. | `AAPL` | 4.11 | 35.3 | 39.1 | 8.6% | 10.5% | 2.2% | **5** | **60** | 0.0% |
| Microsoft Corporation | `MSFT` | 1.09 | 21.5 | 28.4 | 19.8% | 19.5% | 0.4% | **59 WATCH** | **20** | 0.0% |
| NAVER | `NAVER` | 0.96 | 13.3 | — | 13.9% | 14.1% | 3.1% | **58 WATCH** | **30** | 51.5% |
| ServiceNow, Inc. | `NOW` | 1.14 | 26.3 | 82.2 | 23.1% | 18.8% | 3.8% | **57 CORE** | **25** | 0.0% |
| Cognex Corporation | `CGNX` | 1.49 | 29.1 | 56.5 | 19.5% | 9.7% | 2.0% | **44** | **55** | 0.0% |
| BitMine Immersion Technologies, | `BMNR` | 0.28 | 28.6 | — | 103.2% | 421.8% | -3.2% | **52** | **20** | 26.4% |
| Coherent Corp. | `COHR` | 0.42 | 20.2 | 71.9 | 48.2% | 38.2% | -1.2% | **52** | **35** | 18.0% |
| Super Micro Computer, Inc. | `SMCI` | 0.34 | 7.8 | 13.3 | 22.8% | 17.3% | -30.5% | **52** | **20** | 0.0% |
| GoPro, Inc. | `GPRO` | -1.35 | -133.0 | — | 98.6% | 35.5% | 21.5% | **50** | **0** | 0.0% |
| Strategy Inc | `MSTR` | 0.02 | 3.2 | — | 156.0% | 2.2% | -36.0% | **50** | **20** | 15.6% |
| Teradyne, Inc. | `TER` | 1.22 | 34.4 | 55.0 | 28.2% | 21.8% | 0.7% | **50** | **35** | 0.0% |
| Netflix, Inc. | `NFLX` | 2.89 | 18.2 | 22.4 | 6.3% | 11.3% | 8.8% | **35** | **50** | 22.4% |
| Zoom Communications, Inc. | `ZM` | 4.13 | 13.8 | 8.3 | 3.3% | 4.2% | 7.8% | **30** | **50** | 0.0% |
| Wendy's Company (The) | `WEN` | 3.55 | 12.3 | 9.8 | 3.5% | -0.5% | 14.2% | **20** | **50** | 0.0% |
| KLA Corporation | `KLAC` | 1.23 | 28.2 | 51.3 | 22.9% | 18.2% | 1.1% | **49** | **35** | 0.0% |
| Lam Research Corporation | `LRCX` | 1.12 | 26.8 | 54.7 | 24.0% | 18.4% | 0.8% | **49** | **35** | 0.0% |
| Intel Corporation | `INTC` | 1.58 | 56.3 | — | 35.6% | 14.2% | 0.8% | **28** | **45** | 17.3% |
| Rockwell Automation, Inc. | `ROK` | 2.32 | 29.0 | 40.6 | 12.5% | 5.7% | 2.7% | **15** | **45** | 0.0% |
| Circle Internet Group, Inc. | `CRCL` | 1.82 | 56.1 | 17.2 | 30.9% | 24.1% | 0.9% | **43** | **25** | 21.6% |
| Arm Holdings plc | `ARM` | 2.48 | 92.8 | 286.2 | 37.4% | 36.2% | 0.4% | **35** | **40** | 15.3% |
| GameStop Corporation | `GME` | 3.87 | 12.9 | 15.4 | 3.3% | 11.0% | 0.7% | **30** | **40** | 0.0% |
| Meta Platforms, Inc. | `META` | 2.28 | 20.5 | 28.3 | 9.0% | 20.6% | 1.2% | **17** | **40** | 0.0% |
| Alphabet Inc. | `GOOGL` | — | 22.7 | 17.3 | -27.6% | 23.3% | 0.5% | **2** | **40** | 0.0% |
| Amazon.com, Inc. | `AMZN` | — | 23.5 | 20.1 | -18.5% | 14.4% | 0.1% | **0** | **40** | 0.0% |
| CoreWeave, Inc. | `CRWV` | -3.15 | -46.7 | — | 14.8% | 104.0% | -19.4% | **0** | **40** | 0.0% |
| IREN LIMITED | `IREN` | — | -10.5 | — | -16.4% | 158.8% | -25.7% | **0** | **40** | 0.0% |
| Nebius Group N.V. | `NBIS` | — | -66.4 | — | -123.5% | 270.0% | -16.3% | **0** | **40** | 0.0% |
| SOFTBANK GROUP CORP | `SOFTBANK` | — | 20.4 | 6.9 | -39.7% | 7.2% | -6.4% | **0** | **40** | 0.0% |
| Fluence Energy, Inc. | `FLNC` | -0.40 | -28.2 | — | 70.1% | 36.0% | 0.2% | **35** | **0** | 0.0% |
| KIOXIA HOLDINGS CORPORATION | `KIOXIA` | — | — | 17.7 | 36.8% | 30.0% | 3.0% | **33** | **10** | 37.5% |
| International Business Machines | `IBM` | 2.47 | 16.8 | 20.0 | 6.8% | 3.9% | 5.8% | **30** | **30** | 0.0% |
| Cisco Systems, Inc. | `CSCO` | 2.06 | 19.0 | 32.1 | 9.2% | 6.6% | 2.7% | **23** | **30** | 0.0% |
| Salesforce, Inc. | `CRM` | — | 14.2 | 20.8 | -4.5% | 9.7% | 9.5% | **20** | **30** | 0.0% |
| Johnson & Johnson | `JNJ` | 2.33 | 22.4 | 31.4 | 9.6% | 7.4% | 2.6% | **15** | **30** | 0.0% |
| GE Vernova Inc. | `GEV` | — | 37.8 | 27.5 | -19.3% | 13.9% | 6.2% | **5** | **30** | 0.0% |
| ExxonMobil Holdings Corporation | `XOM` | — | 14.7 | 20.7 | -7.4% | -1.2% | 3.1% | **0** | **30** | 0.0% |
| QUALCOMM Incorporated | `QCOM` | — | 18.4 | 23.1 | -2.7% | 4.8% | 5.1% | **25** | **10** | 1.2% |
| Applied Digital Corporation | `APLD` | -0.91 | -50.7 | — | 55.6% | 131.1% | -67.6% | **20** | **0** | 0.0% |
| AST SpaceMobile, Inc. | `ASTS` | -0.91 | -47.3 | — | 51.8% | 285.4% | -7.6% | **20** | **0** | 3.3% |
| Intuitive Machines, Inc. | `LUNR` | -1.40 | -98.1 | — | 70.2% | 28.2% | -3.3% | **10** | **20** | 0.0% |
| Ondas Inc | `ONDS` | -4.24 | -384.0 | — | 90.5% | 87.7% | -1.5% | **10** | **20** | 0.0% |
| Redwire Corporation | `RDW` | -1.21 | -32.9 | — | 27.1% | 18.6% | -0.9% | **10** | **20** | 0.0% |
| Rivian Automotive, Inc. | `RIVN` | -0.76 | -8.5 | — | 11.1% | 58.3% | -7.2% | **0** | **20** | 0.0% |
| SharonAI Holdings, Inc. | `SHAZ` | -0.13 | -6.7 | — | 51.6% | 1195.1% | -12.1% | **15** | **10** | 105.2% |
| AMC Entertainment Holdings, Inc | `AMC` | — | -41.1 | — | — | 4.1% | 4.9% | **10** | **10** | 0.0% |
| RoboStrategy, Inc. | `BOT` | — | — | — | — | — | — | **0** | **0** | 377.2% |

## Files

- `scanner.py` — scanner and scoring logic
- `reports/latest.md` — latest full report
- `data/latest.csv` — latest machine-readable snapshot
- `data/history.csv` — hourly history of **all companies** for later backtests
- `.github/workflows/hourly-okx-scanner.yml` — hourly GitHub Action

## Data

OKX public market data provides the TradFi/perpetual context and funding. Yahoo Finance/yfinance supplies valuation, cash-flow and analyst-growth estimates. Availability can differ by OKX account/jurisdiction.

This is a quantitative research screen, not an automatic trading system. It does not place orders or select leverage.
