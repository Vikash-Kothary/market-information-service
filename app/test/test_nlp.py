#!/usr/bin/env python3
"""
test_app.py - Tests for nlp.py
"""

from nlp import NLP

import unittest


class TestApp(unittest.TestCase):

    def setUp(self):
        self.speech_to_query = NLP()

    def tearDown(self):
        pass

if __name__ == '__main__':
    pass
