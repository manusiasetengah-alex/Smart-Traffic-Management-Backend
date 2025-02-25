from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity, JWTManager
from models import db, User
from message_template import MESSAGE as message

routes = Blueprint('auth', __name__)

jwt = JWTManager()

@routes.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()
    
    if user and user.check_password(data['password']):
        access_token = create_access_token(identity=user.id)
        return jsonify(access_token=access_token), 200
    
    return jsonify(message[401]), 401

# hapus aja jwtnya di frontend
@routes.route('/logout', methods=['DELETE'])
@jwt_required()
def logout():
    return jsonify(message[204]), 204