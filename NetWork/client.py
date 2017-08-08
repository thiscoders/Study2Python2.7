# coding=utf-8
# !/usr/bin/env python2.7

import socket

s=socket.socket()
host=socket.gethostname()
port=32201

s.connect((host,port))
print s.recv(1024)
s.close()

