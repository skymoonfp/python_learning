#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""


**************************
文件:     redis_test.py
 IDE：    PyCharm
创建时间： 2019/5/29 10:35
@author： skymoon
"""

import redis

if __name__ == "__main__":
    conn = redis.Redis(host="localhost")
    conn.set("age", 18)
    conn.set("name", "Sam")
    print(conn.get("name").decode())
    print(conn.get("age").decode())
