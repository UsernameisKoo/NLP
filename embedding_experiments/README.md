# Embedding Experiments

한국어 감정 분류 태스크에서 임베딩 방식에 따른 성능 차이를 비교하는 실험 기록

---

## 실험 목적

`Mental_wellness_chatbot` 프로젝트에서 감정 분류 모델의 입력 임베딩 방식을 결정하기 위해 진행한 탐색 실험이다.

처음에는 레퍼런스 기반으로 통계적 임베딩(PPMI + SVD)을 학습했으나, 해당 방식이 영어 말뭉치(PTB) 기반이라 한국어 감정 데이터에 직접 적용이 불가능하다는 한계를 확인했다. 이후 한국어에 적합한 임베딩 방식으로 전환하는 과정을 실험으로 기록한다.

---

## 실험 흐름

```
00. PTB 데이터셋 구조 파악
        ↓
01. 통계 기반 임베딩 실험 (PPMI + SVD, 대규모 말뭉치)
        ↓
02. 통계 기반 임베딩 실험 (PPMI + SVD, 소규모 말뭉치)
        ↓
03. Context-Target 쌍 생성 구조 이해
        ↓
[한계 확인] 영어 기반 → 한국어 감정 데이터 적용 불가
```

### 파일 구성

| 파일 | 내용 |
|---|---|
| `00_ptb_dataset_overview.ipynb` | PTB 데이터셋 로드, corpus 구조 및 word-id 매핑 확인 |
| `01_count_method_big.ipynb` | 대규모 말뭉치 기반 동시발생 행렬 + PPMI + SVD 실험 |
| `02_count_method_small.ipynb` | 소규모 말뭉치 기반 동일 실험, 결과 시각화 |
| `03_create_context_target.ipynb` | Context-Target 쌍 생성 함수 구현 (Word2Vec 학습 전처리 구조) |
| `results/` | 각 실험 실행화면 스크린샷 |

---

## 실험 결과 요약

### 통계 기반 임베딩 (PPMI + SVD)
- PTB 학습 데이터 기준 유사 단어 검색 결과 (코사인 유사도)

| Query | Top 유사 단어 |
|---|---|
| `you` | `i (0.69)`, `we (0.65)` |
| `year` | `month (0.69)`, `earlier (0.66)` |
| `car` | `auto (0.60)`, `cars (0.58)` |
| `toyota` | `motor (0.75)`, `nissan (0.71)` |


- **한계**: PTB는 영어 말뭉치이므로 한국어 감정 데이터에 동일 방식 적용 불가
- **결론**: 한국어 임베딩은 신경망 기반 방식으로 전환 필요

