#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""


**************************
文件:     index.py
 IDE：    PyCharm
创建时间： 2019/5/24 17:45
@author： skymoon
"""

from model.admin import Admin


def main():
    user = input("username: ")
    psw = input("password: ")
    admin = Admin()
    result = admin.check_validate(user, psw)
    if not result:
        print("用户名或密码错误！")
    else:
        print("进入后台管理页面！")


if __name__ == "__main__":
    main()
