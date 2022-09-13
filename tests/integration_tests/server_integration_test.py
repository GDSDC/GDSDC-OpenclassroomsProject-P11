from server import loadClubs, loadCompetitions, clubs, competitions


def test_index(client):
    """Function to test server.index function"""

    # GIVEN
    # a client

    # WHEN
    # access index
    response = client.get('/')

    # THEN
    assert response.status_code == 200
    assert "Welcome to the GUDLFT Registration Portal!" in str(response.data)


def test_showSummary(client, valid_club):
    """Function that tests server.showSummary function"""

    # GIVEN
    # an email in club
    known_email = valid_club['email']

    # WHEN
    # login
    response = client.post('/showSummary', data={'email': known_email})

    # THEN
    assert response.status_code == 200


def test_book(client, valid_club, new_future_competition):
    """Function that tests server.book function"""

    # GIVEN
    # a club and a future competition
    club = valid_club
    future_competition = new_future_competition

    # WHEN
    # access booking page
    response = client.get(f"/book/{future_competition['name']}/{club['name']}")

    # THEN
    # valid response status
    assert response.status_code == 200


def test_purchasePlaces(client, valid_club, valid_competition):
    """Function that tests server.purchasePlaces function"""

    # GIVEN
    # a club and a competition and places
    club = valid_club
    club_initial_points = int(valid_club['points'])
    competition = valid_competition
    competition_initial_number_of_places = int(valid_competition['numberOfPlaces'])
    places = '1' if int(club['points']) > 1 else '0'

    # WHEN
    # purchasing
    response = client.post('/purchasePlaces', data={'club': club['name'],
                                                    'competition': competition['name'],
                                                    'places': places})

    # THEN
    # valid response status
    assert response.status_code == 200
    # points well updated from club points
    assert int([c for c in clubs if c['name'] == valid_club['name']][0]['points']) == club_initial_points - int(places)
    # places well deducted from competitions numberOfPlaces
    assert int([c for c in competitions if c['name'] == valid_competition['name']][0]['numberOfPlaces']) \
           == competition_initial_number_of_places - int(places)


def test_showClubsSummary(client):
    """Function that tests server.showClubsSummary function"""

    # GIVEN
    # a client

    # WHEN
    # access showClubsSummary
    response = client.get('/showClubsSummary')

    # THEN
    assert response.status_code == 200
    assert "Clubs:" in str(response.data)


def test_logout(client):
    """Function that tests server.logout function"""

    # GIVEN
    # a client

    # WHEN
    # logout
    response = client.get('/logout')

    # THEN
    assert response.status_code == 302


def test_loadClubs():
    """Function that tests server.loadClubs function."""

    # GIVEN
    # a list of clubs from clubs.json
    initial_clubs = [{"name": "Simply Lift", "email": "john@simplylift.co", "points": "13"},
                     {"name": "Iron Temple", "email": "admin@irontemple.com", "points": "4"},
                     {"name": "She Lifts", "email": "kate@shelifts.co.uk", "points": "12"}]

    # WHEN
    # execute loadClubs
    result_clubs = loadClubs()

    # THEN
    assert result_clubs == initial_clubs


def test_loadCompetitions():
    """Function that tests server.loadCompetitions function."""

    # GIVEN
    # a list of competitions from competitions.json
    initial_competitions = [{"name": "Spring Festival", "date": "2020-03-27 10:00:00", "numberOfPlaces": "25"},
                            {"name": "Fall Classic", "date": "2022-10-22 13:30:00", "numberOfPlaces": "13"}]

    # WHEN
    # execute loadCompetitions
    result_competitions = loadCompetitions()

    # THEN
    assert result_competitions == initial_competitions
