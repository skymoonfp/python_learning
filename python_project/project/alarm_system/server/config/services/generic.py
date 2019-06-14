#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""


**************************
文件:     generic.py
 IDE：    PyCharm
创建时间： 2019/5/29 18:25
@author： skymoon
"""


class BaseService(object):
    def __init__(self):
        self.name = "BaseService"
        self.interval = 300
        self.last_time = 0
        self.plugin_name = "your_plugin_name"
        self.triggers = {}
