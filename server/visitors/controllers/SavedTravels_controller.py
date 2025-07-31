from flask import Blueprint, request, jsonify
from dto.SavedTravels_DTO import SavedTravelsDTO
from services.SavedTravels_services import SavedTravelsServices

SavedTravels_blueprint = Blueprint('SavedTravels', __name__)
service = SavedTravelsServices()

@SavedTravels_blueprint.route('', methods=['POST'])
def add_SavedTravels():
    dto = SavedTravelsDTO(**request.get_json())
    service.add(dto)
    return jsonify({'message': 'SavedTravels added'}), 201


@SavedTravels_blueprint.route('', methods=['GET'])
def get_SavedTravels():
    SavedTravels = service.get_all()
    return jsonify([{'SavedTravelsID': s.SavedTravelsID,'TraelID':s.TraelID,'AttractionId':s.AttractionId,'Timeable':s.Timeable} for s in SavedTravels])


@SavedTravels_blueprint.route('/<int:SavedTravelsID>', methods=['GET'])
def get_SavedTravels_by_id(SavedTravelsID):
    savedTravels = service.get_by_id(SavedTravelsID)
    return jsonify({'SavedTravelsID':savedTravels.SavedTravelsID, 'TraelID':savedTravels.TraelID,'AttractionId':savedTravels.AttractionId,'Timeable':savedTravels.Timeable})


@SavedTravels_blueprint.route('/<int:SavedTravelsID>', methods=['PUT'])
def update_SavedTravels(SavedTravelsID):
    dto = SavedTravelsDTO(**request.get_json())
    savedTravels = service.update(SavedTravelsID, dto)
    return jsonify({'message': 'SavedTravels updated'})


@SavedTravels_blueprint.route('/<int:SavedTravelsID>', methods=['DELETE'])
def delete_SavedTravels(SavedTravelsID):
    service.delete(SavedTravelsID)
    return jsonify({'message': 'SavedTravels deleted'})
