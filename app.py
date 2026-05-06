import streamlit as st

st.title("Hello, SI ?")

name = st.text_input("What is your name ?")

if name:
    st.write(f"Welcome, {name.title()} 👋")