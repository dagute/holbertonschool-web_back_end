#!/usr/bin/env python3
"""Parametrize templates"""
from flask import Flask, jsonify, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config:
    """Config app class"""
    LANGUAGES = ["en", "fr"]


app.config.from_object(Config)
Babel.default_locale = "en"
Babel.default_timezone = "UTC"


@babel.localeselector
def get_locale():
    """get locale"""
    local_l = request.args.get("locale")
    if local_l:
        return local_l
    return request.accept_languages.best_match(Config.LANGUAGES)


@app.route("/", methods=["GET"])
def welcome():
    """Welcome Message"""
    return render_template("4-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
