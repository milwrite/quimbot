# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

Portable dissertation writing workspace for PhD research on Reddit discourse across CUNY communities during the COVID-19 transition (2010-2025).

This is the writing bundle — no scripts, no venv, no scraping infrastructure. The full research repo lives elsewhere. `_meta/CLAUDE.md` documents the complete project architecture (databases, scripts, analysis pipelines, tools) — consult it when you need context about anything outside this bundle.

---

## Working Mode

Keep each pass small. Finish one discrete task, record the result, then stop.

Start with `_meta/TODO.md`. The **DISS-BUNDLE-NN** items (numbered sequentially) define bundle-safe maintenance work: file cleanup, indexes, source maps, document crosswalks, and formatting-only passes. Complete one per pass, then update the checklist.

When working here:

- complete exactly one atomic task per pass
- update `_meta/TODO.md` when the task is done
- if a task depends on missing databases, scripts, or external context, write the blocker down and stop
- prefer edits that improve orientation, consistency, and traceability over broad prose rewrites

### Multi-Agent Ownership

Two agents operate in this bundle — **Quimbot** and **Petrarch**. Task ownership in `_meta/TODO.md` governs who works what:

- `Owner: Quimbot` — reserved for Quimbot; Petrarch does not touch these
- `Owner: Open` — available for Petrarch to claim by editing the line to `Owner: Petrarch`
- once a task is marked `Owner: Petrarch`, Quimbot leaves it alone unless explicitly asked

### Bundle-Safe Contributions

Good tasks in this repo:

- removing confirmed duplicate files
- creating inventories, indexes, and file maps
- mapping markdown files to generated `.docx` outputs
- building chapter source maps and evidence allocation scaffolds
- light formatting cleanup on existing notes and progress documents
- clarifying which files are canonical and which are exports or derived artifacts

### Bundle Limits

This repo cannot support full-pipeline work. Do not treat it like the main research environment.

Avoid or defer unless the required materials are present:

- database validation against live SQLite files
- rerunning analysis scripts or scrapers
- regenerating findings from missing code or data
- heavy revision of generated findings without checking provenance
- direct edits to `writing/CURRENT.docx` unless explicitly requested

---

## Four-Domain Structure

The bundle is organized into four domains plus a metadata directory:

| Domain | Path | Contains |
|--------|------|----------|
| **Writing** | `writing/` | Your prose — drafts, chapters, proposals, advisement, addendum |
| **Research** | `research/` | Other people's words — bibliographies, lit reviews, reading lists |
| **Evidence** | `evidence/` | The data speaking — findings, narratives, interviews, database exports, text analysis, network validation |
| **Visualizations** | `visualizations/` | The data shown — 13 numbered suites (Viz 01-13) with PDF/PNG/SVG/HTML |
| **Meta** | `_meta/` | Reference docs — TODO, DOCS chronicle, dashboard plan, OUTPUT_CATALOG, Drive manifest |

---

## Key Files

| File | Purpose |
|------|---------|
| `writing/CURRENT.docx` | **Canonical dissertation draft** — do not edit unless explicitly requested |
| `writing/proposal.md` | Dissertation proposal |
| `writing/drafts.md` | Draft tracking across all chapters |
| `research/bibliography/refannbib.json` | Master bibliography (structured JSON) |
| `research/bibliography/reviews_refannbib.md` | Annotated bibliography (readable markdown) |
| `_meta/TODO.md` | Task list, DISS-BUNDLE items, evidence protocols |
| `_meta/DOCS.md` | Month-by-month document generation chronicle |
| `_meta/CLAUDE.md` | Full research repo architecture (databases, scripts, tools) |
| `_meta/OUTPUT_CATALOG.json` | Index of pre-aggregated chapter evidence |

---

## Database Context

The SQLite databases (300 MB, 12 subreddits, 574K+ posts) live in the main repo at `data/databases/current/`, not here. But this bundle contains **exported database artifacts** and evidence that reference the database schema:

- `evidence/databases/CUNY_DATABASE_REPORT_2026-02-08.md` — corpus composition, integrity scores, temporal distribution
- `evidence/databases/baseline_participation/` — participation typology data and visualizations
- `evidence/databases/*.xlsx`, `*.csv` — exported data tables (subreddit posts, CUNY contributors)

### Schema (all databases share this)

Evidence IDs map to these tables:

- `submissions` — Reddit posts (id, title, selftext, score, created_utc, author, subreddit)
- `comments` — Reddit comments (id, body, score, created_utc, author, parent_id)
- `users` — User accounts and processing status

Format: `submission_XXXXX` or `comment_XXXXX` (the XXXXX is the Reddit post/comment ID from the `id` column). All dissertation claims are grounded in these evidence IDs.

### Corpus Summary

- **8 CUNY subreddits** (core): 60K submissions, 245K comments, ~22K authors, 94-100% integrity
- **4 comparative** (NYU, Columbia, Fordham, St. John's): 57K submissions, 254K comments, 57-74% integrity
- **COVID-19 signal**: 3-5x activity spike during March 2020 emergency remote transition

---

## Evidence Structure

```
evidence/
├── findings/
│   ├── bridge_users/              bridge user discourse (md, docx, pdf, json)
│   ├── transfer_barriers/         CUNY transfer barriers + enrollment data
│   └── baseline_participation/    participation typology data
├── narratives/                    student voice evidence documents
├── databases/                     exported db reports, data tables, participation analysis
├── interviews/                    4 transcripts + protocol + candidate list + audio
├── text_analysis_ch1/             Ch1 text analysis outputs (JSON)
├── text_analysis_ch2/             Ch2 text analysis + user activity data
├── networks_ch1/                  Ch1 network validation
└── networks_ch2/                  Ch2 networks (EXCLUDED.md — 16 GB excluded from bundle)
```

---

## Three-Scale Framework

1. **Macroscopic** (computational): network density, temporal spikes, sentiment
2. **Mesoscopic** (network): community detection, bridge users, influence
3. **Microscopic** (ethnographic): individual posts as evidence, student voices

---

## Visualizations

13 numbered suites in `visualizations/` (01-13). Each contains PDF/PNG/SVG static exports and data JSON. Interactive HTML where applicable.

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

# with dissertation formatting template (TNR, 1" margins, double spacing)
pandoc INPUT.md -o OUTPUT.docx --reference-doc=templates/reference_base.docx
```

---

## Commit Convention

- lowercase, short, no sign-offs
- no "Co-Authored-By: Claude" signatures
- descriptive but concise (max 100 chars)

---

## What's Not Here

- SQLite databases (300 MB) — live in main repo at `data/databases/current/`
- Network graph data (16 GB) — raw .gexf, .graphml, .json
- Python scripts and venv — analysis infrastructure
- Jekyll site — `tools/jekyll-site/` (753 evidence pages)
- Query results — `data/output/queries/`

For database queries, analysis pipelines, or scraping: use the main research repo. See `_meta/CLAUDE.md` for commands and architecture.
