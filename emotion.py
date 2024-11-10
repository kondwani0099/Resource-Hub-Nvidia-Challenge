from flask import Flask, request, jsonify, render_template
import cv2
import base64
import numpy as np
from PIL import Image
from deepface import DeepFace
from gtts import gTTS
import logging
import groq
import io
from flask_cors import CORS
import google.generativeai as genai
# from google.colab import userdata

# Initialize the Flask app
app = Flask(__name__, template_folder='templates')
CORS(app)

# Configure logging
logging.basicConfig(level=logging.INFO)

# Set your Groq API key (ensure to set it securely in the environment)
api_key = ''  # Replace with your Groq API key

# Configure Google API Key
GOOGLE_API_KEY = ''
genai.configure(api_key=GOOGLE_API_KEY)


# Choose a Gemini model
model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest")

# Function to generate response using Groq
def generate_response(emotion):
    prompt = ""
    if emotion == "happy":
        prompt = "The user seems happy. Generate an advanced Data Science learning topic or a quiz question on Reinforcement Learning."
    elif emotion == "sad":
        prompt = "The user seems sad. Provide encouragement and a simple introduction to Decision Trees in Machine Learning."
    elif emotion == "neutral":
        prompt = "The user seems neutral. Generate a quiz question or a learning path on Regression Analysis."
    else:
        prompt = f"The user seems {emotion.lower()}. Provide advice and motivation to keep learning Data Science."

    client = groq.Client(api_key=api_key)
    completion = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=1,
        max_tokens=1024,
        top_p=1,
        stream=True,
        stop=None,
    )

    response = ""
    for chunk in completion:
        response += (chunk.choices[0].delta.content or "")

    return response

# Function to convert text to speech
def speak_text(text):
    # Use gTTS to convert text to speech
    tts = gTTS(text=text, lang='en')

    # Save the audio file
    tts.save("response.mp3")
    
    return "response.mp3"
