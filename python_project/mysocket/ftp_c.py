#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""


**************************
文件:     ftp_c.py
 IDE：    PyCharm
创建时间： 2019/5/26 20:25
@author： skymoon
"""

from mysocket import ftp

if __name__ == "__main__":
    client = ftp.MyFtpClient("127.0.0.1", 8888)
    client()
