# TODO: Feature 3

from src.repositories.movie_repository import get_movie_repository

def test_get_movie_by_title():
    # Create an instance of MovieRepository
    movie_repository_test = get_movie_repository()

    # Add some sample movies to the repository
    movie_repository_test.create_movie("The Shawshank Redemption", "Frank Darabont", 3.2)
    movie_repository_test.create_movie("The Godfather", "Francis Ford Coppola", 5.0)
    movie_repository_test.create_movie("The Dark Knight", "Christopher Nolan", 4.3)
    movie_repository_test.create_movie("Forrest Gump", "Robert Zemeckis", 4.5)

    # Test getting movies by title
    # Tests the movies by title director and rating
    movie_title = movie_repository_test.get_movie_by_title("The Shawshank Redemption").title
    movie_director = movie_repository_test.get_movie_by_title("The Shawshank Redemption").director
    movie_rating = movie_repository_test.get_movie_by_title("The Shawshank Redemption").rating

    assert movie_title == "The Shawshank Redemption"
    assert movie_rating == 3.2
    assert movie_director == "Frank Darabont"

    #Test case sensitivity (there should be none)
    

