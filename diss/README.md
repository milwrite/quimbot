# dissertation bundle

Portable dissertation workspace organized into four domains.

## structure

    diss/
    |
    |-- writing/              YOUR PROSE -- drafts, chapters, outlines, proposals
    |   |-- CURRENT.docx      main dissertation document
    |   |-- proposal.md       dissertation proposal
    |   |-- progress_reports.md
    |   |-- drafts.md         draft tracking
    |   |-- chapters/         chapter drafts (Ch1, Ch3/bridge-users, VP/surveillance, outlines)
    |   |-- proposals/        fellowship proposals, guidelines, final proposal
    |   |-- addendum/         methodological addendum (AI scaffold)
    |   |-- advisement/       meeting transcripts, progress reports PDF
    |   |-- quotes.md
    |   +-- vp_post_ai_detection.md
    |
    |-- research/             ACADEMIC RESEARCH -- sources, bibliographies, reading lists
    |   |-- bibliography/     master refannbib.json + per-chapter annotated bibliographies
    |   |-- lit_review/       lit review synthesis, Ch1 research compendium
    |   |-- tools/            Reddit discourse analysis tool config
    |   |-- cuny_facts_database.json
    |   +-- 2024-12-03_cail_reading_list.json
    |
    |-- evidence/             EVIDENCE -- findings, data, narratives, interviews
    |   |-- findings/
    |   |   |-- bridge_users/           bridge user discourse findings, methodology, study overview
    |   |   |-- transfer_barriers/      CUNY transfer barriers findings, enrollment data
    |   |   +-- baseline_participation/ participation typology data
    |   |-- narratives/       student voice evidence (trajectory narratives, Reddit corpus)
    |   |-- databases/        subreddit data tables, CUNY contributors, database reports
    |   |-- interviews/       4 transcripts, protocol, candidate list, audio
    |   |-- text_analysis_ch1/
    |   |-- text_analysis_ch2/
    |   |-- networks_ch1/
    |   +-- networks_ch2/
    |
    |-- visualizations/       VISUALIZATIONS -- 13 numbered interactive suites
    |   |-- 01_march2020_pandemic_timeline/
    |   |-- 02_crisis_topic_intensification/
    |   |-- 03_federated_vs_centralized_architecture/
    |   |-- 04_network_density_comparison/
    |   |-- 05_bridge_users_edgewise_clustering/
    |   |-- 06_late_night_support_infrastructure/
    |   |-- 07_user_participation_inequality/
    |   |-- 08_subreddit_territory_edge_map/
    |   |-- 09_edge_flow_chord_diagram/
    |   |-- 10_temporal_edge_genesis/
    |   |-- 11_edge_weight_distributions/
    |   |-- 12_bridge_user_connections/
    |   +-- 13_participation_typology/
    |
    +-- _meta/                REFERENCE -- TODO, docs chronicle, dashboard catalog, Drive manifest
        |-- TODO.md
        |-- DOCS.md
        |-- CLAUDE.md
        |-- DASHBOARD_WEB_PLAN.md
        |-- OUTPUT_CATALOG.json
        +-- gdrive_sync/MANIFEST.md


## the four domains

WRITING    -- your words. Drafts, chapters, proposals, addenda, advisement notes.
               Everything here is prose you wrote or are writing.

RESEARCH   -- other people's words. Bibliographies, lit reviews, reading lists,
               tool documentation. Source material that informs the dissertation.

EVIDENCE   -- the data speaking. Findings reports, narratives, interview transcripts,
               database exports, text analysis outputs, network validation.
               Grounded in specific accounts of what the corpus shows.

VISUALIZATIONS -- the data shown. 13 numbered suites (Viz 1-13), each with
               PDF/PNG/SVG static exports and interactive HTML where applicable.


## what's excluded from this bundle

- network graph data (16 GB): raw .gexf, .graphml, .json
- sqlite databases (300 MB): live in data/databases/current/
- python scripts and venv: analysis infrastructure
- jekyll site: tools/jekyll-site/ (753 evidence pages)
- query results: data/output/queries/


## document generation

    pandoc INPUT.md -o OUTPUT.docx
    pandoc INPUT.md -o OUTPUT.docx --reference-doc=templates/reference_base.docx
