#!/usr/bin/env python3
# -*- coding:utf-8 -*-


# 定义最小最大数函数
def findMinAndMax(L):
    if len(L) == 0:
        return (None, None)
    elif len(L) == 1:
        return (L[0], L[0])
    else:
        min, max = L[0], L[0]
        for i in L:
            if i <= min:
                min = i
        for j in L:
            if j >= max:
                max = j
    return (min, max)


# 定义主函数
def main():
    # L = [float(n) for n in input('请输入： ').split()]
    L = list(map(float, input('请输入： ').strip().split()))
    print('L的最小值和最大值分别是： ', findMinAndMax(L))


main()

'''
# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')
'''
