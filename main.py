from audio_recorder import record_audio
from speech_to_text import transcribe_audio
from pronunciation_analysis import analyze_pronunciation

import os

def process_audio(reference_text, duration, output_filename):
    """
    Full pipeline: record, transcribe, analyze pronunciation, and return results.
    Parameters:
        reference_text (str): The reference sentence for pronunciation comparison.
        duration (int): Duration of the audio recording in seconds.
        output_filename (str): Name of the audio file to save.
    Returns:
        dict: A dictionary containing the spoken text and pronunciation analysis.
    """
    # Record the user's speech
    audio_file = record_audio(duration=duration, output_filename=output_filename)# Record for 10 seconds
    
    # Transcribe the recorded audio
    spoken_text = transcribe_audio(audio_file)
    
    # Analyze the pronunciation
    analysis = analyze_pronunciation(reference_text, spoken_text)
 
    
    return {'spoken_text': spoken_text, 'analysis': analysis}

# Example Usage
if __name__ == "__main__":
    reference_sentence = "The quick brown fox jumps over the lazy dog"
    result = process_audio(reference_sentence, duration=10, output_filename="my_audio.wav")
    
    print("\nSpoken Text:", result['spoken_text'])
    print("\nPronunciation Analysis:")
    for entry in result['analysis']:
        print(entry)