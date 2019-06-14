#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""


**************************
文件:     index
 IDE：    PyCharm
创建时间： 2019/6/12 17:59
@author： skymoon
"""

from http.client import *


def submit_data(self, host, port, source, params, timeout):
    headers = {"Content-type": "application/json"}
    try:
        conn = HTTPConnection(host, port, timeout)
        conn.request("POST", source, params, headers)
        response = conn.getresponse()
        original = response.read()
        print(original)
    except Exception as e:
        raise e
    return original


if __name__ == "__main__":
    pass
