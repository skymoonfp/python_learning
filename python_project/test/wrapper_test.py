#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""


**************************
文件:     wrapper_test.py
 IDE：    PyCharm
创建时间： 2019/5/25 10:07
@author： skymoon
"""

import functools
import time


def add_datetime_info(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        ctime = time.ctime()
        func(*args, **kwargs, ctime)

    # wrapper.__name__ = func.__name__  # other method of remaining name of func
    return wrapper


@add_datetime_info
def my_name(time=ctime):
