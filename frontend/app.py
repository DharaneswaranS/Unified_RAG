import streamlit as st
from chat_ui import render_chat
from api_client import upload_file
st.set_page_config(page_title="Unified RAG Assistant", page_icon="🧠", layout="wide")
st.title("🧠 Unified Knowledge Assistant")
st.sidebar.header("Upload Knowledge Sources")
uploaded_files = st.sidebar.file_uploader(
    "Upload documents (PDF, DOCX, PPTX, TXT, JSON, CSV, DB)",
    accept_multiple_files=True
)
if uploaded_files:
    for file in uploaded_files:
        with st.spinner(f"Uploading {file.name}..."):
            res = upload_file(file)
            st.sidebar.success(res)
st.sidebar.markdown("---")
st.sidebar.info("After uploading, ask questions in the chat.")
render_chat()
