#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""


**************************
文件:     users_log.py
 IDE：    PyCharm
创建时间： 2019/5/25 8:09
@author： skymoon
"""

from utility.sql_helper import MySQLHelper


class UsersLog(object):

    def __init__(self):
        self.__helper = MySQLHelper()

    def check_validate(self, username, password):
        """Check input is or not in Database.

        If is in, return (username, password);

        if not in, return None.

        """
        sql = "select username, password from users_log_table where username = %s and password = %s"
        params = (username, password)
        return self.__helper.fetch_one(sql, params)

    def registration(self, username, password):
        """Add user's register information to Database.

        If Database doesn't have the relative table, create it first.

        """
        sql = "insert into users_log_table(username, password) values(%s, %s)"
        params = [(username, password)]

        # 判断表是否存在
        tables_list = self.__helper.fetch_all("show tables")
        tables = []
        for table in tables_list:
            tables.append(table["Tables_in_pymysql"])
        if "users_log_table" not in tables:
            sql_1 = """create table users_log_table(
                           id int not null primary key auto_increment,
                           username varchar(20) not null,
                           password varchar(30) not null default "666666",
                           e_mail varchar(30),
                           ID_number varchar(18)
                           )
                    """
            self.__helper.create_table("users_log_table", sql_1)
            self.__helper.insert(sql, params)
            return True
        else:
            sql_2 = "select count(*) as count from users_log_table where username = '%s'" % (username)
            data_dict = self.__helper.fetch_one(sql_2)
            if data_dict["count"]:
                return False  # 该用户名已经存在
            else:
                self.__helper.insert(sql, params)
                return True
