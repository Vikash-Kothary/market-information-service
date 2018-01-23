#!/usr/bin/env python3
"""
app.py - 
"""
from flask import Flask

app = Flask(__name__)
app.debug = True


@app.route("/success")
def success():
    return "App is working"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
