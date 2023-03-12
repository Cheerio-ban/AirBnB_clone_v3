#!/usr/bin/python3
"""index"""

from api.v1.views import app_views
from models.amenity import Amenity
from models.review import Review
from models.city import City
from models.place import Place
from models.state import State
from models.user import User
from flask import jsonify

@app_views.route('/status', strict_slashes=False)
def status():
    status = {"status": 'ok'}
    return jsonify(status)

@app_views.route('/stats', strict_slashes=False)
def stats():
    """get the stats of the database"""
    from models import storage
    classes = [Amenity, City, Place, Review, State, User]
    dict = {'amenities': 0, 'cities': 0, 'places': 0, 'reviews': 0, 'states': 0, 'users': 0}
    i = 0
    for cls in classes:
        dict[list(dict.keys())[i]] = storage.count(cls)
        i += 1
    return jsonify(dict)

