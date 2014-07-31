#!/usr/bin/python

import socket
import threading
import sys

PORT=8081
HOST=''

class receiveComm(threading.Thread):
    def __init__(self, s):
        threading.Thread.__init__(self)
        self.s = s
        self.done = threading.Event()
    def run(self):
        # check to see if the main
        # thread wants us to stop.
        while not self.stopped():
            # check to see if we received any
            # data from the network.
            try:
                data = self.s.recv(20)
            #If not, then just keep waiting for data.
            except:
                continue
            #If so, then print it out.
            sys.stdout.write(data)
            sys.stdout.flush()
    # Allow the calling thread to stop
    # this thread.
    def stop(self):
        self.done.set()
    # Signal this thread that it has
    # been stopped.
    def stopped(self):
        return self.done.isSet()

# Set up the socket connection.
s = socket.socket()
s.connect((HOST,PORT))
s.settimeout(.001)

# setup the network thread.
recvThread = receiveComm(s)
recvThread.start()

while 1:
    data = raw_input()
    if data.strip() == "exitNow":
        print "Exiting..."
        break
    data += "\n"
    s.send(data)

print "Stopping thread..."
recvThread.stop()
