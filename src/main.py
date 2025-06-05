# from src.pages.login import login_page
import streamlit as st
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pages.login import login_page
from pages.profile import profile_page
from pages.chatbot import chatbot_page
from pages.rag_chatbot import rag_chatbot_page
# from .pages.about import about_page

def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Login", "Profile", "Chatbot", "RAG Chatbot", "About"])

    if page == "Login":
        login_page()
    elif page == "Profile":
        profile_page()
    elif page == "Chatbot":
        chatbot_page()
    elif page == "RAG Chatbot":
        rag_chatbot_page()
    # elif page == "About":
    #     about_page()

if __name__ == "__main__":
    main()
