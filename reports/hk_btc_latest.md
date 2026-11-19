# BTC ↔ Hong Kong Correlation Scanner

**Updated:** 2026-11-19 03:37 UTC

Purpose: test whether Bitcoin weakness is associated with Hong Kong market weakness,
without mixing ordinary intraday co-movement with the overnight period when HKEX is closed.

## Summary

| Asset | Same 5m corr | Best BTC lead | Best corr | BTC -0.25%/5m events | HK down hit-rate | Avg HK return on BTC drop | Overnight corr | BTC-down -> negative open | Avg opening gap when BTC down |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Hang Seng Index | +0.18 | 0m | +0.18 | 49 | 63% | -0.02% | +0.35 | 62% | -0.25% |
| Hang Seng TECH | +0.20 | 0m | +0.20 | 49 | 67% | -0.07% | +0.48 | 69% | -0.41% |
| Xiaomi | +0.09 | 0m | +0.09 | 46 | 54% | -0.03% | +0.16 | 38% | +0.14% |

## BTC lead / lag detail

0m means the same 5-minute bar. 15m means the BTC return happened 15 minutes before the Hong Kong return.

| Asset | BTC lead | Correlation | Samples |
|---|---:|---:|---:|
| Hang Seng Index | 0m | +0.18 | 2810 |
| Hang Seng Index | 5m | +0.03 | 2810 |
| Hang Seng Index | 15m | +0.01 | 2810 |
| Hang Seng Index | 30m | +0.04 | 2810 |
| Hang Seng Index | 60m | -0.02 | 2810 |
| Hang Seng TECH | 0m | +0.20 | 2810 |
| Hang Seng TECH | 5m | +0.02 | 2810 |
| Hang Seng TECH | 15m | +0.03 | 2810 |
| Hang Seng TECH | 30m | +0.04 | 2810 |
| Hang Seng TECH | 60m | -0.02 | 2810 |
| Xiaomi | 0m | +0.09 | 2643 |
| Xiaomi | 5m | -0.01 | 2643 |
| Xiaomi | 15m | +0.02 | 2643 |
| Xiaomi | 30m | +0.04 | 2643 |
| Xiaomi | 60m | -0.01 | 2643 |

## Method

- Intraday: 5-minute returns over the latest ~60 days available from Yahoo Finance.
- Session gaps and the HK lunch break are excluded from the intraday return pairs.
- Stress test: when BTC falls at least 0.25% in a 5-minute bar, measure how often HK is also down and the average HK return.
- Overnight: BTC return from 16:10 HKT after the previous HK session to 09:30 HKT at the next continuous-session open, compared with the next HK opening gap.
- Assets: Hang Seng Index, Hang Seng TECH, and Xiaomi 1810.HK.

Correlation is descriptive, not proof of causality or a trade signal. The short intraday history available at 5-minute resolution can change materially as new sessions are added.
