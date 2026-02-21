import os
DOCUMENT_TYPES = {".pdf", ".docx", ".pptx", ".txt"}
JSON_TYPES = {".json", ".xml"}
CSV_TYPES = {".csv"}
SQL_TYPES = {".db", ".sqlite", ".sqlite3"}
def detect_file_type(path: str):
    ext = os.path.splitext(path)[1].lower()
    if ext in DOCUMENT_TYPES:
        return "document"
    if ext in JSON_TYPES:
        return "json"
    if ext in CSV_TYPES:
        return "csv"
    if ext in SQL_TYPES:
        return "sql"
    return "unsupported"
