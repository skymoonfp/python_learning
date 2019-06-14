#!/usr/bin/env python3
# coding=utf-8


# 定义斐波那契数列输出函数
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        if n < 1:
            yield ('斐波那契数列的第%3d项是:%8d' % ((n + 1), b))
        else:
            yield ('斐波那契数列的第%3d项是:%8d      第%3d项与第%3d项的比是：%.5f' % ((n + 1), b, (n + 1), n, float(b / a)))
        a, b = b, a + b
        n = n + 1
    return 'done'


# 定义主函数
def main():
    n = int(input('请输入想要输出的斐波那契数列的项数：'))
    for i in fib(n):
        print(i)


main()
