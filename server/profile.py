from local_data_manager import *
from abc import ABC, abstractmethod


class Profile(object):
    """
    Interface Class for Profiles implemented by LocalProfile and RemoteProfile
    """

    @abstractmethod
    def __init__(self, id, serverInstance):
        raise NotImplementedError
