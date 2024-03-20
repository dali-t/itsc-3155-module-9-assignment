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
    movie_case1 = movie_repository_test.get_movie_by_title("The ShawShank Redemption")

    assert movie_case1.title == "The Shawshank Redemption"
    assert movie_case1.rating == 3.2
    assert movie_case1.director == "Frank Darabont"

    movie_case_insensitivity = "FoRrEsT GuMp"
    movie_case2 = movie_repository_test.get_movie_by_title(movie_case_insensitivity)

    assert movie_case2.title == "Forrest Gump"
    assert movie_case2.director == "Robert Zemeckis"
    assert movie_case2.rating == 4.5

