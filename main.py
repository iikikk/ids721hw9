import streamlit as st
from transformers import pipeline

# model = pipeline("text-generation", model="openai-gpt")
generator = pipeline('text-generation', model='gpt2')

user_input = st.text_input("Enter your text here", "")
generate_button = st.button('Generate Text')

if generate_button:
    with st.spinner('Generating...'):
        output = generator(user_input, max_length=100, num_return_sequences=1)
        generated_text = output[0]['generated_text']
        st.write(generated_text)