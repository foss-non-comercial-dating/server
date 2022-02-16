from enum import Enum


class ClientRequestType(Enum):
    GET_MATCHES = 1
    SEND_MESSAGE = 2


class InstanceRequestType(Enum):
    GET_MATCHES = 1
    SEND_MESSAGE = 2
