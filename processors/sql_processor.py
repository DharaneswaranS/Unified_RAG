import sqlite3
from langchain_core.documents import Document
def process_sqlite(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    docs = []
    tables = cursor.execute(
        "SELECT name FROM sqlite_master WHERE type='table';"
    ).fetchall()
    for (table,) in tables:
        columns = [c[1] for c in cursor.execute(f"PRAGMA table_info({table})")]
        rows = cursor.execute(f"SELECT * FROM {table}").fetchall()
        for row in rows:
            text = ", ".join(f"{c} is {v}" for c,v in zip(columns,row))
            docs.append(Document(page_content=text))
    return docs
