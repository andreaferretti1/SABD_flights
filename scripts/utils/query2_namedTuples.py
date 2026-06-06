from collections import namedtuple

BaseRecord = namedtuple("BaseRecord", ["arr_delay", "cancelled", "diverted", "carrier_delay", "weather_delay", "nas_delay", "security_delay",
                                       "late_aircraft_delay"])

