# app.py
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from preprocess import load_and_clean_data

# Charger les données prétraitées
df = load_and_clean_data('data/movies.csv', 'data/ratings.csv')

st.title("Analyseur de Données de Films - MovieLens")

# Afficher un aperçu des données
st.write("Aperçu des données des films :")
st.write(df.head())

# Visualisation des genres populaires
st.header("Distribution des Genres")
genre_count = df['genres'].str.split('|').explode().value_counts()
st.bar_chart(genre_count.head(20))  # Afficher les 20 genres les plus communs

# Visualisation des notes moyennes par année
st.header("Notes Moyennes par Année")
avg_rating_by_year = df.groupby('year')['avg_rating'].mean().dropna()
st.line_chart(avg_rating_by_year)
# Fonctionnalité de Recherche par Nom de Film
st.header("Recherche par Nom de Film")
film_name = st.text_input("Entrez le nom du film :")

if film_name:
    # Rechercher le film par nom (insensible à la casse)
    film_data = df[df['title'].str.contains(film_name, case=False, na=False)]

    if not film_data.empty:
        st.write(f"Résultats pour : **{film_name}**")
        st.write(film_data[['title', 'avg_rating', 'num_ratings', 'popularity']])

        # Visualiser les statistiques du film sélectionné
        st.header("Statistiques du Film")

        # Afficher un graphique des notes moyennes par année (si disponible)
        if 'year' in film_data.columns and not film_data['year'].isnull().all():
            st.subheader("Évolution des Notes Moyennes par Année")
            avg_rating_by_year = film_data.groupby('year')['avg_rating'].mean().dropna()
            st.line_chart(avg_rating_by_year)
        
        # Afficher la popularité du film
        st.subheader("Popularité du Film")
        st.bar_chart(film_data['popularity'])
        
        # Afficher les genres du film
        st.subheader("Genres")
        st.write(", ".join(film_data['genres'].iloc[0].split('|')))
    else:
        st.warning("Aucun film trouvé avec ce nom.")
else:
    st.info("Entrez un nom de film pour voir ses statistiques.")
    
# Visualisation des films les plus populaires
st.header("Top 10 des Films les Plus Populaires")
top_popular_movies = df.sort_values(by='popularity', ascending=False).head(10)
st.write(top_popular_movies[['title', 'avg_rating', 'num_ratings']])

# Visualisation interactive avec Seaborn
st.header("Popularité vs Notes")
fig, ax = plt.subplots(figsize=(10, 6))
sns.scatterplot(data=df, x='popularity', y='avg_rating', ax=ax)
st.pyplot(fig)
