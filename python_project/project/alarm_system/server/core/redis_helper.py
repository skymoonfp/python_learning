#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""


**************************
文件:     redis_helper.py
 IDE：    PyCharm
创建时间： 2019/5/29 10:41
@author： skymoon
"""

import redis


class RedisHelper(object):

    def __init__(self, host="localhost", chan_sub="fm0", chan_pub="fm0"):
        self.__conn = redis.Redis(host=host)
        self.chan_sub = chan_sub
        self.chan_pub = chan_pub

    def get(self, key):
        return self.__conn.get(key)

    def set(self, key, value):
        self.__conn.set(key, value)

    def publish(self, msg):
        self.__conn.publish(self.chan_pub, msg)
        return True

    def subscribe(self):
        pub = self.__conn.pubsub()
        pub.subscribe(self.chan_sub)
        pub.parse_response()
        return pub
