import zmq, hashlib, auth_pb2
context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://rum.mit.edu:5000")
SECRET = 'pete'
def auth():
    auth_message = auth_pb2.AuthMessage()
    auth_message.type = auth_pb2.AuthMessage.HELLO
    auth_message.name = "isaac"
    socket.send(auth_message.SerializeToString())

    data = socket.recv()
    
    challenge = auth_pb2.AuthMessage()
    challenge.ParseFromString(data)
    
    if challenge.type != auth_pb2.AuthMessage.CHALLENGE:
        raise Exception("Unexpected resposne from server")
    else:
        response = auth_pb2.AuthMessage()
        response.response.response = hashlib.sha256(challenge.nonce + SECRET ).hexdigest()
        socket.send(response.SerializeToString())

    data = socket.recv()
        
    

auth()
