#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""


**************************
文件:     multi_pro_lock.py
 IDE：    PyCharm
创建时间： 2019/5/28 0:18
@author： skymoon
"""

from multiprocessing import Process, Lock


def f(l, i):
    l.acquire()
    print("hello", i)
    l.release()


if __name__ == "__main__":

    lock = Lock()
    for num in range(10):
        Process(target=f, args=(lock, num)).start()
