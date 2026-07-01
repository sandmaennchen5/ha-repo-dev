import aiohttp
import async_timeout
from homeassistant.components.sensor import SensorEntity

UV_URL = "https://api.openuv.io/api/v1/uv?lat={}&lng={}"

class UvIndexSensor(SensorEntity):
    def __init__(self, lat, lon, api_key):
        self.lat = lat
        self.lon = lon
        self.api_key = api_key

    @property
    def name(self):
        return "UV Index"

    @property
    def unique_id(self):
        return "wbi_uv_index"

    async def async_update(self):
        headers = {"x-access-token": self.api_key}
        async with aiohttp.ClientSession() as session:
            async with async_timeout.timeout(10):
                async with session.get(UV_URL.format(self.lat, self.lon), headers=headers) as resp:
                    data = await resp.json()
                    self._attr_state = data["result"]["uv"]
