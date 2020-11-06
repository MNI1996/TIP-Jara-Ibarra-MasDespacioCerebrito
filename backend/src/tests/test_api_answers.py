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


class TestApiAnswersQuestions(TestCase):

    def setUp(self):
        disconnect()
        self.test_app = app.get_flask_app(test_config)
        self.test_app.testing = True
        self.test_app.debug = True
        self.test_client = self.test_app.test_client()
        connect('testing_db', is_mock=True)

    def test_answer_a_question_creates_an_answer_document(self):
        art_category = Category(name="Art")
        art_category.save()
        player = Player.objects.create(nick="tester")
        data = {"text": "Las 3 carabelas eran: la pinta, la niña y ...",
                "options": [{"sentence": "Santa Martina"},
                            {"sentence": "Santa Marina"},
                            {"sentence": "Santa Maria", "correct": "True"}
                            ],
                'categories': ['Art']}
        question = Question(**data)
        question.save()
        question_id = question.pk

        room_data_2 = {'owner': "tester",
                       'name': "a room name",
                       'rounds_amount': 1,
                       'categories': ['Art']
                       }
        response_2 = self.test_client.post("/rooms/", json=room_data_2)
        self.assertEqual(200, response_2.status_code)

        option = question.options.filter(correct=True).first()
        data = {
            'id': str(option._id),
            'sentence': option.sentence,
            'nick': str(player.id),
            'room_name': "a room name"
        }
        response = self.test_client.post(f"question/{question_id}/", json={'data': data})
        self.assertEqual(200, response.status_code)
        round_obj = Room.objects.getRoundForAQuestion("a room name", str(question_id))
        self.assertEqual(round_obj.answers.first().question_option_id, str(option._id))

    def test_answer_a_question_creates_an_answer_document_2_questions(self):
        art_category = Category(name="Art")
        art_category.save()
        player = Player.objects.create(nick="tester")
        data = {"text": "Las 3 carabelas eran: la pinta, la niña y ...",
                "options": [{"sentence": "Santa Martina"},
                            {"sentence": "Santa Marina"},
                            {"sentence": "Santa Maria", "correct": "True"}
                            ],
                'categories': ['Art']}
        question = Question(**data)
        question.save()
        question_id = question.pk

        data_2 = {"text": "Las 3 carabelas eran: la pinta, la niña y ...",
                "options": [{"sentence": "Santa Martina"},
                            {"sentence": "Santa Marina"},
                            {"sentence": "Santa Maria", "correct": "True"}
                            ],
                'categories': ['Art']}
        question_2 = Question(**data_2)
        question_2.save()
        question_2_id = question_2.pk

        room_data_2 = {'owner': "tester",
                       'name': "a room name",
                       'rounds_amount': 2,
                       'categories': ['Art']
                       }
        response_2 = self.test_client.post("/rooms/", json=room_data_2)
        self.assertEqual(200, response_2.status_code)

        option = question.options.filter(correct=True).first()
        data = {
            'id': str(option._id),
            'sentence': option.sentence,
            'nick': str(player.id),
            'room_name': "a room name"
        }
        response = self.test_client.post(f"question/{question_id}/", json={'data': data})
        self.assertEqual(200, response.status_code)
        round_obj = Room.objects.getRoundForAQuestion("a room name", str(question_id))
        self.assertEqual(round_obj.answers.first().question_option_id, str(option._id))

        option_2 = question_2.options.filter(correct=True).first()
        data_2 = {
            'id': str(option_2._id),
            'sentence': option_2.sentence,
            'nick': str(player.id),
            'room_name': "a room name"
        }
        response_2 = self.test_client.post(f"question/{question_2_id}/", json={'data': data_2})
        self.assertEqual(200, response_2.status_code)
        round_obj = Room.objects.getRoundForAQuestion("a room name", str(question_2_id))
        self.assertEqual(round_obj.answers.first().question_option_id, str(option_2._id))

    def tearDown(self):
        disconnect('testing_db')

