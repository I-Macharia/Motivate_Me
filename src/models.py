
import pandas as pd


import zipfile
import pickle
import string


import numpy as np

import matplotlib.pyplot as plt
from wordcloud import WordCloud
from nltk import FreqDist


# from langdetect import detect
# from googletrans import Translator


from sklearn.metrics.pairwise import cosine_similarity, linear_kernel


# from sklearn.cluster import KMeans
# from sklearn.neighbors import NearestNeighbors
# from sklearn.metrics import mean_squared_error, accuracy_score
# from sklearn.model_selection import cross_val_score, GridSearchCV, train_test_split
# from sklearn.neighbors import  KNeighborsRegressor
# from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, VotingClassifier
# from tensorflow.keras.preprocessing.text import Tokenizer
# from tensorflow.keras.preprocessing.sequence import pad_sequences
from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.metrics.pairwise import cosine_similarity
# from sklearn.utils import resample
from sklearn.svm import SVC


import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
# from textblob import TextBlob



from my_functions import (translate_to_english, preprocess_text, preprocesss_text,
                          compress_tags, clean_text, aggregate_statistics, plot_histograms, sentiment_categories, 
                          correlation_analysis, save_results, load_results, QuoteFinder)





# Reading the new file 
quotes_2 = pd.read_csv(r'data/quotes_2.csv')

#Read the data into a data frame
tweets = pd.read_csv(r'data/Tweets.csv')


# Data

quotes_df = quotes_2.loc[:, ['quote_2', 'author_2']].copy()


# tweets_sample = tweets.sample(3000).reset_index(drop=True)

# # Preprocess quotes
# quotes_2['processed_quote'] = quotes_2['quote_2'].apply(lambda x: ' '.join([word.lower() for word in word_tokenize(x) if word.isalnum()]))
# # Preprocess tweets
# tweets_sample['processed_text'] = tweets_sample['token_text'].apply(lambda x: ' '.join([word.lower() for word in word_tokenize(str(x)) if word.isalnum()]))

# Trial function to text the model
# Combine quotes and authors into a single text for vectorization
quotes_df['combined'] = quotes_df['quote_2'] + " " + quotes_df['author_2']

# Vectorize the combined quotes
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(quotes_df['combined'])

# Assign column for labels
y = quotes_df.index  # Use the index of the DataFrame as the labels

# Train the SVM model
svm_model = SVC(C=10, gamma=1, kernel='rbf')
svm_model.fit(X, y)


# Instantiate and train the QuoteFinder class found within my_functions file
quote_finder = QuoteFinder(quotes_df)
quote_finder.train_model()

# Save the components
# quote_finder.save('data/vectorizer.pkl.gz', 'data/svm_model.pkl.gz', 'data/quotes_df.pkl.gz')

quote_finder.save(
    'src/data/model/vectorizer.pkl.gz', 
    'src/data/model/svm_model.pkl.gz', 
    'src/data/model/quotes_df.pkl.gz'
)

# Load the QuoteFinder class with the saved components

# quote_finder = QuoteFinder.load('data/vectorizer.pkl.gz', 'data/svm_model.pkl.gz', 'data/quotes_df.pkl.gz')

quote_finder = QuoteFinder.load(
    'src/data/vectorizer.pkl.gz', 
    'src/data/svm_model.pkl.gz', 
    'src/data/quotes_df.pkl.gz'
)

# Test the loaded model
quote, author = quote_finder.find_quote_for_tweet("Life is beautiful.")
print("Quote:", quote)
print("Author:", author)