LMSYS-Chat-1M anchors the dialogic baseline by supplying broad, natural multi-turn conversations. In the pedagogical framework, it preserves conversational flow and keeps tutoring behavior grounded in authentic exchange rather than scripted instruction.

Magpie-Pro-300K-Filtered strengthens instructional alignment without collapsing into didactic responses. It supports question-led guidance and scaffolding behaviors that match the framework’s emphasis on co-investigation and iterative prompting.

Prosocial-Dialog provides the affective and interpersonal layer required by a dialogic tutor. It stabilizes supportive tone, reduces punitive phrasing, and helps maintain learner agency during corrective or clarifying turns.

UltraChat-200K (train_sft) served as a pilot and sanity-check dataset to validate the LoRA pipeline before larger mixed runs. It offers a general conversational and instruction-following substrate that keeps early training stable while higher-priority pedagogical mixes are prepared.

TOEFL-style scaffolding dialogues are used as targeted augmentation to reinforce adaptive error-focused tutoring (recasts, follow-up questions, and gentle prompts). This augmentation operationalizes the framework’s emphasis on multi-turn scaffolding, though the latest +500 generation run with openai/gpt-oss-120b requires a clean rerun due to prior job termination.