import requests
import random

API_KEY = "15fdc9a36e2d3723f0e65ba51377f3af"
BASE_URL = "https://api.themoviedb.org/3"

# Function to get available genres
def get_genres():
    url = f"{BASE_URL}/genre/movie/list?api_key={API_KEY}&language=en-US"
    response = requests.get(url)
    data = response.json()
    return {genre["name"].lower(): genre["id"] for genre in data["genres"]}

# Function to get movies by genre
def get_movies_by_genre(genre_id):
    url = f"{BASE_URL}/discover/movie?api_key={API_KEY}&with_genres={genre_id}"
    response = requests.get(url)
    data = response.json()
    return data["results"]

# Main program
def recommend_movie():
    genres = get_genres()
    print("Available genres:", ", ".join(genres.keys()))

    user_input = input("Enter a movie genre: ").strip().lower()
    if user_input not in genres:
        print("Genre not found. Please try again.")
        return

    genre_id = genres[user_input]
    movies = get_movies_by_genre(genre_id)

    if not movies:
        print("No movies found for this genre.")
        return

    movie = random.choice(movies)
    print(f"Title: {movie['title']}")
    print(f"Overview: {movie['overview']}")
    print(f"Rating: {movie['vote_average']}/10")

recommend_movie()