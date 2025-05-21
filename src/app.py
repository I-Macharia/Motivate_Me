import streamlit as st
from pages.about import about_page
from pages.chatbot import chatbot_page
from pages.main import main_page
from pages.rag_chatbot import rag_chatbot_page
from utils.db_utils import init_db

# Initialize database
init_db()

# Configure the app with custom theme
st.set_page_config(
    page_title="Motivate Me",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded",
)

# # Add custom CSS
# st.markdown("""
#     <style>
#     .main { padding: 2rem; }
#     .stButton>button { 
#         width: 100%;
#         background-color: #ff4b4b;
#         color: white;
#         border-radius: 5px;
#     }
#     .stTitle { 
#         text-align: center;
#         color: #ff4b4b;
#     }
#     .stSidebar .stRadio > div {
#         background-color: #1e1e1e;
#         padding: 1rem;
#         border-radius: 5px;
#     }
#     </style>
#     """, unsafe_allow_html=True)

# Sidebar configuration
with st.sidebar:
    st.title("Navigation 🧭")
    
    # Navigation options
    selection = st.radio(
        "Choose a page",
        options=["Home", "Chat", "Advanced Chat", "About"],
        label_visibility="collapsed",
        key="navigation"
    )
    
    st.markdown("---")
    # st.markdown("v1.0.0")
    st.markdown("Made with ❤️ by Bobby")

# --- Navigation fix ---
# if "nav_target" in st.session_state:
#     selection = st.session_state.pop("nav_target")

# Page mapping
pages = {
    "Home": main_page,
    "Chat": chatbot_page,
    "Advanced Chat": rag_chatbot_page,
    "About": about_page
}

# Display selected page
pages[selection]()