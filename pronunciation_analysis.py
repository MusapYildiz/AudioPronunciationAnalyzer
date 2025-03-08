import nltk
from nltk.corpus import cmudict

# Download CMU Pronouncing Dictionary (first time only)
nltk.download('cmudict')
phoneme_dict = cmudict.dict()

def get_phonemes(word):
    """
    Fetch phonemes for a given word from the CMU dictionary.
    Parameters:
        word (str): The word whose phonemes are needed.
    Returns:
        list: A list of phonemes for the given word.
    """
    word = word.lower()
    return phoneme_dict.get(word, [["UNKNOWN"]])[0]

def analyze_pronunciation(reference_text, spoken_text):
    """
    Compare expected and spoken phonemes.
    Parameters:
        reference_text (str): The reference sentence (correct text).
        spoken_text (str): The transcribed text from the audio.
    Returns:
        list: A list of pronunciation accuracy results for each word.
    """
    reference_words = reference_text.lower().split()
    spoken_words = spoken_text.lower().split()
    
    analysis = []
    for ref_word, spoken_word in zip(reference_words, spoken_words):
        ref_phonemes = get_phonemes(ref_word)
        spoken_phonemes = get_phonemes(spoken_word)
        accuracy = compare_phonemes(ref_phonemes, spoken_phonemes)
        
        analysis.append({
            'word': ref_word,
            'expected_phonemes': ref_phonemes,
            'spoken_phonemes': spoken_phonemes,
            'accuracy': accuracy
        })
    
    return analysis

def compare_phonemes(ref_phonemes, spoken_phonemes):
    """
    Calculate similarity score between two phoneme sequences.
    Parameters:
        ref_phonemes (list): List of expected phonemes.
        spoken_phonemes (list): List of spoken phonemes.
    Returns:
        float: Accuracy percentage between 0 and 100.
    """
    if ref_phonemes == ["UNKNOWN"] or spoken_phonemes == ["UNKNOWN"]:
        return 0.0  # Unable to analyze
    
    correct_matches = sum(1 for r, s in zip(ref_phonemes, spoken_phonemes) if r == s)
    return round((correct_matches / max(len(ref_phonemes), len(spoken_phonemes))) * 100, 2)