#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""


**************************
文件:     hosts.py
 IDE：    PyCharm
创建时间： 2019/5/29 16:51
@author： skymoon
"""

from server.config import templates

g1 = templates.LinuxTemplate()
g1.group_name = "Test groups"
g1.hosts = ["192.168.23.123", "10.165.13.233", "192.168.1.135"]

# ---------------------


g2 = templates.LinuxTemplate()
g2.group_name = "puppet server groups"
g2.hosts = ["202.123.12.111", "10.112.11.231", "10.165.13.233", "192.168.1.135"]

monitored_groups = [g1,
                    g2]

# print(monitored_groups)
