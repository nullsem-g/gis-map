import math
from dataclasses import dataclass


@dataclass
class Point:
    latitude: float
    longitude: float


def haversine_distance(p1: Point, p2: Point) -> float:
    """Calculate the great-circle distance between two points in kilometers."""
    radius_earth_km = 6371.0
    lat1_rad = math.radians(p1.latitude)
    lat2_rad = math.radians(p2.latitude)
    d_lat = math.radians(p2.latitude - p1.latitude)
    d_lon = math.radians(p2.longitude - p1.longitude)

    a = (
        math.sin(d_lat / 2) ** 2
        + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(d_lon / 2) ** 2
    )
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return radius_earth_km * c
