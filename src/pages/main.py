# File: /my-streamlit-app/my-streamlit-app/src/pages/main.py

import streamlit as st

def main_page():
    st.title("Welcome to the Quotes App")
    st.write("""
    This application allows you to interact with a chatbot that provides quotes and information.
    
    Use the sidebar to navigate to different functionalities:
    - **Chatbot**: Interact with a basic chatbot.
    - **Advanced Chatbot**: Engage with an advanced chatbot using retrieval-augmented generation (RAG).
    - **About**: Learn more about the application and its purpose.
    """)

if __name__ == "__main__":
    main_page()