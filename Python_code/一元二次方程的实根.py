#!/usr/bin/env python3
# coding=utf-8


import math


# 定义输入函数
def d_input():
    # 输入方程的系数
    # a, b, c = map(float, input('请依次输入二次方程a * x*x + b * x + c = 0的系数a、b、c的值：').split())
    # A = [float(a) for a in input('请依次输入二次方程a * x*x + b * x + c = 0的系数a、b、c的值：').split()]
    # a, b, c= A[0], A[1], A[2]
    a, b, c = eval(input('请依次输入二次方程a * x*x + b * x + c = 0的系数a、b、c的值：\n'))
    A = [a, b, c]

    # 判断输入是否为数值类型
    if not isinstance(a, (int, float)):
        raise TypeError('bad operand type')
    if not isinstance(b, (int, float)):
        raise TypeError('bad operand type')
    if not isinstance(c, (int, float)):
        raise TypeError('bad operand type')

    return A


# 定义输出函数
def d_output(d_input, r_calc):
    if r_calc == []:
        print('该方程没有实根！\n')
    else:
        print('二次方程%s * x*x + %s * x + %s = 0的两个实根分别是：%f，%f\n' % (
        d_input[0], d_input[1], d_input[2], r_calc[0], r_calc[1]))

    # 判断是否继续
    yn = input('继续请输入Y，退出请输入任意键：')
    if yn == 'Y' or yn == 'y':
        main()
    else:
        return


# 定义计算实根的函数
def root_calc(d_input):
    a, b, c = d_input[0], d_input[1], d_input[2]

    # 判断是否有实根
    delta = b * b - 4 * a * c
    if delta < 0:
        R = []
    else:
        discRoot = math.sqrt(delta)
        root1 = (-b + discRoot) / (2 * a)
        root2 = (-b - discRoot) / (2 * a)
        R = [root1, root2]
    return R


def main():
    I = d_input()
    R = root_calc(I)
    d_output(I, R)


main()
