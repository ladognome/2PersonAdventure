#!/usr/bin/python

import socket
import sys

PORT=8081
HOST=''

s = socket.socket()
s.bind((HOST,PORT))
s.listen(12)
s.settimeout(.001)

# keep a list of connected clients
# and let them contact each other.
clients = []

# just be an echo server.
while 1:
    try:
        sys.stdout.write("\rWaiting for conn.")
        conn, addr = s.accept()
    except:
        pass
    else:
        print "adding conn:", conn
        clients.append(conn)
        conn.settimeout(.001)
    # Check all clients for
    # data being sent.
    for conn in clients:
        print "checking conn:", conn
        data = ''
        try:
            data = conn.recv(20)
        except:
            pass
        # if data was sent, then send
        # the data to everyone else.
        if (len(data) > 0):
            print "received data from:", conn
            for conn2 in clients:
                if (conn != conn2):
                    try:
                        print "sending data:", conn2
                        conn2.send(data)
                    except:
                        print "removing conn:", conn2
                        conn2.close()
                        clients.remove(conn)
    # Continue

#    while data != "":
#        conn.send(data)
#        data = conn.recv(20)
