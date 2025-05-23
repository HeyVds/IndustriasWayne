from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from .models import db, User

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/api/register', methods=['POST'])
def register():
    data = request.get_json()
    if User.query.filter_by(email=data['email']).first():
        return jsonify({'msg': 'Usuário já existe'}), 400
    user = User(name=data['name'], email=data['email'], password=data['password'], role=data.get('role', 'funcionario'))
    db.session.add(user)
    db.session.commit()
    return jsonify({'msg': 'Usuário registrado com sucesso'})


@auth_bp.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    if not data or 'email' not in data or 'password' not in data:
        return jsonify({'msg': 'Dados incompletos'}), 400

    user = User.query.filter_by(email=data['email']).first()

    if not user or user.password != data['password']:
        return jsonify({'msg': 'Credenciais inválidas'}), 401

    additional_claims = {
        'role': user.role,
        'name': user.name
    }
    token = create_access_token(identity=str(user.id), additional_claims=additional_claims)


    return jsonify({'token': token})
