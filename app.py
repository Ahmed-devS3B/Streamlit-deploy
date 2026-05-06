import streamlit as st

st.title("Hello, SI 👋")

name = st.text_input("What's your name ?")

if name:
    st.write(f"Welcome, {name.title()} 👋")

age = st.slider("What's your age ?", 0, 100, 25)

if age < 18:
    st.write("You are a kid.")
elif age > 18 and age < 65:
    st.write("You are an adult.")
else:
    st.write("You are a senior.")