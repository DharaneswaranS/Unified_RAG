import streamlit as st
import os
import uuid
import sys

# Add project root to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from langchain_text_splitters import RecursiveCharacterTextSplitter
from processors.document_processor import process_document
from processors.json_processor import process_json
from processors.csv_processor import process_csv
from processors.sql_processor import process_sqlite
from utils.file_detector import detect_file_type
from ai.vectorstore import get_vectorstore
from ai.rag_pipeline import generate

# ---------------- Streamlit Config ----------------
st.set_page_config(page_title="Unified Knowledge Assistant", layout="wide")
st.title("🧠 Unified Knowledge Assistant")

# ---------------- Session State ----------------
if "collection_id" not in st.session_state:
    st.session_state.collection_id = None

if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------------- File Upload ----------------
uploaded_file = st.sidebar.file_uploader(
    "Upload documents (PDF, DOCX, PPTX, TXT, JSON, CSV, DB)",
    type=["pdf", "docx", "pptx", "txt", "json", "csv", "db"]
)

if uploaded_file:
    file_path = os.path.join("temp_upload", uploaded_file.name)
    os.makedirs("temp_upload", exist_ok=True)

    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    file_type = detect_file_type(file_path)

    if file_type == "document":
        docs = process_document(file_path)
    elif file_type == "json":
        docs = process_json(file_path)
    elif file_type == "csv":
        docs = process_csv(file_path)
    elif file_type == "sql":
        docs = process_sqlite(file_path)
    else:
        st.error("Unsupported file type")
        st.stop()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=150
    )

    chunks = splitter.split_documents(docs)

    # Create new isolated collection
    collection_id = str(uuid.uuid4())
    st.session_state.collection_id = collection_id

    vectordb = get_vectorstore(collection_id)
    vectordb.add_documents(chunks)

    st.success("File processed successfully!")

# ---------------- Chat Interface ----------------
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("Ask anything from uploaded knowledge..."):

    if not st.session_state.collection_id:
        st.warning("Please upload a file first.")
        st.stop()

    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    vectordb = get_vectorstore(st.session_state.collection_id)
    docs = vectordb.similarity_search(prompt, k=5)
    context = "\n".join(d.page_content for d in docs)

    answer = generate(prompt, context)

    with st.chat_message("assistant"):
        st.markdown(answer)

    st.session_state.messages.append({"role": "assistant", "content": answer})