# 🧠 Emotion Classification ResponseGen
감성 대화 말뭉치를 활용하여 사용자의 감정을 분류 학습하고, 대화 흐름에 따른 감정 변화 분석과 감정 기반 응답 생성을 수행하는 정신상담 AI를 개발하는 프로젝트

### 정신상담 AI : 감정 분석 & 문장 생성 Project 파일 구성 
-----
```markdown
Mental_wellness_chatbot/
    ├── DATASET/
		    ├── Training.xlsx
		    ├── Validation.xlsx
    ├── Original_CNN_BiLSTM_Attention.ipynb      # -중간발표용 감정 분석 모델 (초안)
    ├── Proposal_CNN_BiLSTM_Attention.ipynb      # -최종발표용 감정 분석 모델 (개선 ver)
    ├── create_sen.ipynb                         # -문장 생성 모델 학습 & 저장 ipynb
    ├── demo_chatbot.ipynb                       # -문장 생성 모델 시연 ipynb
    ├── sen_gen_model.py                         # -문장 생성 모델 class 정의 파일 (import용)
    ├── sen_vocab.pkl                            # -vocab
    ├── utils.py
```
