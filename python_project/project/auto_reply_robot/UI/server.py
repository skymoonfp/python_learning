#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""


**************************
文件:     server.py
 IDE：    PyCharm
创建时间： 2019/5/25 17:42
@author： skymoon
"""

import socketserver

from BLL.client_server_interaction import Interact
from BLL.user_action import RegAndLog


class MyServer(socketserver.BaseRequestHandler):

    def setup(self):
        pass

    def handle(self):
        print(self.request, self.client_address, self.server, sep="\n\n", end="\n\n")
        r_l = RegAndLog(self.request, self.client_address, self.server)
        username, password = r_l()
        c_s = Interact(self.request, self.client_address, self.server, username, password)
        c_s()
        self.request.close()

    def finish(self):
        pass


def server_on():
    server = socketserver.ThreadingTCPServer(('127.0.0.1', 9999), MyServer)
    server.serve_forever()


if __name__ == "__main__":
    server_on()
