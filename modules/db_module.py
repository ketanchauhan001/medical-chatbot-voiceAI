# modules/db_module.py
import os
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_huggingface.embeddings import HuggingFaceEmbeddings

EMBED_MODEL = "sentence-transformers/all-mpnet-base-v2"
embedder = HuggingFaceEmbeddings(model_name=EMBED_MODEL)

def create_vector_db(text, db_folder):
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    chunks = splitter.split_text(text)
    vectordb = FAISS.from_texts(chunks, embedder)
    os.makedirs(db_folder, exist_ok=True)
    vectordb.save_local(db_folder)

def load_vector_db(db_folder):
    if not os.path.exists(db_folder):
        return None
    return FAISS.load_local(db_folder, embedder, allow_dangerous_deserialization=True)
