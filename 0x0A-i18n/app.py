#!/usr/bin/env python3
"""Route module for the API"""
import datetime
from flask import Flask, render_template, request, g
from flask_babel import Babel
from typing import Dict
import locale
import pytz

app = Flask(__name__)
babel = Babel(app)
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    """Config class"""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale() -> str:
    """
    This function is invoked for each request
    to select a language translation to use for that request
    """
    languages = app.config['LANGUAGES']
    locale = request.args.get("locale")
    if locale and locale in languages:
        return locale
    try:
        if g.user["locale"] in languages:
            return g.user["locale"]
    except Exception:
        pass
    return request.accept_languages.best_match(languages)


@babel.timezoneselector
def get_timezone() -> pytz.timezone:
    """Returns a URL-provided or user time zone"""
    timezone_url = request.args.get("timezone")
    try:
        if not timezone_url:
            timezone = g.user["timezone"]
        else:
            timezone = timezone_url
        return pytz.timezone(timezone)
    except (pytz.exceptions.UnknownTimeZoneError, Exception):
        print("je vais dans l'exception")
        return pytz.timezone(app.config['BABEL_DEFAULT_TIMEZONE'])


def get_user() -> Dict:
    """Returns a user dictionary or None based on the ID"""
    try:
        user_id = int(request.args.get("login_as"))
        if user_id in users.keys():
            return users[user_id]
    except Exception:
        return None


@app.before_request
def before_request():
    """Finds a user if any, and set it as a global on flask.g.user"""
    user = get_user()
    if user:
        g.user = user


@app.route("/")
def hello_world():
    """Route that renders a simple template"""
    try:
        username = g.user["name"]
    except Exception:
        username = None
    current_time = datetime.datetime.now(get_timezone())
    if get_locale() == "fr":
        locale.setlocale(locale.LC_TIME, "fr_FR.UTF-8")
        formatted_date = current_time.strftime("%d %b %Y à %H:%M:%S")
    else:
        formatted_date = current_time.strftime("%b %d, %Y, %I:%M:%S %p")
    return render_template("index.html", username=username,
                           current_time=formatted_date)


if __name__ == "__main__":
    app.run()
