# Recent Work: CUNY Social Stories

Last updated: 2026-05-12

## Status

The social stories work now exists as a small static presentation package for yearly CUNY Reddit vignettes. It covers 2014 through 2025, uses the cross-year throughline of **CUNY Reddit as student-made infrastructure**, and keeps source prose in `_src/YYYY.md` so the presentation can be regenerated from editable research text.

The current package is both a research artifact and a readable site:

- Source markdown: `_src/2014.md` through `_src/2025.md`
- Future-year template: `_src/_TEMPLATE.md`
- Build script: `build.py`
- Generated site pages: `index.html`, `2014.html` through `2025.html`, and `all.html`
- Consolidated prose artifact: `all.md`
- Local workflow documentation: `README.md`

## Research and Writing Work Completed

The current pass built a twelve-year social-story arc from the CUNY-only Reddit corpus. The vignettes are not raw excerpts; they are paraphrased narrative accounts that preserve traceability through evidence IDs while following the dissertation's disguise protocol.

The main interpretive frame treats CUNY Reddit as **student-made infrastructure** because students use subreddit space to make CUNY's hidden social, administrative, financial, and professional procedures usable for one another. The arc begins with belonging, registration, and commuter friendship in 2014 and ends in 2025 with peer-built registration tools, textbook-cost workarounds, and rapid interpretation of federal aid uncertainty.

Each yearly source file now includes:

- YAML-style frontmatter with `year`, `title`, `date`, `subreddits`, and `evidence_ids`
- A yearly vignette organized around two or three anchor moments
- A closing paragraph that links the year to adjacent years in the arc
- An evidence line that records submission/comment IDs, subreddit, score, and date

## Yearly Content Map

| Year | Title | Main emphasis |
| --- | --- | --- |
| 2014 | Learning to Belong While Moving Through | Commuter belonging, graduation after work, friendship scripts, and registration access. |
| 2015 | The Four-Year Clock and the Aid Clock | Degree timing, transfer orientation, credit loads, and financial-aid portal interpretation. |
| 2016 | Commuting, Verification, and Falling Through | GPA repair, work/commute pressure, aid verification limbo, and graduation-audit self-defense. |
| 2017 | Repair After Isolation and Academic Collapse | Academic recovery, DegreeWorks record repair, transfer loneliness, and re-entry after collapse. |
| 2018 | Workarounds for Offices, Bills, and Phones That Do Not Pick Up | Collections anxiety, office-contact tactics, ePermit confusion, and procedural workarounds. |
| 2019 | Petitioning the Campus and Decoding Aid Holds | Course complaints, WiFi petitioning, aid holds, and collective infrastructure pressure. |
| 2020 | Pandemic Survival and the Limits of Resource Lists | Remote-learning breakdown, homelessness/basic needs, textbook costs, and the limits of peer referral. |
| 2021 | Mutual Aid After the Emergency Becomes Routine | Alumni textbook/transit help, professor archives, ARPA grant navigation, and routine mutual aid. |
| 2022 | Return-to-Campus Logistics and Basic Needs | CUNYfirst redesign, emergency housing support, refund guidance, and return-to-campus logistics. |
| 2023 | Digital Breakage and Career Translation | Ransomware anxiety, professor accountability, finance career advice, and post-graduation mobility. |
| 2024 | Advising Damage and Alumni Care Work | Advisor error, degree-audit self-checking, alumni resume help, and salary transparency. |
| 2025 | Tools for Registration and Panic Around the Safety Net | Federal aid panic, Schedule Builder add-ons, textbook workarounds, and technical and political peer infrastructure. |

## Site and Workflow Work Completed

The static site generator in `build.py` now reads each published `_src/YYYY.md` file, parses the frontmatter, converts the limited markdown body to HTML, sorts vignettes by year, and rewrites the generated pages.

Implemented presentation surfaces:

- `index.html`: landing page with preface, coda, and a linked list of all vignettes.
- `YYYY.html`: one page per year, with metadata, evidence section styling, and previous/next navigation.
- `all.html`: single-page reading version with a sticky horizontal year timeline.
- `all.md`: consolidated markdown version for review, sharing, or copying back into the canonical findings artifact.

The site also has shared styling in `build.py`: dark reading surface, responsive typography, compact metadata, evidence styling, footer navigation, and mobile behavior for the single-page timeline. The timeline uses browser-side JavaScript to highlight the current year while scrolling and to smooth-scroll to selected year sections.

## Planned AI-Detection Track

The 2023-current AI-detection / Javabot material should become a parallel thematic track rather than being folded wholesale into the existing 2023-2025 yearly pages. The working throughline is **writing process as audit trail** because students preserve drafts, timestamps, version histories, detector results, notes, and oral explanations when AI-detection software and instructor suspicion turn writing into evidence.

See `AI_DETECTION_INTEGRATION.md` for the proposed source structure, content map, builder changes, and chapter-level use.

## Ethics and Traceability

This work keeps Reddit material paraphrased rather than reproduced verbatim. The README and source template explicitly preserve the working rule: do not quote more than about five consecutive original words, and keep evidence IDs so claims remain auditable against the corpus.

The source databases named in the preface are:

- `CUNY`
- `Baruch`
- `QueensCollege`
- `HunterCollege`
- `CCNY`
- `BrooklynCollege`
- `JohnJay`
- `CUNYuncensored`

## Current Gaps and Next Work

- Confirm whether `all.md` should remain a manual consolidated artifact or be generated by `build.py`.
- Sync the cleaned `_src/` version back to the canonical findings file named in the README if that file still remains the source of record.
- Run visual QA on `index.html`, yearly pages, and `all.html` after any style or builder changes.
- Add the AI-detection thematic track from the 2023-current Javabot / narrative material once the source vignettes are split into yearly `_src/ai-detection/` files.
- Add a 2026 vignette only when the research sample and evidence IDs are ready.
- Decide whether the static site should stay embedded here or be copied into the published `quimbot/docs/cuny-social-stories/` path during deployment.

## Build Command

From this directory:

```bash
python3 build.py
```

The command regenerates `index.html`, each yearly HTML page, and `all.html` from `_src/`.
