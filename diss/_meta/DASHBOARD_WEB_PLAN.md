# Dashboard Web Launch Plan

## Goal

Get the dissertation dashboard running on the public web in a form that is stable, legible, and usable on phones from day one.

This plan assumes the current state of the writing bundle:

- the bundle references a **Flask research website** at `tools/interactive-website/`
- the bundle references a **legacy Streamlit dashboard** at `tools/research-dashboard/`
- the actual dashboard application code is **not present in this bundle**
- the bundle does include evidence of existing outputs, dashboards, and visualization artifacts in `reference/DOCS.md` and `core_docs/compendium/OUTPUT_CATALOG.json`

Because of that, the first milestone is not deployment. The first milestone is **recovering and inventorying the actual dashboard code and its runtime dependencies**.

---

## Executive Recommendation

Use a **two-stage launch**.

### Stage A — Public dashboard-lite

Launch a static, mobile-friendly web presentation first using already-generated outputs, visualization exports, summaries, and narrative framing.

**Recommended host:** GitHub Pages or Cloudflare Pages

Why:

- easiest to ship quickly
- lowest ops burden
- easiest to make fast on mobile
- safe for public dissemination if only derived outputs are exposed
- works even before the Flask app is fully recovered

### Stage B — Full interactive dashboard

After the app code is recovered and audited, deploy the Flask dashboard as a proper web app with responsive UI and a clean mobile mode.

**Recommended host:** Render, Fly.io, or Railway

Why:

- supports Python app hosting cleanly
- easier than trying to force Flask into a static host
- allows separation of app server from static assets and derived data files

### Non-recommendation

Do **not** lead with the legacy Streamlit dashboard unless the Flask app proves unrecoverable.

Reason:

- the project notes already mark Streamlit as legacy
- public mobile UX is usually weaker out of the box
- layout control is more limited
- dissemination polish is harder

---

## Phase 0 — Recovery and Audit

### Objective

Recover the dashboard code, confirm what already works, and identify the minimum viable deployment target.

### Deliverables

- recovered app source for `tools/interactive-website/`
- dependency manifest
- list of routes/pages/API endpoints
- list of required data files
- inventory of assets that are safe for public exposure
- inventory of assets that must remain private or offline

### Tasks

1. **Recover the missing app code**
   - pull `tools/interactive-website/`
   - pull `tools/research-dashboard/`
   - pull any shared CSS, templates, JS, or API helpers
   - identify the real entrypoint: `enhanced_server.py` or successor

2. **Audit runtime requirements**
   - Python version
   - pip requirements
   - file paths assumed by the server
   - local absolute paths that must be removed
   - whether the app expects SQLite access, JSON exports, or generated HTML files

3. **Audit deployability**
   - can the app run from derived JSON/HTML artifacts only?
   - does it require local databases?
   - does it require live filesystem browsing?
   - can expensive computations be precomputed?

4. **Create a public/private data matrix**
   - safe public: derived stats, static visualizations, summaries, aggregated findings
   - restricted: raw databases, transcripts with sensitive material, admin tools, local paths

### Exit Criteria

You know whether the first public release should be:

- static-only
- hybrid static + API
- full Flask app

---

## Phase 1 — Public Dashboard-Lite

### Objective

Get a public-facing dashboard on the web fast using assets that already exist or can be exported cheaply.

### Recommended Scope

Create a site with these sections:

1. **Overview**
   - project summary
   - three-scale framework
   - corpus summary
   - what the dashboard covers

2. **Visualizations index**
   - numbered visualization cards
   - one-line interpretation per card
   - links to HTML, PNG, PDF, or summary pages when available

3. **Findings browser**
   - bridge users
   - transfer barriers
   - baseline participation
   - narratives

4. **Methods / data notes**
   - what is in the corpus
   - what is excluded
   - what counts as evidence
   - caveats and ethics statement

5. **Downloads / references**
   - selected reports
   - bibliography-facing materials
   - annotated outputs

### Technical Shape

Use a static site generated from:

- Markdown summaries
- exported charts
- generated HTML visualizations where safe
- a manifest JSON for navigation and metadata

### Recommended Host

- **GitHub Pages** if the site is mostly static HTML, Markdown, JS, and exported assets
- **Cloudflare Pages** if better asset handling, redirects, or preview deploys are needed

### Why this stage matters

It gives the project:

- a public URL
- a shareable research surface
- mobile access immediately
- a low-risk dissemination path while the full app is still being recovered

---

## Phase 2 — Full Flask Dashboard

### Objective

Deploy the actual research dashboard once the codebase is recovered and cleaned.

### Recommended Architecture

**Frontend/UI layer**
- server-rendered Flask templates or a light JS frontend
- responsive chart wrappers
- route-level progressive disclosure

**Data layer**
- derived JSON files checked into a deploy-safe artifact store
- no direct exposure of raw SQLite databases to the public app
- precomputed aggregates for expensive views

**Hosting**
- Render or Fly.io preferred
- object/static asset storage for charts and large derived files if needed

### Required Refactors Before Deployment

