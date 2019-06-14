#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""


**************************
文件:     search.py
 IDE：    PyCharm
创建时间： 2019/5/31 10:51
@author： skymoon
"""

import requests


def search(url, keyword, leng=()):
    try:
        r = requests.get(url, params=keyword)
        print(r.request.url)
        r.raise_for_status()
        text = r.text
        long = len(text)
        if leng:
            return text[leng[0]:leng[1]]
        else:
            if long <= 3000:
                return text
            else:
                return len(text)
    except:
        print("爬取失败")


if __name__ == "__main__":
    url_1 = "http://www.baidu.com/s"
    keyword_1 = {"wd": "python"}
    print(search(url_1, keyword_1))

    url_2 = "http://www.so.com/s"
    keyword_2 = {"q": "python"}
    leng_2 = (100, 1100)
    print(search(url_2, keyword_2, leng_2))
