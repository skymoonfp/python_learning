#!/usr/bin/env python3
# coding=utf-8


import turtle


def main():
    # 设置窗口信息
    turtle.title('数据驱动的动态路径绘制')
    turtle.setup(800, 600, 0, 0)

    # 设置画笔
    pen = turtle.Turtle()
    pen.color("red")
    pen.width(5)
    pen.shape("turtle")
    pen.speed(5)

    # 读取文件
    result = []
    file = open("E:/dataanalysis/python_code/从文件绘制五角星.txt", "r")
    for line in file:
        result.append(list(map(float, line.split(','))))
    print(result)

    # 动态绘制
    for i in range(len(result)):
        pen.color((result[i][3], result[i][4], result[i][5]))
        pen.fd(result[i][0])
        if result[i][1]:
            pen.rt(result[i][2])
        else:
            pen.lt(result[i][2])
    pen.goto(0, 0)


main()
