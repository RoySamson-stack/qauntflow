from flask import Blueprint, jsonify, request
from app.utils.data.fetcher import fetch_data


data_blueprint = Blueprint('data', __name__)

@data_blueprint.route('/data/<symbol>', methods=['GET'])
def get_data(symbol):
    data = fetch_data(symbol)
    return jsonify(data)