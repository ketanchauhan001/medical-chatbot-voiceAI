# modules/rag_pipeline.py
from modules.llm_module import ask_llm

def rag_query(query, vectordb, top_k=3):
    retriever = vectordb.as_retriever(search_kwargs={"k": top_k})
    docs = retriever.invoke(query)
    context = "\n\n".join([d.page_content for d in docs])
    prompt = f"Use ONLY the context below to answer the question.\n\nContext:\n{context}\n\nQuestion: {query}\nAnswer:"
    return ask_llm(prompt)
