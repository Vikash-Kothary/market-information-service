#!/usr/bin/env python3
"""
main.py - Run the complete application
"""

from app import create_app
from views import views
from chatbot import chatbot
from models import Product, User

app = create_app()
app.register_blueprint(views)
app.register_blueprint(chatbot)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
