#! E:\DataAnalysis\Anaconda3\python.exe
# -*- coding:UTF-8 -*-

"""
实现加减乘除的运算
~~~~~~~~~~~~~~~~
add(num01,num02) --实现两数相加
sub(num01,num02) --实现两数相减
mul(num01,num02) --实现两数相乘
div(num01,num02) --实现两数相除
"""


def add(num01, num02):
    return num01 + num02


def sub(num01, num02):
    return num01 - num02


def mul(num01, num02):
    return num01 * num02


def div(num01, num02):
    return num01 / num02


# 调用add函数实现两数相加
# print(add(100, 200))
# print(sub(100, 200))
# print(mul(100, 200))
# print(div(100, 200))

# 指明程序的入口：main函数
if __name__ == "__main__":
    # 调用computation模块add函数进行加法计算
    print(add(100, 100))
