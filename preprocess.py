# preprocess.py
import pandas as pd

def load_and_clean_data(movies_file, ratings_file):
    # Charger les données des films et des notations
    movies = pd.read_csv('data/movie.csv')
    ratings = pd.read_csv('data/rating.csv')

    # Joindre les films et les notations sur le champ 'movieId'
    df = pd.merge(ratings, movies, on='movieId')

    # Extraire l'année des titres des films
    df['year'] = df['title'].str.extract(r'\((\d{4})\)').astype(float)

    # Calculer la note moyenne et le nombre de notations pour chaque film
    df = df.groupby(['movieId', 'title', 'genres', 'year']).agg(
        avg_rating=('rating', 'mean'),
        num_ratings=('rating', 'count'),
        popularity=('rating', 'sum')
    ).reset_index()

    # Filtrer les films avec au moins 50 notations pour une analyse significative
    df = df[df['num_ratings'] >= 50]

    return df
