from unittest import TestCase

from mongoengine import connect, disconnect

import app
from backend.src.model.Answer import Answer
from backend.src.model.Player import Player
from backend.src.model.Question import Question

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

    def test_answer_a_question_creates_a_answer_document(self):
        player = Player.objects.create(nick="tester")
        data = {"text": "Las 3 carabelas eran: la pinta, la niña y ...",
                "options": [{"sentence": "Santa Martina"},
                            {"sentence": "Santa Marina"},
                            {"sentence": "Santa Maria", "correct": "True"}
                            ]}
        question = Question(**data)
        question.save()
        question_id = question.pk
        option = question.options.filter(correct=True).first()
        data = {
            'id': str(option._id),
            'sentence': option.sentence,
            'nick': str(player.id),
        }
        response = self.test_client.post(f"question/{question_id}/", json={'data': data})
        self.assertEqual(200, response.status_code)
        answer = Answer.objects.filter(player_id=player.id).first()
        self.assertEqual(answer.question_option_id, str(option._id))

    def tearDown(self):
        disconnect('testing_db')

