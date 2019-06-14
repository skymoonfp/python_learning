#!/usr/bin/env python3
# -*- coding:UTF-8 -*-


def check_input(input_number: str, lower_limit, upper_limit):
    """
    用来判断输入的内容是否符合要求！
    1.是否是一个数字
    2.是否在以下范围之内（包含lower_limit、upper_limit）：lower_limit~upper_limit
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    :param input_number: 输入的内容
    :param lower_limit: 范围最小值
    :param upper_limit: 范围最大值
    :return: 返回判断的结果
    """
    if input_number.lstrip('-').isdigit() and lower_limit <= int(input_number) <= upper_limit:
        return True
    else:
        return False


def number_input(name_number: str):
    """
    输入给定范围内的一个数字
    1.提示"请输入name_number（"年份"或"月份"）："，并等待用户输入
    2.当输入"年份"时，a、b不限大小；当输入月份时，a=1、b=12
    2.输入不是数字或者数字不在给定范围内，则说明"输入的name_number不符合要求！"
    3.输入符合要求，则返回输入的数字
    :param name_number: 输入变量对应的名称："月份"、"年份"
    :return: 返回符合要求的数值
    """
    # 判断name_number是否是"年份"或"月份"
    if name_number not in ["年份", "月份"]:
        print("要求输入的变量名称有误！")
        exit()

    # 年份时
    elif name_number == "年份":
        return year_input()

    # 月份时
    else:
        return month_input()


def year_input(name_number="年份"):
    """
    判断输入的年份是否有效，无效重新输入，直至输入为有效时止
    1.年份为整数
    2.公元前用负整数表示
    :param name_number: "年份"
    :return: 输入有效时返回输入值
    """
    # 输入年份值
    number = input("请输入" + name_number + ":\n")

    # 判断输入的值，并返回符合要求的值
    if check_input(number, -10 ** 38, 10 ** 38):
        return number

    else:
        print("输入的" + name_number + "不符合要求！")

        # 输入不符合要求时再次输入，直至得到符合要求的数值
        i = 1  # 设置循环调用哨兵
        while i:
            number = input("请再次输入" + name_number + "：\n")  # a、b的数值请根据实际要求进行替换 #
            if check_input(number, -10 ** 38, 10 ** 38):
                return number
                i = 0
            else:
                print("输入的" + name_number + "不符合要求！")


def month_input(name_number="月份"):
    """
    判断输入的月份是否有效，无效重新输入，直至输入为有效时止
    1.月份为整数
    2.范围在1~12之间
    :param name_number: "月份"
    :return: 输入有效时返回输入值
    """
    # 输入年份值
    number = input("请输入" + name_number + ":\n")

    # 判断输入的值，并返回符合要求的值
    if check_input(number, 1, 12):
        return number
    else:
        print("输入的" + name_number + "不符合要求！")

        # 输入不符合要求时再次输入，直至得到符合要求的数值
        i = 1  # 设置循环调用哨兵
        while i:
            number = input("请再次输入" + name_number + "：\n")  # a、b的数值请根据实际要求进行替换 #
            if check_input(number, 1, 12):
                return number
                i = 0
            else:
                print("输入的" + name_number + "不符合要求！")


def leap_year(year):
    """
    判断输入的年份是否为闰年
    1.判断年份是大于0还是小于0，如果小于0，将其取绝对值并减去1
    2.判断上面得到的数是否是闰年：
        （1）不能被4整除，则不是闰年
        （2）能被100整除但不能被400整除，则不是闰年
        （3）能被3200整除但不能被172800整除，则不是闰年
    :param year: 输入要判断的年份
    :return: 返回判断结果（闰年返回True，平年返回False）
    """
    if year < 0:
        year = abs(year) - 1
        if year % 4 != 0:
            return False
        elif year % 100 == 0 and year % 400 != 0:
            return False
        elif year % 3200 == 0 and year % 172800 != 0:
            return False
        else:
            return True


def days_of_month(year, month):
    """
    判断给定的年份的月份中有多少天
    1.一、三、五、七、八、十、十二月有31天
    2.四、六、九、十一月有30天
    3.闰年二月有29天，平年二月有28天
    :param year: 输入要判断的年份
    :param month: 输入要判断的月份
    :return: 返回天数
    """
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif leap_year(year):
        return 29
    else:
        return 28


if __name__ == "__main__":
    # 输入年份、月份
    year = int(number_input("年份"))
    month = int(number_input("月份"))
    print("%d年%d月有%d天！" % (year, month, days_of_month(year, month)))
