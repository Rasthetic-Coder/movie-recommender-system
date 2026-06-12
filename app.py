from dotenv import load_dotenv
import streamlit as st
import requests
import os


load_dotenv()
TMDB_API_KEY = os.getenv("TMDB_API_KEY")

API_URL = "https://movie-recommender-system-bmr9.onrender.com/recommend"


def fetch_poster(movie_id):
    try:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={TMDB_API_KEY}&language=en-US"
        response = requests.get(url)

        if response.status_code != 200:
            return "https://via.placeholder.com/300x450?text=No+Image"

        data = response.json()
        poster_path = data.get("poster_path")

        if poster_path:
            return f"https://image.tmdb.org/t/p/w500{poster_path}"

        return "https://via.placeholder.com/300x450?text=No+Image"

    except:
        return "https://via.placeholder.com/300x450?text=No+Image"

st.title(" Movie Recommender System")

movie_name = st.text_input("Enter Movie Name")

if st.button("Recommend"):

    if not movie_name:
        st.warning("Please enter a movie name")
    else:

        response = requests.post(
            API_URL,
            json={"movie_name": movie_name}
        )

        if response.status_code == 200:

            data = response.json()
            recommendations = data["recommendations"]

            st.subheader("Recommended Movies:")

            cols = st.columns(5)

            for i, movie in enumerate(recommendations[:5]):

                poster = fetch_poster(movie["movie_id"])

                with cols[i]:
                    st.write(movie["title"])
                    st.image(poster, use_container_width=True)

        else:
            st.error("Movie not found or server error")