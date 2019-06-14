#!/usr/bin/env python3
# coding=utf-8


# 定义月份缩写转换函数
def month():
    n = input('请输入月份数字(1-12)： ')
    months = "JanFebMarAprMayJunJulAugSepOctNovDec"
    pos = (int(n) - 1) * 3
    monthAbbrev = months[pos:pos + 3]
    print("月份简写是：" + monthAbbrev + ".")


# 定义星期缩写转换函数
def week():
    n = input('请输入星期数字(1-7)： ')
    weeks = "Mon TuesWed ThurFri Sat Sun "
    pos = (int(n) - 1) * 4
    weekAbbrev = weeks[pos:pos + 4]
    weekA = weekAbbrev.rstrip()
    print("星期简写是：" + weekA + ".")


def main():
    n = input('请问需要转换何种类型(月份请输入M，星期请输入W)： ')
    if n == "m" or n == "M":
        month()
    elif n == "w" or n == "W":
        week()
    else:
        print("输入类型有误，请重新输入！")
        main()
    print("\n")
    J = input("继续请输入Y，退出请输入任意键： ")
    if J == "y" or J == "Y":
        print("\n")
        main()
    else:
        return


main()
print("\n")
input("按Enter退出！")
