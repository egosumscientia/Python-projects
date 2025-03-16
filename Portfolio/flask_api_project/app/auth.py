from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from .models import db, User

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    user = User.query.filter_by(username=data.get("username")).first()

    if user and user.check_password(data.get("password")):
        token = create_access_token(identity=user.id)
        return jsonify({"token": token})

    return jsonify({"error": "Invalid credentials"}), 401
