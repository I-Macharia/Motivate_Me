import streamlit as st

# Import pages
from pages.about import about_page
from pages.chatbot import chatbot_page
from pages.main import main_page
from pages.rag_chatbot import rag_chatbot_page

# Set up the main title of the app
st.title("My Streamlit App")

# Create a sidebar for navigation
pages = {
    "Main": main_page,
    "Chatbot": chatbot_page,
    "RAG Chatbot": rag_chatbot_page,
    "About": about_page
}

# Sidebar for page selection
selected_page = st.sidebar.selectbox("Select a page", list(pages.keys()))

# Render the selected page
pages[selected_page]()