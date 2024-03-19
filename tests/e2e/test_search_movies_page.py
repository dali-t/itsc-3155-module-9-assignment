# TODO: Feature 3


def test_search_before_search(test_app):
    response = test_app.get('/movies/search')
    data = response.data.decode('utf-8')

    assert response.status_code == 200
    assert '<p>Please enter a movie!</p>' in data

def test_search_with_valid_entry(test_app):
    response = test_app.post("/movies/search", data = {
        'movie-search' : 'The Dark Knight'
    })

    data = response.data.decode('utf-8')

    assert response.status_code == 200
    assert '<p>The rating for "The Dark Knight" is 4.3</p>' in data
    
# Not supposed to be case sensitive
def test_search_case_sensitivity(test_app):
    response = test_app.post("/movies/search", data = {
        'movie-search' : 'tHe DaRk KnIgHt'
    })

    data = response.data.decode('utf-8')

    assert response.status_code == 200
    assert '<p>The rating for "The Dark Knight" is 4.3</p>' in data

def test_search_with_invalid_entry(test_app):
    response = test_app.post('/movies/search', data = {
        'movie-search' : 'Kung-Fu Panda'
    })
    data = response.data.decode('utf-8')

    assert response.status_code == 200
    assert '<p>The Movie you have requested is not in the database (or spelled incorrectly!) 😢</p>' in data
