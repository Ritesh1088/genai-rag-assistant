import os
import faiss
import numpy as np
from embeddings import embed_text
from transformers import pipeline

# Load LLM
llm = pipeline(
    "text2text-generation",
    model="google/flan-t5-base",
    max_length=256
)

# Load knowledge file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "data", "knowledge.txt")

with open(DATA_PATH, encoding="utf-8") as f:
    documents = [d for d in f.read().split("\n") if d.strip()]

# Create embeddings
doc_embeddings = np.array(embed_text(documents)).astype("float32")

# FAISS index
index = faiss.IndexFlatL2(doc_embeddings.shape[1])
index.add(doc_embeddings)

def rag_answer(query: str):
    try:
        query_vec = np.array(embed_text([query])).astype("float32")
        _, idx = index.search(query_vec, 3)

        sources = [documents[i] for i in idx[0]]
        context = " ".join(sources)

        prompt = f"""
Answer the question using the context below in 3–4 clear sentences.

Context:
{context}

Question:
{query}

Answer:
"""

        response = llm(prompt)[0]["generated_text"]

        return {
            "answer": response,
            "sources": sources
        }

    except Exception as e:
        return {
            "error": str(e)
        }
