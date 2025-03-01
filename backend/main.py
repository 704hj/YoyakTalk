from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI()

# Summarizer (예: 영어 BART)
model_name = "facebook/bart-large-cnn"
summarizer = pipeline("summarization", model=model_name)

class TextInput(BaseModel):
    text: str 

@app.get("/")
def read_root(): 
    return {"message": "연결 성공!!! Python 3.11 & FastAPI!"}

@app.post("/summarize")
def summarize_text(data: TextInput):
    summary = summarizer(
        data.text,
        max_length=50,
        min_length=20,
        do_sample=False
    )
    return {"summary": summary[0]["summary_text"]}
