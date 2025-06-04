# filepath: /my-streamlit-app/my-streamlit-app/src/utils/data_utils.py
import pandas as pd
import os
import requests

def load_quotes_data(file_path):
    """Load quotes from CSV file"""
    try:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Quotes file not found at {file_path}")
        return pd.read_csv(file_path)
    except Exception as e:
        raise Exception(f"Error loading quotes data: {e}")

def fetch_user_details_from_nextjs(username):
    """Fetch user details from the Next.js API."""
    try:
        response = requests.get(f"http://localhost:3000/api/getUser?username={username}")
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching user details: {e}")
        return None