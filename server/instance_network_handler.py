import json
from twisted.internet import reactor
from twisted.internet.protocol import Protocol
from twisted.internet.protocol import ClientFactory
from twisted.internet.protocol import ServerFactory
from twisted.internet.endpoints import TCP4ServerEndpoint


class InstanceRequestMaker(object):
    """Requesting data from other Instances"""
    def __init__(self):
        """Dict containing a Queue for each instance {InstanceID : []}"""
        self.requestQueues = {}


class InstanceRequestClient(Protocol):
    def __init__(self):
        pass


class InstanceRequestClientFactory(ClientFactory):
    def __init__(self):
        pass


class InstanceRequestHandler(object):
    "Handles requests coming in from other Instances"
    def __init__(self):
        pass

    def run(self):
        """Runs the server to handle requests of other instances"""


class InstanceRequestServer(Protocol):
    def __init__(self):
        pass


class InstanceRequestServerFactory(ServerFactory):
    def __init__(self):
        pass
