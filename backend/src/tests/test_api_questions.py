from unittest import TestCase

from mongoengine import connect, disconnect

import app
from backend.src.model.Category import Category

test_config = {
    'MONGODB_SETTINGS': {'alias': 'testing_db'}
}


class TestApiQuestions(TestCase):

    def setUp(self):
        disconnect()
        self.test_app = app.get_flask_app(test_config)
        self.test_app.testing = True
        self.test_app.debug = True
        self.test_client = self.test_app.test_client()
        connect('testing_db', is_mock=True)

    def test_01_connection_on_questions_get_and_empty_result(self):
        response = self.test_client.get("/questions/")
        self.assertEqual(200, response.status_code)
        self.assertEqual([], response.json["result"])

    def test_02_create_a_question(self):
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

    def test_03_create_a_question_with_no_text(self):
        data = {"options": [{"sentence": "Santa Martina"},
                            {"sentence": "Santa Marina"},
                            {"sentence": "Santa Maria", "correct": "True"}
                            ]}
        response = self.test_client.post("/questions/", json=data)
        self.assertEqual(400, response.status_code)
        self.assertEqual("ValidationError (Question:None) (Field is required: ['text'])", response.json['message'])

    def test_04_create_a_question_with_category(self):
        biology_category = Category(name="Biology")
        biology_category.save()

        data = {"text": "Las 3 carabelas eran: la pinta, la niña y ...",
                "options": [{"sentence": "Santa Martina"},
                            {"sentence": "Santa Marina"},
                            {"sentence": "Santa Maria", "correct": "True"}
                            ],
                "categories": ['Biology']}
        response = self.test_client.post("/questions/", json=data)
        self.assertEqual(200, response.status_code)
        self.assertEqual(data["categories"], response.json['result']['categories'])

    def test_05_create_a_question_with_difficulty(self):
        biology_category = Category(name="Biology")
        biology_category.save()

        data = {"text": "Las 3 carabelas eran: la pinta, la niña y ...",
                "options": [{"sentence": "Santa Martina"},
                            {"sentence": "Santa Marina"},
                            {"sentence": "Santa Maria", "correct": "True"}
                            ],
                "categories": ['Biology'],
                "difficulty": 3}
        response = self.test_client.post("/questions/", json=data)
        self.assertEqual(200, response.status_code)
        self.assertEqual(data["difficulty"], response.json['result']['difficulty'])

    def test_06_create_a_question_difficulty_default_value(self):
        biology_category = Category(name="Biology")
        biology_category.save()

        data = {"text": "Las 3 carabelas eran: la pinta, la niña y ...",
                "options": [{"sentence": "Santa Martina"},
                            {"sentence": "Santa Marina"},
                            {"sentence": "Santa Maria", "correct": "True"}
                            ],
                "categories": ['Biology'],
                }
        response = self.test_client.post("/questions/", json=data)
        self.assertEqual(200, response.status_code)
        self.assertEqual(1, response.json['result']['difficulty'])

    def test_07_create_a_question_categories_default_value(self):
        data = {"text": "Las 3 carabelas eran: la pinta, la niña y ...",
                "options": [{"sentence": "Santa Martina"},
                            {"sentence": "Santa Marina"},
                            {"sentence": "Santa Maria", "correct": "True"}
                            ],
                }
        response = self.test_client.post("/questions/", json=data)
        self.assertEqual(200, response.status_code)
        self.assertEqual([], response.json['result']['categories'])

    def tearDown(self):
        disconnect('testing_db')
