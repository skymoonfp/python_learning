#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""


**************************
文件:     中国大学排名
 IDE：    PyCharm
创建时间： 2019/6/17 16:19
@author： skymoon
"""

import bs4
import requests
from bs4 import BeautifulSoup


def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except Exception as e:
        return ""


def fillUnivList(ulist, html):
    soup = BeautifulSoup(html, "html.parser")
    for tr in soup.find("tbody").children:
        if isinstance(tr, bs4.element.Tag):
            tds = tr("td")
            ulist.append([tds[0].string, tds[1].string, tds[2].string, tds[3].string])


def printUnivList(ulist, num):
    tplt = "{0:^10}\t{1:{4}^10}\t{2:^10}\t{3:^10}"
    print(tplt.format("排名", "学校名称", "属地", "总分", chr(12288)))
    for i in range(num):
        u = ulist[i]
        print(tplt.format(u[0], u[1], u[2], u[3], chr(12288)))


def main():
    uinfo = []
    url = "http://www.zuihaodaxue.com/zuihaodaxuepaiming2019.html"
    html = getHTMLText(url)
    fillUnivList(uinfo, html)
    printUnivList(uinfo, 20)  # 20 univs


if __name__ == "__main__":
    main()
