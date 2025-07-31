from flask import Blueprint, request, jsonify
from dto.User_DTO import UserDTO
from services.User_services import UserService

User_blueprint = Blueprint('Users', __name__)
service = UserService()

@User_blueprint.route('', methods=['POST'])
def add_user():
    dto = UserDTO(**request.get_json())
    service.add_user(dto)
    return jsonify({'message': 'User added'}), 201

@User_blueprint.route('', methods=['GET'])
def get_all_users():
    users = service.get_all_users()
    return jsonify([user.to_dict() for user in users])

@User_blueprint.route('/<int:user_id>', methods=['GET'])
def get_user_by_id(user_id):
    user = service.get_user_by_id(user_id)
    return jsonify(user.to_dict())

@User_blueprint.route('/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    dto = UserDTO(**request.get_json())
    service.update_user(user_id, dto)
    return jsonify({'message': 'User updated'})

@User_blueprint.route('/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    service.delete_user(user_id)
    return jsonify({'message': 'User deleted'})
