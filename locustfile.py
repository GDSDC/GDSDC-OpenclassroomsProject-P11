from datetime import datetime
from random import choice
from uuid import uuid4

from locust import HttpUser, task

from server import clubs, competitions


class appLocustTests(HttpUser):
    @task
    def index(self):
        self.client.get("/")

    @task
    def unknown_user_login(self):
        unknown_email = str(uuid4()) + "@domain.com"
        self.client.post('/showSummary', data={'email': unknown_email})

    @task
    def logout(self):
        self.client.get('/logout')

    @task
    def valid_login(self):
        valid_email = choice(clubs)['email']
        self.client.post('/showSummary', data={'email': valid_email})

    @task
    def clubs_summary(self):
        self.client.get('/showClubsSummary')

    @task
    def purshace_places(self):
        valid_club = choice(clubs)
        valid_competetion = choice(competitions)
        places = 1
        self.client.post('/purchasePlaces', data={'club': valid_club['name'],
                                                  'competition': valid_competetion['name'],
                                                  'places': str(places)})
        # purchase -1 to get back initial club points to prevent failures
        self.client.post('/purchasePlaces', data={'club': valid_club['name'],
                                                  'competition': valid_competetion['name'],
                                                  'places': str(-places)})

    @task
    def book_future_competition(self):
        valid_club = choice(clubs)
        future_competition = choice(
            [comp for comp in competitions if datetime.fromisoformat(comp['date']) > datetime.now()])
        self.client.get(f"/book/{future_competition['name']}/{valid_club['name']}")
