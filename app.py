import streamlit as st
from huggingface_hub import InferenceClient
from dotenv import load_dotenv
import os

load_dotenv()

st.title("Hello, SI 👋")

input_user = st.text_input("Enter your text here:")

client = InferenceClient(
    provider="auto",
    api_key=os.getenv("HF_TOKEN"),
)

if input_user:
    result = client.text_classification(
        input_user,
        model="distilbert/distilbert-base-uncased-finetuned-sst-2-english"
    )

    st.write(result[0]['label'])