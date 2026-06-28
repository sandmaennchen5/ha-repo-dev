import voluptuous as vol
from homeassistant import config_entries
from homeassistant.helpers import location

from .const import DOMAIN, CONF_STATION
from .station_list import fetch_stations, station_dropdown
from .auto_station import find_nearest_station

class WbiConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    async def async_step_user(self, user_input=None):
        stations = await fetch_stations()
        dropdown = station_dropdown(stations)

        if user_input is not None:
            if user_input[CONF_STATION] == "auto":
                loc = await location.async_detect_location_info(self.hass)
                auto_id = find_nearest_station(loc.latitude, loc.longitude, stations)
                user_input[CONF_STATION] = auto_id

            return self.async_create_entry(
                title=f"DWD Index Station {user_input[CONF_STATION]}",
                data=user_input
            )

        schema = vol.Schema({
            vol.Required(CONF_STATION): vol.In(
                {"auto": "Automatisch (GPS)"} | dropdown
            )
        })

        return self.async_show_form(step_id="user", data_schema=schema)
