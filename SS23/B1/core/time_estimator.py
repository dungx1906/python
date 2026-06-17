from datetime import datetime, timedelta


def predict_eta(
        departure_time_string,
        distance_km,
        vehicle_speed_kmh=60):

    departure_time = datetime.strptime(
        departure_time_string,
        "%Y-%m-%d %H:%M:%S"
    )

    travel_hours = distance_km / vehicle_speed_kmh

    estimated_arrival_time = (
        departure_time +
        timedelta(hours=travel_hours)
    )

    return estimated_arrival_time