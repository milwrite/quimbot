# CUNY Reddit Corpus - Participation Baselines Report

The CUNY Reddit ecosystem comprises **24,857 unique users** generating **274,950 contributions** across 8 subreddits. Compared to Reddit at large, CUNY communities show **2-3x higher participation rates**, with 17x more power users and a distinctive comment-dominant culture where 44.4% of users exclusively answer others' questions.

**Key finding:** While Reddit's 90-9-1 rule predicts 90% lurkers, CUNY subreddits show only 34.3% one-time contributors—reflecting the practical mutual-aid function of student communities navigating bureaucratic complexity.

## Participation vs. Reddit Baselines


| Metric | Reddit Baseline | CUNY | Multiplier |
| -------- | ----------------- | ------ | ------------ |
| Lurker rate | 90-98% | 34.3% | **2.6x more active** |
| Regular contributors (10+) | 1-2% | 20.6% | **10-20x higher** |
| Power users (100+) | <0.1% | 1.7% | **17x higher** |
| Comments per user | ~7 | 9.4 | **1.3x more** |

---

## Contributor Typology

### Six-Tier Participation Model


| Tier | Contributions | Users | % | Role |
| ------ | --------------- | ------- | ---- | ------ |
| One-time | 1 | 8,535 | 34.3% | Drop-in askers |
| Light | 2-4 | 7,177 | 28.9% | Occasional |
| Moderate | 5-10 | 4,023 | 16.2% | Semi-regular |
| Regular | 11-50 | 4,054 | 16.3% | Consistent |
| Heavy | 51-100 | 652 | 2.6% | Reliable answerers |
| Super | 100+ | 416 | 1.7% | Community stewards |

### Contribution Distribution

```
One-time  |████████████████████████████████████  34.3%  (8,535)
Light     |██████████████████████████████        28.9%  (7,177)
Moderate  |████████████████                      16.2%  (4,023)
Regular   |████████████████                      16.3%  (4,054)
Heavy     |███                                    2.6%    (652)
Super     |██                                     1.7%    (416)
```

**Observation:** The 416 super contributors (1.7%) function as de facto community stewards—17x the Reddit baseline for sustained engagement.

---

## Behavioral Modalities


| Behavior | Users | % | Interpretation |
| ---------- | ------- | ---- | ---------------- |
| Comment-only | 11,039 | 44.4% | Reactive helpers |
| Both post & comment | 9,409 | 37.9% | Full participants |
| Post-only | 4,409 | 17.7% | Question-askers |

**Observation:** The comment-dominant culture (44.4% never post) indicates Q&A forum structure rather than content broadcasting—characteristic of support communities.

---

## Per-Campus Engagement


| Community | Users | Avg/User | Posts/User | Comments/User |
| ----------- | ------- | ---------- | ------------ | --------------- |
| r/Baruch | 9,265 | 12.76 | 1.98 | 10.78 |
| r/CUNY | 10,967 | 8.75 | 1.13 | 7.62 |
| r/QueensCollege | 2,930 | 8.66 | 1.44 | 7.22 |
| r/HunterCollege | 3,222 | 7.66 | 1.23 | 6.43 |
| r/CCNY | 1,445 | 6.40 | 1.09 | 5.31 |
| r/BrooklynCollege | 424 | 2.60 | 0.82 | 1.78 |
| r/JohnJay | 87 | 2.33 | 0.61 | 1.72 |

**Observation:** Baruch leads at 12.76 contributions/user (1.8x Reddit baseline)—likely reflecting Zicklin Business School's networking culture.

![CUNY Reddit Participation Typology](/Users/zacharymuhlbauer/Desktop/studio/projects/reddit-diss/00_ACTIVE/visualizations/13_participation_typology/viz13_participation_typology.png)

---

## Cross-Community Participation

### Bridge User Distribution


| Subreddit Span | Users | % | Category |
| ---------------- | ------- | ---- | ---------- |
| 1 subreddit | 21,794 | 87.7% | Community-bound |
| 2 subreddits | 2,675 | 10.8% | Dual participants |
| 3+ subreddits | 388 | 1.6% | Bridge users |

### Bridge User Network Impact


| Metric | Reddit Baseline | CUNY | Significance |
| -------- | ----------------- | ------ | -------------- |
| Cross-subreddit rate | 17.7% | 12.3% | Institutionally-focused |
| Meaningful dual participation | 1.2% | 2.8% | **2.3x baseline** |
| Cross-community edges | — | 4,891 | Binds 8 subreddits |
| Clustering improvement | — | 1.9x | 0.18 → 0.34 |

**Observation:** The 1.6% bridge users create 4,891 cross-community edges, improving network clustering by 1.9x. Cross-community replies are 3x more efficient at network cohesion per edge.

![Bridge User Ego Networks](/Users/zacharymuhlbauer/Desktop/studio/projects/reddit-diss/00_ACTIVE/visualizations/12_bridge_user_connections/viz12_bridge_connections.png)

---

## Information Flow Analysis

