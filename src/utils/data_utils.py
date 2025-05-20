# filepath: /my-streamlit-app/my-streamlit-app/src/utils/data_utils.py
import pandas as pd
import os

def load_quotes_data(file_path):
    """Load quotes from CSV file"""
    try:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Quotes file not found at {file_path}")
        return pd.read_csv(file_path)
    except Exception as e:
        raise Exception(f"Error loading quotes data: {e}")