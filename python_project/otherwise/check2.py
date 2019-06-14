#!/usr/bin/env python3
# -*- coding:UTF-8 -*-


def check_input(input_string: str):
    """
    用来判断输入的内容是否符合要求！
    1.是否是一个数字
    2.是否在以下范围之内（包含a、b）：a~b   # 例如：a = -273.15, b = 10000
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    :param input_string: 输入的内容
    :return: 返回判断的结果
    """
    a = -273.15
    b = 10000
    if input_string.isdigit() and a <= int(input_string) <= b:
        return True
    else:
        return False


def number_input(name_number: str):
    """
    输入给定范围内的一个数字
    1.提示"请输入（name_number）【a~b之间】："，并等待用户输入
    2.输入不是数字或者数字不在给定范围内，则说明"输入的（name_number）不符合要求！"
    3.输入符合要求，则返回输入的数字
    :param name_number: 输入数值型变量对应的实际名称，如温度、学生成绩、长度等
    :return: 返回符合要求的数值
    """

    # 输入一个数值
    number = input("请输入" + name_number + "【a~b之间】：")  # a、b的数值请根据实际要求进行替换 #

    # 判断输入的值，并返回符合要求的值
    if check_input(number):
        return number
    else:
        print("输入的" + name_number + "不符合要求！")

        # 输入不符合要求时再次输入，直至得到符合要求的数值
        # 定义递归调用函数
        def number_input2(name_number2: str):
            number2 = input("请再次输入" + name_number2 + "【a~b之间】：")  # a、b的数值请根据实际要求进行替换 #
            if check_input(number2):
                return number2
            else:
                print("输入的" + name_number2 + "不符合要求！")
                return number_input2(name_number2)

        # 调用递归调用函数
        return number_input2(name_number)


if __name__ == "__main__":
    # maths_result = number_input("数学成绩")
    # chinese_result = number_input("语文成绩")
    temperature = float(number_input("温度"))
    print("你输入的温度值为：%.2f℃" % temperature)
