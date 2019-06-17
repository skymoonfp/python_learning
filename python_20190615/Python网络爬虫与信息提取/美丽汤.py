#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""


**************************
文件:     美丽汤
 IDE：    PyCharm
创建时间： 2019/6/17 14:55
@author： skymoon
"""

import requests
from bs4 import BeautifulSoup


def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "产生异常"


if __name__ == "__main__":
    douban = getHTMLText("http://www.douban.com")[:10000]
    soup = BeautifulSoup(douban, "html.parser")
    print(soup)
    douban_title = soup.title
    print(douban_title)
    print(douban_title.attrs)
    print(soup.a.attrs["href"])
