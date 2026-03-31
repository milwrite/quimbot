# DOCS.md

Document and report generation chronicle for the CUNY Reddit dissertation research project. Organized by month, from earliest to most recent.

---

## July 2025

### Compendium Infrastructure

- `core_docs/compendium/chapter_2/assets/text_analysis/user_activity.csv` — user activity data extracted for Chapter 2 text analysis
- `core_docs/compendium/chapter_1/assets/networks/validation_report.json` — network validation for Chapter 1
- `core_docs/compendium/chapter_2/assets/networks/validation_report.json` — network validation for Chapter 2

### Interviews

- `00_ACTIVE/interviews/03-ej-transcript.txt` — third interview transcript (participant EJ)

> First evidence of compendium asset pipeline producing structured JSON outputs for chapter-level evidence integration.

---

## August 2025

### Temporal Analysis Visualizations (archived)

Generated the first wave of per-subreddit temporal analysis dashboards:

- `output/04_temporal_analysis/Baruch_temporal_analysis.html`
- `output/04_temporal_analysis/CUNY_temporal_analysis.html`
- `output/04_temporal_analysis/HunterCollege_temporal_analysis.html`
- `output/04_temporal_analysis/JohnJay_temporal_analysis.html`
- `output/04_temporal_analysis/QueensCollege_temporal_analysis.html`
- `output/04_temporal_analysis/CUNY_activity_bursts.html`
- `output/04_temporal_analysis/CUNY_cohort_analysis.html`
- `output/04_temporal_analysis/CUNY_topic_lifecycles.html`
- `output/04_temporal_analysis/may_2020_finals_graduation.html`
- `output/04_temporal_analysis/pandemic_impact_summary_table.html`
- `output/04_temporal_analysis/visualizations/comprehensive_dashboard.html`
- `output/04_temporal_analysis/visualizations/activity_timeline.html`
- `output/04_temporal_analysis/visualizations/activity_heatmap.html`
- `output/04_temporal_analysis/visualizations/event_detection.html`
- `output/04_temporal_analysis/visualizations/user_retention.html`
- `output/04_temporal_analysis/visualizations/seasonal_patterns.html`
- `output/04_temporal_analysis/visualizations/growth_curves.html`
- `output/04_temporal_analysis/visualizations/comparative_timeline.html`

### Text Analysis Outputs (archived)

- `output/03_text_analysis/index.html` — text analysis index page
- `output/03_text_analysis/frequency/temporal_analysis.html`
- `output/03_text_analysis/frequency/pandemic_transition_dashboard.html`

### Network Reconstruction — First Wave

Generated initial network graph files for CUNY interaction, coparticipation, topic bipartite, and topic projected networks in GraphML, GEXF, and JSON formats. Multiple runs produced timestamped outputs:

- `core_docs/compendium/chapter_2/assets/networks/CUNY_interaction_20250827_*.{graphml,gexf,json}`
- `core_docs/compendium/chapter_2/assets/networks/CUNY_coparticipation_20250827_*.{graphml,gexf,json}`
- `core_docs/compendium/chapter_2/assets/networks/CUNY_topic_bipartite_20250827_*.{graphml,gexf,json}`
- `core_docs/compendium/chapter_2/assets/networks/CUNY_topic_projected_20250827_*.{graphml,gexf,json}`
- `core_docs/compendium/chapter_2/assets/networks/CUNY_interaction_gephi_20250827_*.gexf` — Gephi-optimized exports

### Network Reconstruction — Second Wave (Aug 31)

Refined network generation with updated parameters:

- `core_docs/compendium/chapter_2/assets/networks/CUNY_interaction_20250831_*.{graphml,gexf,json}`
- `core_docs/compendium/chapter_2/assets/networks/CUNY_coparticipation_20250831_*.{graphml,gexf,json}`
- `core_docs/compendium/chapter_2/assets/networks/CUNY_topic_bipartite_20250831_*.{graphml,gexf,json}`
- `core_docs/compendium/chapter_2/assets/networks/CUNY_topic_projected_20250831_*.{graphml,gexf,json}`

### Compendium Text Analysis Assets

- `core_docs/compendium/chapter_1/assets/text_analysis/text_analysis_20250825_160252.json`
- `core_docs/compendium/chapter_1/assets/text_analysis/coverage_report_20250825_160252.json`
- `core_docs/compendium/chapter_1/assets/text_analysis/coverage_report.json`
- `core_docs/compendium/chapter_2/assets/text_analysis/pandemic_data.json`

