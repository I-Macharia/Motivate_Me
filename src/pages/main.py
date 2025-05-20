# File: /my-streamlit-app/my-streamlit-app/src/pages/main.py

import streamlit as st

def main_page():
    st.title("Welcome to Motivate Me! 🚀")
    
    # Add a subtitle/description
    st.markdown("""
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
    
    # Add call to action with better navigation
    st.markdown("### Ready to get started?")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Try Chat Bot", use_container_width=True):
            st.session_state['navigation'] = "Chat"
            st.rerun()  # Using st.rerun instead of experimental_rerun
    with col2:
        if st.button("Learn More", use_container_width=True):
            st.session_state['navigation'] = "About"
            st.rerun()  # Using st.rerun instead of experimental_rerun
