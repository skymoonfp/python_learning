#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""

"""


# 由dict_value查找dict_key，返回全部key列表

# 错误类型：无错误，找不到时返回空列表
def get_key(dictation: dict, value):
    return [k for k, v in dictation.items() if v == value]


# 错误类型：要查找的value不存在于字典中时，ValueError（即要查找的元素不存在于list中，查找该元素在list中的index位置时的错误类型）
def get_key1(dictation: dict, value):  # 错误类型：ValueError
    list(dictation.keys())[list(dictation.values()).index(value)]


# 反转，value值有重时，返回的key为具有该值的item中随机某个的key
# 错误类型：字典中任意value为可变对象时，TypeError（即dict中的key为可变对象时的错误类型）
def get_key2(dictation: dict, value):  #
    new_dict = {v: k for k, v in dictation.items()}
    new_dict[value]
