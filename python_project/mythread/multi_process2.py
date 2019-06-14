#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""


**************************
文件:     multiprocess2.py
 IDE：    PyCharm
创建时间： 2019/5/27 20:24
@author： skymoon
"""

import os
import time
from multiprocessing import Process


def info(title):
    print(title)
    print("module name:", __name__)
    if hasattr(os, "getppid"):  # only available on Unix
        print("parent process:", os.getppid())
    # time.sleep(5)
    print("process id:", os.getpid())


def f(name):
    info("function f")
    time.sleep(10)
    print("hello", name)


def f2(name):
    info("function f")
    time.sleep(5)
    print("hello", name)


if __name__ == "__main__":
    info("main line")
    print("---------------------------")
    p = Process(target=f, args=("bob",))
    p.start()
    # p.join()
    p = Process(target=f2, args=("pop",))
    p.start()
    f("bs")
    f2("sb")
