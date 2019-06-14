#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""


**************************
文件:     lock.py
 IDE：    PyCharm
创建时间： 2019/5/27 10:39
@author： skymoon
"""

import threading
import time

num = 0
num2 = 0


def run(n):
    global num, num2
    time.sleep(1)

    samp.acquire()  # 加锁
    time.sleep(0.01)
    # lock.acquire()
    num += 1
    # samp.acquire()

    # num2 += 2
    print("%s" % num)
    # print("Second: %s\n" % num2)
    # samp.release()
    # time.sleep(1)
    # num += 1
    # num2 += 2
    # print("Third: %s\n" % num)
    # print("Fourth: %s\n" % num2)
    samp.release()  # 释放

    time.sleep(0.01)
    # print("%s\n" % num)


# run("dd")
# print(num)

# lock = threading.Lock()
# lock = threading.RLock()
samp = threading.BoundedSemaphore(2)

for i in range(1000):
    t = threading.Thread(target=run, args=[i, ])
    t.start()
