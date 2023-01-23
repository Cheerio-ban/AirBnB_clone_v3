#!/usr/bin/python3
"""Connecting to the api using flask functions"""

from api.v1.views import app_views


@app_views.route('/status', strict_slashes=False)
def status():
    """hbnb status"""
    return (jsonify({"status": "OK"}))


if __name__ == "__main__":
    pass
