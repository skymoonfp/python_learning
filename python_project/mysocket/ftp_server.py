#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""


**************************
文件:     ftp_server.py
 IDE：    PyCharm
创建时间： 2019/5/26 10:22
@author： skymoon
"""

import os
import socketserver


class MyServer(socketserver.BaseRequestHandler):

    def handle(self):
        pass


class MyFTPServer(MyServer):

    def handle(self):
        base_path = "E:\\DataAnalysis\\python_temp"
        conn = self.request
        print("connected...")
        while True:
            pre_data = conn.recv(1024).decode()

            if pre_data == "exit":
                print("user already disconnected...")
                break

            # 获取请求方法、文件名、文件大小
            print(pre_data)
            cmd, file_name, file_size = pre_data.split("|")

            # 已经接收文件大小
            recv_size = 0

            # 上传文件路径拼接
            file_dir = os.path.join(base_path, file_name)
            with open(file_dir, "wb") as f:
                flag = True
                while flag:
                    # 未上传完毕
                    if int(file_size) > recv_size:
                        data = conn.recv(1024)
                        recv_size += len(data)
                        f.write(data)
                        # print(data.decode("utf-8", "ignore"))
                    else:
                        flag = False
            print("upload succeed.")


instance = socketserver.ThreadingTCPServer(("127.0.0.1", 8888), MyFTPServer)
instance.serve_forever()
