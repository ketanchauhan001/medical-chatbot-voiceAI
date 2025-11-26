# modules/tts_module.py
import os, uuid
# simple TTS using pyttsx3 OR a better model (ai4bharat or Coqui). Below is pyttsx3 fallback.
import pyttsx3

def text_to_speech_file(text, output_dir="static/audio"):
    os.makedirs(output_dir, exist_ok=True)
    filename = f"{uuid.uuid4().hex}.mp3"
    path = os.path.join(output_dir, filename)
    engine = pyttsx3.init()
    engine.save_to_file(text, path)
    engine.runAndWait()
    return path
