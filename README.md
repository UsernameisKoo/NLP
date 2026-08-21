## Projects
### Mental_wellness_chatbot

한국어 감성 대화 데이터 기반 감정 분석 및 문장 생성 프로젝트
- 모델: CNN + BiLSTM + Attention (PyTorch 직접 구현)
- 데이터: AI-Hub 감성 대화 말뭉치 (6개 감정 클래스)
- 구현 범위: 감정 다중 분류 → 감정 흐름 분석 → 클로징 멘트 생성
- 최종 성능: Test Accuracy 0.70 (6-class 다중 분류)

```
Mental_wellness_chatbot/
├── dataset/
│   ├── Training.xlsx
│   └── Validation.xlsx
├── models/
│   ├── Original_CNN_BiLSTM_Attention.ipynb   # 중간발표용 감정 분석 모델 (초안)
│   └── Proposal_CNN_BiLSTM_Attention.ipynb   # 최종발표용 감정 분석 모델 (개선 ver)
├── generation/
│   ├── create_sen.ipynb                       # 문장 생성 모델 학습 & 저장
│   ├── demo_chatbot.ipynb                     # 문장 생성 모델 시연
│   └── sen_gen_model.py                       # 문장 생성 모델 class 정의 (import용)
├── utils.py
├── sen_vocab.pkl
└── README.md
```

---

## Experiments
### embedding_experiments

한국어 감정 분류 태스크에서 임베딩 방식에 따른 성능 차이를 비교하는 실험 기록

- 실험 배경: PTB 데이터셋 기반 통계적 임베딩(PPMI + SVD) 실습 → 한국어 적용 한계 확인 → 신경망 기반 임베딩으로 전환
- 실험 흐름: 통계 기반 (PPMI + SVD) → Word2Vec → KoBERT
- 목적: 임베딩 선택 근거를 실험으로 검증

```
embedding_experiments/
├── results/
│   ├── show_ptb_실행화면.png
│   ├── count_method_big_실행화면.png
│   └── count_method_small_실행화면.png
├── 00_ptb_dataset_overview.ipynb
├── 01_statistical_embedding_large.ipynb
├── 02_statistical_embedding_small.ipynb
├── 03_create_context_target.ipynb
└── README.md
```
