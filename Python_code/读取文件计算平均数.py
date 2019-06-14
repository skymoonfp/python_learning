#!/usr/bin/env python3
# -*- coding:utf-8 -*-


def main():
    fileName = input("请输入数据所在的文件名：")
    infile = open(fileName, 'r')
    sum = 0.0
    count = 0
    line = infile.readline()
    while line != "":
        for xStr in line.split(" "):
            sum = sum + eval(xStr)
            count = count + 1
        line = infile.readline()
    print("\n该文件数据的平均数是：", sum / count)


main()
