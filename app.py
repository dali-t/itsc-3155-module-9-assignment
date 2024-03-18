from flask import Flask, redirect, render_template, request, url_for

from src.repositories.movie_repository import get_movie_repository

app = Flask(__name__)

# Get the movie repository singleton to use throughout the application
movie_repository = get_movie_repository()

def populate_movie_repo():
    # Sample movie data
    movies_data = [
        {
            "title": "The Shawshank Redemption",
            "director": "Frank Darabont",
            "rating": 4.9
        },
        {
            "title": "The Godfather",
            "director": "Francis Ford Coppola",
            "rating": 4.6
        },
        {
            "title": "The Dark Knight",
            "director": "Christopher Nolan",
            "rating": 4.8
        },
        {
            'title': 'Attack on Titan',
            'director': 'Crunchyroll',
            'rating': 4.5
        }
    ]

    # Populate the movie repository
    for movie_data in movies_data:
        movie_repository.create_movie(
            title=movie_data['title'],
            director=movie_data['director'],
            rating=movie_data['rating']
        )

# Call the function to populate _movie_repo
populate_movie_repo()

@app.get('/')
def index():
    return render_template('index.html')


@app.get('/movies')
def list_all_movies():
    # TODO: Feature 1
    return render_template('list_all_movies.html', list_movies_active=True)


@app.get('/movies/new')
def create_movies_form():
    return render_template('create_movies_form.html', create_rating_active=True)


@app.post('/movies')
def create_movie():
    # TODO: Feature 2
    # After creating the movie in the database, we redirect to the list all movies page
    return redirect('/movies')


@app.route('/movies/search', methods=['GET', 'POST'])
def search_movies():
    # TODO: Feature 3
    # first get the movie by title
    # Somehow get the movie's rating
    # return that to the search_movies.html
    if request.method == 'POST':
        movie_search = request.form.get('movie-search')
        movie_search_trim = movie_search.strip().lower()

        movie = movie_repository.get_movie_by_title(movie_search_trim)

        if movie is not None:
            rating = movie.rating
            movie_title = movie.title
        else:
            rating = -1;
            movie_title = ''
        return render_template('search_movies.html', search_active=True, rating=rating, movie_title=movie_title)
    return render_template('search_movies.html', search_active=True, rating=None)


@app.get('/movies/<int:movie_id>')
def get_single_movie(movie_id: int):
    # TODO: Feature 4
    return render_template('get_single_movie.html')


@app.get('/movies/<int:movie_id>/edit')
def get_edit_movies_page(movie_id: int):
    return render_template('edit_movies_form.html')


@app.post('/movies/<int:movie_id>')
def update_movie(movie_id: int):
    # TODO: Feature 5
    # After updating the movie in the database, we redirect back to that single movie page
    return redirect(f'/movies/{movie_id}')


@app.post('/movies/<int:movie_id>/delete')
def delete_movie(movie_id: int):
    # TODO: Feature 6
    pass
