# Multilingual & Dialect-Specific Datasets for Secondary Fine-Tuning
**Research Date:** 2026-02-04  
**Purpose:** Identify datasets for secondary LoRA fine-tuning to cover linguistically native and dialect-specific conversational patterns

---

## Overview: Secondary Fine-Tuning Strategy

After initial training on general conversational datasets, apply **secondary fine-tuning** with multilingual and dialect-specific data to:
1. **Linguistic diversity:** Native speaker patterns across languages
2. **Code-switching competence:** Handle bilingual/multilingual conversations
3. **Dialect awareness:** Regional varieties within languages
4. **Cultural context:** Sociolinguistic norms and communication styles

**Approach:** Train base LoRA → Fine-tune with dialect/multilingual mix → Evaluate cross-lingual transfer

---

## Dataset 1: SwitchLingua (Code-Switching - 11 Languages)
**Location:** `Shelton1013/SwitchLingua_text` (HuggingFace)  
**Link:** https://huggingface.co/datasets/Shelton1013/SwitchLingua_text  
**Size:** 420K textual samples + 80+ hours audio  
**Languages:** Arabic, Cantonese, French, German, Hindi, Italian, Japanese, Korean, Mandarin, Russian, Spanish  
**License:** Gated (requires agreement) | NeurIPS 2025 dataset  
**Format:** Multi-turn conversations with code-switching annotations

**Training Approach:**
```python
from datasets import load_dataset
cs_data = load_dataset("Shelton1013/SwitchLingua_text")
```

**Code-Switching Details:**
- **Generation Framework:** LinguaMaster (fluency, naturalness, CS ratio agents)
- **Scoring:** Each sample scored for quality (0-10)
- **Metadata:** Includes CS type, CS ratio, social/cultural context, speaker demographics
- **Audio:** 174 bilingual speakers from diverse backgrounds

**Linguistic Coverage:**
- **11 language pairs** with English as pivot
- **Intra-sentential CS:** Switches within sentences (tests syntactic alignment)
- **Inter-sentential CS:** Switches between sentences
- **Social markers:** Gender, education, age, tense, perspective annotated

**Diversification Value:**
- **Authentic bilingualism:** Models real code-switching patterns
- **Cross-linguistic transfer:** Teaches syntactic/semantic alignment across languages
- **Cultural context:** Social/cultural metadata enriches pragmatic understanding
- **Quality control:** LinguaMaster framework ensures natural CS (not random)

**Pros:**
- Large scale (420K samples)
- High-quality curation (scored by agents)
- Rich metadata (demographics, CS type)
- Audio available (multimodal option)
- Covers major world languages

**Cons:**
- Gated access
- AI-generated (LinguaMaster framework - not entirely natural)
- English-centric (all pairs include English)

---

## Dataset 2: CS-FLEURS (Massively Multilingual Code-Switching)
**Location:** `byan/cs-fleurs` (HuggingFace)  
**Link:** https://huggingface.co/datasets/byan/cs-fleurs  
**Size:** 300 hours speech | 113 unique CS pairs across 52 languages  
**License:** CC BY 4.0 (Non-Commercial)  
**Format:** Audio + transcriptions (read + synthetic TTS)

**Training Approach:**
```python
from datasets import load_dataset
cs_fleurs = load_dataset("byan/cs-fleurs")
```

**Subsets:**
1. **Read-Test:** 14 X-English pairs (read speech) - 17 hours
2. **XTTS-Train:** 16 X-English pairs (generative TTS) - 128 hours
3. **XTTS-Test1:** 16 X-English pairs (generative TTS) - 36 hours
4. **XTTS-Test2:** 60 {Arabic, Chinese, Hindi, Spanish}-X pairs (generative TTS) - 42 hours
5. **MMS-Test:** 45 X-English pairs (concatenative TTS) - 56 hours

**Script Diversity:**
- **Same-script pairs:** 49 total (e.g., Spanish-English)
- **Distinct-script pairs:** 87 total (e.g., Arabic-English, Chinese-English)

**Diversification Value:**
- **Massive scale:** 113 language pairs (largest CS coverage)
- **Script diversity:** Tests cross-script CS handling
- **Synthetic + read:** Mix of TTS and human speech
- **Global coverage:** 52 languages across continents

**Pros:**
- Largest CS dataset by language pair count
- CC BY 4.0 license
- Script diversity (cross-alphabet CS)
- Well-structured subsets (train/test splits)

