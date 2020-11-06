from unittest import TestCase

from mongoengine import connect, disconnect

import app
from backend.src.model.Player import Player

test_config = {
    'MONGODB_SETTINGS': {'alias': 'testing_db'}
}


class TestApiPlayers(TestCase):

    def setUp(self):
        disconnect()
        self.test_app = app.get_flask_app(test_config)
        self.test_app.testing = True
        self.test_app.debug = True
        self.test_client = self.test_app.test_client()
        connect('testing_db', is_mock=True)

    def test_create_a_player(self):
        data = {"nick": "TestPlayer"}
        response = self.test_client.post("/players/", json=data)
        self.assertEqual(200, response.status_code)
        self.assertEqual(data["nick"], response.json['result']['_id'])

    def test_get_a_player(self):
        data = {"nick": "TestPlayer"}
        self.test_client.post("/players/", json=data)
        response = self.test_client.get("/players/?nick=TestPlayer")
        self.assertEqual(200, response.status_code)
        self.assertEqual(data["nick"], response.json['result']['_id'])

    def test_create_a_player_with_existing_nick_and_not_creates_a_new_one(self):
        data = {"nick": "TestPlayer"}
        self.test_client.post("/players/", json=data)
        player = Player.objects.get(nick=data['nick'])
        player.points = 2
        player.save()
        response = self.test_client.post("/players/", json=data)
        self.assertEqual(200, response.status_code)
        self.assertEqual(1, len(Player.objects.all()))
        self.assertEqual(2, Player.objects.get(nick=data['nick']).points)

    def test_get_a_player_none_existing_nick(self):
        response = self.test_client.get("/players/?nick=NonExistingUser")
        self.assertEqual(404, response.status_code)

    def tearDown(self):
        disconnect('testing_db')
