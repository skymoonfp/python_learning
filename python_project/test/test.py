#!/usr/bin/env python3
# -*- coding:UTF-8 -*-

print("3")

# # 查看当前文件路径
# import os
# os.system("cd")
#
# # 显示当前文件夹信息
# import os
# os.system("dir")
#
# # 保存当前文件路径
# import os
# path = os.popen("cd").read()
# print(path)
#
# # 查看模块详细信息
# help("os")
#
# # 查看模块内方法
# print(dir(os))


# # 文件读写方式
# encode_test = open("E:\\DataAnalysis\\python_project\\encode_test.txt", "w")
# encode_test.write("柏拉12ab、_%图、苏格拉底、赫拉克利特\n")
# encode_test.write("亚里士多德、笛卡尔")
# encode_test.close()
#
# encode_test = open("encode_test.txt", "r")
# for line in encode_test.readlines():
#     list01 = line.strip().split("、")
#     # for element in list01:
#     #     print(element)
#     for i in range(len(list01)):
#         print(list01[i])
# encode_test.close()
#
# # 文件属性和方法
# help(encode_test)
# encode_test = open("encode_test.txt", "w")
# encode_test = open("encode_test.txt", "a")
# encode_test = open("encode_test.txt", "r")
# encode_test.close()
# encode_test.mode
# encode_test.name
# encode_test.read(25)
# encode_test.readline(25)
# encode_test.readlines(25)
# encode_test.next()   # 过气
# next(encode_test)
# encode_test.tell()
# encode_test.seek(4)
# encode_test.write("李斯")
# encode_test.truncate(12)
# # 始终从头开始截取；
# # "w"（在清空之后进行截取，结果始终为空），"a"（在原文本上进行截取）；
# # 截取数为字节数；
# # txt文本用gbk编码，每个汉字占两个字节，每个数字或英文字母占一个字节，每个全角标点占两个字节，每个半角标点占一个字节
# print(encode_test)
# help(encode_test.readlines)


# list
list01 = ["ad", "分配", "1", "7**"]
help(list01)
list01.insert(2, "a+b=")
list01.index("a")
help(list)
# -----------同步变化---------------
list01 = ["ad", "分配", "1", "7**"]
list02 = list01
list01[0] = "AD"
print(list01, list02)
# -----------相互独立---------------
str01 = "abd"
str02 = str01
str01 = str01[1:]
print(str01, str02)
# -----------相互独立---------------
list01 = ["ad", "分配", "1", "7**"]
list02 = list01
list01 = list01[1:]
print(list01, list02)
# -----------同步变化---------------
list01 = ["ad", "分配", "1", "7**"]
list02 = list01
list01.insert(2, "a+b=")
print(list01, list02)
# -----------同步变化---------------
list01 = ["ad", "分配", "1", "7**"]
list02 = list01
list01.append("a+b=c")
print(list01, list02)
# ---------------------------------
list01 = ["1", ["2", "3"], ["2", "3"]]
list02 = list01
list03 = list01.copy()
list04 = []
for i in range(3):
    list04.append(list01[i].copy())
print(list01, list02, list03, list04)
list01.insert(1, ["2"])  # 1
list01.pop()  # 2
list01.replace(["2", "3"], ["4"])  # 3
list01[1] = ["4"]  # 4
list01[1].append("5")  # 5
# ---------------------------------
list01 = [["1"], ["2", "3"], ["2", "3"]]
list04 = []
list05 = []
for i in range(3):
    list04.append(list01[i].copy())
for i in range(len(list04)):
    if list04[i] not in list05:
        list05.append(list04[i])
    else:
        pass
print(list01)
print(list04)
print(list05)
# ---------------------------------
list01 = [["1"], ["2", "3"], ["2", "3"]]
list04 = []
list05 = []
for i in range(3):
    list04.append(list01[i].copy())
for i in range(len(list04)):
    if list04[i] not in list05:
        list05.append(list04[i])
    else:
        pass
list01 = [["1", "2"], ["2", "3"], ["2", "3"]]
print(list01)
print(list04)
print(list05)
# ---------------------------------
list01 = [["1"], ["2", "3"], ["2", "3"]]
list04 = []
list05 = []
for i in range(3):
    list04.append(list01[i].copy())
for i in range(len(list04)):
    if list04[i] not in list05:
        list05.append(list04[i])
    else:
        pass
list01 = [["1"], ["2", "3", "4"], ["2", "3"]]
print(list01)
print(list04)
print(list05)
# ---------------------------------
list01 = [["1"], ["2", "3"], ["2", "3"]]
list04 = []
list05 = []
for i in range(3):
    list04.append(list01[i].copy())
for i in range(len(list04)):
    if list04[i] not in list05:
        list05.append(list04[i])
    else:
        pass
list01[1] = ["2", "3", "4"]
print(list01)
print(list04)
print(list05)
# ---------------------------------
list01 = []
list01.append(["1"])
a = []
a.append("2")
a.append("3")
list01.append(a.copy())
a.pop()
a.pop()
a.append("2")
a.append("3")
list01.append(a.copy())
list05 = []
for i in range(len(list01)):
    if list01[i] not in list05:
        list05.append(list01[i])
    else:
        pass
print(list01)
print(list05)
# ---------------------------------
list01 = []
list01.append(["1"])
a = []
a.append("2")
a.append("3")
list01.append(a.copy())
a.pop()
a.pop()
a.append("2")
a.append("3")
list01.append(a.copy())
list05 = []
for i in range(len(list01)):
    list01[i].append("0")
    if list01[i] not in list05:
        list05.append(list01[i])
    else:
        pass
print(list01)
print(list05)
# ---------------------------------
list01 = []
list01.append(["1"])
a = []
a.append("2")
a.append("3")
list01.append(a.copy())
a.pop()
a.pop()
a.append("2")
a.append("3")
list01.append(a.copy())
list05 = []
for i in range(len(list01)):
    list01[i].append("0")
    if list01[i] not in list05:
        list05.append(list01[i].copy())
    else:
        pass
print(list01)
print(list05)


def back():
    a = input("input")
    b = input("input")
    return a, b


print(back())
