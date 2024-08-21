# my_tts_project/dataset_creator.py

import os

def create_dataset_directory(base_path):
    wavs_path = os.path.join(base_path, "wavs/")
    os.makedirs(wavs_path, exist_ok=True)
    return wavs_path

def save_transcription(transcript_path, file_name, text):
    with open(transcript_path, "a", encoding="utf-8") as f:
        f.write(f"{file_name}|{text}\n")

def create_dataset(tts, phrases, dataset_path, speaker_wav=None, language="fr"):
    wavs_path = create_dataset_directory(dataset_path)
    transcript_path = os.path.join(dataset_path, "transcript.txt")

    for i, phrase in enumerate(phrases):
        wav_file = f"wav{i+1}.wav"
        wav_file_path = os.path.join(wavs_path, wav_file)

        # Generate speech
        tts.tts_to_file(
            text=phrase,
            file_path=wav_file_path,
            speaker_wav=speaker_wav,
            language=language,
            split_sentences=True
        )

        # Save transcription
        save_transcription(transcript_path, wav_file, phrase)

    print("Jeu de données créé avec succès.")
