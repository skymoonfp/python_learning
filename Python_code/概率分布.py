#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
# 二项分布
from scipy.stats import binom as B

n, p = map(float, input('请输入二项分布的两个参数：').split())
rvB = B(n, p)
x = np.arange(0, 11, 1)
y = rvB.pmf(x)

print(y)
plt.bar(x, y, width=0.6, color='grey')
plt.show()

# 几何分布
from scipy.stats import geom as G

g = float(input('请输入几何分布的参数：'))
rvG = G(g)
x = np.arange(1, 11, 1)
y = rvG.pmf(x)

print(y)
plt.bar(x, y, width=0.6, color='grey')
plt.show()

# 泊松分布
from scipy.stats import poisson as Pie

l = float(input('请输入泊松分布的参数：'))
rvP = Pie(l)
x = np.arange(0, 11, 1)
y = rvP.pmf(x)

print(y)
plt.bar(x, y, width=0.6, color='grey')
plt.show()

print('\n')
input('Please press Enter to exit!')
