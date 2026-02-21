from langchain_text_splitters import RecursiveCharacterTextSplitter
from ai.vectorstore import add_documents
import uuid
from utils.file_detector import detect_file_type
from processors.document_processor import process_document
from processors.json_processor import process_json
from processors.csv_processor import process_csv
from processors.sql_processor import process_sqlite
from flask import current_app
splitter = RecursiveCharacterTextSplitter(
    chunk_size=800,
    chunk_overlap=150
)
def ingest_file(path):
    collection_id = str(uuid.uuid4())
    current_app.config["ACTIVE_COLLECTION"] = collection_id
    file_type = detect_file_type(path)
    if file_type == "document":
        docs = process_document(path)
    elif file_type == "json":
        docs = process_json(path)
    elif file_type == "csv":
        docs = process_csv(path)
    elif file_type == "sql":
        docs = process_sqlite(path)
    else:
        return "Unsupported file type"
    chunks = splitter.split_documents(docs)
    add_documents(chunks, collection_id)
    return f"Ingested {len(chunks)} chunks"