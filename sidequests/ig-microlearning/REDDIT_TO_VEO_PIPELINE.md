# Reddit Data → Veo 3 Prompts: Executive Summary

**Created:** 2026-02-15  
**Pipeline:** Trend Discovery → Visual Storytelling  
**Goal:** Transform trending Reddit content into cinematic video prompts

---

## Overview

Reddit's engagement signals (upvotes, comment depth, cross-posting) reveal what topics resonate with audiences. By systematically mining these signals and translating them into Veo 3-compatible visual prompts, we create an automated pipeline from "what's trending" to "what's watchable."

---

## Data Collection Strategy

### Target Subreddits (Ranked by Educational + Visual Potential)

**Tier 1: High-Quality, Visually Rich**
- `/r/TodayILearned` — 25M+ subscribers, pre-vetted facts, strong visual angles
- `/r/AskHistorians` — Expert-moderated, rich historical imagery potential
- `/r/space` — Stunning imagery, high engagement on discoveries
- `/r/NatureIsFuckingLit` — Viral animal/nature content, perfect for Veo

**Tier 2: Trending + Explainable**
- `/r/explainlikeimfive` — Complex topics simplified, good for educational hooks
- `/r/AskScience` — STEM content with strong visual metaphors
- `/r/todayilearned` — Broad appeal, varied topics

**Tier 3: Niche but High-Engagement**
- `/r/HistoryMemes` — Viral historical moments with humor angle
- `/r/Damnthatsinteresting` — Curated surprising content

### Scraping Parameters

**PRAW (Python Reddit API Wrapper):**
```python
import praw

reddit = praw.Reddit(
    client_id=REDDIT_CLIENT_ID,
    client_secret=REDDIT_SECRET,
    user_agent="IGMicrolearning/1.0"
)

# Fetch top rising posts (highest velocity)
for post in reddit.subreddit("todayilearned").rising(limit=50):
    if post.score > 500 and post.num_comments > 50:
        # High engagement signal
        collect_post(post)
```

**Scrape Frequency:**
- **Hourly:** Check `/rising` for velocity signals
- **Daily:** Aggregate top posts from past 24h for evergreen content
- **Weekly:** Mine `/r/bestof` for cross-posted gems

**Data Structure:**
```json
{
  "post_id": "abc123",
  "title": "TIL that octopuses have three hearts...",
  "score": 12500,
  "upvote_ratio": 0.94,
  "num_comments": 387,
  "created_utc": 1771211890,
  "subreddit": "todayilearned",
  "url": "https://reddit.com/r/todayilearned/comments/abc123",
  "top_comments": [
    "This is wild! I had no idea...",
    "Actually, two pump blood to the gills..."
  ],
  "velocity_score": 8.7,  // upvotes per hour since posting
  "visual_potential": 9.2  // AI-scored richness of visual imagery
}
```

---

## Trend Filtering Algorithm

### Scoring Model

**Engagement Velocity (40% weight):**
```python
velocity = (post.score / hours_since_posted) * upvote_ratio
```
- High velocity = topic is "hot" right now
- Upvote ratio filters out controversial/polarizing topics

**Comment Depth Quality (30% weight):**
```python
comment_quality = (
    avg_comment_length +
    num_top_level_comments +
    num_award_winning_comments
) / num_total_comments
```
- Thoughtful discussion > spam/jokes
- Awards signal community value

**Evergreen Potential (20% weight):**
```python
evergreen_score = topic_model.predict_timelessness(post.title)
```
- "TIL about the Roman aqueduct system" > "TIL about today's stock market"
- Use keyword matching: history, science, nature = high; politics, celebrities = low

**Visual Richness (10% weight):**
```python
visual_potential = vision_llm.score_imagery(post.title + top_comment)
```
- GPT-4V rates: "Can this topic be visualized compellingly in video?"
- Score 1-10:
  - **10:** "bioluminescent jellyfish in the Mariana Trench"
  - **5:** "the history of calculus"
  - **2:** "changes in tax policy"

**Final Trend Score:**
```python
trend_score = (
    0.4 * velocity +
    0.3 * comment_quality +
    0.2 * evergreen_score +
    0.1 * visual_potential
)
```

**Threshold:** Only process posts with `trend_score > 7.0`

---

## Topic → Visual Concept Translation

### Step 1: Extract Core Insight
Use LLM to distill Reddit post + top comments into a single **aha moment**.

**Prompt:**
```
Reddit Post Title: "{post.title}"
Top Comments: "{top_3_comments}"

Extract the ONE core surprising insight that would hook a viewer in 3 seconds.
Format: One sentence, <15 words.

Example: "Octopuses can taste with their arms"
```

### Step 2: Identify Visual Anchors
Map abstract concepts to **concrete, filmable imagery**.

**Mapping Table:**
| Abstract Concept | Visual Anchor |
|------------------|---------------|
| "Evolution" | Time-lapse of organisms morphing |
| "Ancient Rome" | Colosseum, toga-clad senators, marble columns |
| "Quantum physics" | Particle collisions, glowing energy fields |
| "Ocean pressure" | Submersible descending into darkness |
| "Memory formation" | Neurons firing (stylized CGI) |

**LLM Prompt:**
```
Topic: "{core_insight}"

Generate 3 concrete visual scenes that illustrate this concept.
Each scene should include:
- Physical objects (not abstract ideas)
- Setting/environment
- Lighting mood
- Camera movement suggestion

Example:
Scene 1: Close-up of octopus tentacle exploring coral reef, dappled sunlight, slow zoom
Scene 2: Underwater POV of octopus "tasting" a crab shell, dramatic shadows, tracking shot
Scene 3: Split-screen showing octopus arm + human tongue under microscope, clinical lighting, static
```

