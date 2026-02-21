import pandas as pd
from langchain_core.documents import Document

def process_csv(path):
    df = pd.read_csv(path)
    docs = []
    for _, row in df.iterrows():
        text = ", ".join(f"{col} is {val}" for col, val in row.items())
        docs.append(Document(page_content=text))
    return docs
