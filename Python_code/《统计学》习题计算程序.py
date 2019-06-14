#!/usr/bin/env python3
# coding=utf-8


import math
import scipy.stats


# 基本参数的计算：
# 定义平均值计算函数
def avg(X):
    x_avg = 0
    x_sum = 0
    for x in X:
        x_sum = x_sum + x
    x_avg = x_sum / len(X)
    return x_avg


# 定义方差值计算函数
def var(X):
    x_var = 0
    sum = 0
    for x in X:
        sum = sum + (x - avg(X)) ** 2
    x_var = sum / len(X)
    return x_var


# 定义样本方差值计算函数
def var_u(X):
    x_var_u = 0
    sum = 0
    for x in X:
        sum = sum + (x - avg(X)) ** 2
    x_var_u = sum / (len(X) - 1)
    return x_var_u


# 定义标准差值计算函数
def stdev(X):
    return pow(var(X), 0.5)


# 定义标样本准差值计算函数
def stdev_u(X):
    return pow(var_u(X), 0.5)


# 定义匹配样本的配对差值计算函数
def delta(X1, X2):
    D = []
    i = 0
    if len(X1) != len(X2):
        print('两组样本数量不相等，无法配对！')
        return
    else:
        while i < len(X1):
            D.append(X1[i] - X2[i])
            i = i + 1
        return D


# 定义调用平均值函数的函数
def avg_calling():
    L0 = input('继续使用刚才的数据请输入Y，使用新数据请输入N！')
    global G
    if L0 == 'Y' or L0 == 'y':
        if G != []:
            print('平均值是：%.3f\n' % (avg(G)))
        else:
            print('刚才没有输入数据！')
            avg_calling()
    elif L0 == 'N' or L0 == 'n':
        L = dataInput()
        print('平均值是：%.3f\n' % (avg(L)))
    else:
        print('输入有误！')
        avg_calling()
    a = int(input('继续计算平均值请输入1，需要计算其他类型请输入2，退出请输入0：'))
    if a == 0:
        return
    elif a == 1:
        avg_calling()
    else:
        type_calling()


# 定义调用方差值函数的函数
def var_calling():
    L0 = input('继续使用刚才的数据请输入Y，使用新数据请输入N！')
    global G
    if L0 == 'Y' or L0 == 'y':
        if G != []:
            print('方差值是：%.3f\n' % (var(G)))
        else:
            print('刚才没有输入数据！')
            var_calling()
    elif L0 == 'N' or L0 == 'n':
        L = dataInput()
        print('方差值是：%.3f\n' % (var(L)))
    else:
        print('输入有误！')
        var_calling()
    a = int(input('继续计算方差值请输入1，需要计算其他类型请输入2，退出请输入0：'))
    if a == 0:
        return
    elif a == 1:
        var_calling()
    else:
        type_calling()


# 定义调用样本修正方差值函数的函数
def var_u_calling():
    L0 = input('继续使用刚才的数据请输入Y，使用新数据请输入N！')
    global G
    if L0 == 'Y' or L0 == 'y':
        if G != []:
            print('样本修正方差值是：%.3f\n' % (var_u(G)))
        else:
            print('刚才没有输入数据！')
            var_u_calling()
    elif L0 == 'N' or L0 == 'n':
        L = dataInput()
        print('样本修正方差值是：%.3f\n' % (var_u(L)))
        a = int(input('继续计算样本修正方差值请输入1，需要计算其他类型请输入2，退出请输入0：'))
        if a == 0:
            return
        elif a == 1:
            var_u_calling()
        else:
            type_calling()
    else:
        print('输入有误！')
        var_u_calling()
    a = int(input('继续计算样本修正方差值请输入1，需要计算其他类型请输入2，退出请输入0：'))
    if a == 0:
        return
    elif a == 1:
        var_u_calling()
    else:
        type_calling()


# 定义调用标准差值函数的函数
def stdev_calling():
    L0 = input('继续使用刚才的数据请输入Y，使用新数据请输入N！')
    global G
    if L0 == 'Y' or L0 == 'y':
        if G != []:
            print('标准差值是：%.3f\n' % (stdev(G)))
        else:
            print('刚才没有输入数据！')
            stdev_calling()
    elif L0 == 'N' or L0 == 'n':
        L = dataInput()
        print('标准差值是：%.3f\n' % (stdev(L)))
    else:
        print('输入有误！')
        stdev_calling()
    a = int(input('继续计算标准差差值请输入1，需要计算其他类型请输入2，退出请输入0：'))
    if a == 0:
        return
    elif a == 1:
        stdev_calling()
    else:
        type_calling()()


# 定义调用样本修正标准差值函数的函数
def stdev_u_calling():
    L0 = input('继续使用刚才的数据请输入Y，使用新数据请输入N！')
    global G
    if L0 == 'Y' or L0 == 'y':
        if G != []:
            print('样本修正标准差值是：%.3f\n' % (stdev_u(G)))
        else:
            print('刚才没有输入数据！')
            stdev_u_calling()
    elif L0 == 'N' or L0 == 'n':
        L = dataInput()
        print('样本修正标准差值是：%.3f\n' % (stdev_u(L)))
    else:
        print('输入有误！')
        stdev_u_calling()
    a = int(input('继续计算样本修正标准差值请输入1，需要计算其他类型请输入2，退出请输入0：'))
    if a == 0:
        return
    elif a == 1:
        stdev_u_calling()
    else:
        type_calling()


# 参数估计：
# 定义调用参数估计函数的函数
def parameterEstimate_calling():
    a = int(input('一个参数的参数估计请输入1，两个参数的参数估计请输入2，样本容量估计请输入3：'))
    if a == 1:
        oneParameterEstimate_calling()
    elif a == 2:
        twoParameterEstimate_calling()
    elif a == 3:
        n_estimate()
    else:
        print('输入有误！')
        parameterEstimate_calling()


# 定义调用一个参数的参数估计函数的函数
def oneParameterEstimate_calling():
    a = int(input('计算均值的区间估计请输入1，计算比例的区间估计请输入2，计算方差的区间估计请输入3：'))
    if a == 1:
        oneParameterEstimate_avg()
    elif a == 2:
        oneParameterEstimate_pi()
    elif a == 3:
        oneParameterEstimate_sigma2()
    else:
        print('输入有误！')
        parameterEstimate_calling()


# 定义调用两个参数的参数估计函数的函数
def twoParameterEstimate_calling():
    a = int(input('计算均值之差的区间估计请输入1，计算比例之差的区间估计请输入2，计算方差之比的区间估计请输入3：'))
    if a == 1:
        twoParameterEstimate_avg()
    elif a == 2:
        twoParameterEstimate_pi()
    elif a == 3:
        twoParameterEstimate_sigma2()
    else:
        print('输入有误！')
        parameterEstimate_calling()


# 定义调用总体均值的区间估计函数的函数
def oneParameterEstimate_avg():
    a = int(input('根据样本统计量计算请输入1，根据样本观测值计算请输入2：'))
    global G
    if a == 1:
        b = int(input('大样本且总体标准差已知请输入1；\n大样本且总体标准差未知请输入2；\n正态总体小样本且总体标准差已知请输入3；\n正态总体小样本且总体标准差未知请输入4：\n'))
        if b == 1:
            L = [float(n) for n in input('请依次输入样本容量、样本均值、置信水平、总体标准差：').split()]
            min = L[1] - scipy.stats.norm.ppf(1 - (1 - L[2]) / 2) * L[3] * pow(L[0], -0.5)
            max = L[1] + scipy.stats.norm.ppf(1 - (1 - L[2]) / 2) * L[3] * pow(L[0], -0.5)
            print('总体均值的置信区间是（%.3f，%.3f）\n' % (min, max))
        elif b == 2:
            L = [float(n) for n in input('请依次输入样本容量、样本均值、置信水平、样本标准差：').split()]
            min = L[1] - scipy.stats.norm.ppf(1 - (1 - L[2]) / 2) * L[3] * pow(L[0], -0.5)
            max = L[1] + scipy.stats.norm.ppf(1 - (1 - L[2]) / 2) * L[3] * pow(L[0], -0.5)
            print('总体均值的置信区间是（%.3f，%.3f）\n' % (min, max))
        elif b == 3:
            L = [float(n) for n in input('请依次输入样本容量、样本均值、置信水平、总体标准差：').split()]
            min = L[1] - scipy.stats.norm.ppf(1 - (1 - L[2]) / 2) * L[3] * pow(L[0], -0.5)
            max = L[1] + scipy.stats.norm.ppf(1 - (1 - L[2]) / 2) * L[3] * pow(L[0], -0.5)
            print('总体均值的置信区间是（%.3f，%.3f）\n' % (min, max))
        elif b == 4:
            L = [float(n) for n in input('请依次输入样本容量、样本均值、置信水平、样本标准差：').split()]
            max = L[1] - scipy.stats.t.ppf((1 - L[2]) / 2, (L[0] - 1)) * L[3] * pow(L[0], -0.5)
            min = L[1] + scipy.stats.t.ppf((1 - L[2]) / 2, (L[0] - 1)) * L[3] * pow(L[0], -0.5)
            print('总体均值的置信区间是（%.3f，%.3f）\n' % (min, max))
        else:
            print('输入有误！')
            oneParameterEstimate_avg()
    elif a == 2:
        L_last = input('继续使用刚才的数据请输入Y，使用新数据请输入N！')
        if L_last == 'Y' or L_last == 'y':
            if G != []:
                b = int(input('大样本且总体标准差已知请输入1；\n大样本且总体标准差未知请输入2；\n正态总体小样本且总体标准差已知请输入3；\n正态总体小样本且总体标准差未知请输入4：\n'))
                if b == 1:
                    L = [float(n) for n in input('请依次输入置信水平、总体标准差：').split()]
                    min = avg(G) - scipy.stats.norm.ppf(1 - (1 - L[0]) / 2) * L[1] * pow(len(G), -0.5)
                    max = avg(G) + scipy.stats.norm.ppf(1 - (1 - L[0]) / 2) * L[1] * pow(len(G), -0.5)
                    print('总体均值的置信区间是（%.3f，%.3f）\n' % (min, max))
                elif b == 2:
                    L = float(input('请输入置信水平：'))
                    min = avg(G) - scipy.stats.norm.ppf(1 - (1 - L) / 2) * stdev_u(G) * pow(len(G), -0.5)
                    max = avg(G) + scipy.stats.norm.ppf(1 - (1 - L) / 2) * stdev_u(G) * pow(len(G), -0.5)
                    print('总体均值的置信区间是（%.3f，%.3f）\n' % (min, max))
                elif b == 3:
                    L = [float(n) for n in input('请依次输入置信水平、总体标准差：').split()]
                    min = avg(G) - scipy.stats.norm.ppf(1 - (1 - L[0]) / 2) * L[1] * pow(len(G), -0.5)
                    max = avg(G) + scipy.stats.norm.ppf(1 - (1 - L[0]) / 2) * L[1] * pow(len(G), -0.5)
                    print('总体均值的置信区间是（%.3f，%.3f）\n' % (min, max))
                elif b == 4:
                    L = float(input('请输入置信水平：'))
                    max = avg(G) - scipy.stats.t.ppf((1 - L) / 2, (len(G) - 1)) * stdev_u(G) * pow(len(G), -0.5)
                    min = avg(G) + scipy.stats.t.ppf((1 - L) / 2, (len(G) - 1)) * stdev_u(G) * pow(len(G), -0.5)
                    print('总体均值的置信区间是（%.3f，%.3f）\n' % (min, max))
                else:
                    print('输入有误！')
                    oneParameterEstimate_avg()
            else:
                print('刚才没有输入数据！')
                oneParameterEstimate_avg()
        elif L_last == 'N' or L_last == 'n':
            L0 = dataInput()
            G = L0
            b = int(input('大样本且总体标准差已知请输入1；\n大样本且总体标准差未知请输入2；\n正态总体小样本且总体标准差已知请输入3；\n正态总体小样本且总体标准差未知请输入4：\n'))
            if b == 1:
                L = [float(n) for n in input('请依次输入置信水平、总体标准差：').split()]
                min = avg(L0) - scipy.stats.norm.ppf(1 - (1 - L[0]) / 2) * L[1] * pow(len(L0), -0.5)
                max = avg(L0) + scipy.stats.norm.ppf(1 - (1 - L[0]) / 2) * L[1] * pow(len(L0), -0.5)
                print('总体均值的置信区间是（%.3f，%.3f）\n' % (min, max))
            elif b == 2:
                L = float(input('请输入置信水平：'))
                min = avg(L0) - scipy.stats.norm.ppf(1 - (1 - L) / 2) * stdev_u(L0) * pow(len(L0), -0.5)
                max = avg(L0) + scipy.stats.norm.ppf(1 - (1 - L) / 2) * stdev_u(L0) * pow(len(L0), -0.5)
                print('总体均值的置信区间是（%.3f，%.3f）\n' % (min, max))
            elif b == 3:
                L = [float(n) for n in input('请依次输入置信水平、总体标准差：').split()]
                min = avg(L0) - scipy.stats.norm.ppf(1 - (1 - L[0]) / 2) * L[1] * pow(len(L0), -0.5)
                max = avg(L0) + scipy.stats.norm.ppf(1 - (1 - L[0]) / 2) * L[1] * pow(len(L0), -0.5)
                print('总体均值的置信区间是（%.3f，%.3f）\n' % (min, max))
            elif b == 4:
                L = float(input('请输入置信水平：'))
                max = avg(L0) - scipy.stats.t.ppf((1 - L) / 2, (len(L0) - 1)) * stdev_u(L0) * pow(len(L0), -0.5)
                min = avg(L0) + scipy.stats.t.ppf((1 - L) / 2, (len(L0) - 1)) * stdev_u(L0) * pow(len(L0), -0.5)
                print('总体均值的置信区间是（%.3f，%.3f）\n' % (min, max))
            else:
                print('输入有误！')
                oneParameterEstimate_avg()
        else:
            print('输入有误！')
            oneParameterEstimate_avg()
    else:
        print('输入有误！')
        oneParameterEstimate_avg()
    c = int(input('继续计算总体均值的置信区间请输入1，需要计算其他类型请输入2，退出请输入0：'))
    if c == 0:
        return
    elif c == 1:
        oneParameterEstimate_avg()
    else:
        type_calling()


# 定义调用总体比例的区间估计函数的函数
def oneParameterEstimate_pi():
    L = [float(n) for n in input('请依次输入样本容量、样本比例或观察量数量、置信水平：').split()]
    # 根据样本比例或观察量数量的大小判断该数值到底是样本比例还是观察者数量：观察者数量总是大于或等于1的（因为为0就没有必要计算），而样本比例总是小于1的（因为为1也没有必要计算）
    if L[1] >= 1:
        L[1] = L[1] / L[0]
        min = L[1] - scipy.stats.norm.ppf(1 - (1 - L[2]) / 2) * pow((L[1] * (1 - L[1])), 0.5) * pow(L[0], -0.5)
        max = L[1] + scipy.stats.norm.ppf(1 - (1 - L[2]) / 2) * pow((L[1] * (1 - L[1])), 0.5) * pow(L[0], -0.5)
        min = min * 100
        max = max * 100
        print('总体比例的置信区间是（%.3f%%，%.3f%%）\n' % (min, max))
    elif L[1] < 1 and L[1] > 0:
        min = L[1] - scipy.stats.norm.ppf(1 - (1 - L[2]) / 2) * pow((L[1] * (1 - L[1])), 0.5) * pow(L[0], -0.5)
        max = L[1] + scipy.stats.norm.ppf(1 - (1 - L[2]) / 2) * pow((L[1] * (1 - L[1])), 0.5) * pow(L[0], -0.5)
        min = min * 100
        max = max * 100
        print('总体比例的置信区间是（%.3f%%，%.3f%%）\n' % (min, max))
    else:
        print('输入有误！')
        oneParameterEstimate_pi()
    a = int(input('继续计算总体比例的置信区间请输入1，需要计算其他类型请输入2，退出请输入0：'))
    if a == 0:
        return
    elif a == 1:
        oneParameterEstimate_pi()
    else:
        type_calling()


# 定义调用总体方差的区间估计函数的函数
def oneParameterEstimate_sigma2():
    a = int(input('根据样本统计量计算请输入1，根据样本观测值计算请输入2：'))
    global G
    if a == 1:
        L = [float(n) for n in input('请依次输入样本容量、样本标准差或样本方差（标准差请输入“标准差值” 1，方差请输入“方差值” 2)、置信水平：').split()]
        if L[2] == 1:
            max = (L[0] - 1) * pow(L[1], 2) / scipy.stats.chi2.ppf(((1 - L[3]) / 2), (L[0] - 1))
            min = (L[0] - 1) * pow(L[1], 2) / scipy.stats.chi2.ppf((1 - ((1 - L[3]) / 2)), (L[0] - 1))
            max0 = pow(max, 0.5)
            min0 = pow(min, 0.5)
            print('总体方差的置信区间是（%.3f，%.3f）' % (min, max))
            print('总体标准差的置信区间是（%.3f，%.3f）\n' % (min0, max0))
        elif L[2] == 2:
            max = (L[0] - 1) * pow(L[1], 1) / scipy.stats.chi2.ppf(((1 - L[3]) / 2), (L[0] - 1))
            min = (L[0] - 1) * pow(L[1], 1) / scipy.stats.chi2.ppf((1 - ((1 - L[3]) / 2)), (L[0] - 1))
            max0 = pow(max, 0.5)
            min0 = pow(min, 0.5)
            print('总体方差的置信区间是（%.4f，%.4f）' % (min, max))
            print('总体标准差的置信区间是（%.3f，%.3f）\n' % (min0, max0))
        else:
            print('输入有误！')
            oneParameterEstimate_sigma2()
    elif a == 2:
        L_last = input('继续使用刚才的数据请输入Y，使用新数据请输入N！')
        if L_last == 'Y' or L_last == 'y':
            if G != []:
                L = float(input('请输入置信水平：'))
                max = (len(G) - 1) * pow(stdev_u(G), 2) / scipy.stats.chi2.ppf(((1 - L) / 2), (len(G) - 1))
                min = (len(G) - 1) * pow(stdev_u(G), 2) / scipy.stats.chi2.ppf((1 - ((1 - L) / 2)), (len(G) - 1))
                max0 = pow(max, 0.5)
                min0 = pow(min, 0.5)
                print('总体方差的置信区间是（%.3f，%.3f）' % (min, max))
                print('总体标准差的置信区间是（%.3f，%.3f）\n' % (min0, max0))
            else:
                print('刚才没有输入数据！')
                oneParameterEstimate_sigma2()
        elif L_last == 'N' or L_last == 'n':
            L0 = dataInput()
            G = L0
            L = float(input('请输入置信水平：'))
            max = (len(L0) - 1) * pow(stdev_u(L0), 2) / scipy.stats.chi2.ppf(((1 - L) / 2), (len(L0) - 1))
            min = (len(L0) - 1) * pow(stdev_u(L0), 2) / scipy.stats.chi2.ppf((1 - ((1 - L) / 2)), (len(L0) - 1))
            max0 = pow(max, 0.5)
            min0 = pow(min, 0.5)
            print('总体方差的置信区间是（%.3f，%.3f）' % (min, max))
            print('总体标准差的置信区间是（%.3f，%.3f）\n' % (min0, max0))
    else:
        print('输入有误！')
        oneParameterEstimate_sigma2()
    b = int(input('继续计算总体方差的置信区间请输入1，需要计算其他类型请输入2，退出请输入0：'))
    if b == 0:
        return
    elif b == 1:
        oneParameterEstimate_sigma2()
    else:
        type_calling()


