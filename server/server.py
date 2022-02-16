import logging


from local_data_manager import LocalDataManager
from instance_network_handler import InstanceRequestHandler, InstanceRequestMaker
from client_network_handler import ClientNetworkHandler
from crypdate import CryptDate


class Server(object):
    """The Main class that runs the server"""

    def __init__(self, argv):
        self.argv = argv
        self.data_manager = LocalDataManager(self)
        self.cryptdate = CryptDate(self)
        self.instance_request_handler = InstanceRequestHandler(self)
        self.instance_request_maker = InstanceRequestMaker(self)
        self.client_network_handler = ClientNetworkHandler(self)

    def run(self):
        """Runs the main Server"""
        self.client_network_handler.run()
        self.instance_request_handler.run()
