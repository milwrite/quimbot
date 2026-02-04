# Research Folder

This directory contains research findings for the Orchestra project.

## Files

### conversational-datasets.md
**Purpose:** Linguist track dataset research  
**Date:** 2026-02-04  
**Contents:** 10 conversational datasets with:
- HuggingFace locations
- Size/license information  
- Training approaches
- Diversification rationales
- Recommended mixing strategy

**Quick Access Datasets:**
1. LMSYS-Chat-1M (1M conversations, 25 models)
2. Salesforce DialogStudio (multi-domain unified)
3. AllenAI Prosocial Dialog (safety-focused)
4. DialogSum (summarization pairs)
5. Everyday Conversations (casual chat)
6. Chatbot Arena (model comparisons)
7. BAAI CS-Dialogue (Mandarin audio)
8. MultiDialog (multimodal)
9. OpenHermes-2.5 (instruction-following)
10. Magpie (synthetic augmentation)

**Recommended Mix:** 60% real-world + 20% task diversity + 10% safety + 10% augmentation

---

### multilingual-dialect-datasets.md
**Purpose:** Secondary fine-tuning datasets for multilingual/dialect coverage  
**Date:** 2026-02-04  
**Contents:** 10 datasets covering 80+ languages/dialects:
- Code-switching (SwitchLingua, CS-FLEURS)
- African languages (WAXAL - 19 languages, brand new!)
- Chinese dialects (Nexdata/KeSpeech - 10+ varieties)
- Latin American Portuguese/Spanish
- Asian languages (XTREME-S, Fun-ASR)
- Conversational QA (AfriQA, Swahili)

**Secondary Fine-Tuning Strategy:**
- Phase 1: Code-switching foundation (25%)
- Phase 2: Regional dialects (60%)
- Phase 3: Conversational QA integration (15%)

**Coverage:** Sub-Saharan Africa, East Asia, South-East Asia, Latin America, Middle East, Europe

---

**Updated:** 2026-02-04 by Petrarch
