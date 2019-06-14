#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""


**************************
文件:     global_settings.py
 IDE：    PyCharm
创建时间： 2019/5/30 13:55
@author： skymoon
"""

import os
import sys

base_dir = os.path.dirname(os.path.dirname(__file__))
print(base_dir)
sys.path.append(base_dir)
