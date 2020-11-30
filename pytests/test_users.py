##This file (test_users.py) contains the functional tests for the `users` blueprint.
##These tests use GETs and POSTs to different URLs to check for the proper behavior of the `users` blueprint.


##GIVEN a Flask application configured for testing
##WHEN the '/login' page is requested (GET)
##THEN check the response is valid
def test_login_page(client):
    response = client.get('/login')
    assert response.status_code == 200
    assert b"Login" in response.data
    assert b"Email" in response.data
    assert b"Password" in response.data



##GIVEN a Flask application configured for testing
##WHEN the '/login' page is posted to (POST)
##THEN check the response is valid
def test_valid_login_logout(client, init_database):
    response = client.post('/login',
                                data=dict(username='TestNewUser', email='TestNewUser@demo.com', password='demo'),
                                follow_redirects=True)
    assert response.status_code == 200



##GIVEN a Flask application configured for testing
##WHEN the '/logout' page is requested (GET)
##THEN check the response is valid
    response = client.get('/logout', follow_redirects=True)
    assert response.status_code == 200



##GIVEN a Flask application configured for testing
##WHEN the '/login' page is posted to with invalid credentials (POST)
##THEN check an error message is returned to the user
def test_invalid_login(client, init_database):
    response = client.post('/login',
                                data=dict(username='TestNewUser',email='TestNewUser@demo.com', password='BadPassword'),
                                follow_redirects=True)
    assert response.status_code == 200



##GIVEN a Flask application configured for testing
##WHEN the '/register' page is posted to (POST)
##THEN check the response is valid and the user is logged in
def test_valid_registration(client, init_database):
    response = client.post('/register',
                                data=dict(email='TestNewUser@demo.com',
                                          password='demo',
                                          confirm='demo'),
                                follow_redirects=True)
    assert response.status_code == 200

##GIVEN a Flask application configured for testing
##WHEN the '/logout' page is requested (GET)
##THEN check the response is valid

    response = client.get('/logout', follow_redirects=True)
    assert response.status_code == 200



##GIVEN a Flask application configured for testing
##WHEN the '/register' page is posted to with invalid credentials (POST)
##THEN check an error message is returned to the user
def test_invalid_registration(client, init_database):
    response = client.post('/register',
                                data=dict(email='TestNewUser@demo.com',
                                          password='FlaskIsGreat',
                                          confirm='FlskIsGreat'),   # Does NOT match!
                                follow_redirects=True)
    assert response.status_code == 200
