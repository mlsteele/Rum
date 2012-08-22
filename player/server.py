import zmq
context = zmq.Context()
sub  = context.socket(zmq.SUB)
sub.bind("tcp://*:5000")
sub.setsockopt(zmq.SUBSCRIBE, "update")


while True:
    message = sub.recv()
    messages = message.split(":")
    print messages[1]
