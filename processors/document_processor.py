from langchain_community.document_loaders import (
    PyPDFLoader,
    Docx2txtLoader,
    TextLoader,
    UnstructuredPowerPointLoader
)
def process_document(path):
    if path.endswith(".pdf"):
        docs = PyPDFLoader(path).load()
    elif path.endswith(".docx"):
        docs = Docx2txtLoader(path).load()
    elif path.endswith(".pptx"):
        docs = UnstructuredPowerPointLoader(path).load()
    else:
        docs = TextLoader(path).load()
    return docs
