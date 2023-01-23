#!/usr/bin/python3
"""Connecting to the api using flask functions"""
from api.v1.views import app_views

@app_views.route('/status')
def status():
    """hbnb status"""
    return (jsonify({"status": "OK"}))
