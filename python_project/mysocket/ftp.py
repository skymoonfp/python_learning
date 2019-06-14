#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""


**************************
文件:     ftp.py
 IDE：    PyCharm
创建时间： 2019/5/26 16:45
@author： skymoon
"""

import os
import socket
import socketserver
import time


class FtpTransaction(object):

    def __init__(self, cmd, path, size, sk):

        self.cmd = cmd
        self.path = path
        self.size = size
        self.sk = sk

    def sending(self):

        send_size = 0
        with open(self.path, "rb") as f:
            while True:
                if send_size + 1024 > self.size:
                    data = f.read(self.size - send_size)
                    self.sk.send(data)
                else:
                    data = f.read(1024)
                    self.sk.send(data)
                    send_size += 1024

    def receive(self):

        recv_size = 0
        with open(self.path, "wb") as f:
            while True:
                if self.size > recv_size:
                    data = self.sk.recv(1024)
                    recv_size += len(data)
                    f.write(data)
                else:
                    break


class MyFtpServer(socketserver.BaseRequestHandler):
    """Ftp server.

    """

    def handle(self):
        print("connected...")
        self.request.send("connected...\nrequest like this: cmd | path".encode())

        self.judgement_mode()

    def client_exit_check(self, recv_data):

        if recv_data == "exit":
            return False
        else:
            return recv_data

    def path_analysis(self, recv_data):

        cmd, file_name, size = recv_data.split("|")
        base_path = "E:\\DataAnalysis\\python_temp"
        path = os.path.join(base_path, file_name)
        return cmd, path, size

    def file_exist(self, cmd, path):

        while True:
            if cmd == "upload":
                if os.path.exists(path):
                    file_name = os.path.basename(path)
                    file_size = os.stat(path).st_size
                    return file_name, file_size
                else:
                    print("文件不存在！请重新选择！")
                    cmd, path = self.input_check()
            elif cmd == "download":
                if os.path.exists(path):
                    print("文件已存在！请重新选择！")
                    cmd, path = self.input_check()
                else:
                    file_name = os.path.basename(path)
                    file_size = os.stat(path).st_size
                    return file_name, file_size

    def input_check(self):

        while True:
            input_path = input("path: ")
            if input_path != "exit":
                try:
                    cmd, path = input_path.split("|")
                except ValueError as e:
                    err = "ValueError: " + str(e)
                    print(err)
                    continue
                else:
                    if cmd not in ["upload", "download"]:
                        print("'cmd' error!")
                        continue
                    else:
                        return cmd, path
            else:
                return False

    def judgement_mode(self):
        pass


class MyFtpClient(object):
    """Ftp client.

    All inquiry to user is made independently by client, such as whether exit or not.

    All functions that can be realized by client independently is also only made by client.

    Only information couldn't acquire from local send to server for feedback,

    namely only information that is necessity for server is sent to server for processing,

    such as "exit" and regular file path.

    """

    def __init__(self, *ip_port):

        self.ip_port = ip_port

    def connection(self):

        sk = socket.socket()
        sk.connect(self.ip_port)
        return sk

    def recv_judge(self, sk):

        recv_data = sk.recv(1024).decode()
        time.sleep(1)
        if not recv_data:
            return False
        else:
            print(recv_data)
            return recv_data

    def input_check(self):

        while True:
            input_path = input("path: ")
            if input_path != "exit":
                try:
                    cmd, path = input_path.split("|")
                except ValueError as e:
                    err = "ValueError: " + str(e)
                    print(err)
                    continue
                else:
                    if cmd not in ["upload", "download"]:
                        print("'cmd' error!")
                        continue
                    else:
                        return cmd, path
            else:
                return False

    def file_exist(self, cmd, path, sk):

        while True:
            if cmd == "upload":
                self.upload(path, sk)
            elif cmd == "download":
                if os.path.exists(path):
                    print("文件已存在！请重新选择！")
                    cmd, path = self.input_check()
                else:
                    file_name = os.path.basename(path)
                    file_size = os.stat(path).st_size
                    return file_name, file_size

    def upload(self, path, sk):

        if os.path.exists(path):
            file_name = os.path.basename(path)
            file_size = os.stat(path).st_size
            sk.send("upload | file_name | file_size".encode())
            self.recv_judge(sk)  ############
            return file_name, file_size
        else:
            print("文件不存在！请重新选择！")
            return False

    def go_on(self, sk):
        while True:
            choise = input("continue? (y/n)")
            if choise == "y":
                return True
            elif choise == "n":
                sk.send("exit".encode())
                return False
            else:
                continue

    def __call__(self):

        sk = self.connection()

        recv_data = self.recv_judge(sk)

        # 没有收到数据的原因只能是服务器在等待，等待的原因可能是等待客户input，也可能是等待客户upload文件，怎么识别这两者呢？假设一开始由服务器发送数据，则一开始能收到数据，这个时候如果调用input，服务器是会等待的，如果input后服务器有返回，表示input有问题，如果无返回，表示input无问题，可以upload。即upload状态下的服务器等待始终判定为等待load。
        cmd = ""
        path = ""

        if recv_data:
            input_data = self.input_check()
            if input_data:
                cmd, path = input_data
            else:
                sk.send("exit".encode())
                sk.close()
        else:  # 第一次调用肯定能收到数据
            pass

        file_name, size = self.file_exist(cmd, path)
        sk.send((cmd + "|" + file_name + "|" + str(size)).encode())

        while True:
            recv_data = self.recv_judge(sk)
            if not recv_data:
                ft = FtpTransaction(cmd, path, size, sk)
                if cmd == "upload":
                    ft.sending()
                    print("upload succeed.")
                    choise = self.go_on(sk)
                    if choise:
                        continue
                    else:
                        sk.close()
                elif cmd == "download":
                    ft.receive()
                    print("download succeed.")
                    choise = self.go_on(sk)
                    if choise:
                        continue
                    else:
                        sk.close()
            else:
                input_data = self.input_check()
                if input_data:
                    cmd, path = input_data
                else:
                    sk.send("exit".encode())
                    sk.close()
                file_name, size = self.file_exist(cmd, path)
                sk.send((cmd + "|" + file_name + "|" + str(size)).encode())
