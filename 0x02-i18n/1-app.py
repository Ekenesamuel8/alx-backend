#!/usr/bin/env python3
"""Basic flask setup"""


from flask import Flask, render_template
from flask_babelex import Babel
app = Flask(__name__)


class Config:
    """Config class for the app"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


babel = Babel(app)


app.config.from_object(Config)


@app.route('/')
def index():
    return "render_template('1-index.html')"


if __name__ == '__main__':
    """run the app"""
    app.run(debug=True)
