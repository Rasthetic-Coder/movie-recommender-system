from dotenv import load_dotenv
import streamlit as st
import requests
import os

API_URL = "https://movie-recommender-system-bmr9.onrender.com/recommend"

load_dotenv()

TMDB_API_KEY = os.getenv("TMDB_API_KEY")


def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={TMDB_API_KEY}&language=en-US"

    data = requests.get(url).json()

    poster_path = data.get("poster_path")

    if poster_path:
        return f"https://image.tmdb.org/t/p/w500/{poster_path}"

    return None


st.title("Movie Recommender System")

movie_name = st.text_input("Enter Movie Name")
if st.button("Recommend"):

    response = requests.post(
        API_URL,
        json={
            "movie_name": movie_name
        }
    )

    if response.status_code == 200:

        data = response.json()

        recommendations = data["recommendations"]

        cols = st.columns(5)

        for i, movie in enumerate(recommendations):

            poster = fetch_poster(movie["movie_id"])

            with cols[i]:
                st.write(movie["title"])
                st.image(poster)

    else:
        st.error("Movie not found")

