#!/usr/bin/env python3
"""
main.py - Run the complete application
"""

from app import app
from views import views
from models import Product, User

app.register_blueprint(views)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
