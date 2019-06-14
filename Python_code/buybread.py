#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import matplotlib.pyplot as plt
# 投诉前随机取
import numpy
import scipy.stats as sta

X = sta.norm(loc=950, scale=20)
wbread = []
for i in range(365):
    x = X.rvs(size=100)
    wbread.append(x[0])

print(numpy.mean(wbread))
print(sta.skew(wbread))
plt.hist(wbread, color='grey')
plt.show()

# 投诉后取最大
X = sta.norm(loc=950, scale=20)
wbread = []
for i in range(365):
    x = X.rvs(size=100)
    wbread.append(max(x))

print(numpy.mean(wbread))
print(sta.skew(wbread))
plt.hist(wbread, color='grey')
plt.show()

print('\n')
input('Please press Enter to exit!')
