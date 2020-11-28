#!/usr/bin/env python3
"""Parametrize templates"""
from flask import Flask, jsonify, render_template, request, g
from flask_babel import Babel, gettext
from typing import Dict


app = Flask(__name__)
babel = Babel(app)


class Config:
    """Config app class"""
    LANGUAGES = ["en", "fr"]


app.config.from_object(Config)
Babel.default_locale = "en"
Babel.default_timezone = "UTC"

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """Gets user"""
    try:
        user_id = request.args.get('login_as')
        return users[int(user_id)]
    except Exception:
        return None


@app.before_request
def before_request():
    """Before request"""
    g.user = get_user()


@babel.localeselector
def get_locale():
    """get locale"""
    local_l = request.args.get("locale")
    s_lang = app.config['LANGUAGES']
    if local_l in s_lang:
        return local_l
    user_id = request.args.get('login_as')
    if user_id:
        local_l = users[int(user_id)]['locale']
        if local_l in s_lang:
            return local_l
    local_l = request.headers.get('locale')
    if local_l in s_lang:
        return local_l
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/", methods=["GET"])
def welcome():
    """Welcome Message"""
    return render_template("6-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
