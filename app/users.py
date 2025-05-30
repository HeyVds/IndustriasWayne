from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt
from .models import db, User

usuarios_bp = Blueprint('usuarios', __name__)

def verificar_admin():
    claims = get_jwt()
    return claims.get('role') == 'admin'

@usuarios_bp.route('/api/usuarios', methods=['GET'])
@jwt_required()
def listar_usuarios():
    if not verificar_admin():
        return jsonify({'msg': 'Acesso negado'}), 403

    usuarios = User.query.all()
    return jsonify([{
        'id': u.id,
        'name': u.name,
        'email': u.email,
        'role': u.role
    } for u in usuarios])

@usuarios_bp.route('/api/usuarios', methods=['POST'])
@jwt_required()
def adicionar_usuario():
    if not verificar_admin():
        return jsonify({'msg': 'Acesso negado'}), 403

    data = request.get_json()
    if User.query.filter_by(email=data['email']).first():
        return jsonify({'msg': 'Usuário já existe'}), 400

    usuario = User(
        name=data['name'],
        email=data['email'],
        password=data['password'],
        role=data.get('role', 'funcionario')
    )
    db.session.add(usuario)
    db.session.commit()
    return jsonify({'msg': 'Usuário adicionado com sucesso'}), 201

@usuarios_bp.route('/api/usuarios/<int:usuario_id>', methods=['PUT'])
@jwt_required()
def atualizar_usuario(usuario_id):
    if not verificar_admin():
        return jsonify({'msg': 'Acesso negado'}), 403

    usuario = User.query.get(usuario_id)
    if not usuario:
        return jsonify({'msg': 'Usuário não encontrado'}), 404

    data = request.get_json()
    usuario.name = data.get('name', usuario.name)
    usuario.email = data.get('email', usuario.email)
    usuario.password = data.get('password', usuario.password)
    usuario.role = data.get('role', usuario.role)

    db.session.commit()
    return jsonify({'msg': 'Usuário atualizado com sucesso'})

@usuarios_bp.route('/api/usuarios/<int:usuario_id>', methods=['DELETE'])
@jwt_required()
def deletar_usuario(usuario_id):
    if not verificar_admin():
        return jsonify({'msg': 'Acesso negado'}), 403

    usuario = User.query.get(usuario_id)
    if not usuario:
        return jsonify({'msg': 'Usuário não encontrado'}), 404

    db.session.delete(usuario)
    db.session.commit()
    return jsonify({'msg': 'Usuário deletado com sucesso'})
