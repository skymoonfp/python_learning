#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""

"""

import time


# 装饰器，计算执行函数需要的时间
def timer(func):
    def decor(*args):
        start_time = time.time()
        func(*args)
        end_time = time.time()
        d_time = end_time - start_time
        print("the running time is : ", d_time)
        return d_time

    return decor
