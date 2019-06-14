#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""

"""

import time

# # 指定数字位置停10s后继续
# pause_number = 1000
# count = 0
# while count < 100000:
#     if count != pause_number:
#         print("loop:", count)
#     elif count == pause_number:
#         print("已经到达%d！将在10s后继续！" % pause_number)
#         for i in range(10):
#             print(10-i)
#             mytime.sleep(1)
#     count += 1


# 指定分位位置停5s后继续
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
            break
