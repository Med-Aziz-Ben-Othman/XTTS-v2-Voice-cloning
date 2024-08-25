# my_tts_project/prepare_data.py

def replace_characters(text, replacements):
    for old_char, new_char in replacements.items():
        text = text.replace(old_char, new_char)
    return text

def load_phrases(file_path, encoding='utf-8'):

    # Define the replacements
    replacements = {
        'Ã»': 'u',
        'Ã©': 'ai',
        'Ã¨': 'e',
        'Ã': 'à',
    }
    with open(file_path, 'r', encoding=encoding) as file:
        phrases = [replace_characters(line.strip(), replacements) for line in file if line.strip()]
    
    return phrases

