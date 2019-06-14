#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""


**************************
文件:     files_auto_classify
 IDE：    PyCharm
创建时间： 2019/6/2 19:05
@author： skymoon
"""

import os
import shutil


def file_move():
    path = "./"
    files = os.listdir(path)

    for f in files:

        folder_name = "./" + f.split(".")[-1]
        if not os.path.exists(path):
            os.makedirs(folder_name)
            shutil.move(f, folder_name)
        else:
            shutil.move(f, path)


if __name__ == "__main__":
    file_move()
