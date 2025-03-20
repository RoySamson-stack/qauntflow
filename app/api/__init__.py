from flask import Blueprint, jsonify, request
from .core import api

api_blueprint = Blueprint('api', __name__)

from . import routes