### Compendium Network Analytics

- `core_docs/compendium/chapter_2/assets/networks/centrality_measures.json`
- `core_docs/compendium/chapter_2/assets/networks/nlp_analysis.json`
- `core_docs/compendium/chapter_2/assets/networks/temporal_analysis.json`
- `core_docs/compendium/chapter_2/assets/networks/comprehensive_network_dataset.json`
- `core_docs/compendium/chapter_2/assets/networks/thread_hierarchies.json`
- `core_docs/compendium/chapter_2/assets/networks/user_network.json`
- `core_docs/compendium/chapter_2/assets/networks/user_interaction_network.{graphml,gexf}`
- `core_docs/compendium/chapter_2/assets/networks/user_thread_bipartite.graphml`
- `core_docs/compendium/chapter_2/assets/networks/thread_network.{graphml,gexf}`
- `core_docs/compendium/chapter_2/assets/networks/subreddit_network.graphml`

### Corpus Generation

- `output/corpus/combined/general_text_corpus.jsonl` — full text corpus for NLP
- `output/corpus/combined/all_submissions.jsonl` — all submission text
- `output/corpus/combined/all_comments.jsonl` — all comment text

### Research Process Documentation

- `core_docs/process/research_process_narrative.md` — narrative account of research process
- `core_docs/process/research_process.md` — structured research log

> August 2025 was the foundational month: temporal analysis dashboards, network reconstruction graphs, text analysis pipelines, and corpus generation all came online. The three-scale analytical framework (macroscopic/mesoscopic/microscopic) was operationalized for the first time.

---

## September 2025

### Reports and Synthesis

- `output/05_reports/dissertation_findings_synthesis.md` — first integrated findings synthesis
- `output/05_reports/dissertation_grounded_synthesis.md` — grounded theory synthesis document
- `output/05_reports/knowledge_graph_analysis_summary.md` — knowledge graph analysis
- `output/05_reports/problem_discourse_analysis_20250912_135818.json` — problem discourse raw data
- `output/05_reports/problem_discourse_comparative_analysis.md` — comparative analysis of problem discourse patterns

### Semantic Search Tool

- `tools/semantic-search/semantic_search_cli.py` — CLI for semantic search across databases
- `tools/semantic-search/create_factual_embeddings_dataset.py` — embedding dataset creation
- `tools/semantic-search/factual_annotation_interface.py` — annotation interface
- `tools/semantic-search/factual_semantic_search.py` — factual search implementation

### Search and Collection Outputs

- `output/searches/food_pantry_test.md` — test search for food pantry discourse
- `output/collections/test_sample_metadata.json` — sample collection metadata

### Compendium Bibliography

- `core_docs/refannbib.json` — annotated bibliography in JSON
- `core_docs/compendium/chapter_1/assets/bibliography/refannbib.json`
- `core_docs/compendium/chapter_2/assets/bibliography/refannbib.json`

### Research Process

- `core_docs/process/master_document.md` — master research coordination document

### Interactive Website Tool

- `tools/interactive-website/enhanced_server.py` — enhanced Flask server for research website

> September marked a shift from data generation to synthesis: the first integrated findings documents emerged, semantic search tools were built, and the problem discourse analysis framework was tested.

---

## October 2025

### Chapter Evidence Reports

Evidence extraction reports generated per chapter section, all under `scripts/ch1/`:

- `ch1/digital_ethnography_evidence_20250109.md`
- `ch1/ethnomethodological_evidence_section_1_3_2.md`
- `ch1/critical_infrastructure_evidence_20251009_175442.md`
- `ch1/critical_infrastructure_evidence_fixed_20251009_175629.md`
- `ch1/boyd_affordances_comprehensive_20251009_175800.md`
- `ch1/section_133_evidence_summary_20251009.md`
- `ch1/section_1_3_4_platform_studies_evidence.md`
- `ch1/section_1_3_5_evidence_report_20251009.md`
- `ch1/harney_moten_evidence_20251009_182415.json`
- `ch1/tactical_innovations_20251009_182507.json`
- `ch1/THEORETICAL_CONCEPTS_EVIDENCE_TAXONOMY.md`
- `ch1/LINGUISTIC_MARKERS_EVIDENCE_CROSSREFERENCE.md`

### Chapter 2 Evidence

- `scripts/ch2/orphaned_content_examples_20250105.md`
- `scripts/ch2/statistical_validation_evidence_20250105.md`
- `scripts/ch2/metadiscourse_reflexive_circulation_20251023_091942.md`
- `scripts/metadiscourse_thematic_examples.json`
- `scripts/metadiscourse_query_results.json`

