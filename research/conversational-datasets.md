# Conversational Datasets for Linguist Track
**Research Date:** 2026-02-04  
**Purpose:** Identify 10 diverse conversational datasets for fine-tuning language models

---

## Dataset 1: LMSYS-Chat-1M
**Location:** `lmsys/lmsys-chat-1m` (HuggingFace)  
**Link:** https://huggingface.co/datasets/lmsys/lmsys-chat-1m  
**Size:** 1,000,000 conversations | 25 models | 210K unique users | 154 languages  
**License:** LMSYS-Chat-1M Dataset License (gated - requires agreement)  
**Format:** OpenAI API JSON format with conversation ID, model name, language tags

**Training Approach:**
- Load via `datasets` library: `load_dataset("lmsys/lmsys-chat-1m")`
- Pre-redacted PII (names → NAME_1, NAME_2)
- Includes OpenAI moderation API tags for safety filtering
- Multi-turn conversations (avg 2.0 turns, 69.5 tokens/prompt, 214.5 tokens/response)

**Diversification Value:**
- **Real-world data:** Actual user interactions with 25 SOTA LLMs (GPT-4, Claude, etc.)
- **Multi-lingual:** 154 languages for global conversation patterns
- **Safety insights:** Includes unsafe conversations + moderation tags for robustness training
- **Failure cases:** Contains errors from SOTA models (valuable for learning edge cases)

**Pros:**
- Massive scale (1M conversations)
- Real user prompts (not synthetic)
- Diverse languages and use cases
- Well-documented with moderation labels

**Cons:**
- Gated access (requires form submission for raw data)
- May contain benchmark contamination
- PII redaction may impact some contexts

---

## Dataset 2: Salesforce DialogStudio
**Location:** `Salesforce/dialogstudio` (HuggingFace)  
**Link:** https://huggingface.co/datasets/Salesforce/dialogstudio  
**Size:** Multiple datasets across 6 categories (unified framework)  
**License:** Requires acknowledgment of individual dataset licenses  
**Format:** Unified JSON schema across all dialog types

**Categories:**
1. Knowledge-Grounded Dialogues
2. Natural Language Understanding
3. Open-Domain Dialogues
4. Task-Oriented Dialogues (e.g., MultiWOZ2.2: 8,437 train)
5. Dialogue Summarization
6. Conversational Recommendation

**Training Approach:**
- Load specific datasets: `load_dataset('Salesforce/dialogstudio', 'MULTIWOZ2_2')`
- Standardized schema: dialog ID, log, prompt, external knowledge, dst/intent knowledge
- Mix multiple categories for diverse training

**Diversification Value:**
- **Multi-domain:** Covers task-oriented, open-domain, knowledge-grounded, recommendations
- **Structured learning:** Includes external knowledge fields for grounding
- **Instruction-aware:** Designed for instruction-following model training
- **Unified format:** Easy to combine multiple dialog types

**Pros:**
- Comprehensive coverage of dialog types
- Standardized format simplifies multi-dataset training
- Includes metadata (knowledge, intents, states)
- Active maintenance (updated March 2024)

**Cons:**
- Gated access (requires license acknowledgment)
- Individual dataset licenses vary
- Dataset viewer issues on HuggingFace (use GitHub for examples)

---

## Dataset 3: AllenAI Prosocial Dialog
**Location:** `allenai/prosocial-dialog` (HuggingFace)  
**Link:** https://huggingface.co/datasets/allenai/prosocial-dialog  
**Size:** 58K dialogues | 331K utterances | 160K unique RoTs | 497K safety labels  
**License:** Apache 2.0 (likely - AllenAI standard)  
**Format:** JSON with dialogues, Rules of Thumb (RoTs), safety labels + rationales

**Training Approach:**
- Human-AI collaborative framework
- Load via: `load_dataset("allenai/prosocial-dialog")`
- Includes safety labels with free-form rationales

**Diversification Value:**
- **Safety-first:** Explicit prosocial behavior modeling
- **Rationale-driven:** Includes reasoning behind safety judgments
- **Rule-grounded:** 160K unique Rules of Thumb for ethical guidance
- **Intervention training:** Teaches models to steer toward helpful/safe responses

**Pros:**
- Strong safety/ethics focus
- Rationales support explainable AI
- High-quality human-AI collaboration
- Open license (AllenAI)

**Cons:**
- Smaller scale (58K vs 1M)
- Narrow focus (prosocial) - less general conversation

---

## Dataset 4: DialogSum (Dialogue Summarization)
**Location:** `knkarthick/dialogsum` (HuggingFace)  
**Link:** https://huggingface.co/datasets/knkarthick/dialogsum  
**Size:** 13,460 dialogues + 1,000 test | train/val/test splits  
**License:** Not specified (likely permissive - check repo)  
**Format:** JSON with `id`, `dialogue`, `summary`

