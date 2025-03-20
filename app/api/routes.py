from flask import Blueprint

routes_blueprint = Blueprint('routes', __name__)
from .core import api


@routes_blueprint.route('/')
def example():
    from . import api  # Import here to avoid circular import
    return "Example route"

