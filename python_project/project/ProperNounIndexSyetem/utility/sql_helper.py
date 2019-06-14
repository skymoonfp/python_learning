#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""


**************************
文件:     sql_helper.py
 IDE：    PyCharm
创建时间： 2019/5/25 8:16
@author： skymoon
"""

import traceback

import config
import pymysql


class SQLHelper(object):
    """Operation of SQL."""

    def __init__(self):
        """Database information."""
        pass

    def link_database(self):
        """Link to database."""
        pass

    def create_table(self, table_name, sql):
        """Create table."""
        pass

    def alter_table(self):
        """Alter table.

        Add, reduce, alter attribute of table fields.

        """
        pass

    def insert_table(self, sql, params):
        """Insert into table."""
        pass


class MySQLHelper(SQLHelper):
    """Operation of MySQL."""

    def __init__(self):
        """Database information."""
        super(MySQLHelper, self).__init__()
        self.__connect_dict = config.connect_dict

    def link_database(self):
        """Link to database."""
        db_conn = pymysql.connect(**self.__connect_dict)
        cursor = db_conn.cursor(cursor=pymysql.cursors.DictCursor)

        return db_conn, cursor

    def create_table(self, table_name, sql):
        """Create table."""
        db_conn, cursor = self.link_database()

        # 使用execute()方法执行sql ，如果表存在则删除
        cursor.execute("drop table if exists %s" % table_name)
        # 使用预处理语句创建表
        cursor.execute(sql)

        cursor.close()
        db_conn.close()

    def alter_table(self):
        """Alter table.

        Add, reduce, alter attribute of table fields.

        """
        pass

    def insert(self, sql, params=None):
        """Insert into table values."""
        db_conn, cursor = self.link_database()

        try:
            if not params:
                count = cursor.execute(sql)
            else:
                count = cursor.executemany(sql, params)
            db_conn.commit()
        except:
            # 将错误日志输入到目录文件中
            with open(r"files\database_operate_anomaly_log.txt", 'a') as file:
                traceback.print_exc(file=file)
                file.flush()
            # except FileNotFoundError:
            #     with open(r"files\database_operate_anomaly_log.txt", 'w') as file:
            #         traceback.print_exc(file=file)
            #         file.flush()
            db_conn.rollback()
            count = 0
        finally:
            cursor.close()
            db_conn.close()

        return count

    def delete(self, sql, *params):
        """Delete from table [where conditions]."""
        db_conn, cursor = self.link_database()

        try:
            cursor.execute(sql, *params)
            db_conn.commit()
        except:
            # 将错误日志输入到目录文件中
            with open(r"files\database_operate_anomaly_log.txt", 'a') as file:
                traceback.print_exc(file=file)
                file.flush()
            db_conn.rollback()
        finally:
            cursor.close()
            db_conn.close()

    def update(self, sql, *params):
        """Update from table [where conditions]."""
        db_conn, cursor = self.link_database()

        try:
            cursor.execute(sql, *params)
            db_conn.commit()
        except:
            # 将错误日志输入到目录文件中
            with open(r"..\files\database_operate_anomaly_log.txt", 'a') as file:
                traceback.print_exc(file=file)
                file.flush()
            db_conn.rollback()
        finally:
            cursor.close()
            db_conn.close()

    def fetch_one(self, sql, *params):
        """Fetch one record_row from table [where conditions]."""
        db_conn, cursor = self.link_database()
        result = dict()

        try:
            cursor.execute(sql, *params)
            result = cursor.fetchone()
        except:
            # 将错误日志输入到目录文件中
            with open(r"files\database_operate_anomaly_log.txt", 'a') as file:
                traceback.print_exc(file=file)
                file.flush()
            db_conn.rollback()
        finally:
            cursor.close()
            db_conn.close()

        return result

    def fetch_many(self, sql, *params):
        """Fetch one record_row from table [where conditions]."""
        db_conn, cursor = self.link_database()
        result = dict()

        try:
            cursor.execute(sql, *params)
            result = cursor.fetchmany()
        except:
            # 将错误日志输入到目录文件中
            with open(r"..\files\database_operate_anomaly_log.txt", 'a') as file:
                traceback.print_exc(file=file)
                file.flush()
            db_conn.rollback()
        finally:
            cursor.close()
            db_conn.close()

        return result

    def fetch_all(self, sql, *params):
        """Fetch one record_row from table [where conditions]."""
        db_conn, cursor = self.link_database()
        result = dict()

        try:
            cursor.execute(sql, *params)
            result = cursor.fetchall()
        except:
            # 将错误日志输入到目录文件中
            with open(r"..\files\database_operate_anomaly_log.txt", 'a') as file:
                traceback.print_exc(file=file)
                file.flush()
            db_conn.rollback()
        finally:
            cursor.close()
            db_conn.close()

        return result