### Chapter 3 Evidence

- `scripts/ch3/shopping_cart_knowledge_circulation_20251028_173229.md`
- `scripts/ch3/shopping_cart_knowledge_circulation_20251028_173229.json`
- `scripts/ch3/SHOPPING_CART_EXECUTIVE_SUMMARY.md`
- `scripts/ch3/shopping_cart_strategy_evolution_analysis.md`
- `scripts/ch3/rate_my_schedule_risk_management_20251028.md`
- `scripts/shopping_cart_strategy_thread_report_20251028_153225.md`
- `scripts/tactical_barrier_comprehensive_report.md`
- `scripts/tactical_barrier_analysis_20251004_145018.json`
- `scripts/tactical_barrier_analysis_20251004_144949.json`

### Planning Documents

- `core_docs/planning/FINAL_ORGANIZATION.md` — project reorganization plan
- `core_docs/planning/CH1_TO_CH2_MIGRATION_PLAN.md` — evidence migration between chapters
- `core_docs/planning/CHAPTER_1_TODO.md`
- `core_docs/planning/CHAPTER_2_TODO.md`
- `core_docs/planning/CHAPTER_3_TODO.md`
- `core_docs/evidence/EVIDENCE_MASTER_ALLOCATION.md` — master evidence allocation tracker
- `core_docs/planning/BARUCH_INTERVIEW_QUESTIONS.md` — interview protocol for Baruch students

### Chapter Outlines

- `core_docs/chapters/chapter_3_microscopic_outline.md` — Chapter 3 (microscopic scale) outline

### Literature

- `literature/10-year-lit-review-dissertation.md` — 10-year literature review
- `literature/books-export/apple_books_highlights.{md,json,csv}` — Apple Books annotations export

### Interviews

- `00_ACTIVE/interviews/04-rf-transcript.txt` — fourth interview transcript (participant RF)

### Jekyll Dissertation Site

- Git commits for Jekyll evidence pages, link fixes, navigation updates

### Data Reorganization

- `databases/current/REORGANIZATION_SUMMARY.md` — database directory reorganization complete
- `cuny_month_over_month_2020.csv` — month-over-month activity data for 2020

> October was chapter-evidence extraction month. Systematic evidence reports were generated for all three chapters, the evidence master allocation was formalized, and the project directory underwent a major reorganization. Shopping cart registration strategy and rate-my-schedule analyses were key Chapter 3 contributions.

---

## November 2025

### Annotated Bibliography

- `core_docs/compendium/chapter_1/assets/bibliography/refannbib.md`
- `core_docs/compendium/chapter_2/assets/bibliography/refannbib.md`

### Chapter Outlines

- `core_docs/chapters/chapter_1_revised_outline.md` — revised Chapter 1 outline
- `core_docs/chapters/chapter_2_macroscopic_outline.md` — Chapter 2 (macroscopic scale) outline

### Research Process Log

- `core_docs/process/research_process_log.md` — updated research process log

### Discord Platform Analysis

- `scripts/ch2/discord_comprehensive_report_20251108.md`
- `scripts/ch2/DISCORD_ANALYSIS_EXECUTIVE_SUMMARY.md`
- `scripts/ch2/README_DISCORD_ANALYSIS.md`
- `scripts/discord_platform_analysis_20251108_134133.{md,json}`
- `scripts/discord_evidence_highlights.md`
- `scripts/discord_analysis_executive_summary.md`

### r/CUNY Data Export

- `output/01_raw_data/subreddit_exports/r_CUNY/` — full CSV/JSON export of r/CUNY data:
  - `r_CUNY_SUMMARY.md` — subreddit summary report
  - `r_CUNY_coverage_report.json` — data coverage metrics
  - CSV/JSON exports for users, comments, submissions, user activity

### Style Guide

- `archive/deprecated-directories/jan2026/DISSERTATION_STYLE_GUIDE.md` — style guide with theoretical terminology section

> November produced the Discord comparative analysis, the first full r/CUNY data export, and revised chapter outlines. The dissertation style guide was formalized. After this, a gap in commits suggests a writing-intensive period.

---

## December 2025

*No git commits recorded. This appears to have been a period of off-repository writing and revision.*

---

## January 2026

### Fellowship Proposal

