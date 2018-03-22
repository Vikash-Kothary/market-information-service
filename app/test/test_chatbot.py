#!/usr/bin/env python3
"""
test_app.py - Tests for nlp.py
"""

from chatbot import Chatbot

import unittest


class TestChatbot(unittest.TestCase):

    def setUp(self):
        self.chatbot = Chatbot()

    def tearDown(self):
        pass


if __name__ == '__main__':
    pass
