#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""


**************************
文件:     auto_reply.py
 IDE：    PyCharm
创建时间： 2019/5/26 0:13
@author： skymoon
"""

from utility.sql_helper import MySQLHelper


class SentenceAnalysis(object):
    pass


class AutoReplyRobot(object):

    def __init__(self, recv_data):

        self.__helper = MySQLHelper()
        self.recv_data = recv_data

    def greeting_word_check(self):
        for word in ["您好", "你好", "Hello", "hello", "nihao"]:
            if self.recv_data.__contains__(word):
                return "主人，" + word + "!"
        return False

    def dirty_word_check(self):
        for word in ["cao", "草", "操", "妈的", "尼玛", "fuck", "shit", "bitch"]:
            if self.recv_data.__contains__(word):
                return "主人，请不要讲脏话！"
        return False

    def sensitive_word_check(self):
        for word in ["习近平", "毛泽东", "老毛", "国父", "金正恩", "极权", "集权", "泰迪"]:
            if self.recv_data.__contains__(word):
                return "主人，蕾姆不想谈论国是！"
        return False

    def incomprehensible(self):
        pass

    def __call__(self):

        greeting_response = self.greeting_word_check()
        dirtyword_response = self.dirty_word_check()
        sensitiveword_response = self.sensitive_word_check()
        if greeting_response:
            return greeting_response
        elif dirtyword_response:
            return dirtyword_response
        elif sensitiveword_response:
            return sensitiveword_response
        else:
            return "主人，您说的话蕾姆不懂哦！"
