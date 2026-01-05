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
    query = data.get("question")
    if not query:
        return {"error": "Question is required"}

    return rag_answer(query)
