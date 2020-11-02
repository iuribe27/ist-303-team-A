import pytest
from postproject import app
from postproject import routes

#pytest for app URLs
def test_home_route():
    client = app.test_client()
    url = '/'
    response = client.get(url)
    assert response.status_code == 200

def test_login_route():
    client = app.test_client()
    url = '/login'
    response = client.get(url)
    assert response.status_code == 200

def test_register_route():
    client = app.test_client()
    url = '/register'
    response = client.get(url)
    assert response.status_code == 200

def test_postits_route():
    client = app.test_client()
    url = '/post_its'
    response = client.get(url)
    assert response.status_code == 200
