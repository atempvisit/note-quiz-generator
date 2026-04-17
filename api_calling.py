import io
import os
from dotenv import load_dotenv
from google import genai
from gtts import gTTS
import re
from markdown import markdown
from bs4 import BeautifulSoup

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

def note_generator(images):

    prompt = f"""Summarize the pictures in note format in 100 words. Make sure to add necessary markdown to differentiate different sections."""

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=[images, prompt]
    )

    # Convert markdown to plain text

    html = markdown(response.text)
    soup = BeautifulSoup(html, "html.parser")
    return soup.get_text()

    # or without any package you can use regex to remove markdown syntax
    # Like this:

# import re

# def clean_markdown(md_text):
#     text = md_text

#     # Remove headings (#, ##, etc.)
#     text = re.sub(r"#+", "", text)

#     # Remove bold/italic (**text**, *text*)
#     text = re.sub(r"\*\*(.*?)\*\*", r"\1", text)
#     text = re.sub(r"\*(.*?)\*", r"\1", text)

#     # Remove inline code (`code`)
#     text = re.sub(r"`(.*?)`", r"\1", text)

#     # Remove links [text](url)
#     text = re.sub(r"\[(.*?)\]\((.*?)\)", r"\1", text)

#     # Remove bullet points
#     text = re.sub(r"[-•]\s*", "", text)

#     # Clean extra spaces/newlines
#     text = re.sub(r"\n+", "\n", text).strip()

#     return text


def audio_transcription(audio):
    speech = gTTS(text=audio, lang='en', slow=False)

    audio_buffer = io.BytesIO()

    speech.write_to_fp(audio_buffer)

    return audio_buffer


def quiz_generator(images, difficulty):
    prompt = f"""Generate 3 quizzes based on the {difficulty}. Make sure to add necessary markdown to differentiate different sections. Add correct answer for each quiz and make sure to add 4 options for each quiz."""

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=[images, prompt]
    )

    return response.text
