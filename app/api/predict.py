from flask import request, jsonify
from flask_jwt_extended import jwt_required
from ..models.lstm_model import load_model, make_prediction
from . import api_blueprint

@api_blueprint.route('/predict/<symbol>', methods=['GET'])
@jwt_required()
def predict(symbol):
    interval = request.args.get('interval', default='1h')
    prediction_days = int(request.args.get('days', default=7))
    
    try:
        # Load trained model
        model = load_model(symbol)
        
        if not model:
            return jsonify({'error': f'No trained model for {symbol}'}), 404
        
        # Get historical data
        data = fetch_data(symbol, interval)  # Implement this function
        
        # Make prediction
        prediction = make_prediction(model, data, prediction_days)
        
        return jsonify({
            'symbol': symbol,
            'prediction': prediction,
            'timeframe': f'next {prediction_days} days'
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500