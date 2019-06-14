#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""

"""

"""
load data [low_priority] [local] infile ‘file_name txt’ [replace | ignore]
into table tbl_name
[fields
[terminated by’t’]
[OPTIONALLY] enclosed by ‘’]
[escaped by’’ ]]
[lines terminated by’n’]
[ignore number lines]
[(col_name, )]
"""


def exc_data():
    conn = connect(host='主机名', port='端口号', user='用户名', password='密码', database='数据库名', charset='utf8')
    cs = conn.cursor()
    # 注意表明后边添加的字段名要与自己写的文本文件相对应，如果文本文件有主键，而且与其他字段也是一一对应，这里只需要写上一个数据表即可，但是如果文本文件一般情况下是没有定义主键的，因此我们需要在这里添加上几个除主键外其他的字段名
    sql = "load data infile '/var/lib/mysql-files/data.txt' into table '表名'(字段名);"
    # 针对定义好的数据表以及文本，就是应该添加上这几个字段(name,age,gender,classify_id)
    cs.execute(sql)
    conn.commit()
    cs.close()
    conn.close()
    print('OK')
