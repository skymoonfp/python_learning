#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""


**************************
文件:     sql_helper.py
 IDE：    PyCharm
创建时间： 2019/5/24 17:47
@author： skymoon
"""

import config
import pymysql


class MySQLHelper(object):

    def __init__(self):
        self.__conn_dict = config.conn_dict

    def get_dict(self, sql, params):
        conn = pymysql.connect(**self.__conn_dict)
        cur = conn.cursor(cursorclass=pymysql.cursors.DictCursor)

        count = cur.executemany(sql, params)
        data = cur.fetchall()
        conn.commit()

        cur.close()
        conn.close()
        return count, data

    def get_one(self, sql, params):
        conn = pymysql.connect(host="127.0.0.1", user="root", passwd="", db="pymysql")
        cur = conn.cursor(cursor=pymysql.cursors.DictCursor)

        count = cur.execute(sql, params)
        data = cur.fetchone()
        conn.commit()

        cur.close()
        conn.close()
        return count, data