**Cons:**
- Non-commercial license (CC BY 4.0 NC clause)
- Heavy TTS component (less natural than human speech)
- Focused on ASR/TTS tasks (may need adaptation for conversational AI)

---

## Dataset 3: Google WAXAL (African Languages - 19 Languages)
**Location:** `google/WaxalNLP` (HuggingFace)  
**Link:** https://huggingface.co/datasets/google/WaxalNLP  
**Size:** 1,250 hours ASR + 180 hours TTS  
**Languages (ASR):** Acholi, Luganda, Masaaba, Nyankole, Soga, Akan, Ewe, Dagbani, Dagaare, Ikposo, Fula, Lingala, Shona, Malagasy, Amharic, Oromo, Sidama, Tigrinya, Wolaytta  
**Languages (TTS):** Acholi, Luganda, Kiswahili, Nyankole, Akan (Fante, Twi), Fula, Igbo, Hausa, Yoruba, Kikuyu, Luo  
**License:** CC-BY-4.0 / CC-BY-SA-4.0 (varies by provider)  
**Format:** Audio + transcriptions (ASR) | Phonetically balanced scripts (TTS)

**Training Approach:**
```python
from datasets import load_dataset
# Load Shona ASR dataset
waxal_shona = load_dataset("google/WaxalNLP", "sna_asr")
```

**Provider Partnerships:**
- **Makerere University:** Ugandan languages (Acholi, Luganda, etc.)
- **University of Ghana:** Ghanaian languages (Akan, Ewe, etc.)
- **Digital Umuganda:** East/Southern African languages (Fula, Lingala, Amharic, etc.)
- **Media Trust:** West African languages (Hausa, Yoruba, Igbo, Fula)

**Diversification Value:**
- **Underrepresented languages:** First large-scale corpus for many African languages
- **Linguistic diversity:** Niger-Congo, Afroasiatic, Nilo-Saharan families
- **Cultural preservation:** Digital archiving of endangered languages
- **100M+ speakers:** Covers 40 Sub-Saharan African countries

**Pros:**
- **Brand new (released 2 days ago!)**
- Permissive licenses (CC-BY/CC-BY-SA)
- High-quality transcriptions
- Massive speaker diversity (natural speech)
- Google/Gates Foundation backing (trusted source)

**Cons:**
- Focused on ASR/TTS (may need conversational context adaptation)
- Smaller conversational coverage (more isolated utterances than dialogues)

---

## Dataset 4: Nexdata Chinese Dialects (25,000 Hours)
**Location:** `Nexdata/chinese_dialect` (HuggingFace - sample)  
**Link:** https://huggingface.co/datasets/Nexdata/chinese_dialect  
**Size:** 25,000 hours (PAID dataset - HF has sample)  
**Dialects:** Hokkien, Cantonese, Sichuan, Henan, Northeastern, Shanghai, Uyghur, + more  
**License:** Proprietary (sample available for preview)  
**Format:** Audio + transcriptions from local dialect speakers

**Training Approach:**
- **Sample available:** Test with free sample, evaluate ROI for paid access
- **Alternative:** Use open Cantonese/Mandarin datasets separately

**Diversification Value:**
- **Dialect depth:** 7+ major Chinese dialect families
- **Regional accents:** 26+ regional variations
- **Massive scale:** 25K hours (largest Chinese dialect corpus)
- **Authentic speakers:** Local native speakers (not Mandarin speakers imitating dialects)

**Pros:**
- Unmatched scale for Chinese dialects
- Authentic local speakers
- Covers mutually unintelligible varieties (Cantonese ≠ Mandarin)

**Cons:**
- **PAID dataset** (licensing required)
- Sample only on HuggingFace (not full access)
- No pricing information visible

**Open Alternatives:**
- **KeSpeech:** Mandarin + 8 subdialects (free, OpenReview)
- **Cantonese-Traditional Chinese Parallel Corpus:** `raptorkwok/cantonese-traditional-chinese-parallel-corpus`

---

## Dataset 5: XTREME-S (Multilingual Speech - 52 Languages)
**Location:** `google/xtreme_s` (HuggingFace)  
**Link:** https://huggingface.co/datasets/google/xtreme_s  
**Size:** Varies by subset (multilingual speech benchmark)  
**Languages:** Includes South-East Asian (Burmese, Cebuano, Filipino, Indonesian, Javanese, Khmer, Lao, Malay, Maori, Thai, Vietnamese) + CJK (Cantonese, Mandarin, Japanese, Korean) + more  
**License:** Apache 2.0 (check individual subsets)  
**Format:** Multi-task benchmark (ASR, translation, retrieval, etc.)

