# filepath: /my-streamlit-app/my-streamlit-app/src/utils/model_utils.py
import pickle
import gzip
from pathlib import Path

def load_model(model_path):
    """Load the model from a pickle file"""
    try:
        model_path = Path(model_path)
        if not model_path.exists():
            raise FileNotFoundError(f"Model file not found: {model_path}")
            
        if model_path.suffix == '.gz':
            with gzip.open(model_path, 'rb') as f:
                return pickle.load(f)
        else:
            with open(model_path, 'rb') as f:
                return pickle.load(f)
    except Exception as e:
        raise Exception(f"Error loading model: {e}")

def generate_response(model, vectorizer, user_input):
    """Generate a response using the model"""
    try:
        # Vectorize input
        vec_input = vectorizer.transform([user_input])
        
        # Get prediction/response from model
        response = model.predict(vec_input)[0]
        
        return response
    except Exception as e:
        return f"Error generating response: {e}"