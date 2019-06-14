#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""


**************************
文件:     p_c.py
 IDE：    PyCharm
创建时间： 2019/5/27 9:33
@author： skymoon
"""

import queue
import random
import threading
import time


def producer(name, que):
    while True:
        if que.qsize() < 3:
            que.put("包子")
            print("%.2f：%s：生产了一个包子" % (time.time(), name))
        else:
            print("%.2f：包子还有！" % time.time())
        time.sleep(random.randrange(3))


def consumer(name, que):
    while True:
        try:
            que.get_nowait()
            print("%.2f：%s: 消费了一个包子" % (time.time(), name))
        except Exception:
            print("%.2f：包子不够了……" % time.time())
        time.sleep(random.randrange(5))


q = queue.Queue(10)
p1 = threading.Thread(target=producer, args=["张三", q])
p1.start()
p2 = threading.Thread(target=producer, args=["lisi", q])
p2.start()

c1 = threading.Thread(target=consumer, args=["李逍遥", q])
c1.start()
c2 = threading.Thread(target=consumer, args=["灵儿", q])
c2.start()
