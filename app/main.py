#!/usr/bin/env python3
"""
main.py - Run the complete application
"""

from app import app, db
from views import views
from phone import phone
from chatbot import chatbot
from listenbot import listenbot
from models import *

db.create_tables()
app.register_blueprint(views)
app.register_blueprint(phone, url_prefix='/phone')
app.register_blueprint(chatbot, url_prefix='/chat')
app.register_blueprint(listenbot, url_prefix='/listen')


def run():
    app.run(host='0.0.0.0', port=5000, debug=True)

if __name__ == '__main__':
    run()
