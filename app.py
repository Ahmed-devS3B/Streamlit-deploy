import streamlit as st
from huggingface_hub import InferenceClient
from dotenv import load_dotenv
import os

# Load token from .env file
load_dotenv()

# Page title
st.title("AI Emotion Detector")

# User input
user_text = st.text_area("Write something here:")

# Hugging Face Client
client = InferenceClient(
    provider="auto",
    api_key=os.getenv("HF_TOKEN"),
)

# Analyze Button
if st.button("Analyze Emotion"):

    if user_text:

        result = client.text_classification(
            user_text,
            model="j-hartmann/emotion-english-distilroberta-base"
        )

        # Get highest emotion
        emotion = result[0]['label']
        score = round(result[0]['score'] * 100, 2)

        st.subheader("Result 👇")
        st.write(f"Emotion: **{emotion}**")
        st.write(f"Confidence: **{score}%**")

    else:
        st.warning("Please enter some text first.")