- `docs/dissertation_proposal_fellowship/fellowship_proposal_it1.docx` (Jan 6)
- `docs/dissertation_proposal_fellowship/proposal_FINAL.docx` (Jan 8)
- `archive/deprecated-directories/old-data/output/output/fellowship_project-description.docx` (Jan 8)
- `archive/old-proposals/DISSERTATION_PROPOSAL.docx` — earlier proposal archived
- `archive/old-proposals/DISSERTATION_PROPOSAL.md`
- `archive/old-chapters/chapter_1_fellowship.md`

### CURRENT.docx and Compendium System

- `core_docs/CURRENT.docx` — main dissertation document (Jan 4)
- `core_docs/compendium/CHAPTER_1_RESEARCH_COMPENDIUM.md` (Jan 5)
- `core_docs/compendium/chapter_1/COMPENDIUM.md` (Jan 5)
- `core_docs/compendium/chapter_1/evidence/EVIDENCE_INDEX.md` (Jan 5)
- `core_docs/compendium/chapter_2/COMPENDIUM.md` (Jan 5)
- `core_docs/compendium/chapter_2/evidence/EVIDENCE_INDEX.md` (Jan 5)
- `core_docs/compendium/CURRENT_SYNC.md` — sync status document (Jan 5)
- `core_docs/compendium/OUTPUT_CATALOG.{md,json}` (Jan 5)
- `core_docs/compendium/OUTPUT_TIMELINE.html` (Jan 5)

### Chapter Drafts

- `core_docs/chapters/chapter_1_full.md` — full Chapter 1 draft (Jan 5)
- `core_docs/chapters/chapter-1-latest.md` — latest Chapter 1 iteration (Jan 6)

### CUNY Statistical Analysis

- `databases/current/scripts/CUNY_statistical_analysis_20260105_010841.{md,json}` (Jan 5)

### DOCX Build System

- `output/docx_build/cover.md` — cover page template (Jan 8)
- `output/docx_build/combined.md` — combined document source
- `output/docx_build/body.md` — body content
- `output/docx_build/bibliography.md` — bibliography section
- `tools/docx/reference.docx` — reference template (Jan 8)
- `tools/docx/reference_base.docx` — base reference template
- `tools/docx/postprocess_docx.py` — DOCX post-processing script

### Claude Code Skills

- `.claude/skills/output-data-curator.md` (Jan 5)
- `.claude/skills/compendium-synthesizer.md` (Jan 5)
- `.claude/skills/research-writer.md` (Jan 9)
- `.claude/skills/evidence-query.md` (Jan 9)
- `.claude/skills/chapter-builder.md` (Jan 9)
- `.claude/skills/findings-generator.md` (Jan 24)

### Research Writing Skills

- Git commit: `add research writing skills for dissertation evidence workflow` (Jan 10)
- Git commit: `add chapter 1 iteration a1 with boland, panek, barton/hamilton, smith integrations` (Jan 5)

### Chapter Planning

- `core_docs/planning/CHAPTER_CONVERGENCE_OVERVIEW.md` (Jan 12)
- `core_docs/planning/CONSOLIDATED_CHAPTER_OUTLINES.md` (Jan 12)

### Dissertation Argument

- `00_ACTIVE/argument.md` — dissertation argument document (Jan 16)

### Baseline Analysis

- `data/databases/current/scripts/BASELINE_ANALYSIS_2011-2020.md` (Jan 16)
- `data/databases/current/scripts/BASELINE_EVIDENCE_IDS.md` (Jan 16)
- `data/databases/current/scripts/BASELINE_SUMMARY.txt` (Jan 16)

### Corpus and Semantic Search

- `data/output/corpus/general_text_corpus.jsonl` (Jan 17)
- `data/output/corpus/test_corpus.jsonl` (Jan 17)
- `tools/semantic-search/gradio_app.py` — Gradio search interface (Jan 17)
- `tools/semantic-search/gradio_rag_app.py` — RAG search interface (Jan 17)
- `tools/semantic-search/generate_corpus_from_db.py` — corpus generator (Jan 17)

### TUI Query Tool

Major development sprint on the terminal query tool (all Jan 17):

- `tools/tui-query/tui_query.py` — interactive database query TUI
- Git commits: reactive property fixes, full passage display, fullscreen toggle, async execution fix, duplicate detection, CSV export

### Data Queries

- `data/output/queries/test_financial_aid.{csv,json}` (Jan 17)
- `data/output/queries/housing_crisis_2020.{csv,json}` (Jan 17)

### Literature Reviews

