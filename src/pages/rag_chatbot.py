# filepath: /my-streamlit-app/my-streamlit-app/src/pages/rag_chatbot.py
import streamlit as st
from utils.chat_utils import process_user_input, format_response
from utils.model_utils import load_model, generate_response
import pickle

# Load the model and embeddings
with open('data/models/vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)

# Initialize the gAIAnet.ai model (assuming a function to load it exists)
model = load_model('path/to/gAIAnet/model')

def rag_chatbot():
    st.title("Advanced RAG Chatbot")
    st.write("This chatbot uses retrieval-augmented generation (RAG) to provide enhanced responses.")

    user_input = st.text_input("You -->")
    
    if st.button("Send") and user_input:
        processed_input = process_user_input(user_input)
        response = generate_response(model, vectorizer, processed_input)
        formatted_response = format_response(response)
        
        st.write("Bobby -->")
        st.write(formatted_response)

if __name__ == "__main__":
    rag_chatbot()