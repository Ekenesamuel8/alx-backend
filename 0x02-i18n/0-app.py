#!/usr/bin/env python3
"""Basic flask setup"""


from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def hello_world():
    """create a route for the app in the web browser"""
    return render_template('0-index.html')


if __name__ == '__main__':
    """run the app"""
    app.run()