- `00_ACTIVE/lit_reviews/reddit-research.md` (Jan 18)
- `00_ACTIVE/lit_reviews/critical-university-studies.md` (Jan 18)
- `00_ACTIVE/lit_reviews/meta.md` (Jan 18)
- `00_ACTIVE/lit_reviews/knowledge_commons_scholarship.md.md` (Jan 18)
- `00_ACTIVE/refannbib.md` — annotated bibliography (Jan 18)
- `core_docs/refannbib.md` (Jan 18)

### Outlines

- `00_ACTIVE/outlines.md` — master outline (Jan 18)
- `00_ACTIVE/chapter_drafts/chapter_1_proposal_aligned_outline.md` (Jan 19)
- `00_ACTIVE/chapter_drafts/chapter_2_proposal_aligned_outline.md` (Jan 19)
- `00_ACTIVE/chapter_drafts/chapter_3_proposal_aligned_outline.md` (Jan 17)

### Dissertation Visualizations (Viz 1-4)

Created Jan 19-20, the first numbered visualization suite:

- **Viz 1** — March 2020 pandemic timeline: `viz1_march2020_timeline.html`
- **Viz 2** — Crisis topic intensification: `viz2_intensification_ratios.html`, `viz2_intensification_butterfly.html`, `viz2_intensification_summary.md`
- **Viz 3** — Federated vs centralized architecture: `viz3_federated_architecture.html`, `viz3_architecture_metrics.html`
- **Viz 4** — Network density comparison: `viz4_network_density.html`, `viz4_density_butterfly.html`, `viz4_density_explainer.html`, `viz4_density_summary.md`

### Dissertation Visualizations (Viz 5-7)

Created Jan 21:

- **Viz 5** — Bridge users edgewise clustering: `viz5_bridge_edge_network.html`, `viz5_clustering_impact.html`, `viz5_community_activity.html`, `viz5_edge_type_breakdown.html`, `viz5_posts_vs_comments.html`
- **Viz 6** — Late-night support infrastructure: `viz6_crisis_heatmap.html`, `viz6_engagement_comparison.html`, `viz6_hourly_distribution.html`, `viz6_late_night_intensification.html`, `viz6_late_night_summary.md`
- **Viz 7** — User participation inequality: `viz7_lorenz_curve.html`, `viz7_participation_evolution.html`, `viz7_participation_pyramid.html`, `viz7_super_user_concentration.html`, `viz7_user_participation_summary.md`

### Transfer Findings

- `00_ACTIVE/dissertation/findings/transferring/CUNY_TRANSFER_BARRIERS_FINDINGS.{md,docx}` (Jan 22)
- `00_ACTIVE/dissertation/findings/transferring/CUNY_TRANSFER_ENROLLED_2020-2025.{md,docx}` (Jan 24)

### Database Repair and Recovery

Major database recovery operation (Jan 22-27):

- Created `scripts/utilities/db_safety.py` — database safety module after B-tree corruption
- Multiple backup files generated: `*.backup_20260123_*.db`, `*.comment_recovery_backup_*.db`
- `CUNY_historical_data.CORRUPTED_20260127.db` — corrupted database preserved
- `Baruch_historical_data.BEFORE_REINDEX_20260127.db` — pre-reindex backup
- Git commit: `add retry logic and timeout to comment recovery for database corruption resilience` (Jan 27)
- Git commit: `add data collection and analysis infrastructure` (Jan 25)

### Audit Reports

- `data/output/05_reports/post_repair_audit_report.md` (Jan 23)
- `data/output/05_reports/database_audit_report.md` (Jan 25)

### Dissertation Visualizations (Viz 8-12)

Created Jan 24:

- **Viz 8** — Subreddit territory edge map: `viz8_territory_edge_map.html`, `viz8_territory_bridge_focus.html`, `viz8_territory_summary.md`
- **Viz 9** — Edge flow chord diagram: `viz9_edge_flow_chord.html`, `viz9_edge_flow_asymmetry.html`, `viz9_chord_summary.md`
- **Viz 10** — Temporal edge genesis: `viz10_temporal_edge_genesis.html`, `viz10_edge_pair_breakdown.html`, `viz10_cumulative_growth.html`, `viz10_temporal_summary.md`
- **Viz 11** — Edge weight distributions: `viz11_edge_weight_violins.html`, `viz11_edge_type_comparison.html`, `viz11_weak_strong_ties.html`, `viz11_distribution_summary.md`
- **Viz 12** — Bridge user connections: `viz12_bridge_connections.html`, `viz12_connection_summary.md`

### Bridge User Findings

