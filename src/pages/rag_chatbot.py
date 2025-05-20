# filepath: /my-streamlit-app/my-streamlit-app/src/pages/rag_chatbot.py
import streamlit as st
from utils.chat_utils import process_user_input, format_response
from utils.model_utils import load_model, generate_response
import pickle
from pathlib import Path

def rag_chatbot_page():
    st.title("AI-Powered Quote Chatbot 🤖")
    st.markdown("""
    ### Enhanced with Retrieval Augmented Generation
    Have a deeper conversation about motivation and inspiration with our advanced AI chatbot.
    """)

    # Initialize session state for chat history
    if 'messages' not in st.session_state:
        st.session_state.messages = []

    try:
        # Load the model and vectorizer
        model_path = Path('src/data/models/vectorizer.pkl')
        if not model_path.exists():
            st.error("Model files not found. Please ensure the model is properly trained and saved.")
            return

        with open(model_path, 'rb') as f:
            vectorizer = pickle.load(f)

        model = load_model('src/data/models/model.pkl')

        # Display chat history
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        # Chat input
        if prompt := st.chat_input("What's on your mind?"):
            # Add user message to chat history
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)

            # Generate response
            with st.chat_message("assistant"):
                with st.spinner("Thinking..."):
                    processed_input = process_user_input(prompt)
                    response = generate_response(model, vectorizer, processed_input)
                    formatted_response = format_response(response)
                    st.markdown(formatted_response)
                    
                    # Add assistant response to chat history
                    st.session_state.messages.append({
                        "role": "assistant", 
                        "content": formatted_response
                    })

    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
        st.info("Please try again or contact support if the problem persists.")

if __name__ == "__main__":
    rag_chatbot_page()