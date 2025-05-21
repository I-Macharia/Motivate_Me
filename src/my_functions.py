import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from nltk import FreqDist
import os

import zipfile
import pickle
import string
import gzip
import spacy

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

import streamlit as st

# Initialize lemmatizer and stop words
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

# Import everything needed for the application to work
try:
    nltk.data.find('tokenizers/punkt')
    nltk.data.find('corpora/stopwords')
    nltk.data.find('corpora/wordnet')
except LookupError:
    nltk.download('punkt')
    nltk.download('stopwords')
    nltk.download('wordnet')

# Load spaCy model
try:
    nlp = spacy.load('en_core_web_sm')
except OSError:
    # For deployment, we'll handle the error and provide guidance
    pass


def translate_to_english(text):
    """
    Translates the given text to English if it is not already in English.
    
    Note: This function is a placeholder since we've removed external dependencies.
    In a real application, you would need to install and import language detection and 
    translation libraries.

    Args:
        text (str): The text to be translated.

    Returns:
        str: The original text (translation functionality removed for simplicity).
    """
    # We're removing the actual translation functionality to eliminate dependencies
    return text


def preprocess_text(text):
    """
    Preprocesses the given text by converting it to lowercase, tokenizing it, 
    removing stopwords, and joining the tokens back into text.

    Args:
        text (str): The text to be preprocessed.

    Returns:
        tuple: A tuple containing the preprocessed text and the list of words.
    """
    if not isinstance(text, str):
        text = str(text)
        
    # Lowercase
    text = text.lower()
    
    # Tokenization
    tokens = word_tokenize(text)
    
    # Remove stopwords
    tokens = [word for word in tokens if word not in stop_words]

    # Tokenize again for words list
    words = nltk.word_tokenize(text.lower())
    
    # Remove stopwords and punctuation
    words = [word for word in words if word.isalpha() and word not in stop_words]
    
    # Lemmatize
    words = [lemmatizer.lemmatize(word) for word in words]
    
    # Join tokens back into text 
    return ' '.join(tokens), words


def compress_tags(tags_list):
    """
    Compresses a list of tags to only unique values with a maximum of 5.
    
    Args:
        tags_list (list): List of tags to compress.
        
    Returns:
        list: Compressed list with unique tags (max 5).
    """
    return list(set(tags_list))[:5]


def preprocesss_text(text):
    """
    Preprocesses text by converting to lowercase, tokenizing, removing stopwords.
    
    Args:
        text (str): The input text.
    
    Returns:
        str: The preprocessed text.
    """
    if isinstance(text, float):
        # Return an empty string for float values
        return ''
        
    # Lowercase
    text = text.lower()
    
    # Tokenization
    tokens = word_tokenize(text)
    
    # Remove stopwords
    tokens = [word for word in tokens if word.isalnum() and word not in stop_words]
    
    return ' '.join(tokens)


def clean_text(text):
    """
    Performs basic text cleaning.
    
    Args:
        text (str): The text to clean.
        
    Returns:
        str: Cleaned text.
    """
    if isinstance(text, str):
        # Convert to lowercase
        text = text.lower()
        # Remove specific punctuation marks
        text = ''.join([c for c in text if c not in ('!', '.', ':', '?', ',', '\"')])
        # Remove any remaining punctuation
        text = text.translate(str.maketrans('', '', string.punctuation))
    return text


def aggregate_statistics(polarity_scores, subjectivity_scores):
    """
    Calculate aggregate statistics for polarity and subjectivity scores.
    
    Args:
        polarity_scores (list): List of polarity scores.
        subjectivity_scores (list): List of subjectivity scores.
        
    Returns:
        dict: Dictionary of calculated statistics.
    """
    polarity_mean = np.mean(polarity_scores)
    polarity_median = np.median(polarity_scores)
    polarity_std = np.std(polarity_scores)
    subjectivity_mean = np.mean(subjectivity_scores)
    subjectivity_median = np.median(subjectivity_scores)
    subjectivity_std = np.std(subjectivity_scores)

    stats = {
        "polarity_mean": polarity_mean,
        "polarity_median": polarity_median,
        "polarity_std": polarity_std,
        "subjectivity_mean": subjectivity_mean,
        "subjectivity_median": subjectivity_median,
        "subjectivity_std": subjectivity_std,
    }

    st.write("### Aggregate Statistics")
    st.write(f"**Polarity Mean:** {polarity_mean:.3f}")
    st.write(f"**Polarity Median:** {polarity_median:.3f}")
    st.write(f"**Polarity Standard Deviation:** {polarity_std:.3f}")
    st.write(f"**Subjectivity Mean:** {subjectivity_mean:.3f}")
    st.write(f"**Subjectivity Median:** {subjectivity_median:.3f}")
    st.write(f"**Subjectivity Standard Deviation:** {subjectivity_std:.3f}")

    return stats


