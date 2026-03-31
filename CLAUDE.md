# CLAUDE.md

Portable dissertation writing workspace for PhD research on Reddit discourse across CUNY communities during the COVID-19 transition (2010-2025).

This is the writing bundle — no scripts, no venv, no scraping infrastructure. The full research repo lives elsewhere. See `reference/CLAUDE.md` for the complete project architecture.

---

## Structure

```
diss/
├── core_docs/
│   ├── CURRENT.docx              main dissertation document
│   ├── refannbib.json            master bibliography (3.7 MB)
│   ├── chapters/                 chapter organization
│   ├── compendium/               per-chapter evidence aggregation
│   │   ├── chapter_1/
│   │   ├── chapter_2/            text analysis, bibliography
│   │   └── chapter_3/
│   ├── proposal.md               dissertation proposal
│   └── progress_reports.md       monthly progress
│
├── chapter_drafts/
│   ├── outlines.docx             proposal-aligned outlines
│   ├── chapter-1-iteration-a1.md chapter 1 draft
│   ├── chapter_3_bridge_users_rewritten.docx
│   └── bridge-users/             ch3 drafts + lit review
│
├── dissertation/
│   ├── findings/                 generated analysis findings
│   │   ├── bridge_users/         md, docx, pdf, json
│   │   ├── transfer_barriers/
│   │   └── baseline_participation/
│   ├── narratives/               student voice evidence docs
│   └── databases/data/           database report
│
├── visualizations/               13 numbered interactive viz suites (01-13)
├── interviews/                   4 transcripts + protocol
├── reviews/refannbib.md          annotated bibliography
├── addendum/                     methodological AI scaffold addendum
├── reference/                    DOCS.md, TODO.md, CLAUDE.md, proposals/
│
├── drafts.md                     draft tracking
├── quotes.md                     collected quotes
└── vp_post_ai_detection.md
```

---

## Key Files

| File | Purpose |
|------|---------|
| `core_docs/CURRENT.docx` | Main dissertation document — the canonical draft |
| `core_docs/refannbib.json` | Master bibliography (structured JSON) |
| `reviews/refannbib.md` | Annotated bibliography (readable markdown) |
| `core_docs/proposal.md` | Dissertation proposal |
| `reference/TODO.md` | Research priorities and evidence protocols |
| `reference/DOCS.md` | Month-by-month document generation chronicle |

---

## Evidence ID System

Format: `submission_XXXXX` or `comment_XXXXX` (Reddit post/comment IDs). All dissertation claims are grounded in these evidence IDs. The compendium files in `core_docs/compendium/` contain pre-aggregated evidence per chapter.

---

## Three-Scale Framework

1. **Macroscopic** (computational): network density, temporal spikes, sentiment
2. **Mesoscopic** (network): community detection, bridge users, influence
3. **Microscopic** (ethnographic): individual posts as evidence, student voices

---

## Visualizations

13 numbered suites in `visualizations/` (01-13). Each contains interactive HTML (Plotly), summary markdown, and exports.

| Viz | Topic | Ch |
|-----|-------|----|
| 01 | March 2020 pandemic timeline | 2 |
| 02 | Crisis topic intensification | 2 |
| 03 | Federated vs centralized architecture | 2 |
| 04 | Network density comparison | 2 |
| 05 | Bridge users edgewise clustering | 3 |
| 06 | Late-night support infrastructure | 2 |
| 07 | User participation inequality | 2 |
| 08 | Subreddit territory edge map | 2 |
| 09 | Edge flow chord diagram | 2 |
| 10 | Temporal edge genesis | 2 |
| 11 | Edge weight distributions | 2 |
| 12 | Bridge user connections (ego networks) | 3 |
| 13 | Participation typology | 2 |

---

## Document Generation

```bash
# markdown to docx
pandoc INPUT.md -o OUTPUT.docx

# with dissertation formatting template
pandoc INPUT.md -o OUTPUT.docx --reference-doc=templates/reference_base.docx
```

Findings output: `dissertation/findings/` as both `.md` and `.docx`.

---

## Commit Convention

- lowercase, short, no sign-offs

---

## What's Not Here

- SQLite databases (300 MB) — live in main repo at `data/databases/current/`
- Network graph data (16 GB) — raw .gexf, .graphml, .json
- Python scripts and venv — analysis infrastructure
- Jekyll site — `tools/jekyll-site/` (753 evidence pages)
- Query results — `data/output/queries/`

For database queries, analysis pipelines, or scraping: use the main research repo.
