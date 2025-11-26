# main.py
import os
from modules.pdf_processor import extract_text_from_pdfs
from modules.db_module import create_vector_db

PDF_FOLDER = "pdfs"
DB_FOLDER = "vector_db"

def build_vector_database():
    print("📄 Extracting text from PDFs...")
    text_data = extract_text_from_pdfs(PDF_FOLDER)

    if not text_data.strip():
        print("❌ No text found in PDFs. Put PDF files inside /pdfs folder.")
        return False

    print("📦 Creating vector database...")
    os.makedirs(DB_FOLDER, exist_ok=True)
    create_vector_db(text_data, DB_FOLDER)
    print("✅ Vector DB created successfully!")
    return True

if __name__ == "__main__":
    print("=== RUNNING PDF → VECTOR PREPROCESSOR ===")
    if not os.path.exists(DB_FOLDER) or not os.listdir(DB_FOLDER):
        ok = build_vector_database()
        if not ok:
            exit(1)
    else:
        print("⚠️ vector_db already exists. If you want to rebuild, delete the folder and re-run this script.")
    print("Done. You can now run: python app.py")
