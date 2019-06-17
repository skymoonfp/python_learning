#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""


**************************
文件:     淘宝商品比价定向爬虫
 IDE：    PyCharm
创建时间： 2019/6/17 18:26
@author： skymoon
"""

import re

import requests


def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except Exception as e:
        return ""


def parsePage(ilt, html):
    try:
        plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"', html)
        tlt = re.findall(r'\"raw_title\"\:\".*?\"', html)
        for i in range(len(plt)):
            price = eval(plt[i].split(":")[1])
            title = eval(tlt[i].split(":")[1])
            ilt.append([price, title])
    except Exception as e:
        print("")


def printGoodsList(ilt):
    tplt = "{:4}\t{:8}\t{:16}"
    print(tplt.format("序号", "价格", "商品名称"))
    count = 0
    for g in ilt:
        count = count + 1
        print(tplt.format(count, g[0], g[1]))


def main():
    goods = "书包"
    depth = 2
    start_url = "https://s.taobao.com/search?q=" + goods
    infoList = []
    for i in range(depth):
        try:
            url = start_url + "&s=" + str(44 * i)
            html = getHTMLText(url)
            print(html)
            parsePage(infoList, html)
        except Exception as e:
            continue
    printGoodsList(infoList)


if __name__ == "__main__":
    main()
