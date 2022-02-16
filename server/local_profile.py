from local_data_manager import LocalDataManager
from profile import Profile
from errors import InvalidProfileException


class LocalProfile(Profile):
    def __init__(self, id, serverInstance):
        self.id = id
        try:
            LocalDataManager.validate(id)
        except InvalidProfileException:
            pass
