#!/usr/bin/env python3
# -*- coding:UTF-8 -*-


"""
************* 计算水仙花数 *************

水仙花数定义：
1.N位整数
2.每个位上的数字的N次幂之和等于它本身

************* 计算水仙花数 *************
"""

import timeit

from mytime import timing


# 判断一个给定数是否是水仙花数
# 计算水仙花数
def narcissistic_judge(number):
    number_figure = []  # 依次存放number的个位、十位、百位数……
    number_sum = 0  # 存放幂数之和
    figures = len(str(number))  # 给定数的位数

    for k in range(figures):
        # 计算相应位数上的数字
        number_figure.append((number % pow(10, k + 1) - number % pow(10, k)) / pow(10, k))
        # number_figure[k] = (number % pow(10, k + 1) - number % pow(10, k)) / pow(10, k)
        number_sum = number_sum + pow(number_figure[k], figures)

    if number == number_sum:
        return number
    else:
        return False


# 输出给定范围内的水仙花数
def narcissistic_number(figures):
    # 变量定义
    narcissisticnumber = []

    # 判断输入的位数（参数figures)是否为正整数
    if (not isinstance(figures, int)) or figures <= 0:
        print("输入位数有误，请检查后重新输入！")
    else:
        # 输出已经位数的整数的取值范围的上下限值
        number_down = pow(10, figures - 1)
        number_up = pow(10, figures) - 1

        # 计算水仙花数
        for i in range(number_down, number_up + 1):
            if narcissistic_judge(i) != False:
                narcissisticnumber.append(narcissistic_judge(i))

        # 输出结果
        if narcissisticnumber == []:
            print("%d位数（%d~%d）中没有水仙花数！\n" % (figures, number_down, number_up))
        else:
            print("所有%d位数（%d~%d）中的水仙花数为:" % (figures, number_down, number_up))
            print(narcissisticnumber)


# 计算输出给定范围内的水仙花数的时间
@timing.timer
def narcissistic_number2(figures):
    # 变量定义
    narcissisticnumber = []

    # 判断输入的位数（参数figures)是否为正整数
    if (not isinstance(figures, int)) or figures <= 0:
        print("输入位数有误，请检查后重新输入！")
    else:
        # 输出已经位数的整数的取值范围的上下限值
        number_down = pow(10, figures - 1)
        number_up = pow(10, figures) - 1

        # 计算水仙花数
        for i in range(number_down, number_up + 1):
            if narcissistic_judge(i) != False:
                narcissisticnumber.append(narcissistic_judge(i))

        # 输出结果
        if narcissisticnumber == []:
            print("%d位数（%d~%d）中没有水仙花数！\n" % (figures, number_down, number_up))
        else:
            print("所有%d位数（%d~%d）中的水仙花数为:" % (figures, number_down, number_up))
            print(narcissisticnumber)


if __name__ == "__main__":
    figures = int(input("请输入要查找的整数位数(大于7请慎重，计算时间过长）：\n"))
    narcissistic_number(figures)
    print()

    t = timeit.Timer(lambda: narcissistic_number(figures))
    print(t.timeit(number=2 * 3))
    print()

    t = narcissistic_number2(figures)
