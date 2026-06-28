import logging
import voluptuous as vol
from homeassistant import config_entries
from homeassistant.helpers import location

from .const import DOMAIN, CONF_STATION
from .station_list import fetch_stations, station_dropdown
from .auto_station import find_nearest_station

_LOGGER = logging.getLogger(__name__)

class WbiConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    async def async_step_user(self, user_input=None):
        errors = {}
        stations = {}
        try:
            stations = await fetch_stations()
        except Exception as err:
            # Do not crash the config flow on upstream/API issues.
            _LOGGER.warning("Could not fetch station list: %s", err)

        if user_input is not None:
            station = str(user_input.get(CONF_STATION, "")).strip()

            if station == "auto":
                if not stations:
                    errors["base"] = "cannot_connect"
                else:
                    try:
                        loc = await location.async_detect_location_info(self.hass)
                        auto_id = find_nearest_station(loc.latitude, loc.longitude, stations)
                        if auto_id is None:
                            errors["base"] = "cannot_connect"
                        else:
                            station = auto_id
                    except Exception as err:
                        _LOGGER.warning("Could not auto-detect nearest station: %s", err)
                        errors["base"] = "cannot_connect"

            if not station:
                errors["base"] = "cannot_connect"

            if not errors:
                user_input[CONF_STATION] = station
                return self.async_create_entry(
                    title=f"DWD Index Station {user_input[CONF_STATION]}",
                    data=user_input
                )

        if stations:
            dropdown = station_dropdown(stations)
            schema = vol.Schema({
                vol.Required(CONF_STATION): vol.In(
                    {"auto": "Automatisch (GPS)"} | dropdown
                )
            })
        else:
            schema = vol.Schema({
                vol.Required(CONF_STATION): str
            })

        return self.async_show_form(step_id="user", data_schema=schema, errors=errors)
