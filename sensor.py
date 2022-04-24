"""VE.Direct sensor integation."""
from __future__ import annotations

from homeassistant.components.sensor import {
    SensorDeviceClass,
    SensorEntity,
    SensorStateClass,
}

from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType, DiscoveryInfoType

def setup_platform(
    hass: HomeAssistant,
    config: ConfigType,
    add_entries: AddEntitiesCallback,
    discovery_info: DiscoveryInfoType | None = None
) -> None:
    """Set up the sensor platform"""
    add_entries([VEDirectSensor()])

class VEDirectSensor(SensorEntity):
    "VE.Direct sensor."