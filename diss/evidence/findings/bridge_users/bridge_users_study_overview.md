# Bridge Users Analytical Suite

All materials for the bridge user analysis (Chapter 3) of the CUNY Reddit dissertation. Bridge users participate across multiple CUNY subreddit communities, creating the cross-community edges that hold the federated network together.

## Structure

```
bridge-users/
├── README.md
├── chapters/        3 Word docs — Chapter 3 drafts
├── findings/        Findings, lit review, methodology
├── visualizations/  Static images, interactive HTML, data JSON
├── scripts/         Python analysis pipeline (3 files)
└── interviews/      4 transcripts + protocol + NP audio
```

## Key Numbers

- 727 bridge users span 2+ communities (8.84% of active users)
- 229 core connectors span 3+ communities
- 11 super bridges span 4-5 communities
- 28,792 edges created, 83% from comments
- 1.9x clustering coefficient improvement (0.18 → 0.34)
- 4,891 cross-community edges binding 8 subreddits into one network

## chapters/

| File | Description |
|------|-------------|
| ch3-bridge-users.docx | Initial Chapter 3 draft |
| chapter_3_bridge_users_rewritten.docx | Revised draft (Jan 30 2025) |
| chapter_3_bridge_users_viz12.docx | Draft with embedded network visualizations (2.8 MB) |

## findings/

| File | Description |
|------|-------------|
| CUNY_BRIDGE_USERS_FINDINGS.md | Main findings — 727 bridge users, 7 behavioral categories, named profiles |
| CUNY_BRIDGE_USERS_FINDINGS.docx | Word version |
| bridge_users_literature_review.md | 55 KB lit review: Burt (structural holes), Putnam (bridging capital), Latour (ANT), Reddit platform architecture |
| chapter_3_methodology.md | Bridge user identification, network reconstruction, clustering analysis methods |
| chapter_3_methodology.pdf | PDF version |

## visualizations/

Two visualization suites, all files flat in one folder.

**Viz 5 — Edgewise Clustering** (how bridge users improve network clustering through edge creation):

| File | What it shows |
|------|---------------|
| viz5_bridge_clustering.png/pdf/svg | Static composite — edge creation by type, clustering impact |
| viz5_bridge_clustering_summary.md | Written summary with tables |
| viz5_bridge_clustering_data.json | Backing data |
| viz5_bridge_edge_network.html | Interactive edge network |
| viz5_clustering_impact.html | Clustering coefficient with/without bridges |
| viz5_community_activity.html | Activity patterns per community |
| viz5_edge_type_breakdown.html | Comment replies vs thread co-participation vs cross-community |
| viz5_posts_vs_comments.html | Why comments create 83% of edges |

**Viz 12 — Bridge User Connections** (ego networks for top 16 bridge users):

| File | What it shows |
|------|---------------|
| viz12_bridge_connections.png/pdf/svg | 16-panel grid of individual bridge user ego networks |
| viz12_connection_summary.md | Top 16 users: primary sub, communities spanned, reciprocity |
| viz12_connection_data.json | Backing data |
| viz12_bridge_connections.html | Interactive ego networks |

## scripts/

| File | Lines | What it does |
|------|-------|-------------|
| bridge_users_viz.py | 1,090 | Generates Viz 5 (edgewise clustering analysis) |
| viz12_bridge_ego_edges.py | 427 | Generates Viz 12 (ego network small multiples) |
| edge_data_extractor.py | ~300 | Shared dependency — queries 8 CUNY SQLite DBs, reconstructs edges via parent_id |

Regenerate from project root:

```bash
python3 scripts/analysis/visualization/bridge_users_viz.py
python3 scripts/analysis/visualization/viz12_bridge_ego_edges.py
```

## interviews/

| File | Participant | Date | Size |
|------|-------------|------|------|
| 01-np-transcript.txt | NP (CCNY) | Apr 2025 | 41 KB |
| 02-hi-transcript.txt | HI | Apr 2025 | 54 KB |
| 03-ej-transcript.txt | EJ | Jul 2025 | 61 KB |
| 04-rf-transcript.txt | RF | Oct 2025 | 76 KB |
| interview-01-NP-full.pdf | NP (CCNY) | — | 96 KB (PDF formatted) |
| interview-01-NP-audio.srt | NP (CCNY) | — | 46 KB (timestamped audio transcript) |
| BARUCH_INTERVIEW_QUESTIONS.md | — | — | Semi-structured protocol, 45-55 min sessions |

## Theoretical Framework

- **Ostrom** — bridge users as boundary spanners enabling polycentric governance
- **Granovetter** — cross-community edges as weak ties with disproportionate structural impact
- **Warner** — high clustering enables reflexive circulation of knowledge

## Bridge User Categories

1. Institutional navigators — CUNY bureaucracy across campuses
2. Transfer advisors — inter-campus transfer guidance
3. Financial aid specialists — aid, tuition, payment systems
4. Academic mentors — cross-school course/professor recommendations
5. Social connectors — interpersonal bridges between communities
6. Crisis responders — mobilization during March 2020 transition
7. Information brokers — redistributing official comms in accessible language

## Provenance

All files copied from originals within `reddit-diss/`. Sources: `00_ACTIVE/chapter_drafts/`, `00_ACTIVE/dissertation/findings/`, `00_ACTIVE/visualizations/{05,12}_*`, `scripts/analysis/visualization/`, `00_ACTIVE/transcripts.zip`, `archive/deprecated-directories/`. Assembled 2026-02-02.
