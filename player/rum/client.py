import auth_helper
import protocol.auth_pb2 as auth_pb2

class Client:
    def __init__(self, name, secret):
        self.name = name
        self.secret = secret
        self.token = ""
        self.nonce = ""
    def make_challenge(self):
        self.nonce = auth_helper.make_nonce()
        auth_message = auth_pb2.AuthMessage()
        auth_message.name = self.name
        auth_message.type = auth_pb2.AuthMessage.CHALLENGE
        auth_message.nonce = self.nonce
        return auth_message
