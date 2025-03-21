from flask import request, jsonify
from flask_jwt_extended import create_access_token
from . import api_blueprint  # Import the blueprint

@api_blueprint.route('/auth/register', methods=['POST'])
def register():
    data = request.get_json()
    return jsonify({'message': 'User registered successfully'}), 201

@api_blueprint.route('/auth/login', methods=['POST'])
def login():
    data = request.get_json()
    access_token = create_access_token(identity=data['username'])
    return jsonify({'access_token': access_token}), 200