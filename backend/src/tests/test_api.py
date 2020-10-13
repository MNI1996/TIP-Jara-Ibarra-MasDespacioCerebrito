import unittest
from unittest.case import TestCase
from mongoengine import connect, disconnect
import app
from backend.src.model.Player import Player
from backend.src.model.Room import Room

test_config = {
    'MONGODB_SETTINGS': {'alias': 'testing_db'}
}


class TestApiQuestions(TestCase):

    def setUp(self):
        self.test_app = app.get_flask_app(test_config)
        self.test_app.testing = True
        self.test_app.debug = True
        self.test_client = self.test_app.test_client()
        connect('testing_db', is_mock=True)

    def test_connection_on_questions_get_and_empty_result(self):
        response = self.test_client.get("/questions/")
        self.assertEqual(200, response.status_code)
        self.assertEqual([], response.json["result"])

    def test_create_a_question(self):
        data = {"text": "Las 3 carabelas eran: la pinta, la niña y ...",
                "options": [{"sentence": "Santa Martina"},
                            {"sentence": "Santa Marina"},
                            {"sentence": "Santa Maria", "correct": "True"}
                            ]}
        response = self.test_client.post("/questions/", json=data)
        self.assertEqual(200, response.status_code)
        self.assertEqual(data["text"], response.json['result']['text'])

        response2 = self.test_client.get("/questions/")
        self.assertEqual(1, len(response2.json["result"]))
        self.assertEqual(data["text"], response2.json["result"][0]['text'])

    def test_create_a_question_with_no_text(self):
        data = {"options": [{"sentence": "Santa Martina"},
                            {"sentence": "Santa Marina"},
                            {"sentence": "Santa Maria", "correct": "True"}
                            ]}
        response = self.test_client.post("/questions/", json=data)
        self.assertEqual(400, response.status_code)
        self.assertEqual("ValidationError (Question:None) (Field is required: ['text'])", response.json['message'])

    def tearDown(self):
        disconnect('testing_db')


class TestApiPlayers(TestCase):

    def setUp(self):
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
        self.assertEqual(1, Player.objects.all().count())
        self.assertEqual(2, Player.objects.get(nick=data['nick']).points)

    def test_get_a_player_none_existing_nick(self):
        response = self.test_client.get("/players/?nick=NonExistingUser")
        self.assertEqual(404, response.status_code)

    def tearDown(self):
        disconnect('testing_db')


class TestApiRoom(TestCase):

    def setUp(self):
        self.test_app = app.get_flask_app(test_config)
        self.test_app.testing = True
        self.test_app.debug = True
        self.test_client = self.test_app.test_client()
        connect('testing_db', is_mock=True)

    def test_01_get_all_rooms_empty(self):
        response = self.test_client.get("/rooms/")
        self.assertEqual(200, response.status_code)
        self.assertEqual([], response.json['result'])

    def test_02_get_all_rooms_1_found(self):
        player = Player(nick="Juan")
        player_2 = Player(nick="Milagros")
        room = Room(name="sala del test 2", owner=player, participants=[player_2])
        room.save()
        response = self.test_client.get("/rooms/")
        self.assertEqual(200, response.status_code)
        self.assertEqual(room.name, response.json['result'][0]['_id'])
        self.assertEqual(player.nick, response.json['result'][0]['owner'])
        self.assertEqual(player_2.nick, response.json['result'][0]['participants'][0])

    def test_03_get_one_room_1_found(self):
        player = Player(nick="Juan")
        room = Room(name="sala del test 3", owner=player)
        room.save()
        response = self.test_client.get(f"/rooms/{room.name}/")
        self.assertEqual(200, response.status_code)
        self.assertEqual(room.name, response.json['result']['_id'])
        self.assertEqual(player.nick, response.json['result']['owner'])

    def test_04_get_one_room_1_not_found(self):
        response = self.test_client.get(f"/rooms/999/")
        self.assertEqual(404, response.status_code)

    def test_05_create_a_room(self):
        player = Player(nick="Juan")
        player.save()
        room_data = {'owner': "Juan",
                     'name': "Sala 1",
                     }
        response = self.test_client.post("/rooms/", data=room_data)
        self.assertEqual(200, response.status_code)
        self.assertEqual(player.nick, response.json['result']['owner'])
        self.assertEqual(room_data['name'], response.json['result']['_id'])

    def tearDown(self):
        disconnect('testing_db')


if __name__ == '__main__':
    unittest.main()
