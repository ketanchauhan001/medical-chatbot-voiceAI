# modules/pdf_processor.py
import os
from PyPDF2 import PdfReader

def extract_text_from_pdfs(folder_path):
    text = ""
    if not os.path.exists(folder_path):
        return text
    for fname in os.listdir(folder_path):
        if fname.lower().endswith(".pdf"):
            path = os.path.join(folder_path, fname)
            reader = PdfReader(path)
            for page in reader.pages:
                txt = page.extract_text()
                if txt:
                    text += txt + "\n"
    return text
