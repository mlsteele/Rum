import zmq, hashlib, auth_pb2
context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://rum.mit.edu:5000")
SECRET = 'omgsecret'
def auth():
    auth_message = auth_pb2.AuthMessage()
    auth_message.type = auth_pb2.AuthMessage.HELLO
    hello = auth_pb2.HelloMessage()
    auth_message.hello.name = "isaac"
    socket.send(auth_message.SerializeToString())

    data = socket.recv()
    response_auth_message = auth_pb2.AuthMessage()
    response_auth_message.ParseFromString(data)
    print response_auth_message
auth()
