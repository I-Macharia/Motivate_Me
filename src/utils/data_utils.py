# filepath: /my-streamlit-app/my-streamlit-app/src/utils/data_utils.py
import pandas as pd
import os
import requests

NEXTJS_API_BASE = "http://localhost:3000/api"

def load_quotes_data(file_path):
    """Load quotes from CSV file"""
    try:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Quotes file not found at {file_path}")
        return pd.read_csv(file_path)
    except Exception as e:
        raise Exception(f"Error loading quotes data: {e}")


def fetch_user_details_from_nextjs(username):
    """
    Fetch user details from the Next.js API endpoint
    
    Args:
        username (str): Username to look up
        
    Returns:
        dict or None: User details if found, None otherwise
    """
    import requests

    try:
        response = requests.get(
            f"http://localhost:3000/api/getUser/{username}")
        if response.status_code == 200:
            return response.json()
        return None
    except Exception as e:
        print(f"Error fetching user details: {e}")
        return None
