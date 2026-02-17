# Slide 1
## Creative Coding with Generative AI
### Welcome: “What does code look like?”
- Watch a one-line program build a maze
- Treat code as a visual pattern generator
- Choose “/” or “\” at random; repeat
- Notice how randomness creates structure over time  
Artifact: 10 PRINT (Commodore 64, 1982) — a one-rule maze generator.

---

# Slide 2
## Icebreaker
### Describe an algorithm you already know
- Write a routine in three steps or fewer
- Name the shape: sequence, conditional, loop
- See “rules executed by hand” as code
- Share one example; spot the hidden logic  
Note: Keep it fast — read 2–3 examples aloud.

Stage text:
- In chat, post:
- “Describe something you do by following steps… in three instructions or fewer.”
- Look for: “If X then Y” (conditional), “Repeat until done” (loop), “First A then B” (sequence).

---

# Slide 3
## Origins (1962–1965)
### Bell Labs + first computer art
- Place early computer art in Bell Labs era
- Combine equations with pseudo-random variation
- Generate order first; introduce disorder gradually
- Move from plotter output to public exhibitions  
Artifact: “Schotter”-style plotter disorder — click to re-roll.

---

# Slide 4
## Vera Molnar
### The “machine imaginaire”
- Define art as rules plus “a hint of disorder”
- Constrain a system; let chance disturb it
- Treat constraints as the artwork’s engine
- Connect constraint prompts to Molnar’s method  
Artifact: a grid disrupted by an interruption zone.

---

# Slide 5
## Creative Coding Today
### p5.js + browser as canvas
- Use the browser as a portable art canvas
- Learn with p5.js; ship with plain HTML/JS
- Prefer single-file artifacts you can share
- Keep tools lightweight: no build step

Stage text:
- p5.js — Start fast with friendly drawing primitives.
- Vanilla HTML/CSS/JS — Ship single-file sketches; run anywhere instantly.

---

# Slide 6
## Key Concept
### The creative coding triangle
- Map a piece across: Rules / Randomness / Interpretation
- Shift the balance to change the work’s feel
- Translate to LLMs: system prompt / temperature / curation
- Use the triangle to diagnose “why this output”  
Artifact: drag the point; watch emphasis change.

---

# Slide 7
## Vibe Coding
### Prompts as prototypes
- Prototype with prompts; test in the browser
- Generate fast; evaluate with your own eyes
- Contrast: “no-review” vs reviewed iteration
- Adopt the mode that matches your goal
- Attribute “vibe coding” to Karpathy (Feb 2025)

---

# Slide 8
## Spectrum
### Vibe → deliberate collaboration
- Place AI coding on a continuum of control
- Move from one-shot → iterate → constrain
- Decompose tasks to increase reflection (Xu et al., 2024)
- Design workflow to push toward deliberate choices

Stage text:
- Vibe coding → Iterative prompting → Constraint rules → Traditional
- Move left→right: add feedback, then add rules.

---

# Slide 9
## Prompt Anatomy
### Structure prompts for creative code
- Assign a role: creative coder + collaborator
- Constrain the stack: Canvas + vanilla JS
- Declare the look: monochrome, geometric, early-computer
- Require motion + interaction: rAF + input
- Demand a runnable deliverable: single HTML only

Stage text (example prompt scaffold):
- Copy/paste prompt scaffold:
- You are a creative coder.
- Constraints: vanilla JS only; Canvas; full viewport; no external libs.
- Aesthetic: monochrome; geometric; early computer art.
- Tech: requestAnimationFrame; mouse interaction.
- Output: return single HTML only (no markdown/explanation).

---

# Slide 10
## Live Demo
### CUNY AI Lab Sandbox (Open WebUI)
- Open: https://chat.ailab.gc.cuny.edu
- Create an account; await pending approval; then sign in
- Confirm you’re in by posting a 👍 in the chat
- Choose a model: GLM 5 or Kimi K2.5 (MoE)
- Open the Configuration panel (right side)
- Paste the system prompt; set temperature + max tokens
- Optional: model notes: https://ailab.gc.cuny.edu/models

Stage text:
- Run the same prompt 3× at low temp, then 3× at high temp; then force truncation with low max tokens.

---

# Slide 11
## Activity 1 (10m)
### One prompt, one artifact
- Paste the Activity 1 system prompt
- Set temperature 0.9; max tokens 4096
- Write one prompt; generate once; no edits
- Save the HTML; run it locally
- Observe: what did the model assume?  
Artifact: example starfield — move pointer for parallax.

---

# Slide 12
## Activity 2 (15m)
### Iterate and refine
- Switch to the Activity 2 system prompt
- Test the artifact; describe what changed
- Request one change at a time; regenerate
- Complete ≥3 rounds: generate → test → revise
- Keep a log: prompt + parameters + outcome

Stage text:
- Request: “Keep the artifact, but add trails / change palette / add speed control UI.” Re-test each full HTML output.

---

# Slide 13
## Activity 3 (15m)
### Write the rules, not the request
- Write a constraint-based system prompt
- Choose a temperature range; explore variation
- Generate 3 versions; curate your favorite
- Explain your rules like a score or recipe
- Notice how constraints shape the aesthetic

Stage text:
- Copy/paste rules:
- 1) Single HTML with inline CSS+JS
- 2) Canvas only; no libraries
- 3) Grid ≥ 100 elements
- 4) Vary property by distance from center
- 5) Exactly one randomness source
- 6) Only 3 colors
- 7) Fill viewport
- 8) Animate with requestAnimationFrame
- Return HTML only

---

# Slide 14
## Reflection
### Map activities to triangle
- Locate Activity 1 near Interpretation
- Locate Activity 2 between Rules and Interpretation
- Locate Activity 3 near Rules (then curate)
- Ask: what changed—rules, randomness, or judgment?

---

# Slide 15
## Takeaways
### Keep what’s portable
- Teach a progression: one-shot → iterate → constraints
- Save prompts + parameters to reproduce results
- Share artifacts as single-page HTML sketches
- Treat curation as part of the creative act  
Sources live in `expanded.md` (Appendix D).

Stage text:
- Save the recipe:
  - System prompt
  - Model + temperature + max tokens
  - The HTML file (with a date)
