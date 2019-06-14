#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def move(n, a, b, c):
    if n == 1:
        print('move', a, '-->', c)
    else:
        move(n - 1, a, c, b)
        move(1, a, b, c)
        move(n - 1, b, a, c)


n = int(input('请输入盘子总数: '))
print('移动方法是: ')
move(n, 'A', 'B', 'C')
print('\n')
input('Please press Enter to exit!')
