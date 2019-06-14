#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""


**************************
文件:     client.py
 IDE：    PyCharm
创建时间： 2019/5/25 17:50
@author： skymoon
"""

import os
import socket
import time


def pre_install():
    with open("..\\files\\data_not_wait_response.txt", "w", encoding="utf-8") as file:
        file.write("Two passwords is not same! Try again! OK?\n")
        file.write("登陆成功！Go on！\n")
        file.write("You have become a member of us! Have your fun!\n")
        file.write("The account is already exiting!\n")


client = socket.socket()

ip_port = ("localhost", 9999)
client.connect(ip_port)

if os.path.exists("..\\files\\data_not_wait_response.txt"):
    pass
else:
    pre_install()

with open("..\\files\\data_not_wait_response.txt", "r", encoding="utf-8") as file:
    data_not_wait_response = file.read().split("\n")

while True:
    data = client.recv(1024).decode()
    print(data)

    # if data == "Two passwords is not same! Try again! OK?":
    #     time.sleep(0.5)
    # elif data == "登陆成功！Go on！":
    #     time.sleep(0.5)
    # elif data == "You have become a member of us! Have your fun!":
    #     time.sleep(0.5)

    if data in data_not_wait_response:
        time.sleep(0.5)
    else:
        inp = input("【我】")
        client.send(inp.encode())
        if inp == "exit":
            break
