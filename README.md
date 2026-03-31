# writing bundle

portable dissertation writing workspace (143 files, ~90 MB).
mirrors 00_ACTIVE/ from the main research repository with supplements.

## structure

```
writing/
├── core_docs/
│   ├── CURRENT.docx              main dissertation document
│   ├── refannbib.json            master bibliography (3.7 MB)
│   ├── chapters/                 chapter organization
│   ├── compendium/               per-chapter evidence aggregation
│   │   ├── chapter_1/            5 asset files
│   │   ├── chapter_2/            text analysis, bibliography (networks excluded — 16 GB)
│   │   └── chapter_3/            placeholder
│   └── evidence/                 citation tracking
│
├── visualizations/               13 numbered interactive visualization suites
│   ├── 01_pandemic_timeline/
│   ├── 02_crisis_topic_intensification/
│   ├── 03_federated_centralized_architecture/
│   ├── 04_network_density_comparison/
│   ├── 05_bridge_users_clustering/
│   ├── 06_late_night_support/
│   ├── 07_user_participation_inequality/
│   ├── 08_subreddit_territory_edge_map/
│   ├── 09_edge_flow_chord_diagram/
│   ├── 10_temporal_edge_genesis/
│   ├── 11_edge_weight_distributions/
│   ├── 12_bridge_user_connections/
│   └── 13_participation_typology/
│
├── dissertation/
│   └── findings/
│       ├── bridge_users/         core bridge user analysis (md, docx, pdf, json)
│       ├── transfer_barriers/    transfer obstacle findings
│       ├── baseline_participation/  participation pattern data
│       └── narratives/           student voice evidence documents
│
├── chapter_drafts/
│   ├── outlines.docx             proposal-aligned chapter outlines
│   ├── chapter_3_bridge_users_rewritten.docx
│   └── bridge-users/             ch3 drafts + literature review
│
├── interviews/                   4 transcripts + protocol
│   ├── 01-np-transcript.txt
│   ├── 02-hi-transcript.txt
│   ├── 03-ej-transcript.txt
│   ├── 04-rf-transcript.txt
│   ├── BARUCH_INTERVIEW_QUESTIONS.md
│   └── transcripts.zip
│
├── reviews/
│   ├── quotes.md                 collected quotes
│   └── refannbib.md              annotated bibliography
│
├── ## root-level working documents ##
├── chapter-1-iteration-a1.md     chapter 1 draft (59 KB)
├── proposal.md                   dissertation proposal
├── progress_reports.md           monthly progress tracking
├── mar14.md                      session notes
├── methodological_addendum_ai_scaffold.md/docx
├── vp_post_ai_detection.md
├── drafts.md                     draft tracking
│
├── ## supplements ##
├── reference/
│   ├── DOCS.md                   document generation chronicle
│   ├── TODO.md                   research priorities & evidence protocols
│   ├── CLAUDE.md                 project architecture reference
│   ├── cuny_facts_database.json  institutional metadata
│   └── proposals/                fellowship proposal drafts + FINAL + guidelines
│
└── templates/
    └── reference_base.docx       pandoc template (TNR, 1" margins, double spacing)
```

## what's excluded

- **network graph data** (16 GB): raw .gexf, .graphml, .json in compendium/chapter_2/assets/networks/
- **sqlite databases** (300 MB): live in data/databases/current/
- **python scripts & venv**: analysis infrastructure
- **jekyll site**: tools/jekyll-site/ (753 evidence pages)
- **query results**: data/output/queries/

## document generation

```bash
# convert markdown to docx
pandoc INPUT.md -o OUTPUT.docx

# with template formatting
pandoc INPUT.md -o OUTPUT.docx --reference-doc=templates/reference_base.docx
```
