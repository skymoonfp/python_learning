#!/usr/bin/env python3
# coding=utf-8


import math


# 定义杨辉三角输出函数
def triangles(row):
    i = 0
    while i < row:
        Tria = []
        for j in range(i + 1):
            Tria_i_j = int(math.factorial(i) / (math.factorial(j) * math.factorial(i - j)))
            Tria.append(Tria_i_j)
        yield Tria
        i = i + 1


# 定义主函数
def main():
    n = int(input('请输入想要输出的杨辉三角的行数：'))
    for i in triangles(n):
        print(i)


main()

'''
# 期待输出:
# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
# [1, 5, 10, 10, 5, 1]
# [1, 6, 15, 20, 15, 6, 1]
# [1, 7, 21, 35, 35, 21, 7, 1]
# [1, 8, 28, 56, 70, 56, 28, 8, 1]
# [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
n = 0
results = []
for t in triangles():
    print(t)
    results.append(t)
    n = n + 1
    if n == 10:
        break
if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')
'''
