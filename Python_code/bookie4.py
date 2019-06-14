#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import numpy as np


# 定义分赌本函数
def Bookie(n, n1, n2, n3, n4, n5, p1, p2, p3, p4, p5):
    for i in range(5 * n - n1 - n2 - n3 - n4 - n5 - 4):
        # np.random.seed(0)
        # p = np.array([p1,p2,p3,p4,p5])
        D = np.random.choice(['a', 'b', 'c', 'd', 'e'], 1, p=[p1, p2, p3, p4, p5])
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
n = int(input('输入模拟次数： '))
n0 = int(input('输入总需赢次数： '))
n1, n2, n3, n4, n5 = map(int, input('依次输入\'甲已赢次数\'、\'乙已赢次数\'、\'丙已赢次数\'、\'丁已赢次数\'、\'戊已赢次数\'： ').split())
p1, p2, p3, p4, p5 = map(float, input('依次输入\'甲的技术概率\'、\'乙的技术概率\'、\'丙的技术概率\'、\'丁的技术概率\'、\'戊的技术概率\'： ').split())
win1, win2, win3, win4, win5 = 0, 0, 0, 0, 0
for i in range(n):
    B = Bookie(n0, n1, n2, n3, n4, n5, p1, p2, p3, p4, p5)
    if B == 'a':
        win1 += 1
    elif B == 'b':
        win2 += 1
    elif B == 'c':
        win3 += 1
    elif B == 'd':
        win4 += 1
    elif B == 'e':
        win5 += 1
print('甲最终赢的概率： ', float(win1) / float(n))
print('乙最终赢的概率： ', float(win2) / float(n))
print('丙最终赢的概率： ', float(win3) / float(n))
print('丁最终赢的概率： ', float(win4) / float(n))
print('戊最终赢的概率： ', float(win5) / float(n))
print('\n')
input('Please press Enter to exit!')
