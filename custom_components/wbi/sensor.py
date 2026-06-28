import aiohttp
import async_timeout
import logging
from datetime import timedelta
from homeassistant.components.sensor import SensorEntity
from homeassistant.helpers.update_coordinator import (
    DataUpdateCoordinator,
    UpdateFailed,
)

from .const import DOMAIN, CONF_STATION, BASE_URL_WBI, BASE_URL_GFI

_LOGGER = logging.getLogger(__name__)

async def async_setup_entry(hass, entry, async_add_entities):
    station = entry.data[CONF_STATION]

    coordinator = DwdCoordinator(hass, station)
    await coordinator.async_config_entry_first_refresh()

    async_add_entities([
        WaldbrandSensor(coordinator),
        GraslandSensor(coordinator),
    ])

class DwdCoordinator(DataUpdateCoordinator):
    def __init__(self, hass, station):
        super().__init__(
            hass,
            logger=_LOGGER,
            name="DWD Gefahrenindex",
            update_interval=timedelta(minutes=60),
        )
        self.station = station

    async def _async_update_data(self):
        async with aiohttp.ClientSession() as session:
            try:
                async with async_timeout.timeout(10):
                    wbi_url = BASE_URL_WBI.format(self.station)
                    gfi_url = BASE_URL_GFI.format(self.station)

                    async with session.get(wbi_url) as wbi:
                        wbi_json = await wbi.json()

                    async with session.get(gfi_url) as gfi:
                        gfi_json = await gfi.json()

                    return {
                        "wbi": wbi_json["forecast"][0]["index"],
                        "gfi": gfi_json["forecast"][0]["index"],
                    }
            except Exception as err:
                raise UpdateFailed(err)

class WaldbrandSensor(SensorEntity):
    def __init__(self, coordinator):
        self.coordinator = coordinator

    @property
    def name(self):
        return "Waldbrandindex"

    @property
    def unique_id(self):
        return "wbi_waldbrandindex"

    @property
    def state(self):
        return self.coordinator.data.get("wbi")

    @property
    def should_poll(self):
        return False

    async def async_update(self):
        await self.coordinator.async_request_refresh()

class GraslandSensor(SensorEntity):
    def __init__(self, coordinator):
        self.coordinator = coordinator

    @property
    def name(self):
        return "Graslandfeuerindex"

    @property
    def unique_id(self):
        return "wbi_graslandfeuerindex"

    @property
    def state(self):
        return self.coordinator.data.get("gfi")

    @property
    def should_poll(self):
        return False

    async def async_update(self):
        await self.coordinator.async_request_refresh()
