# main.py
import os 
from my_tts_project.prepare_data import load_phrases
from my_tts_project.tts_generator import initialize_tts_model, generate_speech
from my_tts_project.dataset_creator import create_dataset_directory, save_transcription
from my_tts_project.visualization import plot_metrics

def main():
  # Path to the phrases text file
    phrases_file_path = "./data/phrases.txt"
    phrases = load_phrases(phrases_file_path)

    dataset_path = "./MyTTSDataset/"
    speaker_wav = ["./source_voice/dora.wav"]

    # Initialize TTS model
    tts = initialize_tts_model(gpu=False)

    # Create dataset directory
    wavs_path = create_dataset_directory(dataset_path)
    transcript_path = os.path.join(dataset_path, "transcript.txt")

    process_times = []
    real_time_factors = []

    # Generate dataset and collect metrics
    for i, phrase in enumerate(phrases):
        wav_file = f"wav{i+1}.wav"
        wav_file_path = os.path.join(wavs_path, wav_file)

        # Generate speech and get metrics
        processing_time, real_time_factor = generate_speech(
            tts, 
            text=phrase, 
            output_path=wav_file_path, 
            speaker_wav=speaker_wav, 
            language="fr"
        )

        process_times.append(processing_time)
        real_time_factors.append(real_time_factor)

        # Save transcription
        save_transcription(transcript_path, wav_file, phrase)
    
    # Visualize the metrics
    plot_metrics(process_times, real_time_factors)


if __name__ == "__main__":
    main()
