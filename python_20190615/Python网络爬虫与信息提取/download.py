#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""


**************************
文件:     download.py
 IDE：    PyCharm
创建时间： 2019/5/31 11:08
@author： skymoon
"""

import os

import requests


def download(url, root):
    root = root.strip("/") + "/"
    file = url.split("/")[-1]

    if not os.path.exists(root):
        os.mkdir(root)
    path = root + file

    i = 1
    while i:
        if os.path.exists(path):
            print("文件已存在！")
            file = ".".join(file.split(".")[:-1]) + "(" + str(i) + ")." + file.split(".")[-1]
            path = root + file
            i += 1
        else:
            break

    try:
        r = requests.get(url)
        with open(path, "wb") as f:
            f.write(r.content)
        print("文件保存成功！")
    except Exception as e:
        print(e)
        print("爬取失败")


if __name__ == "__main__":
    root = "d:/download"
    url = "http://img2.ph.126.net/EOYMpNMNmscOZEVQs9PK0A==/1143632830475687477.jpg"
    download(url, root)
