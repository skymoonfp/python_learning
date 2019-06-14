#!/usr/bin/env python3
# -*- coding:utf-8 -*-


import numpy as np
import scipy.stats


# 定义数组(或向量）差值计算函数
def delta(X1, X2):
    D = []
    i = 0
    if len(X1) != len(X2):
        print('两组数组（或向量）的元素数量（或维度）不相等，无法计算差值！\n')
        return
    else:
        while i < len(X1):
            D.append(X1[i] - X2[i])
            i = i + 1
        return D


# 定义拟合优度检验函数
def GOFT():
    # 数据输入
    L = [float(n) for n in input('请输入观察频数：\n').split()]
    L0 = [float(n) for n in input('请输入经验（或期望）数据：\n').split()]
    alpha = float(input('请输入显著性水平：\n'))

    # 计算期望值
    Le = []
    for l0 in L0:
        l0 = l0 / sum(L0)
        Le.append(sum(L) * l0)

    # 计算差值
    D = delta(L, Le)

    # 计算差值的平方
    S = []
    for d in D:
        S.append(d * d)

    # 计算差值平方与期望值之比
    Pi = []
    for i in range(len(L)):
        Pi.append(S[i] / Le[i])

    # 计算卡方值
    ch2 = 0
    for pi in Pi:
        ch2 = ch2 + pi
    P = 1 - scipy.stats.chi2.cdf(ch2, len(L) - 1)

    # 计算临界卡方值
    ch20 = scipy.stats.chi2.ppf(1 - alpha, len(L) - 1)

    # 比较卡方值和临界卡方值，得出结论
    # if chi2 >= chi20:
    #    print('观察频数fo是：%.3f\n期望频数fe是：%.3f\nfo-fe是：%.3f\n(fo-fe)**2是：%.3f\n(fo-fe)**2/fe是：%.3f\nchi2是：%.3f\nchi20是：%.3f\n因为chi2 >= chi20，所以拒绝原假设H0，接受H1！\n'%(L, Le, D, S, P, chi2, chi20))
    # else:
    #     print('观察频数fo是：%.3f\n期望频数fe是：%.3f\nfo-fe是：%.3f\n(fo-fe)**2是：%.3f\n(fo-fe)**2/fe是：%.3f\nchi2是：%.3f\nchi20是：%.3f\n因为chi2 < chi20，所以不能拒绝原假设H0，拒绝H1\n'%(L, Le, D, S, P, chi2, chi20))

    # 格式化数组
    L = np.array(L)
    Le = np.array(Le)
    D = np.array(D)
    S = np.array(S)
    Pi = np.array(Pi)
    # np.set_printoptions(precision = 3)
    np.set_printoptions(formatter={'float': '{:10.3f}'.format})

    # 进行比较，得出结论
    if ch2 >= ch20:
        print(' 观察频数fo    是：', L, '\n', '期望频数fe    是：', Le, '\n', ' fo-fe        是：', D, '\n', '(fo-fe)**2    是：', S,
              '\n', '(fo-fe)**2/fe 是：', Pi)
        print('chi2 是：%6.3f\nchi20是：%6.3f\nP    是：%6.3f\n因为chi2 >= chi20，所以拒绝原假设H0，接受H1！' % (ch2, ch20, P))
    else:
        print(' 观察频数fo    是：', L, '\n', '期望频数fe    是：', Le, '\n', ' fo-fe        是：', D, '\n', '(fo-fe)**2    是：', S,
              '\n', '(fo-fe)**2/fe 是：', Pi)
        print('chi2 是：%6.3f\nchi20是：%6.3f\nP    是：%6.3f\n因为chi2 < chi20，所以不能拒绝原假设H0，拒绝H1！' % (ch2, ch20, P))


