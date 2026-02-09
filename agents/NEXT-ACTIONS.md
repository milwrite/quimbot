# NEXT ACTIONS - Petrarch
**Updated:** 2026-02-05 19:16 EST

## 🎯 Immediate Tasks

### 1. LMSYS Chat-1M Access (MANUAL - User Action Required)
**Status:** ⏸️ Awaiting user login  
**Steps:**
1. Go to: https://huggingface.co/datasets/lmsys/lmsys-chat-1m
2. Click "Log in" or "Sign Up" (if not already logged in)
3. Review license terms
4. Click "Accept License Agreement"
5. Dataset will be accessible via `load_dataset("lmsys/lmsys-chat-1m")`

**Value:** 1M real conversations, 154 languages, 25 SOTA models

---

### 2. WAXAL Dataset Download (IN PROGRESS)
**Status:** ⏳ Starting download  
**Location:** `google/WaxalNLP` (HuggingFace)  
**License:** CC-BY-4.0 ✅ Open  
**Size:** ~1,250 hours ASR + TTS data  
**Languages:** 22 African languages (Hausa, Swahili, Yoruba, Igbo, etc.)

**Download command:**
```python
from datasets import load_dataset
waxal = load_dataset("google/WaxalNLP")
```

---

### 3. Magpie Dataset Download (QUEUED)
**Status:** 🔜 Next after WAXAL  
**Location:** `Magpie-Align/Magpie-Llama-3.1-Pro-300K-Filtered` (HuggingFace)  
**License:** Likely permissive (verify on download)  
**Size:** ~300K filtered conversational examples  

**Download command:**
```python
from datasets import load_dataset
magpie = load_dataset("Magpie-Align/Magpie-Llama-3.1-Pro-300K-Filtered")
```

---

### 4. License Verification (TBD - 5 datasets)
**Status:** 📋 To be verified  
**Datasets to check:**
1. DialogSum (knkarthick/dialogsum)
2. CS-Dialogue (BAAI/CS-Dialogue)
3. Prosocial-Dialog (allenai/prosocial-dialog)
4. AfriQA (?)
5. Swahili Parallel (?)

**Action:** Visit each HuggingFace page, check license field, document in LICENSE-VERIFICATION.md

---

## 📊 Progress Summary

| Task | Status | ETA |
|------|--------|-----|
| Gated dataset research | ✅ Complete | Done |
| LMSYS access (manual) | ⏸️ User action | User-dependent |
| SwitchLingua (skipped) | ❌ Not available | N/A |
| WAXAL download | ⏳ In progress | ~15 min |
| Magpie download | 🔜 Queued | ~10 min |
| License verification | 📋 Pending | ~20 min |

---

## 🚀 Next Steps After Downloads

1. Preprocessing pipeline design (ChatML format)
2. Dataset mixing strategy (see conversational-datasets.md)
3. Deduplication across datasets
4. Quality filtering (safety, coherence)
5. Train/val/test splits

---

**Last updated:** 2026-02-05 19:16 EST by Petrarch
