from unittest import TestCase

from mongoengine import connect, disconnect

import app
from backend.src.model.Player import Player

test_config = {
    'MONGODB_SETTINGS': {'alias': 'testing_db'}
}


class TestApiAuthentication(TestCase):

    def setUp(self):
        disconnect()
        self.test_app = app.get_flask_app(test_config)
        self.test_app.testing = True
        self.test_app.debug = True
        self.test_client = self.test_app.test_client()
        connect('testing_db', is_mock=True)

    def test_register_a_player(self):
        data = {"nick": "TestPlayer", "password": "123456"}
        response = self.test_client.post("/register/", json=data)
        self.assertEqual(200, response.status_code)
        self.assertEqual(data["nick"], response.json['result']['_id'])
        self.assertEqual(data["password"], response.json['result']['password'])

    def test_register_a_player_with_used_nick(self):
        data = {"nick": "TestPlayer", "password": "123456"}
        self.test_client.post("/register/", json=data)
        response = self.test_client.post("/register/", json=data)
        self.assertEqual(400, response.status_code)

    def test_login_a_player(self):
        data = {"nick": "TestPlayer", "password": "123456"}
        self.test_client.post("/register/", json=data)
        response = self.test_client.post("/login/", json=data)
        self.assertEqual(200, response.status_code)
        self.assertEqual(data["nick"], response.json['result']['_id'])
        self.assertEqual(data["password"], response.json['result']['password'])

    def test_login_a_player_wrong_password(self):
        data = {"nick": "TestPlayer", "password": "123456"}
        self.test_client.post("/register/", json=data)
        data_2 = {"nick": "TestPlayer", "password": "1234562"}
        response = self.test_client.post("/login/", json=data_2)
        self.assertEqual(400, response.status_code)

    def test_login_a_player_with_empty_password(self):
        data = {"nick": "TestPlayer", "password": "123456"}
        self.test_client.post("/register/", json=data)
        data_2 = {"nick": "TestPlayer", "password": ""}
        response = self.test_client.post("/login/", json=data_2)
        self.assertEqual(400, response.status_code)

    def test_login_a_player_no_send_password_field(self):
        data = {"nick": "TestPlayer", "password": "123456"}
        self.test_client.post("/register/", json=data)
        data_2 = {"nick": "TestPlayer"}
        response = self.test_client.post("/login/", json=data_2)
        self.assertEqual(400, response.status_code)

    def test_login_a_player_non_existing_user(self):
        data_2 = {"nick": "TestPlayer", "password": "1234562"}
        response = self.test_client.post("/login/", json=data_2)
        self.assertEqual(400, response.status_code)

    def tearDown(self):
        disconnect('testing_db')
