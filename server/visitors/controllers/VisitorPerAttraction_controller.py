from flask import Blueprint, request, jsonify
from dto.VisitorPerAttraction_DTO import VisitorPerAttractionDTO
from services.VisitorPerAttraction_services import VisitorPerAttractionServices

VisitorPerAttraction_blueprint = Blueprint('VisitorPerAttraction', __name__)
service = VisitorPerAttractionServices()


@VisitorPerAttraction_blueprint.route('', methods=['POST'])
def add_VisitorPerAttraction():
    dto = VisitorPerAttractionDTO(**request.get_json())
    service.add(dto)
    return jsonify({'message': 'VisitorPerAttraction added'}), 201


@VisitorPerAttraction_blueprint.route('', methods=['GET'])
def get_VisitorPerAttraction():
    VisitorPerAttraction = service.get_all()
    return jsonify([{'VisitorPerAttractionID': v.VisitorPerAttractionID, 'VisitorPerAttractionName': v.VisitorPerAttractionName} for v in VisitorPerAttraction])


@VisitorPerAttraction_blueprint.route('/<int:VisitorPerAttractionID>', methods=['GET'])
def get_VisitorPerAttraction_by_id(VisitorPerAttractionID):
    VisitorPerAttraction = service.get_by_id(VisitorPerAttractionID)
    return jsonify({'VisitorPerAttractionID': VisitorPerAttraction.VisitorID, 'VisitorPerAttractionName': VisitorPerAttraction.VisitorName})


@VisitorPerAttraction_blueprint.route('/<int:VisitorPerAttractionID>', methods=['PUT'])
def update_Visitor(VisitorPerAttractionID):
    dto = VisitorPerAttractionDTO(**request.get_json())
    VisitorPerAttraction = service.update(VisitorPerAttractionID, dto)
    return jsonify({'message': 'VisitorPerAttraction updated'})


@VisitorPerAttraction_blueprint.route('/<int:VisitorPerAttractionID>', methods=['DELETE'])
def delete_VisitorPerAttraction(VisitorPerAttractionID):
    service.delete(VisitorPerAttractionID)
    return jsonify({'message': 'VisitorPerAttraction deleted'})
