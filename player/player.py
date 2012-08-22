import zmq, hashlib
context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://rum.mit.edu:5000")
SECRET = 'omgsecret'
def auth():
    socket.send("auth#isaac")

    challenge = socket.recv().split("#")
    if challenge[0] == "challenge":

        response = "response#" + challenge[1] + "#" + hashlib.sha256(challenge[1] +
                                                SECRET).hexdigest()
        socket.send(response)
        print socket.recv()



auth()