### Step 3: Craft Veo 3 Prompts

**Template:**
```
{camera_movement} of {subject} in {environment}.
{lighting_description}.
{secondary_element}.
Cinematic, {mood}, 4K quality.
```

**Example Output (from octopus topic):**
```
Prompt 1 (Hook, 3s):
"Extreme close-up tracking shot of octopus tentacle gliding over vibrant coral reef. 
Dappled sunlight filtering through water. 
Tiny suction cups pulse with bioluminescent glow. 
Mysterious, ethereal, cinematic 4K."

Prompt 2 (Explanation, 10s):
"Slow-motion underwater scene of octopus arm wrapping around crab shell. 
Dramatic side lighting creates deep shadows. 
Microscopic view overlay shows chemical receptors firing. 
Scientific, awe-inspiring, 4K quality."

Prompt 3 (Conclusion, 5s):
"Wide aerial shot of octopus camouflaging into rocky ocean floor. 
Golden hour lighting, calm seas. 
Zoom out revealing vast underwater landscape. 
Uplifting, cinematic, 4K quality."
```

---

## Automation Workflow

```
[Reddit API] → [Trend Filter] → [LLM: Extract Insight] → [LLM: Visual Concepts] → [Veo Prompt Generator] → [JSONL Output]
```

**Output Format (`veo_prompts_{timestamp}.jsonl`):**
```jsonl
{"topic": "octopuses_taste_with_arms", "hook_prompt": "Extreme close-up tracking...", "setup_prompts": [...], "conclusion_prompt": "..."}
{"topic": "roman_concrete_stronger", "hook_prompt": "...", "setup_prompts": [...], "conclusion_prompt": "..."}
```

---

## Quality Gates

**Pre-Prompt Generation:**
- [ ] Trend score > 7.0
- [ ] Visual potential score > 6.0 (Veo can't render abstract well)
- [ ] Topic not already covered in past 30 days (avoid repetition)

**Post-Prompt Validation:**
- [ ] Each prompt includes camera movement + lighting + mood
- [ ] No abstract terms like "concept of" or "idea of" (Veo needs concrete nouns)
- [ ] Prompts map 1:1 to script sections (no orphaned visuals)

---

## Example: End-to-End Pipeline

**Input (Reddit Post):**
- Title: "TIL that Cleopatra lived closer in time to the Moon landing than to the construction of the Great Pyramid"
- Score: 15,200 | Comments: 412 | Velocity: 9.1

**Step 1: Core Insight**
> "Cleopatra was born 2,500 years after the pyramids were built, but only 2,000 years before we landed on the moon."

**Step 2: Visual Anchors**
1. Great Pyramid of Giza under construction (ancient workers, massive stones)
2. Cleopatra in palace with scrolls (gold accents, dramatic lighting)
3. Apollo 11 landing on the moon (grainy archival footage style)

**Step 3: Veo Prompts**

```
Hook (3s):
"Slow zoom into Great Pyramid of Giza at sunset, ancient workers hauling stones via wooden sledges. 
Golden hour lighting, dusty atmosphere. 
Time-lapse begins: shadows racing across pyramid faces. 
Epic, historical, cinematic 4K."

Setup (12s):
"Elegant tracking shot through Cleopatra's palace in Alexandria. 
Ornate columns, golden sunlight streaming through silk curtains. 
Cleopatra examining star charts and scrolls. 
Regal, opulent, 4K quality."

Conclusion (10s):
"Wide shot of Apollo 11 lunar module descending to Moon surface. 
Stark gray landscape, Earth rising in background. 
Transition to split-screen: Pyramid → Cleopatra → Moon landing timeline. 
Awe-inspiring, triumphant, 4K."
```

**Output:**
- Script: 160 words (60s voiceover)
- Veo Prompts: 4 scenes (hook + 2 setup + conclusion)
- Estimated Cost: $2.40 (4 Veo generations @ $0.60 each)
- Estimated Engagement: High (surprising fact + strong visual progression)

---

## Success Metrics

**Pipeline Efficiency:**
- **Posts processed:** 50/day (from 500 scraped)
- **Topics validated:** 10/day (pass all quality gates)
- **Prompts generated:** 40/day (4 prompts per topic)

**Content Quality:**
- **Veo success rate:** >85% (generations usable without re-prompting)
- **Visual coherence:** Prompts align with script narrative
- **Audience retention:** >45% watch time on published videos

---

## Risk Mitigation

**Challenge:** Reddit trends are unpredictable (may spike at 3 AM)
**Solution:** Run scraper every hour, queue posts by trend score

**Challenge:** Veo can't render certain concepts well (e.g., "democracy")
**Solution:** Visual potential filter (score > 6.0) rejects abstract topics

**Challenge:** Duplicate topics across subreddits
**Solution:** Deduplicate by semantic similarity (embedding distance threshold)

---

## Next Phase: 10 Candidate Topics

See `CANDIDATE_TOPICS.md` for the first batch of Reddit-sourced ideas ready for script + Veo generation.

**Timeline:**
- ✅ Reddit data pipeline design
- 🔄 Generate 10 candidate topics (in progress)
- ⏳ Build TTS + Veo automation (cron job scheduled)
- ⏳ Publish first test video (ETA: 24h)
