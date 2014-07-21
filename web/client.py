#!/usr/bin/python

import socket

PORT=8082
HOST=''

s = socket.socket()
s.connect((HOST,PORT))

while 1:
	data = raw_input()
	s.send(data)
	data = s.recv(20)
	print data
