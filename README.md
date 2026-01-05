# 🧠 NeuroRAG – GenAI Knowledge Assistant

NeuroRAG is a Retrieval-Augmented Generation (RAG) based AI assistant that answers
user questions using contextual knowledge stored in documents.  
It combines **FAISS vector search** with a **Transformer-based language model**
and an **animated, modern frontend UI**.

---

## 🚀 Features

- 🔍 **Retrieval-Augmented Generation (RAG)**
- 📚 **FAISS-based semantic document search**
- 🤖 **Google FLAN-T5 language model**
- 🧠 **Context-aware answers (3–4 sentences)**
- 📌 **Source citation for transparency**
- ⚠️ **Error handling & offline fallback**
- ⏳ **Loading spinner for better UX**
- 🎨 **Animated glassmorphism UI**
- 🌐 **FastAPI backend with REST API**

---

## 🏗️ Architecture

Frontend (HTML/CSS/JS)
↓
FastAPI Backend
↓
FAISS Vector Search
↓
LLM (FLAN-T5)
↓
Response


## 🏗️ Project Structure
genai-rag-assistant/
│
├── backend/
│ ├── app.py # FastAPI server
│ ├── rag_pipeline.py # RAG logic (FAISS + LLM)
│ ├── embeddings.py # Text embeddings
│ └── data/
│ └── knowledge.txt # Knowledge base
│
└── frontend/
├── index.html # UI layout
├── style.css # Animated styles
└── script.js # API interaction
│
└── README.md

---

## ⚙️ Tech Stack

**Backend**
- Python
- FastAPI
- FAISS
- HuggingFace Transformers
- NumPy

**Frontend**
- HTML5
- CSS3 (Glassmorphism + Animations)
- Vanilla JavaScript

---

## 🧪 How It Works

1. User enters a question in the UI
2. Question is converted into embeddings
3. FAISS retrieves top relevant document chunks
4. Retrieved context is passed to the LLM
5. LLM generates a contextual answer
6. Sources used are displayed for explainability

---

## ▶️ How to Run Locally

### 🔹 Backend Setup

```bash
cd backend
python -m venv venv
venv\Scripts\activate   # Windows
pip install -r requirements.txt
uvicorn app:app --reload

http://127.0.0.1:8000/docs


🔹 Frontend

Open frontend/index.html in browser
