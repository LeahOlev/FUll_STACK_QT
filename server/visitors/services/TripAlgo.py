import itertools
from collections import defaultdict
from dto import Location_DTO
from dto.Location_DTO import LocationDTO

from services.googleMaps import get_drive_time_minutes


# דירוג כללי
def score(attraction, origin):
    return (
            0.5 * attraction.Price +
            0.3 * get_drive_time_minutes(origin, attraction) -
            0.2 * (attraction.closingHours - attraction.openingHours)
    )


# אלגוריתם ראשי
def select_attractions(trip, all_attractions, visitor_matchings):
    origin = trip.pointDeparture

    # קהל יעד
    allowed_ids = {
        x.AttractionId for x in visitor_matchings
        if x.VisitorPerAttraction == trip.typeVisitor
    }

    # סינון ראשוני
    filtered = [
        a for a in all_attractions
        if a.RegionId == trip.area
           and a.AttractionID in allowed_ids
           and a.openingHours <= trip.startHour
           and a.closingHours >= trip.endHour
           and a.Price * trip.countPepole <= trip.budget
    ]

    # קיבוץ לפי סוג
    grouped = defaultdict(list)
    for a in filtered:
        grouped[a.AttractionTypeID].append(a)

    # בחירה של N מכל סוג
    selected = []
    for type_id, count in trip.attraction.items():
        group = grouped.get(type_id, [])
        if len(group) < count:
            continue  # לא מספיק מהסוג הזה

        ranked = sorted(group, key=lambda a: score(a, origin))
        selected.extend(ranked[:count])

    return selected


def is_valid_route(route, trip, api_key):
    time = trip.startHour
    location = trip.pointDeparture

    for attraction in route:
        drive_time = get_drive_time_minutes(location, attraction)
        time += drive_time

        if time < attraction.openingHours:
            time = attraction.openingHours
        if time > attraction.closingHours:
            return False

        time += attraction.DurationMax
        location = LocationDTO(attraction.Lat, attraction.Lng)

    # חזרה לנקודת מוצא
    return_drive = get_drive_time_minutes(location, trip.pointDeparture)
    time += return_drive

    return time <= trip.endHour


def compute_best_route(selected, trip):
    best_route = None
    min_total_time = float('inf')

    for perm in itertools.permutations(selected):
        if is_valid_route(perm, trip):
            # נחשב זמן כולל
            time = trip.startHour
            location = trip.pointDeparture

            for a in perm:
                dist = get_drive_time_minutes(location, a)
                time += dist / 60 + a.DurationMax
                location = LocationDTO(a.Lat, a.Lng)

            # חזרה
            time += get_drive_time_minutes(location, trip.pointDeparture) / 60

            if time < min_total_time:
                min_total_time = time
                best_route = perm

    return best_route


def compute_total_cost(route, trip):
    return sum(a.Price for a in route) * trip.countPepole


import json


# ייצוא המסלול לJSON
def export_route_to_json(route, trip):
    output = []
    time = trip.startHour
    location = trip.pointDeparture

    for attraction in route:
        distance = get_drive_time_minutes(location, attraction)
        drive_time = distance / 60

        time += drive_time
        if time < attraction.openingHours:
            time = attraction.openingHours

        arrival_time = time

        output.append({
            "id": attraction.AttractionID,
            "name": attraction.AttractionName,
            "lat": attraction.Lat,
            "lng": attraction.Lng,
            "arrival_time": round(arrival_time, 2),
            "price_per_person": attraction.Price,
            "link": attraction.DescriptionLink,
            "type": attraction.AttractionTypeID
        })

        time += attraction.DurationMax
        location = LocationDTO(attraction.Lat, attraction.Lng)

    return json.dumps({
        "route": output,
        "total_cost": compute_total_cost(route, trip),
        "total_people": trip.countPepole,
        "budget": trip.budget,
        "within_budget": compute_total_cost(route, trip) <= trip.budget
    }, indent=2)


# בדיקה מקומית
selected = select_attractions(trip, all_attractions, visitor_matchings)
route = compute_best_route(selected, trip)

if route:
    print("Total cost:", compute_total_cost(route, trip))
    json_output = export_route_to_json(route, trip)
    print(json_output)
else:
    print("No valid route found within constraints.")
