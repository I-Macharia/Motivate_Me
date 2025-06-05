# from src.pages.login import login_page
import streamlit as st
import sys
import os
from utils.db_utils import init_db

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pages.login import login_page
from pages.profile import profile_page
from pages.chatbot import chatbot_page
from pages.rag_chatbot import rag_chatbot_page
from pages.about import about_page

# Initialize database
init_db()

# Configure the app with custom theme
st.set_page_config(
    page_title="Motivate Me",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded",
)

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
    elif page == "About":
        about_page()

if __name__ == "__main__":
    main()
