import json

from twisted.websocket import WebSocketServerProtocol

from user import User
from enums import ClientRequestType
from errors import InvalidRequestType, UserAuthFailed


class ClientNetworkHandler(object):
    def __init__(self, server):
        self.server = server

    def run(self):
        """Runs the server for Handeling Client Requests"""
        pass

    def request(self, request):
        request_dict = json.loads(request.decode("utf-8"))
        auth = request_dict["auth"]
        data_raw = request_dict["data"]
        data = json.loads(data)
        if data["type"] == ClientRequestType.REGISTER:
            raise NotImplementedError
        elif data["type"] == ClientRequestType.SIGNIN:
            raise NotImplementedError

        if not self.server.cryptdate.validateUserAuth():
            raise UserAuthFailed

        if data["type"] == ClientRequestType.GET_MATCHES:
            pass
        elif data["type"] == "...":
            pass
        else:
            raise InvalidRequestType

    def handleGetMatches(self, auth):
        user = User(auth)
        self.reply(ClientRequestType.GET_MATCHES, user.matches)

    def reply(self, reply_type, data):
        """This will reply to user requests"""
        pass
