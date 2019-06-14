#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""


**************************
文件:     聚类
 IDE：    PyCharm
创建时间： 2019/6/15 14:30
@author： skymoon
"""

from pylab import *
from scipy.cluster.vq import *


def clustering(data_tuple, centre_count):
    """

    :param data_tuple: 处理的数据
    :param centre_count: 生成的聚类中心数
    :return: 聚类中心值，处理的数据中每一条属于哪个聚类中心
    """
    data = vstack(data_tuple)
    centroids, _ = kmeans(data, centre_count)
    result, _ = vq(data, centroids)
    return centroids, result


if __name__ == "__main__":
    score = ([88.0, 74.0, 96.0, 85.0],
             [92.0, 99.0, 95.0, 94.0],
             [91.0, 87.0, 99.0, 95.0],
             [78.0, 99.0, 97.0, 81.0],
             [88.0, 78.0, 98.0, 84.0],
             [100.0, 95.0, 100.0, 92.0])
    grade_count = 2
    grade_sample, student_grade = clustering(score, grade_count)
    print(grade_sample)
    print(student_grade)
