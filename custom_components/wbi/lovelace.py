def get_cards(station_lat: float, station_lon: float):
    return {
        "mushroom": {
            "type": "horizontal-stack",
            "cards": [
                {
                    "type": "custom:mushroom-template-card",
                    "entity": "sensor.waldbrandindex",
                    "primary": "Waldbrandindex",
                    "secondary": "Stufe: {{ states('sensor.waldbrandindex') }}",
                    "icon": "mdi:fire-alert",
                    "badge_color": "{% set v = states('sensor.waldbrandindex') | int %}{% if v == 1 %}green{% elif v == 2 %}light-green{% elif v == 3 %}orange{% elif v == 4 %}red{% elif v == 5 %}purple{% else %}grey{% endif %}",
                },
                {
                    "type": "custom:mushroom-template-card",
                    "entity": "sensor.graslandfeuerindex",
                    "primary": "Graslandfeuerindex",
                    "secondary": "Stufe: {{ states('sensor.graslandfeuerindex') }}",
                    "icon": "mdi:grass",
                    "badge_color": "{% set v = states('sensor.graslandfeuerindex') | int %}{% if v == 1 %}green{% elif v == 2 %}yellow{% elif v == 3 %}orange{% elif v == 4 %}red{% elif v == 5 %}purple{% else %}grey{% endif %}",
                },
            ],
        },
        "tile": {
            "type": "horizontal-stack",
            "cards": [
                {
                    "type": "tile",
                    "entity": "sensor.waldbrandindex",
                    "name": "Waldbrandindex",
                    "icon": "mdi:fire-alert",
                    "color": "{% set v = states('sensor.waldbrandindex') | int %}{% if v == 1 %}green{% elif v == 2 %}light-green{% elif v == 3 %}orange{% elif v == 4 %}red{% elif v == 5 %}purple{% else %}grey{% endif %}",
                },
                {
                    "type": "tile",
                    "entity": "sensor.graslandfeuerindex",
                    "name": "Graslandfeuerindex",
                    "icon": "mdi:grass",
                    "color": "{% set v = states('sensor.graslandfeuerindex') | int %}{% if v == 1 %}green{% elif v == 2 %}yellow{% elif v == 3 %}orange{% elif v == 4 %}red{% elif v == 5 %}purple{% else %}grey{% endif %}",
                },
            ],
        },
        "map": {
            "type": "custom:leaflet-map",
            "layers": [
                {
                    "type": "marker",
                    "name": "Waldbrandindex",
                    "latitude": station_lat,
                    "longitude": station_lon,
                    "icon": "mdi:fire-alert",
                    "icon_color": "{% set v = states('sensor.waldbrandindex') | int %}{% if v == 1 %}green{% elif v == 2 %}yellow{% elif v == 3 %}orange{% elif v == 4 %}red{% elif v == 5 %}purple{% else %}grey{% endif %}",
                },
                {
                    "type": "marker",
                    "name": "Graslandfeuerindex",
                    "latitude": station_lat,
                    "longitude": station_lon,
                    "icon": "mdi:grass",
                    "icon_color": "{% set v = states('sensor.graslandfeuerindex') | int %}{% if v == 1 %}green{% elif v == 2 %}yellow{% elif v == 3 %}orange{% elif v == 4 %}red{% elif v == 5 %}purple{% else %}grey{% endif %}",
                },
            ],
        },
        "apex": {
            "type": "custom:apexcharts-card",
            "graph_span": "7d",
            "header": {"title": "DWD Gefahrenindex Verlauf"},
            "series": [
                {
                    "entity": "sensor.waldbrandindex",
                    "name": "Waldbrandindex",
                    "color": "red",
                },
                {
                    "entity": "sensor.graslandfeuerindex",
                    "name": "Graslandfeuerindex",
                    "color": "green",
                },
            ],
        },
    }

def get_heatmap(stations, wbi_values):
    heat_data = []
    for sid, info in stations.items():
        heat_data.append([info["lat"], info["lon"], wbi_values.get(sid, 0)])

    return {
        "type": "custom:leaflet-map",
        "layers": [
            {
                "type": "heatmap",
                "data": heat_data,
                "radius": 25,
                "blur": 15
            }
        ]
    }
