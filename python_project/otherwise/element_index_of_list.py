#!/usr/bin/env python3
# -*- coding:utf-8 -*-


def element_index_of_list(list_name: list, element: str):
    """
    查找列表中指定元素出现在列表中的所有位置信息
    :param list_name: 要查找的列表
    :param element: 要查找的元素
    :return: 位置信息的列表
    """
    element_index = []
    new_start_point = 0  # 初始新起点为0

    # 不存在于列表中
    if element not in list_name:
        return element_index
    # 存在于列表中
    else:
        times = list_name.count(element)
        for i in range(times):
            new_list = list_name[new_start_point:]  # 新表new_list：以新起点new_start_point为第一个元素
            new_start_point += new_list.index(element) + 1  # 新起点：以上一个新起点+上一个新表中element所处的位置（从0开始）+1
            element_index.append(new_start_point - 1)
        return element_index


if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5, 6, 7, 2, 3, 3, 4, 5, 6, 3, 4, 5, 4]
    number = 3
    indexes = [str(i) for i in element_index_of_list(numbers, number)]
    print(str(number) + "依次出现于numbers的下列位置（初始位置为0）：" + "、".join(indexes))
