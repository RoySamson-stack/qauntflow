from flask import request, jsonify
from flask_jwt_extended import jwt_required
import pandas as pd
from ..utils.data_fetcher import fetch_stock_data, fetch_crypto_data
from . import api_blueprint

@api_blueprint.route('/data/<symbol>', methods=['GET'])
@jwt_required()
def get_data(symbol):
    interval = request.args.get('interval', default='1d')
    data_type = request.args.get('type', default='stock')  # 'stock' or 'crypto'
    
    try:
        if data_type == 'stock':
            data = fetch_stock_data(symbol, interval)
        elif data_type == 'crypto':
            data = fetch_crypto_data(symbol, interval)
        else:
            return jsonify({'error': 'Invalid data type'}), 400
        
        return jsonify(data.to_dict(orient='records')), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
    
@api_blueprint.route('/test')
def test():
    return "API is working!", 200