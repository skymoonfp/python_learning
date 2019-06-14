#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""


**************************
文件:     producer_consumer.py
 IDE：    PyCharm
创建时间： 2019/5/26 23:27
@author： skymoon
"""

import time
from queue import Queue
from threading import Thread


class Producer(Thread):

    def __init__(self, name1, queue):
        """

        :param name1: 生产者名单
        :param queue: 容器
        """
        self.__name = name1
        self.__queue = queue
        Thread.__init__(self)

    def run(self):
        while True:
            if self.__queue.full():
                time.sleep(20)
            else:
                self.__queue.put("产品")
                print(time.time(), ":%s(%s)生产了一个产品" % (self.__name, self._name))
                time.sleep(1)
        # Thread.run(self)


class Consumer(Thread):

    def __init__(self, name1, queue):
        """

        :param name1: 消费者名单
        :param queue: 容器
        """
        self.__name = name1
        self.__queue = queue
        Thread.__init__(self)

    def run(self):
        while True:
            if self.__queue.empty():
                time.sleep(10)
            else:
                self.__queue.get("产品")
                print(time.time(), ":%s(%s)消费了一个产品" % (self.__name, self._name))
                time.sleep(5)
        # Thread.run(self)


que = Queue(10)
zs = Producer("zhangsan", que)
zs.start()
ls = Producer("lisi", que)
ls.start()
ww = Producer("wangwu", que)
ww.start()

for i in range(20):
    name = "xiaoming%d" % (i,)
    temp = Consumer(name, que)
    temp.start()

# print(que.qsize())
# que.put("a")
# que.put("b")
# print(que.empty())
# print(que.qsize())
# print(que.get())
# print(que.qsize())
# print(que.get())
# print(que.empty())
