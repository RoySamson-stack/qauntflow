from flask import request, jsonify
from flask_jwt_extended import jwt_required
from ..utils.data_processor import calculate_technical_indicators
from ..utils.visualization import generate_chart
from . import api_blueprint

@api_blueprint.route('/analysis/<symbol>', methods=['GET'])
@jwt_required()
def analyze_data(symbol):
    interval = request.args.get('interval', default='1d')
    indicators = request.args.get('indicators', default='sma,rsi,macd')
    
    try:
        # Fetch data (you might want to get this from your database)
        # data = fetch_data(symbol, interval)  # Implement this function
        
        # Calculate indicators
        indicators_list = indicators.split(',')
        processed_data = calculate_technical_indicators(data, indicators_list)
        
        # Generate chart
        chart = generate_chart(processed_data, chart_type='candlestick')
        
        return jsonify({
            'symbol': symbol,
            'interval': interval,
            'indicators': processed_data.to_dict(orient='records'),
            'chart': chart
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500