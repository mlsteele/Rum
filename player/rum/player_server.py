import threading, zmq
from rum_message import *


class PlayerServer(threading.Thread):
    def __init__(self, auth_server=None):
        self.context = zmq.Context()

        self.clients = self.context.socket(zmq.PUB)
        self.clients.bind("tcp://*:5001")
        self.clients_in = self.context.socket(zmq.SUB)

        self.clients_in.bind("tcp://*:5002")
        self.clients_in.setsockopt(zmq.SUBSCRIBE, "")

        threading.Thread.__init__(self)
        self.auth_server = auth_server

    def run(self):
        while True:
            body = self.clients_in.recv_multipart()
            message = RumMessage()
            message.parse_from_multipart(body)
            if self.auth_server.verify_message(message):
                pass
            else:
                print "Message verification failed"
            self.auth_server.modify_to_forward(message)
            self.clients.send_multipart(message.serialize_to_multipart())

