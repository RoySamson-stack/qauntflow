from flask import request, jsonify
from app.utils.data_processor import calculate_indicators
from app.utils.visualization import generate_candlestick
from . import api_blueprint 

@api_blueprint.route('/analysis/<symbol>', methods=['GET'])
def analyze_data(symbol):
    interval = request.args.get('interval', default='1d')
    data = fetch_data(symbol, interval)
    indicators = calculate_indicators(data)
    chart = generate_candlestick(data)
    return jsonify({'indicators': indicators, 'chart': chart}), 200