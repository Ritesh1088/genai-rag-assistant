import faiss
import numpy as np
from embeddings import embed_text
from transformers import pipeline

# ✅ Correct pipeline for T5
llm = pipeline(
    "text2text-generation",
    model="google/flan-t5-base",
    max_length=256
)

# Load documents
documents = open("data/knowledge.txt", encoding="utf-8").read().split("\n")

# Create embeddings
doc_embeddings = embed_text(documents)
doc_embeddings = np.array(doc_embeddings).astype("float32")

# FAISS index
dimension = doc_embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(doc_embeddings)

def rag_answer(query: str):
    # Embed query
    query_embedding = embed_text([query])
    query_embedding = np.array(query_embedding).astype("float32")

    # Search top 2 docs
    _, idx = index.search(query_embedding, 2)

    context = " ".join([documents[i] for i in idx[0]])

    prompt = f"""
Answer the question using the context below.

Context:
{context}

Question:
{query}

Answer:
"""

    result = llm(prompt)
    return result[0]["generated_text"]
