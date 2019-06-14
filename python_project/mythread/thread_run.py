#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""


**************************
文件:     thread_run.py
 IDE：    PyCharm
创建时间： 2019/5/26 22:41
@author： skymoon
"""

import time
from threading import Thread


class MyThread(Thread):

    def run(self):
        time.sleep(5)
        print("我是线程！")
        time.sleep(5)

        # # method one
        # try:
        #     if self._target:
        #         self._target(*self._args, **self._kwargs)
        # finally:
        #     del self._target, self._args, self._kwargs

        # method two
        Thread.run(self)

        time.sleep(2)

        print("我是线程！")


def bar():
    print("bar")


t1 = MyThread(target=bar)
t1.start()
t1.join(7)
print("over")
