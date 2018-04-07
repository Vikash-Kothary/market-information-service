#!/usr/bin/env python3
"""
test_app.py - Tests for nlp.py
"""

from app import create_app as _create_app
from chatbot import chatbot

from flask_testing import TestCase


class TestChatbot(TestCase):

    def create_app(self):
        app = _create_app(environment='testing')
        app.register_blueprint(chatbot)
        return app

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_greeting(self):
        pass

    def test_on_board(self):
        pass


if __name__ == '__main__':
    pass