**Training Approach:**
- Load: `load_dataset("knkarthick/dialogsum")`
- Train on dialogue → summary pairs
- Can reverse for summary → dialogue generation

**Diversification Value:**
- **Summarization skill:** Teaches compression/synthesis of conversations
- **Multi-task:** Dialogue understanding + generation
- **Structured:** Clear topic structure in dialogues
- **Dual-use:** Forward (summarize) or reverse (expand) training

**Pros:**
- Clean train/val/test splits
- Well-structured dialogues
- Summarization adds meta-understanding

**Cons:**
- Smaller dataset
- Single task focus (summarization)
- Less diversity in conversation types

---

## Dataset 5: HuggingFaceTB Everyday Conversations
**Location:** `HuggingFaceTB/everyday-conversations-llama3.1-2k` (HuggingFace)  
**Link:** https://huggingface.co/datasets/HuggingFaceTB/everyday-conversations-llama3.1-2k  
**Size:** 2K everyday conversations  
**License:** HuggingFace permissive (check dataset card)  
**Format:** ChatML preprocessing complete

**Training Approach:**
- Pre-processed for Llama 3.1 architecture
- Augment with OpenHermes-2.5 and Magpie for greeting diversity
- Direct fine-tuning ready

**Diversification Value:**
- **Casual conversation:** Everyday chitchat vs task-oriented
- **Natural greetings:** Multiple greeting formats
- **Human-like flow:** Authentic conversational patterns
- **Model-agnostic lessons:** Despite Llama focus, patterns transfer

**Pros:**
- Pre-processed (saves time)
- Everyday language patterns
- Augmentation guidance included

**Cons:**
- Smaller scale (2K)
- Llama-specific preprocessing (may need adaptation)

---

## Dataset 6: LMSYS Chatbot Arena Conversations
**Location:** `lmsys/chatbot_arena_conversations` (HuggingFace)  
**Link:** https://huggingface.co/datasets/lmsys/chatbot_arena_conversations  
**Size:** 13K+ users | 20 LLMs (GPT-4, Claude-v1, etc.)  
**License:** Similar to LMSYS-Chat-1M (gated)  
**Format:** OpenAI API format with model comparisons

**Training Approach:**
- Load: `load_dataset("lmsys/chatbot_arena_conversations")`
- Contains side-by-side model outputs (comparative learning)
- Includes failure cases of SOTA models

**Diversification Value:**
- **Comparative learning:** See how different models respond to same prompt
- **Unrestricted queries:** 13K wild users (diverse intents)
- **SOTA failures:** Learn from GPT-4/Claude mistakes
- **Preference data potential:** Arena voting data (if included)

**Pros:**
- Multiple model outputs per prompt (rich training signal)
- Strong model coverage (GPT-4, Claude)
- Real user queries (unrestricted)

**Cons:**
- Gated access
- Focus on model comparison (less dialogue depth)

---

## Dataset 7: BAAI CS-Dialogue (Chinese Spontaneous)
**Location:** `BAAI/CS-Dialogue` (HuggingFace)  
**Link:** https://huggingface.co/datasets/BAAI/CS-Dialogue  
**Size:** 104.02 hours | 100 conversation pairs | 200 speakers  
**License:** Not specified (check dataset card)  
**Format:** Audio + transcriptions

**Training Approach:**
- Transcription-based training (or multimodal if using audio)
- Load: `load_dataset("BAAI/CS-Dialogue")`
- Spontaneous (unscripted) dialogue patterns

**Diversification Value:**
- **Language diversity:** Mandarin Chinese conversational patterns
- **Spontaneous speech:** Natural pauses, repairs, overlaps (realistic)
- **Audio-text alignment:** Multimodal learning potential
- **Cultural context:** Chinese communication norms

**Pros:**
- Spontaneous (not scripted)
- Multimodal (audio available)
- Cultural diversity (Chinese)

**Cons:**
- Smaller scale (100 pairs)
- Language-specific (Mandarin) - requires tokenizer support
- May need transcription quality check

---

## Dataset 8: IVLLab MultiDialog (Multimodal)
**Location:** `IVLLab/MultiDialog` (HuggingFace)  
**Link:** https://huggingface.co/datasets/IVLLab/MultiDialog  
**Size:** Multimodal (audio + text) - exact size TBD  
**License:** Gated (requires auth token)  
**Format:** Audio input + transcription values

**Training Approach:**
```python
from datasets import load_dataset
MultiD = load_dataset("IVLLab/MultiDialog", "valid_freq", use_auth_token=True)
audio_input = MultiD["valid_freq"][0]["audio"]
transcription = MultiD["valid_freq"][0]["value"]
```

**Diversification Value:**
- **Multimodal:** Audio-text dialogue generation
- **End-to-end training:** Full pipeline from audio to response
- **Frequency variations:** Dataset includes frequency-based splits
- **Sensory grounding:** Audio context enriches language understanding

