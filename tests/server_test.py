from random import choice
from uuid import uuid4

from server import clubs, competitions

# ------- FUNCTIONAL TESTS ------------------
def test_unknown_email_login(client):
    """Function that tests login of an unknown email"""

    # GIVEN
    # an unknown_email
    unknown_email = str(uuid4()) + "@domain.com"

    # WHEN
    # login
    response = client.post('/showSummary', data={'email': unknown_email})

    # THEN
    assert response.status_code == 404
    assert "that email wasn't found" in str(response.data)


def test_known_email_login(client, valid_club):
    """Function that tests login of a valid email"""

    # GIVEN
    # an email in club
    known_email = valid_club['email']

    # WHEN
    # login
    response = client.post('/showSummary', data={'email': known_email})

    # THEN
    assert response.status_code == 200


def test_error_status_when_purchase_more_than_available(client, valid_club, valid_competition):
    """Function that tests if we receive an error message 400 when purchasing more than available points of the club"""

    # GIVEN
    # a club and a competition
    club = valid_club
    competition = valid_competition

    # WHEN
    # purchasing more places than available points
    response = client.post('/purchasePlaces', data={'club': club['name'],
                                                    'competition': competition['name'],
                                                    'places': str(int(club['points']) + 5)})

    # THEN
    # error response status
    assert response.status_code == 400


def test_valid_status_when_purchase_less_than_available(client, valid_club, valid_competition):
    """Function that tests if we receive a valid message 200 when purchasing less than available points of the club"""

    # GIVEN
    # a club and a competition and places
    club = valid_club
    competition = valid_competition
    places = '1' if int(club['points']) > 1 else '0'

    # WHEN
    # purchasing less places than available points
    response = client.post('/purchasePlaces', data={'club': club['name'],
                                                    'competition': competition['name'],
                                                    'places': places})

    # THEN
    # valid response status
    assert response.status_code == 200


def test_redeemed_points_correctly_deducted_from_club_total(client, valid_club, valid_competition):
    """Function that test if redeemed points are correctly deducted from the club's total"""

    # GIVEN
    # a club and a competition and places
    valid_club = valid_club
    valid_competition = valid_competition
    places = '1' if int(valid_club['points']) > 1 else '0'
    club_initial_points = int(valid_club['points'])

    # WHEN
    # purchasing places
    response = client.post('/purchasePlaces', data={'club': valid_club['name'],
                                                    'competition': valid_competition['name'],
                                                    'places': places})

    # THEN
    # points well updated
    assert int([c for c in clubs if c['name'] == valid_club['name']][0]['points']) == club_initial_points - int(places)


def test_booking_more_than_12_places(client, new_club_with_20_points, valid_competition):
    """Function that tests if we receive an error message 400 when purchasing more 12 places"""

    # GIVEN
    # a club and a competition
    new_club_with_20_points = new_club_with_20_points
    valid_competition = valid_competition
    places = '15'

    # WHEN
    # purchasing more places than available points
    response = client.post('/purchasePlaces', data={'club': new_club_with_20_points['name'],
                                                    'competition': valid_competition['name'],
                                                    'places': places})

    # THEN
    # error response status
    assert response.status_code == 400


def test_booking_less_than_12_places(client, new_club_with_20_points, valid_competition):
    """Function that tests if we receive a valid message 200 when purchasing less 12 places"""

    # GIVEN
    # a club and a competition
    new_club_with_20_points = new_club_with_20_points
    valid_competition = valid_competition
    places = '10'

    # WHEN
    # purchasing more places than available points
    response = client.post('/purchasePlaces', data={'club': new_club_with_20_points['name'],
                                                    'competition': valid_competition['name'],
                                                    'places': str(places)})

    # THEN
    # valid response status
    assert response.status_code == 200


def test_places_correctly_deducted_from_competition(client, new_club_with_20_points, valid_competition):
    """Function that test if places are correctly deducted from the competition when purchasing"""

    # GIVEN
    # a club and a competition and places
    new_club_with_20_points = new_club_with_20_points
    valid_competition = valid_competition
    places = '10'
    competition_initial_number_of_places = int(valid_competition['numberOfPlaces'])

    # WHEN
    # purchasing places
    response = client.post('/purchasePlaces', data={'club': new_club_with_20_points['name'],
                                                    'competition': valid_competition['name'],
                                                    'places': places})

    # THEN
    # places well deducted
    assert int([c for c in competitions if c['name'] == valid_competition['name']][0]['numberOfPlaces']) \
           == competition_initial_number_of_places - int(places)


def test_error_message_when_booking_past_competition(client, valid_club, new_past_competition):
    """Function that tests if we receive an error message 400 when purchasing places for a past competition"""

    # GIVEN
    # a club and a past competition
    club = valid_club
    past_competition = new_past_competition

    # WHEN
    # access booking page
    response = client.get(f"/book/{past_competition['name']}/{club['name']}")

    # THEN
    # error response status
    assert response.status_code == 400

def test_error_message_when_booking_future_competition(client, valid_club, new_future_competition):
    """Function that tests if we receive a valid message 200 when purchasing places for a future competition"""

    # GIVEN
    # a club and a past competition
    club = valid_club
    future_competition = new_future_competition

    # WHEN
    # access booking page
    response = client.get(f"/book/{future_competition['name']}/{club['name']}")

    # THEN
    # valid response status
    assert response.status_code == 200

def test_clubs_list_when_login(client, valid_club):
    """Function that check if user can see clubs lists when login"""

    # GIVEN
    # a valid club email
    known_email = valid_club['email']

    # WHEN
    # login
    response = client.post('/showSummary', data={'email': known_email})

    # THEN
    assert "Clubs" in str(response.data)
    assert "current points balance" in str(response.data)