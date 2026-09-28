# OKX Overvaluation Scanner

**Updated:** 2026-09-28 21:01 UTC
**OKX stock/RWA perps discovered:** 108
**Public companies with usable fundamentals:** 101
**CORE candidates:** 2

CORE rule: **Forward P/E > 40 + PEG(1y) > 2.5 + expected EPS growth next year < 20%**.

> Positive funding is generally favorable carry for a short; negative funding means the short generally pays. Funding is annualized mechanically from the current interval and can change quickly.

| Rank | Signal | Company | OKX perp | Score | Trail P/E | Fwd P/E | EPS +1y | PEG 1y | FCF yield | Rev +1y | Funding ann. |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | **CORE** | Okta, Inc. | `OKTA-USDT-SWAP` | **90** | 121.8 | 46.2 | 11.4% | 4.04 | 2.9% | 10.0% | -25.1% |
| 2 | **CORE** | Twilio Inc. | `TWLO-USDT-SWAP` | **85** | 39.6 | 42.3 | 14.5% | 2.91 | 2.2% | 11.5% | 0.0% |
| 3 | **WATCH** | Tesla, Inc. | `TSLA-USDT-SWAP` | **70** | 331.0 | 165.3 | 23.5% | 7.04 | 0.3% | 13.8% | 25.9% |

## Why each candidate scored

- **OKTA (90/100):** Forward P/E > 40; Trailing P/E > 40; PEG(1y) > 2.5; EPS growth < 20%; Revenue growth decelerating
- **TWLO (85/100):** Forward P/E > 40; PEG(1y) > 2.5; EPS growth < 20%; FCF yield < 2.5%; Revenue growth decelerating
- **TSLA (70/100):** Forward P/E > 40; Trailing P/E > 40; PEG(1y) > 2.5; FCF yield < 2.5%

## Interpretation

- **CORE** = satisfies the three central valuation-vs-growth conditions.
- **WATCH** = forward P/E > 40, expected EPS growth < 25%, plus PEG > 2 when calculable; it narrowly misses CORE.
- This is a research screen, not a prediction that the stock will fall.
- The scanner does not place trades or choose leverage.

Data: OKX EEA public API + Yahoo Finance/yfinance. Analyst estimates and funding can change between runs.
