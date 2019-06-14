#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""


**************************
文件:     thread_test.py
 IDE：    PyCharm
创建时间： 2019/5/26 22:09
@author： skymoon
"""

import time
from threading import Thread


def foo(arg, v):
    print(arg)
    for i in range(10):
        print(i)
        time.sleep(1)


print("before")

t1 = Thread(target=foo, args=("dfew", 11,))
t1.setDaemon(True)
t1.start()
print(t1.getName())
t1.join(4)

time.sleep(3)
print("after")
