#!/usr/bin/python3
"""Connecting to the api using flask functions"""

from api.v1.views import app_views
from flask import jsonify

cities = {
    "amenities": Amenity,
    "cities": City,
    "places": Place,
    "reviews": Review,
    "states": State,
    "users": User
}

@app_views.route('/status', strict_slashes=False)
def status():
    """hbnb status"""
    return jsonify({"status": "OK"})

@app_views.route('/stats', strict_slashes=False)
def stats():
    objects_stats = {}
    for key, value in cities.items():
        objects_stats[key] = len(storage.all(value))
    return jsonify(objects_stats)

if __name__ == "__main__":
    pass
