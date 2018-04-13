#!/usr/bin/env python3
"""
test_views.py - Tests for views.py
"""

from app import _create_app
from views import views

from flask_testing import TestCase


class TestChatbot(TestCase):

    def create_app(self):
        app = _create_app(environment='testing')
        app.register_blueprint(views)
        return app

    def setUp(self):
        app = self.create_app()
        self.client = app.test_client()
        self.client.testing = True

    def tearDown(self):
        pass

    def test_root(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    import unittest
    unittest.main()
