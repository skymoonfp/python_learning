#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""


**************************
文件:     redis_subscription_client.py
 IDE：    PyCharm
创建时间： 2019/5/30 上午1:21
@author： skymoon
"""

import pickle

from mysocket import redis_subscription

if __name__ == "__main__":
    # t = redis_subscription.RedisHelper("localhost", "fm114", "fm114")
    #
    # t.publish("You")
    # time.sleep(3)
    # t.publish("are")
    # time.sleep(2)
    # t.publish("sb")
    # time.sleep(1)
    # t.publish("?")
    # time.sleep(5)
    # t.publish("over")

    t = redis_subscription.RedisHelper("localhost", "fm0", "fm0")
    print(pickle.loads(t.get("HostConfig::10.165.13.233")))
