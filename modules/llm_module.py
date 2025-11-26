# modules/llm_module.py
from langchain_community.llms import Ollama

# Use deepseek-r1:1.5b because it's small enough for your system
llm = Ollama(model="deepseek-r1:1.5b")

def ask_llm(prompt):
    """
    Sends a prompt to the LLM and returns the response.
    """
    resp = llm.invoke(prompt)
    return resp