**Pros:**
- Multimodal capabilities
- Audio data for richer context
- Structured splits (valid_freq)

**Cons:**
- Gated access (requires token)
- Smaller community (less documentation)
- Audio processing overhead

---

## Dataset 9: OpenHermes-2.5 (Mentioned in Everyday Conversations)
**Location:** Teknium's OpenHermes-2.5 (HuggingFace - search `OpenHermes`)  
**Link:** https://huggingface.co/datasets/teknium/OpenHermes-2.5  
**Size:** ~1M instruction-following examples (verify exact count)  
**License:** Apache 2.0 (typical for OpenHermes)  
**Format:** Instruction-response pairs (ChatML format)

**Training Approach:**
- Load: `load_dataset("teknium/OpenHermes-2.5")`
- Mix with conversational datasets for instruction+dialogue training
- ChatML format (system, user, assistant)

**Diversification Value:**
- **Instruction-following:** Complements conversation with task completion
- **Broad coverage:** Coding, math, reasoning, creative writing
- **High quality:** Curated from multiple sources (GPT-4 distillation)
- **Format diversity:** Teaches structured instruction adherence

**Pros:**
- Large scale (~1M)
- High-quality curation
- Instruction diversity
- Open license

**Cons:**
- Not purely conversational (task-heavy)
- GPT-4 distillation (synthetic)

---

## Dataset 10: Magpie (Mentioned in Everyday Conversations)
**Location:** HuggingFace (search for Magpie datasets - multiple versions)  
**Link:** https://huggingface.co/datasets/Magpie-Align/Magpie-Llama-3.1-Pro-300K-Filtered  
**Size:** ~300K (filtered version) | larger raw versions available  
**License:** Permissive (check specific version)  
**Format:** Instruction-response, conversational turns

**Training Approach:**
- Load: `load_dataset("Magpie-Align/Magpie-Llama-3.1-Pro-300K-Filtered")`
- Generated via self-instruct from Llama 3.1
- Filter for quality (use filtered versions)

**Diversification Value:**
- **Synthetic diversity:** AI-generated variety in prompts
- **Quality filtering:** Curated for coherence
- **Complementary to real data:** Fills gaps in real-world datasets
- **Scalable:** Can generate more if needed

**Pros:**
- Large scale (300K+)
- High quality (filtered)
- No privacy concerns (synthetic)
- Active development

**Cons:**
- Synthetic (less authentic than real user data)
- Model-specific generation (Llama 3.1 bias)

---

## Training Strategy: Dataset Mixing

### Recommended Mix for Balanced Linguist Training:
1. **Real-world foundation (60%):** LMSYS-Chat-1M (40%) + Chatbot Arena (20%)
2. **Task diversity (20%):** DialogStudio (10%) + OpenHermes-2.5 (10%)
3. **Safety/ethics (10%):** Prosocial Dialog
4. **Everyday patterns (5%):** Everyday Conversations + DialogSum
5. **Augmentation (5%):** Magpie (fill gaps)

### Rationale:
- **Majority real-world:** Authentic user behavior
- **Task coverage:** Instruction-following + open-domain + task-oriented
- **Safety grounding:** Prosocial guardrails
- **Quality synthetic:** Magpie/OpenHermes for diversity without privacy risk

### Training Workflow:
1. **Pre-process:** Convert all to unified ChatML format
2. **Deduplicate:** Remove overlaps (especially between LMSYS datasets)
3. **Balance:** Sample proportionally or weight loss by dataset
4. **Validate:** Hold out test sets from each source
5. **Fine-tune:** Start with base model (Gemma 3 14B), iterate

---

## License Summary

| Dataset | License | Access |
|---------|---------|--------|
| LMSYS-Chat-1M | Custom (gated) | Requires agreement |
| DialogStudio | Mixed (per dataset) | Gated |
| Prosocial Dialog | Apache 2.0 (likely) | Open |
| DialogSum | TBD (check repo) | Open |
| Everyday Conversations | HF Permissive | Open |
| Chatbot Arena | Custom (gated) | Requires agreement |
| CS-Dialogue | TBD | Open |
| MultiDialog | Gated | Requires token |
| OpenHermes-2.5 | Apache 2.0 | Open |
| Magpie | Permissive | Open |

**Action:** Verify all licenses before commercial use. Prioritize Apache 2.0 / MIT / CC-BY for unrestricted training.

---

## Next Steps
1. ✅ Document datasets (this file)
2. ⏳ Download and verify licenses
3. ⏳ Pre-process to unified format
4. ⏳ Build training pipeline with mixing ratios
5. ⏳ Start fine-tuning on Gemma 3 14B

**Report compiled:** 2026-02-04 (30 min deadline)  
**Status:** 10 datasets identified with training details and diversification rationale
