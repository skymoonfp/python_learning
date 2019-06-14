#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 生成1~100内奇数
L = []
n = 1
while n <= 100:
    L.append(n)
    n = n + 2
print(L)

# 取L前一半元素
L_half = []
i = 0
while i < len(L) / 2:
    L_half.append(L[i])
    i += 1
print(L_half)

# 生成1~100内偶数
M = []
m = 1
# while (m<= 100 and m % 2 == 0):
while m <= 100:
    if m % 2 == 0:
        M.append(m)
    m = m + 1
print(M)

# 取M前一半元素
M_half = []
i = 0
while i < len(M) / 2:
    M_half.append(M[i])
    i += 1
print(M_half)

print('\n')
input('Please press Enter to exit!')