**Training Approach:**
```python
from datasets import load_dataset
xtreme = load_dataset("google/xtreme_s", "mls.tha")  # Thai subset example
```

**Diversification Value:**
- **Global coverage:** 52 languages across continents
- **Multi-task:** ASR, speech translation, retrieval, classification
- **Low-resource focus:** Includes underrepresented languages
- **Benchmark quality:** Google-curated standardized tasks

**Pros:**
- Apache 2.0 license (open)
- Well-documented benchmark
- Includes low-resource Asian languages (Khmer, Lao, Burmese)
- Multi-task evaluation framework

**Cons:**
- Not conversational (task-oriented)
- Requires subset selection (large, complex structure)
- Some subsets may be small

---

## Dataset 6: ASR-BPCSC (Brazilian Portuguese Conversational)
**Location:** MagicHub / GitHub (Nexdata)  
**Link:** https://magichub.com/datasets/brazilian-portuguese-conversational-speech-corpus/  
**Size:** 10 hours (open-source) | 104 hours (Nexdata paid version)  
**Language:** Brazilian Portuguese (pt-BR)  
**License:** Open-source (check MagicHub terms)  
**Format:** Transcribed conversational speech (30 conversations, 5 speaker pairs)

**Training Approach:**
- **Open version:** 10 hours from MagicHub
- **Paid version:** 104 hours via Nexdata GitHub

**Diversification Value:**
- **Dialect-specific:** Brazilian Portuguese (vs European Portuguese)
- **Conversational:** True dialogues (not read speech)
- **Topic diversity:** Multiple conversation topics
- **Natural speech:** Spontaneous conversations (includes disfluencies)

**Pros:**
- Conversational format (directly applicable)
- Dialect specificity (Brazilian vs European)
- Open-source option available

**Cons:**
- Small scale (10 hours open-source)
- Limited speaker diversity (5 pairs)
- Paid version needed for larger scale

**Complement With:**
- **brwac corpus:** `UFRGS/brwac` (Brazilian Portuguese web corpus - text-only)
- **Falabrasil ASR datasets:** Multiple open Brazilian Portuguese speech datasets

---

## Dataset 7: Chilean Spanish TTS (Latin American Spanish)
**Location:** `ylacombe/google-chilean-spanish` (HuggingFace)  
**Link:** https://huggingface.co/datasets/ylacombe/google-chilean-spanish  
**Size:** TBD (check dataset card)  
**Language:** Chilean Spanish (Latin American variety)  
**License:** CC-BY-4.0 (likely - check card)  
**Format:** TTS recordings (phonetically balanced)

**Training Approach:**
```python
from datasets import load_dataset
chilean_es = load_dataset("ylacombe/google-chilean-spanish")
```

**Diversification Value:**
- **Latin American Spanish:** Chilean accent (distinct from European Spanish)
- **Low-resource dialect:** Underrepresented in most datasets
- **Google-backed:** High-quality recordings
- **Regional identity:** Captures Chilean phonetics and lexicon

**Pros:**
- Latin American Spanish representation
- Google Crowdsourcing project (quality assured)
- Permissive license

**Cons:**
- TTS focus (read speech, not conversational)
- Single dialect (Chilean - not Pan-Latin American)

**Complement With:**
- **Common Voice Spanish:** Multiple Latin American accents (Mexico, Colombia, Argentina, etc.)
- **CORAA:** Spanish conversational datasets

---

## Dataset 8: Masakhane AfriQA (10 African Languages)
**Location:** `masakhane/afriqa` (HuggingFace)  
**Link:** https://huggingface.co/datasets/masakhane/afriqa  
**Size:** 12,000+ XOR QA examples across 10 languages  
**Languages:** TBD (Swahili, Yoruba, Hausa likely included)  
**License:** Open (check dataset card)  
**Format:** Cross-lingual QA (question-answer pairs)

**Training Approach:**
```python
from datasets import load_dataset
afriqa = load_dataset("masakhane/afriqa")
```

**Diversification Value:**
- **African language QA:** Extends beyond ASR/TTS to conversational understanding
- **Cross-lingual:** XOR (cross-lingual open retrieval) format
- **10 languages:** Broad African language coverage
- **Masakhane project:** Community-driven (high cultural authenticity)

**Pros:**
- Conversational QA format (applicable to dialogue)
- Open-source
- Community-driven (Masakhane = "we build together")
- Train/val/test splits included

