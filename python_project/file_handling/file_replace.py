#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""
替换文本内容
————————————————————————————————
1.命令格式为：python  ./file_replace.py  old_text  new_text  file_name  [--bak]
2.如果命令中没有 --bak，则直接替换原文件
3.如果命令中有 --bak，则创建一个后缀为.bak的原文件副本，并且替换原文件
"""

import os
import sys

if len(sys.argv) < 4:
    print("usage: ./file_replace.py  old_text  new_text  file_name  [--bak]")
else:
    old_text = sys.argv[1]
    new_text = sys.argv[2]
    file_name = sys.argv[3]

    old_file = open(file_name, "r+")
    new_file = open("%s2.bak" % file_name, "w+")  # 创建文件名为"原文件名"+"2.bak"的备份文件，存放替换文本
    while True:
        line = old_file.readline()
        if line == "":
            break
        else:
            new_file.write(line.replace(old_text, new_text))
    old_file.close()
    new_file.close()

    os.rename(file_name, "%s.bak" % file_name)  # 将原文件名修改为"原文件名"+".bak"，也即，将原文本存放在文件名为"原文件名"+".bak"的文件中
    os.rename("%s2.bak" % file_name, file_name)  # 将存放替换文本的文件名修改为原文件名
    if "--bak" in sys.argv:
        pass  # 要求备份时
    else:
        os.remove("%s.bak" % file_name)  # 不要求备份时，删除存放原文本的文件