def plot_histograms(polarity_scores, subjectivity_scores):
    """
    Plot histograms for polarity and subjectivity scores.
    
    Note: This function has been modified to work without seaborn.
    
    Args:
        polarity_scores (list): List of polarity scores.
        subjectivity_scores (list): List of subjectivity scores.
    """
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

    # Plot histogram for polarity scores
    ax1.hist(polarity_scores, bins=10, color='skyblue', edgecolor='black')
    ax1.set_title('Distribution of Polarity Scores')
    ax1.set_xlabel('Polarity')
    ax1.set_ylabel('Frequency')

    # Plot histogram for subjectivity scores
    ax2.hist(subjectivity_scores, bins=10, color='salmon', edgecolor='black')
    ax2.set_title('Distribution of Subjectivity Scores')
    ax2.set_xlabel('Subjectivity')
    ax2.set_ylabel('Frequency')

    plt.tight_layout()
    st.pyplot(fig)


def sentiment_categories(polarity_scores, positive_threshold=0.2, negative_threshold=-0.2):
    """
    Categorize sentiment based on polarity scores.
    
    Args:
        polarity_scores (list): List of polarity scores.
        positive_threshold (float, optional): Threshold for positive sentiment. Defaults to 0.2.
        negative_threshold (float, optional): Threshold for negative sentiment. Defaults to -0.2.
        
    Returns:
        dict: Dictionary with counts of positive, neutral, and negative quotes.
    """
    positive_quotes = sum(p > positive_threshold for p in polarity_scores)
    neutral_quotes = sum(
        -positive_threshold <= p <= positive_threshold for p in polarity_scores
    )
    negative_quotes = sum(p < negative_threshold for p in polarity_scores)

    categories = {
        "positive_quotes": positive_quotes,
        "neutral_quotes": neutral_quotes,
        "negative_quotes": negative_quotes,
    }

    st.write("### Sentiment Categories")
    st.write(f"**Positive Quotes:** {positive_quotes}")
    st.write(f"**Neutral Quotes:** {neutral_quotes}")
    st.write(f"**Negative Quotes:** {negative_quotes}")

    return categories


def correlation_analysis(polarity_scores):
    """
    Perform correlation analysis between polarity scores and random quote lengths.
    
    Args:
        polarity_scores (list): List of polarity scores.
        
    Returns:
        float: Correlation coefficient.
    """
    quote_lengths = np.random.randint(10, 200, size=len(polarity_scores))
    correlation = np.corrcoef(polarity_scores, quote_lengths)[0, 1]

    st.write("### Correlation Analysis")
    st.write(f"**Correlation between Polarity Scores and Quote Lengths:** {correlation:.3f}")

    return correlation


def save_results(filename, results):
    """
    Save results to a pickle file.
    
    Args:
        filename (str): Path to save the file.
        results (object): Object to save.
    """
    with open(filename, 'wb') as f:
        pickle.dump(results, f, protocol=pickle.HIGHEST_PROTOCOL)


def load_results(filename):
    """
    Load results from a pickle file.
    
    Args:
        filename (str): Path to the file.
        
    Returns:
        object: Loaded object.
    """
    with open(filename, 'rb') as f:
        return pickle.load(f)


