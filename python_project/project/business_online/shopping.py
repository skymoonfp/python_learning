#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""
购物车程序
————————————————————————————————
1.用户输入工资
2.显示可购商品清单
3.用户可以不断购买商品，直到钱不够为止
4.退出时格式化打印用户已购商品清单和剩余金额
"""

# 输入工资
total_money = float(input("您总共有多少钱？\n"))

# 打开商品清单文件
numbers_of_goods = []
names_of_goods = []
prices_of_goods = []
shopping_goods_list = open(r"..\..\data_files\shopping_goods_list.txt", "r")
shopping_goods_list.readline()
shopping_goods_list.readline()  # 跳过前两行
line = shopping_goods_list.readline()
while line[0] != "=":
    line_list = line.strip().split("\t")
    numbers_of_goods.append(line_list[0])
    names_of_goods.append(line_list[1])
    prices_of_goods.append(float(line_list[2]))
    line = shopping_goods_list.readline()
shopping_goods_list.seek(0)
total_goods_list = shopping_goods_list.read()

shopping_cart = []  # 累计购物信息
shopping_cart_element = []  # 当前购物信息
money_spent = 0  # 截止目前已经花了多少钱
count = 0  # 成功购物次数
number = 0  # 成功购买的商品序号
goods_temp = []  # 统计不重复商品的信息，包括购买件数

# 循环购物过程
go_on_shopping = True
while go_on_shopping:

    # 判断余额
    if (total_money - money_spent) < min([i for i in prices_of_goods]):
        print("您的余额已经不足！")
        break
    else:
        pass

    # 打印可购商品清单
    print(total_goods_list)

    # 请用户选择商品
    goods_buying = input("请问您需要购买什么东西（请输入商品编号或者商品名）？\n")
    if goods_buying in numbers_of_goods:
        number = numbers_of_goods.index(goods_buying)
    elif goods_buying in names_of_goods:
        number = names_of_goods.index(goods_buying)
    else:
        print("没有您所需要的商品！请重新输入！\n")
        continue

    # 判断余额是否买得起
    if (total_money - money_spent) < prices_of_goods[number]:
        print("您的余额已经买不起这件商品了！", end="")
        while True:
            choice = input("请问是否还需要购买其他商品（y/n）？")
            if choice == "y":
                go_on_shopping = True
                break
            elif choice == "n":
                go_on_shopping = False
                break
            else:
                print("输入有误！")
                continue
        continue
    else:
        pass

    # 购买成功时
    for i in range(len(shopping_cart_element)):
        shopping_cart_element.pop()
    shopping_cart_element.append(numbers_of_goods[number])
    shopping_cart_element.append(names_of_goods[number])
    shopping_cart_element.append(prices_of_goods[number])
    shopping_cart.append(shopping_cart_element.copy())
    count += 1
    money_spent += float(shopping_cart[-1][2])
    print("您还剩余\033[1;31m %.2f \033[0m元，" % (total_money - money_spent), end="")
    while True:
        choice = input("请问是否继续购物（y/n）？")
        if choice == "y":
            go_on_shopping = True
            break
        elif choice == "n":
            go_on_shopping = False
            break
        else:
            print("输入有误！")
            continue
    continue

# 打印购物信息
print(
    "\033[22;36m 您总计购买了\033[1;34m %d \033[22;36m件商品，总计花费\033[1;30;47m %.2f \033[22;36m元，剩余\033[1;31m %.2f \033[22;36m元，购物清单如下：" % (
    count, money_spent, total_money - money_spent))
for i in range(len(shopping_cart)):
    shopping_cart[i].append("0")  # 添加计数位
    shopping_cart[i][3] = int(shopping_cart[i][3])
    if shopping_cart[i][0] not in [goods_temp[i][0] for i in range(len(goods_temp))]:
        goods_temp.append(shopping_cart[i])
        goods_temp[-1][3] += 1
    else:
        goods_temp[[goods_temp[i][0] for i in range(len(goods_temp))].index(shopping_cart[i][0])][3] += 1
for i in range(len(goods_temp)):
    print("\033[22;33m %10s%2d件，花费%10.2f元 \033[0m" % (
    goods_temp[i][1], goods_temp[i][3], goods_temp[i][2] * goods_temp[i][3]))

shopping_goods_list.close()
