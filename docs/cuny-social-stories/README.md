# CUNY Social Stories

Yearly vignettes from the CUNY Reddit corpus (2014–present). Static site under `quimbot/docs/cuny-social-stories/`, served at `milwrite.github.io/quimbot/cuny-social-stories/`.

For the current work log and content map, see [`RECENT_WORK.md`](RECENT_WORK.md).

## Layout

```
cuny-social-stories/
├── _src/                  source markdown, one file per year
│   ├── 2014.md
│   ├── 2015.md
│   ├── ...
│   └── _TEMPLATE.md
├── build.py               regenerates HTML from _src/
├── index.html             generated landing page
├── all.html               generated single-page version with timeline
├── all.md                 consolidated markdown version for review/sync
├── 2014.html ... 2025.html   generated per-year pages
├── RECENT_WORK.md         dated status, content map, and next work
└── README.md
```

## Add a new vignette

1. Copy `_src/_TEMPLATE.md` to `_src/YYYY.md`.
2. Fill in frontmatter and body. Paraphrase Reddit posts — never quote verbatim.
3. Run:

   ```
   python3 build.py
   ```

4. Commit `_src/YYYY.md` and the regenerated HTML.

The build script reads every `_src/YYYY.md` whose frontmatter `published` is not `false`, sorts by `year`, and rewrites `index.html`, `all.html`, and `YYYY.html` from scratch. Prev/next nav between years is derived from the sort order.

## Source format

```markdown
---
year: 2026
title: "Short sub-theme phrase"
date: 2026-01-01
subreddits: [CUNY, Baruch]
evidence_ids:
  - submission_xxxxx
  - comment_yyyyy
---
Body paragraphs. Markdown supported: paragraphs, `code`, **bold**, *italic*, and the special evidence line.

**Evidence**: submission_xxxxx (r/sub, Score: N, Date: YYYY-MM-DD); ...
```

## Conventions

- One vignette per year. Build expects unique `year` values.
- Evidence IDs follow `submission_XXXXX` / `comment_XXXXX` and link back to the corpus.
- Paraphrase per Reagle/Bruckman disguise protocol. Never reproduce more than ~5 consecutive original words.
- Motif (cross-year through-line) is currently "student-made scaffolding"; if you change it, update `MOTIF` in `build.py` and the index preface.

## Source of truth

The canonical research artifact lives at
`reddit-diss/00_ACTIVE/dissertation/findings/social_stories/CUNY_SOCIAL_STORIES_YEARLY_VIGNETTES.md`.
This site is the readable presentation; if the two diverge, edit `_src/` here and copy the cleaned version back to the findings file.
