#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""
文件预处理
"""


# 表格格式化存储的文件内容进行预处理（返回全部内容的二维列表）
def table_file_pretreatment_list2d(file_name: str):
    """
    表格格式化存储的文件内容进行预处理（返回全部内容的二维列表）
    ————————————————————————————————
    文件格式为：
    1.表头占一行
    2.字段名占一行（各字段之间用空格隔开）
    3.每条记录占一行
    4.任意字段和记录均无空值
    :param file_name: 文件名
    :return: 二维列表file_data；file_data[row][col]
    """
    file_data_list2d = []
    with open(file_name, "r", encoding="utf-8") as file:
        file_data_row = file.readline()
        while file_data_row:
            row_data = file_data_row.strip().split()
            file_data_list2d.append(row_data)
            file_data_row = file.readline()
        else:
            return file_data_list2d


# 将二维矩阵形式的二维list（list下的每个元素list中的元素个数相同，即二维矩阵）按给定关键字位置转换成dict
def list2d_into_dict(list2d: list, key_index: list):
    """
    将二维矩阵形式的二维list（list下的每个元素list中的元素个数相同，即二维矩阵）按给定关键字位置转换成dict
    :param list2d: 给定二维list
    :param key_index: 给定关键字位置
    :return: 生成的dict
    """
    keys = []  # 存放keys的所有记录
    keys_tuple = []  # 存放每条keys记录中的所有keys字段值
    values = []  # 存放values的所有记录
    dict_return = {}  # 存放返回的dict
    # 分离key和value
    if key_index:
        for list2d_row in list2d:
            keys.append(list2d_row[0])
            del list2d_row[0]
            values.append(list2d_row)
    elif len(key_index) == 1:
        for list2d_row in list2d:
            keys.append(list2d_row[key_index[0]])
            del list2d_row[key_index[0]]
            values.append(list2d_row)
    else:
        for list2d_row in list2d:
            for col in key_index:
                keys_tuple.append(list2d_row[col])
                del list2d_row[col]
            keys_tuple = tuple(keys_tuple)
            keys.append(keys_tuple)
            values.append(list2d_row)
    # 组装字典
    for i in range(len(keys)):
        dict_return[keys[i]] = values[i]
    return dict_return


# 将二维矩阵形式的二维list（list下的每个元素list中的元素个数相同，即二维矩阵）按给定表头信息、是否有字段名行、以及给定key字段名转换成dict
def table_file_pretreatment_dict_2(file_data_list2d: list, table_file_title_flag: int = 0, key_flag: int = 0,
                                   *key: str):
    """
    将二维矩阵形式的二维list（list下的每个元素list中的元素个数相同，即二维矩阵）按给定表头信息、是否有字段名行、以及给定key字段名转换成dict
    :param file_data_list2d: 要处理文件的二维list
    :param table_file_title_flag: 表头判断信息：默认0为无表头；具体数字为表头所占行数
    :param key_flag: 判断字段名信息：默认0为无字段名行；1为有字段名
    :param key: 作为字典key的字段名，输入为空时默认第一个字段为字典key
    :return: 生成的字典
    """
    file_data_dict = {}  # 要返回的dict
    key_index = []  # 输入的key字段名在字段名行中的索引位置
    if not table_file_title_flag and not key and not key_flag:  # 无表头、无key字段名（默认第1个字段为key）、无字段名行
        file_data_dict = list2d_into_dict(file_data_list2d)
    elif not key and not key_flag:  # 仅有表头
        for i in range(table_file_title_flag):
            del file_data_list2d[i]
            file_data_dict = list2d_into_dict(file_data_list2d)
    elif not table_file_title_flag and not key_flag:  # 仅有key字段名
        print("该文件没有字段名行！无法确认您输入的字段名是哪一字段的名！\n")
        return
    elif not table_file_title_flag and not key:  # 仅有字段名行
        del file_data_list2d[0]
        file_data_dict = list2d_into_dict(file_data_list2d)
    elif not table_file_title_flag:  # 有key字段名和字段名行
        for i in range(len(key)):
            key_index.append(file_data_list2d[0].index(key[i]))
        del file_data_list2d[0]
        file_data_dict = list2d_into_dict(file_data_list2d, key_index)
    elif not key_flag:  # 有表头和key字段名
        print("该文件没有字段名行！无法确认您输入的字段名是哪一字段的名！\n")
        return
    elif not key:  # 有表头和字段名行
        for i in range(table_file_title_flag + 1):
            del file_data_list2d[i]
            file_data_dict = list2d_into_dict(file_data_list2d)
    else:  # 有表头、字段名行、key字段名
        for i in range(table_file_title_flag):
            del file_data_list2d[i]
        for i in range(len(key)):
            key_index.append(file_data_list2d[0].index(key[i]))
        del file_data_list2d[0]
        file_data_dict = list2d_into_dict(file_data_list2d, key_index)

    return file_data_dict


# 表格格式化存储的文件内容进行预处理（返回不包含表头和字段名称的信息的字典）
def table_file_pretreatment_dict(file_name: str, table_file_title_flag: int = 0, key_flag: int = 0, *key: str):
    """
    :param file_name: 要处理的文件
    :param table_file_title_flag: 表头判断信息：默认0为无表头；具体数字为表头所占行数
    :param key_flag: 判断字段名信息：默认0为无字段名行；1为有字段名
    :param key: 作为字典key的字段名，输入为空时默认第一个字段为字典key
    :return: 生成的字典
    """
    file_data_list2d = table_file_pretreatment_list2d(file_name)
    file_data_dict = table_file_pretreatment_dict_2(file_data_list2d, table_file_title_flag, key_flag, *key)
    return file_data_dict


if __name__ == "__main__":
    print(table_file_pretreatment_list2d(r"..\..\txt_files\customers_info_table.txt"))
