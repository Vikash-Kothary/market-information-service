#/usr/bin/python3
"""  
config.py - Configuration for Flask application  
"""

import os


basedir = os.path.abspath(os.path.dirname(__file__))
config_env = {
    "development": "config.DevelopmentConfig",
    "testing": "config.TestingConfig",
    "production": "config.ProductionConfig",
}


class BaseConfig(object):
    """Default configuration"""
    DEBUG = False
    TESTING = False
    ACCOUNT_SID = ''
    AUTH_TOKEN = ''
    SECRET_KEY = __name__
    SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(basedir, 'default.sqlite'))
    PHONE_NUMBER = '+441929509853'
    CELERY_BROKER_URL = 'redis://localhost:6379',
    CELERY_RESULT_BACKEND = 'redis://localhost:6379'


class ProductionConfig(BaseConfig):
    """Configuration for a production environemnt"""
    ACCOUNT_SID = 'AC1a690fafa38430df4f4116952f705359'
    AUTH_TOKEN = '6a2bf933d3cb4d6c94f93cf9e2363d23'


class DevelopmentConfig(BaseConfig):
    """Configuration for a development environemnt. All settings can be changed."""
    if 'DEBUG' in os.environ:
        DEBUG = os.getenv('DEBUG', 'true').lower() == 'true'
    if 'TESTING' in os.environ:
        TESTING = os.getenv('TESTING', 'false').lower() == 'true'
    if 'ACCOUNT_SID' in os.environ:
        ACCOUNT_SID = os.getenv('ACCOUNT_SID', TestingConfig.ACCOUNT_SID)
    if 'AUTH_TOKEN' in os.environ:
        AUTH_TOKEN = os.getenv('AUTH_TOKEN', TestingConfig.AUTH_TOKEN)
    if 'SECRET_KEY' in os.environ:
        SECRET_KEY = os.getenv('SECRET_KEY', __name__)
    if 'SQLALCHEMY_DATABASE_URI' in os.environ:
        SQLALCHEMY_DATABASE_URI = os.getenv(
            'SQLALCHEMY_DATABASE_URI', 'sqlite:///{}'.format(os.path.join(basedir, 'dev.sqlite')))


class TestingConfig(BaseConfig):
    """Configuration when running tests"""
    DEBUG = False
    TESTING = True
    # Test Credentials
    ACCOUNT_SID = 'ACdab50f233a93d277f7518b830148d5cb'
    AUTH_TOKEN = 'caacae6e1da3561db5152c870c4b6f63'
