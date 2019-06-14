#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""
员工信息表检索
————————————————————————
1.用户可以模糊查询员工信息
2.显示匹配了多少条
3.匹配字符高亮输出
"""


def employee_table_search(file_name: str, text: str):
    """
    在给定文件中检索给定内容，返回所有包含给定内容的信息（以row为单位）
    :param file_name: 给定文件
    :param text: 给定内容
    :return: 检索结果list
    """
    search_result = []
    employee_table = open(file_name, "r")

    while True:
        employee = employee_table.readline().strip()
        if employee != "":
            if text in employee:
                search_result.append(employee)
            else:
                continue
        else:
            break

    employee_table.close()
    return search_result


def output_format(context: str, text: str, format: str):
    """
    对给定文本中的给定内容按给定格式打印
    :param context: 给定文本
    :param text: 给定内容
    :param format: 给定格式
    :return: 直接打印，无返回
    """
    output_context = context.replace(text, format + text + "\033[0m")
    print(output_context)


if __name__ == "__main__":
    file_name = input("请输入要检索的文件：\n")
    text = input("请输入要检索的内容：\n")
    search_result = employee_table_search(file_name, text)

    # 格式化输出
    print("\033[1;32m" + file_name + "\033[0m" + "中共有" + "\033[1;35m" + str(
        len(search_result)) + "\033[0m" + "条记录包含" + "\033[1;31m" + text + "\033[0m" + "：")
    for i in range(len(search_result)):
        output_format(search_result[i], text, "\033[1;31m")
