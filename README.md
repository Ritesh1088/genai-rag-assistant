# 🧠 NeuroRAG – GenAI Knowledge Assistant

A Retrieval-Augmented Generation (RAG) based AI assistant that answers user queries
using contextual knowledge, semantic search (FAISS), and large language models.

## 🚀 Features
- Semantic Search using FAISS
- Sentence Transformers Embeddings
- FLAN-T5 LLM
- Image Retrieval via Unsplash API
- Modern 3D Frontend UI
- FastAPI Backend

## 🏗️ Architecture
Frontend → FastAPI → RAG Pipeline → FAISS → LLM → Response

## 🏗️ Project Structure
genai-rag-assistant/
│
├── backend/
│ ├── app.py
│ ├── embeddings.py
│ ├── rag_pipeline.py
│ ├── requirements.txt
│
├── frontend/
│ ├── index.html
│ ├── style.css
│ ├── script.js
│
├── screenshots/
│ ├── ui.png
│ ├── api.png
│
└── README.md

yaml
Copy code

---

## ⚙️ How to Run Locally

### Backend
```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn app:app --reload
http://127.0.0.1:8000/docs


3️⃣ Frontend

Open frontend/index.html in browser
