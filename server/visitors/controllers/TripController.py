from urllib import request

import requests
from flask import Blueprint, jsonify
from app import app
from dto.Trip_DTO import TripDTO
from models.SavedTravels import SavedTravels
from services import TripAlgo
from services.SavedTravels_services import SavedTravelsServices

# engine = create_engine('sqlite:///SavedTravels.db')
# Base.metadata.create_all(engine)
# Session = sessionmaker(bind=engine)
# session = Session()
repo = SavedTravels()##repo
service = SavedTravelsServices(repo)

SavedTravels_blueprint = Blueprint('SavedTravels', __name__)

@app.route('/api/plan-trip', methods=['POST'])
def plan_trip():
    # trip_data = request.json
    trip = TripDTO(**request.get_json())
    result = TripAlgo.plan_trip(trip)
    return jsonify(result)
