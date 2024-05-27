import pandas as pd
import os
import pickle

# Define the path to the popular.pkl file
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
POPULAR_DATA_PATH = os.path.join(BASE_DIR, 'data', r'C:\Users\ABHINDHIRA\OneDrive\Documents\django\myworld\mangacart\manga\data\popular.pkl')

def get_popular_books():
    """
    Function to fetch popular books from precomputed data.
    Returns a list of dictionaries containing book information.
    """
    with open(POPULAR_DATA_PATH, 'rb') as f:
        popular_data = pickle.load(f)
    return popular_data.to_dict('records')
