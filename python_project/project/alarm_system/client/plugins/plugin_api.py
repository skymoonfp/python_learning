#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""


**************************
文件:     plugin_api.py
 IDE：    PyCharm
创建时间： 2019/5/30 下午7:06
@author： skymoon
"""

from client.plugins import *


def get_load_info():
    return load.monitor()


def get_cpu_status():
    return cpu.monitor()


def get_memory_info():
    return memory.monitor()
