# Movie Recommender System 🎬

A content-based movie recommendation application built with **FastAPI** backend and **Streamlit** frontend. Discover movies similar to your favorites using intelligent similarity analysis.

## 🚀 Live Demo
- **Streamlit Frontend:** https://movie-recommender-system-rasthetic-coder.streamlit.app/
- **FastAPI Backend:** https://movie-recommender-system-bmr9.onrender.com

## Features

- ✨ **Smart Recommendations**: Get 5 movies similar to any movie you select using cosine similarity
- 🎞️ **Movie Posters**: Beautiful poster display fetched from TMDB API
- ⚡ **High-Performance Backend**: FastAPI with async support for fast API responses
- 🎨 **Interactive UI**: Clean and intuitive Streamlit web interface
- 🔍 **Content-Based Filtering**: Analyzes movie features to find related content
- 🚀 **Production Ready**: Deployed on Streamlit Cloud for seamless access

## Tech Stack

| Layer | Technology |
|-------|-----------|
| **Backend** | FastAPI 0.136.3, Uvicorn |
| **Frontend** | Streamlit |
| **Deployment** | Streamlit Cloud |
| **Data Processing** | Pandas, NumPy |
| **Machine Learning** | Scikit-learn (Cosine Similarity) |
| **API Integration** | TMDB API (The Movie Database) |
| **Environment** | Python 3.8+, python-dotenv |

## Prerequisites

- **Python 3.8** or higher
- **TMDB API key** - Get your free account at [TMDB](https://www.themoviedb.org/settings/api)
- Pre-computed data files:
  - `movie_list.pkl` - Movie dataset with metadata
  - `similarity.pkl` - Pre-calculated similarity matrix

## Installation & Setup

### 1. Clone the Repository
```bash
git clone <repository-url>
cd fastapi
```

### 2. Create Virtual Environment
```bash
# Windows
python -m venv myenv
myenv\Scripts\activate

# macOS/Linux
python3 -m venv myenv
source myenv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Create a `.env` file in the project root:
```env
TMDB_API_KEY=your_api_key_here
```

Get your free API key from [TMDB Settings](https://www.themoviedb.org/settings/api)

## Running the Application

### Local Development

**Terminal 1 - Start Backend API:**
```bash
uvicorn main:app --reload --port 8000
```
- API docs: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

**Terminal 2 - Start Frontend:**
```bash
streamlit run app.py
```
- Frontend: http://localhost:8501

## Deployment

### Streamlit Cloud Deployment

The Streamlit frontend is live at: **https://movie-recommender-system-rasthetic-coder.streamlit.app/**

### Render Backend Deployment

The FastAPI backend is deployed on Render at: **https://movie-recommender-system-bmr9.onrender.com**

#### Deploy Your Own

**Streamlit Cloud:**
1. Push your code to a GitHub repository
2. Go to [Streamlit Cloud](https://streamlit.io/cloud)
3. Click "New app" and select your repository
4. Set the main file path to `app.py`
5. Add your `TMDB_API_KEY` in the Secrets section

**Render (FastAPI Backend):**
1. Create a Render account at [render.com](https://render.com)
2. Create a new Web Service and connect your GitHub repository
3. Set the build command: `pip install -r requirements.txt`
4. Set the start command: `uvicorn main:app --host 0.0.0.0`
5. Add environment variable: `TMDB_API_KEY=your_api_key_here`
6. Deploy and note the provided URL

## API Documentation

### How the Application Works

The **Streamlit frontend** communicates with the **FastAPI backend** to get movie recommendations:

1. User enters a movie name in the Streamlit interface
2. Streamlit sends a POST request to the FastAPI `/recommend` endpoint
3. FastAPI processes the request and returns 5 similar movies
4. Streamlit fetches movie posters from TMDB API and displays them

### Endpoints

#### Health Check
```
GET /
Response: {"message": "Movie Recommendation API"}
```

#### Get Recommendations
```
POST /recommend
Content-Type: application/json

Request:
{
  "movie_name": "The Shawshank Redemption"
}

Response:
{
  "selected_movie": "The Shawshank Redemption",
  "recommendations": [
    {
      "movie_id": 278,
      "title": "The Shawshank Redemption"
    },
    ...
  ]
}
```

## Project Structure

```
fastapi/
├── main.py                      # FastAPI application & recommendation logic
├── app.py                       # Streamlit web interface
├── movie_list.pkl              # Serialized movie dataset (required)
├── similarity.pkl              # Serialized similarity matrix (required)
├── requirements.txt            # Python dependencies
├── .env                        # Environment variables (create this)
├── .gitignore                  # Git ignore rules
├── README.md                   # This file
└── patients.json               # Sample/reference data
```

## How It Works

1. **Data Loading**: Pre-computed movie data and similarity matrix are loaded from pickle files
2. **Movie Search**: User enters a movie name in the Streamlit interface
3. **Similarity Calculation**: The FastAPI backend finds the movie index and retrieves top 5 similar movies using cosine similarity scores
4. **Poster Fetching**: Streamlit fetches movie posters from TMDB API for visual display
5. **Beautiful Display**: Results are shown in an attractive grid layout with movie titles and posters

## Dependencies

See `requirements.txt`:
- fastapi==0.136.3
- uvicorn
- streamlit
- pandas
- numpy
- scikit-learn
- requests
- python-dotenv

## Troubleshooting

### Movie Not Found Error
- Ensure the movie name exists in your `movie_list.pkl` dataset
- Movie names are case-sensitive
- Try searching for popular movies like "Inception" or "The Matrix"

### No Posters Displayed
- Check that `TMDB_API_KEY` is set correctly in `.env` or Streamlit Secrets
- Verify your API key has read access
- Some movies may not have poster images available

### Pickle Files Missing
- Generate `movie_list.pkl` and `similarity.pkl` using your movie dataset
- Ensure they're in the project root directory before running the app

### Backend Connection Issues (Local Development)
- Ensure the FastAPI backend is running on `http://127.0.0.1:8000`
- Update the `API_URL` in `app.py` if using a different backend URL
- Check that the backend and frontend are on the same network

## Future Enhancements

- [ ] Hybrid filtering (collaborative + content-based)
- [ ] User rating system
- [ ] Movie watchlist feature
- [ ] Advanced filters (genre, year, rating)
- [ ] Database integration (PostgreSQL/MongoDB)
- [ ] User authentication
- [ ] Caching for improved performance
- [ ] Deploy backend to cloud for production use

## License

This project is open source and available under the MIT License.

## Contact & Support

For issues, feature requests, or contributions, please open an issue in the repository.

---

**Happy Movie Hunting!** 🍿✨
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
