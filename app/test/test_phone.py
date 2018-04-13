#!/usr/bin/env python3
"""
test_phone.py - Tests for phone.py
"""

from flask_testing import TestCase

from app import _create_app
from phone import phone
from chatbot import chatbot


class TestPhone(TestCase):

    def create_app(self):
        app = _create_app(environment='testing')
        app.register_blueprint(phone)
        app.register_blueprint(chatbot)
        return app

    def setUp(self):
        app = self.create_app()
        self.client = app.test_client()
        self.client.testing = True

    def tearDown(self):
        pass

    def test_new_user(self):
        """ """
        expected = b'<Response><Redirect method="GET">/greeting</Redirect></Response>'
        response = self.client.get('/voice')
        self.assertEqual(response.status_code, 200)
        # print(response.data)
        #self.assertEqual(expected, response.data)


if __name__ == '__main__':
    import unittest
    unittest.main()
