#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""


**************************
文件:     读取excel文件
 IDE：    PyCharm
创建时间： 2019/6/15 15:19
@author： skymoon
"""

import pandas as pd

result = pd.read_excel("e:\\dataanalysis\\Historia.xlsx", encoding="utf-8")
print(result)
print(result[2:20])
print(result[2:30]["Person"])
