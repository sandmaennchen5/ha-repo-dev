import aiohttp
import json

STATIONS_URL = "https://opendata.dwd.de/weather/fire_forecast/stations.json"

async def fetch_stations():
    async with aiohttp.ClientSession() as session:
        async with session.get(STATIONS_URL) as resp:
            if resp.status != 200:
                raise ValueError(f"Stations request failed with HTTP {resp.status}")
            payload = await resp.text()
            data = json.loads(payload)

    stations = {}
    for s in data.get("stations", []):
        if not all(k in s for k in ("id", "name", "lat", "lon")):
            continue
        stations[s["id"]] = {
            "name": s["name"],
            "lat": float(s["lat"]),
            "lon": float(s["lon"])
        }

    if not stations:
        raise ValueError("No stations found in payload")

    return stations

def station_dropdown(stations):
    return {sid: f"{info['name']} ({sid})" for sid, info in stations.items()}
