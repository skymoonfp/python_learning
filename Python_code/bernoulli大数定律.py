#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import bernoulli


#
def bernoulli0():
    n, p = map(float, input('请依次输入抽样次数、每次试验出现的概率： ').split())
    x = np.arange(1, n + 1, 1)
    r = bernoulli.rvs(p, size=int(n))
    y = []
    rsum = 0.0
    for i in range(int(n)):
        if r[i] == 1:
            rsum = rsum + 1
        y.append(rsum / (i + 1))
    plt.plot(x, y, color='red')
    plt.show()
    J = input('如果想继续，请输入Y；如果想结束，请输入N： ')
    if J == 'Y' or J == 'y':
        bernoulli0()
    else:
        return


bernoulli0()
print('\n')
input('Please press Enter to exit!')
