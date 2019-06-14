#!/usr/bin/env python3
# -*- coding:UTF-8 -*-


"""
扑克牌游戏（不包含大小王）
"""

import random


def get_poker(number=1):
    """
    生成一套扑克牌（不包含大小王）
    :param number: 包含的扑克牌副数，默认为1
    :return: 返回该套扑克牌的list
    """
    one_poker = []
    poker_type = ["♠", "♡", "♢", "♣"]
    poker_number = ["3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A", "2"]
    for num in range(number):
        for i in poker_number:
            for j in poker_type:
                one_poker.append(j + i)
    return one_poker


def deal_poker(poker: list, people: int = 4):
    """
    从洗好的牌中依次给玩家发牌
    :param poker: 一套准备的牌
    :param people: 玩家人数，默认为4
    :return:
    """
    deal_list = []
    # 洗牌
    random.shuffle(poker)
    # 给玩家发牌
    for i in range(people):
        temp_deal = []
        for j in range(len(poker)):
            if j % people == i:
                temp_deal.append(poker[j])
        # 把该人的牌加入deal_list
        deal_list.append(temp_deal)
    return deal_list


# 测试
if __name__ == "__main__":
    my_poker = get_poker(1)
    deal_poker_list = deal_poker(my_poker, 4)
    for i in range(len(deal_poker_list)):
        print("第" + str(i + 1) + "家的牌是：", deal_poker_list[i])