class QuoteFinder:
    """
    A class for finding quotes in text data and training a model for quote prediction.

    Methods:
    - train_model: Trains a Support Vector Machine model on the quotes data.
    - clean_text: Cleans and preprocesses text data.
    - find_quote_for_tweet: Predicts a quote and author for a given tweet.
    - save: Serialize and compress the model, vectorizer, and data.
    - load: Decompress and deserialize the model, vectorizer, and data.

    Raises:
        ValueError: If quotes DataFrame is not set.
    """
    
    def __init__(self, quotes_df=None):
        """
        Initialize the QuoteFinder with a DataFrame of quotes.
        
        Args:
            quotes_df (DataFrame, optional): DataFrame with quotes and authors. Defaults to None.
        """
        self.quotes_df = quotes_df
        self.vectorizer = None
        self.svm_model = None

        if self.quotes_df is not None:
            self.quotes_df['combined'] = self.quotes_df['quote_2'] + " " + self.quotes_df['author_2']

    def train_model(self):
        """
        Train the SVM model on the quotes data.
        
        Raises:
            ValueError: If quotes DataFrame is not set.
        """
        if self.quotes_df is None:
            raise ValueError("Quotes DataFrame is not set.")
        
        self.vectorizer = TfidfVectorizer()
        X = self.vectorizer.fit_transform(self.quotes_df['combined'])
        
        y = self.quotes_df.index
        
        self.svm_model = SVC(C=10, gamma=1, kernel='rbf')
        self.svm_model.fit(X, y)

    def clean_text(self, text):
        """
        Clean and preprocess text.
        
        Args:
            text (str): The text to clean.
            
        Returns:
            str: Cleaned text.
        """
        text = text.lower()
        tokens = word_tokenize(text)
        tokens = [word for word in tokens if word.isalnum() and word not in stopwords.words('english')]
        return ' '.join(tokens)

    def find_quote_for_tweet(self, tweet):
        """
        Find a relevant quote and author for a given tweet.
        
        Args:
            tweet (str): The tweet or user input.
            
        Returns:
            tuple: A tuple containing the quote and author.
        """
        cleaned_tweet = self.clean_text(tweet)
        vectorized_tweet = self.vectorizer.transform([cleaned_tweet])

        try:
            index = self.svm_model.predict(vectorized_tweet)[0]
            quote = self.quotes_df.iloc[index]['quote_2']
            author = self.quotes_df.iloc[index]['author_2']
            return quote, author
        except IndexError as e:
            print(f"Error: {e}")
            print(f"Predicted index {index} is out of range.")
            return "No quote found.", "Unknown"
        except Exception as e:
            print(f"An error occurred: {e}")
            return "An error occurred.", "Unknown"

    def save(self, vectorizer_filepath, model_filepath, dataframe_filepath):
        """
        Serialize and compress the model, vectorizer, and data.
        
        Args:
            vectorizer_filepath (str): Path to save the vectorizer.
            model_filepath (str): Path to save the model.
            dataframe_filepath (str): Path to save the DataFrame.
        """
        # Create directory if it doesn't exist
        os.makedirs(os.path.dirname(vectorizer_filepath), exist_ok=True)
        os.makedirs(os.path.dirname(model_filepath), exist_ok=True)
        os.makedirs(os.path.dirname(dataframe_filepath), exist_ok=True)
        
        with gzip.open(vectorizer_filepath, 'wb') as file:
            pickle.dump(self.vectorizer, file, protocol=pickle.HIGHEST_PROTOCOL)

        with gzip.open(model_filepath, 'wb') as file:
            pickle.dump(self.svm_model, file, protocol=pickle.HIGHEST_PROTOCOL)

        with gzip.open(dataframe_filepath, 'wb') as file:
            pickle.dump(self.quotes_df, file, protocol=pickle.HIGHEST_PROTOCOL)
            
    @classmethod
    def load(cls, vectorizer_filepath, model_filepath, dataframe_filepath):
        """
        Decompress and deserialize the model, vectorizer, and data.
        
        Args:
            vectorizer_filepath (str): Path to the vectorizer file.
            model_filepath (str): Path to the model file.
            dataframe_filepath (str): Path to the DataFrame file.
            
        Returns:
            QuoteFinder: An instance of QuoteFinder with loaded components.
            
        Raises:
            FileNotFoundError: If any of the files don't exist.
        """
        # Validate paths
        for filepath in [vectorizer_filepath, model_filepath, dataframe_filepath]:
            if not os.path.exists(filepath):
                raise FileNotFoundError(f"File not found: {filepath}")
        
        try:
            with gzip.open(vectorizer_filepath, 'rb') as file:
                vectorizer = pickle.load(file)

            with gzip.open(model_filepath, 'rb') as file:
                svm_model = pickle.load(file)

            with gzip.open(dataframe_filepath, 'rb') as file:
                quotes_df = pickle.load(file)

            instance = cls(quotes_df)
            instance.vectorizer = vectorizer
            instance.svm_model = svm_model

            return instance
        except Exception as e:
            raise Exception(f"Error loading model components: {e}")
