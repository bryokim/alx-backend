#!/usr/bin/env python3
"""4-app.py module"""

from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """Flask configuration"""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
babel = Babel()

app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """Get locale from query parameter if provided else
    return accept-language header
    """

    locale = request.args.get("locale")

    if locale and locale in Config.LANGUAGES:
        return locale

    return request.accept_languages.best_match(Config.LANGUAGES)


babel.init_app(app)


@app.route("/")
def hello_world():
    """Render the 4-index.html"""
    return render_template("4-index.html")


if __name__ == "__main__":
    app.run()
