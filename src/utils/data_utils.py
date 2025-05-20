# filepath: /my-streamlit-app/my-streamlit-app/src/utils/data_utils.py

import pandas as pd
import pickle

def load_quotes_data(file_path):
    return pd.read_csv(file_path)

def load_embeddings(file_path):
    with open(file_path, 'rb') as f:
        return pickle.load(f)

def save_embeddings(file_path, embeddings):
    with open(file_path, 'wb') as f:
        pickle.dump(embeddings, f)

def load_vectorizer(file_path):
    with open(file_path, 'rb') as f:
        return pickle.load(f)