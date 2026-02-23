# LoRA On‑Policy Fine‑Tuning Roadmap

## 목적
현재 `fine-tuning/` 스크립트와 Tinker LoRA 파이프라인을 기반으로 **온‑폴리시 대화형 튜터 모델**을 반복적으로 개선하는 운영 절차를 확립한다.

---

## 0) 기준 정의 (Done/Assumed)
- **Base model:** `Qwen/Qwen3-8B`
- **Training method:** Tinker LoRA (`run_tinker_lora.py`)
- **Checkpointing:** `save_weights_for_sampler()` with `step_XXXX`, `final`
- **HF repo:** `https://huggingface.co/milwright/qwen-8b-dialog-v1`

---

## 1) 데이터 레이어 설계
### 1.1 Anchor (오프‑폴리시 안정화 데이터)
- LMSYS‑Chat‑1M
- Magpie‑Pro‑300K‑Filtered
- Prosocial‑Dialog
- 목적: 일반 대화성 + 안정성 유지

### 1.2 On‑Policy (현재 모델 기반 생성 데이터)
- 현재 LoRA 체크포인트로 샘플 생성
- 목적: **대화 질문/스캐폴딩 스타일 강화**

### 1.3 Mix Policy
- **권장 비율:** On‑policy 70–80% + Anchor 20–30%
- 향후 성능/안정성에 따라 비율 가변

---

## 2) 스크립트 추가 (필수)

### 2.1 `onpolicy_sample.py`
**기능**
- 입력: base model + LoRA checkpoint
- 출력: ChatML JSONL + metadata

**요구사항**
- `tokenizer.apply_chat_template` 동일 사용
- 템플릿에 system prompt 포함 가능
- 샘플링 설정 기록 (temp, top_p, max_tokens)

---

### 2.2 `onpolicy_score.py`
**기능**
- 생성 결과에 점수 부여
- 로컬 규칙 기반 → 나중에 reward model로 교체

**초기 규칙 예시**
- 질문 비율 (문장 끝 `?` 빈도)
- 대답 길이 제한 (짧고 명료)
- 스캐폴딩 여부 (follow‑up 질문 존재)

출력:
- JSONL에 `score` 또는 `weight` 컬럼 추가

---

### 2.3 `onpolicy_train.py`
**기능**
- `run_tinker_lora.py` 감싸는 래퍼
- On‑policy + Anchor 혼합
- weights 적용 (loss weighting)

**옵션**
- `--mix-ratio 0.8`
- `--rounds N`
- `--anchor-path`
- `--onpolicy-path`

---

## 3) 루프 설계 (Round‑based)

```
[Checkpoint_n]
   ↓
1) onpolicy_sample
   ↓
2) onpolicy_score
   ↓
3) onpolicy_train (mixed)
   ↓
4) eval + report
   ↓
[Checkpoint_n+1]
```

**권장 Round 규모**
- On‑policy: 10k–20k 샘플
- Anchor: 2k–5k 샘플
- Steps: 200–500

---

## 4) 평가 지표 (자동화)

**대화성/튜터링 지표**
- 질문 비율 (% of assistant turns ending in `?`)
- 평균 응답 길이
- multi‑turn 유지 (turn depth)
- 질문/설명 균형

**안정성 지표**
- Prosocial/Politeness heuristic
- Excess verbosity check

**출력:** `eval_round_<n>.json`

---

## 5) 체크포인트 & 리포팅
- 매 Round 후 Tinker URIs 기록
- HF 모델 카드 갱신 (README.md)
- changelog에 round별 성능 요약

---

## 6) 운영 순서 (권장 첫 실행)
1. Anchor 데이터 준비 (`prepare_stage1.py`)
2. On‑policy 샘플 생성 (10k)
3. 스코어링
4. Mixed LoRA 학습 (200–500 steps)
5. 평가 및 리포트
6. 반복

---

## 7) 향후 확장
- Reward model 도입
- Human feedback 루프 통합
- Variant‑specific rounds (ESL, Academic, K‑12)

---

## 최종 산출물
- `onpolicy_sample.py`
- `onpolicy_score.py`
- `onpolicy_train.py`
- `eval_round_<n>.json`
- 업데이트된 HF 모델 카드
