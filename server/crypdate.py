from PyCrypto import *


from server import Server


class CryptDate(object):
    """Class that does all the crypto validation an verification"""

    def __init__(self, server: Server):
        self.server = server

    def validateUserAuth(self, auth) -> bool:
        return True

    def validateInstanceAuth(self, auth) -> bool:
        return True