1. remove absolute local paths
2. move config to environment variables
3. separate public derived assets from private research files
4. add a reproducible startup command
5. add a healthcheck endpoint
6. add a minimal error page and offline fallback behavior

### API Strategy

If the current dashboard depends on local file access, convert that dependency into one of these:

- prebuilt JSON manifests committed to the deploy repo
- scheduled export step that writes public-safe JSON
- lightweight read-only API endpoints backed by derived files

Do not expose raw research databases directly to the public server.

---

## Mobile Requirements

Mobile has to be treated as a first-class target.

### Layout

- design for **single-column portrait** first
- use breakpoints around `480px`, `768px`, and `1024px`
- avoid wide desktop control panels that collapse badly
- move secondary controls into expandable drawers or accordions on small screens
- use sticky top or bottom navigation for section switching
- respect safe-area insets on iPhone-class devices

### Touch Interaction

- minimum hit target size: **44x44 px**
- no hover-only affordances
- no controls that require precise dragging unless there is a tap-based fallback
- legends, filters, and tabs must be finger-friendly
- chart interactions must support tap, pan, and reset without needing a mouse

### Visualization Strategy on Mobile

For each visualization, define a mobile behavior explicitly:

1. **full interactive version** if it remains legible on phones
2. **simplified mobile version** if legends, labels, or interaction density break down
3. **static preview + open full version** if the original chart is too dense for inline mobile use

### Chart-Specific Rules

- collapse long legends into toggles or drawers
- reduce simultaneous series shown by default
- shorten axis labels
- use tabular numerals for metric cards and tables
- convert wide data tables into stacked cards on small screens
- pre-render image fallbacks for especially heavy charts

### Performance

- lazy-load charts below the fold
- preload only above-the-fold summary content
- compress large assets
- keep initial payload light
- avoid shipping every visualization library to every page
- prefer route-level or component-level code splitting where possible

### Usability Rules

- first meaningful content under ~400ms when cached, and as fast as possible when uncached
- show clear loading states for heavy charts
- provide a visible reset control for every complex chart interaction
- chunk long explanatory text into collapsible sections on mobile
- keep one focal interaction per screen

### Accessibility

- keyboard reachable on desktop, touch-usable on mobile
- sufficient contrast in charts and UI chrome
- alt text or text summaries for nontrivial visuals
- reduced-motion friendly transitions
- transcripts or text equivalents for audio/video if any are added later

---

## Information Architecture

### Recommended Route Map

- `/` — overview and project framing
- `/dashboard` — index of modules
- `/dashboard/participation`
- `/dashboard/network`
- `/dashboard/bridge-users`
- `/dashboard/transfer-barriers`
- `/dashboard/narratives`
- `/methods`
- `/about-data`

### Mobile Navigation Recommendation

Use one of these patterns:

- **top tab bar** for 3-5 primary sections
- **bottom nav** if the mobile experience is app-like and section switching is frequent
- **accordion index** inside `/dashboard` for dense secondary routes

For this project, a **dashboard landing page + sectional cards** is safer than dropping users directly into a giant control panel.

---

## Data and Ethics Guardrails

Before public launch, verify that the web surface does **not** expose:

- raw SQLite databases
- local paths
- admin/debug endpoints
- private transcripts or personally identifying information
- unpublished or unreviewed internal working files by accident

Preferred public data forms:

- aggregated counts
- derived JSON summaries
- visual exports
- redacted excerpts
- interpretation-first findings pages

---

## Rollout Plan

### Milestone 1 — Inventory

- recover app code
- identify dependencies
- identify public-safe assets
- choose static-first or Flask-first path

### Milestone 2 — Mobile wireframes

- dashboard home
- section page
- chart page
- findings page
- methods/data note page

### Milestone 3 — Static public release

- launch dashboard-lite
- test on iPhone + Android widths
- test on slow network
- verify all links and assets

### Milestone 4 — Full app recovery

- restore Flask app locally
- replace local file assumptions
- build deploy config
- confirm public/private data split

### Milestone 5 — Full web app launch

- deploy Flask app
- preserve static pages as landing and fallback layer
- add analytics or simple usage logging if wanted

---

## Suggested Division of Labor

### Quimbot

- information architecture
- route planning
- manifests and indexes
- mobile content structure
- public/private asset matrix
- deployment checklist and launch docs

### Petrarch

- claim UI cleanup and text-structure tasks if desired
- help audit prose, navigation labels, and mobile readability
- claim any open dashboard planning subtasks in `reference/TODO.md`

---

## Definition of Done

The dashboard is meaningfully “running on the web” when all of the following are true:

- there is a stable public URL
- the main dashboard pages load on mobile without horizontal scrolling
- at least the core visualizations and findings are navigable from a dashboard landing page
- heavy views have mobile-safe fallbacks
- no private research infrastructure is exposed
- the deployment can be reproduced from documented steps

---

## Immediate Next Step

Create a **dashboard recovery checklist** from the full research repo and decide whether the first deployment is:

- **static dashboard-lite first**
- or **Flask app first**

Given the bundle state right now, **static dashboard-lite first** is the safer path.