from flask import Blueprint, request, jsonify
from dto.Region_DTO import RegionDTO
from services.Region_services import RegionServices
from repository.RegionRepository import RegionRepository





Region_blueprint = Blueprint('Region', __name__)
service = RegionServices()


@Region_blueprint.route('', methods=['POST'])
def add_Region():
    dto = RegionDTO(**request.get_json())
    service.add_region(dto)
    return jsonify({'message': 'Region added'}), 201


@Region_blueprint.route('', methods=['GET'])
def get_Region():
    Region = service.get_all()
    return jsonify([{'RegionID': r.RegionID, 'RegionName': r.RegionName} for r in Region])


@Region_blueprint.route('/<int:RegionID>', methods=['GET'])
def get_Region_by_id(RegionID):
    Region = service.get_by_id(RegionID)
    return jsonify({'RegionID': Region.RegionID, 'RegionName': Region.RegionName})


@Region_blueprint.route('/<int:RegionID>', methods=['PUT'])
def update_Region(RegionID):
    dto = RegionDTO(**request.get_json())
    Region = service.update(RegionID, dto)
    return jsonify({'message': 'Region updated'})


@Region_blueprint.route('/<int:RegionID>', methods=['DELETE'])
def delete_Region(RegionID):
    service.delete(RegionID)
    return jsonify({'message': 'Region deleted'})
