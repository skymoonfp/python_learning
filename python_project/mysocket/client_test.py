#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""


**************************
文件:     client_test.py
 IDE：    PyCharm
创建时间： 2019/5/24 20:59
@author： skymoon
"""

import socket

client = socket.socket()

ip_port = ("localhost", 6666)
client.connect(ip_port)

while True:
    data = client.recv(1024).decode()
    print(data)
    inp = input("clend：")
    client.send(inp.encode())
    if inp == "exit":
        break
