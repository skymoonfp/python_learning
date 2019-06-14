#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""


**************************
文件:     socket_select_server_test.py
 IDE：    PyCharm
创建时间： 2019/5/28 17:32
@author： skymoon
"""

import queue
import socket
import sys

import select


def socket_select_server():
    # Create a TCP/IP socket
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setblocking(0)

    # Bind the socket to the port
    server_address = ("localhost", 10000)
    print("starting up on %s port %s" % server_address, file=sys.stderr)
    server.bind(server_address)

    # Listen for incoming connections
    server.listen(5)

    # Sockets from which we expect to read
    inputs = [server]

    # Sockets to which we expect to write
    outputs = []

    # Outgoing message queues (socket : Queue)
    message_queues = {}

    while True:

        # Wait at least one of the sockets to be ready for processing
        print("\nwaiting for the next event", file=sys.stderr)
        readable, writable, exceptional = select.select(inputs, outputs, inputs)

        # Handle inputs
        for s in readable:

            if s is server:
                # A "readable" server socket is ready to accept a connection
                connection, client_address = s.accept()
                print("new connection from", client_address, file=sys.stderr)
                connection.setblocking(0)
                inputs.append(connection)

                # Give the connection a queue for data we want to send
                message_queues[connection] = queue.Queue()

            else:
                data = s.recv(1024)
                if data:
                    # A readable client socket has data
                    print('received "%s" from %s' % (data, s.getpeername()), file=sys.stderr)
                    message_queues[s].put(data)
                    # Add output channel for response
                    if s not in outputs:
                        outputs.append(s)
                else:
                    # Interpret empty result as closed connection
                    print('closing', client_address, 'after reading no data', file=sys.stderr)
                    # Stop listening for input on the connection
                    if s in outputs:
                        outputs.remove(s)  # 既然客户端都断开了，我就不用再给它返回数据了，所以这时候如果这个客户端的连接对象还在outputs列表中，就把它删掉
                    inputs.remove(s)  # inputs中也删除掉
                    s.close()  # 把这个连接关闭掉

                    # Remove message queue
                    del message_queues[s]

        # Handle outputs
        for s in writable:
            try:
                next_msg = message_queues[s].get_nowait()
            except queue.Empty:
                # No messages waiting so stop checking for writability.
                print('output queue for', s.getpeername(), 'is empty', file=sys.stderr)
                outputs.remove(s)
            else:
                print('sending "%s" to %s' % (next_msg, s.getpeername()), file=sys.stderr)
                s.send(next_msg.upper())

        # Handle "exceptional conditions"
        for s in exceptional:
            print('handling exceptional condition for', s.getpeername(), file=sys.stderr)
            # Stop listening for input on the connection
            inputs.remove(s)
            if s in outputs:
                outputs.remove(s)
            s.close()

            # Remove message queue
            del message_queues[s]


if __name__ == "__main__":
    socket_select_server()
