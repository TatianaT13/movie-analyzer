# Analyseur de Données de Films - MovieLens

Ce projet est une application interactive qui permet d'analyser et de visualiser des données de films à partir du dataset MovieLens 20M. L'application permet de rechercher des films par nom et d'explorer leurs statistiques, comme les notes moyennes, la popularité, et les genres.

## Description

L'application utilise Streamlit pour fournir une interface utilisateur intuitive qui permet d'explorer des données de films. Elle offre des visualisations interactives pour la distribution des genres, l'évolution des notes moyennes par année, et la popularité des films. Une fonctionnalité de recherche permet de trouver des films par nom et d'afficher leurs statistiques détaillées.

## Installation

1. **Cloner le dépôt :**

   ```bash
   git clone https://github.com/TatianaT13/movie-analyzer.git
   cd movie-analyzer
   ```
Créer un environnement virtuel et activer-le :

    ```
    python -m venv env
    source env/bin/activate  # Sur Windows: env\Scripts\activate
    ````

Installer les dépendances :

    ```
    pip install -r requirements.txt
    ````

## Télécharger le dataset :

Télécharge le dataset MovieLens 20M depuis Kaggle et place les fichiers movies.csv et ratings.csv dans le dossier data/.

## Utilisation
Pour lancer l'application, exécute la commande suivante :

    ```
    streamlit run app.py
    ```

Cela ouvrira l'application dans ton navigateur. Tu pourras explorer les données, rechercher des films par nom, et voir leurs statistiques détaillées.

## Fonctionnalités

Recherche par Nom de Film : Entrez un nom de film pour voir ses statistiques, y compris les notes moyennes, la popularité, et les genres.

Distribution des Genres : Affiche un graphique des genres les plus populaires parmi les films du dataset.

Notes Moyennes par Année : Visualise l'évolution des notes moyennes des films au fil des ans.

Top 10 des Films les Plus Populaires : Liste les films les plus populaires selon le nombre de notations et leur popularité.

Popularité vs Notes : Graphique interactif montrant la relation entre la popularité des films et leurs notes moyennes.
