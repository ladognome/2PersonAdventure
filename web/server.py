#!/usr/bin/python

import socket

PORT=8082
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
		conn, addr = s.accept()
	except:
		pass
	else:
		clients.append(conn)
	# Check all clients for
	# data being sent.
	for conn in clients:
		data = conn.recv(20)
		# if data was sent, then send
		# the data to everyone else.
		if (len(data) > 0):
			for conn in clients:
				try:
					conn.send(data)
				except:
					conn.close()
					clients.remove(conn)
	# Continue

#	while data != "":
#		conn.send(data)
#		data = conn.recv(20)
