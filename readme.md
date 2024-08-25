# Voice Cloning Project
* **Overview**
This project allows you to generate voice clones from given text phrases using a TTS (Text-to-Speech) model. The main.py script orchestrates the entire process, from text generation to voice synthesis, and saves the generated speech files.

* **Setup**
Before running the project, make sure you have Python installed and follow the steps below to set up your environment.

1. Download the SDK:
First, download the SDK to your local machine. You can do this by cloning the repository or downloading the ZIP file from the repository page.
~~~sh
git clone git@gitlab.com:llms-tts/way-sdk.git
~~~
2. Navigate to the SDK Directory: Change your directory to the location of the downloaded SDK.

3. Run the following command to install the SDK:
~~~sh
pip install -e . 
~~~
now the sdk is ready to be used, let's set up the voice cloning project: 
1. Install Dependencies
First, you'll need to install the required Python packages. These are listed in the requirements.txt file.

bash
Copier le code
~~~sh
pip install -r requirements.txt
~~~
2. Run the Main Script
Once the dependencies are installed, you can run the main script to start the voice cloning process:

bash
Copier le code
~~~sh
python main.py
~~~
* **Project Structure**
* ***main.py***
The main script that handles the entire voice cloning process.
* ***requirements.txt***
Contains all the necessary Python packages.
* ***my_tts_project/***
Contains the modules for data preparation, TTS model initialization, and visualization.
* ***voice cloning/***
Directory where output files, datasets, and other resources are stored.
* **How It Works**
* ***Text Generation*** 
The script generates French text using a pre-trained model.
* ***Data Cleaning***
The generated text is cleaned and pre-processed to improve clarity during voice synthesis.
* ***Voice Synthesis***
The cleaned text is passed to a TTS model, which generates corresponding speech files.
* ***Output*** 
The generated speech files and transcriptions are saved in the specified directory.
* **Customization**
You can modify the text generation prompt in main.py to change the output.
Adjust the data cleaning process in my_tts_project/prepare_data.py to better suit your needs.
Contributing

Feel free to fork this project, open issues, and submit pull requests. Contributions are welcome!