# Microlearning Sidequest (POC)

This folder is a proof-of-concept scaffold for a fully automated microlearning content pipeline:

**Reddit ingest → topic ranking → human approval → content packet → (video) → publish**

The goal is to standardize the *handoff contracts* between components so Petrarch (scraper) and Quimbot (ranker/generator) can interoperate cleanly.

## Directory layout

- `schemas/` — canonical JSON Schemas for pipeline artifacts
- `examples/` — example JSON/JSONL records
- `notes/` — implementation notes / scoring heuristics
- `docs/` — comprehensive pipeline design documentation
  - `AUTOMATION_BEST_PRACTICES.md` — Complete architecture, quality gates, success metrics
  - `REDDIT_TO_VEO_PIPELINE.md` — Trend discovery → visual storytelling methodology
  - `CANDIDATE_TOPICS.md` — 10 validated topics with Veo prompts and scripts

## Artifacts

1. **Topic record** (`topic_record`)
   - One record per candidate topic (typically 1 Reddit post).
   - Produced by the ingest + enrich steps.

2. **Shortlist record** (`shortlist_record`)
   - A ranked list of topics for a given day/run.

3. **Approval record** (`approval_record`)
   - Captures the human gate decision.

4. **Content packet** (`content_packet`)
   - The script + metadata used by video generation and publishing.

## File formats

- Prefer **JSONL** for large collections (e.g., ingest output).
- Prefer **JSON** for single documents (shortlist, content packet).
