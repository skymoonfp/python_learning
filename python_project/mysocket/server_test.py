#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""


**************************
文件:     server_test.py
 IDE：    PyCharm
创建时间： 2019/5/24 20:55
@author： skymoon
"""

import socket

server = socket.socket()
server.bind(("localhost", 6666))
server.listen(5)

while True:
    conn, addre = server.accept()
    message = "小丽：您好！".encode()
    conn.send(message)
    flag = True
    while flag:
        recv_data = conn.recv(1024).decode()
        print(recv_data)
        if recv_data == "exit":
            flag = False
        conn.send("小丽：sb".encode())
    conn.close()
