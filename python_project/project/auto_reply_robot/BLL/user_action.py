#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""


**************************
文件:     user_action.py
 IDE：    PyCharm
创建时间： 2019/5/25 19:26
@author： skymoon
"""

from model.users_log import UsersLog


class RegAndLog(object):

    def __init__(self, request, client_address, server):

        self.request = request
        self.client_address = client_address
        self.server = server

    def log(self):

        userlog = UsersLog()

        self.request.send("username: ".encode())
        user = self.request.recv(1024).decode()
        self.request.send("password: ".encode())
        psw = self.request.recv(1024).decode()

        result = userlog.check_validate(user, psw)

        if not result:
            self.request.send("用户名或密码错误！注册（R）还是继续尝试（T）：".encode())
            choise = self.request.recv(1024).decode()
            while True:
                if choise == "R":
                    self.reg()
                    return
                elif choise == "T":
                    return self.log()
                else:
                    self.request.send("抉择有误！注册（R）还是继续尝试（T）：".encode())
                    choise = self.request.recv(1024).decode()
        else:
            self.request.send("登陆成功！Go on！".encode())
            # self.request.recv(1024).decode()
            return user, psw

    def reg(self):

        userlog = UsersLog()

        self.request.send("username: ".encode())
        user = self.request.recv(1024).decode()
        self.request.send("password: ".encode())
        psw = self.request.recv(1024).decode()
        self.request.send("password again: ".encode())
        psw2 = self.request.recv(1024).decode()

        if psw == psw2:
            if userlog.registration(user, psw):
                self.request.send("You have become a member of us! Have your fun!".encode())
                return
            else:
                self.request.send("The account is already exiting!".encode())
                return
        else:
            self.request.send("Two passwords is not same! Try again! OK?".encode())
            # self.request.recv(1024).decode()
            self.reg()

    def __call__(self):

        while True:
            self.request.send("登陆（1）还是注册（0）：".encode())
            choise = self.request.recv(1024).decode()
            if choise == "1":
                return self.log()
            elif choise == "0":
                self.reg()
                continue
            else:
                self.request.send("error!".encode())
