# FootStats – Analyse et Modélisation des Données Footballistiques

## Contexte
FootStats est un projet qui permet d'automatiser la collecte, l’analyse et la visualisation de données footballistiques.  
Le projet inclut la récupération des données depuis des sources publiques (scraping), leur traitement, l’analyse statistique et la création d’une interface interactive avec Streamlit.

---

## Objectifs
- Collecter les données des matchs, joueurs, équipes et compétitions.
- Nettoyer et structurer les données pour l’analyse.
- Identifier les meilleurs buteurs, joueurs les plus décisifs et les équipes performantes.
- Visualiser les statistiques de manière interactive.
- Permettre le téléchargement des données filtrées.

---

## Étapes du projet

### 1️⃣ Récupération des données (Scraping)
- Collecter les données de matchs, joueurs et compétitions depuis des sites de football ou fichiers CSV.
- Extraire les informations clés : nom de l’équipe, joueur, position, buts, passes décisives, cartons, résultat du match, etc.
- Stocker les données dans une base PostgreSQL pour faciliter les requêtes et analyses.

### 2️⃣ Traitement des données
- Nettoyer et typager les colonnes.
- Remplir les valeurs manquantes.
- Créer des identifiants uniques pour équipes, joueurs, compétitions et matchs.
- Générer des tables relationnelles : `Joueur`, `Equipe`, `Competition`, `Match`, `StatistiqueJoueur`, `ResultatMatch`, `Participation`.

### 3️⃣ Analyse des données
- Top 10 des meilleurs buteurs.
- Joueurs les plus décisifs (buts + passes décisives).
- Joueurs les plus disciplinés (cartons jaunes et rouges).
- Répartition des nationalités par équipe.
- Puissance offensive et défensive des équipes.
- Classement des équipes par points.

### 4️⃣ Visualisation interactive avec Streamlit
- Filtres dynamiques par compétition et saison.
- Graphiques interactifs avec Plotly (bar charts, countplots, etc.).
- Tableau interactif pour afficher toutes les statistiques.
- Bouton de téléchargement des données filtrées au format CSV.
