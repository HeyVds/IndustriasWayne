from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from .models import db, Recurso

recursos_bp = Blueprint('recursos', __name__)

@recursos_bp.route('/api/recursos', methods=['GET'])
@jwt_required()
def listar_recursos():
    recursos = Recurso.query.all()
    return jsonify([{
        'id': r.id,
        'nome': r.nome,
        'tipo': r.tipo,
        'status': r.status
    } for r in recursos])

@recursos_bp.route('/api/recursos', methods=['POST'])
@jwt_required()
def adicionar_recurso():
    data = request.get_json()
    recurso = Recurso(
        nome=data['nome'],
        tipo=data['tipo'],
        status=data.get('status', 'ativo')
    )
    db.session.add(recurso)
    db.session.commit()
    return jsonify({'msg': 'Recurso adicionado com sucesso'}), 201

@recursos_bp.route('/api/recursos/<int:recurso_id>', methods=['PUT'])
@jwt_required()
def atualizar_recurso(recurso_id):
    recurso = Recurso.query.get(recurso_id)
    if not recurso:
        return jsonify({'msg': 'Recurso não encontrado'}), 404

    data = request.get_json()
    recurso.nome = data.get('nome', recurso.nome)
    recurso.tipo = data.get('tipo', recurso.tipo)
    recurso.status = data.get('status', recurso.status)

    db.session.commit()
    return jsonify({'msg': 'Recurso atualizado com sucesso'})

@recursos_bp.route('/api/recursos/<int:recurso_id>', methods=['DELETE'])
@jwt_required()
def deletar_recurso(recurso_id):
    recurso = Recurso.query.get(recurso_id)
    if not recurso:
        return jsonify({'msg': 'Recurso não encontrado'}), 404

    db.session.delete(recurso)
    db.session.commit()
    return jsonify({'msg': 'Recurso deletado com sucesso'})
