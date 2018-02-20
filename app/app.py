#!/usr/bin/env python3
"""
app.py - Creates the flask web server
"""
from flask import Flask

app = Flask(__name__, static_folder='static', static_url_path='')
app.debug = True


@app.route("/success")
def success():
    """Check if the Flask web server is working"""
    return "App is working"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
