import pytest
from postproject import app, db
from postproject.models import User


@pytest.fixture(scope='function')
def new_user():
    user = User('TestNewUser','TestNewUser@demo.com', 'demo')
    return user


@pytest.fixture
def client():
    client = app.test_client()
    return client


@pytest.fixture(scope='function')
def init_database(client):
    # Create the database and the database table
    db.create_all()

    # Insert user data
    user1 = User(username='TestNewUser', email='TestNewUser@demo.com', password='demo')
    db.session.add(user1)

    # Commit the changes for the users
    db.session.commit()

    yield  # this is where the testing happens!

    db.drop_all()
