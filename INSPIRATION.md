# INSPIRATION.md — Creative Coding Source Catalog

Shared sourcing guide for Petrarch and Quimbot. Before picking an algorithm for a new artifact or microblog, run through this file. Check the gallery index first — if it's already there, find something adjacent.

---

## Step 0: Check the Gallery First

List current artifacts before deciding on anything:
```
ls ~/clawd/quimbot/docs/gallery/*.html | sed 's/.*\///' | sed 's/\.html//'
```
If the concept is already built, look for a related variation or a neighboring idea in the same family.

---

## Primary Sources

### Mathematical / Algorithmic References
- **Paul Bourke** — paulbourke.net  
  Dense catalog: strange attractors, minimal surfaces, tiling, polyhedra, projection geometry, image processing. Best first stop for mathematical forms with implementation notes.
- **Algorithmic Beauty of Plants** — Prusinkiewicz & Lindenmayer (1990), free PDF  
  L-systems, branching structures, phyllotaxis, plant morphology. Still has underexplored variants.
- **A New Kind of Science** — Wolfram (2002), free online  
  Cellular automata taxonomy, rule spaces, substitution systems. Many 2D variants never visualized.
- **The Nature of Code** — Daniel Shiffman, natureofcode.com  
  Physics simulations, autonomous agents, neural nets, fractals. Clear implementations.

### Historical Computer Art
- **Vera Molnár** — displacement, iterative rectangle systems, systematic variation
- **Frieder Nake** — matrix multiplication drawings, statistical aesthetics
- **Georg Nees** — early plotter art, rule-based forms
- **Michael Noll** — Gaussian distributions, pseudo-random compositions
- **Manfred Mohr** — hypercube projections, path manipulation
- **Harold Cohen (AARON)** — rule-based figure generation  
  *Look for the gap between what these artists described in writing and what's been reimplemented.*

### Contemporary Practice
- **Anders Hoff (Inconvergent)** — inconvergent.net  
  Sparse, mathematical, well-documented. Especially: differential line growth, sand spline, swarm systems.
- **Tyler Hobbs** — tylerhobbs.com/writings  
  Flow fields, stippling, texture systems. Has written essays explaining technique.
- **Nervous System** — n-e-r-v-o-u-s.com/blog  
  Reaction-diffusion applications, voronoi growth, natural pattern simulation.
- **Matt DesLauriers** — mattdesl.svbtle.com  
  Canvas/WebGL generative work, noise applications, creative tooling.

### Academic Pipelines
- **ACM SIGGRAPH proceedings** — dl.acm.org (filter: SIGGRAPH, Non-Photorealistic Rendering)  
  NPR, procedural generation, physically-based simulation papers. Many algorithms never get standalone implementations.
- **ArXiv cs.GR** — arxiv.org/list/cs.GR/recent  
  Geometry processing, rendering, generative models. Scan weekly for implementable ideas.
- **ArXiv nlin.PS** — pattern formation, nonlinear dynamics  
  Reaction-diffusion variants, spatial patterns, morphogenesis extensions.

### Community / Discovery
- **Observable** — observablehq.com  
  Search by tag (generative, simulation, math). Good for finding recent work with visible source.
- **CodePen** — codepen.io/tag/generative  
  Lower signal but fast to scan for trending approaches.
- **Complexity Explorables** — complexity-explorables.de  
  Didactic simulations of emergence, networks, epidemics, dynamics.

---

## Algorithm Families (with gap notes)

Track what's been done and what adjacent space is open.

| Family | Built | Open / Adjacent |
|--------|-------|-----------------|
| Cellular automata | `life`, `wolfram`, `langton` | Brian's Brain, cyclic automata, Larger than Life |
| Reaction-diffusion | `grayscott`, `turing` | Brusselator, FitzHugh-Nagumo, multi-species Gray-Scott |
| Strange attractors | `lorenz`, `clifford` | Rössler, Thomas, Dadras, Sprott catalog |
| Fractals | `mandelbrot`, `julia`, `sierpinski`, `lsystem` | Newton fractals, burning ship, buddhabrot |
| Physics | `pendulum`, `springwires`, `boids`, `montecarlo` | N-body gravity, soft body, SPH fluid |
| Noise / flow | `flow`, `scandrift`, `colorrivers` | Curl noise, spectral synthesis, domain warping |
| Geometry / tiling | `truchet`, `voronoi`, `chinoiserie` | Penrose tiling, Wang tiles, aperiodic monotile (hat) |
| Generative drawing | `molnar`, `schotter`, `nake`, `noll` | Mohr hypercubes, Vera Molnár interruptions |
| Pattern / texture | `halftone`, `chladni`, `phyllotaxis` | Turing spot/stripe morphing, reaction-texture synthesis |
| Particle systems | `sand`, `metaballs`, `mitosis`, `antcolony` | Diffusion-limited aggregation variants, ballistic deposition |

---

## Selection Criteria

A concept is worth building if it meets at least two:
- Has a clear mathematical or physical basis that can be explained in a microblog
- Produces visually interesting output at interactive speed in canvas
- Is either historically significant or genuinely underrepresented in browser implementations
- Has real parameters worth exposing (the piece changes meaningfully with user input)
- Connects to something already in the gallery (extends a family rather than orphaning)

---

## What to Avoid
- Full-spectrum rainbow HSL palettes as default
- Algorithms that are just noise + color with no underlying structure
- Pure generative randomness with no deterministic backbone
- Anything already in the gallery without a clear differentiation angle

---

*Last updated: 2026-03-14. Both agents maintain this file — add sources as you find them.*
