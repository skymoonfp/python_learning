#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""


**************************
文件:     process_value_array.py
 IDE：    PyCharm
创建时间： 2019/5/28 0:36
@author： skymoon
"""

from ctypes import c_double, Structure
from multiprocessing import Process, Value as V1, Lock
from multiprocessing.sharedctypes import Value as V2, Array


def f(n, n2, a, a2):
    n.value = 3.1415927
    n2.value = n2.value + 1
    for i in range(len(a)):
        a[i] = -2 * a[i]
    list(a2).append(999)


def main1():
    num = V1('d', 0.0)
    num2 = V2("d", 1.1)
    arr = Array("i", range(10))
    arr2 = range(10)

    p = Process(target=f, args=(num, num2, arr, arr2))
    p.start()
    p.join()

    print(num.value, num2.value, list(arr), list(arr2))
    print(num.value, num2.value, arr[:], list(arr2))  # 同上
    print(num.value, num2.value, arr[:], arr2[:])  # 不同上
    # print(num.value, num2.value, arr.value, list(arr2))  # 错误


class Point(Structure):
    _fields_ = [('x', c_double), ('y', c_double)]


def modify(n, x, s, A):
    n.value **= 2
    x.value **= 2
    s.value = s.value.upper()
    for a in A:
        a.x **= 2
        a.y **= 2


def main2():
    lock = Lock()

    n = V2('i', 7)
    x = V2(c_double, 1.0 / 3.0, lock=False)
    s = Array('c', b'hello world', lock=lock)
    A = Array(Point, [(1.875, -6.25), (-5.75, 2.0), (2.375, 9.5)], lock=lock)

    p = Process(target=modify, args=(n, x, s, A))
    p.start()
    p.join()

    print(n.value)
    print(x.value)
    print(s.value)
    print([(a.x, a.y) for a in A])


if __name__ == '__main__':
    main1()
    main2()
