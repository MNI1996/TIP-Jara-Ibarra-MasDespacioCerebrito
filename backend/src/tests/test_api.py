import unittest
from unittest.case import TestCase
from mongoengine import connect, disconnect
import app

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

    def tearDown(self):
        disconnect('testing_db')


if __name__ == '__main__':
    unittest.main()
