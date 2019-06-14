#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""


**************************
文件:     socket_server_test.py
 IDE：    PyCharm
创建时间： 2019/5/25 1:08
@author： skymoon
"""

import socketserver


class MyServer(socketserver.BaseRequestHandler):

    def setup(self):
        pass

    def handle(self):
        print(self.request, self.client_address, self.server, sep="\n\n", end="\n\n")
        conn = self.request
        addre = self.client_address
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

    def finish(self):
        pass


if __name__ == "__main__":
    server = socketserver.ThreadingTCPServer(('127.0.0.1', 6666), MyServer)
    server.serve_forever()
