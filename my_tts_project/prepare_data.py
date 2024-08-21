# my_tts_project/prepare_data.py

def load_phrases(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        phrases = [line.strip() for line in file if line.strip()]
    return phrases