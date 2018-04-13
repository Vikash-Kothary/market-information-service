#!/usr/bin/env python3
""" 
test_config.py - Tests for config.py 
"""

import unittest
from unittest.mock import patch


from app import _create_app
from config import BaseConfig, ProductionConfig, DevelopmentConfig, TestingConfig


class TestConfig(unittest.TestCase):

    def test_config_production(self):
        app = _create_app(environment='production')
        self.assertFalse(app.debug)
        self.assertFalse(app.testing)

    def test_config_testing(self):
        app = _create_app(environment='testing')
        self.assertFalse(app.debug)
        self.assertTrue(app.testing)

    def test_config_development(self):
        with patch.dict('os.environ', {'DEBUG': 'false', 'TESTING': 'false'}):
            app = _create_app(environment='development')
            self.assertFalse(app.debug)
            self.assertFalse(app.testing)

    def test_config_no_enviroment(self):
        app = _create_app()
        self.assertFalse(app.debug)
        self.assertFalse(app.testing)

    def test_config_environment_variable(self):
        with patch.dict('os.environ', {'ENVIRONMENT': 'testing'}):
            app = _create_app()
            self.assertFalse(app.debug)
            self.assertTrue(app.testing)

    def test_config_invalid_environment(self):
        with self.assertRaises(ValueError):
            app = _create_app(environment='all')


if __name__ == '__main__':
    unittest.main()
