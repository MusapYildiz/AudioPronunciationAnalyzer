import pyaudio
import wave

def record_audio(duration, output_filename, sample_rate=16000):
    """
    Record audio from the microphone for a given duration and save it to a file.
    Parameters:
        duration (int): Length of the recording in seconds.
        sample_rate (int): The sample rate of the audio.
        output_filename (str): Name of the file where the audio will be saved.
    Returns:
        str: The path to the saved audio file.
    """
    p = pyaudio.PyAudio()

    # Set up audio stream
    stream = p.open(format=pyaudio.paInt16,
                    channels=1,
                    rate=sample_rate,
                    input=True,
                    frames_per_buffer=1024)
    print(f"Recording for {duration} seconds...")
    frames = []

    for _ in range(0, int(sample_rate / 1024 * duration)):
        data = stream.read(1024)
        frames.append(data)

    print("Recording finished.")
    stream.stop_stream()
    stream.close()
    p.terminate()

    # Save the recorded audio to a .wav file
    with wave.open(output_filename, 'wb') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(p.get_sample_size(pyaudio.paInt16))
        wf.setframerate(sample_rate)
        wf.writeframes(b''.join(frames))
    
    return output_filename