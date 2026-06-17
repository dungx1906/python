import math


def calculate_distance(
        departure_latitude,
        departure_longitude,
        destination_latitude,
        destination_longitude):

    earth_radius_km = 6371

    departure_latitude_rad = math.radians(departure_latitude)
    departure_longitude_rad = math.radians(departure_longitude)

    destination_latitude_rad = math.radians(destination_latitude)
    destination_longitude_rad = math.radians(destination_longitude)

    latitude_difference = (
        destination_latitude_rad -
        departure_latitude_rad
    )

    longitude_difference = (
        destination_longitude_rad -
        departure_longitude_rad
    )

    haversine_value = (
        math.sin(latitude_difference / 2) ** 2
        + math.cos(departure_latitude_rad)
        * math.cos(destination_latitude_rad)
        * math.sin(longitude_difference / 2) ** 2
    )

    central_angle = (
        2 *
        math.atan2(
            math.sqrt(haversine_value),
            math.sqrt(1 - haversine_value)
        )
    )

    distance_km = earth_radius_km * central_angle

    return distance_km