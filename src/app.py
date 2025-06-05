import streamlit as st
# from pages.about import about_page
from pages.chatbot import chatbot_page
# from main import main_page
from pages.rag_chatbot import rag_chatbot_page
from pages.profile import profile_page
from utils.db_utils import init_db
import sys
from pathlib import Path

# Add the src directory to the Python path
sys.path.append(str(Path(__file__).resolve().parent))

st.title("Welcome to Motivate Me! 🚀")

st.markdown("""
    ## Our Mission

    At Motivate Me, we believe in the power of words to transform lives. Our platform is designed to provide:

    - **Personalized Inspiration**: Tailored quotes that resonate with your current situation
    - **AI-Powered Interactions**: Advanced chatbot technology for meaningful conversations
    - **Community Growth**: A space for sharing and discovering motivational content

    ## Technology Stack

    Our application leverages cutting-edge technologies:
    - Streamlit for the user interface
    - Advanced NLP models for quote recommendations
    - RAG (Retrieval Augmented Generation) for enhanced responses


    ### Your daily dose of inspiration, powered by words that move you.

    This platform helps you:
    - Find motivational quotes tailored to your mood
    - Engage with an AI-powered chatbot for personalized inspiration
    - Explore a curated collection of uplifting content

   """)

# Embed Gamma presentation
st.markdown("## Our Vision")

# Embed the presentation with custom HTML and CSS for responsive design
st.markdown("""
        <div style="display: flex; justify-content: center; margin: 2rem 0;">
            <iframe
                src="https://gamma.app/embed/7o9jimawz7eeton"
                style="width: 700px; max-width: 100%; height: 450px; border: none; border-radius: 10px; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);"
                allow="fullscreen"
                title="Motivate Me 🚀">
            </iframe>
        </div>
    """, unsafe_allow_html=True)

# Add call to action buttons

# Add a subtitle/description
st.markdown("""
                 ## The Team

    Created by passionate individuals who believe in making motivation accessible to everyone.

    ## Contact Us

    Have questions or suggestions? Reach out to us:
    - X: [contact@motivateme.com](mailto:contact@motivateme.com)
    - GitHub: [Motivate_Me Repository](https://github.com/I-Macharia/Motivate_Me)

    """)


st.markdown("### Ready to get started?")

# Create two columns for buttons
col1, col2 = st.columns([1, 1])
with col1:
    if st.button("💬 Start Chatting", key="start_chat", use_container_width=True):
        st.session_state["nav_target"] = "Chat"
        # st.rerun()
with col2:
        if st.button("🔍 Learn More", key="learn_more", use_container_width=True):
            st.session_state["nav_target"] = "About"
            # st.rerun()







# # Initialize database
# init_db()

# # Configure the app with custom theme
# st.set_page_config(
#     page_title="Motivate Me",
#     page_icon="🚀",
#     layout="wide",
#     initial_sidebar_state="expanded",
# )
#     st.title("Welcome to Motivate Me! 🚀")
    
#     st.markdown("""
#         ## Our Mission
    
#         At Motivate Me, we believe in the power of words to transform lives. Our platform is designed to provide:
    
#         - **Personalized Inspiration**: Tailored quotes that resonate with your current situation
#         - **AI-Powered Interactions**: Advanced chatbot technology for meaningful conversations
#         - **Community Growth**: A space for sharing and discovering motivational content
    
#         ## Technology Stack
    
#         Our application leverages cutting-edge technologies:
#         - Streamlit for the user interface
#         - Advanced NLP models for quote recommendations
#         - RAG (Retrieval Augmented Generation) for enhanced responses
    
    
#         ### Your daily dose of inspiration, powered by words that move you.
    
#         This platform helps you:
#         - Find motivational quotes tailored to your mood
#         - Engage with an AI-powered chatbot for personalized inspiration
#         - Explore a curated collection of uplifting content
    
#     """)
    
#     # Add a subtitle/description
#     st.markdown("""
#         ## The Team
    
#         Created by passionate individuals who believe in making motivation accessible to everyone.
    
#         ## Contact Us
    
#         Have questions or suggestions? Reach out to us:
#         - X: [contact@motivateme.com](mailto:contact@motivateme.com)
#         - GitHub: [Motivate_Me Repository](https://github.com/I-Macharia/Motivate_Me)
    
#     """)
    
#     # Embed Gamma presentation
#     st.markdown("## Our Vision")
    
#     # Embed the presentation with custom HTML and CSS for responsive design
#     st.markdown("""
#         <div style="display: flex; justify-content: center; margin: 2rem 0;">
#             <iframe
#                 src="https://gamma.app/embed/7o9jimawz7eeton"
#                 style="width: 700px; max-width: 100%; height: 450px; border: none; border-radius: 10px; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);"
#                 allow="fullscreen"
#                 title="Motivate Me 🚀">
#             </iframe>
#         </div>
#     """, unsafe_allow_html=True)
    
#     # Add call to action buttons
#     st.markdown("### Ready to get started?")
    
#     # Create two columns for buttons
#     col1, col2 = st.columns([1, 1])
#     with col1:
#         if st.button("💬 Start Chatting", key="start_chat", use_container_width=True):
#             st.session_state["nav_target"] = "Chat"
#             # st.rerun()
#     with col2:
#         if st.button("🔍 Learn More", key="learn_more", use_container_width=True):
#             st.session_state["nav_target"] = "About"
#             # st.rerun()


# # # Add custom CSS
# # st.markdown("""
# #     <style>
# #     .main { padding: 2rem; }
# #     .stButton>button { 
# #         width: 100%;
# #         background-color: #ff4b4b;
# #         color: white;
# #         border-radius: 5px;
# #     }
# #     .stTitle { 
# #         text-align: center;
# #         color: #ff4b4b;
# #     }
# #     .stSidebar .stRadio > div {
# #         background-color: #1e1e1e;
# #         padding: 1rem;
# #         border-radius: 5px;
# #     }
# #     </style>
# #     """, unsafe_allow_html=True)

# # # Sidebar configuration
# # with st.sidebar:
# #     st.title("Navigation 🧭")
    
# #     # Navigation options
# #     selection = st.radio(
# #         "Choose a page",
# #         options=["Home", "Chat", "Advanced Chat", "About"],
# #         label_visibility="collapsed",
# #         key="navigation"
# #     )
    
#     # st.markdown("---")
#     # st.markdown("v1.0.0")
#     # st.markdown("Made with ❤️ by Bobby")

# # # --- Navigation fix ---
# # if "nav_target" in st.session_state:
# #     selection = st.session_state.pop("nav_target")

# # Page mapping
# pages = {
#     # "About": about_page,
#     "Home": main_page,
#     "Chat": chatbot_page,
#     "Advanced Chat": rag_chatbot_page,
#     "Profile": profile_page
# }
# # # Display selected page
# # pages[selection]()
# if "nav_target" in st.session_state:
#     pages[st.session_state["nav_target"]]()
# else:
#     pages["Home"]()
