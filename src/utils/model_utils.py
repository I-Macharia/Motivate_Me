# filepath: /my-streamlit-app/my-streamlit-app/src/utils/model_utils.py

import pickle
import os

def load_vectorizer(model_path):
    if os.path.exists(model_path):
        with open(model_path, 'rb') as file:
            vectorizer = pickle.load(file)
        return vectorizer
    else:
        raise FileNotFoundError(f"The model file at {model_path} does not exist.")

def save_model(model, model_path):
    with open(model_path, 'wb') as file:
        pickle.dump(model, file)

def load_model(model_path):
    if os.path.exists(model_path):
        with open(model_path, 'rb') as file:
            model = pickle.load(file)
        return model
    else:
        raise FileNotFoundError(f"The model file at {model_path} does not exist.")