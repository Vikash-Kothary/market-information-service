#!/usr/bin/env python3
"""
app.py - Creates the flask web server
"""

import os

from flask import Flask


def create_app(environment=None):
    if environment is None:
        environment = os.getenv('ENVIRONMENT', 'production')
    app = Flask(__name__, static_folder='static', static_url_path='')
    config = {
        "development": "config.DevelopmentConfig",
        "testing": "config.TestingConfig",
        "production": "config.ProductionConfig",
    }
    if environment not in config:
        raise ValueError('Not a valid environment name')
    app.config.from_object(config[environment])
    # app.config.from_pyfile('config.cfg', silent=True)
    return app


app = create_app()


@app.route("/success")
def success():
    """Check if the Flask web server is working"""
    return "App is working"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
