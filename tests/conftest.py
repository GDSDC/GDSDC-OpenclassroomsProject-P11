import pytest
from random import choice
from server import app, loadClubs, loadCompetitions, clubs, competitions


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
    return choice(clubs)


@pytest.fixture
def new_club_with_20_points():
    new_club = {
        "name": "New Club 20 points",
        "email": "test@test.co",
        "points": "20"
    }
    clubs.append(new_club)
    return new_club


@pytest.fixture
def valid_competition():
    return choice(competitions)
