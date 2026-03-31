# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

---

## Python Environment

The project uses a virtual environment with Python 3.9:

```bash
# Use the project venv for scripts requiring pandas/numpy
venv/bin/python3 scripts/analysis/...

# Required packages: pandas, numpy, networkx, plotly, matplotlib
# TUI tool: textual (for tools/tui-query/)
# Fine-tuning: unsloth, transformers (GPU-only, see tools/finetuning/)
```

---

## Project Overview

PhD dissertation research system analyzing Reddit discourse across CUNY university communities during the COVID-19 transition (2010-2025). Combines user-centric web scraping, network analysis, temporal analysis, and evidence synthesis.

---

## Directory Structure

```
reddit-diss/
├── 00_ACTIVE/ ..................... Current work
│   ├── core_docs/ ................ Primary research documents
│   │   ├── CURRENT.docx ......... Main dissertation document
│   │   ├── compendium/ .......... Per-chapter evidence aggregation
│   │   ├── chapters/ ............ Chapter outlines & drafts
│   │   ├── evidence/ ............ Evidence allocation tracking
│   │   └── refannbib.md ......... Annotated bibliography
│   ├── dissertation/findings/ .... Generated findings documents (md + docx)
│   ├── chapter_drafts/ ........... Proposal-aligned chapter outlines
│   ├── lit_reviews/ .............. Literature reviews (4 files)
│   ├── interviews/ ............... 4 interview transcripts + protocol
│   ├── visualizations/ ........... Numbered viz suites (Viz 1-13)
│   ├── DRAFTS.md ................. Draft tracking
│   └── quotes.md ................. Collected quotes
│
├── data/
│   ├── databases/current/ ........ 10 SQLite databases (primary location)
│   └── output/ ................... Analysis results
│       ├── 05_reports/
│       ├── corpus/
│       ├── queries/
│       └── visualizations/
│
├── scripts/
│   ├── collection/ ............... Reddit scrapers
│   ├── analysis/
│   │   ├── network/ ............. Network reconstruction (5 scripts)
│   │   ├── temporal/ ............ Temporal analysis (6 scripts)
│   │   ├── text/ ................ NLP/content analysis (6 scripts)
│   │   ├── synthesis/ ........... Compendium & orchestration (8 scripts)
│   │   └── visualization/ ....... Chart generation (viz1-viz13 scripts)
│   ├── scraping/ ................. Scraping framework (analysis, core, tools)
│   └── utilities/ ................ Helpers (db_safety.py, extract_pdf_text.py)
│
├── tools/
│   ├── tui-query/ ................ Terminal UI for database querying
│   ├── finetuning/ ............... Unsloth CPT pipeline (Qwen 2.5 14B)
│   ├── docx/ ..................... DOCX templates and post-processing
│   ├── semantic-search/ .......... Embedding-based search (Gradio + CLI)
│   ├── interactive-website/ ...... Flask research dashboard
│   ├── jekyll-site/ .............. Dissertation website (GitHub Pages)
│   └── research-dashboard/ ....... Streamlit dashboard (legacy)
│
├── bin/ ........................... Shell scripts (scraping, querying, export)
├── docs/ .......................... Documentation & guides
├── archive/ ....................... Historical/deprecated materials
├── config/ ........................ Credentials & config
├── DOCS.md ....................... Monthly document generation chronicle
└── *.db ........................... 5 databases at project root (legacy copies)
```

---

## Databases

### Primary Location: `data/databases/current/`

| Database | Size | Content |
|----------|------|---------|
| Baruch_historical_data.db | 145 MB | Largest single school |
| CUNY_historical_data.db | 92 MB | Main hub subreddit |
| QueensCollege_historical_data.db | 20 MB | |
| HunterCollege_historical_data.db | 16 MB | |
| Fordham_historical_data.db | 13 MB | Comparative |
| CCNY_historical_data.db | 6.2 MB | |
| BrooklynCollege_historical_data.db | 1.1 MB | |
| STJOHNS_historical_data.db | 1.0 MB | Comparative |
| CUNYuncensored_historical_data.db | 264 KB | Splinter community |
| JohnJay_historical_data.db | 184 KB | |

NYU and Columbia databases exist but are empty (0 bytes).

5 databases also exist at the project root (Baruch, CCNY, CUNY, Hunter, Queens) — these are legacy copies from before the reorganization. The canonical versions are in `data/databases/current/`.

### Schema (all databases share this)

- `submissions` — Reddit posts (id, title, selftext, score, created_utc, author, subreddit)
- `comments` — Reddit comments (id, body, score, created_utc, author, parent_id)
- `users` — User accounts and processing status (pending/completed/failed)
- `user_activity` — Activity summaries
- `subreddit_info` — Metadata

### SQL Conventions

Use `<>` instead of `!=` in sqlite3 shell commands (shell escapes `!`):
```sql
WHERE author <> '[deleted]' AND author <> 'AutoModerator'
```

