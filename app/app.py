#!/usr/bin/env python3
"""
app.py - Creates the flask web server
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import os

from config import config_env


def _create_app(environment=None):
    """ """
    if environment is None:
        environment = os.getenv('ENVIRONMENT', 'production')
    app = Flask(__name__, static_folder='static', static_url_path='')
    if environment not in config_env:
        raise ValueError('Not a valid environment name')
    app.config.from_object(config_env[environment])
    # app.config.from_pyfile('config.cfg', silent=True)
    return app


def _create_db(app):
    def _init_db():
        with app.app_context():
            db.drop_all()
            db.create_all()

    def _save_util(user=None):
        if user:
            db.session.add(user)
        db.session.commit()

    def _clear_data():
        session = db.session
        meta = db.metadata
        for table in reversed(meta.sorted_tables):
            session.execute(table.delete())
        session.commit()
    db = SQLAlchemy()
    db.init_app(app)
    db.create_tables = _init_db
    db.save = _save_util
    db.clear_all = _clear_data
    return db


app = _create_app()
db = _create_db(app)


@app.route("/success")
def success():
    """Check if the Flask web server is working"""
    return "App is working"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
