# TODO: Feature 2
from app import app, movie_repository
from pathlib import Path


def test_creating_movie_redirection(test_app):
    data={
        "moviename":"Titanic",
        "directorname" : "James Cameron",
        "movierating" : '3'
    }
    response = test_app.post("/movies", data=data)
    assert response.status_code == 302

# code 302 is for redirection 
    
def test_title(test_app):
    data={
        "moviename":"Titanic",
        "directorname" : "James Cameron",
        "rating" : '3'
    }
    response = test_app.post("/movies", data=data)
    
    movie = movie_repository.get_movie_by_title("Titanic")
    assert movie is not None
    assert movie.title == "Titanic"

def test_director(test_app):
    data={
        "moviename":"Titanic",
        "directorname" : "James Cameron",
        "rating" : '3'
    }
    response = test_app.post("/movies", data=data)
    
    movie = movie_repository.get_movie_by_title("Titanic")
    assert movie is not None
    assert movie.director == "James Cameron"

def test_director(test_app):
    data={
        "moviename":"Titanic",
        "directorname" : "James Cameron",
        "rating" : '3'
    }
    response = test_app.post("/movies", data=data)
    
    movie = movie_repository.get_movie_by_title("Titanic")
    assert movie is not None
    assert movie.director == "James Cameron"

def test_rating(test_app):
    data={
        "moviename":"Titanic",
        "directorname" : "James Cameron",
        "movierating" : '3'
    }
    response = test_app.post("/movies", data=data)
    
    movie = movie_repository.get_movie_by_title("Titanic")
    assert movie is not None
    assert movie.rating == '3'






    


    

    





    

