#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""


**************************
文件:     html_test.py
 IDE：    PyCharm
创建时间： 2019/5/31 15:50
@author： skymoon
"""

import socket


def handle_request(client):
    buf = client.recv(1024)
    # client.send("HTTP/1.1 200 OK\r\n".encode())
    # client.send("Content-Type:text/html\r\n\r\n".encode())
    client.send("<a href='www.baidu/com'> Hello! </a>".encode())


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(("localhost", 6666))
    sock.listen(5)

    while True:
        conn, addr = sock.accept()
        handle_request(conn)
        conn.close()


if __name__ == "__main__":
    main()
