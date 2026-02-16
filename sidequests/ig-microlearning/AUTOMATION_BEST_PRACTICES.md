# IG Microlearning Video Automation — Best Practices

**Created:** 2026-02-15  
**Owner:** Petrarch  
**Status:** Design Phase

---

## Executive Summary

Automated short-form educational video production for Instagram requires orchestration across:
- **Trend discovery** (Reddit API → trending topics)
- **Script generation** (LLM → concise educational hooks)
- **Voiceover synthesis** (ElevenLabs TTS → human-quality narration)
- **Video generation** (Google Veo 3 → visual storytelling)
- **Post-production** (FFmpeg → assembly, captions, branding)
- **Publishing** (Instagram Graph API → scheduled posts)

This document establishes design principles for maximum throughput, quality, and scalability.

---

## Core Design Principles

### 1. **Modular Pipeline Architecture**
Each stage should be independently testable and replaceable:
```
[Reddit Scraper] → [Trend Filter] → [Script Generator] → [TTS Engine] → [Veo Prompter] → [Video Assembler] → [Publisher]
```

**Why:**
- Swap Reddit for X/Twitter/TikTok trends without rewriting downstream logic
- Test script quality before burning Veo credits
- Retry failed video generations without re-running TTS

**Implementation:**
- Use JSONL pipelines for data flow between stages
- Store intermediate artifacts (scripts, audio, raw video) in timestamped directories
- Each stage logs inputs/outputs for debugging

---

### 2. **Trend Discovery → Topic Validation**
Not all trending topics make good 60-second educational videos.

**Filtering Criteria:**
- **Velocity:** Rising engagement (upvotes/hour growth rate)
- **Evergreen potential:** Topic remains relevant beyond 24 hours
- **Educational angle:** Can be explained with a clear hook + 3 key points
- **Visual richness:** Veo can generate compelling imagery (avoid abstract concepts like "inflation rates")

**Data Sources (Ranked):**
1. **Reddit `/r/TodayILearned`** — Pre-vetted for educational value
2. **Reddit `/r/explainlikeimfive`** — High engagement, accessible language
3. **Reddit `/r/AskScience`, `/r/AskHistorians`** — Deep expertise, credibility
4. **X/Twitter Trending** — Real-time, but noisy (requires heavier filtering)

**Scoring Model:**
```python
trend_score = (
    0.4 * engagement_velocity +
    0.3 * comment_depth_quality +
    0.2 * evergreen_score +
    0.1 * visual_potential
)
```

---

### 3. **Script Generation → Retention Optimization**
Instagram users scroll fast. First 3 seconds determine watch-through rate.

**Hook Patterns (Proven High-Retention):**
- **Surprising fact:** "90% of people don't know this about..."
- **Common misconception:** "You've been lied to about..."
- **Historical mystery:** "In 1945, something bizarre happened..."
- **Counterfactual:** "What if I told you X is actually Y?"

**Structure (60 seconds):**
```
0-3s:   Hook (question or surprising statement)
3-15s:  Setup (context, why it matters)
15-45s: Explanation (3 key points, each 10s)
45-55s: Conclusion (aha moment, payoff)
55-60s: CTA ("Follow for more" or "Comment your thoughts")
```

**LLM Prompt Template:**
```
You are writing a 60-second educational Instagram video script.

Topic: {reddit_post_title}
Context: {top_3_comments}

Requirements:
- Hook in first 3 seconds (surprising or counterintuitive)
- Exactly 150-180 words (60s at conversational pace)
- 3 key points, each 1 sentence
- Conclude with aha moment
- Avoid jargon; write for general audience

Output format:
HOOK: [3-second opener]
SETUP: [context]
POINT_1: [insight]
POINT_2: [insight]
POINT_3: [insight]
CONCLUSION: [payoff]
CTA: [engagement prompt]
```

---

### 4. **TTS Integration → Natural Delivery**
Robotic voiceovers kill engagement. ElevenLabs delivers near-human quality.

**Voice Selection:**
- **Educational content:** Use "Josh" or "Rachel" (neutral, trustworthy)
- **Story-driven:** Use "Bella" (warm, narrative)
- **Science/tech:** Use "Adam" (authoritative, clear)

**Delivery Optimization:**
- Insert `<break time="500ms"/>` after hook for dramatic pause
- Use `<emphasis>` tags on key numbers or surprising facts
- Set `stability=0.6, clarity=0.8` for conversational naturalness

**API Call:**
```python
from elevenlabs import generate, Voice

audio = generate(
    text=script,
    voice=Voice(voice_id="dAlhI9qAHVIjXuVppzhW"),  # From TOOLS.md
    model="eleven_multilingual_v2",
    stability=0.6,
    clarity_boost=True
)
```

**Output:** `audio/{timestamp}_{topic_slug}.mp3`

---

### 5. **Veo 3 Prompting → Visual Storytelling**
Veo 3 generates cinematic video from text. Quality depends on prompt specificity.

**Prompt Engineering Best Practices:**

**DO:**
- Specify camera movement ("slow zoom in," "tracking shot," "aerial view")
- Define lighting ("golden hour," "dramatic shadows," "soft natural light")
- Include concrete objects ("ancient manuscript," "bustling marketplace," "laboratory beaker")
- Set mood/tone ("mysterious," "uplifting," "tense")

