import json
from langchain_core.documents import Document
def process_json(path):
    data = json.load(open(path))
    docs = []
    def flatten(obj, prefix=""):
        if isinstance(obj, dict):
            for k, v in obj.items():
                flatten(v, prefix + k + " ")
        elif isinstance(obj, list):
            for item in obj:
                flatten(item, prefix)
        else:
            docs.append(Document(page_content=f"{prefix}is {obj}"))
    flatten(data)
    return docs
