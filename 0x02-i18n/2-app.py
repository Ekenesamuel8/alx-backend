#!/usr/bin/env python3
"""Basic flask setup"""


from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """config some setting for the app"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_LOCALE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
# Initialize Babel
babel = Babel(app)


# Define the get_locale function with babel.localeselector decorator
@babel.localeselector
def get_locale():
    """get locale"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """render a basic html template"""
    return render_template('2-index.html')


if __name__ == '__main__':
    """run the app"""
    app.run(debug=True)
