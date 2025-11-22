import esphome.codegen as cg
from esphome.components import text_sensor
import esphome.config_validation as cv
from esphome.const import CONF_ID, ENTITY_CATEGORY_DIAGNOSTIC

from . import CONF_SEPLOS_BMS_ID, SEPLOS_BMS_COMPONENT_SCHEMA

DEPENDENCIES = ["seplos_bms"]

CODEOWNERS = ["@syssi"]

CONF_ERRORS = "errors"
CONF_SYSSTATUS = "systemstatus"
CONF_POWERSTATUS = "powerstatus"
CONF_WARNINGS = "warnings"
CONF_CELLDISCONNECT = "celldisconnect"
CONF_CELLEQUI = "cellequalization"
CONF_CELLSTATUS = "cellstatus"

ICON_ERRORS = "mdi:alert-circle-outline"

TEXT_SENSORS = [
    CONF_CELLDISCONNECT,
    CONF_CELLEQUI,
    CONF_CELLSTATUS,
    CONF_ERRORS,
    CONF_SYSSTATUS,
    CONF_POWERSTATUS,
    CONF_WARNINGS,
]

CONFIG_SCHEMA = SEPLOS_BMS_COMPONENT_SCHEMA.extend(
    {
        cv.Optional(CONF_ERRORS): text_sensor.text_sensor_schema(
            text_sensor.TextSensor,
            icon=ICON_ERRORS,
            entity_category=ENTITY_CATEGORY_DIAGNOSTIC,
        ),
        cv.Optional(CONF_SYSSTATUS): text_sensor.text_sensor_schema(
            text_sensor.TextSensor,
            icon=ICON_ERRORS,
            entity_category=ENTITY_CATEGORY_DIAGNOSTIC,
        ),
        cv.Optional(CONF_POWERSTATUS): text_sensor.text_sensor_schema(
            text_sensor.TextSensor,

        ),
        cv.Optional(CONF_WARNINGS): text_sensor.text_sensor_schema(
            text_sensor.TextSensor,

        ),
            cv.Optional(CONF_CELLDISCONNECT): text_sensor.text_sensor_schema(
            text_sensor.TextSensor,

        ),
            cv.Optional(CONF_CELLEQUI): text_sensor.text_sensor_schema(
            text_sensor.TextSensor,

        ),
            cv.Optional(CONF_CELLSTATUS): text_sensor.text_sensor_schema(
            text_sensor.TextSensor,

        ),
    }
)


async def to_code(config):
    hub = await cg.get_variable(config[CONF_SEPLOS_BMS_ID])
    for key in TEXT_SENSORS:
        if key in config:
            conf = config[key]
            sens = cg.new_Pvariable(conf[CONF_ID])
            await text_sensor.register_text_sensor(sens, conf)
            cg.add(getattr(hub, f"set_{key}_text_sensor")(sens))
