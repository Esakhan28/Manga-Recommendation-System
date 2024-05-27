import numpy as np
import pickle



def recommend(book_name):
    with open(r'C:\Users\ABHINDHIRA\OneDrive\Documents\django\myworld\mangacart\manga\data\book_recommendation_model.pkl', 'rb') as file:
      data = pickle.load(file)

    pt = data['pivot_table']
    similarities = data['similarities']
    books = data['books']
    if book_name in pt.index:
        index = np.where(pt.index == book_name)[0][0]
        similar_books_list = sorted(
            list(enumerate(similarities[index])), key=lambda x: x[1], reverse=True)[1:11]

        recommended_books = [pt.index[book[0]] for book in similar_books_list]
        return recommended_books
    else:
        return 'Book Not Found'