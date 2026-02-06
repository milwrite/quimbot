# TOEFL11 Integration Plan
**Date:** 2026-02-05  
**Purpose:** Leverage learner error patterns for Stage 1 training

---

## Dataset Overview

**TOEFL11 Corpus (LDC2014T06):**
- 12,100 essays from non-native English writers
- 11 L1 backgrounds: Arabic, Chinese, French, German, Hindi, Italian, Japanese, Korean, Spanish, Telugu, Turkish
- Essay length: ~300-600 words
- Proficiency levels: Low-intermediate to high-intermediate

**TOEFL-Spell Annotations:**
- 883 annotated essays (subset of TOEFL11)
- 6,121 spelling error annotations (type M)
- Format: Filename, Offset, Misspelling, Correction
- **Publicly available:** https://github.com/EducationalTestingService/TOEFL-Spell

---

## Access Challenge

**Full TOEFL11 essays:** Gated behind LDC (Linguistic Data Consortium)
- Requires institutional license (universities can purchase)
- **CUNY may already have LDC access** — worth checking with library/research office
- Cost: ~$2,500 for institutional members (one-time)

**Alternative (free):** TOEFL-Spell annotations only
- We have error annotations (misspelling → correction)
- Missing: full essay context
- Can still be useful for error pattern extraction

---

## How TOEFL11 Would Work in Training

### Challenge: Essay Data ≠ Dialogue Data

**Original format (essay):**
```
"In my opinion, technology is very important for modern life. It help us to 
communicate with people around world. For example, we can use internet to 
send email or make video call..."
```

**Needed format (conversational):**
Teacher-student dialogue with error correction scaffolding.

### Conversion Strategy: Essay → Dialogue

**Method 1: Direct Error-Focused Dialogue**
```json
{
  "messages": [
    {"role": "user", "content": "How do you say this in English: Technology help us communicate."},
    {"role": "assistant", "content": "Good try! Just a small correction: 'Technology *helps* us communicate.' Remember, singular subjects take 's' in present tense."},
    {"role": "user", "content": "Oh right! Technology helps us communicate with people around the world."},
    {"role": "assistant", "content": "Perfect! You got it. Around *the* world — nice addition of the article."}
  ]
}
```

**Method 2: Comprehension + Error Patterns**
Extract common L1-specific error patterns and embed in Q&A dialogues:
- Spanish speakers: *ser* vs. *estar* confusion, missing articles
- Chinese speakers: Missing plurals, verb tense issues, article omission
- Arabic speakers: Word order issues, gendered pronoun confusion

### Preprocessing Pipeline

**Step 1: Extract L1-specific error patterns**
```python
# From TOEFL-Spell annotations
errors_by_l1 = {
    "Chinese": [
        {"error": "I have three book", "correction": "I have three books", "pattern": "plural_omission"},
        {"error": "Yesterday I go", "correction": "Yesterday I went", "pattern": "past_tense"}
    ],
    "Spanish": [
        {"error": "She is teacher", "correction": "She is a teacher", "pattern": "article_omission"},
        {"error": "He have car", "correction": "He has a car", "pattern": "verb_agreement"}
    ],
    # ... etc for all 11 L1s
}
```

**Step 2: Generate synthetic dialogues**
Use error patterns to create scaffolded correction dialogues:
```python
templates = [
    # Gentle correction (recast)
    {"user": "{error_sentence}", "assistant": "I think you mean: {corrected}. {explanation}"},
    
    # Explicit correction
    {"user": "{error_sentence}", "assistant": "Good try, but remember: {rule}. So it should be: {corrected}."},
    
    # Encouragement + correction
    {"user": "{error_sentence}", "assistant": "You're on the right track! Just one small change: {corrected}. {encouragement}"}
]
```

**Step 3: Mix with real dialogue data**
Integrate TOEFL11-derived error dialogues at ~10-15% of Stage 1 mix.

---

## If We Get Full TOEFL11 Access

