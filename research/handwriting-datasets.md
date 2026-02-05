# Handwriting Datasets for Movement 2 (Scribe)

**Research Date:** 2026-02-05  
**Purpose:** Identify datasets for handwriting recognition/generation (Movement 2 - Scribe)

---

## Dataset 1: IAM Handwriting Database
**Location:** 
- Official: https://fki.tic.heia-fr.ch/databases/iam-handwriting-database
- HuggingFace: `Teklia/IAM-line`
- Kaggle: https://www.kaggle.com/datasets/naderabdalghani/iam-handwritten-forms-dataset

**Size:** Forms of handwritten English text  
**License:** Academic/research (registration required on official site)  
**Format:** Handwritten forms, line-level annotations

**Use Cases:**
- Handwritten text recognition (HTR)
- Writer identification
- Writer verification

**Availability:**
- **Official site:** Requires registration for academic use
- **HuggingFace:** Available at `Teklia/IAM-line` (check license)
- **Kaggle:** Public datasets available

**Recommendation:** Start with HuggingFace version for easier access

---

## Dataset 2: MNIST (Handwritten Digits)
**Location:** `ylecun/mnist` (HuggingFace)  
**Link:** https://huggingface.co/datasets/ylecun/mnist  
**Size:** 60,000 training images + 10,000 test images  
**License:** Public domain  
**Format:** 28×28 pixel grayscale images of single digits (0-9)

**Use Cases:**
- Digit recognition
- Basic OCR training
- Baseline model validation

**Pros:**
- Widely used benchmark
- Small, fast to train
- Public domain license
- Available on HuggingFace

**Cons:**
- Only digits (no letters)
- Simple/limited compared to full handwriting

---

## Dataset 3: EMNIST (Extended MNIST)
**Location:** Search HuggingFace for EMNIST or NIST variations  
**Size:** Larger than MNIST, includes letters + digits  
**License:** Public domain (NIST data)  
**Format:** Similar to MNIST (grayscale images)

**Use Cases:**
- Alphanumeric handwriting recognition
- More complex OCR than MNIST
- Character-level recognition

**Recommendation:** Better than MNIST for actual Scribe task (includes letters)

---

## Dataset 4: 15 Best Open-Source Handwriting Datasets
**Source:** https://weareshaip.medium.com/the-15-best-open-source-handwriting-datasets-to-train-your-ml-models-5154e42788d3

**Mentioned datasets include:**
1. NIST (National Institute of Standards)
2. MNIST
3. IAM
4. CVL Database
5. RIMES (French handwriting)
6. And 10 more...

**Action:** Review this article for comprehensive list of alternatives

---

## Recommended Approach for Movement 2

### Phase 1: Quick Start (Digits Only)
**Dataset:** MNIST (`ylecun/mnist`)  
**Why:** 
- Public domain, instant access
- Fast training (60K examples, small images)
- Good for validating pipeline

**Timeline:** Can start immediately

---

### Phase 2: Full Handwriting (Letters + Digits)
**Primary Option:** IAM Database via HuggingFace  
**Backup Options:**
1. EMNIST (if IAM requires registration hassle)
2. CVL Database
3. RIMES (if multilingual needed)

**Why:**
- IAM is industry standard
- Real handwritten text (not just isolated characters)
- Supports full HTR training

**Timeline:** After MNIST baseline works

---

### Phase 3: Multilingual/Advanced (Optional)
**Consider:**
- RIMES (French)
- Chinese handwriting datasets
- Arabic script datasets

**Timeline:** Future enhancement

---

## License Summary

| Dataset | License | Access |
|---------|---------|--------|
| MNIST | Public domain | ✅ Immediate (HuggingFace) |
| EMNIST | Public domain | ✅ Immediate (HuggingFace likely) |
| IAM (Official) | Academic (registration) | ⏳ Requires form |
| IAM (HuggingFace) | Check `Teklia/IAM-line` card | ⏳ Verify license |
| IAM (Kaggle) | Public datasets | ✅ Immediate |

---

## Next Actions

### Immediate (This Morning)
- [ ] Download MNIST from HuggingFace (`ylecun/mnist`)
- [ ] Verify IAM license on HuggingFace (`Teklia/IAM-line`)
- [ ] Check Kaggle IAM dataset accessibility

### This Week
- [ ] Test MNIST with simple OCR model (validation)
- [ ] Download IAM dataset (HuggingFace or Kaggle)
- [ ] Research EMNIST availability

### Handoff to Quimbot
- [ ] Share dataset paths + format details
- [ ] Recommend starting with MNIST for pipeline validation
- [ ] Provide IAM download instructions once verified

---

## Download Commands

### MNIST
```python
from datasets import load_dataset
mnist = load_dataset("ylecun/mnist")
mnist['train'].save_to_disk("datasets/mnist-train")
mnist['test'].save_to_disk("datasets/mnist-test")
```

### IAM (HuggingFace)
```python
from datasets import load_dataset
iam = load_dataset("Teklia/IAM-line")
iam.save_to_disk("datasets/iam-handwriting")
```

### IAM (Kaggle - requires Kaggle API)
```bash
kaggle datasets download -d naderabdalghani/iam-handwritten-forms-dataset
unzip iam-handwritten-forms-dataset.zip -d datasets/iam-kaggle
```

---

**Status:** Research complete, ready to begin downloads  
**Recommendation:** Start with MNIST today (fast validation), then IAM for production Scribe model