# 定义调用两个总体均值之差的区间估计函数的函数
def twoParameterEstimate_avg():
    a = int(input('根据样本统计量计算请输入1，根据样本观测值计算请输入2：'))
    global G1
    global G2
    if a == 1:
        b = int(input('独立样本请输入1，匹配样本请输入2：'))
        if b == 1:
            c = int(input('大样本且总体标准差已知请输入1；\n大样本且总体标准差未知请输入2；\n正态总体小样本且总体标准差已知请输入3；\n正态总体小样本且总体标准差未知请输入4：\n'))
            if c == 1:
                L1 = [float(n) for n in input('请依次输入总体1的样本容量、总体1的样本均值、总体1的标准差：').split()]
                L2 = [float(n) for n in input('请依次输入总体2的样本容量、总体2的样本均值、总体2的标准差：').split()]
                L = float(input('请输入置信水平：'))
                min = (L1[1] - L2[1]) - scipy.stats.norm.ppf(1 - (1 - L) / 2) * pow(
                    (pow(L1[2], 2) / L1[0] + pow(L2[2], 2) / L2[0]), 0.5)
                max = (L1[1] - L2[1]) + scipy.stats.norm.ppf(1 - (1 - L) / 2) * pow(
                    (pow(L1[2], 2) / L1[0] + pow(L2[2], 2) / L2[0]), 0.5)
                print('总体均值之差的置信区间是（%.3f，%.3f）\n' % (min, max))
            elif c == 2:
                L1 = [float(n) for n in input('请依次输入总体1的样本容量、总体1的样本均值、总体1的样本标准差：').split()]
                L2 = [float(n) for n in input('请依次输入总体2的样本容量、总体2的样本均值、总体2的样本标准差：').split()]
                L = float(input('请输入置信水平：'))
                min = (L1[1] - L2[1]) - scipy.stats.norm.ppf(1 - (1 - L) / 2) * pow(
                    (pow(L1[2], 2) / L1[0] + pow(L2[2], 2) / L2[0]), 0.5)
                max = (L1[1] - L2[1]) + scipy.stats.norm.ppf(1 - (1 - L) / 2) * pow(
                    (pow(L1[2], 2) / L1[0] + pow(L2[2], 2) / L2[0]), 0.5)
                print('总体均值之差的置信区间是（%.3f，%.3f）\n' % (min, max))
            elif c == 3:
                L1 = [float(n) for n in input('请依次输入总体1的样本容量、总体1的样本均值、总体1的标准差：').split()]
                L2 = [float(n) for n in input('请依次输入总体2的样本容量、总体2的样本均值、总体2的标准差：').split()]
                L = float(input('请输入置信水平：'))
                min = (L1[1] - L2[1]) - scipy.stats.norm.ppf(1 - (1 - L) / 2) * pow(
                    (pow(L1[2], 2) / L1[0] + pow(L2[2], 2) / L2[0]), 0.5)
                max = (L1[1] - L2[1]) + scipy.stats.norm.ppf(1 - (1 - L) / 2) * pow(
                    (pow(L1[2], 2) / L1[0] + pow(L2[2], 2) / L2[0]), 0.5)
                print('总体均值之差的置信区间是（%.3f，%.3f）\n' % (min, max))
            elif c == 4:
                d = int(input('两个总体的标准差未知但相等，请输入1；未知且不相等，请输入2：'))
                if d == 1:
                    L1 = [float(n) for n in input('请依次输入总体1的样本容量、总体1的样本均值、总体1的样本标准差：').split()]
                    L2 = [float(n) for n in input('请依次输入总体2的样本容量、总体2的样本均值、总体2的样本标准差：').split()]
                    L = float(input('请输入置信水平：'))
                    sp = pow(((L1[0] - 1) * pow(L1[2], 2) + (L2[0] - 1) * pow(L2[2], 2)) / (L1[0] + L2[0] - 2), 0.5)
                    max = (L1[1] - L2[1]) - scipy.stats.t.ppf((1 - L) / 2, (L1[0] + L2[0] - 2)) * sp * pow(
                        (1 / L1[0] + 1 / L2[0]), 0.5)
                    min = (L1[1] - L2[1]) + scipy.stats.t.ppf((1 - L) / 2, (L1[0] + L2[0] - 2)) * sp * pow(
                        (1 / L1[0] + 1 / L2[0]), 0.5)
                    # print('sp是%.3f，scipy.stats.t.ppf((1-L)/2,(L1[0]+L2[0]-2))是%.3f'%(sp, scipy.stats.t.ppf((1-L)/2,(L1[0]+L2[0]-2))))
                    print('总体均值之差的置信区间是（%.3f，%.3f）\n' % (min, max))
                elif d == 2:
                    L1 = [float(n) for n in input('请依次输入总体1的样本容量、总体1的样本均值、总体1的样本标准差：').split()]
                    L2 = [float(n) for n in input('请依次输入总体2的样本容量、总体2的样本均值、总体2的样本标准差：').split()]
                    L = float(input('请输入置信水平：'))
                    v = pow((pow(L1[2], 2) / L1[0] + pow(L2[2], 2) / L2[0]), 2) / (
                                pow((pow(L1[2], 2) / L1[0]), 2) / (L1[0] - 1) + pow((pow(L2[2], 2) / L2[0]), 2) / (
                                    L2[0] - 1))
                    max = (L1[1] - L2[1]) - scipy.stats.t.ppf((1 - L) / 2, int(v)) * pow(
                        (pow(L1[2], 2) / L1[0] + pow(L2[2], 2) / L2[0]), 0.5)
                    min = (L1[1] - L2[1]) + scipy.stats.t.ppf((1 - L) / 2, int(v)) * pow(
                        (pow(L1[2], 2) / L1[0] + pow(L2[2], 2) / L2[0]), 0.5)
                    print('总体均值之差的置信区间是（%.3f，%.3f）\n' % (min, max))
                else:
                    print('输入有误！')
                    twoParameterEstimate_avg()
            else:
                print('输入有误！')
                twoParameterEstimate_avg()
        # 匹配样本
        elif b == 2:
            c = int(input('大样本请输入1；小样本且两总体各观察值的配对差d服从正态分布请输入2：'))
            if c == 1:
                L = [float(n) for n in input('请依次输入样本容量、配对差的平均值、总体或样本配对差的标准差、置信水平：').split()]
                min = L[1] - scipy.stats.norm.ppf(1 - (1 - L[3]) / 2) * L[2] * pow(L[0], -0.5)
                max = L[1] + scipy.stats.norm.ppf(1 - (1 - L[3]) / 2) * L[2] * pow(L[0], -0.5)
                print('总体均值之差的置信区间是（%.3f，%.3f）\n' % (min, max))
            elif c == 2:
                L = [float(n) for n in input('请依次输入样本容量、配对差的平均值、总体或样本配对差的标准差、置信水平：').split()]
                max = L[1] - scipy.stats.t.ppf((1 - L[3]) / 2, (L[0] - 1)) * L[2] * pow(L[0], -0.5)
                min = L[1] + scipy.stats.t.ppf((1 - L[3]) / 2, (L[0] - 1)) * L[2] * pow(L[0], -0.5)
                print('总体均值之差的置信区间是（%.3f，%.3f）\n' % (min, max))
            else:
                print('输入有误！')
                twoParameterEstimate_avg()
        else:
            print('输入有误！')
            twoParameterEstimate_avg()
    elif a == 2:
        L_last = input('继续使用刚才的数据请输入Y，使用新数据请输入N！')
        if L_last == 'Y' or L_last == 'y':
            if G1 != [] and G2 != []:
                b = int(input('独立样本请输入1，匹配样本请输入2：'))
                if b == 1:
                    c = int(input('大样本且总体标准差已知请输入1；\n大样本且总体标准差未知请输入2；\n正态总体小样本且总体标准差已知请输入3；\n正态总体小样本且总体标准差未知请输入4：\n'))
                    if c == 1:
                        L = [float(n) for n in input('请依次输入置信水平、总体1的标准差、总体2的标准差：').split()]
                        min = (avg(G1) - avg(G2)) - scipy.stats.norm.ppf(1 - (1 - L[0]) / 2) * pow(
                            (pow(L[1], 2) / len(G1) + pow(L[2], 2) / len(G2)), 0.5)
                        max = (avg(G1) - avg(G2)) + scipy.stats.norm.ppf(1 - (1 - L[0]) / 2) * pow(
                            (pow(L[1], 2) / len(G1) + pow(L[2], 2) / len(G2)), 0.5)
                        print('总体均值之差的置信区间是（%.3f，%.3f）\n' % (min, max))
                    elif c == 2:
                        L = float(input('请输入置信水平：'))
                        min = (avg(G1) - avg(G2)) - scipy.stats.norm.ppf(1 - (1 - L) / 2) * pow(
                            (pow(stdev_u(G1), 2) / len(G1) + pow(stdev_u(G2), 2) / len(G2)), 0.5)
                        max = (avg(G1) - avg(G2)) + scipy.stats.norm.ppf(1 - (1 - L) / 2) * pow(
                            (pow(stdev_u(G1), 2) / len(G1) + pow(stdev_u(G2), 2) / len(G2)), 0.5)
                        print('总体均值之差的置信区间是（%.3f，%.3f）\n' % (min, max))
                    elif c == 3:
                        L = [float(n) for n in input('请依次输入置信水平、总体1的标准差、总体2的标准差：').split()]
                        min = (avg(G1) - avg(G2)) - scipy.stats.norm.ppf(1 - (1 - L[0]) / 2) * pow(
                            (pow(L[1], 2) / len(G1) + pow(L[2], 2) / len(G2)), 0.5)
                        max = (avg(G1) - avg(G2)) + scipy.stats.norm.ppf(1 - (1 - L[0]) / 2) * pow(
                            (pow(L[1], 2) / len(G1) + pow(L[2], 2) / len(G2)), 0.5)
                        print('总体均值之差的置信区间是（%.3f，%.3f）\n' % (min, max))
                    elif c == 4:
                        d = int(input('两个总体的标准差未知但相等，请输入1；未知且不相等，请输入2：'))
                        if d == 1:
                            L = float(input('请输入置信水平：'))
                            sp = pow((((len(G1) - 1) * pow(stdev_u(G1), 2) + (len(G2) - 1) * pow(stdev_u(G2), 2)) / (
                                        len(G1) + len(G2) - 2)), 0.5)
                            max = (avg(G1) - avg(G2)) - scipy.stats.t.ppf((1 - L) / 2,
                                                                          (len(G1) + len(G2) - 2)) * sp * pow(
                                (1 / len(G1) + 1 / len(G2)), 0.5)
                            min = (avg(G1) - avg(G2)) + scipy.stats.t.ppf((1 - L) / 2,
                                                                          (len(G1) + len(G2) - 2)) * sp * pow(
                                (1 / len(G1) + 1 / len(G2)), 0.5)
                            print('总体均值之差的置信区间是（%.3f，%.3f）\n' % (min, max))
                        elif d == 2:
                            L = float(input('请输入置信水平：'))
                            v = pow((pow(stdev_u(G1), 2) / len(G1) + pow(stdev_u(G2), 2) / len(G2)), 2) / (
                                        pow((pow(stdev_u(G1), 2) / len(G1)), 2) / (len(G1) - 1) + pow(
                                    (pow(stdev_u(G2), 2) / len(G2)), 2) / (len(G2) - 1))
                            max = (avg(G1) - avg(G2)) - scipy.stats.t.ppf((1 - L) / 2, int(v)) * pow(
                                (pow(stdev_u(G1), 2) / len(G1) + pow(stdev_u(G2), 2) / len(G2)), 0.5)
                            min = (avg(G1) - avg(G2)) + scipy.stats.t.ppf((1 - L) / 2, int(v)) * pow(
                                (pow(stdev_u(G1), 2) / len(G1) + pow(stdev_u(G2), 2) / len(G2)), 0.5)
                            print('总体均值之差的置信区间是（%.3f，%.3f）\n' % (min, max))
                        else:
                            print('输入有误！')
                            twoParameterEstimate_avg()
                    else:
                        print('输入有误！')
                        twoParameterEstimate_avg()
                # 匹配样本
                elif b == 2:
                    c = int(input('大样本请输入1；小样本且两总体各观察值的配对差d服从正态分布请输入2：'))
                    if c == 1:
                        L = float(input('请输入置信水平：'))
                        min = avg(delta(G1, G2)) - scipy.stats.norm.ppf(1 - (1 - L) / 2) * stdev_u(delta(G1, G2)) * pow(
                            len(G1), -0.5)
                        max = avg(delta(G1, G2)) + scipy.stats.norm.ppf(1 - (1 - L) / 2) * stdev_u(delta(G1, G2)) * pow(
                            len(G1), -0.5)
                        print('总体均值之差的置信区间是（%.3f，%.3f）\n' % (min, max))
                    elif c == 2:
                        L = float(input('请输入置信水平：'))
                        max = avg(delta(G1, G2)) - scipy.stats.t.ppf((1 - L) / 2, len(G1) - 1) * stdev_u(
                            delta(G1, G2)) * pow(len(G1), -0.5)
                        min = avg(delta(G1, G2)) + scipy.stats.t.ppf((1 - L) / 2, len(G1) - 1) * stdev_u(
                            delta(G1, G2)) * pow(len(G1), -0.5)
                        print('总体均值之差的置信区间是（%.3f，%.3f）\n' % (min, max))
                    else:
                        print('输入有误！')
                        twoParameterEstimate_avg()
                else:
                    print('输入有误！')
                    twoParameterEstimate_avg()
            else:
                print('刚才没有输入数据！')
                twoParameterEstimate_avg()
        elif L_last == 'N' or L_last == 'n':
            L1 = dataInput()
            L2 = dataInput()
            G1 = L1
            G2 = L2
            b = int(input('独立样本请输入1，匹配样本请输入2：'))
            if b == 1:
                c = int(input('大样本且总体标准差已知请输入1；\n大样本且总体标准差未知请输入2；\n正态总体小样本且总体标准差已知请输入3；\n正态总体小样本且总体标准差未知请输入4：\n'))
                if c == 1:
                    L = [float(n) for n in input('请依次输入置信水平、总体1的标准差、总体2的标准差：').split()]
                    min = (avg(L1) - avg(L2)) - scipy.stats.norm.ppf(1 - (1 - L[0]) / 2) * pow(
                        (pow(L[1], 2) / len(L1) + pow(L[2], 2) / len(L2)), 0.5)
                    max = (avg(L1) - avg(L2)) + scipy.stats.norm.ppf(1 - (1 - L[0]) / 2) * pow(
                        (pow(L[1], 2) / len(L1) + pow(L[2], 2) / len(L2)), 0.5)
                    print('总体均值之差的置信区间是（%.3f，%.3f）\n' % (min, max))
                elif c == 2:
                    L = float(input('请输入置信水平：'))
                    min = (avg(L1) - avg(L2)) - scipy.stats.norm.ppf(1 - (1 - L) / 2) * pow(
                        (pow(stdev_u(L1), 2) / len(L1) + pow(stdev_u(L2), 2) / len(L2)), 0.5)
                    max = (avg(L1) - avg(L2)) + scipy.stats.norm.ppf(1 - (1 - L) / 2) * pow(
                        (pow(stdev_u(L1), 2) / len(L1) + pow(stdev_u(L2), 2) / len(L2)), 0.5)
                    print('总体均值之差的置信区间是（%.3f，%.3f）\n' % (min, max))
                elif c == 3:
                    L = [float(n) for n in input('请依次输入置信水平、总体1的标准差、总体2的标准差：').split()]
                    min = (avg(L1) - avg(L2)) - scipy.stats.norm.ppf(1 - (1 - L[0]) / 2) * pow(
                        (pow(L[1], 2) / len(L1) + pow(L[2], 2) / len(L2)), 0.5)
                    max = (avg(L1) - avg(L2)) + scipy.stats.norm.ppf(1 - (1 - L[0]) / 2) * pow(
                        (pow(L[1], 2) / len(L1) + pow(L[2], 2) / len(L2)), 0.5)
                    print('总体均值之差的置信区间是（%.3f，%.3f）\n' % (min, max))
                elif c == 4:
                    d = int(input('两个总体的标准差未知但相等，请输入1；未知且不相等，请输入2：'))
                    if d == 1:
                        L = float(input('请输入置信水平：'))
                        sp = pow((((len(L1) - 1) * pow(stdev_u(L1), 2) + (len(L2) - 1) * pow(stdev_u(L2), 2)) / (
                                    len(L1) + len(L2) - 2)), 0.5)
                        max = (avg(L1) - avg(L2)) - scipy.stats.t.ppf((1 - L) / 2, (len(L1) + len(L2) - 2)) * sp * pow(
                            (1 / len(L1) + 1 / len(L2)), 0.5)
                        min = (avg(L1) - avg(L2)) + scipy.stats.t.ppf((1 - L) / 2, (len(L1) + len(L2) - 2)) * sp * pow(
                            (1 / len(L1) + 1 / len(L2)), 0.5)
                        print('总体均值之差的置信区间是（%.3f，%.3f）\n' % (min, max))
                    elif d == 2:
                        L = float(input('请输入置信水平：'))
                        v = pow((pow(stdev_u(L1), 2) / len(L1) + pow(stdev_u(L2), 2) / len(L2)), 2) / (
                                    pow((pow(stdev_u(L1), 2) / len(L1)), 2) / (len(L1) - 1) + pow(
                                (pow(stdev_u(L2), 2) / len(L2)), 2) / (len(L2) - 1))
                        max = (avg(L1) - avg(L2)) - scipy.stats.t.ppf((1 - L) / 2, int(v)) * pow(
                            (pow(stdev_u(L1), 2) / len(L1) + pow(stdev_u(L2), 2) / len(L2)), 0.5)
                        min = (avg(L1) - avg(L2)) + scipy.stats.t.ppf((1 - L) / 2, int(v)) * pow(
                            (pow(stdev_u(L1), 2) / len(L1) + pow(stdev_u(L2), 2) / len(L2)), 0.5)
                        print('总体均值之差的置信区间是（%.3f，%.3f）\n' % (min, max))
                    else:
                        print('输入有误！')
                        twoParameterEstimate_avg()
                else:
                    print('输入有误！')
                    twoParameterEstimate_avg()
            # 匹配样本
            elif b == 2:
                c = int(input('大样本请输入1；小样本且两总体各观察值的配对差d服从正态分布请输入2：'))
                if c == 1:
                    L = float(input('请输入置信水平：'))
                    min = avg(delta(L1, L2)) - scipy.stats.norm.ppf(1 - (1 - L) / 2) * stdev_u(delta(L1, L2)) * pow(
                        len(L1), -0.5)
                    max = avg(delta(L1, L2)) + scipy.stats.norm.ppf(1 - (1 - L) / 2) * stdev_u(delta(L1, L2)) * pow(
                        len(L1), -0.5)
                    print('总体均值之差的置信区间是（%.3f，%.3f）\n' % (min, max))
                elif c == 2:
                    L = float(input('请输入置信水平：'))
                    max = avg(delta(L1, L2)) - scipy.stats.t.ppf((1 - L) / 2, len(L1) - 1) * stdev_u(
                        delta(L1, L2)) * pow(len(L1), -0.5)
                    min = avg(delta(L1, L2)) + scipy.stats.t.ppf((1 - L) / 2, len(L1) - 1) * stdev_u(
                        delta(L1, L2)) * pow(len(L1), -0.5)
                    print('总体均值之差的置信区间是（%.3f，%.3f）\n' % (min, max))
                else:
                    print('输入有误！')
                    twoParameterEstimate_avg()
            else:
                print('输入有误！')
                twoParameterEstimate_avg()
        else:
            print('输入有误！')
            twoParameterEstimate_avg()
    else:
        print('输入有误！')
        twoParameterEstimate_avg()
    d = int(input('继续计算总体均值之差的置信区间请输入1，需要计算其他类型请输入2，退出请输入0：'))
    if d == 0:
        return
    elif d == 1:
        twoParameterEstimate_avg()
    else:
        type_calling()


