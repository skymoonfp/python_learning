#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""


**************************
文件:     multi-process.py
 IDE：    PyCharm
创建时间： 2019/5/27 17:24
@author： skymoon
"""

import time
from multiprocessing import Pool
from threading import Thread

from mytime.timing import timer


def f(x):
    time.sleep(0.05)  # 无阻塞时，singleprocessing快；有阻塞时，multiprocessing快
    return x * x


@timer
def multiprocessing(n):
    with Pool(n) as p:
        a = p.map(f, list(range(100)))
    print(a)


@timer
def singleprocessing():
    a = list(map(f, list(range(100))))
    print(a)


class MyThread(Thread):

    def __init__(self, target, args):
        # Thread.__init__(self)
        super(MyThread, self).__init__()
        self.targer = target
        self.args = args
        self.result = self.targer(self.args)

    def get_result(self):
        return self.result


# @timer
# def multithreading():
#     a = []
#     for i in range(100):
#         for j in range(5):
#             t = MyThread(func=f, x=i)
#             t.start()
#             a.append(t.get_result())
#             i += 1
#     print(a)
#
# @timer
# def multithreading(n):
#     with Thread(n) as p:
#         a = p.map(f, list(range(100)))
#     print(a)
#
@timer
def multithreading():
    lis = list(range(100))
    threads = []
    for i in range(12):
        t = MyThread(target=f, args=lis[i])
        threads.append(t)
    for i in range(12):
        threads[i].start()
    for i in range(12):
        threads[i].join()
    for i in range(100):
        for j in range(12):
            print(threads[j].get_result())


if __name__ == '__main__':
    # multiprocessing(1)  # 5.28586483001709
    # print()
    # multiprocessing(5)  # 1.3174772262573242
    # print()
    multiprocessing(12)  # 1.148735761642456
    # print()
    # multiprocessing(20)  # 1.372330665588379
    # print()
    # singleprocessing()  # 5.072439432144165
    # print()
    multithreading()
