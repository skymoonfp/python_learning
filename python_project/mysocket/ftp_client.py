#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""


**************************
文件:     ftp.client.py
 IDE：    PyCharm
创建时间： 2019/5/26 9:42
@author： skymoon
"""

import os
import socket

ip_port = ("127.0.0.1", 8888)
sk = socket.socket()
sk.connect(ip_port)

flag = True
while flag:
    input_path = input("path: ")
    # cmd: 自命名，如upload(send), download(get)
    # path: 路径
    # (e.g.)upload|E:\DataAnalysis\python_project\data_files\replace_test.txt
    cmd, path = input_path.split("|")

    file_name = os.path.basename(path)
    file_size = os.stat(path).st_size
    sk.send((cmd + "|" + file_name + "|" + str(file_size)).encode())
    send_size = 0
    with open(path, "rb") as f:
        flag_1 = True
        while flag_1:
            if send_size + 1024 > file_size:
                data = f.read(file_size - send_size)
                flag_1 = False
            else:
                data = f.read(1024)
                send_size += 1024
            sk.send(data)

    flag_2 = True
    while flag_2:
        choise = input("continue? (y/n)")
        if choise == "y":
            flag_2 = False
        elif choise == "n":
            flag_2 = False
            flag = False
            sk.send("exit".encode())
        else:
            continue

sk.close()
