from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Annotated
import pickle
import os

app = FastAPI()

# Load pickle files
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(BASE_DIR, "movie_list.pkl"), "rb") as f:
    movies = pickle.load(f)

with open(os.path.join(BASE_DIR, "similarity.pkl"), "rb") as f:
    similarity = pickle.load(f)


class MovieInput(BaseModel):
    movie_name: Annotated[
        str,
        Field(..., description="Movie name")
    ]


@app.get("/")
def home():
    return {
        "message": "Movie Recommendation API"
    }


@app.post("/recommend")
def recommend_movie(data: MovieInput):

    movie = data.movie_name

    if movie not in movies["title"].values:
        raise HTTPException(
            status_code=404,
            detail="Movie not found"
        )

    movie_index = movies[movies["title"] == movie].index[0]

    distances = sorted(
        list(enumerate(similarity[movie_index])),
        reverse=True,
        key=lambda x: x[1]
    )

    recommendations = []

    for i in distances[1:6]:

        recommendations.append({
            "movie_id": int(movies.iloc[i[0]].movie_id),
            "title": movies.iloc[i[0]].title
        })

    return {
        "selected_movie": movie,
        "recommendations": recommendations
    }