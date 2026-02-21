from langchain_chroma import Chroma
from ai.embeddings import embeddings
from backend.config import VECTOR_DB_PATH
import os
os.makedirs(VECTOR_DB_PATH, exist_ok=True)
def get_vectorstore(collection_name: str):
    return Chroma(
        persist_directory=VECTOR_DB_PATH,
        collection_name=collection_name,
        embedding_function=embeddings
    )
def add_documents(docs, collection_name: str):
    vectordb = get_vectorstore(collection_name)
    vectordb.add_documents(docs)
def similarity_search(query, collection_name: str, k=5):
    vectordb = get_vectorstore(collection_name)
    return vectordb.similarity_search(query, k=k)