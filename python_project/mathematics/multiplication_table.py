#!/usr/bin/env python3
# -*- coding:UTF-8 -*-


"""
打印乘法口诀表
"""

if __name__ == "__main__":
    # 乘数结果为个位数，输出时，乘数结果左边补一个空格
    for i in range(1, 10):
        for j in range(1, 1 + i):
            print(str(j) + "*" + str(i) + "=" + ((" " + str(i * j)) if i * j < 10 else (str(i * j))), end="  ")
        print("\n")
