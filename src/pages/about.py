# filepath: /my-streamlit-app/my-streamlit-app/src/pages/about.py
import streamlit as st

def about_page():
    st.title("About Motivate Me 💡")
    
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
    
    ## The Team
    
    Created by passionate individuals who believe in making motivation accessible to everyone.
    
    ## Contact Us
    
    Have questions or suggestions? Reach out to us:
    - X: [contact@motivateme.com](mailto:contact@motivateme.com)
    - GitHub: [Motivate_Me Repository](https://github.com/I-Macharia/Motivate_Me)
    """)
    
    # Add version information
    # st.sidebar.markdown("---")
    # st.sidebar.markdown("v1.0.0")
    
    if __name__ == "__about__":
        about_page()