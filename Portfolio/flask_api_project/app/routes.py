from flask import Blueprint, request, jsonify
from .models import db, User
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

api_bp = Blueprint('api', __name__)

@api_bp.route('/users', methods=['GET'])
@jwt_required()
def get_users():
    users = User.query.all()
    return jsonify([{"id": u.id, "username": u.username, "email": u.email} for u in users])

@api_bp.route('/users/<int:id>', methods=['GET'])
@jwt_required()
def get_user(id):
    user = User.query.get(id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify({"id": user.id, "username": user.username, "email": user.email})

@api_bp.route('/users', methods=['POST'])
def create_user():
    data = request.json
    if not data.get("username") or not data.get("password") or not data.get("email"):
        return jsonify({"error": "Missing fields"}), 400

    user = User(username=data["username"], email=data["email"])
    user.set_password(data["password"])
    db.session.add(user)
    db.session.commit()
    return jsonify({"message": "User created"}), 201

@api_bp.route('/users/<int:id>', methods=['PUT'])
@jwt_required()
def update_user(id):
    data = request.json
    user = User.query.get(id)
    if not user:
        return jsonify({"error": "User not found"}), 404

    if "username" in data:
        user.username = data["username"]
    if "email" in data:
        user.email = data["email"]
    if "password" in data:
        user.set_password(data["password"])

    db.session.commit()
    return jsonify({"message": "User updated"}), 200

@api_bp.route('/users/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_user(id):
    user = User.query.get(id)
    if not user:
        return jsonify({"error": "User not found"}), 404

    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": "User deleted"}), 200
