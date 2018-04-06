#/usr/bin/python3
"""  
config.py - Configuration for Flask application  
"""
import os


class BaseConfig(object):
    """Default configuration"""
    DEBUG = False
    TESTING = False
    ACCOUNT_SID = ''
    AUTH_TOKEN = ''


class ProductionConfig(BaseConfig):
    """Configuration for a production environemnt"""
    ACCOUNT_SID = ''
    AUTH_TOKEN = ''


class DevelopmentConfig(BaseConfig):
    """Configuration for a development environemnt. All settings can be changed."""
    if 'DEBUG' in os.environ:
        DEBUG = os.getenv('DEBUG', 'true').lower() == 'true'
    if 'TESTING' in os.environ:
        TESTING = os.getenv('TESTING', 'false').lower() == 'true'
    if 'ACCOUNT_SID' in os.environ:
        ACCOUNT_SID = os.getenv('ACCOUNT_SID', '')
    if 'AUTH_TOKEN' in os.environ:
        AUTH_TOKEN = os.getenv('AUTH_TOKEN', '')


class TestingConfig(BaseConfig):
    """Configuration when running tests"""
    DEBUG = True
    TESTING = True
    # Test Creden
    ACCOUNT_SID = ''
    AUTH_TOKEN = ''