**Cons:**
- QA format (not free-form dialogue)
- May need adaptation for conversational flow

---

## Dataset 9: Swahili Words Speech-Text Parallel
**Location:** `michsethowusu/swahili-words-speech-text-parallel` (HuggingFace)  
**Link:** https://huggingface.co/datasets/michsethowusu/swahili-words-speech-text-parallel  
**Size:** 411,048 parallel speech-text pairs  
**Language:** Swahili (East African lingua franca)  
**License:** TBD (check card)  
**Format:** Audio + text pairs (word-level)

**Training Approach:**
```python
from datasets import load_dataset
swahili = load_dataset("michsethowusu/swahili-words-speech-text-parallel")
```

**Diversification Value:**
- **Swahili:** 100M+ speakers across East Africa
- **Large scale:** 411K pairs (substantial coverage)
- **Multimodal:** Audio-text alignment
- **Regional importance:** Swahili is official in Kenya, Tanzania, Uganda

**Pros:**
- Large scale (411K pairs)
- Swahili is major African lingua franca
- Multimodal training option

**Cons:**
- Word-level (not sentence/dialogue-level)
- May need aggregation for conversational context

---

## Dataset 10: Fun-ASR Multilingual (31 Languages + Dialects)
**Location:** GitHub - FunAudioLLM/Fun-ASR  
**Link:** https://github.com/FunAudioLLM/Fun-ASR  
**Size:** Varies (models + datasets)  
**Languages:** Cantonese, Japanese, Korean, Vietnamese, Indonesian, Thai, Malay, Filipino, Arabic, Hindi, + 21 more  
**Chinese Dialects:** Wu, Cantonese, Min, Hakka, Gan, Xiang, Jin + 26 regional accents  
**License:** Open-source (check GitHub)  
**Format:** End-to-end ASR models + datasets

**Training Approach:**
- Use Fun-ASR's datasets or pre-trained models for transfer learning
- Supports 31 languages + extensive Chinese dialect coverage

**Diversification Value:**
- **Asian language depth:** Extensive coverage (CJK + SEA + South Asian)
- **Chinese dialect richness:** 7 families + 26 regional accents
- **Specialized features:** Lyric recognition, rap speech (creative language use)
- **Multilingual backbone:** Can bootstrap from pre-trained models

**Pros:**
- **Comprehensive Asian coverage**
- Chinese dialect depth unmatched
- Open-source
- Pre-trained models available (transfer learning)

**Cons:**
- GitHub-based (not standardized HuggingFace format)
- Documentation may be in Chinese
- Dataset access varies by component

---

## Secondary Fine-Tuning Strategy

### Phase 1: Code-Switching Foundation
**Datasets:** SwitchLingua + CS-FLEURS  
**Duration:** 20-30% of initial training time  
**Goal:** Teach bilingual/multilingual conversation handling

**Training Mix:**
- 60% SwitchLingua (high-quality, scored samples)
- 40% CS-FLEURS (massively multilingual coverage)

**Rationale:**
- SwitchLingua provides **quality** (LinguaMaster framework)
- CS-FLEURS provides **breadth** (113 pairs, 52 languages)

---

### Phase 2: Regional Dialect Specialization
**Datasets:** WAXAL (African) + Nexdata/KeSpeech (Chinese) + Brazilian Portuguese + Chilean Spanish  
**Duration:** 30-40% of initial training time  
**Goal:** Capture regional varieties within language families

**Training Mix:**
- 40% WAXAL (African languages - high priority for underrepresentation)
- 30% Chinese dialects (KeSpeech open-source or Nexdata sample)
- 20% Brazilian Portuguese (ASR-BPCSC + brwac)
- 10% Latin American Spanish (Chilean + Common Voice LATAM)

**Rationale:**
- **African languages:** Largest underserved population (WAXAL brand new, high quality)
- **Chinese dialects:** Mutually unintelligible varieties (Cantonese ≠ Mandarin)
- **Portuguese/Spanish:** Dialect divergence (Brazilian vs European, Chilean vs Iberian)

---

### Phase 3: Conversational QA Integration
**Datasets:** AfriQA + Swahili parallel + XTREME-S subsets  
**Duration:** 10-20% of initial training time  
**Goal:** Add conversational understanding (QA, retrieval) to dialect competence

**Training Mix:**
- 50% AfriQA (conversational QA in African languages)
- 30% XTREME-S (multilingual speech tasks)
- 20% Swahili parallel (large-scale Swahili alignment)

