#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""


**************************
文件:     ftp_s.py
 IDE：    PyCharm
创建时间： 2019/5/26 20:26
@author： skymoon
"""

import socketserver

from mysocket import ftp

if __name__ == "__main__":
    instance = socketserver.ThreadingTCPServer(("127.0.0.1", 8888), ftp.MyFtpServer)
    instance.serve_forever()
