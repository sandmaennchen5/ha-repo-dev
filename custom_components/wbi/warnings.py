import aiohttp
import async_timeout
from homeassistant.components.sensor import SensorEntity

WARN_URL = "https://opendata.dwd.de/weather/alerts/cap/DE000000.json"

async def fetch_warnings():
    async with aiohttp.ClientSession() as session:
        async with async_timeout.timeout(10):
            async with session.get(WARN_URL) as resp:
                return await resp.json()

class DwdWarningSensor(SensorEntity):
    @property
    def name(self):
        return "DWD Warnungen"

    @property
    def unique_id(self):
        return "wbi_dwd_warnings"

    async def async_update(self):
        data = await fetch_warnings()
        if "alerts" in data and len(data["alerts"]) > 0:
            alert = data["alerts"][0]
            self._attr_state = alert.get("severity", "None")
            self._attr_extra_state_attributes = {
                "headline": alert.get("headline"),
                "description": alert.get("description")
            }
        else:
            self._attr_state = "None"
