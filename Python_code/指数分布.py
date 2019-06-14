#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
# 指数分布
from scipy.stats import expon as E

scale1 = float(input('请输入第一个指数分布的参数：'))
scale2 = float(input('请输入第二个指数分布的参数：'))
scale3 = float(input('请输入第三个指数分布的参数：'))

rvE1 = E(scale=scale1)
rvE2 = E(scale=scale2)
rvE3 = E(scale=scale3)

x = np.linspace(0, 5, 100)

plt.plot(x, rvE1.pdf(x), color='green')
plt.plot(x, rvE2.pdf(x), color='blue')
plt.plot(x, rvE3.pdf(x), color='red')
plt.show()

# 指数分布的（累积概率）分布函数
scale1 = float(input('请输入第一个指数分布的参数：'))
scale2 = float(input('请输入第二个指数分布的参数：'))
scale3 = float(input('请输入第三个指数分布的参数：'))

rvE1 = E(scale=scale1)
rvE2 = E(scale=scale2)
rvE3 = E(scale=scale3)

x = np.linspace(0, 5, 100)

plt.plot(x, rvE1.pdf(x), color='green')
plt.plot(x, rvE1.cdf(x), color='green')
plt.plot(x, rvE2.pdf(x), color='blue')
plt.plot(x, rvE2.cdf(x), color='blue')
plt.plot(x, rvE3.pdf(x), color='red')
plt.plot(x, rvE3.cdf(x), color='red')
plt.show()

# 指数分布的模拟
import math
import random


# 返回随机概率值的反函数值
def exp(lam):
    p = random.random()
    return -math.log(1 - p) / lam


scale0 = float(input('请输入指数分布的参数：'))

# 绘制模拟图
x1 = []
y1 = np.linspace(0, 1, 1000)
for i in range(1000):
    x1.append(exp(scale0))
x1 = sorted(x1)
plt.plot(x1, y1, color='blue')

# 绘制内置函数图
rv = E(scale=scale0)
x2 = np.linspace(0, 5, 1000)
plt.plot(x2, rv.cdf(x2), color='red')
plt.show()

print('\n')
input('Please press Enter to exit!')
