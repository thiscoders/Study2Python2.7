# coding=utf-8
# !/usr/bin/env python2.7

import socket
s=socket.socket()
host=socket.gethostname()
port=32201
s.bind((host,port))

s.listen(5)
while True:
    c,addr=s.accept()
    print '连接地址：',addr
    c.send('Hello ,welcome!')
    c.close()