# 定义调用两个总体比例之差的区间估计函数的函数
def twoParameterEstimate_pi():
    L = [float(n) for n in input('请依次输入样本1容量、样本1比例或观察量数量、样本2容量、样本2比例或观察量数量、置信水平：').split()]
    # 根据样本比例或观察量数量的大小判断该数值到底是样本比例还是观察者数量：观察者数量总是大于或等于1的（因为为0就没有必要计算），而样本比例总是小于1的（因为为1也没有必要计算）
    if L[1] >= 1:
        L[1] = L[1] / L[0]
    elif L[1] < 1 and L[1] > 0:
        L[1] = L[1]
    else:
        print('样本1输入有误！')
        twoParameterEstimate_pi()
    if L[3] >= 1:
        L[3] = L[3] / L[2]
    elif L[3] < 1 and L[3] > 0:
        L[3] = L[3]
    else:
        print('样本2输入有误！')
        twoParameterEstimate_pi()
    min = (L[1] - L[3]) - scipy.stats.norm.ppf(1 - (1 - L[4]) / 2) * pow(
        ((L[1] * (1 - L[1])) / L[0] + (L[3] * (1 - L[3])) / L[2]), 0.5)
    max = (L[1] - L[3]) + scipy.stats.norm.ppf(1 - (1 - L[4]) / 2) * pow(
        ((L[1] * (1 - L[1])) / L[0] + (L[3] * (1 - L[3])) / L[2]), 0.5)
    min = min * 100
    max = max * 100
    print('总体比例之差的置信区间是（%.3f%%，%.3f%%）\n' % (min, max))
    a = int(input('继续计算总体比例之差的置信区间请输入1，需要计算其他类型请输入2，退出请输入0：'))
    if a == 0:
        return
    elif a == 1:
        twoParameterEstimate_pi()
    else:
        type_calling()


# 定义调用两个总体方差之比的区间估计函数的函数
def twoParameterEstimate_sigma2():
    a = int(input('根据样本统计量计算请输入1，根据样本观测值计算请输入2：'))
    global G1, G2
    if a == 1:
        L1 = [float(n) for n in input('请依次输入样本1容量、样本1标准差或样本方差（标准差请输入“标准差值” 1，方差请输入“方差值” 2)：').split()]
        L2 = [float(n) for n in input('请依次输入样本2容量、样本2标准差或样本方差（标准差请输入“标准差值” 1，方差请输入“方差值” 2)：').split()]
        L = float(input('请输入置信水平：'))
        if L1[2] == 1 and L2[2] == 1:
            max = pow(L1[1], 2) / pow(L2[1], 2) / scipy.stats.f.ppf(((1 - L) / 2), (L1[0] - 1), (L2[0] - 1))
            min = pow(L1[1], 2) / pow(L2[1], 2) / scipy.stats.f.ppf(1 - ((1 - L) / 2), (L1[0] - 1), (L2[0] - 1))
            max0 = pow(max, 0.5)
            min0 = pow(min, 0.5)
            print('总体方差之比的置信区间是（%.4f，%.4f）' % (min, max))
            print('总体标准差之比的置信区间是（%.4f，%.4f）\n' % (min0, max0))
        elif L1[2] == 2 and L2[2] == 2:
            max = pow(L1[1], 1) / pow(L2[1], 1) / scipy.stats.f.ppf(((1 - L) / 2), (L1[0] - 1), (L2[0] - 1))
            min = pow(L1[1], 1) / pow(L2[1], 1) / scipy.stats.f.ppf(1 - ((1 - L) / 2), (L1[0] - 1), (L2[0] - 1))
            max0 = pow(max, 0.5)
            min0 = pow(min, 0.5)
            print('总体方差之比的置信区间是（%.4f，%.4f）' % (min, max))
            print('总体标准差之比的置信区间是（%.4f，%.4f）\n' % (min0, max0))
        else:
            print('输入有误！')
            twoParameterEstimate_sigma2()
    elif a == 2:
        L_last = input('继续使用刚才的数据请输入Y，使用新数据请输入N！')
        if L_last == 'Y' or L_last == 'y':
            if G1 != [] and G2 != []:
                L = float(input('请输入置信水平：'))
                max = var_u(G1) / var_u(G2) / scipy.stats.f.ppf(((1 - L) / 2), (len(G1) - 1), (len(G2) - 1))
                min = var_u(G1) / var_u(G2) / scipy.stats.f.ppf(1 - ((1 - L) / 2), (len(G1) - 1), (len(G2) - 1))
                max0 = pow(max, 0.5)
                min0 = pow(min, 0.5)
                print('总体方差之比的置信区间是（%.4f，%.4f）' % (min, max))
                print('总体标准差之比的置信区间是（%.4f，%.4f）\n' % (min0, max0))
            else:
                print('刚才没有输入数据！')
                twoParameterEstimate_sigma2()
        elif L_last == 'N' or L_last == 'n':
            L1 = dataInput()
            L2 = dataInput()
            G1 = L1
            G2 = L2
            L = float(input('请输入置信水平：'))
            max = var_u(L1) / var_u(L2) / scipy.stats.f.ppf(((1 - L) / 2), (len(L1) - 1), (len(L2) - 1))
            min = var_u(L1) / var_u(L2) / scipy.stats.f.ppf(1 - ((1 - L) / 2), (len(L1) - 1), (len(L2) - 1))
            max0 = pow(max, 0.5)
            min0 = pow(min, 0.5)
            print('总体方差之比的置信区间是（%.4f，%.4f）' % (min, max))
            print('总体标准差之比的置信区间是（%.4f，%.4f）\n' % (min0, max0))
    else:
        print('输入有误！')
        twoParameterEstimate_sigma2()
    b = int(input('继续计算总体方差之比的置信区间请输入1，需要计算其他类型请输入2，退出请输入0：'))
    if b == 0:
        return
    elif b == 1:
        twoParameterEstimate_sigma2()
    else:
        type_calling()


# 定义确定样本容量的函数
def n_estimate():
    a = int(input('估计总体均值时样本量的确定请输入1；估计总体比例时样本量的确定请输入2：'))
    if a == 1:
        L = [float(n) for n in input('请依次输入总体标准差、样本估计误差、置信水平：').split()]
        n = pow(L[0], 2) * pow(scipy.stats.norm.ppf(1 - (1 - L[2]) / 2), 2) / pow(L[1], 2)
        if n % 1 == 0:
            n = int(n)
        else:
            n = math.ceil(n)
        print('所需样本容量为：%d\n' % n)
    elif a == 2:
        L = [float(n) for n in input('请依次输入总体或样本比例（未知时取0.5）、样本估计误差、置信水平：').split()]
        n = L[0] * (1 - L[0]) * pow(scipy.stats.norm.ppf(1 - (1 - L[2]) / 2), 2) / pow(L[1], 2)
        if n % 1 == 0:
            n = int(n)
        else:
            n = math.ceil(n)
        print('所需样本容量为：%d\n' % n)
    a = int(input('继续计算样本容量请输入1，需要计算其他类型请输入2，退出请输入0：'))
    if a == 0:
        return
    elif a == 1:
        n_estimate()
    else:
        type_calling()


# 假设检验：
# 定义调用假设检验函数的函数
def hypothesisTest_calling():
    a = int(input('一个总体参数的检验请输入1，两个总体参数的检验请输入2：'))
    if a == 1:
        oneHypothesisTest_calling()
    elif a == 2:
        twoHypothesisTest_calling()
    else:
        print('输入有误！')
        hypothesisTest_calling()


# 定义调用一个参数的假设检验函数的函数
def oneHypothesisTest_calling():
    a = int(input('总体均值的检验请输入1，总体比例的检验请输入2，总体方差的检验请输入3：'))
    if a == 1:
        oneHypothesisTest_avg()
    elif a == 2:
        oneHypothesisTest_pi()
    elif a == 3:
        oneHypothesisTest_sigma2()
    else:
        print('输入有误！')
        oneHypothesisTest_calling()


# 定义调用两个参数的假设检验函数的函数
def twoHypothesisTest_calling():
    a = int(input('总体均值之差的检验请输入1，总体比例之差的检验请输入2，总体方差之比的检验请输入3：'))
    if a == 1:
        twoHypothesisTest_avg()
    elif a == 2:
        twoHypothesisTest_pi()
    elif a == 3:
        twoHypothesisTest_sigma2()
    else:
        print('输入有误！')
        twoHypothesisTest_calling()


