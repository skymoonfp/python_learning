#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 定义分赌本函数
import numpy as np


def Bookie(n, n1, n2, n3, n4, n5, p1, p2, p3, p4, p5):
    for i in range(5 * n - n1 - n2 - n3 - n4 - n5):
        # np.random.seed(0)
        # p = np.array([p1,p2,p3,p4,p5])
        D = np.random.choice(['a', 'b', 'c', 'd', 'e'], 1, replace=True, p=[p1, p2, p3, p4, p5])
        if D == 'a':
            n1 += 1
        elif D == 'b':
            n2 += 1
        elif D == 'c':
            n3 += 1
        elif D == 'd':
            n4 += 1
        elif D == 'e':
            n5 += 1
        if n1 == n:
            return 'a'
        if n2 == n:
            return 'b'
        if n3 == n:
            return 'c'
        if n4 == n:
            return 'd'
        if n5 == n:
            return 'e'


# 测试分赌本函数
n = int(input('input n:'))
wina = 0
winb = 0
winc = 0
wind = 0
wine = 0
for i in range(n):
    B = Bookie(3, 0, 0, 0, 0, 0, 0.2, 0.2, 0.2, 0.2, 0.2)
    if B == 'a':
        wina += 1
    elif B == 'b':
        winb += 1
    elif B == 'c':
        winc += 1
    elif B == 'd':
        wind += 1
    elif B == 'e':
        wine += 1
print('甲最终赢的概率： ', float(wina) / float(n))
print('乙最终赢的概率： ', float(winb) / float(n))
print('丙最终赢的概率： ', float(winc) / float(n))
print('丁最终赢的概率： ', float(wind) / float(n))
print('戊最终赢的概率： ', float(wine) / float(n))
