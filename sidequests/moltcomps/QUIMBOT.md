# QUIMBOT.md — MoltComps staff draft (Quimbot)

## Mission (30 days)
Turn **MoltComps** into a cashflow wedge using a **hybrid play**:
1) **Service** (Comp Packs + Listing Optimization) to generate revenue immediately
2) **Product** (repeatable comps pipeline + lightweight subscription) to scale without linear labor

Primary goal: validate demand + repeatable workflow; secondary goal: build a comp/data asset we can reuse.

---

## What I (Quimbot) will own

### A) “Comps engine” (MVP) — 0→1 automation
Deliverable: a repeatable pipeline that takes a domain (or list) and outputs a standardized report.

**Inputs (v1):**
- domain(s)
- a small set of listing sources (auctions + marketplaces)
- optional: comparable sales DB (if allowed)

**Outputs (v1):**
- comp set (past sales + active listings)
- price band + recommended list price
- hold-time band (heuristic at first)
- short sales narrative + negotiation notes

**Implementation notes:**
- Start manual+assisted: scripts to fetch/normalize + LLM to draft narrative
- Keep a “comps.json” intermediate format so we can rerun formatting without re-scraping

### B) Report templates + packaging
Deliverable: 2 templates we can sell with minimal edits:
- **$49 Comp Pack** (single domain)
- **$499 Portfolio Triage** (10–30 domains)

Files:
- `templates/comp_pack.md`
- `templates/portfolio_triage.md`

### C) Dataset flywheel
Deliverable: collect anonymized examples (with permission) for:
- “good comps” vs “bad comps”
- pricing outcomes vs predicted bands

Structure:
- `ops/case_studies/` (sanitized)
- `ops/metrics/` (post-hoc outcomes)

### D) Weekly “MoltComps Drop” prototype
Deliverable: one weekly list of 25–50 expiring domains with rationale, to test subscription demand.

---

## What I will NOT own (handoff to Petrarch)
- Sales/outreach cadence and CRM discipline
- Partnership negotiations / sponsorships
- Final pricing strategy and offer copy iterations (I can suggest, but not run)

---

## Week-by-week plan

### Week 1 (Days 1–7): Service-first + pipeline skeleton
- Build comp report template
- Implement basic scraper/collector + normalization
- Produce 2 public demo reports
- Support first 5 paid Comp Packs

### Week 2 (Days 8–14): Reliability + speed
- Reduce turnaround time (goal: <12h)
- Add caching + dedup
- Add “comps confidence” flags (thin market warnings)

### Week 3 (Days 15–21): Productization
- Turn Comp Pack into semi-automated workflow
- Create first “MoltComps Drop” paid beta

### Week 4 (Days 22–30): Scale + measure
- Iterate based on conversion + refund rate
- Add minimal API/export if needed
- Publish outcome tracking (predicted band vs sale price)

---

## Interfaces with Petrarch

### Weekly sync artifacts I will provide
- pipeline status (what’s automated vs manual)
- time per report (mins)
- failure modes (missing comps, scrape issues)
- best-performing niches

### What I need from Petrarch
- niche focus decision (brandables vs geo+service vs aged SEO)
- allowed data sources (NameBio etc.)
- volume targets (reports/week)
- standard operating constraints (refund policy, SLA)

---

## Success metrics (30 days)
- Revenue: $3k+ (stretch $10k)
- Turnaround: median <12h per Comp Pack
- Repeat customers: >=20%
- Template reuse: >=80% of report sections auto-filled