# 一个参数总体均值的假设检验
def oneHypothesisTest_avg():
    a = int(input('双侧检验请输入1，左侧检验请输入2，右侧检验请输入3：'))
    b = int(input('大样本且总体标准差已知请输入1；\n大样本且总体标准差未知请输入2；\n小样本且总体标准差已知请输入3；\n小样本且总体标准差未知请输入4：\n'))
    c = int(input('直接输入样本统计量请输入1，输入样本观测值请输入2：'))
    if a == 1:
        if b == 1:
            if c == 1:
                L = [float(n) for n in input('请依次输入样本容量、样本均值、假设均值、总体标准差、显著性水平：').split()]
                z = (L[1] - L[2]) / (L[3] / pow(L[0], 0.5))
                z0 = scipy.stats.norm.ppf(1 - L[4] / 2)
                z1 = (-1) * z0
                P = 2 * (1 - scipy.stats.norm.cdf(abs(z)))
                if abs(z) > abs(z0):
                    print(
                        '******\nz = %.3f，z0 = %.3f或%.3f，P = %.5f\n因为 abs(z) > abs(z0)，或因为 P < alpha = %.2f，所以拒绝原假设H0！\n******' % (
                        z, z0, z1, P, L[4]))
                elif abs(z) < abs(z0):
                    print(
                        '******\nz = %.3f，z0 = %.3f或%.3f，P = %.5f\n因为 abs(z) < abs(z0)，或因为 P > alpha = %.2f，所以拒绝备择假设H1！\n******' % (
                        z, z0, z1, P, L[4]))
                else:
                    print('******\n怎么会这么巧！\n******')
            elif c == 2:
                L0 = dataInput()
                L = [float(n) for n in input('请依次输入假设均值、总体标准差、显著性水平：').split()]
                z = (avg(L0) - L[0]) / L[1] / pow(len(L0), 0.5)
                z0 = scipy.stats.norm.ppf(1 - L[2] / 2)
                z1 = (-1) * z0
                P = 2 * (1 - scipy.stats.norm.cdf(abs(z)))
                if abs(z) > abs(z0):
                    print(
                        '******\nz = %.3f，z0 = %.3f或%.3f，P = %.5f\n因为 abs(z) > abs(z0)，或因为 P < alpha = %.2f，所以拒绝原假设H0！\n******' % (
                        z, z0, z1, P, L[2]))
                elif abs(z) < abs(z0):
                    print(
                        '******\nz = %.3f，z0 = %.3f或%.3f，P = %.5f\n因为 abs(z) < abs(z0)，或因为 P > alpha = %.2f，所以拒绝备择假设H1！\n******' % (
                        z, z0, z1, P, L[2]))
                else:
                    print('******\n怎么会这么巧！\n******')
            else:
                print('输入有误！')
                oneHypothesisTest_avg()
        elif b == 2:
            if c == 1:
                L = [float(n) for n in input('请依次输入样本容量、样本均值、假设均值、样本标准差、显著性水平：').split()]
                z = (L[1] - L[2]) / (L[3] / pow(L[0], 0.5))
                z0 = scipy.stats.norm.ppf(1 - L[4] / 2)
                z1 = (-1) * z0
                P = 2 * (1 - scipy.stats.norm.cdf(abs(z)))
                if abs(z) > abs(z0):
                    print(
                        '******\nz = %.3f，z0 = %.3f或%.3f，P = %.5f\n因为 abs(z) > abs(z0)，或因为 P < alpha = %.2f，所以拒绝原假设H0！\n******' % (
                        z, z0, z1, P, L[4]))
                elif abs(z) < abs(z0):
                    print(
                        '******\nz = %.3f，z0 = %.3f或%.3f，P = %.5f\n因为 abs(z) < abs(z0)，或因为 P > alpha = %.2f，所以拒绝备择假设H1！\n******' % (
                        z, z0, z1, P, L[4]))
                else:
                    print('******\n怎么会这么巧！\n******')
            elif c == 2:
                L0 = dataInput()
                L = [float(n) for n in input('请依次输入假设均值、显著性水平：').split()]
                z = (avg(L0) - L[0]) / stdev_u(L0) / pow(len(L0), 0.5)
                z0 = scipy.stats.norm.ppf(1 - L[1] / 2)
                z1 = (-1) * z0
                P = 2 * (1 - scipy.stats.norm.cdf(abs(z)))
                if abs(z) > abs(z0):
                    print(
                        '******\nz = %.3f，z0 = %.3f或%.3f，P = %.5f\n因为 abs(z) > abs(z0)，或因为 P < alpha = %.2f，所以拒绝原假设H0！\n******' % (
                        z, z0, z1, P, L[1]))
                elif abs(z) < abs(z0):
                    print(
                        '******\nz = %.3f，z0 = %.3f或%.3f，P = %.5f\n因为 abs(z) < abs(z0)，或因为 P > alpha = %.2f，所以拒绝备择假设H1！\n******' % (
                        z, z0, z1, P, L[1]))
                else:
                    print('******\n怎么会这么巧！\n******')
            else:
                print('输入有误！')
                oneHypothesisTest_avg()
        elif b == 3:
            if c == 1:
                L = [float(n) for n in input('请依次输入样本容量、样本均值、假设均值、总体标准差、显著性水平：').split()]
                z = (L[1] - L[2]) / (L[3] / pow(L[0], 0.5))
                z0 = scipy.stats.norm.ppf(1 - L[4] / 2)
                z1 = (-1) * z0
                P = 2 * (1 - scipy.stats.norm.cdf(abs(z)))
                if abs(z) > abs(z0):
                    print(
                        '******\nz = %.3f，z0 = %.3f或%.3f，P = %.5f\n因为 abs(z) > abs(z0)，或因为 P < alpha = %.2f，所以拒绝原假设H0！\n******' % (
                        z, z0, z1, P, L[4]))
                elif abs(z) < abs(z0):
                    print(
                        '******\nz = %.3f，z0 = %.3f或%.3f，P = %.5f\n因为 abs(z) < abs(z0)，或因为 P > alpha = %.2f，所以拒绝备择假设H1！\n******' % (
                        z, z0, z1, P, L[4]))
                else:
                    print('******\n怎么会这么巧！\n******')
            elif c == 2:
                L0 = dataInput()
                L = [float(n) for n in input('请依次输入假设均值、总体标准差、显著性水平：').split()]
                z = (avg(L0) - L[0]) / L[1] / pow(len(L0), 0.5)
                z0 = scipy.stats.norm.ppf(1 - L[2] / 2)
                z1 = (-1) * z0
                P = 2 * (1 - scipy.stats.norm.cdf(abs(z)))
                if abs(z) > abs(z0):
                    print(
                        '******\nz = %.3f，z0 = %.3f或%.3f，P = %.5f\n因为 abs(z) > abs(z0)，或因为 P < alpha = %.2f，所以拒绝原假设H0！\n******' % (
                        z, z0, z1, P, L[2]))
                elif abs(z) < abs(z0):
                    print(
                        '******\nz = %.3f，z0 = %.3f或%.3f，P = %.5f\n因为 abs(z) < abs(z0)，或因为 P > alpha = %.2f，所以拒绝备择假设H1！\n******' % (
                        z, z0, z1, P, L[2]))
                else:
                    print('******\n怎么会这么巧！\n******')
            else:
                print('输入有误！')
                oneHypothesisTest_avg()
        elif b == 4:
            if c == 1:
                L = [float(n) for n in input('请依次输入样本容量、样本均值、假设均值、样本标准差、显著性水平：').split()]
                t = (L[1] - L[2]) / (L[3] / pow(L[0], 0.5))
                t0 = scipy.stats.t.ppf(L[4] / 2, (L[0] - 1)) * (-1)
                t1 = (-1) * t0
                P = 2 * (1 - scipy.stats.t.cdf(abs(t), (L[0] - 1)))
                if abs(t) > abs(t0):
                    print(
                        '******\nt = %.3f，t0 = %.3f或%.3f，P = %.5f\n因为 abs(t) > abs(t0)，或因为 P < alpha = %.2f，所以拒绝原假设H0！\n******' % (
                        t, t0, t1, P, L[4]))
                elif abs(t) < abs(t0):
                    print(
                        '******\nt = %.3f，t0 = %.3f或%.3f，P = %.5f\n因为 abs(t) < abs(t0)，或因为 P > alpha = %.2f，所以拒绝备择假设H1！\n******' % (
                        t, t0, t1, P, L[4]))
                else:
                    print('******\n怎么会这么巧！\n******')
            elif c == 2:
                L0 = dataInput()
                L = [float(n) for n in input('请依次输入假设均值、显著性水平：').split()]
                t = (avg(L0) - L[0]) / stdev_u(L0) / pow(len(L0), 0.5)
                t0 = scipy.stats.t.ppf(L[1] / 2, (L[0] - 1)) * (-1)
                t1 = (-1) * t0
                P = 2 * (1 - scipy.stats.t.cdf(abs(t), (len(L0) - 1)))
                if abs(t) > abs(t0):
                    print(
                        '******\nt = %.3f，t0 = %.3f或%.3f，P = %.5f\n因为 abs(t) > abs(t0)，或因为 P < alpha = %.2f，所以拒绝原假设H0！\n******' % (
                        t, t0, t1, P, L[1]))
                elif abs(t) < abs(t0):
                    print(
                        '******\nt = %.3f，t0 = %.3f或%.3f，P = %.5f\n因为 abs(t) < abs(t0)，或因为 P > alpha = %.2f，所以拒绝备择假设H1！\n******' % (
                        t, t0, t1, P, L[1]))
                else:
                    print('******\n怎么会这么巧！\n******')
            else:
                print('输入有误！')
                oneHypothesisTest_avg()
        else:
            print('输入有误！')
            oneHypothesisTest_avg()
    elif a == 2:
        if b == 1:
            if c == 1:
                L = [float(n) for n in input('请依次输入样本容量、样本均值、假设均值、总体标准差、显著性水平：').split()]
                z = (L[1] - L[2]) / (L[3] / pow(L[0], 0.5))
                z0 = scipy.stats.norm.ppf(1 - L[4]) * (-1)
                P = 1 - scipy.stats.norm.cdf(abs(z))
                if abs(z) > abs(z0):
                    print(
                        '******\nz = %.3f，z0 = %.3f，P = %.5f\n因为 abs(z) > abs(z0)，或因为 P < alpha = %.2f，所以拒绝原假设H0！\n******' % (
                        z, z0, P, L[4]))
                elif abs(z) < abs(z0):
                    print(
                        '******\nz = %.3f，z0 = %.3f，P = %.5f\n因为 abs(z) < abs(z0)，或因为 P > alpha = %.2f，所以拒绝备择假设H1！\n******' % (
                        z, z0, P, L[4]))
                else:
                    print('******\n怎么会这么巧！\n******')
            elif c == 2:
                L0 = dataInput()
                L = [float(n) for n in input('请依次输入假设均值、总体标准差、显著性水平：').split()]
                z = (avg(L0) - L[0]) / L[1] / pow(len(L0), 0.5)
                z0 = scipy.stats.norm.ppf(1 - L[2]) * (-1)
                P = 1 - scipy.stats.norm.cdf(abs(z))
                if abs(z) > abs(z0):
                    print(
                        '******\nz = %.3f，z0 = %.3f，P = %.5f\n因为 abs(z) > abs(z0)，或因为 P < alpha = %.2f，所以拒绝原假设H0！\n******' % (
                        z, z0, P, L[2]))
                elif abs(z) < abs(z0):
                    print(
                        '******\nz = %.3f，z0 = %.3f，P = %.5f\n因为 abs(z) < abs(z0)，或因为 P > alpha = %.2f，所以拒绝备择假设H1！\n******' % (
                        z, z0, P, L[2]))
                else:
                    print('******\n怎么会这么巧！\n******')
            else:
                print('输入有误！')
                oneHypothesisTest_avg()
        elif b == 2:
            if c == 1:
                L = [float(n) for n in input('请依次输入样本容量、样本均值、假设均值、样本标准差、显著性水平：').split()]
                z = (L[1] - L[2]) / (L[3] / pow(L[0], 0.5))
                z0 = scipy.stats.norm.ppf(1 - L[4]) * (-1)
                P = 1 - scipy.stats.norm.cdf(abs(z))
                if abs(z) > abs(z0):
                    print(
                        '******\nz = %.3f，z0 = %.3f，P = %.5f\n因为 abs(z) > abs(z0)，或因为 P < alpha = %.2f，所以拒绝原假设H0！\n******' % (
                        z, z0, P, L[4]))
                elif abs(z) < abs(z0):
                    print(
                        '******\nz = %.3f，z0 = %.3f，P = %.5f\n因为 abs(z) < abs(z0)，或因为 P > alpha = %.2f，所以拒绝备择假设H1！\n******' % (
                        z, z0, P, L[4]))
                else:
                    print('******\n怎么会这么巧！\n******')
            elif c == 2:
                L0 = dataInput()
                L = [float(n) for n in input('请依次输入假设均值、显著性水平：').split()]
                z = (avg(L0) - L[0]) / stdev_u(L0) / pow(len(L0), 0.5)
                z0 = scipy.stats.norm.ppf(1 - L[1]) * (-1)
                P = 1 - scipy.stats.norm.cdf(abs(z))
                if abs(z) > abs(z0):
                    print(
                        '******\nz = %.3f，z0 = %.3f，P = %.5f\n因为 abs(z) > abs(z0)，或因为 P < alpha = %.2f，所以拒绝原假设H0！\n******' % (
                        z, z0, P, L[1]))
                elif abs(z) < abs(z0):
                    print(
                        '******\nz = %.3f，z0 = %.3f，P = %.5f\n因为 abs(z) < abs(z0)，或因为 P > alpha = %.2f，所以拒绝备择假设H1！\n******' % (
                        z, z0, P, L[1]))
                else:
                    print('******\n怎么会这么巧！\n******')
            else:
                print('输入有误！')
                oneHypothesisTest_avg()
        elif b == 3:
            if c == 1:
                L = [float(n) for n in input('请依次输入样本容量、样本均值、假设均值、总体标准差、显著性水平：').split()]
                z = (L[1] - L[2]) / (L[3] / pow(L[0], 0.5))
                z0 = scipy.stats.norm.ppf(1 - L[4]) * (-1)
                P = 1 - scipy.stats.norm.cdf(abs(z))
                if abs(z) > abs(z0):
                    print(
                        '******\nz = %.3f，z0 = %.3f，P = %.5f\n因为 abs(z) > abs(z0)，或因为 P < alpha = %.2f，所以拒绝原假设H0！\n******' % (
                        z, z0, P, L[4]))
                elif abs(z) < abs(z0):
                    print(
                        '******\nz = %.3f，z0 = %.3f，P = %.5f\n因为 abs(z) < abs(z0)，或因为 P > alpha = %.2f，所以拒绝备择假设H1！\n******' % (
                        z, z0, P, L[4]))
                else:
                    print('******\n怎么会这么巧！\n******')
            elif c == 2:
                L0 = dataInput()
                L = [float(n) for n in input('请依次输入假设均值、总体标准差、显著性水平：').split()]
                z = (avg(L0) - L[0]) / L[1] / pow(len(L0), 0.5)
                z0 = scipy.stats.norm.ppf(1 - L[2]) * (-1)
                P = 1 - scipy.stats.norm.cdf(abs(z))
                if abs(z) > abs(z0):
                    print(
                        '******\nz = %.3f，z0 = %.3f，P = %.5f\n因为 abs(z) > abs(z0)，或因为 P < alpha = %.2f，所以拒绝原假设H0！\n******' % (
                        z, z0, P, L[2]))
                elif abs(z) < abs(z0):
                    print(
                        '******\nz = %.3f，z0 = %.3f，P = %.5f\n因为 abs(z) < abs(z0)，或因为 P > alpha = %.2f，所以拒绝备择假设H1！\n******' % (
                        z, z0, P, L[2]))
                else:
                    print('******\n怎么会这么巧！\n******')
            else:
                print('输入有误！')
                oneHypothesisTest_avg()
        elif b == 4:
            if c == 1:
                L = [float(n) for n in input('请依次输入样本容量、样本均值、假设均值、样本标准差、显著性水平：').split()]
                t = (L[1] - L[2]) / (L[3] / pow(L[0], 0.5))
                t0 = scipy.stats.t.ppf(L[4], (L[0] - 1))
                P = scipy.stats.t.cdf(abs(t), (L[0] - 1))
                if abs(t) > abs(t0):
                    print('******\nt = %.3f，t0 = %.3f，P = %.5f\n因为 abs(t) > abs(t0)，或因为 P < alpha = %.2f，所以拒绝原假设H0！' % (
                    t, t0, P, L[4]))
                elif abs(t) < abs(t0):
                    print(
                        '******\nt = %.3f，t0 = %.3f，P = %.5f\n因为 abs(t) < abs(t0)，或因为 P > alpha = %.2f，所以拒绝备择假设H1！' % (
                        t, t0, P, L[4]))
                else:
                    print('******\n怎么会这么巧！\n******')
            elif c == 2:
                L0 = dataInput()
                L = [float(n) for n in input('请依次输入假设均值、显著性水平：').split()]
                t = (avg(L0) - L[0]) / stdev_u(L0) / pow(len(L0), 0.5)
                t0 = scipy.stats.t.ppf(L[1], (L[0] - 1))
                P = scipy.stats.t.cdf(abs(t), (len(L0) - 1))
                if abs(t) > abs(t0):
                    print('******\nt = %.3f，t0 = %.3f，P = %.5f\n因为 abs(t) > abs(t0)，或因为 P < alpha = %.2f，所以拒绝原假设H0！' % (
                    t, t0, P, L[1]))
                elif abs(t) < abs(t0):
                    print(
                        '******\nt = %.3f，t0 = %.3f，P = %.5f\n因为 abs(t) < abs(t0)，或因为 P > alpha = %.2f，所以拒绝备择假设H1！' % (
                        t, t0, P, L[1]))
                else:
                    print('******\n怎么会这么巧！\n******')
            else:
                print('输入有误！')
                oneHypothesisTest_avg()
        else:
            print('输入有误！')
            oneHypothesisTest_avg()
    elif a == 3:
        if b == 1:
            if c == 1:
                L = [float(n) for n in input('请依次输入样本容量、样本均值、假设均值、总体标准差、显著性水平：').split()]
                z = (L[1] - L[2]) / (L[3] / pow(L[0], 0.5))
                z0 = scipy.stats.norm.ppf(1 - L[4])
                P = 1 - scipy.stats.norm.cdf(abs(z))
                if abs(z) > abs(z0):
                    print(
                        '******\nz = %.3f，z0 = %.3f，P = %.5f\n因为 abs(z) > abs(z0)，或因为 P < alpha = %.2f，所以拒绝原假设H0！\n******' % (
                        z, z0, P, L[4]))
                elif abs(z) < abs(z0):
                    print(
                        '******\nz = %.3f，z0 = %.3f，P = %.5f\n因为 abs(z) < abs(z0)，或因为 P > alpha = %.2f，所以拒绝备择假设H1！\n******' % (
                        z, z0, P, L[4]))
                else:
                    print('******\n怎么会这么巧！\n******')
            elif c == 2:
                L0 = dataInput()
                L = [float(n) for n in input('请依次输入假设均值、总体标准差、显著性水平：').split()]
                z = (avg(L0) - L[0]) / L[1] / pow(len(L0), 0.5)
                z0 = scipy.stats.norm.ppf(1 - L[2])
                P = 1 - scipy.stats.norm.cdf(abs(z))
                if abs(z) > abs(z0):
                    print(
                        '******\nz = %.3f，z0 = %.3f，P = %.5f\n因为 abs(z) > abs(z0)，或因为 P < alpha = %.2f，所以拒绝原假设H0！\n******' % (
                        z, z0, P, L[2]))
                elif abs(z) < abs(z0):
                    print(
                        '******\nz = %.3f，z0 = %.3f，P = %.5f\n因为 abs(z) < abs(z0)，或因为 P > alpha = %.2f，所以拒绝备择假设H1！\n******' % (
                        z, z0, P, L[2]))
                else:
                    print('******\n怎么会这么巧！\n******')
            else:
                print('输入有误！')
                oneHypothesisTest_avg()
        elif b == 2:
            if c == 1:
                L = [float(n) for n in input('请依次输入样本容量、样本均值、假设均值、样本标准差、显著性水平：').split()]
                z = (L[1] - L[2]) / (L[3] / pow(L[0], 0.5))
                z0 = scipy.stats.norm.ppf(1 - L[4])
                P = 1 - scipy.stats.norm.cdf(abs(z))
                if abs(z) > abs(z0):
                    print(
                        '******\nz = %.3f，z0 = %.3f，P = %.5f\n因为 abs(z) > abs(z0)，或因为 P < alpha = %.2f，所以拒绝原假设H0！\n******' % (
                        z, z0, P, L[4]))
                elif abs(z) < abs(z0):
                    print(
                        '******\nz = %.3f，z0 = %.3f，P = %.5f\n因为 abs(z) < abs(z0)，或因为 P > alpha = %.2f，所以拒绝备择假设H1！\n******' % (
                        z, z0, P, L[4]))
                else:
                    print('******\n怎么会这么巧！\n******')
            elif c == 2:
                L0 = dataInput()
                L = [float(n) for n in input('请依次输入假设均值、显著性水平：').split()]
                z = (avg(L0) - L[0]) / stdev_u(L0) / pow(len(L0), 0.5)
                z0 = scipy.stats.norm.ppf(1 - L[1])
                P = 1 - scipy.stats.norm.cdf(abs(z))
                if abs(z) > abs(z0):
                    print(
                        '******\nz = %.3f，z0 = %.3f，P = %.5f\n因为 abs(z) > abs(z0)，或因为 P < alpha = %.2f，所以拒绝原假设H0！\n******' % (
                        z, z0, P, L[1]))
                elif abs(z) < abs(z0):
                    print(
                        '******\nz = %.3f，z0 = %.3f，P = %.5f\n因为 abs(z) < abs(z0)，或因为 P > alpha = %.2f，所以拒绝备择假设H1！\n******' % (
                        z, z0, P, L[1]))
                else:
                    print('******\n怎么会这么巧！\n******')
            else:
                print('输入有误！')
                oneHypothesisTest_avg()
        elif b == 3:
            if c == 1:
                L = [float(n) for n in input('请依次输入样本容量、样本均值、假设均值、总体标准差、显著性水平：').split()]
                z = (L[1] - L[2]) / (L[3] / pow(L[0], 0.5))
                z0 = scipy.stats.norm.ppf(1 - L[4])
                P = 1 - scipy.stats.norm.cdf(abs(z))
                if abs(z) > abs(z0):
                    print(
                        '******\nz = %.3f，z0 = %.3f，P = %.5f\n因为 abs(z) > abs(z0)，或因为 P < alpha = %.2f，所以拒绝原假设H0！\n******' % (
                        z, z0, P, L[4]))
                elif abs(z) < abs(z0):
                    print(
                        '******\nz = %.3f，z0 = %.3f，P = %.5f\n因为 abs(z) < abs(z0)，或因为 P > alpha = %.2f，所以拒绝备择假设H1！\n******' % (
                        z, z0, P, L[4]))
                else:
                    print('******\n怎么会这么巧！\n******')
            elif c == 2:
                L0 = dataInput()
                L = [float(n) for n in input('请依次输入假设均值、总体标准差、显著性水平：').split()]
                z = (avg(L0) - L[0]) / L[1] / pow(len(L0), 0.5)
                z0 = scipy.stats.norm.ppf(1 - L[2])
                P = 1 - scipy.stats.norm.cdf(abs(z))
                if abs(z) > abs(z0):
                    print(
                        '******\nz = %.3f，z0 = %.3f，P = %.5f\n因为 abs(z) > abs(z0)，或因为 P < alpha = %.2f，所以拒绝原假设H0！\n******' % (
                        z, z0, P, L[2]))
                elif abs(z) < abs(z0):
                    print(
                        '******\nz = %.3f，z0 = %.3f，P = %.5f\n因为 abs(z) < abs(z0)，或因为 P > alpha = %.2f，所以拒绝备择假设H1！\n******' % (
                        z, z0, P, L[2]))
                else:
                    print('******\n怎么会这么巧！\n******')
            else:
                print('输入有误！')
                oneHypothesisTest_avg()
        elif b == 4:
            if c == 1:
                L = [float(n) for n in input('请依次输入样本容量、样本均值、假设均值、样本标准差、显著性水平：').split()]
                t = (L[1] - L[2]) / (L[3] / pow(L[0], 0.5))
                t0 = scipy.stats.t.ppf(L[4], (L[0] - 1)) * (-1)
                P = scipy.stats.t.cdf(abs(t), (L[0] - 1))
                if abs(t) > abs(t0):
                    print('******\nt = %.3f，t0 = %.3f，P = %.5f\n因为 abs(t) > abs(t0)，或因为 P < alpha = %.2f，所以拒绝原假设H0！' % (
                    t, t0, P, L[4]))
                elif abs(t) < abs(t0):
                    print(
                        '******\nt = %.3f，t0 = %.3f，P = %.5f\n因为 abs(t) < abs(t0)，或因为 P > alpha = %.2f，所以拒绝备择假设H1！' % (
                        t, t0, P, L[4]))
                else:
                    print('******\n怎么会这么巧！\n******')
            elif c == 2:
                L0 = dataInput()
                L = [float(n) for n in input('请依次输入假设均值、显著性水平：').split()]
                t = (avg(L0) - L[0]) / stdev_u(L0) / pow(len(L0), 0.5)
                t0 = scipy.stats.t.ppf(L[1], (L[0] - 1)) * (-1)
                P = scipy.stats.t.cdf(abs(t), (len(L0) - 1))
                if abs(t) > abs(t0):
                    print('******\nt = %.3f，t0 = %.3f，P = %.5f\n因为 abs(t) > abs(t0)，或因为 P < alpha = %.2f，所以拒绝原假设H0！' % (
                    t, t0, P, L[1]))
                elif abs(t) < abs(t0):
                    print(
                        '******\nt = %.3f，t0 = %.3f，P = %.5f\n因为 abs(t) < abs(t0)，或因为 P > alpha = %.2f，所以拒绝备择假设H1！' % (
                        t, t0, P, L[1]))
                else:
                    print('******\n怎么会这么巧！\n******')
            else:
                print('输入有误！')
                oneHypothesisTest_avg()
        else:
            print('输入有误！')
            oneHypothesisTest_avg()
    else:
        print('输入有误！')
        oneHypothesisTest_avg()
    d = int(input('继续进行总体均值的假设检验请输入1，需要计算其他类型请输入2，退出请输入0：'))
    if d == 0:
        return
    elif d == 1:
        oneHypothesisTest_avg()
    else:
        type_calling()


# 一个参数总体比例的假设检验
def oneHypothesisTest_pi():
    a = int(input('双侧检验请输入1，左侧检验请输入2，右侧检验请输入3：'))
    L = [float(n) for n in input('请依次输入样本容量、样本比例或观察量数量、假设比例、显著性水平：').split()]
    # 根据样本比例或观察量数量的大小判断该数值到底是样本比例还是观察者数量：观察者数量总是大于或等于1的（因为为0就没有必要计算），而样本比例总是小于1的（因为为1也没有必要计算）
    if L[1] >= 1:
        L[1] = L[1] / L[0]
    elif L[1] < 1 and L[1] > 0:
        L[1] = L[1]
    else:
        print('输入有误！')
        twoParameterEstimate_pi()
    if a == 1:
        z = (L[1] - L[2]) / pow((L[2] * (1 - L[2])) / L[0], 0.5)
        z0 = scipy.stats.norm.ppf(1 - L[3] / 2)
        z1 = (-1) * z0
        P = 2 * (1 - scipy.stats.norm.cdf(abs(z)))
        if abs(z) > abs(z0):
            print(
                '******\nz = %.3f，z0 = %.3f或%.3f，P = %.5f\n因为 abs(z) > abs(z0)，或因为 P < alpha = %.2f，所以拒绝原假设H0！\n******' % (
                z, z0, z1, P, L[3]))
        elif abs(z) < abs(z0):
            print(
                '******\nz = %.3f，z0 = %.3f或%.3f，P = %.5f\n因为 abs(z) < abs(z0)，或因为 P > alpha = %.2f，所以拒绝备择假设H1！\n******' % (
                z, z0, z1, P, L[3]))
        else:
            print('******\n怎么会这么巧！\n******')
    elif a == 2:
        z = (L[1] - L[2]) / pow((L[2] * (1 - L[2])) / L[0], 0.5)
        z0 = scipy.stats.norm.ppf(1 - L[3]) * (-1)
        P = 1 - scipy.stats.norm.cdf(abs(z))
        if abs(z) > abs(z0):
            print('******\nz = %.3f，z0 = %.3f，P = %.5f\n因为 abs(z) > abs(z0)，或因为 P < alpha = %.2f，所以拒绝原假设H0！\n******' % (
            z, z0, P, L[3]))
        elif abs(z) < abs(z0):
            print(
                '******\nz = %.3f，z0 = %.3f，P = %.5f\n因为 abs(z) < abs(z0)，或因为 P > alpha = %.2f，所以拒绝备择假设H1！\n******' % (
                z, z0, P, L[3]))
        else:
            print('******\n怎么会这么巧！\n******')
    elif a == 3:
        z = (L[1] - L[2]) / pow((L[2] * (1 - L[2])) / L[0], 0.5)
        z0 = scipy.stats.norm.ppf(1 - L[3])
        P = 1 - scipy.stats.norm.cdf(abs(z))
        if abs(z) > abs(z0):
            print('******\nz = %.3f，z0 = %.3f，P = %.5f\n因为 abs(z) > abs(z0)，或因为 P < alpha = %.2f，所以拒绝原假设H0！\n******' % (
            z, z0, P, L[3]))
        elif abs(z) < abs(z0):
            print(
                '******\nz = %.3f，z0 = %.3f，P = %.5f\n因为 abs(z) < abs(z0)，或因为 P > alpha = %.2f，所以拒绝备择假设H1！\n******' % (
                z, z0, P, L[3]))
        else:
            print('******\n怎么会这么巧！\n******')
    else:
        print('输入有误！')
        oneHypothesisTest_pi()
    b = int(input('继续进行总体比例的假设检验请输入1，需要计算其他类型请输入2，退出请输入0：'))
    if b == 0:
        return
    elif b == 1:
        oneHypothesisTest_pi()
    else:
        type_calling()


