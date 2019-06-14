#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""

"""

import pymysql


def mysql(*sql: str, flag: int = 0, params: list = "", db: str = "pymysql03", **insert_params):
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
    cur = conn.cursor()

    count = 0
    counts = []
    data = ()
    datas = []

    if flag == 0:
        count = cur.execute(*sql)
        data = cur.fetchall()
        conn.commit()
    elif flag == 1:
        count = cur.executemany(*sql, params)
        data = cur.fetchall()
        conn.commit()
    elif flag == 2:
        for item in sql:
            counts.append(cur.execute(item))
            datas.append(cur.fetchall())
        conn.commit()
    elif flag == 3:
        for item in sql:
            if "insert" not in item:
                counts.append(cur.execute(item))
                datas.append(cur.fetchall())
            else:
                counts.append(cur.executemany(item, params))
                datas.append(cur.fetchall())
        conn.commit()
    elif flag == 4:
        i = 1
        for item in sql:
            param_key = "params_" + str(i)
            if "insert" not in item:
                counts.append(cur.execute(item))
                datas.append(cur.fetchall())
            else:
                param = insert_params[param_key]
                counts.append(cur.executemany(item, param))
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

    if counts:
        count_total = sum(counts)
        print("\n\033[1;31m总操作次数：%d" % len(counts))
        print("\n\033[1;32m总操作记录数：%d" % count_total)
        print("\n\033[1;33m每次返回数据如下：")
        for i in range(len(counts)):
            print("\n\033[1;33m【第%d次】操作记录%d条，返回数据为：\033[22;34m" % (i + 1, counts[i]))
            if datas[i] == ():
                print("    ", "没有返回任何数据！")
            else:
                for j in range(len(datas[i])):
                    print(datas[i][j])
        print("\n\033[0m")
        return count_total, tuple(datas)
    else:
        return count, data


if __name__ == "__main__":

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
# sql_result = mysql(sql00, sql000, sql01, sql011, sql02, sql021, sql03, sql04, sql05, sql06, params_1=param_members, params_2=param_books, flag=4)
# print(sql_result)  # (1, ())
# print()

# sql1 = "select * from members"
# sql2 = "select * from books"
# sql_result = mysql(sql1, sql2, flag=2)
# print(sql_result)