---

## Core Commands

### Database Queries

```bash
# Overview and statistics
./bin/query-overview                    # All subreddits
./bin/query-overview Baruch             # Single subreddit

# Direct SQL
sqlite3 data/databases/current/CUNY_historical_data.db "SELECT COUNT(*) FROM comments;"

# Content search
python3 scripts/analysis/text/query_content.py "keyword" --subreddit CUNY

# TUI interactive query tool
venv/bin/python3 tools/tui-query/tui_query.py
```

### Data Collection

```bash
# Full scrape (48-72 hours for all CUNY)
./bin/run_all_cuny_scrapers.sh

# Daily updates (pending users only)
./bin/update_cuny_scrapers.sh

# Single subreddit
python3 scripts/collection/universal_reddit_scraper.py -s CUNY
```

### Analysis Pipeline

```bash
# Full pipeline (network + temporal + text)
python3 scripts/analysis/synthesis/run_comprehensive_analysis.py --all-subreddits

# Individual analyses
python3 scripts/analysis/network/reconstruct_discussion_network.py --subreddit CUNY
python3 scripts/analysis/temporal/generate_temporal_analysis_report.py
python3 scripts/analysis/text/comprehensive_text_analysis.py

# Research compendia (aggregates evidence for dissertation writing)
python3 scripts/analysis/synthesis/compendium_synthesizer.py synthesize --chapter 1
python3 scripts/analysis/synthesis/compendium_synthesizer.py sync  # Validate citations
```

### Document Generation

```bash
# Convert findings to DOCX
pandoc INPUT.md -o OUTPUT.docx --from markdown --to docx

# With reference template for consistent formatting
pandoc INPUT.md -o OUTPUT.docx --reference-doc=tools/docx/reference.docx

# Post-process DOCX (fix styles, headers)
python3 tools/docx/postprocess_docx.py OUTPUT.docx

# Findings output location
00_ACTIVE/dissertation/findings/
```

### Fine-Tuning Pipeline

```bash
# Chunk literature corpus into training examples
python3 tools/finetuning/chunk_cpt_by_paragraph.py

# Validate dataset format
python3 tools/finetuning/validate_dataset.py data/output/literature_unsloth_cpt_chunked.jsonl

# Train (requires NVIDIA GPU — Colab or Legion 7)
python3 tools/finetuning/train_cpt.py --dry-run  # Validate config first
python3 tools/finetuning/train_cpt.py             # Actual training
```

---

## Architecture

### User-Centric Scraping

Bypasses Reddit's 1000-item API limit by discovering users from subreddit posts, then fetching each user's complete history. Enables cross-community tracking. Comment-to-submission linkage via `t3_` prefix recovery.

### Evidence ID System

Format: `submission_XXXXX` or `comment_XXXXX` (Reddit post/comment ID). Used throughout dissertation writing to ground claims in actual data. The compendium synthesizer validates all cited IDs exist in databases.

### Compendium Synthesis

`scripts/analysis/synthesis/compendium_synthesizer.py` aggregates all analysis outputs into per-chapter evidence collections with relevance scoring. This lets the researcher write without manually querying databases — all evidence is pre-aggregated in `00_ACTIVE/core_docs/compendium/`.

### Three-Scale Framework

1. **Macroscopic** (computational): Network density, temporal spikes, sentiment
2. **Mesoscopic** (network): Community detection, bridge users, influence
3. **Microscopic** (ethnographic): Individual posts as evidence, student voices

### Findings Generator Skill

The `/findings-generator` skill (`.claude/skills/findings-generator.md`) documents two replicable analysis methodologies:
- **Mode A (Content-Based)**: Filter posts by topic keywords + population linguistic markers
- **Mode B (Actor-Based)**: Identify users by structural position, classify behavioral archetypes

### Database Safety Module

**CRITICAL**: All scripts that write to SQLite databases MUST use `scripts/utilities/db_safety.py`. This module was created after B-tree index corruption caused by interrupted write operations during comment recovery.

```python
# Import pattern (from scripts/collection/ or scripts/analysis/)
sys.path.insert(0, str(Path(__file__).parent.parent))
from utilities import db_safety

# REQUIRED: Use safe_connection() instead of sqlite3.connect()
with db_safety.safe_connection(db_path) as conn:
    cursor = conn.cursor()
    # ... operations ...

# For writes: Use explicit transactions with rollback
conn.execute("BEGIN IMMEDIATE")
try:
    # ... INSERT/UPDATE/DELETE ...
    conn.execute("COMMIT")
except Exception:
    conn.execute("ROLLBACK")
    raise

# For long-running recovery operations: Periodic integrity checks
if records_processed % 50 == 0:
    if not db_safety.quick_integrity_check(conn):
        save_checkpoint()
        raise sqlite3.IntegrityError("Corruption detected")
```