# 一个参数总体方差的假设检验
def oneHypothesisTest_sigma2():
    a = int(input('双侧检验请输入1，左侧检验请输入2，右侧检验请输入3：'))
    b = int(input('直接输入样本统计量请输入1，输入样本观测值请输入2：'))
    if a == 1:
        if b == 1:
            L = [float(n) for n in input('请依次输入样本容量、样本方差、假设方差、显著性水平：').split()]
            ch2 = (L[0] - 1) * L[1] / L[2]
            ch20 = scipy.stats.chi2.ppf(L[3] / 2, L[0] - 1)
            ch21 = scipy.stats.chi2.ppf(1 - L[3] / 2, L[0] - 1)
            P = 2 * (1 - scipy.stats.chi2.cdf(abs(ch2), L[0] - 1))
            if abs(ch2) > abs(ch20):
                print(
                    '******\nch2 = %.3f，ch20 = %.3f或%.3f，P = %.5f\n因为 abs(ch2) > abs(ch20)，或因为 P < alpha = %.2f，所以拒绝原假设H0！\n******' % (
                    ch2, ch20, ch21, P, L[3]))
            elif abs(ch2) < abs(ch20):
                print(
                    '******\nch2 = %.3f，ch20 = %.3f或%.3f，P = %.5f\n因为 abs(ch2) < abs(ch20)，或因为 P > alpha = %.2f，所以拒绝备择假设H1！\n******' % (
                    ch2, ch20, ch21, P, L[3]))
            else:
                print('******\n怎么会这么巧！\n******')
        elif b == 2:
            L0 = dataInput()
            L = [float(n) for n in input('请依次输入假设方差、显著性水平：').split()]
            ch2 = (len(L0) - 1) * var_u(L0) / L[0]
            ch20 = scipy.stats.chi2.ppf(L[1] / 2, len(L0) - 1)
            ch21 = scipy.stats.chi2.ppf(1 - L[1] / 2, len(L0) - 1)
            P = 2 * (1 - scipy.stats.chi2.cdf(abs(ch2), len(L0) - 1))
            if abs(ch2) > abs(ch20):
                print(
                    '******\nch2 = %.3f，ch20 = %.3f或%.3f，P = %.5f\n因为 abs(ch2) > abs(ch20)，或因为 P < alpha = %.2f，所以拒绝原假设H0！\n******' % (
                    ch2, ch20, ch21, P, L[1]))
            elif abs(ch2) < abs(ch20):
                print(
                    '******\nch2 = %.3f，ch20 = %.3f或%.3f，P = %.5f\n因为 abs(ch2) < abs(ch20)，或因为 P > alpha = %.2f，所以拒绝备择假设H1！\n******' % (
                    ch2, ch20, ch21, P, L[1]))
            else:
                print('******\n怎么会这么巧！\n******')
        else:
            print('输入有误！')
            oneHypothesisTest_sigma2()
    elif a == 2:
        if b == 1:
            L = [float(n) for n in input('请依次输入样本容量、样本方差、假设方差、显著性水平：').split()]
            ch2 = (L[0] - 1) * L[1] / L[2]
            ch20 = scipy.stats.chi2.ppf(L[3], L[0] - 1)
            P = 1 - scipy.stats.chi2.cdf(abs(ch2), L[0] - 1)
            if abs(ch2) < abs(ch20):
                print(
                    '******\nch2 = %.3f，ch20 = %.3f，P = %.5f\n因为 abs(ch2) > abs(ch20)，或因为 P < alpha = %.2f，所以拒绝原假设H0！\n******' % (
                    ch2, ch20, P, L[3]))
            elif abs(ch2) > abs(ch20):
                print(
                    '******\nch2 = %.3f，ch20 = %.3f，P = %.5f\n因为 abs(ch2) < abs(ch20)，或因为 P > alpha = %.2f，所以拒绝备择假设H1！\n******' % (
                    ch2, ch20, P, L[3]))
            else:
                print('******\n怎么会这么巧！\n******')
        elif b == 2:
            L0 = dataInput()
            L = [float(n) for n in input('请依次输入假设方差、显著性水平：').split()]
            ch2 = (len(L0) - 1) * var_u(L0) / L[0]
            ch20 = scipy.stats.chi2.ppf(L[1], len(L0) - 1)
            P = 1 - scipy.stats.chi2.cdf(abs(ch2), len(L0) - 1)
            if abs(ch2) < abs(ch20):
                print(
                    '******\nch2 = %.3f，ch20 = %.3f，P = %.5f\n因为 abs(ch2) > abs(ch20)，或因为 P < alpha = %.2f，所以拒绝原假设H0！\n******' % (
                    ch2, ch20, P, L[1]))
            elif abs(ch2) > abs(ch20):
                print(
                    '******\nch2 = %.3f，ch20 = %.3f，P = %.5f\n因为 abs(ch2) < abs(ch20)，或因为 P > alpha = %.2f，所以拒绝备择假设H1！\n******' % (
                    ch2, ch20, P, L[1]))
            else:
                print('******\n怎么会这么巧！\n******')
        else:
            print('输入有误！')
            oneHypothesisTest_sigma2()
    elif a == 3:
        if b == 1:
            L = [float(n) for n in input('请依次输入样本容量、样本方差、假设方差、显著性水平：').split()]
            ch2 = (L[0] - 1) * L[1] / L[2]
            ch20 = scipy.stats.chi2.ppf(1 - L[3], L[0] - 1)
            P = 1 - scipy.stats.chi2.cdf(abs(ch2), L[0] - 1)
            if abs(ch2) > abs(ch20):
                print(
                    '******\nch2 = %.3f，ch20 = %.3f，P = %.5f\n因为 abs(ch2) > abs(ch20)，或因为 P < alpha = %.2f，所以拒绝原假设H0！\n******' % (
                    ch2, ch20, P, L[3]))
            elif abs(ch2) < abs(ch20):
                print(
                    '******\nch2 = %.3f，ch20 = %.3f，P = %.5f\n因为 abs(ch2) < abs(ch20)，或因为 P > alpha = %.2f，所以拒绝备择假设H1！\n******' % (
                    ch2, ch20, P, L[3]))
            else:
                print('******\n怎么会这么巧！\n******')
        elif b == 2:
            L0 = dataInput()
            L = [float(n) for n in input('请依次输入假设方差、显著性水平：').split()]
            ch2 = (len(L0) - 1) * var_u(L0) / L[0]
            ch20 = scipy.stats.chi2.ppf(1 - L[1], len(L0) - 1)
            P = 1 - scipy.stats.chi2.cdf(abs(ch2), len(L0) - 1)
            if abs(ch2) > abs(ch20):
                print(
                    '******\nch2 = %.3f，ch20 = %.3f，P = %.5f\n因为 abs(ch2) > abs(ch20)，或因为 P < alpha = %.2f，所以拒绝原假设H0！\n******' % (
                    ch2, ch20, P, L[1]))
            elif abs(ch2) < abs(ch20):
                print(
                    '******\nch2 = %.3f，ch20 = %.3f，P = %.5f\n因为 abs(ch2) < abs(ch20)，或因为 P > alpha = %.2f，所以拒绝备择假设H1！\n******' % (
                    ch2, ch20, P, L[1]))
            else:
                print('******\n怎么会这么巧！\n******')
        else:
            print('输入有误！')
            oneHypothesisTest_sigma2()
    else:
        print('输入有误！')
        oneHypothesisTest_sigma2()
    c = int(input('继续进行总体方差的假设检验请输入1，需要计算其他类型请输入2，退出请输入0：'))
    if c == 0:
        return
    elif c == 1:
        oneHypothesisTest_sigma2()
    else:
        type_calling()


