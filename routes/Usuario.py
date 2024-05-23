from flask import Blueprint, jsonify, request
import uuid

# Entities
from models.entities.Usuario import Usuario
# Models
from models.UsuarioModel import UsuarioModel

main = Blueprint('usuario_blueprint', __name__)


@main.route('/')
def get_usuarios():
    try:
        usuarios = UsuarioModel.get_usuarios()
        return jsonify(usuarios)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/<id>')
def get_usuario(id):
    try:
        usuario = UsuarioModel.get_usuario(id)
        if usuario != None:
            return jsonify(usuario)
        else:
            return jsonify({}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/add', methods=['POST'])
def add_usuario():
    try:
        id = int(request.json['id'])
        usuario = request.json['usuario']
        contrasenna = request.json['contrasenna']
        correo = request.json['correo']
        numero = int(request.json['numero'])
        fecha_nacimiento = request.json['fecha_nacimiento']

        usuario = Usuario(id, usuario, contrasenna, correo, numero, fecha_nacimiento)

        affected_rows = UsuarioModel.add_usuario(usuario)

        if affected_rows == 1:
            return jsonify(usuario.id)
        else:
            return jsonify({'message': "Error on insert"}), 500

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/update/<id>', methods=['PUT'])
def update_usuario(id):
    try:
        usuario = request.json['usuario']
        usuario = Usuario(id, usuario)

        affected_rows = UsuarioModel.update_usuario(usuario)

        if affected_rows == 1:
            return jsonify(usuario.id)
        else:
            return jsonify({'message': "No usuario updated"}), 404

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/delete/<id>', methods=['DELETE'])
def delete_usuario(id):
    try:
        usuario = Usuario(id)

        affected_rows = UsuarioModel.delete_usuario(usuario)

        if affected_rows == 1:
            return jsonify(usuario.id)
        else:
            return jsonify({'message': "No usuario deleted"}), 404

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500