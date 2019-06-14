#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""


**************************
文件:     client_server_interaction.py
 IDE：    PyCharm
创建时间： 2019/5/25 17:54
@author： skymoon
"""

import pickle
import time

from model.auto_reply import AutoReplyRobot


class Interact(object):

    def __init__(self, request, client_address, server, username, password):

        self.request = request
        self.client_address = client_address
        self.server = server
        self.username = username
        self.password = password

    def receive(self, file_name):
        """Receive data from client and show it on screen."""

        recv_data = self.request.recv(1024).decode()
        recv_data = "【我】" + recv_data
        print(recv_data)
        self.save(recv_data, file_name)
        return recv_data

    def response(self, recv_data):
        """According to data received, return proper data."""

        arr = AutoReplyRobot(recv_data)
        send_data = arr()

        return send_data

    def sending(self, message, file_name):
        """Send data to client and show it on screen."""

        send_data = "【蕾姆】" + str(message)
        print(send_data)
        self.save(send_data, file_name)
        self.request.send(send_data.encode())

    # def file_temp(self):
    #     """Create temp file to save data receiving from client or sending from server."""
    #
    #     i = 1
    #     while True:
    #         file_name = "files\\user_temp_" + str(i).zfill(3) + ".txt"
    #         if os.path.exists(file_name):
    #             i = i + 1
    #         else:
    #             break
    #
    #     # 初始化文件内容，写入request, client_address, server
    #     with open(file_name, "ab+") as file:
    #         pickle.dump(self.request, file)
    #         pickle.dump(self.client_address, file)
    #         pickle.dump(self.server, file)
    #
    #     return file_name

    def user_file(self):
        """Create user_file to save data receiving from client or sending from server."""

        file_name = "files\\users_interaction\\" + self.username + ".txt"

        with open(file_name, "ab+") as file:
            pickle.dump(str(self.request), file)
            pickle.dump(str(self.client_address), file)
            pickle.dump(str(self.server), file)

        return file_name

    def save(self, data, file_name):
        """Save data receiving from client in files."""

        current_time = time.ctime()
        data_dict = dict()
        data_dict[current_time] = data
        with open(file_name, "ab+") as file:
            pickle.dump(data_dict, file)

    # def file_temp_rename(self):
    #     pass

    def __call__(self):

        file_name = self.user_file()

        self.sending("主人，您好！我是蕾姆！请问有什么可以为您效劳的吗？", file_name)

        while True:
            recv_data = self.receive(file_name)
            if recv_data == "exit":
                return
            send_data = self.response(recv_data)
            self.sending(send_data, file_name)
