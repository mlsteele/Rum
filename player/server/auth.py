import zmq, random, hashlib, auth_pb2
context = zmq.Context()
auth  = context.socket(zmq.REP)
auth.bind("tcp://*:5000")

def make_nonce():
    f = open("/dev/urandom")
    seed = f.read(100)
    f.close()
    return hashlib.sha256(seed).hexdigest()

class Client:
    def __init__(self, name, secret):
        self.name = name
        self.secret = secret
        self.token = ""
        self.nonce = ""
    def make_challenge(self):
        self.nonce = make_nonce()
        auth_message = auth_pb2.AuthMessage()
        auth_message.name = self.name
        auth_message.type = auth_pb2.AuthMessage.CHALLENGE
        auth_message.nonce = self.nonce
        return auth_message
    def verifyRequest(self, request):
        pass

clients_by_name = {"isaac": Client("isaac", "petes")}

class RumAuthServer:

    def __init__(self,clients = {}, zmq_spec="tcp://*:5000")
        self.zmq_spec = zmq_spec
        self.clients = clients
    def make_error(message, name="Unknown"):
        error_message = auth_pb2.AuthMessage()
        error_message.name = name
        error_message.type = auth_pb2.AuthMessage.ERROR
        error_message.error_message = message
        return error_message

    def handle_hello(hello_message):
        name = hello_message.name
        if name in clients_by_name:
            return clients_by_name[name].make_challenge()
        else:
            return  make_error("Client %s does not exist" % name, name)

    def handle_response(response):
        if response.name in clients_by_name:
            client = clients_by_name[response.name]
            if response.response == hashlib.sha256(client.nonce + client.secret).hexdigest():
                token = make_nonce()
                token_message = auth_pb2.AuthMessage()
                token_message.name = response.name
                token_message.type = auth_pb2.AuthMessage.TOKEN 
                token_message.token = token
                client.token = token
                return token_message
                # Sweet. User authenicated
            else:
                return make_error("Failed to authenticated %s" % response.name,
                                  response.name)
        else:
            return  make_error("Client %s does not exist" % response.name,
                               response.name)

    def handle_error(error_message):
        print error_message.error_message


    handlers = {
        auth_pb2.AuthMessage.HELLO      : handle_hello,
        auth_pb2.AuthMessage.RESPONSE   : handle_response,
        auth_pb2.AuthMessage.ERROR      : handle_error
    }
    
    while True:
        # Receive a "packet"
        data = auth.recv()
        auth_message = auth_pb2.AuthMessage()

        # Parse into object
        auth_message.ParseFromString(data)

        # handle request
        handler = handlers[auth_message.type]
        response = handler(auth_message)

        # send response
        auth.send(response.SerializeToString())

