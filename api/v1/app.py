#!/usr/bin/python3

from flask import Flask

app = Flask(__name__)

from models import storage
from api.v1.views import app_views
from os import getenv

app.register_blueprint(app_views)
host = getenv(HBNB_API_HOST) if getenv(HBNB_API_HOST) else 0.0.0.0
port = getenv(HBNB_API_PORT) if getenv(HBNB_API_PORT) else 5000

@app.teardown_appcontext
def teardown():
    storage.close()


if __name__ == '__main__':
    app.run(host=host, port=port, threaded=True)
