#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""
模块学习
"""

from project import computation

print(computation.add(2, 3))

from otherwise import hello

print(__name__)

print(__file__)

print(__doc__)

from project import readlinex

for item in readlinex.readlinex("shopping_goods_list.txt"):
    print(item, end="")

# 该种调用方式，必须先配置learning下__init__文件
import project

for item in project.readlinex.readlinex("shopping_goods_list.txt"):
    print(item, end="")
print("")
print(project.computation.add(2, 3))

print(dir())
print(vars())

import importlib as imp

imp.reload(hello)
imp.reload(hello)
imp.reload(hello)

name = ["张三", "李四", "王五"]
print(n for n in name)
print("")
print([n for n in name])
print("")
for n in name:
    print(n)
print("")
print(enumerate(name))
print("")
print([enumerate(name)])
print("")
print({enumerate(name)})
print("")
print((enumerate(name)))
print("")
for n in enumerate(name):
    print(n)
print("")
for n in enumerate(name, 1):
    print(n)
print("")
for n in enumerate(name):
    print(n[0], n[1])
print("")
for n in enumerate(name, 1):
    print(n[0], n[1])
print("")
a = enumerate(name, 1)
print(a)
print(type(a))
print("")

name = ["张三", "李四", "王五"]
b = {}
for n in enumerate(name, 1):
    b[n[0]] = n[1]
print(b)
print("")

for i in b:
    print(i)
print("")

print(b.items())
print("")

for i in b.items():
    print(i)
print("")

# 转换成数组
c = []
for n in enumerate(name, 1):
    c.append(n)
print(c)
print("")

d = dict(c)
print(d)
print("")

e = list(enumerate(name, 2))
print(e)
print("")

f = dict(enumerate(name, 2))
print(f)

格式化
s = "我是来自\033[1;31m{0}\033[0m的一名{{\033[1;32m{1}\033[0m系}}\033[1;33m{2}\033[0m！"
s1 = "我是来自\033[1;31m{}\033[0m的一名{{\033[1;32m{}\033[0m系}}\033[1;33m{}\033[0m！"
print(s)
print(s1.format("天津大学", "数学", "学生"))
print(s.format("天津大学", "数学", "学生"))

s = "我是来自{university}的一名{dept}系{post}！"
print(s.format(dept="数学", post="学生", university="天津大学"))
c0 = {"dept": "数学", "post": "老师", "university": "天津大学"}
print(s.format(**c0))
c1 = {"dept": ["数学", "中文"], "post": ["学生", "老师"], "university": ["南开大学", "天津大学"]}
# s1 = "我是来自{university[i]}的一名{dept[i]}系{post[i]}！"
for i in range(2):
    print(s.format(**c1))
#     print(s1.format(**c1))

coord = [3, 5]
print('X: {coor[0]};  Y: {coor[1]}'.format(coor=coord))

member_info = {"001": ["张三", "数学", "老师", "南开大学"], "002": ["李四", "中文", "学生", "天津大学"]}
s = "{002[0]}是来自{002[3]}的一名{002[1]}系{002[2]}！"
print(s.format(member_info))

s = "{name}是来自{university}的一名{dept}系{post}！"
c1 = [["张三", "李四"], ["数学", "中文"], ["学生", "老师"], ["南开大学", "天津大学"]]
c2 = [["张三", "数学", "老师", "南开大学"], ["李四", "中文", "学生", "天津大学"]]
c3 = zip(c1[0], c1[1], c1[2], c1[3])
for i in c2:
    print(s.format(name=i[0], dept=i[1], post=i[2], university=i[3]))
for i in c3:
    print(s.format(name=i[0], dept=i[1], post=i[2], university=i[3]))
s1 = "{}是来自{}的一名{}系{}！"
for i in c2:
    print(s1.format(i[0], i[3], i[1], i[2]))

# 以字符串形式导入模块和函数
names = input("请输入要导入的模块和函数名：\n").split()
print(getattr(__import__(names[0]), names[1])(2, 4))
# computation mul


help("format")
help("FORMATTING")

MD5加密
import hashlib

hashlib.md5().update("password".encode("utf-8"))
s = hashlib.md5().hexdigest()
q = hashlib.md5().digest()
print(s)
print(type(s))
print(q)
print(type(q))
t = q.decode("uft-8")
print(t)
print(type(t))
a = hex(int(s, 16))
b = bin(int(s, 16))
c = eval("0x" + s)
d = int(s, 16)
print(a)
print(b)
print(c)
print(d)
print(type(a))
print(type(b))
print(type(c))
print(type(d))
# print(a.decode("utf-8"))
print(len(s))
print(type(len(s) / 2))
s1 = []
for i in range(int(len(s) / 2)):
    u = s[2 * i] + s[2 * i + 1]
    print(u)
    u1 = "\\x" + u
    print(u1)
    s1.append(u1)
print(s1)
s11 = "".join(s1)
print(s11)
s2 = b"s11".decode("utf-8")
print(s2)
# s3 = b"\xd4\x1d\x8c\xd9\x8f\x00\xb2\x04\xe9\x80\x09\x98\xec\xf8\x42\x7e".decode("utf-8")
s4 = b"\xd4\x1d".decode("utf-8")
s5 = b"\x8c\xd9".decode("utf-8")
s6 = b"\x8f\x00".decode("utf-8")
s7 = b"\xb2\x04".decode("utf-8")
s8 = b"\xe9\x80".decode("utf-8")
s9 = b"\x09\x98".decode("utf-8")
s10 = b"\xec\xf8".decode("utf-8")
s11 = b"\x42\x7e".decode("utf-8")
print(s4, s5, s6, s7, s8, s9, s10, s11)

fang = "fang".encode("utf-8")
print(fang)
print(b"fang".decode("utf-8"))
print(b"0xe3".decode("utf-8"))
print("方".encode("utf-8"))
print(b"\xe6\x96\xb9".decode("utf-8"))
import binascii

s = 'test123456test'
str_16 = binascii.b2a_hex(s.encode('utf-8'))  # 字符串转16进制
print(str_16)


def baseN(num, b):
    return ((num == 0) and "0") or \
           (baseN(num // b, b).lstrip("0") + "0123456789abcdefghijklmnopqrstuvwxyz"[num % b])


num_10 = int(str_16, 16)  # 16进制转10进制
print(num_10)

str_32 = baseN(num_10, 32)  # 10进制转32进制
print(str_32)

num_10_2 = int(str_32, 32)  # 32进制转10进制
print(num_10_2)

num_16 = hex(num_10)  # 10进制转16进制数
print(num_16)

ss = str_16.decode('hex')  # 16进制串转字符串
print(ss)

# IP地址匹配
import re

ipbook = "00044931.22.22.11_111d.df5.fd.d223.211.222.11111.44f.33.22.33aff333.32.22.__33931..22.22.11931.22333.22.11"
IP = re.findall("\d{1,3}(?:\.\d{1,3}){3}", ipbook)
IP2 = re.findall("[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}", ipbook)
IP3 = re.findall("(?:\d{1,3}\.){3}\d{1,3}", ipbook)
IP4 = re.findall("\d+(?:\.+\d+){1,3}", ipbook)
print(IP)
print(IP2)
print(IP3)
print(IP4)

import mytime

print(mytime.time())  # 时间戳
print(mytime.gmtime())  # 结构化
print(mytime.localtime())  # 结构化
print(mytime.strftime("%Y%m%d  %H%M%S"))  # 格式化
print(mytime.strftime("%Y-%m-%d  %H:%M:%S"))  # 格式化
print("")
print(mytime.strptime("2019-05-16  15:06:33", "%Y-%m-%d  %H:%M:%S"))  # 格式化转成结构化
print(mytime.mktime(mytime.strptime("2019-05-16", "%Y-%m-%d")))  # 结构化转成时间戳
print(mytime.mktime(mytime.localtime()))  # 结构化转成时间戳
