# Dataset Inventory
_Updated: 2026-03-21 17:10 ET_

## Active Superset (use this for training)

| File | Rows | Notes |
|------|------|-------|
| `toefl_superset9_merged_20260321.jsonl` | 45,555 | **Canonical superset as of 2026-03-21.** Superset8 + batch_20260321, deduped. 0 parse errors. |
| `toefl_superset8_merged_20260320.jsonl` | 46,943 | Superseded by superset9. 0 parse errors. |
| `toefl_superset7_merged_20260317.jsonl` | 39,133 | Superseded by superset8. 0 parse errors. |
| `toefl_batch_20260321.jsonl` | 10,000 | **New batch (2026-03-21).** Off-day generation. 10 new error categories: stative verb progressive (AA), countable/uncountable (AB), verb complementation (AC), quantifier errors (AD), definite article overuse (AE), reflexive pronoun misuse (AF), negative inversion (AG), discourse connector errors (AH), causative verb errors (AI), possession construction (AJ). Plus expanded academic sub-patterns across SV agreement, tense, present perfect, articles, prepositions, word order, conditionals, reported speech, question formation, purpose infinitives, was/were, since+duration, gerund/inf. 0 parse errors. Deduped against superset8 (11,388 dupes removed from 56,943 raw). |
| `toefl_batch_20260319.jsonl` | 10,000 | Off-day generation 2026-03-19. 26 error categories. Merged into superset8. |

## Superset9 (completed 2026-03-21)

| Action | Status |
|--------|--------|
| Merge superset8 + toefl_batch_20260321 → `toefl_superset9_merged_20260321.jsonl` | **Done** |
| Rows (post-dedup) | 45,555 (11,388 dupes removed from 56,943 raw) |
| Parse errors | 0 |

## Superset8 (completed 2026-03-20)

| Action | Status |
|--------|--------|
| Merge superset7 + toefl_batch_20260319 → `toefl_superset8_merged_20260320.jsonl` | **Done** |
| Rows (post-dedup) | 46,943 (2,190 dupes removed from 49,133 raw) |
| Parse errors | 0 |

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
| `toefl_superset4_merged_20260311.jsonl` | 17,549 | 0 | Subsumed by superset5 |
| `toefl_superset3_merged_20260227_0701.jsonl` | 5,560 | 0 | Subsumed by superset4 |
| `superset3_cleaned.jsonl` | 5,550 | 0 | Subsumed by superset4 (10 degenerate entries stripped) |
| `toefl_gptoss20b_10k.jsonl` | 11,999 | 0 | Subsumed by superset4 |
| `toefl_kimik2_10k.jsonl` | 1,503 | 0 | Subsumed by superset5 |
| `toefl_ollama_qwen8b_batch_20260313.jsonl` | 81 | 0 | Subsumed by superset5 |
| `toefl_batch_20260315.jsonl` | 10,000 | 0 | Merged into superset6 |
| `toefl_batch_20260317.jsonl` | 10,000 | 0 | New — pending merge into superset7 |

## In-Progress Generation

| File | Rows (live) | Model | Status |
|------|-------------|-------|--------|
| `toefl_batch_20260319.jsonl` | 10,000 | programmatic (Python) | **Complete — awaiting superset8 merge** |

## Prior In-Progress (now complete)

| File | Rows (live) | Model | Status |
|------|-------------|-------|--------|
| `toefl_batch_20260317.jsonl` | 10,000 | programmatic (Python) | **Complete — merged into superset7** |
| `toefl_batch_20260315.jsonl` | 10,000 | programmatic (Python) | **Complete — merged into superset6** |

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
