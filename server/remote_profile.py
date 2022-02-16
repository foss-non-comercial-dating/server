from local_data_manager import LocalDataManager
from errors import InvalidProfileException


class Profile(object):
    def __init__(self, id, serverInstance):
        self.id = id
        try:
            LocalDataManager.validate(id)
        except InvalidProfileException:
            pass
