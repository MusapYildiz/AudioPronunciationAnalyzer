import whisper

# Initialize Whisper model
model = whisper.load_model("base")

def transcribe_audio(audio_path):
    """
    Convert speech to text using OpenAI Whisper model.
    Parameters:
        audio_path (str): Path to the audio file to transcribe.
    Returns:
        str: The transcribed text.
    """
    print("Transcribing audio...")
    result = model.transcribe(audio_path)
    return result['text']