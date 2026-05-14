# Writing Under Surveillance
## The Problem with AI Detection

**Zach Muhlbauer** — Draft v6 (final proof), May 2026

> Source: v5 draft (`writing-under-surveillance-vp-draft-v5.md`). v6 applies targeted Williams/milwrite revisions for the final proof. Body paragraphs and References preserved from v5 except for the enumerated edits at the end of this file.

---

---

![Reddit exchange about AI detection reliability](/Users/zacharymuhlbauer/Desktop/STUDIO/projects/quimbot/docs/writing-under-surveillance/ai-detection-reddit-exchange.jpg)

*Reddit exchange about AI detection reliability.*

During a summer composition course at LaGuardia Community College, a student learns that their work is under suspicion of having been written by AI. Their instructor says their spoken and written English do not match and treats the paper as too composed, too clean to be their own. The student acknowledges revising with Grammarly, but denies using AI to write the paper and even offers version histories and tracked changes to prove it.

Like this student, Reddit replies are often evidence-first and based on personal experience. Students advise one another to document the writing process, compare detector outputs, and prepare to explain the paper aloud across r/HunterCollege, r/Baruch, r/QueensCollege, and r/CUNY threads. While a Hunter student worries that lowering an AI likelihood score would make a long paper less mature, a Baruch student stands by idly as their paper turns from a WU into an F after passing from professor to department chair, registrar, and dean. Across these threads, AI suspicion shifts the burden of proof onto students, making authorship something they must defend once their work has been algorithmically recast as suspect.

Plagiarism detection giants like Turnitin have long shaped how students learn to write and under what conditions they see themselves as writers. More recently, though, the plot has thickened. On top of their usual offerings, these platforms now market AI detection solutions meant to distinguish human writing from machine-generated output.

To grasp the problem with AI detection, take what a prominent service claims to do. GPTZero reports using two metrics: *perplexity*, a measure of how well an LLM would predict each successive word in a passage; and *burstiness*, used to score variation in the sentence-level rhythm and structure of student writing (Tian). Both assume that human writers naturally vary syntax and sentence length while AI models lean toward consistent, flat tempos at the sentence- and paragraph-level ("AI Detectors"; Galczynski). This premise is incredibly shaky and points to a larger problem in why detection failures multiply at scale. Since detectors classify writing by proxy and rely on statistical signals to judge whether a text is machine-generated, those signals travel unevenly across models, genres, revision practices, and linguistic differences, yielding probability scores that break down across real student writing (Krishna et al.; Weber-Wulff et al.; Sadasivan et al.; Liang et al.).

One of the most comprehensive accounts in the field tested twelve publicly available tools alongside Turnitin and PlagiarismCheck, reporting they were "neither accurate nor reliable," and exhibited a systematic bias toward classifying AI-generated text as human-written (Weber-Wulff et al.). Even a "low" 1% false positive rate across 22.35 million first-year college essays amounts to 223,500 essays falsely flagged in a single year (Hirsch).

Those affected are hardly edge cases. The MLA-CCCC Joint Task Force on Writing and AI put it plainly when it warned AI detection tools enable "false accusations" that "may disproportionately affect marginalized groups." Sure enough, Black students face disproportionately higher rates of AI-detection accusations than their white peers (Madden et al.). Students identifying as disabled are also reported more likely to receive a false positive for submitted writing that departs from the narrowed standards these tools inscribe as human (Hirsch). And one study of seven widely used detectors found these services flagged as AI-generated 61.22% of TOEFL essays by non-native English speakers, and, across all seven detectors, 89 of 91 essays were flagged by at least one of the tools sampled in the study (Liang et al.).

At the end of the day, detection services narrow authenticity to features algorithms can count, weight, and score, distributing that burden unevenly among student groups as diverse as those at CUNY. Their encoded "human" criteria define not an inherent quality of submitted writing but a rubric for evaluating prose, treating writing as a process under surveillance, substituting suspicion for trust and audience, and turning assessment into automated verification rather than a context-aware teaching practice.

For all their alleged sophistication, AI detectors still classify writing through statistical signals that do not hold consistently across LLMs and are easily disrupted by simple obfuscation strategies (Weber-Wulff et al.). Their unreliability, and the anxiety they produce, is therefore hardly surprising. The larger problem is that they invite us to accept a hidden standard of human writing that is at once opaque and flattening, one that treats authentic prose as a fixed object or end product.

