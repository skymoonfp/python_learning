#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import matplotlib.pyplot as plt
import numpy as np
import scipy.stats


#
def bignum():
    n, mu0 = map(float, input('请依次输入抽样次数、期望值： ').split())
    n1 = int(input('请输入二项分布的参数n： '))

    x = np.arange(1, n + 1, 1)
    r1 = scipy.stats.binom.rvs(n1, mu0 / n1, size=int(n))
    r2 = scipy.stats.poisson.rvs(mu=mu0, size=int(n))
    r3 = scipy.stats.norm.rvs(loc=mu0, size=int(n))

    y = []
    rsum = 0.0
    for i in range(int(n)):
        rsum = rsum + (r1[i] + r2[i] + r3[i])
        y.append(rsum / ((i + 1) * 3) - mu0)
    plt.plot(x, y, color='red')
    plt.show()
    J = input('如果想继续，请输入Y；如果想结束，请输入N： ')
    if J == 'Y' or J == 'y':
        bignum()
    else:
        return


bignum()
print('\n')
input('Please press Enter to exit!')
