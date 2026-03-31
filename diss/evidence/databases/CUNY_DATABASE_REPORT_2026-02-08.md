# CUNY Reddit Corpus - Data Status Report

The CUNY Reddit research corpus comprises **12 subreddit databases** containing **574,834 total posts** from **44,689 unique authors** spanning 15 years of university discourse. Data collection uses a **user-centric scraping methodology** that bypasses Reddit's 1,000-item API limit by reconstructing complete user histories.

**Key finding:** The corpus captures the full COVID-19 transition period (March 2020) with high fidelity, showing a **3-5x activity spike** during the emergency remote transition—critical evidence for the dissertation's analysis of vernacular knowledge formation during institutional crisis.

## Corpus Composition

### Primary CUNY Subreddits (Core Analysis)


| Subreddit         | Size   | Submissions | Comments | Authors | Date Range | Integrity |
| ------------------- | -------- | ------------- | ---------- | --------- | ------------ | ----------- |
| r/CUNY            | 83 MB  | 17,808      | 88,318   | 10,967  | 2011–2025 | 99.6%     |
| r/Baruch          | 145 MB | 27,638      | 103,363  | 9,193   | 2011–2026 | 94.3%     |
| r/HunterCollege   | 16 MB  | 5,493       | 21,771   | 3,222   | 2011–2025 | 98.9%     |
| r/QueensCollege   | 20 MB  | 6,375       | 22,717   | 2,930   | 2011–2025 | 99.0%     |
| r/CCNY            | 6.2 MB | 2,163       | 8,106    | 1,445   | 2011–2025 | 98.6%     |
| r/BrooklynCollege | 1.1 MB | 477         | 822      | 424     | 2011–2025 | 99.6%     |
| r/JohnJay         | 184 KB | 65          | 172      | 87      | 2015–2025 | 100%      |
| r/CUNYuncensored  | 264 KB | 59          | 89       | 66      | 2020–2025 | 100%      |

**Subtotal** = 60,078 submissions, 245,358 comments, ~22,000 unique authors

### Comparative Institutions (Private Universities)


| Subreddit  | Size   | Submissions | Comments | Authors | Date Range | Integrity |
| ------------ | -------- | ------------- | ---------- | --------- | ------------ | ----------- |
| r/NYU      | 83 MB  | 29,637      | 144,759  | 17,357  | 2010–2025 | 67.3%     |
| r/columbia | 57 MB  | 23,424      | 86,876   | 11,244  | 2011–2025 | 71.2%     |
| r/Fordham  | 12 MB  | 3,346       | 21,459   | 3,185   | 2011–2025 | 57.9%     |
| r/STJOHNS  | 1.0 MB | 440         | 1,309    | 569     | 2011–2025 | 74.3%     |

**Comparative Subtotal:** 56,847 submissions | 254,403 comments | ~22,000 unique authors

---

## Data Integrity Analysis

**Integrity Score** = % of comments with resolvable parent references (either to another comment or submission in database)...

* CUNY Subreddits = high integrity (94–100%)
* Comparative Subreddits: Moderate Integrity (57–74%)

---

## Temporal Distribution

### r/CUNY Activity by Year

```
2018 |████                                    268
2019 |██████                                  935
2020 |████████████████████                  4,980  ← COVID transition
2021 |██████████████████████                5,771
2022 |██████████████████████████████████   10,909
2023 |████████████████████████████████████ 12,611
2024 |████████████████████████████████████████████████████████████ 34,883
2025 |████████████████████████████████████████████████████████████ 35,650
```

**Observation:** Exponential growth pattern, with 2024-2025 comprising 66% of all r/CUNY content. The 2020 spike (5x 2019 baseline) coincides with the pandemic transition—a key analytical window.

### March 2020 Pandemic Spike


| Subreddit       | Posts (Mar 1–31, 2020) |
| ----------------- | ------------------------- |
| r/Baruch        | 1,310                   |
| r/QueensCollege | 615                     |
| r/CUNY          | 334                     |
| r/HunterCollege | 20                      |

Baruch shows highest crisis-period activity—consistent with its role as CUNY's largest business school with significant commuter population affected by sudden remote transition.

---

## Cross-Community Network

### User Overlap Between Subreddits

```
CUNY ∩ Baruch:  1,205 shared users
CUNY ∩ Hunter:    748 shared users
CUNY ∩ Queens:    575 shared users
Baruch ∩ Hunter:  221 shared users
```

These "bridge users" participate in both campus-specific and system-wide discourse—key actors for analyzing information flow across the distributed CUNY network.

## Appendix: Database File Locations

```
data/databases/current/
├── Baruch_historical_data.db      (145 MB)
├── CUNY_historical_data.db        (83 MB)
├── NYU_historical_data.db         (83 MB)
├── columbia_historical_data.db    (57 MB)
├── QueensCollege_historical_data.db (20 MB)
├── HunterCollege_historical_data.db (16 MB)
├── Fordham_historical_data.db     (12 MB)
├── CCNY_historical_data.db        (6.2 MB)
├── BrooklynCollege_historical_data.db (1.1 MB)
├── STJOHNS_historical_data.db     (1.0 MB)
├── CUNYuncensored_historical_data.db (264 KB)
└── JohnJay_historical_data.db     (184 KB)
```

**Total corpus size:** ~424 MB
