# filepath: /my-streamlit-app/my-streamlit-app/src/pages/rag_chatbot.py
import streamlit as st
from utils.chat_utils import process_user_input, format_response
from utils.model_utils import load_model, generate_response
from utils.aimodel import RAGQuoteAgent
import pickle
from pathlib import Path

def rag_chatbot_page():
    st.title("AI-Powered Quote Chatbot 🤖")
    st.markdown("""
    ### Enhanced with Retrieval Augmented Generation
    Have a deeper conversation about motivation and inspiration with our advanced AI chatbot.
    """)
    # Initialize session state for chat history
    agent = RAGQuoteAgent("data/quotes_2.csv")
    user_input = st.text_input("Ask for motivation:")
    if st.button("Get Response"):
        response, quotes = agent.generate(user_input)
        st.write("AI Response:", response)
        st.write("Retrieved Quotes:", quotes)
        
        
if __name__ == "__main__":
    rag_chatbot_page()