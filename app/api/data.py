from flask import request, jsonify
from . import api_blueprint 

@api_blueprint.route('/data/', methods=['GET'])
# def get_data(symbol):
def get_data():
    return " We are testing the apis endpoints for the project"
    # interval = request.args.get('interval', default='1d')
    # return jsonify({"symbol": symbol, "interval": interval}), 200

@api_blueprint.route('/test')
def test():
    return "API is working!", 200