# 两个参数总体均值之差的假设检验
def twoHypothesisTest_avg():
    h = input('独立样本请输入1，匹配样本请输入2：')
    c = input('双侧检验请输入1，左侧检验请输入2，右侧检验请输入3：')
    b = input('直接输入样本统计量请输入1，输入样本观测值请输入2：')

    # 独立样本
    if h == '1':
        a = input('大样本且总体标准差已知请输入1；\n大样本且总体标准差未知请输入2；\n小样本且总体标准差已知请输入3；\n小样本且总体标准差未知请输入4：\n')

        # 独立大样本且总体标准差已知
        if a == '1':
            if b == '1':
                L1 = [float(n) for n in input('请依次输入样本1的容量、样本1的均值：').split()]
                L2 = [float(n) for n in input('请依次输入样本2的容量、样本2的均值：').split()]
                L = [float(n) for n in input('请依次输入总体1的标准差、总体2的标准差：').split()]
                M = [float(n) for n in input('请依次输入均值之差的假设值、显著性水平：').split()]
                if c == '1':
                    z = ((L1[1] - L2[1]) - M[0]) / pow(pow(L[0], 2) / L1[0] + pow(L[1], 2) / L2[0], 0.5)
                    z_right = scipy.stats.norm.ppf(1 - M[1] / 2)
                    z_left = scipy.stats.norm.ppf(M[1] / 2)
                    P = 2 * (1 - scipy.stats.norm.cdf(abs(z)))
                    if abs(z) > abs(z_right):
                        print(
                            '******\nz = %.3f，z_left = %.3f或z_right = %.3f，P = %.5f\n因为 abs(z) > abs(z_right)，或因为 P < alpha = %.3f，所以拒绝原假设H0！\n******' % (
                            z, z_left, z_right, P, M[1]))
                    elif abs(z) < abs(z_right):
                        print(
                            '******\nz = %.3f，z_left = %.3f或z_right = %.3f，P = %.5f\n因为 abs(z) < abs(z_right)，或因为 P > alpha = %.3f，所以拒绝备择假设H1！\n******' % (
                            z, z_left, z_right, P, M[1]))
                    else:
                        print('******\n怎么会这么巧！\n******')
                elif c == '2':
                    z = ((L1[1] - L2[1]) - M[0]) / pow(pow(L[0], 2) / L1[0] + pow(L[1], 2) / L2[0], 0.5)
                    z_left = scipy.stats.norm.ppf(M[1])
                    P = 1 - scipy.stats.norm.cdf(abs(z))
                    if z < z_left:
                        print(
                            '******\nz = %.3f，z_left = %.3f，P = %.5f\n因为 abs(z) > abs(z_left)（即z < z_left），或因为 P < alpha = %.3f，所以拒绝原假设H0！\n******' % (
                            z, z_left, P, M[1]))
                    elif z > z_left:
                        print(
                            '******\nz = %.3f，z_left = %.3f，P = %.5f\n因为 abs(z) < abs(z_left)（即z > z_left），或因为 P > alpha = %.3f，所以拒绝备择假设H1！\n******' % (
                            z, z_left, P, M[1]))
                    else:
                        print('******\n怎么会这么巧！\n******')
                elif c == '3':
                    z = ((L1[1] - L2[1]) - M[0]) / pow(pow(L[0], 2) / L1[0] + pow(L[1], 2) / L2[0], 0.5)
                    z_right = scipy.stats.norm.ppf(1 - M[1])
                    P = 1 - scipy.stats.norm.cdf(abs(z))
                    if z > z_right:
                        print(
                            '******\nz = %.3f，z_right = %.3f，P = %.5f\n因为 abs(z) > abs(z_right)（即z > z_right），或因为 P < alpha = %.3f，所以拒绝原假设H0！\n******' % (
                            z, z_right, P, M[1]))
                    elif z < z_right:
                        print(
                            '******\nz = %.3f，z_right = %.3f，P = %.5f\n因为 abs(z) < abs(z_right)（即z < z_right），或因为 P > alpha = %.3f，所以拒绝备择假设H1！\n******' % (
                            z, z_right, P, M[1]))
                    else:
                        print('******\n怎么会这么巧！\n******')
                else:
                    print('输入有误！')
                    twoHypothesisTest_avg()
            elif b == '2':
                L1 = dataInput()
                L2 = dataInput()
                L = [float(n) for n in input('请依次输入总体1的标准差、总体2的标准差：').split()]
                M = [float(n) for n in input('请依次输入均值之差的假设值、显著性水平：').split()]
                if c == '1':
                    z = ((avg(L1) - avg(L2)) - M[0]) / pow(pow(L[0], 2) / len(L1) + pow(L[1], 2) / len(L2), 0.5)
                    z_right = scipy.stats.norm.ppf(1 - M[1] / 2)
                    z_left = scipy.stats.norm.ppf(M[1] / 2)
                    P = 2 * (1 - scipy.stats.norm.cdf(abs(z)))
                    if abs(z) > abs(z_right):
                        print(
                            '******\nz = %.3f，z_left = %.3f或z_right = %.3f，P = %.5f\n因为 abs(z) > abs(z_right)，或因为 P < alpha = %.3f，所以拒绝原假设H0！\n******' % (
                            z, z_left, z_right, P, M[1]))
                    elif abs(z) < abs(z_right):
                        print(
                            '******\nz = %.3f，z_left = %.3f或z_right = %.3f，P = %.5f\n因为 abs(z) < abs(z_right)，或因为 P > alpha = %.3f，所以拒绝备择假设H1！\n******' % (
                            z, z_left, z_right, P, M[1]))
                    else:
                        print('******\n怎么会这么巧！\n******')
                elif c == '2':
                    z = ((avg(L1) - avg(L2)) - M[0]) / pow(pow(L[0], 2) / len(L1) + pow(L[1], 2) / len(L2), 0.5)
                    z_left = scipy.stats.norm.ppf(M[1])
                    P = 1 - scipy.stats.norm.cdf(abs(z))
                    if z < z_left:
                        print(
                            '******\nz = %.3f，z_left = %.3f，P = %.5f\n因为 abs(z) > abs(z_left)（即z < z_left），或因为 P < alpha = %.3f，所以拒绝原假设H0！\n******' % (
                            z, z_left, P, M[1]))
                    elif z > z_left:
                        print(
                            '******\nz = %.3f，z_left = %.3f，P = %.5f\n因为 abs(z) < abs(z_left)（即z > z_left），或因为 P > alpha = %.3f，所以拒绝备择假设H1！\n******' % (
                            z, z_left, P, M[1]))
                    else:
                        print('******\n怎么会这么巧！\n******')
                elif c == '3':
                    z = ((avg(L1) - avg(L2)) - M[0]) / pow(pow(L[0], 2) / len(L1) + pow(L[1], 2) / len(L2), 0.5)
                    z_right = scipy.stats.norm.ppf(1 - M[1])
                    P = 1 - scipy.stats.norm.cdf(abs(z))
                    if z > z_right:
                        print(
                            '******\nz = %.3f，z_right = %.3f，P = %.5f\n因为 abs(z) > abs(z_right)（即z > z_right），或因为 P < alpha = %.3f，所以拒绝原假设H0！\n******' % (
                            z, z_right, P, M[1]))
                    elif z < z_right:
                        print(
                            '******\nz = %.3f，z_right = %.3f，P = %.5f\n因为 abs(z) < abs(z_right)（即z < z_right），或因为 P > alpha = %.3f，所以拒绝备择假设H1！\n******' % (
                            z, z_right, P, M[1]))
                    else:
                        print('******\n怎么会这么巧！\n******')
                else:
                    print('输入有误！')
                    twoHypothesisTest_avg()
            else:
                print('输入有误！')
                twoHypothesisTest_avg()

        # 独立大样本且总体标准差未知
        elif a == '2':
            if b == '1':
                L1 = [float(n) for n in input('请依次输入样本1的容量、样本1的均值：').split()]
                L2 = [float(n) for n in input('请依次输入样本2的容量、样本2的均值：').split()]
                L = [float(n) for n in input('请依次输入样本1的标准差、样本2的标准差：').split()]
                M = [float(n) for n in input('请依次输入均值之差的假设值、显著性水平：').split()]
                if c == '1':
                    z = ((L1[1] - L2[1]) - M[0]) / pow(pow(L[0], 2) / L1[0] + pow(L[1], 2) / L2[0], 0.5)
                    z_right = scipy.stats.norm.ppf(1 - M[1] / 2)
                    z_left = scipy.stats.norm.ppf(M[1] / 2)
                    P = 2 * (1 - scipy.stats.norm.cdf(abs(z)))
                    if abs(z) > abs(z_right):
                        print(
                            '******\nz = %.3f，z_left = %.3f或z_right = %.3f，P = %.5f\n因为 abs(z) > abs(z_right)，或因为 P < alpha = %.3f，所以拒绝原假设H0！\n******' % (
                            z, z_left, z_right, P, M[1]))
                    elif abs(z) < abs(z_right):
                        print(
                            '******\nz = %.3f，z_left = %.3f或z_right = %.3f，P = %.5f\n因为 abs(z) < abs(z_right)，或因为 P > alpha = %.3f，所以拒绝备择假设H1！\n******' % (
                            z, z_left, z_right, P, M[1]))
                    else:
                        print('******\n怎么会这么巧！\n******')
                elif c == '2':
                    z = ((L1[1] - L2[1]) - M[0]) / pow(pow(L[0], 2) / L1[0] + pow(L[1], 2) / L2[0], 0.5)
                    z_left = scipy.stats.norm.ppf(M[1])
                    P = 1 - scipy.stats.norm.cdf(abs(z))
                    if z < z_left:
                        print(
                            '******\nz = %.3f，z_left = %.3f，P = %.5f\n因为 abs(z) > abs(z_left)（即z < z_left），或因为 P < alpha = %.3f，所以拒绝原假设H0！\n******' % (
                            z, z_left, P, M[1]))
                    elif z > z_left:
                        print(
                            '******\nz = %.3f，z_left = %.3f，P = %.5f\n因为 abs(z) < abs(z_left)（即z > z_left），或因为 P > alpha = %.3f，所以拒绝备择假设H1！\n******' % (
                            z, z_left, P, M[1]))
                    else:
                        print('******\n怎么会这么巧！\n******')
                elif c == '3':
                    z = ((L1[1] - L2[1]) - M[0]) / pow(pow(L[0], 2) / L1[0] + pow(L[1], 2) / L2[0], 0.5)
                    z_right = scipy.stats.norm.ppf(1 - M[1])
                    P = 1 - scipy.stats.norm.cdf(abs(z))
                    if z > z_right:
                        print(
                            '******\nz = %.3f，z_right = %.3f，P = %.5f\n因为 abs(z) > abs(z_right)（即z > z_right），或因为 P < alpha = %.3f，所以拒绝原假设H0！\n******' % (
                            z, z_right, P, M[1]))
                    elif z < z_right:
                        print(
                            '******\nz = %.3f，z_right = %.3f，P = %.5f\n因为 abs(z) < abs(z_right)（即z < z_right），或因为 P > alpha = %.3f，所以拒绝备择假设H1！\n******' % (
                            z, z_right, P, M[1]))
                    else:
                        print('******\n怎么会这么巧！\n******')
                else:
                    print('输入有误！')
                    twoHypothesisTest_avg()
            elif b == '2':
                L1 = dataInput()
                L2 = dataInput()
                M = [float(n) for n in input('请依次输入均值之差的假设值、显著性水平：').split()]
                if c == '1':
                    z = ((avg(L1) - avg(L2)) - M[0]) / pow(
                        pow(stdev_u(L1), 2) / len(L1) + pow(stdev_u(L2), 2) / len(L2), 0.5)
                    z_right = scipy.stats.norm.ppf(1 - M[1] / 2)
                    z_left = scipy.stats.norm.ppf(M[1] / 2)
                    P = 2 * (1 - scipy.stats.norm.cdf(abs(z)))
                    if abs(z) > abs(z_right):
                        print(
                            '******\nz = %.3f，z_left = %.3f或z_right = %.3f，P = %.5f\n因为 abs(z) > abs(z_right)，或因为 P < alpha = %.3f，所以拒绝原假设H0！\n******' % (
                            z, z_left, z_right, P, M[1]))
                    elif abs(z) < abs(z_right):
                        print(
                            '******\nz = %.3f，z_left = %.3f或z_right = %.3f，P = %.5f\n因为 abs(z) < abs(z_right)，或因为 P > alpha = %.3f，所以拒绝备择假设H1！\n******' % (
                            z, z_left, z_right, P, M[1]))
                    else:
                        print('******\n怎么会这么巧！\n******')
                elif c == '2':
                    z = ((avg(L1) - avg(L2)) - M[0]) / pow(
                        pow(stdev_u(L1), 2) / len(L1) + pow(stdev_u(L2), 2) / len(L2), 0.5)
                    z_left = scipy.stats.norm.ppf(M[1])
                    P = 1 - scipy.stats.norm.cdf(abs(z))
                    if z < z_left:
                        print(
                            '******\nz = %.3f，z_left = %.3f，P = %.5f\n因为 abs(z) > abs(z_left)（即z < z_left），或因为 P < alpha = %.3f，所以拒绝原假设H0！\n******' % (
                            z, z_left, P, M[1]))
                    elif z > z_left:
                        print(
                            '******\nz = %.3f，z_left = %.3f，P = %.5f\n因为 abs(z) < abs(z_left)（即z > z_left），或因为 P > alpha = %.3f，所以拒绝备择假设H1！\n******' % (
                            z, z_left, P, M[1]))
                    else:
                        print('******\n怎么会这么巧！\n******')
                elif c == '3':
                    z = ((avg(L1) - avg(L2)) - M[0]) / pow(
                        pow(stdev_u(L1), 2) / len(L1) + pow(stdev_u(L2), 2) / len(L2), 0.5)
                    z_right = scipy.stats.norm.ppf(1 - M[1])
                    P = 1 - scipy.stats.norm.cdf(abs(z))
                    if z > z_right:
                        print(
                            '******\nz = %.3f，z_right = %.3f，P = %.5f\n因为 abs(z) > abs(z_right)（即z > z_right），或因为 P < alpha = %.3f，所以拒绝原假设H0！\n******' % (
                            z, z_right, P, M[1]))
                    elif z < z_right:
                        print(
                            '******\nz = %.3f，z_right = %.3f，P = %.5f\n因为 abs(z) < abs(z_right)（即z < z_right），或因为 P > alpha = %.3f，所以拒绝备择假设H1！\n******' % (
                            z, z_right, P, M[1]))
                    else:
                        print('******\n怎么会这么巧！\n******')
                else:
                    print('输入有误！')
                    twoHypothesisTest_avg()
            else:
                print('输入有误！')
                twoHypothesisTest_avg()

        # 独立小样本且总体标准差已知
        elif a == '3':
            if b == '1':
                L1 = [float(n) for n in input('请依次输入样本1的容量、样本1的均值：').split()]
                L2 = [float(n) for n in input('请依次输入样本2的容量、样本2的均值：').split()]
                L = [float(n) for n in input('请依次输入总体1的标准差、总体2的标准差：').split()]
                M = [float(n) for n in input('请依次输入均值之差的假设值、显著性水平：').split()]
                if c == '1':
                    z = ((L1[1] - L2[1]) - M[0]) / pow(pow(L[0], 2) / L1[0] + pow(L[1], 2) / L2[0], 0.5)
                    z_right = scipy.stats.norm.ppf(1 - M[1] / 2)
                    z_left = scipy.stats.norm.ppf(M[1] / 2)
                    P = 2 * (1 - scipy.stats.norm.cdf(abs(z)))
                    if abs(z) > abs(z_right):
                        print(
                            '******\nz = %.3f，z_left = %.3f或z_right = %.3f，P = %.5f\n因为 abs(z) > abs(z_right)，或因为 P < alpha = %.3f，所以拒绝原假设H0！\n******' % (
                            z, z_left, z_right, P, M[1]))
                    elif abs(z) < abs(z_right):
                        print(
                            '******\nz = %.3f，z_left = %.3f或z_right = %.3f，P = %.5f\n因为 abs(z) < abs(z_right)，或因为 P > alpha = %.3f，所以拒绝备择假设H1！\n******' % (
                            z, z_left, z_right, P, M[1]))
                    else:
                        print('******\n怎么会这么巧！\n******')
                elif c == '2':
                    z = ((L1[1] - L2[1]) - M[0]) / pow(pow(L[0], 2) / L1[0] + pow(L[1], 2) / L2[0], 0.5)
                    z_left = scipy.stats.norm.ppf(M[1])
                    P = 1 - scipy.stats.norm.cdf(abs(z))
                    if z < z_left:
                        print(
                            '******\nz = %.3f，z_left = %.3f，P = %.5f\n因为 abs(z) > abs(z_left)（即z < z_left），或因为 P < alpha = %.3f，所以拒绝原假设H0！\n******' % (
                            z, z_left, P, M[1]))
                    elif z > z_left:
                        print(
                            '******\nz = %.3f，z_left = %.3f，P = %.5f\n因为 abs(z) < abs(z_left)（即z > z_left），或因为 P > alpha = %.3f，所以拒绝备择假设H1！\n******' % (
                            z, z_left, P, M[1]))
                    else:
                        print('******\n怎么会这么巧！\n******')
                elif c == '3':
                    z = ((L1[1] - L2[1]) - M[0]) / pow(pow(L[0], 2) / L1[0] + pow(L[1], 2) / L2[0], 0.5)
                    z_right = scipy.stats.norm.ppf(1 - M[1])
                    P = 1 - scipy.stats.norm.cdf(abs(z))
                    if z > z_right:
                        print(
                            '******\nz = %.3f，z_right = %.3f，P = %.5f\n因为 abs(z) > abs(z_right)（即z > z_right），或因为 P < alpha = %.3f，所以拒绝原假设H0！\n******' % (
                            z, z_right, P, M[1]))
                    elif z < z_right:
                        print(
                            '******\nz = %.3f，z_right = %.3f，P = %.5f\n因为 abs(z) < abs(z_right)（即z < z_right），或因为 P > alpha = %.3f，所以拒绝备择假设H1！\n******' % (
                            z, z_right, P, M[1]))
                    else:
                        print('******\n怎么会这么巧！\n******')
                else:
                    print('输入有误！')
                    twoHypothesisTest_avg()
            elif b == '2':
                L1 = dataInput()
                L2 = dataInput()
                L = [float(n) for n in input('请依次输入总体1的标准差、总体2的标准差：').split()]
                M = [float(n) for n in input('请依次输入均值之差的假设值、显著性水平：').split()]
                if c == '1':
                    z = ((avg(L1) - avg(L2)) - M[0]) / pow(pow(L[0], 2) / len(L1) + pow(L[1], 2) / len(L2), 0.5)
                    z_right = scipy.stats.norm.ppf(1 - M[1] / 2)
                    z_left = scipy.stats.norm.ppf(M[1] / 2)
                    P = 2 * (1 - scipy.stats.norm.cdf(abs(z)))
                    if abs(z) > abs(z_right):
                        print(
                            '******\nz = %.3f，z_left = %.3f或z_right = %.3f，P = %.5f\n因为 abs(z) > abs(z_right)，或因为 P < alpha = %.3f，所以拒绝原假设H0！\n******' % (
                            z, z_left, z_right, P, M[1]))
                    elif abs(z) < abs(z_right):
                        print(
                            '******\nz = %.3f，z_left = %.3f或z_right = %.3f，P = %.5f\n因为 abs(z) < abs(z_right)，或因为 P > alpha = %.3f，所以拒绝备择假设H1！\n******' % (
                            z, z_left, z_right, P, M[1]))
                    else:
                        print('******\n怎么会这么巧！\n******')
                elif c == '2':
                    z = ((avg(L1) - avg(L2)) - M[0]) / pow(pow(L[0], 2) / len(L1) + pow(L[1], 2) / len(L2), 0.5)
                    z_left = scipy.stats.norm.ppf(M[1])
                    P = 1 - scipy.stats.norm.cdf(abs(z))
                    if z < z_left:
                        print(
                            '******\nz = %.3f，z_left = %.3f，P = %.5f\n因为 abs(z) > abs(z_left)（即z < z_left），或因为 P < alpha = %.3f，所以拒绝原假设H0！\n******' % (
                            z, z_left, P, M[1]))
                    elif z > z_left:
                        print(
                            '******\nz = %.3f，z_left = %.3f，P = %.5f\n因为 abs(z) < abs(z_left)（即z > z_left），或因为 P > alpha = %.3f，所以拒绝备择假设H1！\n******' % (
                            z, z_left, P, M[1]))
                    else:
                        print('******\n怎么会这么巧！\n******')
                elif c == '3':
                    z = ((avg(L1) - avg(L2)) - M[0]) / pow(pow(L[0], 2) / len(L1) + pow(L[1], 2) / len(L2), 0.5)
                    z_right = scipy.stats.norm.ppf(1 - M[1])
                    P = 1 - scipy.stats.norm.cdf(abs(z))
                    if z > z_right:
                        print(
                            '******\nz = %.3f，z_right = %.3f，P = %.5f\n因为 abs(z) > abs(z_right)（即z > z_right），或因为 P < alpha = %.3f，所以拒绝原假设H0！\n******' % (
                            z, z_right, P, M[1]))
                    elif z < z_right:
                        print(
                            '******\nz = %.3f，z_right = %.3f，P = %.5f\n因为 abs(z) < abs(z_right)（即z < z_right），或因为 P > alpha = %.3f，所以拒绝备择假设H1！\n******' % (
                            z, z_right, P, M[1]))
                    else:
                        print('******\n怎么会这么巧！\n******')
                else:
                    print('输入有误！')
                    twoHypothesisTest_avg()
            else:
                print('输入有误！')
                twoHypothesisTest_avg()

        # 独立小样本且总体标准差未知
        elif a == '4':
            d = input('总体标准差相等请输入1，总体标准差不等请输入2：')
            if b == '1':
                L1 = [float(n) for n in input('请依次输入样本1的容量、样本1的均值：').split()]
                L2 = [float(n) for n in input('请依次输入样本2的容量、样本2的均值：').split()]
                L = [float(n) for n in input('请依次输入样本1的标准差、样本2的标准差：').split()]
                M = [float(n) for n in input('请依次输入均值之差的假设值、显著性水平：').split()]
                if c == '1':
                    if d == '1':
                        sp = ((L1[0] - 1) * pow(L[0], 2) + (L2[0] - 1) * pow(L[1], 2)) / (L1[0] + L2[0] - 2)
                        sp = pow(sp, 0.5)
                        t = ((L1[1] - L2[1]) - M[0]) / (sp * pow((1 / L1[0] + 1 / L2[0]), 0.5))
                        t_right = scipy.stats.t.ppf(1 - M[1] / 2, L1[0] + L2[0] - 2)
                        t_left = scipy.stats.t.ppf(M[1] / 2, L1[0] + L2[0] - 2)
                        P = 2 * (1 - scipy.stats.t.cdf(abs(t), L1[0] + L2[0] - 2))
                    elif d == '2':
                        t = ((L1[1] - L2[1]) - M[0]) / pow(pow(L[0], 2) / L1[0] + pow(L[1], 2) / L2[0], 0.5)
                        f = pow(pow(L[0], 2) / L1[0] + pow(L[1], 2) / L2[0], 2) / (
                                    pow(pow(L[0], 2) / L1[0], 2) / (L1[0] - 1) + pow(pow(L[1], 2) / L2[0], 2) / (
                                        L2[0] - 1))
                        t_right = scipy.stats.t.ppf(1 - M[1] / 2, f)
                        t_left = scipy.stats.t.ppf(M[1] / 2, f)
                        P = 2 * (1 - scipy.stats.t.cdf(abs(t), f))
                    else:
                        print('输入有误！')
                        twoHypothesisTest_avg()
                    if abs(t) > abs(t_right):
                        print(
                            '******\nt = %.3f，t_left = %.3f或t_right = %.3f，P = %.5f\n因为 abs(t) > abs(t_right)，或因为 P < alpha = %.3f，所以拒绝原假设H0！\n******' % (
                            t, t_left, t_right, P, M[1]))
                    elif abs(t) < abs(t_right):
                        print(
                            '******\nt = %.3f，t_left = %.3f或t_right = %.3f，P = %.5f\n因为 abs(t) < abs(t_right)，或因为 P > alpha = %.3f，所以拒绝备择假设H1！\n******' % (
                            t, t_left, t_right, P, M[1]))
                    else:
                        print('******\n怎么会这么巧！\n******')
                elif c == '2':
                    if d == '1':
                        sp = ((L1[0] - 1) * pow(L[0], 2) + (L2[0] - 1) * pow(L[1], 2)) / (L1[0] + L2[0] - 2)
                        sp = pow(sp, 0.5)
                        t = ((L1[1] - L2[1]) - M[0]) / (sp * pow((1 / L1[0] + 1 / L2[0]), 0.5))
                        t_left = scipy.stats.t.ppf(M[1], L1[0] + L2[0] - 2)
                        P = 1 - scipy.stats.t.cdf(abs(t), L1[0] + L2[0] - 2)
                    elif d == '2':
                        t = ((L1[1] - L2[1]) - M[0]) / pow(pow(L[0], 2) / L1[0] + pow(L[1], 2) / L2[0], 0.5)
                        f = pow(pow(L[0], 2) / L1[0] + pow(L[1], 2) / L2[0], 2) / (
                                    pow(pow(L[0], 2) / L1[0], 2) / (L1[0] - 1) + pow(pow(L[1], 2) / L2[0], 2) / (
                                        L2[0] - 1))
                        t_left = scipy.stats.t.ppf(M[1], f)
                        P = 1 - scipy.stats.t.cdf(abs(t), f)
                    else:
                        print('输入有误！')
                        twoHypothesisTest_avg()
                    if t < t_left:
                        print(
                            '******\nt = %.3f，t_left = %.3f，P = %.5f\n因为 abs(t) > abs(t_left)（即t < t_left），或因为 P < alpha = %.3f，所以拒绝原假设H0！\n******' % (
                            t, t_left, P, M[1]))
                    elif t > t_left:
                        print(
                            '******\nt = %.3f，t_left = %.3f，P = %.5f\n因为 abs(t) < abs(t_left)（即t > t_left），或因为 P > alpha = %.3f，所以拒绝备择假设H1！\n******' % (
                            t, t_left, P, M[1]))
                    else:
                        print('******\n怎么会这么巧！\n******')
                elif c == '3':
                    if d == '1':
                        sp = ((L1[0] - 1) * pow(L[0], 2) + (L2[0] - 1) * pow(L[1], 2)) / (L1[0] + L2[0] - 2)
                        sp = pow(sp, 0.5)
                        t = ((L1[1] - L2[1]) - M[0]) / (sp * pow((1 / L1[0] + 1 / L2[0]), 0.5))
                        t_right = scipy.stats.t.ppf(1 - M[1], L1[0] + L2[0] - 2)
                        P = 1 - scipy.stats.t.cdf(abs(t), L1[0] + L2[0] - 2)
                    elif d == '2':
                        t = ((L1[1] - L2[1]) - M[0]) / pow(pow(L[0], 2) / L1[0] + pow(L[1], 2) / L2[0], 0.5)
                        f = pow(pow(L[0], 2) / L1[0] + pow(L[1], 2) / L2[0], 2) / (
                                    pow(pow(L[0], 2) / L1[0], 2) / (L1[0] - 1) + pow(pow(L[1], 2) / L2[0], 2) / (
                                        L2[0] - 1))
                        t_right = scipy.stats.t.ppf(1 - M[1], f)
                        P = 1 - scipy.stats.t.cdf(abs(t), f)
                    else:
                        print('输入有误！')
                        twoHypothesisTest_avg()
                    if t > t_right:
                        print(
                            '******\nt = %.3f，t_right = %.3f，P = %.5f\n因为 abs(t) > abs(t_right)（即t > t_right），或因为 P < alpha = %.3f，所以拒绝原假设H0！\n******' % (
                            t, t_right, P, M[1]))
                    elif t < t_right:
                        print(
                            '******\nt = %.3f，t_right = %.3f，P = %.5f\n因为 abs(t) < abs(t_right)（即t < t_right），或因为 P > alpha = %.3f，所以拒绝备择假设H1！\n******' % (
                            t, t_right, P, M[1]))
                    else:
                        print('******\n怎么会这么巧！\n******')
                else:
                    print('输入有误！')
                    twoHypothesisTest_avg()
            elif b == '2':
                L1 = dataInput()
                L2 = dataInput()
                M = [float(n) for n in input('请依次输入均值之差的假设值、显著性水平：').split()]
                if c == '1':
                    if d == '1':
                        sp = ((len(L1) - 1) * pow(stdev_u(L1), 2) + (len(L2) - 1) * pow(stdev_u(L2), 2)) / (
                                    len(L1) + len(L2) - 2)
                        sp = pow(sp, 0.5)
                        t = ((avg(L1) - avg(L2)) - M[0]) / (sp * pow((1 / len(L1) + 1 / len(L2)), 0.5))
                        t_right = scipy.stats.t.ppf(1 - M[1] / 2, len(L1) + len(L2) - 2)
                        t_left = scipy.stats.t.ppf(M[1] / 2, len(L1) + len(L2) - 2)
                        P = 2 * (1 - scipy.stats.t.cdf(abs(t), len(L1) + len(L2) - 2))
                    elif d == '2':
                        t = ((avg(L1) - avg(L2)) - M[0]) / pow(
                            pow(stdev_u(L1), 2) / len(L1) + pow(stdev_u(L2), 2) / len(L2), 0.5)
                        f = pow(pow(stdev_u(L1), 2) / len(L1) + pow(stdev_u(L2), 2) / len(L2), 2) / (
                                    pow(pow(stdev_u(L1), 2) / len(L1), 2) / (len(L1) - 1) + pow(
                                pow(stdev_u(L2), 2) / len(L2), 2) / (len(L2) - 1))
                        t_right = scipy.stats.t.ppf(1 - M[1] / 2, f)
                        t_left = scipy.stats.t.ppf(M[1] / 2, f)
                        P = 2 * (1 - scipy.stats.t.cdf(abs(t), f))
                    else:
                        print('输入有误！')
                        twoHypothesisTest_avg()
                    if abs(t) > abs(t_right):
                        print(
                            '******\nt = %.3f，t_left = %.3f或t_right = %.3f，P = %.5f\n因为 abs(t) > abs(t_right)，或因为 P < alpha = %.3f，所以拒绝原假设H0！\n******' % (
                            t, t_left, t_right, P, M[1]))
                    elif abs(t) < abs(t_right):
                        print(
                            '******\nt = %.3f，t_left = %.3f或t_right = %.3f，P = %.5f\n因为 abs(t) < abs(t_right)，或因为 P > alpha = %.3f，所以拒绝备择假设H1！\n******' % (
                            t, t_left, t_right, P, M[1]))
                    else:
                        print('******\n怎么会这么巧！\n******')
                elif c == '2':
                    if d == '1':
                        sp = ((len(L1) - 1) * pow(stdev_u(L1), 2) + (len(L2) - 1) * pow(stdev_u(L2), 2)) / (
                                    len(L1) + len(L2) - 2)
                        sp = pow(sp, 0.5)
                        t = ((avg(L1) - avg(L2)) - M[0]) / (sp * pow((1 / len(L1) + 1 / len(L2)), 0.5))
                        t_left = scipy.stats.t.ppf(M[1], len(L1) + len(L2) - 2)
                        P = 1 - scipy.stats.t.cdf(abs(t), len(L1) + len(L2) - 2)
                    elif d == '2':
                        t = ((avg(L1) - avg(L2)) - M[0]) / pow(
                            pow(stdev_u(L1), 2) / len(L1) + pow(stdev_u(L2), 2) / len(L2), 0.5)
                        f = pow(pow(stdev_u(L1), 2) / len(L1) + pow(stdev_u(L2), 2) / len(L2), 2) / (
                                    pow(pow(stdev_u(L1), 2) / len(L1), 2) / (len(L1) - 1) + pow(
                                pow(stdev_u(L2), 2) / len(L2), 2) / (len(L2) - 1))
                        print(
                            '(avg(L1) = %.3f   stdev_u(L1) = %.3f   (avg(L2) = %.3f   stdev_u(L2) = %.3f   f = %.3f' % (
                            avg(L1), stdev_u(L1), avg(L2), stdev_u(L2), f))
                        t_left = scipy.stats.t.ppf(M[1], f)
                        P = 1 - scipy.stats.t.cdf(abs(t), f)
                    else:
                        print('输入有误！')
                        twoHypothesisTest_avg()
                    if t < t_left:
                        print(
                            '******\nt = %.3f，t_left = %.3f，P = %.5f\n因为 abs(t) > abs(t_left)（即t < t_left），或因为 P < alpha = %.3f，所以拒绝原假设H0！\n******' % (
                            t, t_left, P, M[1]))
                    elif t > t_left:
                        print(
                            '******\nt = %.3f，t_left = %.3f，P = %.5f\n因为 abs(t) < abs(t_left)（即t > t_left），或因为 P > alpha = %.3f，所以拒绝备择假设H1！\n******' % (
                            t, t_left, P, M[1]))
                    else:
                        print('******\n怎么会这么巧！\n******')
                elif c == '3':
                    if d == '1':
                        sp = ((len(L1) - 1) * pow(stdev_u(L1), 2) + (len(L2) - 1) * pow(stdev_u(L2), 2)) / (
                                    len(L1) + len(L2) - 2)
                        sp = pow(sp, 0.5)
                        t = ((avg(L1) - avg(L2)) - M[0]) / (sp * pow((1 / len(L1) + 1 / len(L2)), 0.5))
                        t_right = scipy.stats.t.ppf(1 - M[1], len(L1) + len(L2) - 2)
                        P = 1 - scipy.stats.t.cdf(abs(t), len(L1) + len(L2) - 2)
                    elif d == '2':
                        t = ((avg(L1) - avg(L2)) - M[0]) / pow(
                            pow(stdev_u(L1), 2) / len(L1) + pow(stdev_u(L2), 2) / len(L2), 0.5)
                        f = pow(pow(stdev_u(L1), 2) / len(L1) + pow(stdev_u(L2), 2) / len(L2), 2) / (
                                    pow(pow(stdev_u(L1), 2) / len(L1), 2) / (len(L1) - 1) + pow(
                                pow(stdev_u(L2), 2) / len(L2), 2) / (len(L2) - 1))
                        t_right = scipy.stats.t.ppf(1 - M[1], f)
                        P = 1 - scipy.stats.t.cdf(abs(t), f)
                    else:
                        print('输入有误！')
                        twoHypothesisTest_avg()
                    if t > t_right:
                        print(
                            '******\nt = %.3f，t_right = %.3f，P = %.5f\n因为 abs(t) > abs(t_right)（即t > t_right），或因为 P < alpha = %.3f，所以拒绝原假设H0！\n******' % (
                            t, t_right, P, M[1]))
                    elif t < t_right:
                        print(
                            '******\nt = %.3f，t_right = %.3f，P = %.5f\n因为 abs(t) < abs(t_right)（即t < t_right），或因为 P > alpha = %.3f，所以拒绝备择假设H1！\n******' % (
                            t, t_right, P, M[1]))
                    else:
                        print('******\n怎么会这么巧！\n******')
                else:
                    print('输入有误！')
                    twoHypothesisTest_avg()
            else:
                print('输入有误！')
                twoHypothesisTest_avg()
        else:
            print('输入有误！')
            twoHypothesisTest_avg()

    # 匹配样本
    elif h == '2':
        a = input('大样本请输入1；小样本且两总体各观察值的配对差d服从正态分布请输入2：')

        # 匹配大样本
        if a == '1':
            # 直接输入样本统计量
            if b == '1':
                L = [float(n) for n in input('请依次输入样本容量、配对差的平均值、总体或样本配对差的标准差：').split()]
                M = [float(n) for n in input('请依次输入均值之差的假设值、显著性水平：').split()]
                if c == '1':
                    z = (L[1] - M[0]) / (L[2] / pow(L[0], 0.5))
                    z_right = scipy.stats.norm.ppf(1 - M[1] / 2)
                    z_left = scipy.stats.norm.ppf(M[1] / 2)
                    P = 2 * (1 - scipy.stats.norm.cdf(abs(z)))
                    if abs(z) > abs(z_right):
                        print(
                            '******\nz = %.3f，z_left = %.3f或z_right = %.3f，P = %.5f\n因为 abs(z) > abs(z_right)，或因为 P < alpha = %.3f，所以拒绝原假设H0！\n******' % (
                            z, z_left, z_right, P, M[1]))
                    elif abs(z) < abs(z_right):
                        print(
                            '******\nz = %.3f，z_left = %.3f或z_right = %.3f，P = %.5f\n因为 abs(z) < abs(z_right)，或因为 P > alpha = %.3f，所以拒绝备择假设H1！\n******' % (
                            z, z_left, z_right, P, M[1]))
                    else:
                        print('******\n怎么会这么巧！\n******')
                elif c == '2':
                    z = (L[1] - M[0]) / (L[2] / pow(L[0], 0.5))
                    z_left = scipy.stats.norm.ppf(M[1])
                    P = 1 - scipy.stats.norm.cdf(abs(z))
                    if z < z_left:
                        print(
                            '******\nz = %.3f，z_left = %.3f，P = %.5f\n因为 abs(z) > abs(z_left)（即z < z_left），或因为 P < alpha = %.3f，所以拒绝原假设H0！\n******' % (
                            z, z_left, P, M[1]))
                    elif z > z_left:
                        print(
                            '******\nz = %.3f，z_left = %.3f，P = %.5f\n因为 abs(z) < abs(z_left)（即z > z_left），或因为 P > alpha = %.3f，所以拒绝备择假设H1！\n******' % (
                            z, z_left, P, M[1]))
                    else:
                        print('******\n怎么会这么巧！\n******')
                elif c == '3':
                    z = (L[1] - M[0]) / (L[2] / pow(L[0], 0.5))
                    z_right = scipy.stats.norm.ppf(1 - M[1])
                    P = 1 - scipy.stats.norm.cdf(abs(z))
                    if z > z_right:
                        print(
                            '******\nz = %.3f，z_right = %.3f，P = %.5f\n因为 abs(z) > abs(z_right)（即z > z_right），或因为 P < alpha = %.3f，所以拒绝原假设H0！\n******' % (
                            z, z_right, P, M[1]))
                    elif z < z_right:
                        print(
                            '******\nz = %.3f，z_right = %.3f，P = %.5f\n因为 abs(z) < abs(z_right)（即z < z_right），或因为 P > alpha = %.3f，所以拒绝备择假设H1！\n******' % (
                            z, z_right, P, M[1]))
                    else:
                        print('******\n怎么会这么巧！\n******')
                else:
                    print('输入有误！')
                    twoHypothesisTest_avg()
            # 输入样本观测值
            elif b == '2':
                L1 = dataInput()
                L2 = dataInput()
                M = [float(n) for n in input('请依次输入均值之差的假设值、显著性水平：').split()]
                if c == '1':
                    z = (avg(delta(L1, L2)) - M[0]) / (stdev_u(delta(L1, L2)) / pow(len(L1), 0.5))
                    z_right = scipy.stats.norm.ppf(1 - M[1] / 2)
                    z_left = scipy.stats.norm.ppf(M[1] / 2)
                    P = 2 * (1 - scipy.stats.norm.cdf(abs(z)))
                    if abs(z) > abs(z_right):
                        print(
                            '******\nz = %.3f，z_left = %.3f或z_right = %.3f，P = %.5f\n因为 abs(z) > abs(z_right)，或因为 P < alpha = %.3f，所以拒绝原假设H0！\n******' % (
                            z, z_left, z_right, P, M[1]))
                    elif abs(z) < abs(z_right):
                        print(
                            '******\nz = %.3f，z_left = %.3f或z_right = %.3f，P = %.5f\n因为 abs(z) < abs(z_right)，或因为 P > alpha = %.3f，所以拒绝备择假设H1！\n******' % (
                            z, z_left, z_right, P, M[1]))
                    else:
                        print('******\n怎么会这么巧！\n******')
                elif c == '2':
                    z = (avg(delta(L1, L2)) - M[0]) / (stdev_u(delta(L1, L2)) / pow(len(L1), 0.5))
                    z_left = scipy.stats.norm.ppf(M[1])
                    P = 1 - scipy.stats.norm.cdf(abs(z))
                    if z < z_left:
                        print(
                            '******\nz = %.3f，z_left = %.3f，P = %.5f\n因为 abs(z) > abs(z_left)（即z < z_left），或因为 P < alpha = %.3f，所以拒绝原假设H0！\n******' % (
                            z, z_left, P, M[1]))
                    elif z > z_left:
                        print(
                            '******\nz = %.3f，z_left = %.3f，P = %.5f\n因为 abs(z) < abs(z_left)（即z > z_left），或因为 P > alpha = %.3f，所以拒绝备择假设H1！\n******' % (
                            z, z_left, P, M[1]))
                    else:
                        print('******\n怎么会这么巧！\n******')
                elif c == '3':
                    z = (avg(delta(L1, L2)) - M[0]) / (stdev_u(delta(L1, L2)) / pow(len(L1), 0.5))
                    z_right = scipy.stats.norm.ppf(1 - M[1])
                    P = 1 - scipy.stats.norm.cdf(abs(z))
                    if z > z_right:
                        print(
                            '******\nz = %.3f，z_right = %.3f，P = %.5f\n因为 abs(z) > abs(z_right)（即z > z_right），或因为 P < alpha = %.3f，所以拒绝原假设H0！\n******' % (
                            z, z_right, P, M[1]))
                    elif z < z_right:
                        print(
                            '******\nz = %.3f，z_right = %.3f，P = %.5f\n因为 abs(z) < abs(z_right)（即z < z_right），或因为 P > alpha = %.3f，所以拒绝备择假设H1！\n******' % (
                            z, z_right, P, M[1]))
                    else:
                        print('******\n怎么会这么巧！\n******')
                else:
                    print('输入有误！')
                    twoHypothesisTest_avg()
            else:
                print('输入有误！')
                twoHypothesisTest_avg()

        # 匹配小样本且两总体各观察值的配对差d服从正态分布
        elif a == '2':
            # 直接输入样本统计量
            if b == '1':
                L = [float(n) for n in input('请依次输入样本容量、配对差的平均值、总体或样本配对差的标准差：').split()]
                M = [float(n) for n in input('请依次输入均值之差的假设值、显著性水平：').split()]
                if c == '1':
                    t = (L[1] - M[0]) / (L[2] / pow(L[0], 0.5))
                    t_right = scipy.stats.t.ppf(1 - M[1] / 2, L[0] - 1)
                    t_left = scipy.stats.t.ppf(M[1] / 2, L[0] - 1)
                    P = 2 * (1 - scipy.stats.t.cdf(abs(t), L[0] - 1))
                    if abs(t) > abs(t_right):
                        print(
                            '******\nt = %.3f，t_left = %.3f或t_right = %.3f，P = %.5f\n因为 abs(t) > abs(t_right)，或因为 P < alpha = %.3f，所以拒绝原假设H0！\n******' % (
                            t, t_left, t_right, P, M[1]))
                    elif abs(t) < abs(t_right):
                        print(
                            '******\nt = %.3f，t_left = %.3f或t_right = %.3f，P = %.5f\n因为 abs(t) < abs(t_right)，或因为 P > alpha = %.3f，所以拒绝备择假设H1！\n******' % (
                            t, t_left, t_right, P, M[1]))
                    else:
                        print('******\n怎么会这么巧！\n******')
                elif c == '2':
                    t = (L[1] - M[0]) / (L[2] / pow(L[0], 0.5))
                    t_left = scipy.stats.t.ppf(M[1], L[0] - 1)
                    P = 1 - scipy.stats.t.cdf(abs(t), L[0] - 1)
                    if t < t_left:
                        print(
                            '******\nt = %.3f，t_left = %.3f，P = %.5f\n因为 abs(t) > abs(t_left)（即t < t_left），或因为 P < alpha = %.3f，所以拒绝原假设H0！\n******' % (
                            t, t_left, P, M[1]))
                    elif t > t_left:
                        print(
                            '******\nt = %.3f，t_left = %.3f，P = %.5f\n因为 abs(t) < abs(t_left)（即t > t_left），或因为 P > alpha = %.3f，所以拒绝备择假设H1！\n******' % (
                            t, t_left, P, M[1]))
                    else:
                        print('******\n怎么会这么巧！\n******')
                elif c == '3':
                    t = (L[1] - M[0]) / (L[2] / pow(L[0], 0.5))
                    t_right = scipy.stats.t.ppf(1 - M[1], L[0] - 1)
                    P = 1 - scipy.stats.t.cdf(abs(t), L[0] - 1)
                    if t > t_right:
                        print(
                            '******\nt = %.3f，t_right = %.3f，P = %.5f\n因为 abs(t) > abs(t_right)（即t > t_right），或因为 P < alpha = %.3f，所以拒绝原假设H0！\n******' % (
                            t, t_right, P, M[1]))
                    elif t < t_right:
                        print(
                            '******\nt = %.3f，t_right = %.3f，P = %.5f\n因为 abs(t) < abs(t_right)（即t < t_right），或因为 P > alpha = %.3f，所以拒绝备择假设H1！\n******' % (
                            t, t_right, P, M[1]))
                    else:
                        print('******\n怎么会这么巧！\n******')
                else:
                    print('输入有误！')
                    twoHypothesisTest_avg()
            # 输入样本观测值
            elif b == '2':
                L1 = dataInput()
                L2 = dataInput()
                M = [float(n) for n in input('请依次输入均值之差的假设值、显著性水平：').split()]
                if c == '1':
                    t = (avg(delta(L1, L2)) - M[0]) / (stdev_u(delta(L1, L2)) / pow(len(L1), 0.5))
                    t_right = scipy.stats.t.ppf(1 - M[1] / 2, len(L1) - 1)
                    t_left = scipy.stats.t.ppf(M[1] / 2, len(L1) - 1)
                    P = 2 * (1 - scipy.stats.t.cdf(abs(t), len(L1) - 1))
                    if abs(t) > abs(t_right):
                        print(
                            '******\nt = %.3f，t_left = %.3f或t_right = %.3f，P = %.5f\n因为 abs(t) > abs(t_right)，或因为 P < alpha = %.3f，所以拒绝原假设H0！\n******' % (
                            t, t_left, t_right, P, M[1]))
                    elif abs(t) < abs(t_right):
                        print(
                            '******\nt = %.3f，t_left = %.3f或t_right = %.3f，P = %.5f\n因为 abs(t) < abs(t_right)，或因为 P > alpha = %.3f，所以拒绝备择假设H1！\n******' % (
                            t, t_left, t_right, P, M[1]))
                    else:
                        print('******\n怎么会这么巧！\n******')
                elif c == '2':
                    t = (avg(delta(L1, L2)) - M[0]) / (stdev_u(delta(L1, L2)) / pow(len(L1), 0.5))
                    t_left = scipy.stats.t.ppf(M[1], len(L1) - 1)
                    P = 1 - scipy.stats.t.cdf(abs(t), len(L1) - 1)
                    if t < t_left:
                        print(
                            '******\nt = %.3f，t_left = %.3f，P = %.5f\n因为 abs(t) > abs(t_left)（即t < t_left），或因为 P < alpha = %.3f，所以拒绝原假设H0！\n******' % (
                            t, t_left, P, M[1]))
                    elif t > t_left:
                        print(
                            '******\nt = %.3f，t_left = %.3f，P = %.5f\n因为 abs(t) < abs(t_left)（即t > t_left），或因为 P > alpha = %.3f，所以拒绝备择假设H1！\n******' % (
                            t, t_left, P, M[1]))
                    else:
                        print('******\n怎么会这么巧！\n******')
                elif c == '3':
                    t = (avg(delta(L1, L2)) - M[0]) / (stdev_u(delta(L1, L2)) / pow(len(L1), 0.5))
                    t_right = scipy.stats.t.ppf(1 - M[1], len(L1) - 1)
                    P = 1 - scipy.stats.t.cdf(abs(t), len(L1) - 1)
                    if t > t_right:
                        print(
                            '******\nt = %.3f，t_right = %.3f，P = %.5f\n因为 abs(t) > abs(t_right)（即t > t_right），或因为 P < alpha = %.3f，所以拒绝原假设H0！\n******' % (
                            t, t_right, P, M[1]))
                    elif t < t_right:
                        print(
                            '******\nt = %.3f，t_right = %.3f，P = %.5f\n因为 abs(t) < abs(t_right)（即t < t_right），或因为 P > alpha = %.3f，所以拒绝备择假设H1！\n******' % (
                            t, t_right, P, M[1]))
                    else:
                        print('******\n怎么会这么巧！\n******')
                else:
                    print('输入有误！')
                    twoHypothesisTest_avg()
            else:
                print('输入有误！')
                twoHypothesisTest_avg()
        else:
            print('输入有误！')
            twoHypothesisTest_avg()
    else:
        print('输入有误！')
        twoHypothesisTest_avg()
    e = input('继续进行总体均值之差的假设检验请输入1，需要计算其他类型请输入2，退出请输入0：')
    if e == '0':
        return
    elif e == '1':
        twoHypothesisTest_avg()
    else:
        type_calling()


