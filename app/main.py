#!/usr/bin/env python3
"""
main.py - 
"""

from app import app
from views import *

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
