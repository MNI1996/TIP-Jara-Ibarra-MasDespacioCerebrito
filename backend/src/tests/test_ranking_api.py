from unittest import TestCase

from mongoengine import connect, disconnect

import app
from backend.src.model.Player import Player

test_config = {
    'MONGODB_SETTINGS': {'alias': 'testing_db'}
}


class TestRankingPlayers(TestCase):

    def setUp(self):
        disconnect()
        self.test_app = app.get_flask_app(test_config)
        self.test_app.testing = True
        self.test_app.debug = True
        self.test_client = self.test_app.test_client()
        connect('testing_db', is_mock=True)

    def test_get_basic_ranking(self):
        player_1 = Player(nick='player_1', points=15).save()
        player_2 = Player(nick='player_2', points=2).save()
        player_3 = Player(nick='player_3', points=80).save()
        response = self.test_client.get("/ranking/players/")
        self.assertEqual(200, response.status_code)
        self.assertEqual(player_3.nick, response.json['result'][0]['_id'])
        self.assertEqual(player_1.nick, response.json['result'][1]['_id'])
        self.assertEqual(player_2.nick, response.json['result'][2]['_id'])

    def tearDown(self):
        disconnect()
