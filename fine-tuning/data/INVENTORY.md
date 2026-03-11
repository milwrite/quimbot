# Dataset Inventory
_Updated: 2026-03-11 09:01 ET_

## Active Superset (use this for training)

| File | Rows | Notes |
|------|------|-------|
| `toefl_superset4_merged_20260311.jsonl` | 17,549 | **Current canonical superset.** Merged from superset3_cleaned (5,550) + toefl_gptoss20b_10k (11,999). 0 parse errors, deduplicated by exact JSON key. |

## Source Files

| File | Raw Rows | JSON errors | Status |
|------|----------|-------------|--------|
| `combined_toefl_superset2_clean_dedup_20260219.jsonl` | 9,227 | 0 | Subsumed by superset3 |
| `toefl_superset2_merged_20260223.jsonl` | 14,566 | 0 | Subsumed by superset3 |
| `toefl_synth_10k_20260222_1120.jsonl` | 10,000 | 0 | Subsumed by superset3 |
| `toefl_ollama_10k.jsonl` | 120 | 0 | Subsumed by superset3 (+40 unique) |
| `toefl_ollama_batch_20260224_2130_clean.jsonl` | 21 | 0 | Subsumed by superset3 (+1 unique) |
| `toefl_ollama_gemma27b_10k.jsonl` | 1 | 0 | Subsumed by superset3 (+0 unique) |
| `toefl_ollama_batch_20260224_2130.jsonl` | 51 | 0 | Raw (unclean version of _clean above) |
| `toefl_superset3_merged_20260227_0701.jsonl` | 5,560 | 0 | Subsumed by superset4 (original) |
| `superset3_cleaned.jsonl` | 5,550 | 0 | Subsumed by superset4 (10 degenerate entries stripped) |
| `toefl_gptoss20b_10k.jsonl` | 11,999 | 0 | Subsumed by superset4 |

## In-Progress Generation

| File | Rows (live) | Model | Status |
|------|-------------|-------|--------|
| _(none active — OpenRouter 402 blocking cloud gen; ollama gen paused)_ | — | — | Blocked |

## Misc / Scaffolding

| File | Rows | Notes |
|------|------|-------|
| `scaffolding_1000.jsonl` | 29 | Small scaffolding set |
| `proof_of_concept_10.jsonl` | 10 | Minimal POC |
| `test_scaffolding.jsonl` | 2 | Test set |
| `scaffolding_kimi_k2.5_50.jsonl` | 0 | Empty placeholder |

## QA Flags (2026-03-04)

| File | Lines | Notes |
|------|-------|-------|
| `superset3_flagged_short_lines.txt` | 10 line indices | Degenerate/short replies flagged for review |

## Dedup Summary (2026-02-27)

- **Raw lines across all source files:** ~34,941
- **Intra-baseline duplicates found:** 28,274
- **Unique entries in superset3:** 5,560
- **Dedup key:** MD5 of first user message (lowercased, stripped)
- **New Ollama entries added:** 41 (out of 142 candidate lines)

## Notes

- Superset3 is the canonical training-ready file. All new generation output (`toefl_gptoss20b_10k.jsonl`) should be folded in once generation completes via another merge+dedup pass.
- `toefl_ollama_batch_20260224_2130.jsonl` (raw) is superseded by the `_clean` version; both subsumed by superset3.
