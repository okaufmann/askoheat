"""Parameter block Api descriptor classes."""

# http://www.download.askoma.com/askofamily_plus/modbus/askoheat-modbus.html#Parameter_Block
from __future__ import annotations

from homeassistant.components.sensor.const import (
    SensorDeviceClass,
    SensorStateClass,
)
from homeassistant.const import (
    EntityCategory,
    UnitOfPower,
)

from custom_components.askoheat.api_desc import (
    FlagRegisterInputDescriptor,
    RegisterBlockDescriptor,
    StringRegisterInputDescriptor,
    UnsignedInt16RegisterInputDescriptor,
)
from custom_components.askoheat.const import (
    BinarySensorAttrKey,
    DeviceKey,
    SensorAttrKey,
)
from custom_components.askoheat.model import (
    AskoheatBinarySensorEntityDescription,
    AskoheatSensorEntityDescription,
)

PARAMETER_REGISTER_BLOCK_DESCRIPTOR = RegisterBlockDescriptor(
    starting_register=400,
    number_of_registers=56,
    sensors=[
        AskoheatSensorEntityDescription(
            key=SensorAttrKey.PAR_ID,
            api_descriptor=StringRegisterInputDescriptor(0, 16),
            device_key=DeviceKey.WATER_HEATER_CONTROL_UNIT,
            entity_category=EntityCategory.DIAGNOSTIC,
        ),
        AskoheatSensorEntityDescription(
            key=SensorAttrKey.PAR_HEATER1_POWER,
            api_descriptor=UnsignedInt16RegisterInputDescriptor(17),
            native_min_value=250,
            native_max_value=10000,
            state_class=SensorStateClass.MEASUREMENT,
            device_class=SensorDeviceClass.POWER,
            native_unit_of_measurement=UnitOfPower.WATT,
            device_key=DeviceKey.WATER_HEATER_CONTROL_UNIT,
            entity_category=EntityCategory.DIAGNOSTIC,
        ),
        AskoheatSensorEntityDescription(
            key=SensorAttrKey.PAR_HEATER2_POWER,
            api_descriptor=UnsignedInt16RegisterInputDescriptor(18),
            native_min_value=250,
            native_max_value=10000,
            state_class=SensorStateClass.MEASUREMENT,
            device_class=SensorDeviceClass.POWER,
            native_unit_of_measurement=UnitOfPower.WATT,
            device_key=DeviceKey.WATER_HEATER_CONTROL_UNIT,
            entity_category=EntityCategory.DIAGNOSTIC,
        ),
        AskoheatSensorEntityDescription(
            key=SensorAttrKey.PAR_HEATER3_POWER,
            api_descriptor=UnsignedInt16RegisterInputDescriptor(19),
            native_min_value=250,
            native_max_value=10000,
            state_class=SensorStateClass.MEASUREMENT,
            device_class=SensorDeviceClass.POWER,
            native_unit_of_measurement=UnitOfPower.WATT,
            device_key=DeviceKey.WATER_HEATER_CONTROL_UNIT,
            entity_category=EntityCategory.DIAGNOSTIC,
        ),
        AskoheatSensorEntityDescription(
            key=SensorAttrKey.PAR_ARTICLE_NUMBER,
            api_descriptor=StringRegisterInputDescriptor(20, 8),
            device_key=DeviceKey.WATER_HEATER_CONTROL_UNIT,
            entity_category=EntityCategory.DIAGNOSTIC,
        ),
        AskoheatSensorEntityDescription(
            key=SensorAttrKey.PAR_ARTICLE_NAME,
            api_descriptor=StringRegisterInputDescriptor(28, 16),
            device_key=DeviceKey.WATER_HEATER_CONTROL_UNIT,
            entity_category=EntityCategory.DIAGNOSTIC,
        ),
        AskoheatSensorEntityDescription(
            key=SensorAttrKey.PAR_SOFTWARE_VERSION,
            api_descriptor=StringRegisterInputDescriptor(44, 3),
            device_key=DeviceKey.WATER_HEATER_CONTROL_UNIT,
            entity_category=EntityCategory.DIAGNOSTIC,
        ),
        AskoheatSensorEntityDescription(
            key=SensorAttrKey.PAR_HARDWARE_VERSION,
            api_descriptor=StringRegisterInputDescriptor(47, 3),
            device_key=DeviceKey.WATER_HEATER_CONTROL_UNIT,
            entity_category=EntityCategory.DIAGNOSTIC,
        ),
        AskoheatSensorEntityDescription(
            key=SensorAttrKey.PAR_HEATER4_POWER,
            api_descriptor=UnsignedInt16RegisterInputDescriptor(50),
            native_min_value=250,
            native_max_value=10000,
            state_class=SensorStateClass.MEASUREMENT,
            device_class=SensorDeviceClass.POWER,
            native_unit_of_measurement=UnitOfPower.WATT,
            device_key=DeviceKey.WATER_HEATER_CONTROL_UNIT,
            entity_category=EntityCategory.DIAGNOSTIC,
            entity_registry_enabled_default=False,
        ),
        AskoheatSensorEntityDescription(
            key=SensorAttrKey.PAR_HEATER5_POWER,
            api_descriptor=UnsignedInt16RegisterInputDescriptor(51),
            native_min_value=250,
            native_max_value=10000,
            state_class=SensorStateClass.MEASUREMENT,
            device_class=SensorDeviceClass.POWER,
            native_unit_of_measurement=UnitOfPower.WATT,
            device_key=DeviceKey.WATER_HEATER_CONTROL_UNIT,
            entity_category=EntityCategory.DIAGNOSTIC,
            entity_registry_enabled_default=False,
        ),
        AskoheatSensorEntityDescription(
            key=SensorAttrKey.PAR_HEATER6_POWER,
            api_descriptor=UnsignedInt16RegisterInputDescriptor(52),
            native_min_value=250,
            native_max_value=10000,
            state_class=SensorStateClass.MEASUREMENT,
            device_class=SensorDeviceClass.POWER,
            native_unit_of_measurement=UnitOfPower.WATT,
            device_key=DeviceKey.WATER_HEATER_CONTROL_UNIT,
            entity_category=EntityCategory.DIAGNOSTIC,
            entity_registry_enabled_default=False,
        ),
        AskoheatSensorEntityDescription(
            key=SensorAttrKey.PAR_NUMBER_OF_STEPS,
            api_descriptor=UnsignedInt16RegisterInputDescriptor(53),
            native_min_value=6,
            native_max_value=19,
            device_key=DeviceKey.WATER_HEATER_CONTROL_UNIT,
            entity_category=EntityCategory.DIAGNOSTIC,
        ),
        AskoheatSensorEntityDescription(
            key=SensorAttrKey.PAR_NUMBER_OF_HEATER,
            api_descriptor=UnsignedInt16RegisterInputDescriptor(54),
            native_min_value=3,
            native_max_value=6,
            device_key=DeviceKey.WATER_HEATER_CONTROL_UNIT,
            entity_category=EntityCategory.DIAGNOSTIC,
        ),
        AskoheatSensorEntityDescription(
            key=SensorAttrKey.PAR_MAX_POWER,
            api_descriptor=UnsignedInt16RegisterInputDescriptor(55),
            native_min_value=1750,
            native_max_value=20000,
            state_class=SensorStateClass.MEASUREMENT,
            device_class=SensorDeviceClass.POWER,
            native_unit_of_measurement=UnitOfPower.WATT,
            device_key=DeviceKey.WATER_HEATER_CONTROL_UNIT,
            entity_category=EntityCategory.DIAGNOSTIC,
        ),
    ],
    binary_sensors=[
        AskoheatBinarySensorEntityDescription(
            key=BinarySensorAttrKey.PAR_TYPE_3_STAGE_VERSION,
            icon="mdi:numeric-3",
            api_descriptor=FlagRegisterInputDescriptor(16, 0),
            device_key=DeviceKey.WATER_HEATER_CONTROL_UNIT,
            entity_category=EntityCategory.DIAGNOSTIC,
        ),
        AskoheatBinarySensorEntityDescription(
            key=BinarySensorAttrKey.PAR_TYPE_7_STAGE_VERSION,
            icon="mdi:numeric-7",
            api_descriptor=FlagRegisterInputDescriptor(16, 1),
            device_key=DeviceKey.WATER_HEATER_CONTROL_UNIT,
            entity_category=EntityCategory.DIAGNOSTIC,
        ),
        AskoheatBinarySensorEntityDescription(
            key=BinarySensorAttrKey.PAR_HEATER_TYPE_FLANGE,
            api_descriptor=FlagRegisterInputDescriptor(16, 2),
            device_key=DeviceKey.WATER_HEATER_CONTROL_UNIT,
            entity_category=EntityCategory.DIAGNOSTIC,
            entity_registry_enabled_default=False,
        ),
        AskoheatBinarySensorEntityDescription(
            key=BinarySensorAttrKey.PAR_HEATER_TYPE_SCREW_IN,
            icon="mdi:screw-lag",
            api_descriptor=FlagRegisterInputDescriptor(16, 3),
            device_key=DeviceKey.WATER_HEATER_CONTROL_UNIT,
            entity_category=EntityCategory.DIAGNOSTIC,
            entity_registry_enabled_default=False,
        ),
        AskoheatBinarySensorEntityDescription(
            key=BinarySensorAttrKey.PAR_WIRED_AS_STAR_CONNECTION,
            icon="mdi:connection",
            api_descriptor=FlagRegisterInputDescriptor(16, 4),
            device_key=DeviceKey.WATER_HEATER_CONTROL_UNIT,
            entity_category=EntityCategory.DIAGNOSTIC,
            entity_registry_enabled_default=False,
        ),
        AskoheatBinarySensorEntityDescription(
            key=BinarySensorAttrKey.PAR_WIRED_AS_DELTA_CONECTION,
            icon="mdi:connection",
            api_descriptor=FlagRegisterInputDescriptor(16, 5),
            device_key=DeviceKey.WATER_HEATER_CONTROL_UNIT,
            entity_category=EntityCategory.DIAGNOSTIC,
            entity_registry_enabled_default=False,
        ),
        # bit 6 ignored
        AskoheatBinarySensorEntityDescription(
            key=BinarySensorAttrKey.PAR_TYPE_OEM_VERSION,
            api_descriptor=FlagRegisterInputDescriptor(16, 7),
            device_key=DeviceKey.WATER_HEATER_CONTROL_UNIT,
            entity_category=EntityCategory.DIAGNOSTIC,
            entity_registry_enabled_default=False,
        ),
    ],
)
