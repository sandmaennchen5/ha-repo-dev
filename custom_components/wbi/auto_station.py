from math import sqrt
from .station_list import STATIONS

def find_nearest_station(lat, lon):
    best_station = None
    best_dist = 999999

    for sid, data in STATIONS.items():
        d = sqrt((lat - data["lat"])**2 + (lon - data["lon"])**2)
        if d < best_dist:
            best_dist = d
            best_station = sid

    return best_station

from math import sqrt

def find_nearest_station(lat, lon, stations):
    best_station = None
    best_dist = 999999

    for sid, data in stations.items():
        d = sqrt((lat - data["lat"])**2 + (lon - data["lon"])**2)
        if d < best_dist:
            best_dist = d
            best_station = sid

    return best_station
