#!/usr/bin/env python3
# coding=utf-8


from random import random
from time import process_time, perf_counter

from math import sqrt


def d_input():
    n = int(input('请输入抛洒点个数：'))
    return n


def d_output(n, pi):
    print('抛洒点个数为%10d时，PI值是%.8f，程序运行时间是%-5.5ss，%-5.5ss\n' % (n, pi, process_time(), perf_counter()))
    yn = input('继续请输入Y，退出请输入任意键：')
    if yn == 'Y' or yn == 'y':
        main()
    else:
        return


def PI_calculate(n):
    hits = 0
    pi = []
    process_time()
    perf_counter()

    for i in range(1, n):
        x, y = random(), random()
        dist = sqrt(x ** 2 + y ** 2)
        if dist <= 1.0:
            hits = hits + 1
    pi = 4 * (hits / n)
    return pi


def main():
    n = d_input()
    pi = PI_calculate(n)
    d_output(n, pi)


main()
