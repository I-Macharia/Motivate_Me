import streamlit as st
from pages.about import about_page
from pages.chatbot import chatbot_page
from pages.main import main_page
from pages.rag_chatbot import rag_chatbot_page

# Configure the app with custom theme
st.set_page_config(
    page_title="Motivate Me",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Add custom CSS
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stButton>button {
        width: 100%;
    }
    .stTitle {
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

# Create navigation
pages = {
    "Home": main_page,
    "Chat": chatbot_page,
    "Advanced Chat": rag_chatbot_page,
    "About": about_page
}

# Sidebar navigation with custom styling
st.sidebar.title("Navigation 🧭")
selection = st.sidebar.radio("", list(pages.keys()))

# Display selected page
pages[selection]()

# Add footer
st.sidebar.markdown("---")
st.sidebar.markdown("Made with ❤️ by Bobby")