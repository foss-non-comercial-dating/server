from profile import Profile
import logging


class LocalDataManager(object):
    def __init__(self, server):
        # better solution than dict needed!
        self.profileCache = {}

    def getProfile(self, profileID) -> Profile:
        pass

    def validateProfile(self, profileID):
        """
        Checks weather a weather a Profile has a valid signature. If it doesn't something malicious is going on and it raises an Error
        """
