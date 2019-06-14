#!/usr/bin/env python3
# coding=utf-8


from random import random
from time import process_time, perf_counter

from math import sqrt


def d_input():
    N = [int(n) for n in input('请输入抛洒点个数：').split()]
    return N


def d_output(N, PI):
    for i in range(len(N)):
        print('抛洒点个数为%10d时，PI值是%.8f，程序运行时间是%-5.5ss，%-5.5ss\n' % (N[i], PI[i], process_time(), perf_counter()))


def PI_calculate(N):
    hits = 0
    PI = []
    process_time()
    perf_counter()

    for n in N:
        for i in range(1, n):
            x, y = random(), random()
            dist = sqrt(x ** 2 + y ** 2)
            if dist <= 1.0:
                hits = hits + 1
        PI.append(4 * (hits / n))
    return PI


def main():
    N = d_input()
    PI = PI_calculate(N)
    d_output(N, PI)


main()
