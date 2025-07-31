from flask import Blueprint, request, jsonify
from dto.Visitor_DTO import VisitorDTO
from services.Visitor_services import VisitorServices

Visitor_blueprint = Blueprint('Visitor', __name__)
service = VisitorServices()


@Visitor_blueprint.route('', methods=['POST'])
def add_Visitor():
    dto = VisitorDTO(**request.get_json())
    service.add_visitor(dto)
    return jsonify({'message': 'Visitor added'}), 201


@Visitor_blueprint.route('', methods=['GET'])
def get_Visitor():
    Visitor = service.get_all()
    return jsonify([{'VisitorID': v.VisitorID, 'VisitorName': v.VisitorName} for v in Visitor])


@Visitor_blueprint.route('/<int:VisitorID>', methods=['GET'])
def get_Visitor_by_id(VisitorID):
    Visitor = service.get_by_id(VisitorID)
    return jsonify({'VisitorID': Visitor.VisitorID, 'VisitorName': Visitor.VisitorName})


@Visitor_blueprint.route('/<int:VisitorTypeID>', methods=['PUT'])
def update_Visitor(VisitorID):
    dto = VisitorDTO(**request.get_json())
    Visitor = service.update(VisitorID, dto)
    return jsonify({'message': 'Visitor updated'})


@Visitor_blueprint.route('/<int:VisitorTypeID>', methods=['DELETE'])
def delete_Visitor(VisitorID):
    service.delete(VisitorID)
    return jsonify({'message': 'Visitor deleted'})
