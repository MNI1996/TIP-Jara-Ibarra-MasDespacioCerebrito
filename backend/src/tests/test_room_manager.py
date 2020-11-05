from unittest import TestCase

from mongoengine import connect, disconnect

import app
from backend.src.model.Category import Category
from backend.src.model.Player import Player
from backend.src.model.Question import Question
from backend.src.model.Room import Room

test_config = {
    'MONGODB_SETTINGS': {'alias': 'testing_db'}
}


class TestRoomManager(TestCase):

    def setUp(self):
        self.test_app = app.get_flask_app(test_config)
        self.test_app.testing = True
        self.test_app.debug = True
        self.test_client = self.test_app.test_client()
        connect('testing_db', is_mock=True)

    def test_get_rounds_with_a_room_name(self):
        a_player = Player(nick="a player")
        a_player.save()
        a_room = Room(name="a room name", owner=a_player, rounds_amount=1)
        a_room.save()
        self.assertEqual(a_room.rounds, Room.objects.getRoundsFor("a room name"))

    def test_get_points_for_a_player_no_answers(self):
        a_player = Player(nick="a player")
        a_player.save()
        a_room = Room(name="a room name", owner=a_player, rounds_amount=1)
        a_room.save()
        self.assertEqual(0, Room.objects.getPointsFor("a room name", "a player"))

    def test_get_round_for_a_question_id(self):
        a_player = Player(nick="a player")
        a_player.save()
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

        room_data_2 = {'owner': "a player",
                       'name': "a room name",
                       'rounds_amount': 1,
                       'categories': ['Art']
                       }
        response_2 = self.test_client.post("/rooms/", json=room_data_2)
        self.assertEqual(200, response_2.status_code)
        question_id = question.pk

        self.assertEqual(question, Room.objects.getRoundForAQuestion("a room name", str(question_id)).question)

    def test_get_points_for_a_player_with_1_correct_answer(self):
        a_player = Player(nick="a player")
        a_player.save()
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

        room_data_2 = {'owner': "a player",
                       'name': "a room name",
                       'rounds_amount': 1,
                       'categories': ['Art']
                       }
        response_2 = self.test_client.post("/rooms/", json=room_data_2)
        self.assertEqual(200, response_2.status_code)

        question_id = question.pk
        option = question.options.filter(correct=True).first()
        data = {
            'id': str(option._id),
            'sentence': option.sentence,
            'nick': str(a_player.id),
            'room_name': "a room name",
        }
        response = self.test_client.post(f"question/{question_id}/", json={'data': data})
        self.assertEqual(200, response.status_code)
        self.assertEqual(1, Room.objects.getPointsFor("a room name", "a player"))

    def tearDown(self):
        disconnect()
