#!/usr/bin/env python3
"""
1-app.py
"""

from flask import Flask, render_template
from flask_babel import Babel


class Config(object):
    """
    Sets defaults
    """
    LANGUAGES = ["en", "fr"]
    DEF_LOCALE = "en"
    DEF_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route('/')
def hello():
    """
    Basic flask app
    """
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run(debug=True)
