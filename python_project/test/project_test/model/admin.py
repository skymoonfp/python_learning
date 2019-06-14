#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""


**************************
文件:     admin.py
 IDE：    PyCharm
创建时间： 2019/5/24 19:06
@author： skymoon
"""

from utility.sql_helper import MySQLHelper


class Admin(object):

    def __init__(self):
        self.__helper = MySQLHelper()

    def get_one(self, id):
        sql = "select * from admin where id = %s"
        params = (id,)
        return self.__helper.get_one(sql, params)

    def check_validate(self, username, password):
        sql = "select * from admin where username = %s and password = %s"
        params = (username, password)
        return self.__helper.get_one(sql, params)
