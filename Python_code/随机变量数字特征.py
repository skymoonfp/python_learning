#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import scipy.stats


# 定义二项分布调用函数
def binom0():
    n, p = map(float, input('请输入二项分布的两个参数n，p指： ').split())
    k = int(input('请输入要求计算的二项分布的矩的最高阶数： '))
    rv = scipy.stats.binom(n, p)
    print('该二项分布的期望是： ', rv.mean())
    print('该二项分布的方差是： ', rv.var())
    for i in range(int(k)):
        r = rv.moment(i + 1)
        print('该二项分布的%d阶矩是： %f' % (i + 1, r))
    print('该二项分布的期望、方差、偏度、峰度依次是： ')
    print(rv.stats(moments='mvsk'))


# 定义泊松分布调用函数
def poisson0():
    lam = float(input('请输入泊松分布的参数lam值： '))
    k = int(input('请输入要求计算的泊松分布的矩的最高阶数： '))
    rv = scipy.stats.poisson(mu=lam)
    print('该泊松分布的期望是： ', rv.mean())
    print('该泊松分布的方差是： ', rv.var())
    for i in range(int(k)):
        r = rv.moment(i + 1)
        print('该泊松分布的%d阶矩是： %f' % (i + 1, r))
    print('该泊松分布的期望、方差、偏度、峰度依次是： ')
    print(rv.stats(moments='mvsk'))


# 定义均匀分布调用函数
def uniform0():
    l, s = map(float, input('请输入均匀分布的两个参数l，s(l为均匀分布下限值a，且s为均匀分布区间长度b-a）值： ').split())
    k = int(input('请输入要求计算的均匀分布的矩的最高阶数： '))
    rv = scipy.stats.uniform(loc=l, scale=s)
    print('该均匀分布的期望是： ', rv.mean())
    print('该均匀分布的方差是： ', rv.var())
    for i in range(int(k)):
        r = rv.moment(i + 1)
        print('该均匀分布的%d阶矩是： %f' % (i + 1, r))
    print('该均匀分布的期望、方差、偏度、峰度依次是： ')
    print(rv.stats(moments='mvsk'))


# 定义指数分布调用函数
def expon0():
    theta = float(input('请输入指数分布的参数theta(即1/lam)值： '))
    k = int(input('请输入要求计算的指数分布的矩的最高阶数： '))
    rv = scipy.stats.expon(scale=theta)
    print('该指数分布的期望是： ', rv.mean())
    print('该指数分布的方差是： ', rv.var())
    for i in range(int(k)):
        r = rv.moment(i + 1)
        print('该指数分布的%d阶矩是： %f' % (i + 1, r))
    print('该指数分布的期望、方差、偏度、峰度依次是： ')
    print(rv.stats(moments='mvsk'))


# 定义正态分布调用函数
def norm0():
    l, s = map(float, input('请输入正态分布的两个参数mu，sigma指： ').split())
    k = int(input('请输入要求计算的正态分布的矩的最高阶数： '))
    rv = scipy.stats.norm(l, s)
    print('该正态分布的期望是： ', rv.mean())
    print('该正态分布的方差是： ', rv.var())
    for i in range(int(k)):
        r = rv.moment(i + 1)
        print('该正态分布的%d阶矩是： %f' % (i + 1, r))
    print('该正态分布的期望、方差、偏度、峰度依次是： ')
    print(rv.stats(moments='mvsk'))


# 定义正态分布的函数的调用函数
def norm1():
    # func = input('请输入正态分布的函数的表达式（以x为自变量）： ')
    f = lambda x: x ** 4  # 该处固定函数为f = x**4，如何用input()直接输入函数表达式呢？
    l, s = map(float, input('请输入正态分布的两个参数mu，sigma值： ').split())
    print('该正态分布的函数的期望是： ', scipy.stats.norm.expect(f, loc=l, scale=s))
    J = input('如果想继续，请输入Y；如果想结束，请输入N： ')
    if J == 'Y':
        norm1()
    else:
        return


# 定义调用随机分布调用函数的函数
def calling():
    function_name = input('请输入要调用的随机分布名： ')
    if function_name == '二项' or function_name == '二项分布' or function_name == 'binom':
        binom0()
        J = input('如果想继续，请输入Y；如果想结束，请输入N： ')
        if J == 'Y' or J == 'y':
            calling()
        else:
            return
    elif function_name == '泊松' or function_name == '泊松分布' or function_name == 'poisson':
        poisson0()
        J = input('如果想继续，请输入Y；如果想结束，请输入N： ')
        if J == 'Y' or J == 'y':
            calling()
        else:
            return
    elif function_name == '均匀' or function_name == '均匀分布' or function_name == 'uniform':
        uniform0()
        J = input('如果想继续，请输入Y；如果想结束，请输入N： ')
        if J == 'Y' or J == 'y':
            calling()
        else:
            return
    elif function_name == '指数' or function_name == '指数分布' or function_name == 'expon':
        expon0()
        J = input('如果想继续，请输入Y；如果想结束，请输入N： ')
        if J == 'Y' or J == 'y':
            calling()
        else:
            return
    elif function_name == '正态' or function_name == '正态分布' or function_name == 'norm':
        norm0()
        J = input('如果想继续，请输入Y；如果想结束，请输入N： ')
        if J == 'Y' or J == 'y':
            calling()
        else:
            return
    elif function_name == '正态的函数' or function_name == '正态分布的函数' or function_name == 'func of norm' or function_name == 'function of norm':
        norm1()
        J = input('如果想继续，请输入Y；如果想结束，请输入N： ')
        if J == 'Y' or J == 'y':
            calling()
        else:
            return
    else:
        print('无法调用该函数，请检查函数名是否输入正确！')
        calling()


calling()
print('\n')
input('Please press Enter to exit!')
