from flask import Blueprint, request, jsonify
from dto.Attractions_DTO import AttractionsDTO
from services.Attractions_Services import AttractionsServices

Attractions_blueprint = Blueprint('Attractions', __name__)
service = AttractionsServices()


@Attractions_blueprint.route('', methods=['POST'])
def add_Attractions():
    dto = AttractionsDTO(**request.get_json())
    service.add_attraction(dto)
    return jsonify({'message': 'Attractions added'}), 201

@Attractions_blueprint.route('', methods=['GET'])
def get_Attractions():
    Attractions = service.get_all()
    return jsonify([
        {
            'AttractionsID': a.AttractionID,
            'Lat': a.Lat,
            'Lng': a.Lng,
            'RegionId': a.RegionId,
            'AttractionName': a.AttractionName,
            'openingHours': a.openingHours,
            'closeHoures': a.closingHours,
            'DurationMax': a.DurationMax,
            'Price': a.Price,
            'DescriptionLink': a.DescriptionLink,
            'AttractionTypeID': a.AttractionTypeID
        }
        for a in Attractions
    ])

@Attractions_blueprint.route('/<int:AttractionID>', methods=['GET'])
def get_Attractions_by_id(AttractionID):
    a = service.get_by_id(AttractionID)
    return jsonify({
        'AttractionsID': a.AttractionID,
        'Lat': a.Lat,
        'Lng': a.Lng,
        'RegionId': a.RegionId,
        'AttractionName': a.AttractionName,
        'openingHours': a.openingHours,
        'closeHoures': a.closingHours,
        'DurationMax': a.DurationMax,
        'Price': a.Price,
        'DescriptionLink': a.DescriptionLink,
        'AttractionTypeID': a.AttractionTypeID
    })


@Attractions_blueprint.route('/<int:AttractionsID>', methods=['PUT'])
def update_Attractions(AttractionID):
    dto = AttractionsDTO(**request.get_json())
    Attractions = service.update(AttractionID, dto)
    return jsonify({'message': 'Attractions updated'})


@Attractions_blueprint.route('/<int:AttractionsID>', methods=['DELETE'])
def delete_Attractions(AttractionID):
    service.delete(AttractionID)
    return jsonify({'message': 'Attractions deleted'})
