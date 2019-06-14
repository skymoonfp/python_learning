#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""


**************************
文件:     multi_pro_queue.py
 IDE：    PyCharm
创建时间： 2019/5/27 21:09
@author： skymoon
"""

from multiprocessing import Process
from queue import Queue as Que2


def f(q, n):
    q.put([n, "hello"])
    print(q.get())


if __name__ == "__main__":

    # q1 = Que1()
    # for i in range(5):
    #     p = Process(target=f, args=(q1, i))
    #     p.start()
    # while True:
    #     print(q1.get())

    q2 = Que2(10)
    q2.put("ddd")
    print(q2)
    for i in range(5):
        p = Process(target=f, args=(q2, i))
        p.start()
    # while True:
    #     print(q2.get())
