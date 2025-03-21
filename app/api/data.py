from flask import request, jsonify
from app.utils.data_fetcher import fetch_data
from . import api_blueprint  

@api_blueprint.route('/data/<symbol>', methods=['GET'])
def get_data(symbol):
    interval = request.args.get('interval', default='1d')
    data = fetch_data(symbol, interval)
    return jsonify(data), 200