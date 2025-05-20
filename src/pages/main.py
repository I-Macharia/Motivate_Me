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
    
    # Placeholder for pitch deck (to be added later)
    st.subheader("Our Vision")
    st.markdown("""
    *Pitch deck will be embedded here*
    
    For now, you can:
    - Try our **Chat** feature for quick quotes
    - Explore our **Advanced Chat** for deeper conversations
    - Learn more about us in the **About** section
    """)
    
    # Add some interactive elements
    if st.button("Get Started"):
        st.markdown("Navigate to the **Chat** section using the sidebar to begin your journey! ➡️")

