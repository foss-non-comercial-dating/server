from enum import Enum


class ClientRequestType(Enum):
    """LOCAL INSTANCE INTERACTIONS"""

    REGISTER = 1
    SIGNIN = 2

    """GENERAL INTERACTIONS"""
    GET_MATCHES = 101
    SEND_MESSAGE = 201


class InstanceRequestType(Enum):
    GET_INSTANCES = 1
    ANOUNCE_PRESENCE = 2
    ANOUNCE_LOCATION_CHANGE = 3
