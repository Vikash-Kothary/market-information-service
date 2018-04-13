#!/usr/bin/env python3
"""
test_app.py - Tests for app.py
"""

from flask_testing import TestCase

import app


class TestApp(TestCase):

    def create_app(self):
        return app._create_app(environment='testing')

    def setUp(self):
        self.app = self.create_app()
        with self.app.app_context():
            self.db = app._create_db(self.app)
        self.client = self.app.test_client()
        self.client.testing = True

    def tearDown(self):
        with self.app.app_context():
            self.db.session.remove()
            self.db.drop_all()

    def test_flask_set_up(self):
        """ Test flask successfully set up """
        # Endpoint not available in production
        response = self.client.get('/success')
        self.assertEqual(response.status_code, 404)
        # Endpoint works for testing purposes
        with app.app.test_client() as client:
            response = client.get('/success')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.data, b"App is working")

    def test_static_files(self):
        response = self.client.get('/robots.txt')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    import unittest
    unittest.main()
