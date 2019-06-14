#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""
验证码生成
"""

import random


def random_code(length: int):
    """
    用数字、小写字母生成指定长度的随机字符串
    :param length: 指定长度
    :return: 返回字符串
    """
    numbers = [chr(i) for i in range(48, 58)]
    chars = [chr(i) for i in range(97, 122)]
    char_list = numbers + chars
    code = "".join(random.sample(char_list, length))
    return code


if __name__ == "__main__":
    print(random_code(8))
