#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""


**************************
文件:     requests_test.py
 IDE：    PyCharm
创建时间： 2019/5/29 17:04
@author： skymoon
"""

import requests


def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "产生异常"


if __name__ == "__main__":
    url = "http://www.douban.com"
    print(getHTMLText(url))
