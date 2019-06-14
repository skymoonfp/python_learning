#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""


**************************
文件:     pool_test.py
 IDE：    PyCharm
创建时间： 2019/5/28 2:34
@author： skymoon
"""

import os
import time
from multiprocessing import Pool
from threading import *


def f(x):
    return x * x


def main1():
    with Pool(processes=4) as pool:  # start 4 worker processes
        result = pool.apply_async(f, (10,))  # evaluate "f(10)" asynchronously in a single process
        print(result.get(timeout=1))  # prints "100" unless your computer is *very* slow

        print(pool.map(f, range(10)))  # prints "[0, 1, 4,..., 81]"

        it = pool.imap(f, range(10))
        print(next(it))  # prints "0"
        print(next(it))  # prints "1"
        print(it.next(timeout=1))  # prints "4" unless your computer is *very* slow

        result = pool.apply_async(time.sleep, (10,))
        print(result.get(timeout=1))  # raises multiprocessing.TimeoutError


def main2():
    with Pool(processes=5) as pool:
        res_list = []
        for i in range(100):
            res = pool.apply_async(f, [i, ])
            # res = pool.apply_async(target=f, args=[i, ])

            print("—————：", i)
            res_list.append(res)

        for r in res_list:
            print(r.get(timeout=1))

        # ——————————————————————
        print(pool.map(f, range(100)))


def thread_func(lis, n):
    print("thread: %d <-- %s" % (n, os.getpid()))


def f2(x):
    info_list = []
    for i in range(10):
        thread = Thread(target=thread_func, args=[info_list, i])
        thread.start()


def main3():
    with Pool(processes=5) as pool:
        res_list = []
        for i in range(100):
            res = pool.apply_async(f2, [i, ])
            # res = pool.apply_async(target=f, args=[i, ])

            print("—————：", i)
            res_list.append(res)

        for r in res_list:
            print(r.get(timeout=1))


if __name__ == '__main__':
    # main1()
    # main2()
    main3()
