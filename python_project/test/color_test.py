#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""


**************************
文件:     color_test.py
 IDE：    PyCharm
创建时间： 2019/5/28 1:45
@author： skymoon
"""

if __name__ == "__main__":

    for i in range(108):
        print("%d: \033[%dm颜色\033[0m" % (i, i))

    print("=====================")
    print("=====================")

    for i in range(108):
        for j in range(108):
            print("%d+%d: \033[%dm\033[%dm颜色\033[0m" % (i, j, i, j))
        print("-------------------")

    color_set = [0, 1, 4, 7, ]
