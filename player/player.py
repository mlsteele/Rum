import zmq
context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.connect("tcp://127.0.0.1:5000")
while True:
    message = raw_input("Message: ")
    socket.send("update:" + message)
