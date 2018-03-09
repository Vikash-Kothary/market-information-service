#!/usr/bin/env python3
"""
views.py - Serve webpages
"""

from flask import Blueprint, render_template

views = Blueprint("views", __name__)


@views.route("/")
def root():
    """Root for website"""
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
