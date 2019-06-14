#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 定义分赌本函数
import random


def Bookie(n, n1, n2):
    for i in range(2 * n - n1 - n2 - 1):
        D = random.randint(1, 2)
        if D == 1:
            n1 += 1
        else:
            n2 += 1
        if n1 == n:
            return 1
        if n2 == n:
            return 2


# 测试分赌本函数
n = int(input('输入模拟次数： '))
a, b, c = map(int, input('依次输入\'总需赢次数\'、\'甲已赢次数\'、\'乙已赢次数\'： ').split())
win = 0
for i in range(n):
    if Bookie(a, b, c) == 1:
        win += 1
print('甲最终赢的概率： ', float(win) / float(n))
print('乙最终赢的概率： ', 1 - float(win) / float(n))
print('\n')
input('Please press Enter to exit!')
