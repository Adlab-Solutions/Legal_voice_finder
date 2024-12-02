# Legal Application Finder Using Voice

It is a Streamlit application that records the user's voice to extract relevant information and generate a legal document tailored to their specific situation. The application processes the voice input and prompts the user for key details required for the legal document.

## Description

This is a Streamlit application that records the user's voice to extract relevant information and generate a legal document tailored to their specific situation. The application processes the voice input to identify key details and creates a comprehensive document based on the user's needs.

Upon launching the app, users are presented with three buttons: "Start Recording," "End Recording," and "Reset."

- Start Recording: Begins audio recording, provided no other audio is already present in the app.
- End Recording: Stops the recording if audio was being captured. It allows users to play back the recording, and if satisfied with its quality and content, they can click the "Download Audio" button. This downloads the audio and triggers a function to transcribe and translate it, displaying the translated text.
- Reset: Clears all internal variables, including the audio, transcription, and translation.

If the user is satisfied with the translated text, they can click the "Start Searching" button. This takes the translated text to identify its legal purpose, which is then used to search a vector database (Faiss) comprised of multiple legal templates for matching legal template filenames. The app displays six filenames, allowing the user to select one.

After selecting a template, a dynamic list of fields is generated. These fields correspond to placeholders already present in the selected legal template, prompting the user to input the necessary information for the legal document. Once all required information is entered, the user can click "Down", which replaces the placeholders in the template with the actual information provided by the user. The final legal document is then created and saved in the final_word directory as a complete legal file.

This project uses Whisper AI for voice recognition to transcribe and translate audio, supporting multiple languages. Even if the audio is a mix of English and another language, it ensures a complete English translation. The vector database is powered by Faiss, enabling fast and efficient searches for matching legal templates.

## Getting Started

### 1. Add API Key
1. In the project root directory and the `Lib` subfolder:
   - Create a `.env` file if it doesn’t exist.
   - Add your ChatGPT API key in the following format:
     ```plaintext
     OPENAI_API_KEY=your-api-key-here
     ```

### 2. Modify File Path in `app.py`
- Open `app.py` and go to **line 128**.
- Update the file path to point to your download folder:
  ```python
  filepath = "your/local/download/folder/path"
  ```

### Step 3: Install Required Dependencies

1. Open a terminal or command prompt.
2. Navigate to the project directory containing the `requirements.txt` file.
3. Run the following command to install all dependencies:
   ```bash
   pip install -r requirements.txt
   ```
### Step 4: Run the Streamlit App

1. Open a terminal or command prompt.
2. Navigate to the project directory where `app.py` is located.
3. Run the following command:
   ```bash
   streamlit run app.py
   ```
# Project Directory Structure  

```plaintext
project-root/
├── app/                              # Application source code  
├── lib/                              # Custom libraries and modules  
│   ├── Extract_top_n_files.py        # Module for extracting top N matching files  
│   ├── whisper_api.py                # Module for Whisper API integration  
│   ├── Whisper_extract_text_and_information.py # Module to process text and extract information  
│   ├── __init__.py                   # Initializes the lib module  
│   └── .env                          # Environment variables for the lib folder  
├── lib_whisper/                      # Whisper-related functionality  
├── word_placeholder/                 # Placeholder logic for Word templates  
├── json_placeholder/                 # Placeholder logic for JSON templates  
├── final_word/                       # Generated legal documents  
├── .env                              # Main environment variables file  
├── __init__.py                       # Initializes the main project as a package  
├── README.md                         # Project documentation  
└── requirements.txt                  # Required Python 
```

# Dependencies

## Operating System
- Windows 10 or higher

## Libraries/Tools
- `speech_recognition`
- `OpenAI`
- `python-docx`
- `langchain`
- `streamlit`

## Python Version
- Python 3.8 or higher


# Installation

Clone the repository using the following command:

```bash
git clone https://github.com/your-username/voice-to-legal-document.git
```
