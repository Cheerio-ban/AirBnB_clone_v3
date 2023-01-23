#!/usr/bin/python3

from flask import Flask

app = Flask(__name__)

from models import storage
from api.v1.views import app_views
from os import getenv

app.register_blueprint(app_views)

@app.teardown_appcontext
def teardown_appcontext(error):
    """Tears down context"""
    storage.close()


if __name__ == '__main__':
    app.run(host=getenv(HBNB_API_HOST, 0.0.0.0),\
    port=getenv(HBNB_API_PORT, 5000), threaded=True)
