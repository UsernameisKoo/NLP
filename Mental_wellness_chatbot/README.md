# 정신상담 AI: 감정 분석 & 문장 생성 

## 프로젝트 개요
### 문제 정의
심리 상담 서비스는 심리적 부담, 시간·비용 문제로 실제 접근이 어렵다. 기존 감정 분석 시스템은 문장 단위 분류에 그쳐 대화 흐름 속 감정 변화를 반영하지 못한다.

### 목표 
단순 문장별 감정 분류가 아닌, 대화 흐름 전체를 기반으로 감정 변화를 분석하고 상황에 맞는 클로징 멘트를 생성하는 시스템 구현

### 핵심 구현 범위
1. 6개 감정 다중 분류 (기쁨 / 당황 / 분노 / 불안 / 상처 / 슬픔)

2. 대화 흐름 기반 감정 변화 분석
3. 감정 조건부 클로징 멘트 생성 (Seq2Seq + Attention)

## 시스템 구조
```
사용자 대화 입력
        ↓
[감정 분류] CNN + BiLSTM + Attention
        ↓
[감정 흐름 분석] 대화 시퀀스 기반 감정 변화 추적
        ↓
[시각화] Attention Heatmap → 감정 변화 흐름 직관적 표시
        ↓
[클로징 멘트 생성] EmotionConditionedSeq2Seq
        ↓
맞춤형 응답 출력
```

## 파일 구조
```
Mental_wellness_chatbot/
├── dataset/
│   ├── Training.xlsx
│   └── Validation.xlsx
├── models/
│   ├── Original_CNN_BiLSTM_Attention.ipynb   # 중간발표용 초안
│   └── Proposal_CNN_BiLSTM_Attention.ipynb   # 최종발표용 개선 ver
├── generation/
│   ├── create_sen.ipynb                       # 문장 생성 모델 학습 & 저장
│   ├── demo_chatbot.ipynb                     # 문장 생성 모델 시연
│   └── sen_gen_model.py                       # EmotionConditionedSeq2Seq 클래스 정의
├── utils.py                                   # vocab 빌드, 텍스트 인코딩 유틸
├── sen_vocab.pkl                              # 학습된 vocab
└── README.md
```

## 모델 선택 근거
### 왜 CNN + BiLSTM + Attention인가

|항목|KoBERT + BiLSTM|CNN + BiLSTM + Attention (채택)|
|---|---|---|
|사전학습|사용|직접 구현|
|문맥 표현|뛰어남|제한적|
|구현 난이도|중 (헤드만 설계)|높음 (전체 구현)|


## 실행 방법
```bash
# 1. 환경 설치
pip install torch pandas openpyxl

# 2. 감정 분류 모델 학습
# models/Proposal_CNN_BiLSTM_Attention.ipynb 실행

# 3. 문장 생성 모델 학습
# generation/create_sen.ipynb 실행

# 4. 챗봇 시연
# generation/demo_chatbot.ipynb 실행
```

## 팀 구성 및 역할
|역할|담당 파트|
|---|---|
|감정 분석|CNN + BiLSTM + Attention 모델 구현, 데이터 전처리, 성능 평가|
|문장 생성|EmotionConditionedSeq2Seq 구현, 클로징 멘트 데이터셋 구성, 시연 코드 작성|
