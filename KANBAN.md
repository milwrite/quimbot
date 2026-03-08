# KANBAN.md — Quimbot Project Board

_Last synced: 2026-03-08 09:00 ET_

## ✅ Done
- **Gallery: Langton's Ant + Falling Sand** — merged to `main` (`9a6566e7`) ✅ 3/8
- **Gallery: mobile fixes (12 artifacts) + index (20 artifacts)** — 5 commits overnight ✅ 3/8
- **Gallery: Monte Carlo Pi + Ant Colony** — merged to `main` (`408e3a85`) ✅ 3/7
- **Microblog entry-11 (phyllotaxis) + entry-12 (Chladni)** — published (`a143e173`, `515e00f2`) ✅ 3/7
- **remove_flagged.py committed** — degenerate entry removal script ready to run (`0e9d57bc`) ✅ 3/7
- **Crystal DLA walker bug fixed** — continue/undo logic inversion (`97d90274`) ✅ 3/7
- **Workshop slides synced** — from cuny-ai-lab/gen-dev-foundations (`02ff4f4f`) ✅ 3/7
- **Superset3 flagged replies validated** — all 10 degenerate (2-38 chars), removal script next ✅ 3/7
- **Gallery: ASCII Donut + Crystal Dendrite (DLA snowflake)** — merged to `main` (`ea53d9ff`) ✅ 3/6
- **Superset3 blocker cleared** — data validation clean (`7a660b28`) ✅ 3/6
- **Gallery: Neon Tunnel + Wolfram Automaton** — merged to `main` (`efd3937a`) ✅ 3/5
- **Microblog entry-10: "What a flock doesn't know" (boids)** — published (`6547fc21`) ✅ 3/5
- **Gallery: Metaballs + Gray-Scott Reaction-Diffusion** — merged to `main` (`34c293cd`) ✅ 3/4
- **Gallery: Spring Wires + Cursor Aura visualizations** — merged to `main` (`a44bcf5`) ✅ 3/3
- **Gallery: Mandelbrot Set + Phyllotaxis** — morning drop 3/1 (`0c507ca4`) ✅ 3/1
- **Gallery: Chladni Figures + Julia Set** — added to docs/gallery (`e46913a`) ✅ 3/2
- **Gallery: rendering bugfix pass** — follow-up fixes landed (`201862e`) ✅ 3/2
- **"The Problem with AI Detection"** — 24 rounds of copyediting complete, title finalized, Watters epigraph, teaching tips companion page, citations fully validated (5-round audit), .docx exports ✅ 2/28
- Gallery: Chainwheel rebuild (monochrome → gunmetal → rainbow) + Color Rivers + TDZ/mobile/touch bugfixes ✅ 2/28
- Merge+dedup all sources → superset3 (5,560 unique rows) (`b67bbf4c`) ✅ 2/27
- Morning stand-up sync (2/27 07:00): Coordinated with Quimbot, identified billing block as root cause
- Gallery: Wave Interference + Clifford Attractor (`a20be098`) ✅ 2/27
- Gallery mobile optimization: Turing/voronoi HTML fixes for responsive display
- Microblog entry-6 published: New content in `docs/microblog/entry-6.html`
- TOEFL superset2 merged: 14,566 unique records (Petrarch's gemma3:27b batch deduped + merged)
- Microblog entry-2 (Rubik) + entry-4 (Fourier iframe) published; entry-5 removed
- Gallery bugfix: Clifford attractor var redeclaration (`0b4cf9de`)
- Site cleanup: OpenClaw files removed from repo, .gitignore updated, GH Pages source fixed

## 🔨 In Progress
- **Gallery dropdown nav + mobile responsive** — shipped 5 commits today (`04e1c2a1`..`dc29c3af`) ✅ 3/5
- **Starfield: steering + tracking overhaul** — 4x steering, lerp, cursor-distance speed (`3849b997`) ✅ 3/5
- **Microblog: gallery links for entry-6 + entry-7** — (`3c424fc0`) ✅ 3/5
- **TOEFL gen at 2,834/10,000 — process still stalled** (no active PID found at 07:00 stand-up)
- Gallery/docs iteration continues
- Superset3 quality validation needed (spot-check)
- Article publish prep (final review pass, deploy to site)
- **Workshop deck nearly done** — <https://cuny-ai-lab.github.io/gen-dev-foundations/#1>
  - [ ] Click / Space to advance slides
  - [ ] Images / screenshots for key steps
  - [ ] Parisa LLM intro slide(s)
  - [ ] Scrubber / slider to fast-forward through the deck

### 👇 Waiting on milwrite
- **🔴 CRITICAL: Execute OpenRouter billing fix** — Quimbot session blocked (HTTP 402) since 2/26 morning, blocking all training work
  - Option 1: Top up OpenRouter account
  - Option 2: Execute config.patch to rotate to funded API key (command ready from 2/26 AM stand-up)
- Stage 1 Run 4 eval blocker: Provide adapter weights location/transfer path (step 350 + final checkpoint)
- Stage 2 direction call: Keep local generation push running or pause after merge+dedup completes

## 📋 Backlog
- Stage 2 language/learner variant fine-tuning (Spanish SFT datasets scouted: ~1.1M rows from latam-gpt)
- Evaluation framework build-out (`evaluation/` dir exists, needs population + baseline report templates)
- A2A cross-machine delegation (Petrarch ↔ Quimbot task passing)
- Dataset quality metrics / automated filtering (length histograms, role-order checks, near-dup)

## 🚫 Blocked
- Stage 1 Run 4 checkpoint evaluation: adapter weights not on local disk
- OpenRouter scale-out generation: **HTTP 402 Payment Required** (billing/account state)
- Prospects cron Discord posting loop failing (`/bin/sh: 1: openclaw: not found` in `fine-tuning/prospects/cron.log`)

## 📝 Notes
- **Morning review 3/8 09:00:** Overnight: 5 mobile fix commits + gallery index (20 artifacts). Morning gallery drop: Langton's Ant + Falling Sand (`9a6566e7`). OpenRouter 402 day 11. superset3 file still not on disk. Tasked Petrarch with billing fix, superset3 pull, workshop slides, cron fix.
- **Morning review 3/7 09:00:** Overnight gallery (Monte Carlo Pi + Ant Colony) and microblog (entries 11-12). Flagged replies validated: all degenerate, removal script queued. OpenRouter 402 day 10. Tasked Petrarch with billing fix, removal script, workshop slides, cron fix.
- **Morning review 3/6 09:00:** Superset3 blocker cleared per 07:00 standup. Gallery added ASCII Donut + Crystal Dendrite. Training lane day 9 blocked (OpenRouter 402). Tasked Petrarch with billing fix, flagged-reply review, workshop slides, cron fix.
- **Morning review 3/5 09:00:** Gallery lane advanced overnight (Neon Tunnel + Wolfram Automaton, microblog entry-10). Training lane still blocked day 8. Tasked Petrarch with billing fix + gen restart + superset3 review.
- **Morning stand-up 3/5 07:00:** Pulled latest `main`, reviewed KANBAN, checked runtime/log state, and attempted Quimbot sync.
- **Quimbot sync attempt (3/5 morning):** `sessions_send` to label `Quimbot` returned "No session found with label: Quimbot" from this host.
- **Runtime/log check (3/5 morning):** No active TOEFL generation PID found; `fine-tuning/generation_qwen72b.log` still ends in OpenRouter HTTP 402 credits error; `fine-tuning/prospects/cron.log` is still missing on this checkout.
- **Today focus (3/5):** (1) execute billing fix, (2) restart generation and confirm live PID + log growth, (3) provide adapter weights transfer path for Stage 1 Run 4 eval, (4) verify/fix prospects cron runtime path, (5) continue workshop deck + gallery/docs throughput.
- **Evening stand-up 3/4 19:00:** Pulled latest `main`, reviewed KANBAN, checked runtime/log state, and attempted Quimbot sync.
- **Quimbot sync attempt (3/4 evening):** `sessions_send` to label `Quimbot` returned "No session found with label: Quimbot" from this host.
- **Progress since morning (3/4):** Gallery lane advanced with Metaballs + Gray-Scott pages merged to `main` (`34c293c`, 08:36 ET).
- **Runtime/log check (3/4 evening):** No active TOEFL generation PID found; `fine-tuning/generation_qwen72b.log` still ends in OpenRouter HTTP 402 credits error; `fine-tuning/prospects/cron.log` still missing on this checkout.
- **Tomorrow plan (3/5):** (1) execute billing fix, (2) restart generation and confirm live PID + log growth, (3) provide adapter weights transfer path for Stage 1 Run 4 eval, (4) verify/fix prospects cron runtime path, (5) continue workshop deck + gallery/docs throughput.
- **Morning stand-up 3/4 07:00:** Pulled latest `main`, reviewed KANBAN, and attempted Quimbot sync.
- **Quimbot sync attempt (3/4 morning):** `sessions_send` to label `Quimbot` returned "No session found with label: Quimbot" from this host.
- **Status delta (3/4 morning):** No new unblock signal detected from this host. Training lane remains blocked by billing (HTTP 402), missing adapter-path handoff, and stalled TOEFL generation. Gallery/docs/workshop lane remains active.
- **Today focus (3/4):** (1) execute billing fix, (2) restart generation and confirm live PID + log growth, (3) provide adapter weights transfer path for Stage 1 Run 4 eval, (4) verify/fix prospects cron runtime path, (5) continue workshop deck + gallery/docs throughput.
- **Evening stand-up 3/3 19:00:** Pulled latest `main`, reviewed KANBAN, and attempted Quimbot sync.
- **Quimbot sync attempt (3/3 evening):** `sessions_send` to label `Quimbot` returned "No session found with label: Quimbot" from this host.
- **Progress since morning:** Gallery lane moved forward with Spring Wires + Cursor Aura visualizations merged to `main` (`a44bcf5`).
- **Runtime/log check (3/3 evening):** `generation_qwen72b.log` still ends in OpenRouter HTTP 402 credits error; no `fine-tuning/prospects/cron.log` present in this checkout.
- **Tomorrow plan (3/4):** (1) execute billing fix, (2) restart generation and confirm live PID + log growth, (3) provide adapter weights transfer path for Stage 1 Run 4 eval, (4) verify/fix prospects cron runtime path, (5) continue workshop deck + gallery/docs throughput.
- **Morning stand-up 3/3 07:00:** Pulled latest `main`, reviewed KANBAN, and attempted Quimbot sync.
- **Quimbot sync attempt (3/3 morning):** `sessions_send` to label `Quimbot` returned "No session found with label: Quimbot" from this host.
- **Status delta (3/3 morning):** Workshop deck/gallery/docs lane continues moving. Training lane still blocked by OpenRouter billing (HTTP 402), missing adapter-path handoff, and stalled TOEFL generation.
- **Today focus (3/3):** (1) execute billing fix, (2) restart generation and confirm live PID + log growth, (3) provide adapter weights transfer path for Stage 1 Run 4 eval, (4) verify/fix prospects cron runtime path.
- **Evening stand-up 3/2 19:00:** Pulled latest `main`, reviewed KANBAN, and attempted Quimbot sync.
- **Quimbot sync attempt (evening):** `sessions_send` to label `Quimbot` returned "No session found with label: Quimbot" from this host.
- **Progress since morning:** Gallery lane moved forward with Chladni + Julia pages and a rendering bugfix pass merged to `main` (`e46913a`, `201862e`).
- **Status delta since morning:** Training lane still blocked on billing + adapter-path dependencies; no confirmation of resumed TOEFL generation from this host.
- **Tomorrow plan (3/3):** (1) Execute billing fix first, (2) restart generation and verify live PID + log growth, (3) provide adapter weights path for Stage 1 Run 4 eval, (4) verify/fix prospects cron path/runtime, (5) continue gallery/docs throughput while training lane is blocked.
- **Morning stand-up 3/2 07:00:** Pulled latest `main`, reviewed KANBAN, and attempted Quimbot sync.
- **Quimbot sync attempt (morning):** `sessions_send` to label `Quimbot` still returns "No session found with label: Quimbot" from this host.
- **Runtime check (3/2):** No active TOEFL generation PID found (`pgrep` only shows editor/python service helpers).
- **Log check (3/2):** `fine-tuning/generation_qwen72b.log` still ends in OpenRouter HTTP 402 credits error (insufficient credits).
- **Cron check (3/2):** `fine-tuning/prospects/cron.log` is still missing on this checkout.
- **Status delta vs 3/1 evening:** No net progress change on blocked training lane. Gallery/docs remains the only confirmed unblocked lane.
- **Immediate path:** (1) Execute billing fix, (2) restart generation and verify live PID + log growth, (3) provide adapter weights path for Stage 1 Run 4 eval, (4) restore/fix prospects cron path/runtime.
- **Evening stand-up 3/1 19:00:** Pulled latest `main` and re-checked board state. No net progress change since morning sync.
- **Quimbot sync attempt (evening):** `sessions_send` to label `Quimbot` still returned "No session found with label: Quimbot" from this host.
- **Status delta since morning:** Training pipeline still blocked by OpenRouter HTTP 402. No active TOEFL generation PID found. Gallery/docs lane remains the only confirmed unblocked lane.
- **Tomorrow plan:** (1) Execute billing fix first, (2) restart generation job and verify live PID + log growth, (3) resolve adapter weights transfer path for Stage 1 Run 4 eval, (4) verify/fix prospects cron path/runtime.
- **Gallery drop 3/1 08:33:** Mandelbrot (click-to-zoom fractal explorer, smooth coloring) + Phyllotaxis (golden angle spiral, 1400 dots). Trend: Mandelbrot/fractal content dominating r/CreativeCoding this morning.
- **Morning stand-up 3/1 07:00:** Pulled latest `main` and reviewed board + local runtime/log state.
- **Runtime check:** No active TOEFL generation process found (`pgrep`), while Ollama daemon is still running.
- **Log check:** `fine-tuning/generation_qwen72b.log` still ends in OpenRouter HTTP 402 credits error.
- **Cron check:** `fine-tuning/prospects/cron.log` is currently missing on this checkout (previous board note referenced `/bin/sh: 1: openclaw: not found`).
- **Critical path:** Execute billing fix → resume generation/merge pipeline → restore prospects cron visibility/fix → prepare eval launch when adapter weights arrive.
- Gallery/docs work continues unblocked (static generation, no API calls required).
