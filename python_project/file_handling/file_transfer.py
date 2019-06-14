#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""
文件预处理
***************************

"""

import pickle


def txt_to_pk(file_name: str):
    """
    将.txt文件存储的内容逐行转换成.pk文件存储的内容
    每行有多个以空格或者Tab分割开的内容时，按顺序存入list中
    :param file_name:
    :return:
    """
    index = 0
    for i in range(-1, -len(file_name) - 1, -1):
        if file_name[i] == ".":
            index = i
            break
    new_file_name = file_name[:index] + ".pk"

    with open(file_name, "r", encoding="utf-8") as old_file:
        while True:
            try:
                with open(new_file_name, "ab") as new_file:
                    file_row = old_file.readline()
                    if file_row != "":
                        pickle.dump(file_row.strip().split(), new_file)
                    else:
                        break
            except FileNotFoundError:
                with open(new_file_name, "wb") as new_file:
                    file_row = old_file.readline()
                    if file_row != "":
                        pickle.dump(file_row.strip().split(), new_file)
                    else:
                        break


if __name__ == "__main__":
    txt_to_pk(r"..\data_files\customers_info_table.txt")
