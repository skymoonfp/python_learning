#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
# 正态分布
from scipy.stats import norm as N

loc1, scale1 = map(float, (input('请输入第一个正态分布的参数：').split()))
loc2, scale2 = map(float, (input('请输入第二个正态分布的参数：').split()))
loc3, scale3 = map(float, (input('请输入第三个正态分布的参数：').split()))
x = np.linspace(-10, 10, 100)
rvN1 = N(loc=loc1, scale=scale1)
rvN2 = N(loc=loc2, scale=scale2)
rvN3 = N(loc=loc3, scale=scale3)

plt.plot(x, rvN1.pdf(x), color='green')
plt.plot(x, rvN2.pdf(x), color='blue')
plt.plot(x, rvN3.pdf(x), color='red')
plt.show()

print('\n')
input('Please press Enter to exit!')
