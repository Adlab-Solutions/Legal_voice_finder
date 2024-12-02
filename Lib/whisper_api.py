
import openai
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

# Access the OpenAI API key from environment variables
openai.api_key = os.getenv("OPENAI_KEY")
def transcibe_and_translate(mp3):

    
    client = OpenAI(api_key=openai.api_key)

    audio_file= open(mp3, "rb")
    translation = client.audio.translations.create(
    model="whisper-1", 
    file=audio_file
    )

    transcription = client.audio.transcriptions.create(
    model="whisper-1", 
    file=audio_file, 
    response_format="text"
    )

    return translation.text,transcription


