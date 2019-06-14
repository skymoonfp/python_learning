#!/usr/bin/env python3
# -*- coding:UTF-8 -*-


"""
依次输入10个学生的姓名，随机为每个学生生成语文、数学和外语的分数【生成分数介于50-100】，根据均分来判断综合评定等级
◆ 均分85分以上----综合评定A
◆ 均分70-85----综合评定B
◆ 均分70分以下----综合评定C
统计出综合评定A、B、C的数量及学生姓名

-------------------------- *** 解 *** --------------------------
1.输入：
    输入10个学生姓名
2.处理：
    （1）随机为每个学生生成语文、数学、外语的分数（50~100）
    （2）计算每个学生的平均分
    （3）根据平均分返回该学生的综合评定等级
    （4）根据综合评定等级对学生进行分类
3.输出：
    输出每个综合评定等级中的学生人数和姓名
"""

import numpy as np


def score_random():
    """
    输出相应的语文、数学、外语分数
    :return: 输出相应的语文、数学、外语分数
    """
    scores = []  # 依次记录语文、数学、外语分数
    for i in range(3):
        scores.append(np.random.randint(50, 100))
    return scores


def score_avg_calc(scores):
    """
    计算平均分
    :param scores: 输入分数数组
    :return: 返回平均分数
    """
    score_sum = 0
    for i in range(len(scores)):
        score_sum += scores[i]
    return score_sum / len(scores)


def score_rank(score_avg):
    """
    判断综合评定等级
    :param score_avg: 输入平均分数
    :return: 返回综合评定等级
    """
    if score_avg >= 85:
        return "A"
    elif score_avg >= 70:
        return "B"
    else:
        return "C"


def rank_stat(names, ranks, rank):
    """
    统计指定的综合评定等级的学生
    :param names: 输入学生名单
    :param ranks: 输入与学生名单相对应的学生综合评定等级表
    :param rank: 输入指定综合评定等级
    :return: 返回该综合评定等级的学生集合
    """
    students_of_rank = []
    for i in range(len(names)):
        if ranks[i] == rank:
            students_of_rank.append(names[i])
        else:
            pass
    return students_of_rank


if __name__ == "__main__":

    # 输入学生姓名、生成其分数并判断其综合评定等级
    names = []
    scores = []
    ranks = []

    # names = [str(n) for n in input("请输入学生姓名：").split()]   # 输入学生姓名

    for i in range(10):
        names.append(input("请输入第" + str(i + 1) + "个学生姓名："))  # 输入学生姓名
        np.random.seed()
        scores.append(score_random())  # 生成其三科分数
        ranks.append(score_rank(score_avg_calc(scores[i])))  # 判断综合评定等级
    print("\n")

    # 输出综合评定等级统计结果
    for rank in ["A", "B", "C"]:
        print("综合评定" + rank + "： 学生人数：" + str(len(rank_stat(names, ranks, rank))) + "  学生姓名：" + " ".join(
            rank_stat(names, ranks, rank)))
    print("\n")

    # 输出学生成绩
    for i in range(len(names)):
        for j in range(len(scores[i])):
            scores[i][j] = str(scores[i][j])  # 将scores数组的元素转换成str
        print(names[i] + "的三科成绩分别是：" + "  ".join(scores[i]))
