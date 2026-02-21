from flask import current_app
from ai.vectorstore import similarity_search
def retrieve_context(question):
    collection_id = current_app.config.get("ACTIVE_COLLECTION")
    if not collection_id:
        return ""
    docs = similarity_search(question, collection_id, k=5)
    return "\n".join(d.page_content for d in docs)