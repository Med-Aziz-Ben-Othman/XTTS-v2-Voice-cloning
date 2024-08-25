import os 
from my_tts_project.prepare_data import load_phrases
from my_tts_project.tts_generator import initialize_tts_model, generate_speech
from my_tts_project.dataset_creator import create_dataset_directory, save_transcription
from my_tts_project.visualization import plot_metrics
from way_sdk_llama3.llama3_gentext import llama3_gentext

def main():
    # Initialize the ModelManager with the model name and filepath
    model_manager = llama3_gentext(model_name="Assistant_bot_fr", modelfilepath="voice cloning/way_sdk_llama3/modelfile.txt")

    # Create or check model creation
    model_manager.create_model_if_needed()

    # Generate output_gen.txt using the created model
    model_manager.generate_response(prompt='pouvez vous me donner 5 réponse comme si vous etes en train de répondre un client en francais', output_file='voice cloning/gen_data_from_llama3/output_generated_fr_utf8.txt')

    # Path to the phrases text file
    phrases_file_path = "voice cloning/data/output_generated_fr_utf8.txt"
    phrases = load_phrases(phrases_file_path)

    dataset_path = "./voice cloning/dataset_final/"
    speaker_wav = ["./voice cloning/source_voice/dora.wav"]

    # Initialize TTS model
    tts = initialize_tts_model(gpu=False)

    # Create dataset directory
    wavs_path = create_dataset_directory(dataset_path)
    transcript_path = os.path.join(dataset_path, "transcript.txt")

    process_times = []
    real_time_factors = []

    # Generate dataset and collect metrics
    for i, phrase in enumerate(phrases):
        wav_file = f"wav-fr{i+1}.wav"
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
