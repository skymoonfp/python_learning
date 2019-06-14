#!/usr/bin/env python3
# -*- coding:utf-8 -*-


def element_index_of_list(list_name: list, element: str):
    """
    查找列表中指定元素出现在列表中的所有位置信息
    :param list_name: 要查找的列表
    :param element: 要查找的元素
    :return: 位置信息的列表（无时返回空值；有时返回从0开始的位置值）
    """
    element_indexes = []
    new_start_point = 0  # 初始新起点为0

    # 不存在于列表中
    if element not in list_name:
        return element_indexes
    # 存在于列表中
    else:
        times = list_name.count(element)
        for i in range(times):
            element_index = list_name.index(element, new_start_point)
            element_indexes.append(element_index)
            new_start_point = element_index + 1
            # index查询从new_start_point开始，element第一次出现时处在整个列表中的位置
        return element_indexes


if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5, 6, 7, 2, 3, 3, 4, 5, 6, 3, 4, 5, 4]
    number = 4
    indexes = [str(i) for i in element_index_of_list(numbers, number)]
    print(str(number) + "依次出现于numbers的下列位置（初始位置为0）：" + "、".join(indexes))
