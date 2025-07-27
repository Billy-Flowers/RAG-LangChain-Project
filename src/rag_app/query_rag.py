from dataclasses import dataclass
from typing import List
from langchain.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama
from rag_app.get_chroma_db import get_chroma_db

PROMPT_TEMPLATE = """
Answer the question based only on the following context:

{context}

---

Answer the question based on the above context: {question}
"""

OLLAMA_MODEL_ID = "phi3:mini" #change this based on your llama model


@dataclass
class QueryResponse:
    query_text: str
    response_text: str
    sources: List[str]

model = ChatOllama(model=OLLAMA_MODEL_ID)

def query_rag(query_text: str) -> QueryResponse:
    db = get_chroma_db()

    # Search the DB.
    results = db.similarity_search_with_score(query_text, k=4)
    context_text = "\n\n---\n\n".join([doc.page_content for doc, _score in results])
    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    prompt = prompt_template.format(context=context_text, question=query_text)

    response = model.invoke(prompt)
    response_text = response.content

    sources = [doc.metadata.get("id", None) for doc, _score in results]
    print(f"Response: {response_text}\nSources: {sources}")

    return QueryResponse(
        query_text=query_text, response_text=response_text, sources=sources
    )


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        query_text = sys.argv[1]
    else:
        query_text = "What's your model name lil bro?"
    
    query_rag(query_text)
