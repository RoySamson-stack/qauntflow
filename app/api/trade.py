from flask import request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..models.trading import Trade
from ..utils.trading import execute_trade
from app import db
from . import api_blueprint

@api_blueprint.route('/trade', methods=['POST'])
@jwt_required()
def create_trade():
    data = request.get_json()
    user_id = get_jwt_identity()
    
    # Validate input
    required_fields = ['symbol', 'action', 'amount']
    if not all(field in data for field in required_fields):
        return jsonify({'error': 'Missing required fields'}), 400
    
    try:
        # Execute the trade
        trade_result = execute_trade(
            user_id=user_id,
            symbol=data['symbol'],
            action=data['action'],  # 'buy' or 'sell'
            amount=float(data['amount'])
        )
        
        # Record the trade in database
        new_trade = Trade(
            user_id=user_id,
            symbol=data['symbol'],
            action=data['action'],
            amount=data['amount'],
            price=trade_result['price'],
            status='completed'
        )
        
        db.session.add(new_trade)
        db.session.commit()
        
        return jsonify({
            'message': 'Trade executed successfully',
            'trade': trade_result
        }), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@api_blueprint.route('/trades', methods=['GET'])
@jwt_required()
def get_trades():
    user_id = get_jwt_identity()
    trades = Trade.query.filter_by(user_id=user_id).all()
    return jsonify([trade.to_dict() for trade in trades]), 200