- `00_ACTIVE/dissertation/findings/CUNY_BRIDGE_USERS_FINDINGS.{md,docx}` (Jan 24)

### Chapter 3 Bridge Users

- `00_ACTIVE/chapter_drafts/chapter_3_bridge_users_rewritten.docx` (Jan 30)

### PDF and Fine-Tuning

- `scripts/utilities/extract_pdf_text.py` — PDF text extraction (Jan 31)
- `data/output/literature_texts.jsonl` — extracted literature texts (Jan 31)
- `data/output/literature_unsloth_cpt.jsonl` — Unsloth continued pretraining dataset (Jan 31)
- Git commit: `add pdf text extraction and unsloth continued pretraining dataset` (Jan 31)

> January 2026 was the most productive month: fellowship proposal, DOCX build system, 12 numbered visualization suites, transfer and bridge user findings, database recovery infrastructure, TUI query tool, literature reviews, semantic search tools, fine-tuning dataset creation, and multiple chapter drafts. The visualization numbering system (Viz 1-12) was established as the canonical indexing scheme.

---

## February 2026

### Bridge User Study (00_STUDIES)

Consolidated bridge user research into self-contained study:

- `00_STUDIES/bridge-users/README.md` (Feb 2)
- `00_STUDIES/bridge-users/findings/CUNY_BRIDGE_USERS_FINDINGS.{md,docx}` (Feb 2)
- `00_STUDIES/bridge-users/findings/bridge_users_literature_review.md` (Feb 2)
- `00_STUDIES/bridge-users/findings/chapter_3_methodology.md` (Feb 2)
- `00_STUDIES/bridge-users/chapters/ch3-bridge-users.docx` (Feb 2)
- `00_STUDIES/bridge-users/scripts/edge_data_extractor.py` (Feb 2)
- `00_STUDIES/bridge-users/scripts/viz12_bridge_ego_edges.py` (Feb 2)
- `00_STUDIES/bridge-users/visualizations/viz12_bridge_connections.html` (Feb 2)
- `00_STUDIES/bridge-users/visualizations/viz12_connection_data.json` (Feb 2)
- `00_STUDIES/bridge-users/visualizations/viz12_connection_summary.md` (Feb 2)

### Chapter 3 Draft

- `00_ACTIVE/chapter_drafts/bridge-users/ch3-bridge-users.docx` (Feb 2)

### Fine-Tuning Pipeline

- `tools/finetuning/chunk_cpt_by_paragraph.py` — paragraph-level chunker (Feb 2)
- `tools/finetuning/validate_dataset.py` — dataset validator (Feb 2)
- `tools/finetuning/train_cpt.py` — Unsloth CPT training script (Feb 2)
- `tools/finetuning/literature_unsloth_cpt_chunked.jsonl` — chunked dataset (Feb 2)
- `data/output/literature_unsloth_cpt_chunked.jsonl` — copy in output (Feb 2)

### Quotes Collection

- `00_ACTIVE/quotes.md` — collected quotes for dissertation (Feb 3)

### Bridge User Discourse Analysis

- `00_STUDIES/bridge-users/scripts/analyze_bridge_user_discourse.py` (Feb 4)
- `00_STUDIES/bridge-users/findings/bridge_user_discourse_data.json` (Feb 6)
- `00_STUDIES/bridge-users/findings/bridge_user_discourse_findings.md` (Feb 7)

### Database Safety Hardening

- `scripts/utilities/db_safety.py` — updated with additional safeguards (Feb 7)
- `scripts/scraping/analysis/diagnose_and_repair.py` — hardened with db_safety (Feb 7)
- `scripts/scraping/analysis/migrate_databases.py` — hardened (Feb 7)
- `scripts/analysis/audit_subreddit_databases.py` — hardened (Feb 7)

### Scraper Infrastructure Updates (Feb 8)

All collection scripts hardened with db_safety module:

- `scripts/collection/recover_missing_comments.py`
- `scripts/collection/recover_missing_submissions.py`
- `scripts/collection/universal_reddit_scraper.py`
- `scripts/collection/fast_reddit_scraper.py`
- `scripts/collection/optimized_reddit_scraper.py`
- `scripts/collection/retrieve_former_users.py`
- `scripts/scraping/core/universal_reddit_scraper.py`
- `scripts/scraping/core/enhanced_scraper.py`
- `scripts/scraping/core/comprehensive_cuny_scraper.py`
- `scripts/scraping/tools/scrape_users.py`
- `scripts/scraping/analysis/test_user_access_fix.py`

### CUNY Database Report

