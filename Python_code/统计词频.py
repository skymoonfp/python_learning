#!/usr/bin/env python3
# -*- coding:utf-8 -*-


import turtle

##全局变量##
# 词频排列显示个数
count = 12

# 单词频率数组-作为y轴数据
data = []

# 单词数组-作为x轴数据
words = []

# y轴显示放大倍数-可以根据词频数量进行调节
yScale = 20

# x轴显示放大倍数-可以根据count数量进行调节
xScale = 60


####################  Turtle Start  ####################
# 从点(x1,y1)到(x2,y2)绘制线段
def drawLine(t, x1, y1, x2, y2):
    t.penup()
    t.goto(x1, y1)
    t.pendown()
    t.goto(x2, y2)


# 在坐标(x,y)处写文字
def drawText(t, x, y, text):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.write(text)


def drawGraph(t):
    # 移动画笔到左下角
    t.penup()
    t.goto(-400, -220)
    t.pendown()

    # 绘制x/y轴线
    drawLine(t, -400, -220, 400, -220)
    drawLine(t, -400, -220, -400, 220)

    # x轴：坐标及描述
    for x in range(count):
        x += 1  # 向右移一位，为了不画在原点上
        t.color("red")
        drawText(t, x * xScale - 4 - 400, -20 - 220, (words[x - 1]))
        drawText(t, x * xScale - 4 - 400, data[x - 1] * yScale + 10 - 220, data[x - 1])

    drawBar(t)


# 绘制一个柱体
def drawRectangle(t, x, y):
    x = x * xScale
    y = y * yScale  # 放大倍数显示
    drawLine(t, x - 20 - 400, 0 - 220, x - 20 - 400, y - 220)
    drawLine(t, x - 20 - 400, y - 220, x + 20 - 400, y - 220)
    drawLine(t, x + 20 - 400, y - 220, x + 20 - 400, 0 - 220)
    drawLine(t, x + 20 - 400, 0 - 220, x - 20 - 400, 0 - 220)


# 绘制多个柱体
def drawBar(t):
    for i in range(count):
        if i % 3 == 0:  # 改变柱体颜色
            t.color("orange")
            drawRectangle(t, i + 1, data[i])
        elif i % 3 == 1:
            t.color("green")
            drawRectangle(t, i + 1, data[i])
        else:
            t.color("blue")
            drawRectangle(t, i + 1, data[i])


####################  Turtle End  ####################


# 读文件的每一行并计算词频的数量
def processLine(line, wordCounts):
    # 用空格替换标点符号
    line = replacePunctuation(line)
    # 从每一行获取每个词
    words = line.split()
    for word in words:
        if word in wordCounts:
            wordCounts[word] += 1
        else:
            wordCounts[word] = 1


# 用空格替换文本中的标点符号
def replacePunctuation(line):
    for ch in line:
        if ch in "~@#$%^&*()_-+=<>?/,.:;{}[]|\'""":
            line = line.replace(ch, "")
        return line


def main():
    # 用户输入一个文件名
    filename = input("enter a filename:\n").strip()
    infile = open(filename, "r")

    # 建立用于计算词频的空字典
    wordCounts = {}
    for line in infile:
        processLine(line.lower(), wordCounts)

    # 从字典中获取数据对
    pairs = list(wordCounts.items())

    # 列表中的数据对交换位置，数据对排序
    items = [[x, y] for (y, x) in pairs]
    items.sort()

    # 打印出单词词频统计结果
    for i in range(len(items) - 1, len(items) - count - 1, -1):
        # print(items[i][1] + "\t" + str(items[i][0]))
        print("%15s\t%10d" % (items[i][1], int(items[i][0])))
        data.append(items[i][0])
        words.append(items[i][1])

    # 根据词频结果绘制柱状图
    turtle.title('词频结果柱状图')
    turtle.setup(1000, 600, 0, 0)
    t = turtle.Turtle()
    t.hideturtle()
    t.width(3)
    drawGraph(t)
    turtle.mainloop()


main()
