from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from rag_pipeline import rag_answer

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/ask")
def ask(data: dict):
    return {"answer": rag_answer(data["question"])}
