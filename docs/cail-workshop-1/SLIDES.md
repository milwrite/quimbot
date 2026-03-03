# SLIDES.md — CAIL Spotlight Workshop #1
## Foundations: Coding with Generative AI

Companion to `index.html`. Keep this file in sync whenever slide titles or text content change.
Upstream source: <https://github.com/CUNY-AI-Lab/gen-dev-foundations>
Live deck: <https://cuny-ai-lab.github.io/gen-dev-foundations/>

---

## Slide 1 — Title (`data-slide="title"`)

**Label:** CAIL Spotlight Workshop #1
**Title:** Foundations: Coding with Generative AI
**Stage:** Noll quadratic artifact (`../gallery/noll.html`)

---

## Slide 2 — Agenda (`data-slide="agenda"`)

**Label:** Workshop
**Title:** Agenda

---

## Slide 3 — Section Break: Part 1 (`data-slide="part1"`)

**Tag:** Part 1
**Title:** Concepts & Context

---

## Slide 4 — Icebreaker (`data-slide="icebreaker"`)

**Label:** Icebreaker · 10 min
**Title:** Where does coding live in your imagination?
**Subtitle:** Pick one. Talk to a neighbor.

**Stage cards:** Q1–Q5 _(content in index.html)_

---

## Slide 5 — Demo (`data-slide="demo"`)

**Label:** Demo
**Title:** Vibe Coding in Action

---

## Slide 6 — LLM Concept (`data-slide="llm"`)

**Label:** Concept
**Title:** What is a Large Language Model (LLM)?

---

## Slide 7 — LLM Process (`data-slide="llm-process"`)

**Label:** Concept
**Title:** How Does an LLM Actually Produce an Answer?

---

## Slide 8 — Code Generation (`data-slide="code-generation"`)

**Label:** Concept
**Title:** How Do LLMs Generate Code?

---

## Slide 9 — Good / Bad (`data-slide="good-bad"`)

**Label:** Concept
**Title:** What's Good / What's Bad

---

## Slide 10 — Section Break: Part 2 (`data-slide="part2"`)

**Tag:** Part 2
**Title:** Development Environment

---

## Slide 11 — VS Code Intro (`data-slide="vscode-intro"`)

**Label:** Concept
**Title:** What is VS Code?

---

## Slide 12 — VS Code Setup (`data-slide="vscode"`)

**Label:** Setup
**Title:** Setting up an Interactive Development Environment

**Stage steps:**
1. Download + install VS Code
2. Sign in with your GitHub profile
3. Add the GitHub extension; start tracking your project
4. Open the integrated terminal — this is where CLI + Git live

_(TODO: unpack each step more concretely — download link, OS variants, exact extension names, keyboard shortcut for terminal)_

---

## Slide 13 — CLI Intro (`data-slide="cli-intro"`)

**Label:** Concept
**Title:** What is the Command Line?

---

## Slide 14 — Opening Terminal (`data-slide="cli-open"`)

**Label:** Outside VS Code
**Title:** Opening a Standalone Terminal

---

## Slide 15 — CLI Navigation (`data-slide="cli-nav"`)

**Label:** Tool
**Title:** Command Line Basics
_(navigation: pwd, ls, cd, mkdir)_

---

## Slide 16 — CLI File Ops (`data-slide="cli-files"`)

**Label:** Tool
**Title:** Command Line Basics
_(file ops: touch, mv, cp, rm, cat)_

---

## Slide 17 — Git Intro (`data-slide="git-intro"`)

**Label:** Concept
**Title:** What is Git? What is GitHub?

---

## Slide 18 — Git Setup (`data-slide="git-setup"`)

**Label:** Tool
**Title:** Git Basics
_(init, add, commit)_

---

## Slide 19 — Git Sync (`data-slide="git-sync"`)

**Label:** Tool
**Title:** Git Basics
_(push, pull, log, status, diff)_

---

## Slide 20 — GitHub Login (`data-slide="gh-login"`)

**Label:** Setup
**Title:** Logging into GitHub

**Stage steps:**
1. Install GitHub CLI: `brew install gh` (macOS) / `winget install GitHub.cli` (Windows)
2. Start login: `gh auth login`
3. Choose GitHub.com → HTTPS → Login with a web browser
4. Copy the one-time code, press Enter, approve in browser
5. Confirm: `✓ Logged in as your-username`

---

## Slide 21 — GitHub Repo (`data-slide="gh-repo"`)

**Label:** Setup
**Title:** Staging, Committing, and Pushing to GitHub

**Stage steps:**
_(git init covered on git-setup slide)_
1. Create your first file: `touch README.md`
2. Stage and commit: `git add . && git commit -m "first commit"`
3. Publish to your GitHub: `gh repo create my-project --public --source=. --push`
4. Add the CUNY AI Lab remote and push:
   `git remote add origin https://github.com/cuny-ai-lab/my-project`
   `git push -u origin main` → [github.com/cuny-ai-lab](https://github.com/cuny-ai-lab)

---

## Slide 22 — Section Break: Part 3 (`data-slide="part3"`)

**Tag:** Part 3
**Title:** Installation & Setup

---

## Slide 23 — Install Gemini CLI (`data-slide="install"`)

**Label:** Setup
**Title:** Installing Gemini CLI

---

## Slide 24 — Login (`data-slide="login"`)

**Label:** Setup
**Title:** Login Step

---

## Slide 25 — Troubleshooting (`data-slide="troubleshoot"`)

**Label:** Check-in
**Title:** Troubleshooting

---

## Slide 26 — Next Steps (`data-slide="nextsteps"`)

**Label:** What's Next
**Title:** Upcoming Workshop

---

## Slide 27 — Resources (`data-slide="resources"`)

**Label:** Resources
**Title:** Links & References

**Workshop decks:**
- [cuny-ai-lab.github.io/gen-dev-foundations](https://cuny-ai-lab.github.io/gen-dev-foundations/) — this deck (live)
- [github.com/CUNY-AI-Lab/gen-dev-foundations](https://github.com/CUNY-AI-Lab/gen-dev-foundations) — source repo
- [cuny-ai-lab.github.io/Vibe-Coding-Workshop](https://cuny-ai-lab.github.io/Vibe-Coding-Workshop/) — companion deck

---

_Last synced: 2026-03-02. Upstream: CUNY-AI-Lab/gen-dev-foundations @ main. Update both files together._
