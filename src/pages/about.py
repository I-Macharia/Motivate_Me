# filepath: /my-streamlit-app/my-streamlit-app/src/pages/about.py
import streamlit as st

def about_page():
    st.title("About This Application")
    st.write("""
    Welcome to the Quotes Bot application! This app is designed to provide users with inspirational quotes and facilitate engaging conversations through a chatbot interface.

    ### Objectives:
    - **Curate Inspirational Quotes:** We have gathered a diverse collection of quotes from various sources to inspire and motivate users.
    - **Interactive Chatbot:** The chatbot allows users to interact and receive quotes based on their queries, enhancing user experience.
    - **Advanced AI Integration:** Our application utilizes advanced AI models for improved response generation, ensuring relevant and meaningful interactions.

    ### Features:
    - **Quote Retrieval:** Users can request quotes on specific topics or simply ask for a random quote.
    - **Chatbot Interaction:** Engage in conversations with the chatbot, which is designed to understand and respond to user inputs effectively.
    - **Data Visualization:** The app includes visualizations to analyze quote data, providing insights into sentiment and author contributions.

    ### Technologies Used:
    - **Streamlit:** For building the web application interface.
    - **Natural Language Processing:** To process and understand user inputs.
    - **Machine Learning Models:** For generating responses and retrieving relevant quotes.

    Thank you for using the Quotes Bot application! We hope it brings you daily inspiration and motivation.
    """)