- `00_ACTIVE/CUNY_DATABASE_REPORT_2026-02-08.{md,docx}` (Feb 9)

### Bridge User Contextualization

- `00_STUDIES/bridge-users/findings/bridge_user_contextualization.md` (Feb 9)
- `00_STUDIES/bridge-users/scripts/bridge_users_viz.py` (Feb 9)

### Visualization Updates (Viz 5 refresh)

Updated bridge clustering visualizations:

- `00_ACTIVE/visualizations/05_bridge_users_edgewise_clustering/viz5_*.html` (Feb 9, refreshed)
- `00_STUDIES/bridge-users/visualizations/viz5_*.html` (Feb 9, mirrored)
- `00_ACTIVE/visualizations/05_bridge_users_edgewise_clustering/viz5_bridge_clustering_summary.md` (Feb 9)

### Viz 13 — Participation Typology (new)

- `00_ACTIVE/visualizations/13_participation_typology/viz13_behavior_modality.html` (Feb 9)
- `00_ACTIVE/visualizations/13_participation_typology/viz13_contribution_distribution.html` (Feb 9)
- `00_ACTIVE/visualizations/13_participation_typology/viz13_cross_subreddit.html` (Feb 9)
- `00_ACTIVE/visualizations/13_participation_typology/viz13_cuny_vs_reddit.html` (Feb 9)
- `00_ACTIVE/visualizations/13_participation_typology/viz13_per_campus.html` (Feb 9)
- `00_ACTIVE/visualizations/13_participation_typology/viz13_participation_summary.md` (Feb 9)
- `00_STUDIES/cuny-reddit/scripts/viz13_participation_typology.py` (Feb 9)
- `00_STUDIES/cuny-reddit/visualizations/viz13_*.html` (Feb 9)
- `00_STUDIES/cuny-reddit/CUNY_Reddit_Participation_Typology.md` (Feb 9)

### Participation Statistics

- `data/databases/current/scripts/comprehensive_participation_stats.py` (Feb 9)
- `data/databases/current/scripts/participation_stats_20260209_010534.{md,json}` (Feb 9)
- `data/databases/current/scripts/PARTICIPATION_ANALYSIS_SUMMARY.md` (Feb 9)

### Baselines and Participation Findings

- `00_ACTIVE/dissertation/findings/CUNY_Reddit_Baselines_and_Participation.{md,docx}` (Feb 9)

### Interviews

- `00_ACTIVE/interviews/interview-01-NP-full.pdf` — full interview PDF (Feb 2)
- `00_ACTIVE/interviews/interview-01-NP-audio.srt` — audio transcript (Feb 2)
- `00_ACTIVE/interviews/BARUCH_INTERVIEW_QUESTIONS.md` — interview protocol (Feb 2)

### Project Documentation

- `00_ACTIVE/DRAFTS.md` — draft tracking document (Feb 9)

> February 2026 consolidated the bridge user study into the new `00_STUDIES/` structure, introduced Viz 13 (participation typology), hardened all scraper scripts with the db_safety module, created the fine-tuning pipeline, and generated the baselines/participation findings document. The `00_STUDIES/` directory pattern was established as the canonical location for self-contained research studies.

---

## March 2026

### Google Drive Sync (Mar 31)

Bulk sync of dissertation-related files from Google Drive into the writing bundle. Full manifest at reference/gdrive_sync/MANIFEST.md.

### Chapter Drafts (from Drive)

- chapter_drafts/2026-03-17_VP_Writing_Under_Surveillance.docx -- most recent VP draft on writing under AI surveillance (Mar 2026)
- chapter_drafts/2026-02-27_Writing_Under_Surveillance_Against_AI_Detection.pdf -- argument against AI detection software
- chapter_drafts/2026-02-05_Draft_3.docx -- third full draft iteration
- chapter_drafts/2026-01-15_Project_Narrative_1.5.docx -- project narrative draft
- chapter_drafts/2025-11-11_Writing_Under_AI_Detection_v2.md -- writing-under-surveillance chapter material
- chapter_drafts/2025-09-14_False_Positives_Defense_Strategies.pdf -- AI detection false positives framing
- chapter_drafts/2025-02-26_UNCUT_Drafts_Paragraphs_Fragments.pdf -- raw prose fragments and paragraph drafts (1.3MB)

### Core Documents (from Drive)

