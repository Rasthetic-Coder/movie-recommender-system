# Movie Recommender System

A content-based movie recommendation application built with FastAPI backend and Streamlit frontend. Get personalized movie recommendations based on similarity analysis.

## Features

- 🎬 **Movie Recommendations**: Find similar movies based on a selected movie
- 🖼️ **Poster Display**: View movie posters fetched from TMDB API
- ⚡ **Fast API**: High-performance FastAPI backend with movie similarity matching
- 🎨 **User-Friendly Interface**: Interactive Streamlit web interface
- 🔍 **Content-Based Filtering**: Uses cosine similarity to find related movies

## Tech Stack

- **Backend**: FastAPI + Uvicorn
- **Frontend**: Streamlit
- **Data Processing**: Pandas, NumPy
- **Machine Learning**: Scikit-learn
- **API Integration**: TMDB (The Movie Database)

## Prerequisites

- Python 3.8 or higher
- TMDB API key (get it from [https://www.themoviedb.org/settings/api](https://www.themoviedb.org/settings/api))

## Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd fastapi
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv myenv
   
   # On Windows
   myenv\Scripts\activate
   
   # On macOS/Linux
   source myenv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   
   Create a `.env` file in the project root:
   ```
   TMDB_API_KEY=your_tmdb_api_key_here
   ```

## Usage

The application requires pre-computed movie data and similarity matrix (pickle files):
- `movie_list.pkl` - Processed movie dataset
- `similarity.pkl` - Pre-calculated similarity matrix

### Run the Backend API

```bash
uvicorn main:app --reload --port 8000
```

The API will be available at `http://127.0.0.1:8000`

**API Endpoints:**
- `GET /` - Health check
- `POST /recommend` - Get movie recommendations
  ```json
  {
    "movie_name": "The Shawshank Redemption"
  }
  ```

### Run the Frontend

In a separate terminal:

```bash
streamlit run app.py
```

The Streamlit app will open at `http://localhost:8501`

## Project Structure

```
fastapi/
├── main.py              # FastAPI backend application
├── app.py               # Streamlit frontend application
├── movie_list.pkl       # Pickled movie dataset
├── similarity.pkl       # Pickled similarity matrix
├── patients.json        # Sample/reference data
├── requirements.txt     # Python dependencies
├── .env                 # Environment variables (create this)
└── README.md           # This file
```

## API Response Example

**Request:**
```bash
curl -X POST "http://127.0.0.1:8000/recommend" \
  -H "Content-Type: application/json" \
  -d '{"movie_name": "Inception"}'
```

**Response:**
```json
{
  "selected_movie": "Inception",
  "recommendations": [
    {
      "movie_id": 27205,
      "title": "Inception"
    },
    {
      "movie_id": 155,
      "title": "The Dark Knight"
    }
  ]
}
```

## How It Works

1. User enters a movie name in the Streamlit interface
2. Frontend sends a POST request to the FastAPI backend
3. Backend looks up the movie in the dataset
4. Uses pre-computed similarity matrix to find 5 most similar movies
5. Fetches movie posters from TMDB API
6. Returns recommendations with poster images to the frontend

## Error Handling

- **Movie Not Found**: Returns 404 error if the entered movie is not in the database
- **API Errors**: Graceful error messages displayed in the Streamlit app

## Environment Setup

Make sure you have a `.env` file with your TMDB API key:
```
TMDB_API_KEY=your_key_here
```

## Future Enhancements

- Add collaborative filtering recommendations
- Implement user rating system
- Add movie reviews and ratings display
- Support for advanced filtering (genre, year, rating)
- Caching for improved performance
- User preference profiles

## Contributing

Feel free to fork this project and submit pull requests for any improvements.

## License

This project is open source and available under the MIT License.

## Support

For issues or questions, please open an issue on GitHub.

---

**Note**: This application requires pre-trained model files (`movie_list.pkl` and `similarity.pkl`) to function. These should be generated from a movie dataset using content-based filtering techniques.
