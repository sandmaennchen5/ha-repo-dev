import aiohttp

STATIONS_URL = "https://opendata.dwd.de/weather/fire_forecast/stations.json"

async def fetch_stations():
    async with aiohttp.ClientSession() as session:
        async with session.get(STATIONS_URL) as resp:
            data = await resp.json()

    stations = {}
    for s in data.get("stations", []):
        stations[s["id"]] = {
            "name": s["name"],
            "lat": float(s["lat"]),
            "lon": float(s["lon"])
        }

    return stations

def station_dropdown(stations):
    return {sid: f"{info['name']} ({sid})" for sid, info in stations.items()}
