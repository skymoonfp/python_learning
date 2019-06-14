#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""

"""

# import MySQLdb
import pymysql


def mysql(sql: str, db: str = ""):
    conn01 = pymysql.connect(host="127.0.0.1", user="root", passwd="", db=db)
    cur01 = conn01.cursor()

    exe = cur01.execute(sql)
    data = cur01.fetchall()

    cur01.close()
    conn01.close()

    print("测试")

    return exe, data


def mysql_db(sql: str, flag: int = 0):
    conn01 = pymysql.connect(host="127.0.0.1", user="root", passwd="", db="pymysql")
    cur01 = conn01.cursor(cursor=pymysql.cursors.DictCursor)

    exe = cur01.execute(sql)
    if flag:
        conn01.commit()
    # data = cur01.fetchall()
    data2 = cur01.fetchone()

    cur01.close()
    conn01.close()

    print("测试")

    return exe, data2


def mysql_db2(*sql: str, flag: int = 0, params: list = "", db: str = "pymysql03", **insert_params):
    """
    在默认数据库内进行操作，如果默认数据库被删除，则error
    :param sql:
    :param flag: 0：无需传入params参数的单条sql语句
                 1：需要传入params参数的单条insert语句
                 2：无需传入params参数的多条sql语句
                 3：需要传入params参数的多条sql语句（仅限传递给单条insert语句）
                 4: 需要传入params参数的多条sql语句（传递给多条insert语句）
    :param params: 整理成list的记录数据
    :param db: 默认需要use的数据库；如需使用其他指定数据库db2，传入db="db2"
    :param insert_params: 传递给多条insert语句的多个参数；形式参数以"params_"+"数字"形式命名，如params_1，params_2等，其中数字是从1开始的连续自然数，数字大小对于于sql语句中insert语句出现的位次（即第一个insert语句要传递的参数为params_1，其余以此类推）
    :return: 返回形式：（操作影响记录数，数据tuple）；
             对于无记录返回的单条sql语句操作（如create，insert，update，delete，drop等），“数据tuple”为空tuple；
             对于有记录返回的单条sql语句操作（如show，describe，select等），“数据tuple”为“数据记录的二维tuple”；
             对于全无记录返回的多条sql语句操作，“数据tuple”为二维tuple，且该tuple的元素为空tuple，即((),[(),…])
             对于有记录返回的多条sql语句操作，“数据tuple”为二维tuple，且该二维tuple的元素与操作语句相对应：相应于无记录返回的元素为空tuple，相应于有记录返回的元素为“数据记录的二维tuple”
    """
    conn = pymysql.connect(host="127.0.0.1", user="root", passwd="", db=db)
    cur = conn.cursor(cursor=pymysql.cursors.DictCursor)

    exe = 0
    exes = []
    data = ()
    datas = []

    if flag == 0:
        exe = cur.execute(*sql)
        data = cur.fetchall()
        conn.commit()
    elif flag == 1:
        exe = cur.executemany(sql, *params)
        data = cur.fetchall()
        conn.commit()
    elif flag == 2:
        data = list(data)
        for item in sql:
            exes.append(cur.execute(item))
            datas.append(cur.fetchall())
        conn.commit()
    elif flag == 3:
        for item in sql:
            if "insert" not in item:
                exes.append(cur.execute(item))
                datas.append(cur.fetchall())
            else:
                exes.append(cur.executemany(item, params))
                datas.append(cur.fetchall())
        conn.commit()
    elif flag == 4:
        i = 1
        for item in sql:
            param_key = "params_" + str(i)
            if "insert" not in item:
                exes.append(cur.execute(item))
                datas.append(cur.fetchall())
            else:
                param = insert_params[param_key]
                exes.append(cur.executemany(item, param))
                datas.append(cur.fetchall())
                i += 1
        conn.commit()
    else:
        print("输入有误！")
        cur.close()
        conn.close()
        return

    cur.close()
    conn.close()

    if exes:
        exe_total = sum(exes)
        print("\n\033[1;31m总操作次数：%d" % len(exes))
        print("\n\033[1;32m总操作记录数：%d" % exe_total)
        print("\n\033[1;33m每次返回数据如下：")
        for i in range(len(exes)):
            print("\n\033[1;33m【第%d次】操作记录%d条，返回数据为：\033[22;34m" % (i + 1, exes[i]))
            if datas[i] == ():
                print("    ", "没有返回任何数据！")
            else:
                for j in range(len(datas[i])):
                    print(datas[i][j])
        return exe_total, tuple(datas)
    else:
        return exe, data


if __name__ == "__main__":
    # ############# 数据库 #############
    sql01 = "show databases"
    sql01_result = mysql_db2(sql01)
    print(sql01_result[0])
    print(sql01_result[1])
    print()
    #
    # sql02 = "create database pymysql03"
    # sql02_result = mysql_db2(sql02)
    # print(sql02_result)   # (1, ())
    # print()
    #
    # sql03 = "drop database pymysql02"
    # sql03_result = mysql(sql03)
    # print(sql03_result)   # (0, ())
    # print()
    #
    # sql04 = "use pymysql"
    # sql04_result = mysql(sql04)
    # print(sql04_result)   # (0, ())
    # print()

    # ############# 表 #############
    #
    # sql05 = "create table books(id int, name varchar(50), price decimal(8,2), author varchar(20))"
    # sql05_result = mysql(sql05, "pymysql03")   # 同下
    # sql05_result = mysql_db(sql05)
    # print(sql05_result)   # (0, ())
    # print()
    #
    # sql06 = "show tables"
    # sql06_result = mysql_db(sql06)
    # print(sql06_result)   # (1, (('books',),))
    # print()
    #
    # sql07 = "desc books"
    # sql07_result = mysql_db(sql07)
    # print(sql07_result)   # (1, (('books',),))
    # print()

    # ############# 增 #############
    # # 没有执行commit时，插入无效
    # sql08 = "insert into books(id, name, price, author) values('%d', '%s', '%f', '%s')" % (1, "理想国", 38.2, "柏拉图")
    # sql08_result = mysql_db(sql08)
    # print(sql08_result)   # (1, ())
    # print()
    #
    # sql09 = "insert into books(id, name, price, author) values('%d', '%s', '%f', '%s')" % (1, "理想国", 38.2, "柏拉图")
    # sql09_result = mysql_db(sql09, 1)
    # print(sql09_result)   # (1, ())
    # print()
    #
    # sql09 = "insert into books(id, name, price, author) values('%d', '%s', '%f', '%s')"
    # sql091 = "insert into books(id, name, price, author) values('%d', '%s', '%f', '%s')" % (5, "理想国", 38.2, "柏拉图")
    # sql092 = "insert into books(id, name, price, author) values('%d', '%s', '%f', '%s')" % (6, "斐多篇", 18.2, "柏拉图")
    # sql10 = "select * from books"
    # sql09_result = mysql_db2(sql091, sql092, sql10, flag=2)
    # print(sql09_result)   # (1, ())
    # print()
    #
    # sql09 = "insert into books(id, name, price, author) values(%s, %s, %s, %s)"
    # param = [(5, "理想国", 38.2, "柏拉图"), (6, "斐多篇", 18.2, "柏拉图")]
    # sql09_result = mysql_db2(sql09, params=param, flag=1)
    # print(sql09_result)  # (1, ())
    # print()
    #
    # sql09 = "delete from books where id =5"
    # sql10 = "select * from books"
    # sql09_result = mysql_db2(sql09, sql10, flag=2)
    # print(sql09_result)  # (1, ())
    # print()
    #
    # sql08 = "delete from books where id =6"
    # sql09 = "insert into books(id, name, price, author) values(%s, %s, %s, %s)"
    # param = [(5, "理想国", 38.2, "柏拉图"), (6, "斐多篇", 18.2, "柏拉图")]
    # sql10 = "select * from books"
    # sql09_result = mysql_db2(sql08, sql09, sql10, params=param, flag=3)
    # print(sql09_result)  # (1, ())
    # print()
    #
    # sql09 = "insert into books(id, name, price, author) values('%d', '%s', '%f', '%s')"
    # param = [(5, "理想国", 38.2, "柏拉图"), (6, "斐多篇", 18.2, "柏拉图")]
    # sql10 = "select * from books"
    # sql09_result = mysql_db2(sql09, sql10, params=param, flag=2)
    # print(sql09_result)  # (1, ())
    # print()
    #
    # sql09 = "insert into books(id, name, price, author) values(2, '苏格拉底的申辩', 28.2, '柏拉图')"
    # sql09_result = mysql_db(sql09, 1)
    # print(sql09_result)   # (1, ())
    # print()

    # ############# 查 #############
    # sql10 = "select * from books"
    # sql10_result = mysql_db(sql10)
    # print(sql10_result)  # (1, (……………………))
    # print()

    # ############# 改 #############
    # # 没有执行commit时，更新无效
    # sql11 = "update books set name = '理想国' where id = 1"
    # sql11_result = mysql_db(sql11)
    # print(sql11_result)  # (1, ())
    # print()
    #
    # sql12 = "update books set name = '法律篇' where id = 1"
    # sql12_result = mysql_db(sql12, 1)
    # print(sql12_result)  # (1, ())
    # print()

    # ############# 删 #############
    # sql13 = "delete from books where name = '理想国'"
    # sql13_result = mysql_db(sql13, 1)
    # print(sql13_result)
    # print()
    #
    # sql13 = "delete from books"
    # sql13_result = mysql_db(sql13, 1)
    # print(sql13_result)
    # print()

    # sql00 = "show tables"
    # sql000 = "drop table members"
    # sql01 = "create table members(id int, name varchar(20), book varchar(50))"
    # sql011 = "describe members"
    # sql02 = "insert into members(id, name, book) values(%s,%s,%s)"
    # param_members = [(1, "xiaoming", "理想国"), (2, "张三", "简爱"), (3, "lisi", "historia")]
    # sql021 = "select * from members"
    # sql03 = "select * from books"
    # sql04 = "delete from books"
    # sql05 = "insert into books(id, name, price, author) values(%s, %s, %s, %s)"
    # param_books = [(5, "理想国", 38.2, "柏拉图"), (6, "斐多篇", 18.2, "柏拉图")]
    # sql06 = "select * from books"
    # sql_result = mysql_db2(sql00, sql000, sql01, sql011, sql02, sql021, sql03, sql04, sql05, sql06, params_1=param_members, params_2=param_books, flag=4)
    # print("\n\033[0m", sql_result)  # (1, ())
    # print()

    # sql1 = "select * from members"
    # sql2 = "select * from books"
    # sql_result = mysql_db2(sql1, sql2, flag=3)
    # print(sql_result)

    # sql08 = "insert into book(id, name, price, author) values('%d', '%s', '%f', '%s')" % (1, "理想国", 38.2, "柏拉图")
    # sql_result = mysql_db2(sql08, flag=0)
    # sql = "select count(*) from books"
    # re = mysql_db(sql)
    # print(re)

    sql_1 = "select * from users_log_table"
    sql_2 = "select count(*) as count from users_log_table where username = '%s'" % ('张三')
    data_dict = mysql_db(sql_2)
    print(data_dict)
