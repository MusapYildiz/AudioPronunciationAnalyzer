# Speech Pronunciation Analysis

This project records audio from the user, converts it to text using OpenAI's Whisper model, and analyzes the pronunciation by comparing the spoken words to a reference sentence. It checks the phonetic accuracy of the spoken words using the CMU Pronouncing Dictionary.

## Features

- **Record Audio**: Record a user's speech using the microphone.
- **Speech-to-Text**: Convert the recorded audio into text using Whisper.
- **Pronunciation Analysis**: Compare the spoken text with a reference sentence and calculate phonetic accuracy.

## Setup

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/speech-pronunciation-analysis.git
   cd speech-pronunciation-analysis
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   
## System Requirements

Before you begin, make sure your system is prepared by installing the necessary dependencies.

### Install `ffmpeg`

This project requires `ffmpeg` to be installed on your system for audio and video processing. You can install `ffmpeg` on Linux-based systems using the following commands:

   ```bash
   sudo apt update
   sudo apt install ffmpeg
   
## Usage

You can run the program by executing main.py. It will record audio, transcribe it to text, and analyze the pronunciation against the reference sentence.
   ```bash
   python main.py
   
## Example Output
   ```bash
   Spoken Text: The quick brown fox jumps over the lazy dog
Pronunciation Analysis:
{'word': 'the', 'expected_phonemes': ['T', 'HH', 'AH'], 'spoken_phonemes': ['T', 'HH', 'AH'], 'accuracy': 100.0}
{'word': 'quick', 'expected_phonemes': ['K', 'W', 'IH', 'K'], 'spoken_phonemes': ['K', 'W', 'IH', 'K'], 'accuracy': 100.0}
...

## Author
	https://github.com/MusapYildiz

