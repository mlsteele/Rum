import zmq, random, hashlib,  threading, time
import json
import protocol.auth_pb2 as auth_pb2
from rum_message import *
from client import *
from player_server import *



class AuthServer(threading.Thread):

    def __init__(self,clients = {}, zmq_spec = 'tcp://*:5000'):
        # Init ZMQ context
        self.context = zmq.Context()    # Seperate context per thread
        self.auth  = self.context.socket(zmq.REP)
        self.auth.bind(zmq_spec)
        threading.Thread.__init__(self)
        self.setDaemon(True)        # make this shut down cleanly
        self.clients_by_name = clients
    def make_error(self, message, name="Unknown"):
        error_message = auth_pb2.AuthMessage()
        error_message.name = name
        error_message.type = auth_pb2.AuthMessage.ERROR
        error_message.error_message = message
        return error_message

    def handle_hello(self, hello_message):
        name = hello_message.name
        if name in self.clients_by_name:
            return self.clients_by_name[name].make_challenge()
        else:
            return  self.make_error("Client %s does not exist" % name, name)

    def handle_response(self, response):
        if response.name in self.clients_by_name:
            client = self.clients_by_name[response.name]
            expected_response = auth_helper.sign_nonce(client.nonce,
                                                             client.secret)
            if response.response == expected_response:
                token = auth_helper.make_nonce()
                token_message = auth_pb2.AuthMessage()
                token_message.name = response.name
                token_message.type = auth_pb2.AuthMessage.TOKEN 
                token_message.token = token
                client.token = token
                return token_message
                # Sweet. User authenicated
            else:
                return self.make_error("Failed to authenticated %s" % response.name,
                                  response.name)
        else:
            return  self.make_error("Client %s does not exist" % response.name,
                               response.name)

    def handle_error(self, error_message):
        print error_message.error_message
    def verify_message(self, message):
        if message.src in self.clients_by_name:
            client = self.clients_by_name[message.src]
            token = client.token
            secret = client.secret
            return message.verify(secret,token)
        else:
            print "Unknown sender"
            return False
    def modify_to_forward(self, message):
        if message.src in self.clients_by_name:
            if message.dst in self.clients_by_name:
                source = self.clients_by_name[message.src]
                destination = self.clients_by_name[message.dst]
                if message.security == RumMessage.ENCRYPTED:
                    message.decrypt(source.secret)
                    message.encrypt(destination.secret)
                elif message.security == RumMessage.SIGNED:
                    message.sign(destination.secret, destination.token)

                return message
            else:
                print "Unknown receiver"
        else:
            print "Unknown sender"

    def run(self): 
        while True:
            # Receive a "packet"
            data = self.auth.recv()
            auth_message = auth_pb2.AuthMessage()

            # Parse into object
            auth_message.ParseFromString(data)

            # handle request
            t = auth_message.type
            if t == auth_pb2.AuthMessage.HELLO: 
                response = self.handle_hello(auth_message)
            elif t == auth_pb2.AuthMessage.RESPONSE: 
                response = self.handle_response(auth_message)
            elif t== auth_pb2.AuthMessage.ERROR: 
                response =  self.handle_error(auth_message)

            # send response
            self.auth.send(response.SerializeToString())


