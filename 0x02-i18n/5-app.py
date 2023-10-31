#!/usr/bin/env python3
"""5-app.py module"""

from flask import Flask, g, render_template, request
from flask_babel import Babel


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    """Flask configuration"""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
babel = Babel()

app.config.from_object(Config)


def get_user():
    """Get the user with id in the login_as parameter.
    If id is not found or login_as is not passed, then None is returned
    """
    id = int(request.args.get("login_as", 0))

    if id > 0 and id < 5:
        return users[id]

    return None


@app.before_request
def set_user():
    """Set the g.user to the value returned by get_user"""
    g.user = get_user()


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
    """Render the 5-index.html"""
    return render_template("5-index.html")


if __name__ == "__main__":
    app.run()
