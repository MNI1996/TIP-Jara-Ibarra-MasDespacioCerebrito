import unittest
from unittest.case import TestCase

import app

test_config = {
    'MONGODB_SETTINGS':
    {
        'db': 'testing_db',
        'host': 'localhost',
        'port': 27017,
        'username': 'admin',
        'password': 'password',
        'authentication_source': 'admin'
    }
}


class TestApiQuestions(TestCase):

    def test_connection_on_questions_get_and_empty_result(self):
        test_app = app.get_flask_app(test_config)
        test_app.testing = True
        test_app.debug = True
        test_client = test_app.test_client()
        response = test_client.get("/questions/")
        self.assertEqual(200, response.status_code)
        self.assertEqual([], response.json["result"])


if __name__ == '__main__':
    unittest.main()
