#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""


**************************
文件:     asynchronous.py
 IDE：    PyCharm
创建时间： 2019/5/27 11:46
@author： skymoon
"""

import random
import threading
import time


class TouchAct(object):

    def producer(self, event):
        print("chef: 等人来买包子……")
        event.wait()
        event.clear()

        print("chef: sb来买包子了……")
        print("chef: 给sb做包子……")
        time.sleep(5)

        print("chef: 包子好了！")
        event.set()

    def consumer(self, event):
        print("zhangsan: 去买包子……")
        event.set()

        time.sleep(3)
        print("zhangsan: 等包子准备好……")
        print(event.wait())

        print("包子真好吃！")

    def __call__(self):
        event = threading.Event()
        p = threading.Thread(target=self.producer, args=[event, ])
        p.start()
        c = threading.Thread(target=self.consumer, args=[event, ])
        c.start()


class ActTouchAct(TouchAct):

    def producer(self, event):

        event_stat = event.isSet()
        while True:
            if not event_stat:
                print(
                    "\033[1;35m%s\033[0m: chief: I'am playing poker to waiting for consumer buying my baozi……" % time.ctime())
                time.sleep(1)
                event_stat = event.isSet()
            else:
                break

        print("\033[1;35m%s\033[0m: chef: sb来买包子了……" % time.ctime())
        print("\033[1;35m%s\033[0m: chef: 开始给sb做包子……" % time.ctime())
        event.clear()
        time.sleep(random.randrange(3, 5))  # 花费3~5秒来生产一个包子
        print("\033[1;35m%s\033[0m: chef: 你的包子好了，快来取吧……" % time.ctime())
        event.set()

    def consumer(self, event):

        print("\033[1;35m%s\033[0m: zhangsan: 我在去买包子的路上……" % time.ctime())
        time.sleep(random.randrange(5, 8))  # 在5~10秒之间到达包子铺
        print("\033[1;35m%s\033[0m: zhangsan: 终于到了包子铺，好累……" % time.ctime())
        event.set()
        time.sleep(1)  # 给对方1秒反应时间

        while True:
            if not event.isSet():
                print("\033[1;35m%s\033[0m: zhangsan: 等做包子好无聊啊，去干点儿别的吧……" % time.ctime())
                for i in range(1, 1000000):
                    if not event.isSet():
                        print("\033[1;35m%s\033[0m: zhangsan: %d只羊" % (time.ctime(), i))
                        time.sleep(0.5)
                    else:
                        break
            else:
                break

        print("\033[1;35m%s\033[0m: zhangsan: 谢谢，收到您的包子，我走了……" % time.ctime())
        event.clear()


if __name__ == "__main__":
    # TouchAct()()
    ActTouchAct()()
