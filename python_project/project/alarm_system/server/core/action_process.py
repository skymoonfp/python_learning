#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""


**************************
文件:     action_process.py
 IDE：    PyCharm
创建时间： 2019/5/30 下午8:10
@author： skymoon
"""

import pickle

from server.core import serialize


def action_process(server_instance, msg):  # 第8步：处理客户端主机发布的监控信息

    msg = pickle.loads(msg[2])  # 第8.1步：将客户端主机发布的监控信息反序列化
    print(msg)
    func_name = list(msg.keys())[0]
    func = getattr(serialize, func_name)

    func(server_instance, msg[func_name])
