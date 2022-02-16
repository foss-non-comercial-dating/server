import websockets
import json
from user import User
from enums import ClientRequestType
from errors import InvalidRequestType


class ClientNetworkHandler(object):
    def __init__(self, server):
        self.server = server

    def run(self):
        """Runs the server for Handeling Client Requests"""
        pass

    def request(self, request):
        request_dict = json.loads(request.decode("utf-8"))
        request_type = ClientRequestType(request_dict["type"])

        if request_type == ClientRequestType.GET_MATCHES:
            self.handleGetMatches(request_dict["auth"])
        elif request_type == ClientRequestType.SEND_MESSAGE:
            raise NotImplementedError
        else:
            raise InvalidRequestType

    def handleGetMatches(self, auth):
        user = User(auth)
        self.reply(ClientRequestType.GET_MATCHES, user.matches)

    def reply(self, reply_type, data):
        """This will reply to user requests"""
        pass
