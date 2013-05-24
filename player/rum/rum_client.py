import zmq, hashlib, threading, time
import protocol.auth_pb2 as auth_pb2
from rum_message import RumMessage
from client import Client

class RumClient(threading.Thread):
    def __init__(self, name, secret, handler = None):
        threading.Thread.__init__(self)

        self.name = name
        self.secret = secret
        self.handler = handler
        self.context = zmq.Context()

        self.auth_server = self.context.socket(zmq.REQ)
        self.auth_server.connect("tcp://rum.mit.edu:5000")

        self.server = self.context.socket(zmq.SUB)
        self.server.connect("tcp://rum.mit.edu:5001")
        self.server.setsockopt(zmq.SUBSCRIBE, self.name)

        self.server_out = self.context.socket(zmq.PUB)
        self.server_out.connect("tcp://rum.mit.edu:5002")

    def authenticate(self):
        auth_message = auth_pb2.AuthMessage()
        auth_message.type = auth_pb2.AuthMessage.HELLO
        auth_message.name = self.name
        self.auth_server.send(auth_message.SerializeToString())
        data = self.auth_server.recv()
        challenge = auth_pb2.AuthMessage()
        challenge.ParseFromString(data)
        
        if challenge.type != auth_pb2.AuthMessage.CHALLENGE:
            raise Exception("Unexpected response from server %s " %
                            str(challenge))
        else:
            response = auth_pb2.AuthMessage()
            response.name = self.name
            response.type = auth_pb2.AuthMessage.RESPONSE
            response.response = hashlib.sha256(challenge.nonce + self.secret ).hexdigest()

            self.auth_server.send(response.SerializeToString())

        data = self.auth_server.recv()

        response = auth_pb2.AuthMessage()
        response.ParseFromString(data)
        if response.type == auth_pb2.AuthMessage.TOKEN:
            self.token = response.token
            return True
        else:
            print response.error_message
            return False

    def run(self):
        while True:
            multipart = self.server.recv_multipart()
            # Message format [dest, type, message, crypto]
            # For signed messages, crypto is sig
            # For encrypted messages, crypto is a nonce
            message = RumMessage()
            message.parse_from_multipart(multipart)
            if message.verify(self.secret, self.token):
                print message.payload

            if self.handler:
                self.handler(message.payload)
            else:
                print "received message", message.payload

    def register_message_handler(self, handler):
        self.handler = handler

    def send(self, destination, payload):
        message = RumMessage(payload, self.name, destination)
        #message.encrypt(self.secret)
        message.sign(self.secret, self.token)
        self.server_out.send_multipart(message.serialize_to_multipart())
        
        





        
if __name__ == '__main__' :
    r = RumClient("isaac", "pete")
    if r.authenticate():
        print "Authenticated"
    r.setDaemon(True)
    r.start()
    r.send("isaac", {"message": "test"})
    while True:
        time.sleep(.1)
