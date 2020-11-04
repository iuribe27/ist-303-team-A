import pytest
from postproject import app
from postproject import routes

@pytest.fixture
def client():
    client = app.test_client() 
    return client    

#pytest for app URLs
def test_home_route(client):
    url = '/'
    response = client.get(url)
    assert response.status_code == 200

def test_login_route(client):
    url = '/login'
    response = client.get(url)
    assert response.status_code == 200

def test_register_route(client):
    url = '/register'
    response = client.get(url)
    assert response.status_code == 200

def test_postits_route(client):
    url = '/post_its'
    response = client.get(url)
    assert response.status_code == 200
