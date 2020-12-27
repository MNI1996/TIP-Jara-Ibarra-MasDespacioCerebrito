from unittest import TestCase

from mongoengine import connect, disconnect

import app
from backend.src.model.Player import Player

test_config = {
    'MONGODB_SETTINGS': {'alias': 'testing_db'}
}


class TestApiUpdateProfile(TestCase):

    def setUp(self):
        disconnect()
        self.test_app = app.get_flask_app(test_config)
        self.test_app.testing = True
        self.test_app.debug = True
        self.test_client = self.test_app.test_client()
        connect('testing_db', is_mock=True)

    def test_update_a_player_avatar_image(self):
        player = Player.objects.create(nick="Jose")
        self.assertEqual('man', player.avatar_image_name)
        data = {"avatar_image": "woman"}
        response = self.test_client.post(f"/player/{player.nick}/update/", json=data)
        player.reload()
        self.assertEqual(200, response.status_code)
        self.assertEqual('woman', player.avatar_image_name)
        self.assertEqual('woman', response.json['result']['avatar_image_name'])

    def tearDown(self):
        disconnect('testing_db')