Trust is hard work in any classroom, and AI detectors make that work harder by turning a paper into a case before the conversation begins. AI detectors are but a problem dressed in its own solution, an instance of what Evgeny Morozov calls solutionism, which "presumes rather than investigates the problems that it is trying to solve" (6).

As for the LaGuardia student, their instructor cleared the paper of all charges, but not without taking a moment to warn them about Grammarly, and as it happens, the thesaurus too.

---

## References

"Why Don't AI Detectors Work?" *Instructional Resources*, Center for Integrated Professional Development, Illinois State University, 2024, https://prodev.illinoisstate.edu/instructional-resources/pedagogy/ai/detectors/. Accessed 5 Feb. 2026.

"AI Detectors Biased Against Non-Native English Writers." *Stanford HAI*, Stanford University, 10 July 2023, https://hai.stanford.edu/news/ai-detectors-biased-against-non-native-english-writers. Accessed 5 Feb. 2026.

"Generative AI Detection Tools." *USD Law Library Guides*, University of San Diego Legal Research Center, https://lawlibguides.sandiego.edu/generative-AI-detectors. Accessed 5 Feb. 2026.

Cheng, Adam, et al. "Ability of AI Detection Tools and Humans to Accurately Identify Different Forms of AI-Generated Written Content." *Advances in Simulation*, vol. 10, no. 66, 22 Nov. 2025, https://doi.org/10.1186/s41077-025-00396-6.

Galczynski, Jordan. "The Imperfection of AI Detection Tools." *HumTech*, UCLA, 9 Oct. 2025, https://humtech.ucla.edu/technology/the-imperfection-of-ai-detection-tools/. Accessed 7 Feb. 2026.

Hirsch, Amanda. "AI Detectors: An Ethical Minefield." *Center for Innovative Teaching and Learning*, Northern Illinois University, 12 Dec. 2024, https://citl.news.niu.edu/2024/12/12/ai-detectors-an-ethical-minefield/. Accessed 5 Feb. 2026.

Krishna, Kalpesh, et al. "Paraphrasing Evades Detectors of AI-Generated Text, but Retrieval Is an Effective Defense." *NeurIPS 2023*, 2023, https://doi.org/10.48550/arXiv.2303.13408.

Liang, Weixin, et al. "GPT Detectors Are Biased Against Non-Native English Writers." *Patterns*, vol. 4, no. 7, 14 July 2023, p. 100779, https://doi.org/10.1016/j.patter.2023.100779.

Madden, Mary, et al. *The Dawn of the AI Era: Teens, Parents, and the Adoption of Generative AI at Home and School*. Common Sense Media, 18 Sept. 2024, https://www.commonsensemedia.org/sites/default/files/research/report/2024-the-dawn-of-the-ai-era_final-release-for-web.pdf.

MLA-CCCC Joint Task Force on Writing and AI. *Overview of the Issues, Statement of Principles, and Recommendations*. Working Paper 1, July 2023, https://aiandwriting.hcommons.org/.

Morozov, Evgeny. *To Save Everything, Click Here: The Folly of Technological Solutionism*. PublicAffairs, 2013.

Sadasivan, Vinu Sankar, et al. "Can AI-Generated Text Be Reliably Detected?" *Transactions on Machine Learning Research*, Jan. 2025, https://doi.org/10.48550/arXiv.2303.11156.

Tian, Edward. "Perplexity, Burstiness, and Statistical AI Detection." *GPTZero*, 1 Mar. 2023, https://gptzero.me/news/perplexity-and-burstiness-what-is-it/. Accessed 5 Feb. 2026.


Weber-Wulff, Debora, et al. "Testing of Detection Tools for AI-Generated Text." *International Journal for Educational Integrity*, vol. 19, no. 26, 2023, https://doi.org/10.1007/s40979-023-00146-z. Accessed 28 Feb. 2026.

---

## Change notes (v5 → v6)

Targeted Williams/milwrite revisions for the final proof. User direction (2026-05-12): keep "incredibly"; rephrase the matter/matters subject-verb issue; render the "human" criteria line as plural.

Add below: 
* 
