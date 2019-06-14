#!/usr/bin/env python3
# -*- coding:UTF-8 -*-


"""
打印井号阵列
"""

if __name__ == "__main__":
    rows = int(input("请输入要打印的行数："))

    for row in range(1, rows + 1):
        for i in range(1, rows * 2):
            # 每行总字符数为rows*2-1，其中#个数为row*2-1，空格个数为rows*2-row*2，左右各有rows-row个
            if i <= rows - row or i >= rows + row:
                print(" ", end="")
            else:
                print("#", end="")
        print("\n", end="")
