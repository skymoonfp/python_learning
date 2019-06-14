#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""

"""

import time

import schedule


def func1():
    print("我是神！")


def func2():
    print("我是猪！")


if __name__ == "__main__":

    # schedule.every(4).seconds.do(func1)
    # schedule.every(6).seconds.do(func2)
    # while True:
    #     schedule.run_pending()
    #     time.sleep(2)
    #     print("-")

    # 第一次输出（02s）：-
    # 第二次输出（04s）：-
    #                  我是神！
    # 第三次输出（06s）：-
    #                  我是猪！
    # 第四次输出（08s）：-
    #                  我是神！
    # 第五次输出（10s）：-
    # 第六次输出（12s）：-
    #                  我是神！
    #                  我是猪！
    # 第七次输出（14s）：同第一次

    # schedule.every(2).seconds.do(func1)
    # schedule.every(6).seconds.do(func2)
    # while True:
    #     schedule.run_pending()
    #     time.sleep(2)
    #     print("-")

    # 第一次输出（02s）：-
    #                  我是神！
    # 第二次输出（04s）：-
    #                  我是神！
    # 第三次输出（06s）：-
    #                  我是猪！
    #                  我是神！
    # 第四次输出（08s）：同第一次

    schedule.every(3).seconds.do(func1)
    schedule.every(6).seconds.do(func2)
    while True:
        schedule.run_pending()
        time.sleep(2)
        print("-")

    # 第一次输出（02s）：-
    # 第二次输出（04s）：-
    #                  我是神！
    # 第三次输出（06s）：-
    #                  我是猪！
    # 第四次输出（08s）：-
    #                  我是神！
    # 第五次输出（10s）：-
    # 第六次输出（12s）：-
    #                  我是神！
    #                  我是猪！
    # 第七次输出（14s）：同第一次
