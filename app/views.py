#!/usr/bin/venv python3
"""
views.py - Serve webpages
"""

from app import app


@app.route('/')
def root():
    return "Market Information Service"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