**Rationale:**
- QA format teaches **targeted comprehension**
- XTREME-S adds **multi-task robustness**
- Swahili bridges **East African linguistic diversity**

---

## Recommended Total Mix (Secondary Fine-Tuning)

| Dataset                  | % of Secondary Training | Primary Benefit                  |
|--------------------------|-------------------------|----------------------------------|
| SwitchLingua             | 15%                     | Code-switching quality           |
| CS-FLEURS                | 10%                     | Massively multilingual CS breadth|
| WAXAL (African)          | 25%                     | African language coverage        |
| Chinese Dialects         | 15%                     | Mutually unintelligible varieties|
| Brazilian Portuguese     | 10%                     | Portuguese dialect divergence    |
| Chilean Spanish          | 5%                      | Latin American Spanish           |
| AfriQA                   | 10%                     | Conversational QA understanding  |
| XTREME-S                 | 5%                      | Multi-task robustness            |
| Swahili Parallel         | 5%                      | Swahili depth (East Africa)      |

**Total:** 100% of secondary fine-tuning budget

---

## Linguistic Coverage Summary

### By Language Family:
- **Niger-Congo:** 15+ languages (WAXAL: Swahili, Yoruba, Igbo, Hausa, etc.)
- **Afroasiatic:** 5+ languages (WAXAL: Amharic, Oromo, Tigrinya; SwitchLingua: Arabic)
- **Sino-Tibetan:** 10+ Chinese dialects (Nexdata/KeSpeech: Cantonese, Wu, Min, Hakka, etc.)
- **Indo-European:** Portuguese (Brazilian), Spanish (Chilean, LATAM), Hindi, Russian
- **Austronesian:** Filipino, Malay, Indonesian, Javanese (XTREME-S)
- **Tai-Kadai:** Thai, Lao (XTREME-S)
- **Japonic/Koreanic:** Japanese, Korean (SwitchLingua, Fun-ASR)

### By Geographic Region:
- **Sub-Saharan Africa:** 19 languages (WAXAL) + AfriQA + Swahili
- **East Asia:** Chinese dialects, Japanese, Korean, Cantonese
- **South-East Asia:** Thai, Vietnamese, Malay, Indonesian, Filipino, Khmer, Lao
- **South Asia:** Hindi, Urdu (SwitchLingua/XTREME-S)
- **Latin America:** Brazilian Portuguese, Chilean Spanish
- **Middle East/North Africa:** Arabic (SwitchLingua, CS-FLEURS)
- **Europe:** French, German, Italian, Russian, Spanish (SwitchLingua)

### Total Unique Languages/Dialects: ~80+

---

## License Summary

| Dataset                  | License                  | Access      |
|--------------------------|--------------------------|-------------|
| SwitchLingua             | Gated (custom)           | Requires agreement |
| CS-FLEURS                | CC BY 4.0 (NC)           | Open (non-commercial) |
| WAXAL                    | CC-BY-4.0 / CC-BY-SA-4.0 | Open        |
| Nexdata Chinese Dialects | Proprietary (paid)       | Sample available |
| XTREME-S                 | Apache 2.0 (varies)      | Open        |
| ASR-BPCSC                | Open-source              | Open (10h)  |
| Chilean Spanish          | CC-BY-4.0                | Open        |
| AfriQA                   | Open (TBD)               | Open        |
| Swahili Parallel         | TBD                      | Open        |
| Fun-ASR                  | Open-source              | GitHub      |

**Priority:** Focus on CC-BY-4.0, CC-BY-SA-4.0, Apache 2.0 for commercial use.  
**Evaluate:** SwitchLingua, CS-FLEURS gated access (may have research-friendly terms).

---

## Next Steps

1. ✅ Document multilingual/dialect datasets (this file)
2. ⏳ **Download & verify licenses** (prioritize open-source)
3. ⏳ **Pre-process to unified format** (ChatML with language tags)
4. ⏳ **Build secondary fine-tuning pipeline** with mixing ratios
5. ⏳ **Train base LoRA** on initial conversational datasets
6. ⏳ **Apply secondary fine-tuning** with multilingual/dialect mix
7. ⏳ **Evaluate cross-lingual transfer** (test on unseen language pairs)

**Expected Outcome:**
- Base model handles general conversation (English-centric)
- Secondary LoRA adds multilingual competence + dialect awareness
- Final model: conversational fluency across 80+ languages/dialects with code-switching support

---

**Report compiled:** 2026-02-04  
**Status:** 10 multilingual/dialect datasets identified with secondary fine-tuning strategy
