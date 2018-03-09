#!/usr/bin/env python3
"""
test_views.py - Tests for views.py
"""

from main import app

import unittest


class TestViews(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def tearDown(self):
        pass

    def test_root(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
