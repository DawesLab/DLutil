"""
A client for the camserver
"""
import zmq

REQUEST_TIMEOUT = 25000
SERVER_ENDPOINT = "tcp://localhost:5555"

context = zmq.Context()

#  Socket to talk to server
print("Connecting to array server...")
client = context.socket(zmq.REQ)
client.connect(SERVER_ENDPOINT)

poll = zmq.Poller()
poll.register(client, zmq.POLLIN)

def request_images(client,N=1):
    """Send a ZMQ request for data"""
    shots_requested = N
    request = str(shots_requested)  # ask for one shot of data
    #print "I: Sending (%s)" % request

    client.send(request)


def recv_array(socket, flags=0, copy=False, track=False):
    """Recieve a numpy array from ZMQ server"""
    md = socket.recv_json(flags=flags)
    msg = socket.recv(flags=flags, copy=copy, track=track)
    buf = buffer(msg)
    A = frombuffer(buf, dtype=md['dtype'])
    return A.reshape(md['shape'])


def open_images():
    """Open data sent from camserver as a data array"""
    socks = dict(poll.poll(REQUEST_TIMEOUT))
    if socks.get(client) == zmq.POLLIN:
        data_array = recv_array(client)
        #reply = client.recv()

        if len(data_array) > 1:  # TODO test for the right size array
            #print "I: Server replied OK: " + str(data_array.shape)
            return data_array

        else:
            # print "E: Malformed reply from server: %s" % reply
            print("E: no reply from server")
            return -1
