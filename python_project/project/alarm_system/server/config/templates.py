#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""


**************************
文件:     templates.py
 IDE：    PyCharm
创建时间： 2019/5/29 16:52
@author： skymoon
"""

from server.config.services import linux


class BaseTemplate(object):
    def __init__(self):
        self.name = "YourTemplateName"
        self.group_name = "YourGroupName"
        self.hosts = []
        self.services = []


class LinuxTemplate(BaseTemplate):
    def __init__(self):
        super(LinuxTemplate, self).__init__()
        self.name = "LinuxTemplate"
        self.services = [
            linux.Cpu,
            linux.Memory
        ]
