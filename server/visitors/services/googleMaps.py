import requests

def get_drive_time_minutes(origin, destination):
    url = "https://maps.googleapis.com/maps/api/distancematrix/json"
    params = {
        "origins": f"{origin.Lat},{origin.Lng}",
        "destinations": f"{destination.Lat},{destination.Lng}",
        "key": "AIzaSyBNVjEXhyDOUvcCECJFY5x_OGKt38dxVBk",
        "mode": "driving",
        "units": "metric"
    }
    response = requests.get(url, params=params)
    data = response.json()

    try:
        seconds = data['rows'][0]['elements'][0]['duration']['value']
        return seconds / 60
    except (KeyError, IndexError):
        return float('inf')
