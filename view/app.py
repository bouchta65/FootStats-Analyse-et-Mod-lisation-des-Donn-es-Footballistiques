import pandas as pd
import streamlit as st
from sqlalchemy import create_engine, text
import plotly.express as px


engine = create_engine("postgresql://postgres:123@localhost:5432/Scaping_Data2")

def run_query(query):
    with engine.connect() as conn:
        df = pd.read_sql_query(text(query), conn)
    return df


st.title("Analyse des données de FOOTBALL")


competitions_df = run_query("SELECT nomcompetition FROM Competition")
competition_list = competitions_df["nomcompetition"].tolist()
competition_filter = st.selectbox("Choisir une compétition", competition_list)

saisons_df = run_query("SELECT annee FROM Saison")
saison_list = saisons_df["annee"].tolist()
saison_filter = st.selectbox("Choisir une saison", saison_list)


query = f"""
SELECT j.nomjoueur, j.id_equipe, s.buts, s.passesdecisives, s.nbmatchesplayed
FROM StatistiqueJoueur s
JOIN Joueur j ON s.id_joueur = j.id_joueur
JOIN Equipe e ON j.id_equipe = e.id_equipe
JOIN Participation p ON e.id_equipe = p.id_equipe
JOIN Competition c ON p.id_competition = c.id_competition
JOIN Saison sa ON p.id_saison = sa.id_saison
WHERE c.nomcompetition = '{competition_filter}' AND sa.annee = '{saison_filter}'
"""

df_stats = run_query(query)


top_buteurs = df_stats.sort_values("buts", ascending=False).head(10)
fig_buts = px.bar(top_buteurs, x="nomjoueur", y="buts", title="Top 10 des meilleurs buteurs")
st.plotly_chart(fig_buts)

df_stats["buts_plus_passes"] = df_stats["buts"] + df_stats["passesdecisives"]
top_decisifs = df_stats.sort_values("buts_plus_passes", ascending=False).head(10)
fig_decisifs = px.bar(top_decisifs, x="nomjoueur", y="buts_plus_passes", title="Joueurs les plus décisifs")
st.plotly_chart(fig_decisifs)


st.subheader("Tableau des statistiques")
st.dataframe(df_stats)

csv = df_stats.to_csv(index=False).encode('utf-8')
st.download_button(
    label="Télécharger les données filtrées",
    data=csv,
    file_name='statistiques_football.csv',
    mime='text/csv'
)
