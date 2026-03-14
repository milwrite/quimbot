# INSPIRATION.md — Sourcing for Gallery Artifacts & Microblogs

Before picking an algorithm to build, check these in order.

---

## 1. Cross-check the existing gallery

**Do this first.** Pull up `docs/gallery/` (or `creative-clawing/gallery/`) and confirm the algorithm isn't already there. No duplicates.

---

## 2. Active sourcing (check at least one per session)

### Web catalogs
- **paulbourke.net** — Dense catalog of mathematical surfaces, strange attractors, tiling systems, geometry algorithms. Best single reference for "what exists."
- **inconvergent.net** — Anders Hoff's generative work with write-ups. Good for noise-based and organic algorithms.
- **tylerxhobbs.com** — Tyler Hobbs' essays on flow fields, noise, and fine art generative work. Good for technique depth.
- **r/creativecoding** — Trending implementations, new takes on old algorithms.
- **Observable (observablehq.com)** — Live notebooks; good for seeing what practitioners are actively exploring.
- **CodePen (trending/creative)** — Surface-level but catches momentum.

### Canonical texts (algorithm hunting)
- **The Nature of Code** (Shiffman) — Best taxonomy: physics, cellular automata, neural nets, emergence, fractals.
- **Algorithmic Beauty of Plants** (Prusinkiewicz) — L-systems and parametric growth. Bibliography leads outward.
- **A New Kind of Science** (Wolfram) — Cellular automata taxonomy; Chapter 2 is a catalog.
- **Chaos, Fractals and Dynamics** / Pickover's writing — Index of strange attractors, fractal systems.

### Research trail
- **ACM SIGGRAPH proceedings** (dl.acm.org) — Old papers contain underimplemented ideas. Search by decade.
- **ArXiv cs.GR** (new submissions) — Active research in graphics/geometry. Skim weekly.
- **Wikipedia "computational" categories** — Follow links from known algorithms to obscure predecessors.

---

## 3. Selection criteria

Before committing to an algorithm, answer:
A concept needs to meet **at least two** of these to be worth building:
- [ ] Has historical grounding worth writing about (date, inventor, context)
- [ ] Can be made interactive or visually surprising in <300 lines
- [ ] Adds something the gallery doesn't have (new tag, new era, new technique)
- [ ] Has a clear mathematical or algorithmic structure that can be explained in prose

**Avoid:**
- Rainbow / full-spectrum HSL palettes (restrained palettes only)
- Pure noise fields with no structural logic
- Direct duplicates of existing gallery entries
- Purely decorative work with no historical or technical hook

---

## 4. Microblog sourcing (even-night workflow)

When writing a microblog entry:
1. Pick an **older** artifact — not built this week
2. Web search: use Perplexity or Brave for historical context, related papers, reception
3. Find the **original paper or publication** — date it accurately before writing
4. Pull the **actual code** from the source file for the snippet — no pseudocode

---

## Tags reference (for consistent tagging)

`parametric` · `cellular-automata` · `l-system` · `plotter-era` · `emergence` · `noise` · `interaction` · `fractal` · `simulation` · `math` · `physics`
