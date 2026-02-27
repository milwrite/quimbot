---
theme: default
title: LLMQuery Test Deck
---

# LLMQuery Test Deck

<ConfigPanel />

---
layout: default
---

# Code Review Demo (Live Sync Test)

<LLMQuery
  model="anthropic/claude-sonnet-4"
  position="top-right"
  system-prompt="You are a senior code reviewer. Keep responses under 10 lines."
  prompt="Review this code for bugs and improvements"
  :auto-execute="true"
>

```python
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

for i in range(40):
    print(f"fib({i}) = {fibonacci(i)}")
```

</LLMQuery>

---
layout: default
---

# What is a Transformer?

<LLMQuery
  model="openai/gpt-4.1-mini"
  position="top-left"
  system-prompt="Explain concisely in 3 sentences"
  :auto-execute="false"
/>

<LLMQuery
  model="anthropic/claude-sonnet-4"
  position="top-right"
  system-prompt="Explain with a metaphor"
  :auto-execute="false"
/>

<LLMQuery
  model="google/gemini-2.5-pro"
  position="bottom-left"
  system-prompt="Focus on the math"
  :auto-execute="false"
/>

<LLMQuery
  model="x-ai/grok-4"
  position="bottom-right"
  system-prompt="Explain like I'm 5"
  :auto-execute="false"
/>

## The architecture behind modern LLMs

Compare how different models explain the same concept!


---
layout: default
---

# Creative Coding Fundamentals

<LLMQuery
  model="google/gemini-2.5-flash"
  position="top-right"
  system-prompt="You are a creative coding instructor. Keep answers short and practical with code examples."
  :auto-execute="false"
>

- **Noise functions** — Perlin, Simplex, Worley
- **L-Systems** — recursive string rewriting for organic forms
- **Particle systems** — emergent behavior from simple rules
- **Flow fields** — vector fields that guide movement

*Ask the AI to explain any of these with a p5.js example!*

</LLMQuery>

