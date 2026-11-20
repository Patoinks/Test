# BTC ↔ Hong Kong Correlation Scanner

**Updated:** 2026-11-20 03:31 UTC

Purpose: test whether Bitcoin weakness is associated with Hong Kong market weakness,
without mixing ordinary intraday co-movement with the overnight period when HKEX is closed.

## Summary

| Asset | Same 5m corr | Best BTC lead | Best corr | BTC -0.25%/5m events | HK down hit-rate | Avg HK return on BTC drop | Overnight corr | BTC-down -> negative open | Avg opening gap when BTC down |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Hang Seng Index | +0.19 | 0m | +0.19 | 52 | 62% | -0.03% | +0.35 | 63% | -0.30% |
| Hang Seng TECH | +0.21 | 0m | +0.21 | 52 | 65% | -0.07% | +0.46 | 70% | -0.51% |
| Xiaomi | +0.09 | 0m | +0.09 | 49 | 51% | -0.01% | +0.13 | 41% | +0.09% |

## BTC lead / lag detail

0m means the same 5-minute bar. 15m means the BTC return happened 15 minutes before the Hong Kong return.

| Asset | BTC lead | Correlation | Samples |
|---|---:|---:|---:|
| Hang Seng Index | 0m | +0.19 | 2809 |
| Hang Seng Index | 5m | +0.01 | 2809 |
| Hang Seng Index | 15m | +0.02 | 2809 |
| Hang Seng Index | 30m | +0.05 | 2809 |
| Hang Seng Index | 60m | -0.02 | 2809 |
| Hang Seng TECH | 0m | +0.21 | 2809 |
| Hang Seng TECH | 5m | +0.00 | 2809 |
| Hang Seng TECH | 15m | +0.03 | 2809 |
| Hang Seng TECH | 30m | +0.04 | 2809 |
| Hang Seng TECH | 60m | -0.03 | 2809 |
| Xiaomi | 0m | +0.09 | 2642 |
| Xiaomi | 5m | -0.02 | 2642 |
| Xiaomi | 15m | +0.01 | 2642 |
| Xiaomi | 30m | +0.04 | 2642 |
| Xiaomi | 60m | -0.01 | 2642 |

## Method

- Intraday: 5-minute returns over the latest ~60 days available from Yahoo Finance.
- Session gaps and the HK lunch break are excluded from the intraday return pairs.
- Stress test: when BTC falls at least 0.25% in a 5-minute bar, measure how often HK is also down and the average HK return.
- Overnight: BTC return from 16:10 HKT after the previous HK session to 09:30 HKT at the next continuous-session open, compared with the next HK opening gap.
- Assets: Hang Seng Index, Hang Seng TECH, and Xiaomi 1810.HK.

Correlation is descriptive, not proof of causality or a trade signal. The short intraday history available at 5-minute resolution can change materially as new sessions are added.