# 两个参数总体比例之差的假设检验
def twoHypothesisTest_pi():
    a = input('检验两个总体比例相等的假设请输入1，检验两个总体比例不等的假设请输入2：')
    b = input('双侧检验请输入1，左侧检验请输入2，右侧检验请输入3：')
    L1 = [float(n) for n in input('请依次输入样本1的容量、样本1的比例或观察量数量：').split()]
    L2 = [float(n) for n in input('请依次输入样本2的容量、样本2的比例或观察量数量：').split()]
    M = [float(n) for n in input('请依次输入比例之差的假设值（判断总体比例是否相等请输入0，是否相差某个数值请输入具体差值）、显著性水平：').split()]
    # 根据样本比例或观察量数量的大小判断该数值到底是样本比例还是观察者数量：观察者数量总是大于或等于1的（因为为0就没有必要计算），而样本比例总是小于1的（因为为1也没有必要计算）
    if L1[1] >= 1:
        L1[1] = L1[1] / L1[0]
    elif L1[1] < 1 and L1[1] > 0:
        L1[1] = L1[1]
    else:
        print('输入有误！')
        twoHypothesisTest_pi()
    if L2[1] >= 1:
        L2[1] = L2[1] / L2[0]
    elif L2[1] < 1 and L2[1] > 0:
        L2[1] = L2[1]
    else:
        print('样本2输入有误！')
        twoHypothesisTest_pi()
    # 检验两个总体比例相等的假设
    if a == '1':
        if b == '1':
            p = (L1[0] * L1[1] + L2[0] * L2[1]) / (L1[0] + L2[0])
            z = (L1[1] - L2[1]) / pow(p * (1 - p) * (1 / L1[0] + 1 / L2[0]), 0.5)
            z_right = scipy.stats.norm.ppf(1 - M[1] / 2)
            z_left = scipy.stats.norm.ppf(M[1] / 2)
            P = 2 * (1 - scipy.stats.norm.cdf(abs(z)))
            if abs(z) > abs(z_right):
                print(
                    '******\nz = %.3f，z_left = %.3f或z_right = %.3f，P = %.5f\n因为 abs(z) > abs(z_right)，或因为 P < alpha = %.3f，所以拒绝原假设H0！\n******' % (
                    z, z_left, z_right, P, M[1]))
            elif abs(z) < abs(z_right):
                print(
                    '******\nz = %.3f，z_left = %.3f或z_right = %.3f，P = %.5f\n因为 abs(z) < abs(z_right)，或因为 P > alpha = %.3f，所以拒绝备择假设H1！\n******' % (
                    z, z_left, z_right, P, M[1]))
            else:
                print('******\n怎么会这么巧！\n******')
        elif b == '2':
            p = (L1[0] * L1[1] + L2[0] * L2[1]) / (L1[0] + L2[0])
            z = (L1[1] - L2[1]) / pow(p * (1 - p) * (1 / L1[0] + 1 / L2[0]), 0.5)
            z_left = scipy.stats.norm.ppf(M[1])
            P = 1 - scipy.stats.norm.cdf(abs(z))
            if z < z_left:
                print(
                    '******\nz = %.3f，z_left = %.3f，P = %.5f\n因为 abs(z) > abs(z_left)（即z < z_left），或因为 P < alpha = %.3f，所以拒绝原假设H0！\n******' % (
                    z, z_left, P, M[1]))
            elif z > z_left:
                print(
                    '******\nz = %.3f，z_left = %.3f，P = %.5f\n因为 abs(z) < abs(z_left)（即z > z_left），或因为 P > alpha = %.3f，所以拒绝备择假设H1！\n******' % (
                    z, z_left, P, M[1]))
            else:
                print('******\n怎么会这么巧！\n******')
        elif b == '3':
            p = (L1[0] * L1[1] + L2[0] * L2[1]) / (L1[0] + L2[0])
            z = (L1[1] - L2[1]) / pow(p * (1 - p) * (1 / L1[0] + 1 / L2[0]), 0.5)
            z_right = scipy.stats.norm.ppf(1 - M[1])
            P = 1 - scipy.stats.norm.cdf(abs(z))
            if z > z_right:
                print(
                    '******\nz = %.3f，z_right = %.3f，P = %.5f\n因为 abs(z) > abs(z_right)（即z > z_right），或因为 P < alpha = %.3f，所以拒绝原假设H0！\n******' % (
                    z, z_right, P, M[1]))
            elif z < z_right:
                print(
                    '******\nz = %.3f，z_right = %.3f，P = %.5f\n因为 abs(z) < abs(z_right)（即z < z_right），或因为 P > alpha = %.3f，所以拒绝备择假设H1！\n******' % (
                    z, z_right, P, M[1]))
            else:
                print('******\n怎么会这么巧！\n******')
        else:
            print('输入有误！')
            twoHypothesisTest_pi()
    # 检验两个总体比例不等的假设
    elif a == '2':
        if b == '1':
            z = ((L1[1] - L2[1]) - M[0]) / pow(L1[1] * (1 - L1[1]) / L1[0] + L2[1] * (1 - L2[1]) / L2[0], 0.5)
            z_right = scipy.stats.norm.ppf(1 - M[1] / 2)
            z_left = scipy.stats.norm.ppf(M[1] / 2)
            P = 2 * (1 - scipy.stats.norm.cdf(abs(z)))
            if abs(z) > abs(z_right):
                print(
                    '******\nz = %.3f，z_left = %.3f或z_right = %.3f，P = %.5f\n因为 abs(z) > abs(z_right)，或因为 P < alpha = %.3f，所以拒绝原假设H0！\n******' % (
                    z, z_left, z_right, P, M[1]))
            elif abs(z) < abs(z_right):
                print(
                    '******\nz = %.3f，z_left = %.3f或z_right = %.3f，P = %.5f\n因为 abs(z) < abs(z_right)，或因为 P > alpha = %.3f，所以拒绝备择假设H1！\n******' % (
                    z, z_left, z_right, P, M[1]))
            else:
                print('******\n怎么会这么巧！\n******')
        elif b == '2':
            z = ((L1[1] - L2[1]) - M[0]) / pow(L1[1] * (1 - L1[1]) / L1[0] + L2[1] * (1 - L2[1]) / L2[0], 0.5)
            z_left = scipy.stats.norm.ppf(M[1])
            P = 1 - scipy.stats.norm.cdf(abs(z))
            if z < z_left:
                print(
                    '******\nz = %.3f，z_left = %.3f，P = %.5f\n因为 abs(z) > abs(z_left)（即z < z_left），或因为 P < alpha = %.3f，所以拒绝原假设H0！\n******' % (
                    z, z_left, P, M[1]))
            elif z > z_left:
                print(
                    '******\nz = %.3f，z_left = %.3f，P = %.5f\n因为 abs(z) < abs(z_left)（即z > z_left），或因为 P > alpha = %.3f，所以拒绝备择假设H1！\n******' % (
                    z, z_left, P, M[1]))
            else:
                print('******\n怎么会这么巧！\n******')
        elif b == '3':
            z = ((L1[1] - L2[1]) - M[0]) / pow(L1[1] * (1 - L1[1]) / L1[0] + L2[1] * (1 - L2[1]) / L2[0], 0.5)
            z_right = scipy.stats.norm.ppf(1 - M[1])
            P = 1 - scipy.stats.norm.cdf(abs(z))
            if z > z_right:
                print(
                    '******\nz = %.3f，z_right = %.3f，P = %.5f\n因为 abs(z) > abs(z_right)（即z > z_right），或因为 P < alpha = %.3f，所以拒绝原假设H0！\n******' % (
                    z, z_right, P, M[1]))
            elif z < z_right:
                print(
                    '******\nz = %.3f，z_right = %.3f，P = %.5f\n因为 abs(z) < abs(z_right)（即z < z_right），或因为 P > alpha = %.3f，所以拒绝备择假设H1！\n******' % (
                    z, z_right, P, M[1]))
            else:
                print('******\n怎么会这么巧！\n******')
        else:
            print('输入有误！')
            twoHypothesisTest_pi()
    else:
        print('输入有误！')
        twoHypothesisTest_pi()
    c = input('继续进行总体比例之差的假设检验请输入1，需要计算其他类型请输入2，退出请输入0：')
    if c == '0':
        return
    elif c == '1':
        twoHypothesisTest_pi()
    else:
        type_calling()


