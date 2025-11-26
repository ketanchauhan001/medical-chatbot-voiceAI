from faster_whisper import WhisperModel
import tempfile
import soundfile as sf

# Load faster-whisper model
model = WhisperModel("base", device="cpu", compute_type="int8")


def speech_bytes_to_text(audio_bytes):
    """
    Convert raw audio bytes to text using faster-whisper.
    """

    # Save the incoming bytes to a temporary WAV file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as f:
        f.write(audio_bytes)
        audio_path = f.name

    # Transcribe using faster-whisper
    segments, info = model.transcribe(audio_path)

    # Join final text
    text = " ".join([seg.text for seg in segments])
    return text.strip()
