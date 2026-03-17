# Section III — Continuity and Asymmetry (v3)
## Changes bolded

---

### III. Continuity and Asymmetry

**Taylor's cloze test and BERT's masked language modeling share one mechanism: remove a word, evaluate the ability to restore it. That is where the similarity ends.**

Taylor's procedure assumed its subjects already had language. The test measured how well a reader could draw on syntax, semantics, and discourse context to recover what was deleted — a capacity acquired over years of reading, conversation, and exposure to written prose. A blank in a Melville passage asks the reader to bring knowledge of nineteenth-century diction, narrative convention, and the specific passage's argument to bear on a single missing word. The test does not teach that knowledge. It measures whether the reader has it.

BERT's training worked in the opposite direction. The model began with no linguistic knowledge. Masked language modeling was the mechanism by which it acquired statistical regularities across billions of tokens — each masked word a training signal, each gradient update a small adjustment to the model's internal weights. The "blank" in BERT's pretraining was not a prompt for reflection but a loss function. The model learned to minimize prediction error, not to comprehend.

**The divergence shows up in behavior.** On the CLOTH dataset — 96,000 fill-in-the-blank items authored by experienced teachers for use with human students — baseline language models trained on billion-word corpora achieved roughly 50–55% accuracy. Human test-takers achieved 86% (Xie et al. 2018). The gap is not only quantitative. Studies comparing human and model response distributions find that models systematically under-rank the completions humans most frequently produce and over-rank low-frequency alternatives that are statistically plausible but contextually odd (PMC 2024; arXiv 2024). The model and the human are solving different problems using the same surface form.

**Cloze Reader makes this gap concrete.** The application uses Gemma-3 — a language model trained through the masked-prediction paradigm BERT established — to select which words to remove from a passage. The model picks words with high contextual salience, which means words its training made highly predictable. A player then tries to restore them. The model chose the blank because prediction was easy; the player struggles because comprehension is hard. The same word, the same blank, two entirely different cognitive situations. **The paper tracks that gap between statistical predictability and human interpretive difficulty.**

---

**Word count (v3 Section III only):** ~320
