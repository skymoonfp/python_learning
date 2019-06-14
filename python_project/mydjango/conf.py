#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""


**************************
文件:     conf
 IDE：    PyCharm
创建时间： 2019/6/3 10:26
@author： skymoon
"""


def login():
    return "登陆界面"


def index():
    return "主页"


url = (
    ("/index/", index),
    ("/login/", login)
)
