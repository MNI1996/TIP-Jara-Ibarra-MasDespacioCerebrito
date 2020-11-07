import unittest
from unittest.case import TestCase
from mongoengine import connect, disconnect
import app
from backend.src.model.Player import Player
from backend.src.model.Question import Question
from backend.src.model.Room import Room, Category

test_config = {
    'MONGODB_SETTINGS': {'alias': 'testing_db'}
}


class TestApiRoom(TestCase):

    def setUp(self):
        disconnect()
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
        response = self.test_client.post("/rooms/", json=room_data)
        self.assertEqual(200, response.status_code)
        self.assertEqual(player.nick, response.json['result']['owner'])
        self.assertEqual(room_data['name'], response.json['result']['_id'])

    def test_06_create_a_room_with_art_category(self):
        player = Player(nick="Juan")
        player.save()
        art_category = Category(name="Art")
        art_category.save()
        room_data = {'owner': "Juan",
                     'name': "Sala 2",
                     'categories': ['Art'],
                     }
        response = self.test_client.post("/rooms/", json=room_data)
        self.assertEqual(200, response.status_code)
        self.assertEqual(player.nick, response.json['result']['owner'])
        self.assertEqual(room_data['name'], response.json['result']['_id'])
        self.assertEqual(room_data['categories'], response.json['result']['categories'])

    def test_07_create_a_room_with_biology_and_history_category(self):
        player = Player(nick="Juan")
        player.save()
        biology_category = Category(name="Biology")
        history_category = Category(name="History")
        biology_category.save()
        history_category.save()
        room_data_2 = {'owner': "Juan",
                       'name': "Sala 3",
                       'categories': ['Biology', 'History'],
                       }
        response_2 = self.test_client.post("/rooms/", json=room_data_2)
        self.assertEqual(200, response_2.status_code)
        self.assertEqual(player.nick, response_2.json['result']['owner'])
        self.assertEqual(room_data_2['name'], response_2.json['result']['_id'])
        self.assertEqual(room_data_2['categories'], response_2.json['result']['categories'])

    def test_08_create_a_room_default_amount_value(self):
        player = Player(nick="Juan")
        player.save()
        room_data_2 = {'owner': "Juan",
                       'name': "Sala 3",
                       }
        response_2 = self.test_client.post("/rooms/", json=room_data_2)
        self.assertEqual(200, response_2.status_code)
        self.assertEqual(4, response_2.json['result']['rounds_amount'])

    def test_09_create_a_room_with_1_rounds_amount_set_it_properly(self):
        player = Player(nick="Juan")
        player.save()
        room_data_2 = {'owner': "Juan",
                       'name': "Sala 3",
                       'rounds_amount': 1,
                       }
        response_2 = self.test_client.post("/rooms/", json=room_data_2)
        self.assertEqual(200, response_2.status_code)
        self.assertEqual(1, response_2.json['result']['rounds_amount'])

    def test_10_create_a_room_with_1_round_creates_a_round_object(self):
        art_category = Category(name="Art")
        art_category.save()
        data = {"text": "Las 3 carabelas eran: la pinta, la niña y ...",
                "options": [{"sentence": "Santa Martina"},
                            {"sentence": "Santa Marina"},
                            {"sentence": "Santa Maria", "correct": "True"}
                            ],
                "categories": ["Art"]}
        question = Question(**data)
        question.save()
        player = Player(nick="Juan")
        player.save()
        room_data_2 = {'owner': "Juan",
                       'name': "Sala 3",
                       'rounds_amount': 1,
                       'categories': ['Art']
                       }
        response_2 = self.test_client.post("/rooms/", json=room_data_2)
        self.assertEqual(200, response_2.status_code)
        self.assertEqual(1, response_2.json['result']['rounds_amount'])
        self.assertEqual(1, len(Room.objects.get(name=response_2.json['result']['_id'])['rounds']))


    def tearDown(self):
        disconnect('testing_db')


if __name__ == '__main__':
    unittest.main()
