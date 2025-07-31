from flask import Blueprint, request, jsonify
from dto.AttractionType_DTO import AttractionTypeDTO
from services.AttractionType_services import AttractionTypeServices

AttractionType_blueprint = Blueprint('AttractionType', __name__)
service = AttractionTypeServices()


@AttractionType_blueprint.route('', methods=['POST'])
def add_AttractionType():
    dto = AttractionTypeDTO(**request.get_json())
    service.add_AttractionType(dto)
    return jsonify({'message': 'AttractionType added'}), 201


@AttractionType_blueprint.route('', methods=['GET'])
def get_AttractionType():
    AttractionType = service.get_all_AttractionType()
    return jsonify([{'AttractionTypeID': a.AttractionTypeID, 'TypeName': a.TypeName} for a in AttractionType])


@AttractionType_blueprint.route('/<int:AttractionTypeID>', methods=['GET'])
def get_AttractionType_by_id(AttractionTypeID):
    AttractionType = service.get_AttractionType_by_id(AttractionTypeID)
    return jsonify({'AttractionTypeID': AttractionType.AttractionTypeID, 'TypeName': AttractionType.TypeName})


@AttractionType_blueprint.route('/<int:AttractionTypeID>', methods=['PUT'])
def update_AttractionType(AttractionTypeID):
    dto = AttractionTypeDTO(**request.get_json())
    AttractionType = service.update_AttractionType(AttractionTypeID, dto)
    return jsonify({'message': 'AttractionType updated'})


@AttractionType_blueprint.route('/<int:AttractionTypeID>', methods=['DELETE'])
def delete_AttractionType(AttractionTypeID):
    service.delete(AttractionTypeID)
    return jsonify({'message': 'AttractionType deleted'})
