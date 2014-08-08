#!/usr/bin/python

import socket

PORT=8081
HOST=''
TIMEOUT=.001

# Chat client class
# for sending text
# to the chat server
class ChatClient:
    def __init__(self):
        self.s = socket.socket()
        self.s.connect((HOST,PORT))
        self.s.settimeout(TIMEOUT)
    def send(self, data):
        if (len(data) > 0):
            self.s.send(data)
    def recv(self):
        data = ''
        try:
            data = self.s.recv(20)
        except:
            data = ''
        return data
