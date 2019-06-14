#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""


**************************
文件:     socket_test.py
 IDE：    PyCharm
创建时间： 2019/5/24 20:10
@author： skymoon
"""

import socket


def handle_request(client):
    buf = client.recv(1024)
    client.send("HTTP/1.1 200 OK\r\n\r\n".encode())
    client.send("Hello!".encode())


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(("localhost", 8088))
    sock.listen(5)

    while True:
        connection, address = sock.accept()
        handle_request(connection)
        connection.close()


if __name__ == "__main__":
    main()
