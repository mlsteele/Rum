import zmq
context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.bind("tcp://127.0.0.1:5000")
socket.setsockopt(zmq.SUBSCRIBE, "update")


while True:
    message = socket.recv()
    messages = message.split(":")
    print messages[1]
