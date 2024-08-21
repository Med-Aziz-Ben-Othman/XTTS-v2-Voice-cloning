# TTS Project

## Overview

This project involves text-to-speech (TTS) processing using a multilingual TTS model. It reads phrases from a text file, generates speech audio files, and saves transcriptions. Additionally, it visualizes processing metrics such as processing time and real-time factor.

## Project Structure

- **`main.py`**: The main script that initializes the TTS model, creates datasets, generates speech, saves transcriptions, and plots metrics.
- **`my_tts_project/`**: Contains the core project modules.
  - **`tts_generator.py`**: Functions for initializing the TTS model and generating speech.
  - **`dataset_creator.py`**: Functions for creating the dataset directory and saving transcriptions.
  - **`visualization.py`**: Functions for plotting metrics.
  - **`utils.py`**: Utility functions for text formatting.
- **`phrases.txt`**: A text file containing phrases to be used for TTS processing.
- **`requirements.txt`**: A file listing the required Python packages for the project.
