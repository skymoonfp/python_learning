#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random

# 指数分布的模拟
import math
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import expon as E


# 返回随机概率值的反函数值
def exp(theta):
    p = random.random()
    return -math.log(1 - p) * theta


scale0 = float(input('请输入指数分布的参数：'))

# 绘制模拟图
x1 = []
for i in range(1000):
    x1.append(exp(scale0))
x1 = sorted(x1)
y1 = np.linspace(0, 1, 1000)
plt.plot(x1, y1, color='blue')

# 绘制内置函数图
rv = E(scale=scale0)
x2 = np.linspace(0, 5, 1000)
plt.plot(x2, rv.cdf(x2), color='red')
plt.show()

print('\n')
input('Please press Enter to exit!')
