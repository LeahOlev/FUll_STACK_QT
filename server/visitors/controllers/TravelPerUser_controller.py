from flask import Blueprint, request, jsonify
from dto.TravelPerUser_DTO import TravelPerUserDTO
from services.TravelPerUser_services import TravelPerUserServices

TravelPerUser_blueprint = Blueprint('TravelPerUser', __name__)
service = TravelPerUserServices()

@TravelPerUser_blueprint.route('', methods=['POST'])
def add_TravelPerUser():
    dto = TravelPerUserDTO(**request.get_json())
    service.add(dto)
    return jsonify({'message': 'TravelPerUser added'}), 201


@TravelPerUser_blueprint.route('', methods=['GET'])
def get_TravelPerUser():
    TravelPerUser = service.get_all()
    return jsonify([{'TravelPerUserID': t.TravelPerUserID,'UserId':t.UserID} for t in TravelPerUser])


@TravelPerUser_blueprint.route('/<int:TravelPerUserID>', methods=['GET'])
def get_TravelPerUser_by_id(TravelPerUserID):
    TravelPerUser = service.get_by_id(TravelPerUserID)
    return jsonify({'TravelPerUserID':TravelPerUser.TravelPerUserID, 'UserID':TravelPerUser.UserID})


@TravelPerUser_blueprint.route('/<int:TravelPerUserID>', methods=['PUT'])
def update_TravelPerUser(TravelPerUserID):
    dto = TravelPerUserDTO(**request.get_json())
    TravelPerUser = service.update(TravelPerUserID, dto)
    return jsonify({'message': 'TravelPerUser updated'})


@TravelPerUser_blueprint.route('/<int:TravelPerUserID>', methods=['DELETE'])
def delete_TravelPerUser(TravelPerUserID):
    service.delete(TravelPerUserID)
    return jsonify({'message': 'TravelPerUser deleted'})
