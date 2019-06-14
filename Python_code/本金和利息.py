#!/usr/bin/env python3
# -*- coding:utf-8 -*-


def createTable(principal, apr):
    # 为每一年绘制星号的增长图
    for year in range(1, 11):
        principal = principal * (1 + apr)
        print("%2d" % year, end='')
        total = caculateNum(principal)
        print("*" * total)
    print(" 0.0K     2.5K     5.0k     7.5K     10.0K")


def caculateNum(principal):
    # 计算星号数量
    total = int(principal * 4 / 1000.0)
    return total


def main():
    print("This program plots the growth of a 10-year investment.")
    # 输入本金和利率
    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annualized interest rate: "))
    # 建立图表
    createTable(principal, apr)


main()
