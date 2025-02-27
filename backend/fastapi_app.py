from fastapi import FastAPI
from transformers import pipeline

app = FastAPI()

# 모델 명시적으로 지정
model_name = "facebook/bart-large-cnn"
summarizer = pipeline("summarization", model=model_name)

@app.get("/")
def read_root():
    return {"message": "요약Talk 백엔드 실행 중"}

@app.post("/summarize/")
def summarize_text(text: str):
    summary = summarizer(text, max_length=150, min_length=50, do_sample=False)
    return {"summary": summary[0]["summary_text"]}
