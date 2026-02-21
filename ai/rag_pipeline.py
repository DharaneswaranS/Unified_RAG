from ai.vectorstore import similarity_search
from ai.llm import llm
from ai.prompt_templates import RAG_PROMPT
def retrieve(question):
    docs = similarity_search(question, k=5)
    context = "\n".join(d.page_content for d in docs)
    return context
def generate(question, context):
    prompt = RAG_PROMPT.format(
        context=context,
        question=question
    )
    response = llm.invoke(prompt)
    return response.content
