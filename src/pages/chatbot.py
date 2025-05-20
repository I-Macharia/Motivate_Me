# filepath: /my-streamlit-app/my-streamlit-app/src/pages/chatbot.py
import streamlit as st
from utils.chat_utils import process_user_input, format_response
from utils.data_utils import load_quotes
from utils.model_utils import load_vectorizer

# Load quotes and vectorizer
quotes = load_quotes('data/quotes.csv')
vectorizer = load_vectorizer('data/models/vectorizer.pkl')

def chatbot_response(user_input):
    # Process user input and generate a response
    processed_input = process_user_input(user_input)
    # Here you would integrate your chatbot logic to generate a response
    response = "This is a placeholder response for: " + processed_input
    return format_response(response)

def main():
    st.title("Basic Chatbot")
    st.write("Interact with the chatbot by typing your message below:")

    user_input = st.text_input("You:")
    if st.button("Send"):
        if user_input:
            response = chatbot_response(user_input)
            st.write("Chatbot:", response)

if __name__ == "__main__":
    main()