Key functions:

- `get_safe_connection()` / `safe_connection()`: Apply corruption-resistant PRAGMAs (WAL, synchronous=NORMAL, busy_timeout=30000)
- `create_backup()`: Timestamped backup before dangerous operations
- `quick_integrity_check()`: Fast check during long operations
- `full_integrity_check()`: Thorough check before/after migrations
- `safe_batch_insert()`: Atomic batch with auto-rollback

Scripts already hardened: `recover_missing_comments.py`, `recover_missing_submissions.py`, `universal_reddit_scraper.py`, `fast_reddit_scraper.py`, `optimized_reddit_scraper.py`, `diagnose_and_repair.py`, `migrate_databases.py`, `audit_subreddit_databases.py`

---

## Visualization System

13 numbered interactive visualization suites live in `00_ACTIVE/visualizations/`. Each subdirectory follows the pattern `NN_descriptive_name/` and contains HTML (Plotly), summary markdown, and sometimes PDF/PNG/JSON exports.

| Viz | Topic | Chapter |
|-----|-------|---------|
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

Visualization scripts live in `scripts/analysis/visualization/` (named `viz1_*.py` through `viz13_*.py`).

### Naming Convention

Files within each viz directory follow: `vizN_descriptive_name.{html,pdf,png,json,md}`

The summary markdown (e.g., `viz7_user_participation_summary.md`) documents key findings and is referenced in chapter drafts.

---

## Tools

| Tool | Location | Purpose |
|------|----------|---------|
| TUI Query | `tools/tui-query/` | Interactive terminal UI for multi-database querying with filtering, sorting, and CSV/JSON export |
| Fine-Tuning | `tools/finetuning/` | Unsloth continued pretraining pipeline for Qwen 2.5 14B on dissertation literature corpus |
| DOCX | `tools/docx/` | Reference templates (`reference.docx`) and `postprocess_docx.py` for pandoc output |
| Semantic Search | `tools/semantic-search/` | Gradio and CLI interfaces for embedding-based search across databases |
| Interactive Website | `tools/interactive-website/` | Flask server (`enhanced_server.py`) with API endpoints for research dashboard |
| Jekyll Site | `tools/jekyll-site/` | GitHub Pages dissertation site at zmuhls.github.io/dissertation |
| Research Dashboard | `tools/research-dashboard/` | Streamlit dashboard (legacy, superseded by interactive-website) |

---

## Commit Convention

- Lowercase, short, no sign-offs
- Multi-line with heredoc for complex changes:

```bash
git commit -m "$(cat <<'EOF'
add network density validation for march 2020 spike

- reconstructed interaction network (153k edges, density 0.34)
- validated 3x baseline spike during pandemic transition
EOF
)"
```

---

## Key Patterns

### Running Commands

All commands run from project root. Scripts use relative paths for databases and credentials.

### Querying for Evidence

```sql
-- High-score posts about a topic
SELECT 'submission_' || id as evidence_id, title, score,
       strftime('%Y-%m', datetime(created_utc, 'unixepoch')) as date
FROM submissions
WHERE (title LIKE '%transfer%' OR selftext LIKE '%transfer%')
ORDER BY score DESC LIMIT 20;

-- Cross-database user identification
SELECT author, COUNT(*) as n FROM comments
WHERE author <> '[deleted]'
GROUP BY author HAVING n >= 5
ORDER BY n DESC;
```

### Findings Documents

Generated findings go to `00_ACTIVE/dissertation/findings/` as both `.md` and `.docx`. Naming: `CUNY_[TOPIC]_FINDINGS.{md,docx}`.

### Document History

`DOCS.md` in the project root contains a month-by-month chronicle of all generated documents, reports, and visualizations dating back to August 2025.

---

## Skills (`.claude/skills/`)

| Skill | Purpose |
|-------|---------|
| findings-generator | Mode A (content) and Mode B (actor) analysis workflows |
| evidence-query | Database querying patterns |
| compendium-synthesizer | Multi-source evidence aggregation |
| research-writer | Academic prose from evidence |
| chapter-builder | Chapter drafting |
| output-data-curator | Catalog and select analysis outputs |

---

## Troubleshooting

- **"Database locked"**: `ps aux | grep python3` → `kill -9 [PID]`
- **Shell escapes `!=`**: Use `<>` for SQL inequality
- **Path errors in scripts**: Some scripts have hardcoded old paths. Canonical DB location is `data/databases/current/`
- **Empty NYU/Columbia databases**: These haven't been populated yet
- **"Database disk image is malformed"**: B-tree index corruption from interrupted writes. Restore from `.backup_*.db` file, then use hardened scripts with `db_safety` module. Never `kill -9` a running scraper—use Ctrl+C to allow checkpoint save
- **Git history before Oct 2025**: Corrupted object `8b19956...` prevents traversal; file timestamps are the authority for pre-October dates