# 两个参数总体方差之比的假设检验
def twoHypothesisTest_sigma2():
    a = input('直接输入样本统计量请输入1，输入样本观测值请输入2：')
    b = input('双侧检验请输入1，左侧检验请输入2，右侧检验请输入3：')
    if a == '1':
        L1 = [float(n) for n in input('请依次输入样本1的容量、样本1的方差：').split()]
        L2 = [float(n) for n in input('请依次输入样本2的容量、样本2的方差：').split()]
        M = [float(n) for n in input('请依次输入方差之比的假设值（判断总体方差是否相等请输入1，是否相差某个倍数请输入具体倍数值）、显著性水平：').split()]
        if b == '1':
            F = L1[1] / L2[1] / M[0]
            F_right = scipy.stats.f.ppf(1 - M[1] / 2, L1[0] - 1, L2[0] - 1)
            F_left = 1 / scipy.stats.f.ppf(1 - M[1] / 2, L2[0] - 1, L1[0] - 1)
            # F_left_a =  scipy.stats.f.ppf(M[1]/2, L1[0]-1, L2[0]-1)
            # print('F_left = %.3f，F_left_a = %.3f'%(F_left,F_left_a))
            P = min(2 * scipy.stats.f.cdf(F, L1[0] - 1, L2[0] - 1),
                    2 * (1 - scipy.stats.f.cdf(F, L1[0] - 1, L2[0] - 1)))
            if F < F_left or F > F_right:
                print(
                    '******\nF = %.3f，F_left = %.3f，F_right = %.3f，P = %.5f\n因为 F < F_left or F > F_right，或因为 P < alpha = %.3f，所以拒绝原假设H0！\n******' % (
                    F, F_left, F_right, P, M[1]))
            elif F_left < F < F_right:
                print(
                    '******\nF = %.3f，F_left = %.3f，F_right = %.3f，P = %.5f\n因为 F_left < F < F_right，或因为 P > alpha = %.3f，所以拒绝备择假设H1！\n******' % (
                    F, F_left, F_right, P, M[1]))
            else:
                print('******\n怎么会这么巧！\n******')
        elif b == '2':
            F = L1[1] / L2[1] / M[0]
            F_left = 1 / scipy.stats.f.ppf(1 - M[1], L2[0] - 1, L1[0] - 1)
            P = 1 - scipy.stats.f.cdf(F, L1[0] - 1, L2[0] - 1)
            if F < F_left:
                print(
                    '******\nF = %.3f，F_left = %.3f，P = %.5f\n因为 F < F_left，或因为 P < alpha = %.3f，所以拒绝原假设H0！\n******' % (
                    F, F_left, P, M[1]))
            elif F > F_left:
                print(
                    '******\nF = %.3f，F_left = %.3f，P = %.5f\n因为 F > F_left，或因为 P > alpha = %.3f，所以拒绝备择假设H1！\n******' % (
                    F, F_left, P, M[1]))
            else:
                print('******\n怎么会这么巧！\n******')
        elif b == '3':
            F = L1[1] / L2[1] / M[0]
            F_right = scipy.stats.f.ppf(1 - M[1], L1[0] - 1, L2[0] - 1)
            P = 1 - scipy.stats.f.cdf(F, L1[0] - 1, L2[0] - 1)
            if F > F_right:
                print(
                    '******\nF = %.3f，F_right = %.3f，P = %.5f\n因为 F > F_right，或因为 P < alpha = %.3f，所以拒绝原假设H0！\n******' % (
                    F, F_right, P, M[1]))
            elif F < F_right:
                print(
                    '******\nF = %.3f，F_right = %.3f，P = %.5f\n因为 F < F_right，或因为 P > alpha = %.3f，所以拒绝备择假设H1！\n******' % (
                    F, F_right, P, M[1]))
            else:
                print('******\n怎么会这么巧！\n******')
        else:
            print('输入有误！')
            twoHypothesisTest_sigma2()
    elif a == '2':
        L1 = dataInput()
        L2 = dataInput()
        M = [float(n) for n in input('请依次输入方差之比的假设值（判断总体方差是否相等请输入1，是否相差某个倍数请输入具体倍数值）、显著性水平：').split()]
        if b == '1':
            F = var_u(L1) / var_u(L2) / M[0]
            F_right = scipy.stats.f.ppf(1 - M[1] / 2, len(L1) - 1, len(L2) - 1)
            F_left = 1 / scipy.stats.f.ppf(1 - M[1] / 2, len(L2) - 1, len(L1) - 1)
            F_left_a = scipy.stats.f.ppf(M[1] / 2, len(L2) - 1, len(L1) - 1)
            P = min(2 * scipy.stats.f.cdf(F, len(L1) - 1, len(L2) - 1),
                    2 * (1 - scipy.stats.f.cdf(F, len(L1) - 1, len(L2) - 1)))
            if F < F_left or F > F_right:
                print(
                    '******\nF = %.3f，F_left = %.3f，F_right = %.3f，P = %.5f\n因为 F < F_left or F > F_right，或因为 P < alpha = %.3f，所以拒绝原假设H0！\n******' % (
                    F, F_left, F_right, P, M[1]))
            elif F_left < F < F_right:
                print(
                    '******\nF = %.3f，F_left = %.3f，F_right = %.3f，P = %.5f\n因为 F_left < F < F_right，或因为 P > alpha = %.3f，所以拒绝备择假设H1！\n******' % (
                    F, F_left, F_right, P, M[1]))
            else:
                print('******\n怎么会这么巧！\n******')
        elif b == '2':
            F = var_u(L1) / var_u(L2) / M[0]
            F_left = 1 / scipy.stats.f.ppf(1 - M[1], len(L2) - 1, len(L1) - 1)
            P = 1 - scipy.stats.f.cdf(F, len(L1) - 1, len(L2) - 1)
            if F < F_left:
                print(
                    '******\nF = %.3f，F_left = %.3f，P = %.5f\n因为 F < F_left，或因为 P < alpha = %.3f，所以拒绝原假设H0！\n******' % (
                    F, F_left, P, M[1]))
            elif F > F_left:
                print(
                    '******\nF = %.3f，F_left = %.3f，P = %.5f\n因为 F > F_left，或因为 P > alpha = %.3f，所以拒绝备择假设H1！\n******' % (
                    F, F_left, P, M[1]))
            else:
                print('******\n怎么会这么巧！\n******')
        elif b == '3':
            F = var_u(L1) / var_u(L2) / M[0]
            F_right = scipy.stats.f.ppf(1 - M[1], len(L1) - 1, len(L2) - 1)
            P = 1 - scipy.stats.f.cdf(F, len(L1) - 1, len(L2) - 1)
            if F > F_right:
                print(
                    '******\nF = %.3f，F_right = %.3f，P = %.5f\n因为 F > F_right，或因为 P < alpha = %.3f，所以拒绝原假设H0！\n******' % (
                    F, F_right, P, M[1]))
            elif F < F_right:
                print(
                    '******\nF = %.3f，F_right = %.3f，P = %.5f\n因为 F < F_right，或因为 P > alpha = %.3f，所以拒绝备择假设H1！\n******' % (
                    F, F_right, P, M[1]))
            else:
                print('******\n怎么会这么巧！\n******')
        else:
            print('输入有误！')
            twoHypothesisTest_sigma2()
    else:
        print('输入有误！')
        twoHypothesisTest_sigma2()
    c = input('继续进行总体方差的假设检验请输入1，需要计算其他类型请输入2，退出请输入0：')
    if c == '0':
        return
    elif c == '1':
        twoHypothesisTest_sigma2()
    else:
        type_calling()


# 问题类型：
# 定义函数类型调用识别函数
def type_calling():
    name = input('请输入想要计算的类型(例如，平均数、方差、参数估计、假设检验等）：')
    if '平均' in name or 'avg' in name or 'ave' in name or 'AVG' in name or 'mean' in name:
        avg_calling()
    elif '方差' in name or 'var' in name or 'dev' in name or 'VAR' in name or 'DEV' in name:
        d = int(input('计算总体方差（原始方差）请输入1，计算样本方差（修正方差、无偏方差）请输入0：'))
        if d == 1:
            var_calling()
        elif d == 0:
            var_u_calling()
        else:
            print('输入有误！请检查后重新输入！')
            type_calling()
    elif '标准差' in name or 'var' in name or 'dev' in name or 'std' in name:
        d = int(input('计算总体标准差（原始标准差）请输入1，计算样本标准差（修正标准差、无偏标准差）请输入0：'))
        if d == 1:
            stdev_calling()
        elif d == 0:
            stdev_u_calling()
        else:
            print('输入有误！请检查后重新输入！')
            type_calling()
    elif '参数' in name or '估计' in name or 'par' in name or ('est' in name and 'test' not in name) or (
            'EST' in name and 'TEST' not in name):
        parameterEstimate_calling()
    elif '假设' in name or '检验' in name or 'hyp' in name or 'tes' in name or 'TES' in name:
        hypothesisTest_calling()
    elif '退出' in name or 'esc' in name or 'ESC' in name or 'Esc' in name:
        return
    else:
        print('输入有误！请检查后重新输入！')
        type_calling()


# 定义样本输入函数
def dataInput():
    L = [float(n) for n in input('请输入要计算的数据：').split()]
    yN = input('请问输入是否正确？正确请输入Y；错误请输入N：')
    if yN == 'Y' or yN == 'y':
        return L
    elif yN == 'N' or yN == 'n':
        No = [int(n) for n in input('请问要依次修改哪几个数：').split()]
        Mod = [int(n) for n in input('请依次输入要修改成什么值：').split()]
        j = 0
        for i in No:
            L[(i - 1)] = Mod[j]
            j = j + 1
        return L


# 定义主函数
def main():
    global G, G1, G2
    G = []
    G1 = []
    G2 = []
    type_calling()


main()
