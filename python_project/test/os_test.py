#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""

"""

import os
import time

# 指定分位位置停5s后清屏继续
n = 100
count = 1
pos = 4
m = n
pause_list = list(range(m // pos, m - m % pos, m // pos))
pause_list.append(n + 1)
for pause_number in pause_list:
    while count <= n:
        if count != pause_number:
            print("\033[0mloop:", count)
            count += 1
        elif count == pause_number:
            print("\033[1;31m已经到达\033[22;37m%d分位\033[22;35m%d\033[1;31m！将在\033[22;33m5s\033[1;31m后继续！\033[22;33m" % (
            pos, pause_number))
            for i in range(5):
                print("%ds" % (5 - i))
                time.sleep(1)
            count += 1
            os.system("cls")
            break
