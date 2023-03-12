#!/usr/bin/python3
"""setting up an api"""

from flask import Flask
from os import getenv
from models import storage
from api.v1.views import app_views

app = Flask(__name__)
app.register_blueprint(app_views)

@app.teardown_appcontext
def teardown(app):
    """A method to handle teardown app context"""
    storage.close()


if __name__ == '__main__':
    app.run(host=getenv("HBNB_API_HOST", '0.0.0.0'),
            port=getenv("HBNB_API_PORT", '5000'), threaded=True)