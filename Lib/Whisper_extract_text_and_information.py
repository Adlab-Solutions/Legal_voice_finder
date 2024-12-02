import openai
from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI
from langchain.output_parsers import ResponseSchema
from langchain.output_parsers import StructuredOutputParser
from langchain.prompts import ChatPromptTemplate
import os
import sys
import json
import re
from . import whisper_api

sys.path.append(os.path.abspath("Lib"))


# Set your OpenAI API key
load_dotenv()
openai.api_key = os.getenv("OPENAI_KEY")


def extract_information_from_audio(filename):
    style="""Format the output as JSON so that it has as been key value pairs as possible in a structure but must have the following keys are included:
    - Name
    - Purpose
        """


    template_string = """Format the output as JSON so that it has as been key value pairs as possible in a structure but must have the following keys are included:\
    - Name\
    - Purpose\
    that is delimited by triple backticks \
    text: ```{text}```
    """

    chat = ChatOpenAI(temperature=0.0, model='gpt-4o-mini',openai_api_key=openai.api_key)


    result_translate,result_transcribe=whisper_api.transcibe_and_translate(filename)


    prompt_template = ChatPromptTemplate.from_template(template_string)
    customer_messages = prompt_template.format_messages(
                    style=style,
                    text=result_translate)

    customer_response = chat(customer_messages)
    temp=re.sub(r'json','',customer_response.content)
    temp=re.sub(r'```','',temp)
    json_data=json.loads(temp)

    return result_translate,json_data