**Additional value:**
1. **Essay-to-dialogue conversion** using full context
2. **Proficiency-based filtering** (beginner vs. intermediate essays)
3. **Topic-based scaffolding** (essays cover education, technology, environment → generate topical conversations)

**Example with full essay context:**
Extract key sentences from essay → convert to Q&A:
```
Essay sentence: "In my country, education is very important because parents want children to have good job."

Generated dialogue:
User: "Why is education important in your country?"
Assistant: "In my country, education is very important because parents want their children to have good jobs."
User: "Oh, I said 'want children to have' — is that wrong?"
Assistant: "Almost! In English, we need 'their' before 'children': 'parents want *their* children.' This shows possession."
```

---

## Implementation Plan

### Option A: With Full TOEFL11 (if CUNY has LDC access)

1. **Check CUNY LDC subscription** (contact library/research office)
2. **Download TOEFL11 corpus** via LDC portal
3. **Link error annotations** to essays (via filename + offset)
4. **Build conversion pipeline:**
   - Extract sentences with errors
   - Generate error-correction dialogues (3-5 turn conversations)
   - Tag with L1 background + proficiency level
5. **Integrate at 15% of Stage 1 mix** (~150K-200K examples)

### Option B: Without Full TOEFL11 (free annotations only)

1. **Use TOEFL-Spell annotations** (already downloaded)
2. **Extract error patterns by L1:**
   - Group errors by native language
   - Identify most common error types (spelling, grammar, articles, etc.)
3. **Generate synthetic error dialogues** using templates
4. **Quality control:** Have native speakers review sample dialogues
5. **Integrate at 5-10% of Stage 1 mix** (~50K-100K examples)

### Option C: Hybrid Approach

1. Use TOEFL-Spell for **error pattern identification**
2. Generate synthetic dialogues based on patterns
3. **Augment with GPT-4** for natural conversation flow:
   - Prompt: "Generate a 3-turn teacher-student dialogue where the student (native Spanish speaker) makes this error: {error}, and the teacher corrects it using the recast method."
   - Filter for quality, remove obvious GPT-isms
4. **Validate with CUNY language faculty** before final integration

---

## Expected Outcomes

**With TOEFL11 integration:**
- Model learns **L1-specific error patterns** (Spanish speakers make different errors than Chinese speakers)
- Can provide **targeted corrections** based on learner background
- Develops **pedagogical scaffolding** (how to correct without discouraging)
- Improves **cross-linguistic awareness** (11 L1s → better generalization)

**Evaluation metrics:**
- Error detection accuracy (can it spot learner mistakes?)
- Correction appropriateness (gentle vs. explicit when needed)
- Encouragement tone (does it maintain student confidence?)

---

## Timeline

**Option A (Full TOEFL11):**
- Week 1: Verify CUNY LDC access
- Week 2: Download corpus, build conversion pipeline
- Week 3: Generate dialogues, quality control
- Week 4: Integrate into Stage 1 training

**Option B (Annotations only):**
- Days 1-2: Extract error patterns from TOEFL-Spell
- Days 3-4: Generate synthetic dialogues, validate
- Day 5: Integrate into Stage 1 mix

**Recommendation:** Start with Option B (free), pursue Option A in parallel (check CUNY LDC access).

---

## Next Steps

1. **Immediate:** Check CUNY LDC subscription status
   - Contact: CUNY Graduate Center Library, Research Data Services
   - Ask: "Does CUNY have institutional access to LDC resources?"

2. **Fallback:** Build error pattern extraction script from TOEFL-Spell
   - Parse Annotations.csv
   - Group by L1 (requires linking to TOEFL11 metadata — may need to infer)

3. **Quality check:** Share sample synthetic dialogues with CUNY language faculty
   - Get feedback on pedagogical appropriateness
   - Iterate on templates

---

**Status:** Plan complete. Awaiting decision on LDC access pursuit.  
**Last Updated:** 2026-02-05 22:12 EST by Petrarch 🜁
