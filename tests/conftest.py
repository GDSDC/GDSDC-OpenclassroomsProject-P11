import pytest
from random import choice
from server import app, loadClubs, loadCompetitions


@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()

    ctx = app.app_context()
    ctx.push()
    yield client

    ctx.pop()


@pytest.fixture
def valid_club():
    clubs = loadClubs()
    return choice(clubs)


@pytest.fixture
def valid_competition():
    competitions = loadCompetitions()
    return choice(competitions)
