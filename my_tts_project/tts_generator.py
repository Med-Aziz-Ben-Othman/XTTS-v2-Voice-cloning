# my_tts_project/tts_generator.py

from TTS.api import TTS
import time

def initialize_tts_model(gpu=False):
    return TTS("tts_models/multilingual/multi-dataset/xtts_v2", gpu=gpu)

def generate_speech(tts, text, output_path, speaker_wav=None, language="fr"):
    start_time = time.time()
    
    # Generate the speech
    tts.tts_to_file(
        text=text,
        file_path=output_path,
        speaker_wav=speaker_wav,
        language=language,
        split_sentences=True
    )
    
    processing_time = time.time() - start_time
    real_time_factor = processing_time / len(text.split())
    
    return processing_time, real_time_factor
