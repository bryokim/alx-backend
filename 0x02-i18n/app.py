#!/usr/bin/env python3
"""app.py module"""

from flask import Flask, g, render_template, request
from flask_babel import Babel, format_datetime
import pytz


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
babel = Babel(app)

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
    """Get locale from query parameter or user if provided else
    return accept-language header
    """

    locale = request.args.get("locale")

    if locale and locale in Config.LANGUAGES:
        return locale

    if g.user and g.user["locale"] in Config.LANGUAGES:
        return g.user["locale"]

    return request.accept_languages.best_match(Config.LANGUAGES)


@babel.timezoneselector
def get_timezone():
    """Get the timezone of the current user."""

    timezone = request.args.get("timezone")

    if timezone:
        try:
            tz = pytz.timezone(timezone)
            return tz.zone
        except pytz.UnknownTimeZoneError:
            pass

    if g.user:
        try:
            tz = pytz.timezone(g.user["timezone"])
            return tz.zone
        except pytz.UnknownTimeZoneError:
            pass


@app.route("/")
def hello_world():
    """Render the index.html"""
    return render_template("index.html", current_time=format_datetime())


if __name__ == "__main__":
    app.run()
