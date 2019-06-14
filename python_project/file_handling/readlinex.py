#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""
实现xreadline()功能
"""


def readlinex(file_name: str):
    seek = 0
    while True:
        with open(file_name, "r") as f:
            f.seek(seek)
            data = f.readline()
            if data:
                seek = f.tell()
                yield data
            else:
                return


if __name__ == "__main__":
    for item in readlinex("e:\\dataanalysis\\python_project\\shopping_goods_list.txt"):
        print(item, end="")
