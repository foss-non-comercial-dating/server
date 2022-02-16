import json

from global_config import INSTANCE_REQUEST_PORT, CLIENT_REQUEST_PORT, InvalidRequestType
from enums import InstanceRequestType
from errors import InstanceAuthFailed

from twisted.internet import reactor
from twisted.internet.protocol import Protocol
from twisted.internet.protocol import ClientFactory
from twisted.internet.protocol import ServerFactory
from twisted.internet.endpoints import TCP4ServerEndpoint


class InstanceRequestMaker(object):
    """Requesting data from other Instances"""
    def __init__(self, server):
        self.server = server
        """Dict containing a Queue for each instance {InstanceID : []}"""
        self.requestQueues = {}

    def request(self, type : InstanceRequestType, data : dict):
        pass


class InstanceRequestClient(Protocol):
    def __init__(self):
        pass

    def dataReceived(self, data):
        pass


class InstanceRequestClientFactory(ClientFactory):
    def __init__(self):
        pass


class InstanceRequestHandler(object):
    "Handles requests coming in from other Instances"
    def __init__(self, server):
        self.server = server

    def run(self):
        """Runs the server to handle requests of other instances"""
        endpoint = TCP4ServerEndpoint(reactor, INSTANCE_REQUEST_PORT)
        endpoint.listen(InstanceRequestServerFactory())
        reactor.run()

    def handle(self, requests, serverThread):
        if type == InstanceRequestType.ANOUNCE_PRESENCE:
            pass
        elif type == InstanceRequestType.GET_INSTANCES:
            pass
        else:
            raise InvalidRequestType


class InstanceRequestServer(Protocol):
    def __init__(self, handler):
        self.handler = handler

    def dataReceived(self, data):
        requests = json.loads(data.decode("utf-8"))
        self.handler.handle(requests, self)

    def connectioMade(self):
        pass

    def reply(self, type, data):
        pass


class InstanceRequestServerFactory(ServerFactory):
    def __init__(self, handler):
        self.handler = handler

    def buildProtocol(self, addr):
        return InstanceRequestServer(self.handler)
