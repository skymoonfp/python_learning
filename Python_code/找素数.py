#!usr/bin/env python3
# -*- coding:utf-8 -*-


def primeNumber():
    # 输入范围
    a, b = eval(input('请分别输入要查找的范围的起、止值：\n'))

    for n in range(a, b + 1):
        for x in range(2, n):
            if n % x == 0:
                print(n, '=', x, '*', n // x)
                break
        else:
            print(n, '是一个素数！')


if __name__ == "__main__":
    primeNumber()
