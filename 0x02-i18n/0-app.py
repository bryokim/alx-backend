#!/usr/bin/env python3
"""0-app.py module"""

from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def hello_world():
    """Render the 0-index.html"""
    return render_template("0-index.html")


if __name__ == "__main__":
    app.run()
