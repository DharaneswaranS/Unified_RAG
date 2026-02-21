# Unified RAG Intelligent Knowledge Assistant

A multi-format Retrieval Augmented Generation (RAG) system that allows users to query knowledge across:

- PDFs, DOCX, PPTX, TXT
- JSON & XML
- CSV datasets
- SQLite databases

using a single conversational interface.

## Tech Stack
Frontend: Streamlit
Backend: Flask
AI: LangChain + Groq
Vector DB: Chroma
Embeddings: Sentence Transformers

## Features
- Upload multiple data sources
- Persistent knowledge storage
- Context-aware question answering
- Source grounded responses

## Run

Start backend:
python backend/app.py

Start frontend:
streamlit run frontend/app.py
