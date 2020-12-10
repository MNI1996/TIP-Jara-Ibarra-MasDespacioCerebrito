import unittest
from unittest.case import TestCase

from mongoengine import connect, disconnect

import app
from backend.src.model.Player import Player
from backend.src.model.Room import Room

test_config = {
    'MONGODB_SETTINGS': {'alias': 'testing_db'}
}


class TestApiSearch(TestCase):

    def setUp(self):
        disconnect()
        self.test_app = app.get_flask_app(test_config)
        self.test_app.testing = True
        self.test_app.debug = True
        self.test_client = self.test_app.test_client()
        connect('testing_db', is_mock=True)

    def test_search_no_results(self):
        response = self.test_client.get("/rooms/search/?q=asd")
        self.assertEqual(200, response.status_code)
        self.assertEqual([], response.json['result'])

    def test_search_room_name_1_found(self):
        player = Player(nick="Juan")
        player_2 = Player(nick="Milagros")
        room = Room(name="sala del test 2", owner=player, participants=[player_2])
        room.save()
        response = self.test_client.get("/rooms/search/?q=test")
        self.assertEqual(200, response.status_code)
        self.assertEqual(room.name, response.json['result'][0]['_id'])
        self.assertEqual(player.nick, response.json['result'][0]['owner'])
        self.assertEqual(player_2.nick, response.json['result'][0]['participants'][0])

    def test_search_owner_nick_1_found(self):
        player = Player(nick="Juan").save()
        player_2 = Player(nick="Milagros").save()
        room = Room(name="sala del test 2", owner=player, participants=[player_2])
        room.save()
        response = self.test_client.get("/rooms/search/?q=juan")
        self.assertEqual(200, response.status_code)
        self.assertEqual(room.name, response.json['result'][0]['_id'])
        self.assertEqual(player.nick, response.json['result'][0]['owner'])
        self.assertEqual(player_2.nick, response.json['result'][0]['participants'][0])

    def test_search_owner_nick_and_room_name_1_found(self):
        player = Player(nick="Juan").save()
        player_2 = Player(nick="Milagros").save()
        room = Room(name="Sala de Juan", owner=player, participants=[player_2])
        room.save()
        response = self.test_client.get("/rooms/search/?q=juan")
        self.assertEqual(200, response.status_code)
        self.assertEqual(1,  len(response.json['result']))
        self.assertEqual(room.name, response.json['result'][0]['_id'])
        self.assertEqual(player.nick, response.json['result'][0]['owner'])
        self.assertEqual(player_2.nick, response.json['result'][0]['participants'][0])

    def tearDown(self):
        disconnect()


if __name__ == '__main__':
    unittest.main()
