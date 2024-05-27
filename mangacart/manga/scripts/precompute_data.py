import pandas as pd
import pickle

# Load data
books = pd.read_csv('C://Users//ABHINDHIRA//OneDrive//Documents//django//myworld//mangacart//manga//datasets//Books.csv')
ratings = pd.read_csv('C://Users//ABHINDHIRA//OneDrive//Documents//django//myworld//mangacart//manga//datasets//Ratings.csv')

# Popularity based recommendation system
ratings_with_name = ratings.merge(books, on='ISBN')
num_rating_df = ratings_with_name.groupby('Book-Title').count()['Book-Rating'].reset_index()
num_rating_df.rename(columns={'Book-Rating': 'num_ratings'}, inplace=True)

ratings_with_name['Book-Rating'] = pd.to_numeric(ratings_with_name['Book-Rating'], errors='coerce')
ratings_with_name = ratings_with_name.dropna(subset=['Book-Rating'])

avg_rating = ratings_with_name.groupby('Book-Title')['Book-Rating'].mean().reset_index()
avg_rating.rename(columns={'Book-Rating': 'avg_ratings'}, inplace=True)

popular_df = num_rating_df.merge(avg_rating, on='Book-Title')
popular_df = popular_df[popular_df['num_ratings'] >= 250].sort_values('avg_ratings', ascending=False).head(50)
popular_df = popular_df.merge(books, on='Book-Title').drop_duplicates('Book-Title')[['Book-Title', 'Book-Author', 'Image-URL-M', 'num_ratings', 'avg_ratings']]
popular_df.rename(columns={
    'Book-Title': 'title',
    'Book-Author': 'author',
    'Image-URL-M': 'image_url',
    'num_ratings': 'num_ratings'
}, inplace=True)
# Save precomputed data
with open(r'C:\Users\ABHINDHIRA\OneDrive\Documents\django\myworld\mangacart\manga\data\popular.pkl', 'wb') as f:
    pickle.dump(popular_df, f)

print("Popularity-based data precomputed and saved successfully.")


