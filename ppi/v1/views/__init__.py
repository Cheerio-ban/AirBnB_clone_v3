#!/usr/bin/python3
"""Initialize flasks blueprint views"""
from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix="/api/v1")

from ppi.v1.views.index import *
from ppi.v1.views.states import *
from ppi.v1.views.cities import *
from ppi.v1.views.amenities import *
from ppi.v1.views.places import *
from ppi.v1.views.places_amenities import *
from ppi.v1.views.places_reviews import *
from ppi.v1.views.users import *
