# filepath: /my-streamlit-app/my-streamlit-app/src/pages/chatbot.py
import streamlit as st
from utils.chat_utils import process_user_input, format_response
from my_functions import QuoteFinder

def load_quote_finder():
    try:
        return QuoteFinder.load(
            'src/data/vectorizer.pkl.gz',
            'src/data/svm_model.pkl.gz',
            'src/data/quotes_df.pkl.gz'
        )
    except FileNotFoundError as e:
        st.error(f"Error loading model: {e}")
        return None

def chatbot_page():
    st.title("Bobby's Quote Chatbot")
    st.write("Ask me anything and I'll find a relevant quote for you!")

    # Initialize session state for chat history
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []

    # Load the QuoteFinder model
    quote_finder = load_quote_finder()
    
    if quote_finder is None:
        st.error("Failed to load the quote recommendation model. Please check the model files.")
        return

    # Chat input
    user_input = st.text_input("You:", key="user_input")

    if st.button("Send") and user_input:
        # Get quote recommendation
        try:
            quote, author = quote_finder.find_quote_for_tweet(user_input)
            
            # Add to chat history (new quote at the top)
            st.session_state.chat_history.insert(0, {"user": user_input})
            st.session_state.chat_history.insert(0, {
                "bot": f"Here's a quote that resonates with your message - {user_input}:\n\n\"{quote}\"\n- {author}"
            })

        except Exception as e:
            st.error(f"An error occurred: {e}")
            st.session_state.chat_history.append({"user": user_input})
            st.session_state.chat_history.append({
                "bot": "I apologize, but I couldn't find a relevant quote at the moment."
            })

    # Display chat history
    for message in st.session_state.chat_history:
        if "user" in message:
            st.write(f"You: {message['user']}")
        else:
            st.markdown(f"Bobby: {message['bot']}")

    # Add a clear chat button
    if st.button("Clear Chat"):
        st.session_state.chat_history = []
        st.experimental_rerun()

if __name__ == "__main__":
    chatbot_page()