From 22,782 detected flow events:

```
r/CUNY outflow  |██████████████████████████████  51.7%  (11,769 events)
r/CUNY inflow   |████████████████████████████    46.3%  (10,556 events)
Net outflow     |██                               +5.4%  (1,213 events)
```

**Observation:** r/CUNY functions as primary knowledge hub with bidirectional exchange. Policy knowledge flows outward; campus-specific questions flow inward.

### Edge Type Efficiency


| Activity Type | Edges | % of Total | Clustering Contribution |
| --------------- | ------- | ------------ | ------------------------- |
| Cross-Community Replies | 4,891 | 17% | **0.52** (highest) |
| Comment Replies | 14,221 | 49% | 0.42 |
| Thread Participation | 6,892 | 24% | 0.31 |
| Submission Responses | 2,788 | 10% | 0.24 |

**Observation:** Cross-community edges (17% of total) contribute 52% of clustering improvement—Granovetter's "strength of weak ties" quantified.

---

## Appendix: Data Sources

```
Database Analysis:
├── 8 CUNY SQLite databases
├── 24,857 unique users
├── 274,950 total contributions
└── Analysis date: February 2026

Reddit Baselines:
├── Nielsen (2006) — 90-9-1 Rule
├── Higher Logic (2024) — Updated participation rates
├── PMC9455283 (2022) — Cross-subreddit participation
├── arXiv:2507.16857 (2025) — Meaningful dual participation
└── Science Advances (2025) — Power user behavior
└── Machado et al. arXiv:2503.02661 (2025) — Gini coefficient methodology
```

---

## Participation Inequality (Gini Coefficient)

Following the methodology of Machado et al. (2025), we calculate the Gini coefficient to quantify inequality in user activity distribution. The Gini coefficient ranges from 0 (perfect equality) to 1 (total inequality).

**CUNY Ecosystem Gini Coefficient: 0.738**

| Metric | Value | Interpretation |
| ------ | ----- | -------------- |
| Ecosystem Gini | **0.738** | High inequality |
| Top 1% share | 23.3% | Super-Pareto |
| Top 10% share | 63.9% | — |
| Top 20% share | 78.4% | — |
| Median comments/user | 3 | Low floor |
| 99th percentile | 140 | High ceiling |

### Per-Subreddit Gini Coefficients

| Subreddit | Users | Gini | Top 20% Share | Size Category |
| --------- | ----- | ---- | ------------- | ------------- |
| r/Baruch | 7,521 | **0.740** | 78.5% | Large |
| r/CUNY | 8,956 | **0.725** | 77.3% | Large |
| r/HunterCollege | 2,685 | 0.686 | 73.5% | Medium |
| r/QueensCollege | 2,479 | 0.677 | 72.8% | Medium |
| r/CCNY | 1,181 | 0.650 | 70.0% | Medium |
| r/JohnJay | 55 | 0.499 | 59.3% | Small |
| r/BrooklynCollege | 296 | 0.472 | 55.4% | Small |
| r/CUNYuncensored | 44 | 0.401 | 51.2% | Small |

### Comparison to Reddit Baselines

| Community Size | Reddit Baseline Gini | CUNY Observed | Difference |
| -------------- | -------------------- | ------------- | ---------- |
| 10²-10³ users | 0.40-0.50 | 0.40-0.50 | Consistent |
| 10³-10⁴ users | 0.50-0.60 | 0.65-0.69 | **+0.10 higher** |
| 10⁴+ users | 0.60-0.70 | 0.72-0.74 | **+0.05 higher** |

**Observation:** CUNY's larger subreddits (Baruch, CUNY main) exhibit Gini coefficients 5-10 points above typical Reddit communities of similar size. This suggests more concentrated participation driven by a smaller core of "community stewards" who sustain the mutual-aid function.

![CUNY Gini Coefficient Analysis](/Users/zacharymuhlbauer/Desktop/studio/projects/reddit-diss/00_ACTIVE/visualizations/13_participation_typology/viz13_gini_inequality.png)

The Lorenz curve visualization (left panel) illustrates the cumulative distribution of comments across users. The area between each curve and the diagonal line of perfect equality represents the Gini coefficient—larger gaps indicate greater inequality. The CUNY ecosystem curve (black) bows significantly away from equality, confirming that a small minority of users generate the majority of content.

The size-inequality relationship (right panel) demonstrates that Gini coefficients increase predictably with community size. Smaller subreddits like r/CUNYuncensored (G=0.401) and r/BrooklynCollege (G=0.472) cluster near Reddit baselines for communities of their size. However, larger subreddits—particularly r/Baruch (G=0.740) and r/CUNY (G=0.725)—exceed typical baselines by 5-10 points, suggesting that CUNY's mutual-aid communities develop more pronounced hierarchies as they scale.

This elevated inequality has structural implications: the 416 "super contributors" who anchor these communities represent a critical but fragile resource. Their departure would disproportionately impact community knowledge production—a vulnerability that institutional administrators should recognize when assessing the sustainability of student-run support networks.
