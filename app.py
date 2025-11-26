# app.py
import os
from flask import Flask, render_template, request, jsonify, send_from_directory
from modules.db_module import load_vector_db
from modules.rag_pipeline import rag_query
from modules.stt_module import speech_bytes_to_text  # updated function name (see below)
from modules.tts_module import text_to_speech_file   # returns filepath to audio file

app = Flask(__name__, static_folder="static", template_folder="templates")

DB_FOLDER = "vector_db"
AUDIO_FOLDER = os.path.join("static", "audio")
os.makedirs(AUDIO_FOLDER, exist_ok=True)

# Serve index page
@app.route("/")
def index():
    return render_template("index.html")

# Chat (text mode)
@app.route("/chat", methods=["POST"])
def chat_text():
    data = request.get_json()
    if not data or "query" not in data:
        return jsonify({"error": "No query provided"}), 400

    query = data["query"]
    # Load vectordb once per request (or cache it globally)
    vectordb = load_vector_db(DB_FOLDER)
    if vectordb is None:
        return jsonify({"error": "Vector DB not found. Run main.py first."}), 500

    answer = rag_query(query, vectordb)
    return jsonify({"answer": answer})

# Chat (voice mode) - expects multipart/form-data with field name 'audio'
@app.route("/chat-voice", methods=["POST"])
def chat_voice():
    if "audio" not in request.files:
        return jsonify({"error": "No audio file uploaded"}), 400

    audio_file = request.files["audio"]
    audio_bytes = audio_file.read()

    # convert audio bytes -> text via STT
    text_query = speech_bytes_to_text(audio_bytes)
    if not text_query:
        return jsonify({"error": "STT failed"}), 500

    vectordb = load_vector_db(DB_FOLDER)
    if vectordb is None:
        return jsonify({"error": "Vector DB not found. Run main.py first."}), 500

    answer_text = rag_query(text_query, vectordb)

    # TTS: convert answer to audio file and return URL
    audio_path = text_to_speech_file(answer_text, output_dir=AUDIO_FOLDER)
    audio_url = "/" + audio_path.replace("\\", "/")  # accessible path for browser

    return jsonify({"query_text": text_query, "answer": answer_text, "audio": audio_url})

# Serve static audio files (if Flask static_folder not configured)
@app.route("/static/audio/<path:filename>")
def serve_audio(filename):
    return send_from_directory(AUDIO_FOLDER, filename)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
