import streamlit as st
from langchain_groq import ChatGroq

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0,
    groq_api_key=st.secrets["GROQ_API_KEY"]
)