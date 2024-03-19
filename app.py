from flask import Flask, redirect, render_template, request, url_for

from src.repositories.movie_repository import get_movie_repository

app = Flask(__name__)

# Get the movie repository singleton to use throughout the application
movie_repository = get_movie_repository()

# FOR TESTING PURPOSES ONLY
movie_repository.create_movie("The Shawshank Redemption", "Frank Darabont", 3.2)
movie_repository.create_movie("The Godfather", "Francis Ford Coppola", 5.0)
movie_repository.create_movie("The Dark Knight", "Christopher Nolan", 4.3)
movie_repository.create_movie("Forrest Gump", "Robert Zemeckis", 4.5)


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

#Beginning of Sang's methods for Feature 3
#Sang Vang's Get Request Method
@app.get('/movies/search')
def search_movies():
    # TODO: Feature 3
    # first get the movie by title
    # Somehow get the movie's rating
    # return that to the search_movies.html
    return render_template('search_movies.html', search_active=True, rating=None)

#Sang Vang's Post request Method
@app.post('/movies/search')
def movie_search():
    movie_search = request.form.get('movie-search')
    movie_search_trim = movie_search.strip().lower()

    movie = movie_repository.get_movie_by_title(movie_search_trim)
    if movie is not None:
        rating = movie.rating
        movie_title = movie.title
    else:
        rating = -1;
        movie_title = None
    return render_template('search_movies.html', search_active=True, rating=rating, movie_title=movie_title)

#End of Sang Vang's Methods for Feature 3


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