- core_docs/2025-12-10_Dissertation_Outline_Digital_Commons.pdf -- dissertation outline (Digital Commons and Urban Theo...)
- core_docs/2026-01-13_Dissertation_Prospectus.docx -- current prospectus
- core_docs/compendium/chapter_1/2026-01-05_Chapter_1_Research_Compendium.pdf -- Chapter 1 compendium export

### Advisement (from Drive)

- core_docs/advisement/2025-10-28_meeting_saved_closed_caption.txt -- advisor meeting transcript (Oct 2025)
- core_docs/advisement/2026-03-27_meeting_saved_closed_caption.txt -- advisor meeting transcript (Mar 2026)

### Fellowship Proposals (from Drive)

- reference/proposals/fellowship/2026-01-09_Fellowship_Proposal_Description.pdf
- reference/proposals/fellowship/2026-01-10_Fellowship_Proposal_Compendium.pdf
- reference/proposals/fellowship/2026-01-11_Fellowship_Proposal_Drafts.pdf
- reference/proposals/fellowship/2026-01-12_diss_fellowship.docx
- reference/proposals/fellowship/2026-01-15_Dissertation_Fellowship_Proposal.pdf

### Research Materials (from Drive)

- research_materials/lit_review/2026-01-12_Dissertation_Lit_Review_Synthesis.pdf -- literature review synthesis
- research_materials/2026-03-17_Reddit_Discourse_Analysis_Tool_Config.pdf -- Reddit discourse analysis tool configuration
- research_materials/2024-12-03_cail_reading_list.json -- CUNY AI Lab reading list (209KB JSON)

### Databases and Data (from Drive)

- dissertation/databases/data/2025-04-08_cunytest_v2_dataTable.xlsx -- CUNY test data table v2
- dissertation/databases/data/2024-12-06_10800_Subreddit_Data_Table.csv -- 10,800-subreddit dataset
- dissertation/databases/data/2024-12-05_Top_r_CUNY_Contributors.xlsx -- top r/CUNY contributors
- dissertation/databases/data/2024-08-28_subreddit_posts_saved.xlsx -- saved subreddit posts

### Interviews (from Drive)

- interviews/2025-03-10_interview_candidates_reddit_discord.csv -- recruitment candidate list

### Transfer Barriers (Drive supplement)

- dissertation/findings/transfer_barriers/2026-01-22_CUNY_Transfer_Barriers_Findings_gdrive.docx -- Drive version for comparison against existing canonical

### Cloze Reader Paper (stored in writing/, not diss/)

- writing/cloze-reader-paper/gdrive/2026-03-15_cloze_reader_v13_milwrite_intro_restored.docx
- writing/cloze-reader-paper/gdrive/2026-03-15_cloze_reader_v12_concrete.docx
- writing/cloze-reader-paper/gdrive/2026-03-15_cloze_reader_v02_s2_litreview.docx

### Bundle Maintenance

- reference/gdrive_sync/MANIFEST.md -- Google Drive sync manifest and inventory (exhaustive audit of 100+ Drive files)
- reference/DASHBOARD_WEB_PLAN.md -- staged plan for public dashboard launch

March 2026: exhaustive Google Drive audit downloaded 30 files into the writing bundle and cloze paper directory. Key additions: three Writing Under Surveillance drafts spanning Sep 2025 to Mar 2026, four Reddit/CUNY datasets, interview candidate list, CAIL reading list, three cloze reader paper versions, and the full fellowship proposal arc. Every file on Drive was classified as included or excluded with reason. The research_materials/, core_docs/advisement/, and dissertation/databases/data/ directories were expanded.

---

## Summary Statistics

| Month | Documents | Visualizations | Key Milestone |
|-------|-----------|----------------|---------------|
| Jul 2025 | 3 | 0 | Compendium infrastructure, interview 3 |
| Aug 2025 | ~40 | 18+ | Temporal dashboards, network graphs, corpus |
| Sep 2025 | ~12 | 0 | Synthesis reports, semantic search, problem discourse |
| Oct 2025 | ~25 | 0 | Chapter evidence extraction, project reorganization |
| Nov 2025 | ~15 | 0 | Discord analysis, r/CUNY export, chapter outlines |
| Dec 2025 | 0 | 0 | Writing period (no commits) |
| Jan 2026 | ~60 | 40+ | Viz 1-12, TUI tool, findings, database recovery |
| Feb 2026 | ~30 | 15+ | Bridge user study, Viz 13, db_safety, fine-tuning |
| Mar 2026 | 30 | 0 | Exhaustive Drive sync (100+ files audited), Writing Under Surveillance drafts, Reddit datasets, cloze reader versions |
