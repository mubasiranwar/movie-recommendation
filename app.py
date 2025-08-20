import streamlit as st
import pickle
import requests   # ✅ You forgot this

# Load data
movies = pickle.load(open("movies.pkl", "rb"))
similarity = pickle.load(open("similarity.pkl", "rb"))

# Fetch movie poster using TMDB API
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
    data = requests.get(url).json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

# Recommend function (returns titles + posters)
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = similarity[index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_posters = []

    for i in movie_list:
        movie_id = movies.iloc[i[0]].movie_id   # ✅ get movie_id for poster
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_posters.append(fetch_poster(movie_id))

    return recommended_movies, recommended_posters

# Streamlit UI
st.title("🎬 Movie Recommender System")

selected_movie = st.selectbox(
    "Choose a movie:",
    movies['title'].values
)

if st.button("Recommend"):
    names, posters = recommend(selected_movie)

    # Show movies in 5 columns with posters
    cols = st.columns(5)
    for idx, col in enumerate(cols):
        with col:
            st.text(names[idx])
            st.image(posters[idx])
            st.caption("Poster")
            st.write("---")  # Separator for better UI