# 定义独立性检验函数
def INDT():
    global col_count

    # 数据输入
    alpha = float(input('请输入显著性水平：\n'))
    yN = [str(n) for n in input('请选择数据输入方式（从文件输入请输入F或File，直接输入请输入任意键）：\n').split()]

    # 从文件输入
    if yN[0] == 'F' or yN[0] == 'f':
        L = []
        row_count = 0
        fileName = input("请输入数据所在的文件名：\n")
        infile = open(fileName, 'r')
        line = infile.readline()
        while line != "":
            for xStr in line.split(" "):
                L.append(eval(xStr))
            row_count = row_count + 1
            line = infile.readline()

        # 处理数据
        row_count = int(row_count)
        col_count = int(len(L) / row_count)
        for i in range(1, row_count + 1):
            locals()['row' + str(i)] = L[(i - 1) * col_count:i * col_count]
        for j in range(1, col_count + 1):
            locals()['col' + str(j)] = []
            for k in range(1, row_count + 1):
                locals()['col' + str(j)].append(L[(k - 1) * col_count + j - 1])

        # 计算期望值
        Le = []
        for i in range(1, row_count + 1):
            for j in range(1, col_count + 1):
                locals()['le_' + str(i) + '_' + str(j)] = sum(locals()['row' + str(i)]) * sum(
                    locals()['col' + str(j)]) / sum(L)
                Le.append(locals()['le_' + str(i) + '_' + str(j)])

        # 计算差值
        D = delta(L, Le)

        # 计算差值的平方
        S = []
        for d in D:
            S.append(d * d)

        # 计算差值平方与期望值之比
        Pi = []
        for i in range(len(L)):
            Pi.append(S[i] / Le[i])

        # 计算卡方值
        ch2 = 0
        for pi in Pi:
            ch2 = ch2 + pi
        P = 1 - scipy.stats.chi2.cdf(ch2, (row_count - 1) * (col_count - 1))

        # 计算临界卡方值
        ch20 = scipy.stats.chi2.ppf(1 - alpha, (row_count - 1) * (col_count - 1))

        # 计算Phai、c、V值
        Phai = pow(ch2 / sum(L), 0.5)
        c = pow(ch2 / (ch2 + sum(L)), 0.5)
        V = pow(ch2 / (sum(L) * min(row_count - 1, col_count - 1)), 0.5)

        # 格式化数组
        L = np.array(L)
        Le = np.array(Le)
        D = np.array(D)
        S = np.array(S)
        Pi = np.array(Pi)
        # np.set_printoptions(precision = 3)
        np.set_printoptions(formatter={'float': '{:10.3f}'.format})

        # 进行比较，得出结论
        if ch2 >= ch20:
            print(' 观察频数fo    是：', L, '\n', '期望频数fe    是：', Le, '\n', ' fo-fe        是：', D, '\n', '(fo-fe)**2    是：',
                  S, '\n', '(fo-fe)**2/fe 是：', Pi)
            print(
                'chi2 是：%6.3f\nchi20是：%6.3f\nP    是：%6.3f\nPhai 是：%6.3f\nc    是：%6.3f\nV    是：%6.3f\n因为chi2 >= chi20，所以拒绝原假设H0，接受H1！即存在依赖关系！' % (
                ch2, ch20, P, Phai, c, V))
        else:
            print(' 观察频数fo    是：', L, '\n', '期望频数fe    是：', Le, '\n', ' fo-fe        是：', D, '\n', '(fo-fe)**2    是：',
                  S, '\n', '(fo-fe)**2/fe 是：', Pi)
            print(
                'chi2 是：%6.3f\nchi20是：%6.3f\nP    是：%6.3f\nPhai 是：%6.3f\nc    是：%6.3f\nV    是：%6.3f\n因为chi2 < chi20，所以不能拒绝原假设H0，拒绝H1！即相互独立！' % (
                ch2, ch20, P, Phai, c, V))

    # 直接输入
    else:
        print('请逐行输入观察频数，每输入完一行请回车！数据输入结束请输入Over!\n')
        L = []
        while True:
            M = input()
            if M == 'Over' or M == 'over':
                break  # 读到Over退出输入
            else:
                M = [float(n) for n in M.split()]
                for m in M:
                    L.append(m)  # 把输入的所有数据顺序加入数组L中
                col_count = len(M)

        # 处理数据
        col_count = int(col_count)
        row_count = int(len(L) / col_count)
        for i in range(1, row_count + 1):
            locals()['row' + str(i)] = L[(i - 1) * col_count:i * col_count]
        for j in range(1, col_count + 1):
            locals()['col' + str(j)] = []
            for k in range(1, row_count + 1):
                locals()['col' + str(j)].append(L[(k - 1) * col_count + j - 1])

        # 计算期望值
        Le = []
        for i in range(1, row_count + 1):
            for j in range(1, col_count + 1):
                locals()['le_' + str(i) + '_' + str(j)] = sum(locals()['row' + str(i)]) * sum(
                    locals()['col' + str(j)]) / sum(L)
                Le.append(locals()['le_' + str(i) + '_' + str(j)])

        # 计算差值
        D = delta(L, Le)

        # 计算差值的平方
        S = []
        for d in D:
            S.append(d * d)

        # 计算差值平方与期望值之比
        Pi = []
        for i in range(len(L)):
            Pi.append(S[i] / Le[i])

        # 计算卡方值
        ch2 = 0
        for pi in Pi:
            ch2 = ch2 + pi
        P = 1 - scipy.stats.chi2.cdf(ch2, (row_count - 1) * (col_count - 1))

        # 计算临界卡方值
        ch20 = scipy.stats.chi2.ppf(1 - alpha, (row_count - 1) * (col_count - 1))

        # 计算Phai、c、V值
        Phai = pow(ch2 / sum(L), 0.5)
        c = pow(ch2 / (ch2 + sum(L)), 0.5)
        V = pow(ch2 / (sum(L) * min(row_count - 1, col_count - 1)), 0.5)

        # 格式化数组
        L = np.array(L)
        Le = np.array(Le)
        D = np.array(D)
        S = np.array(S)
        Pi = np.array(Pi)
        # np.set_printoptions(precision = 3)
        np.set_printoptions(formatter={'float': '{:10.3f}'.format})

        # 进行比较，得出结论
        if ch2 >= ch20:
            print(' 观察频数fo    是：', L, '\n', '期望频数fe    是：', Le, '\n', ' fo-fe        是：', D, '\n', '(fo-fe)**2    是：',
                  S, '\n', '(fo-fe)**2/fe 是：', Pi)
            print(
                'chi2 是：%6.3f\nchi20是：%6.3f\nP    是：%6.3f\nPhai 是：%6.3f\nc    是：%6.3f\nV    是：%6.3f\n因为chi2 >= chi20，所以拒绝原假设H0，接受H1！即存在依赖关系！' % (
                ch2, ch20, P, Phai, c, V))
        else:
            print(' 观察频数fo    是：', L, '\n', '期望频数fe    是：', Le, '\n', ' fo-fe        是：', D, '\n', '(fo-fe)**2    是：',
                  S, '\n', '(fo-fe)**2/fe 是：', Pi)
            print(
                'chi2 是：%6.3f\nchi20是：%6.3f\nP    是：%6.3f\nPhai 是：%6.3f\nc    是：%6.3f\nV    是：%6.3f\n因为chi2 < chi20，所以不能拒绝原假设H0，拒绝H1！即相互独立！' % (
                ch2, ch20, P, Phai, c, V))


# 问题类型：
# 定义函数类型调用识别函数
def type_calling():
    name = input('进行拟合优度检验请输入GOFT，进行独立性检验请输入INDT：\n')
    if name == 'goft' or name == 'GOFT':
        GOFT()
    elif name == 'indt' or name == 'INDT':
        INDT()
    else:
        print('输入有误！请检查后重新输入！')
        type_calling()


# 定义主函数
def main():
    global col_count
    col_count = 0
    type_calling()


main()
