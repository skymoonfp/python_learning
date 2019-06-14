#!/usr/bin/env python3
# -*- coding:utf-8 -*-


import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as ss


# 定义服从指数分布的样本统计函数
def expon0():
    n1, n2 = map(int, input('请依次输入样本容量、抽样次数： ').split())
    s = float(input('请输入指数分布参数theta的值： '))
    y = []
    for i in range(n2):
        r = ss.expon.rvs(scale=s, size=n1)
        rsum = np.sum(r)
        z = (rsum - n1 * s) / np.sqrt(n1 * s ** 2)
        y.append(z)
    plt.hist(y, color='grey')
    plt.show()


# 定义服从二项分布的样本统计函数
def binom0():
    n2 = int(input('请输入抽样次数： '))
    n, p = map(float, input('请输入二项分布参数n，p的值： ').split())
    y = []
    for i in range(n2):
        r = ss.binom.rvs(int(n), p)
        rsum = np.sum(r)
        z = (rsum - n * p) / np.sqrt(n * p * (1 - p))
        y.append(z)
    plt.hist(y, color='grey')
    plt.show()


# 定义调用函数
def calling():
    name = input("请输入要调用的分布类型： ")
    if "指数" in name or "exp" in name:
        expon0()
    elif "二项" in name or "bin" in name:
        binom0()
    else:
        print("该分布类型无法调用，请重试！")
        calling()
    J = input("继续请输入Y，退出请输入任意键： ")
    if J == "Y" or J == "y":
        calling()
    else:
        return


calling()
print('\n')
input('Please press Enter to exit!')
