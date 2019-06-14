#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""


**************************
文件:     pythonpathsetter.py
 IDE：    PyCharm
创建时间： 2019/5/30 11:45
@author： skymoon
"""

import fnmatch
import sys
from os.path import abspath, dirname

DIR = dirname(abspath(__file__))


# print(DIR)  # 当前文件（e.g.绝对路径为E:\abc\f\pythonpathsetter.py）的dir（即E:\abc\f），即包含该文件的package（即f）的path（即E:\abc\f）


def add_path(path, end=False):
    if not end:
        remove_path(path)
        sys.path.insert(0, path)
    elif not any(fnmatch.fnmatch(p, path) for p in sys.path):
        sys.path.append(path)


def remove_path(path):
    sys.path = [p for p in sys.path if not fnmatch.fnmatch(p, path)]


# print(dirname(DIR))  # 当前文件的dir的dir（即E:\abc）

add_path(dirname(DIR))
# 将（即E:\abc）（即当前package的上级文件夹的path，而非当前package本身的path）加入系统环境变量；
# 这样，package内的所有module都以"from package.* import *"的形式被导入时，可以避免因为以下三种情况导致的麻烦：
# （1）如果你用PYTHONPATH，那么当有多个项目时，你需要把每个项目的根目录都加入到PYTHONPATH中，会使得PYTHONPATH变得十分臃肿；
# （2）如果你使用sys.path，由于文件夹是动态添加的，所以当你使用相对路径的时候，实际路径会十分依赖于你的入口函数，当入口函数改变很可能就会导致代码无法运行；
# （3）如果你使用绝对路径，将你的代码在其他机器上运行的时候需要重新配置这些变量，十分麻烦。

remove_path(DIR)
