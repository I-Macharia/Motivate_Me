# filepath: /my-streamlit-app/my-streamlit-app/src/utils/chat_utils.py

def process_user_input(user_input):
    # Function to process user input for the chatbot
    processed_input = user_input.strip().lower()
    return processed_input

def format_response(response):
    # Function to format the chatbot's response for display
    return f"**Bobby**: {response}"

def log_conversation(user_input, bot_response):
    # Function to log the conversation for future reference
    with open("conversation_log.txt", "a") as log_file:
        log_file.write(f"You: {user_input}\nBobby: {bot_response}\n\n")

def generate_response(user_input):
    # Placeholder function for generating a response from the chatbot
    # This should be replaced with actual model inference logic
    return "This is a placeholder response."