#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""


**************************
文件:     __main__.py
 IDE：    PyCharm
创建时间： 2019/5/30 11:27
@author： skymoon
"""

import sys

if 'client' not in sys.modules and __name__ == '__main__':
    pass

from client import client_

client_.main()