**DON'T:**
- Use abstract concepts ("the economy," "democracy") — Veo needs physical imagery
- Overload with details (max 3-4 visual elements per prompt)
- Request text overlays (Veo doesn't render readable text reliably)

**Example Prompt (Good):**
```
A slow tracking shot through an ancient Egyptian library at sunset. 
Dust particles float in golden light streaming through stone windows. 
A weathered papyrus scroll unfurls on a wooden table. 
Cinematic, 4K quality, mysterious atmosphere.
```

**Example Prompt (Bad):**
```
Show the concept of knowledge being preserved across millennia.
```

**Prompt Template for Educational Videos:**
```
{camera_movement} showing {concrete_subject} in {setting}. 
{lighting_description}. 
{secondary_visual_element}. 
{mood}, cinematic quality, {duration} seconds.
```

**Mapping Script → Visuals:**
Each script section should map to 1-2 Veo generations:
- **Hook (3s):** Attention-grabbing establishing shot
- **Setup (12s):** Context-setting sequence (2 clips)
- **Points 1-3 (30s):** One visual per point (3 clips)
- **Conclusion (10s):** Satisfying payoff shot
- **CTA (5s):** Simple branded outro

**Budget:** 6-8 Veo generations per video (~$2-3 per video at current pricing)

---

### 6. **Assembly → Automated Editing**
FFmpeg stitches audio + video + captions.

**Workflow:**
1. Align TTS audio to script timestamps
2. Generate SRT captions (Whisper or ElevenLabs transcription API)
3. Overlay captions with high-contrast styling (white text, black stroke)
4. Add subtle background music (royalty-free from Epidemic Sound)
5. Insert 1-second branded intro/outro card

**FFmpeg Command:**
```bash
ffmpeg -i video_concatenated.mp4 -i voiceover.mp3 -i music.mp3 \
  -filter_complex "[1:a]volume=1.0[vo];[2:a]volume=0.2[bg];[vo][bg]amix=inputs=2[audio]" \
  -map 0:v -map "[audio]" \
  -vf "subtitles=captions.srt:force_style='FontName=Montserrat,FontSize=24,Bold=1,PrimaryColour=&HFFFFFF&,OutlineColour=&H000000&,Outline=2'" \
  -c:v libx264 -preset fast -crf 23 -c:a aac -b:a 128k \
  output.mp4
```

**Validation:**
- Duration exactly 60s ± 2s
- Audio levels: -3dB to -6dB (not clipping)
- Resolution: 1080x1920 (Instagram Reels optimal)
- Aspect ratio: 9:16 (vertical)

---

### 7. **Publishing → Scheduled Automation**
Instagram Graph API for automated posting.

**Scheduling Strategy:**
- **Best times:** 11AM-1PM, 7PM-9PM EST (peak engagement)
- **Frequency:** 1-2 videos/day (avoid spam throttling)
- **Hashtags:** 5-8 relevant tags (e.g., #TodayILearned, #ScienceFacts, #History)

**API Call:**
```python
import requests

url = f"https://graph.facebook.com/v18.0/{ig_user_id}/media"
payload = {
    "video_url": "https://yourdomain.com/videos/output.mp4",
    "caption": f"{hook_text}\n\n{hashtags}",
    "access_token": IG_ACCESS_TOKEN
}
response = requests.post(url, data=payload)
creation_id = response.json()["id"]

# Publish
publish_url = f"https://graph.facebook.com/v18.0/{ig_user_id}/media_publish"
requests.post(publish_url, data={"creation_id": creation_id, "access_token": IG_ACCESS_TOKEN})
```

---

## Quality Checkpoints

**Pre-Generation Validation:**
- [ ] Script passes readability test (Flesch-Kincaid Grade 8-10)
- [ ] Veo prompts include camera movement + lighting + mood
- [ ] TTS audio duration matches script target (58-62s)

**Post-Generation Validation:**
- [ ] Video contains no visible artifacts or glitches
- [ ] Audio sync is accurate (no drift >100ms)
- [ ] Captions are readable and correctly timed
- [ ] Final file size <100MB (Instagram upload limit)

**A/B Testing:**
Track which hook patterns, voice styles, and visual themes drive highest retention.

---

## Error Handling

**Common Failure Modes:**
1. **Veo generation timeout** → Retry with simplified prompt (remove secondary elements)
2. **TTS audio clipping** → Reduce stability parameter, add pauses
3. **Caption misalignment** → Re-run Whisper transcription with `--word_timestamps`
4. **Instagram API rate limit** → Queue posts with 10-minute spacing

**Logging:**
Every stage writes to `logs/pipeline_{timestamp}.jsonl`:
```jsonl
{"stage": "trend_discovery", "status": "success", "trends_found": 47, "timestamp": 1771211890}
{"stage": "script_generation", "status": "success", "script_id": "xyz123", "word_count": 165}
{"stage": "veo_generation", "status": "retry", "attempt": 2, "error": "timeout"}
```

---

## Success Metrics

**Leading Indicators:**
- **Pipeline uptime:** >95% (stages complete without manual intervention)
- **Cost per video:** <$5 (Veo + ElevenLabs + API calls)
- **Time to publish:** <30 minutes from trend detection to posted video

**Lagging Indicators (Instagram Analytics):**
- **Average watch time:** >40% (24s of 60s video)
- **Engagement rate:** >5% (likes + comments / views)
- **Follower growth:** +2-5% weekly

---

## Next Steps

1. ✅ Document automation architecture
2. 🔄 Create 10 candidate topic ideas from Reddit data
3. ⏳ Build TTS + Veo prompt pipeline (cron job)
4. ⏳ Assemble first test video end-to-end
5. ⏳ Deploy scheduled posting automation

**Owner:** Petrarch  
**Timeline:** 7 days to MVP (first 10 videos published)
