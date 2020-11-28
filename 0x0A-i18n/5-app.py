#!/usr/bin/env python3
"""Parametrize templates"""
from flask import Flask, jsonify, render_template, request, g
from flask_babel import Babel

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


def get_user(login_as):
    """Gets user"""
    if login_as and int(login_as) in users:
        return users.get(int(login_as))
    return None


@app.before_request
def before_request():
    """Before request"""
    user_id = request.args.get("login_as")
    if user_id:
        user = get_user(user_id)
        g.user = user
    else:
        g.user = None


@babel.localeselector
def get_locale() -> List[str]:
    """get locale"""
    local_l = request.args.get("locale")
    if local_l:
        return local_l
    return request.accept_languages.best_match(Config.LANGUAGES)


@app.route("/", methods=["GET"])
def welcome():
    """Welcome Message"""
    return render_template("5-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
