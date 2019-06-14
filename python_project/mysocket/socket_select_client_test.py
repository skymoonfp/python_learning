#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""


**************************
文件:     socket_select_client_test.py
 IDE：    PyCharm
创建时间： 2019/5/28 20:05
@author： skymoon
"""

import socket
import sys


def socket_select_client():
    messages = ['This is the message. ',
                'It will be sent ',
                'in parts.',
                ]
    server_address = ('localhost', 10000)

    # Create a TCP/IP socket
    socks = [socket.socket(socket.AF_INET, socket.SOCK_STREAM),
             socket.socket(socket.AF_INET, socket.SOCK_STREAM),
             ]

    # Connect the socket to the port where the server is listening
    print('connecting to %s port %s' % server_address, file=sys.stderr)
    for s in socks:
        s.connect(server_address)

    for message in messages:

        # Send messages on both sockets
        for s in socks:
            print('%s: sending "%s"' % (s.getsockname(), message), file=sys.stderr)
            s.send(message.encode())

        # Read responses on both sockets
        for s in socks:
            data = s.recv(1024).decode()
            print('%s: received "%s"' % (s.getsockname(), data), file=sys.stderr)
            if not data:
                print('closing socket', s.getsockname(), file=sys.stderr)


if __name__ == "__main__":
    socket_select_client()
