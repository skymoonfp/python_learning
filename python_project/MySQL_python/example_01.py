#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""


**************************
文件:     example_01.py
 IDE：    PyCharm
创建时间： 2019/5/25 9:25
@author： skymoon
"""

import pymysql


class JD(object):
    def __init__(self):
        self.dic = {0: self.__close,
                    1: self.__fetch_all_info,
                    2: self.__fetch_cate,
                    3: self.__fetch_brand,
                    4: self.__add_info,
                    5: self.__find_info,
                    6: self.__find_info_safe
                    }

        # user,和password换成你的root和密码
        self.__conn = pymysql.Connect(host="localhost",
                                      port=3306,
                                      database="JDDB",
                                      user="demouser",
                                      password="demopassword",
                                      charset="utf8")
        self.__cur = self.__conn.cursor()

    def __show_result(self, result):
        # print(type(result))   # <cass 'tuple'>
        for r in result:
            print(r)

    # 查询所有商品信息
    def __fetch_all_info(self):
        sql = ''' select * from goods '''
        affected = self.__cur.execute(sql)
        print("influenced %d row" % affected)
        self.__show_result(self.__cur.fetchall())

    # 查询种类信息
    def __fetch_cate(self):
        sql = ''' select * from goods_cates '''
        self.__cur.execute(sql)
        self.__show_result(self.__cur.fetchall())

    # 查询品牌信息
    def __fetch_brand(self):
        sql = ''' select * from goods_brands '''
        self.__cur.execute(sql)
        self.__show_result(self.__cur.fetchall())

    # 添加一个商品类型
    def __add_info(self):
        goods_type = input("please input a new goods type: ")
        sql = ''' insert into  goods_cates(name) values ("%s") '''
        self.__cur.execute(sql, goods_type)
        self.__conn.commit()

    # 通过ID 查找商品
    def __find_info(self):
        # 当输入　"id or True" 时会发生sql注入，看到本不该看到的东西
        goods_type = input("please input a ID of cates: ")
        sql = ''' select * from goods where id=%s''' % goods_type
        self.__cur.execute(sql)
        self.__show_result(self.__cur.fetchall())

    # 通过ID 查找商品 防SQL注入
    def __find_info_safe(self):
        goods_type = input("please input a ID of cates: ")
        # 此处不同于python的字符串格式化，必须全部使用%s占位
        sql = ''' select * from goods where id=%s'''
        # 通过参数化列表（元组）防止这种攻击,但是会产生一个warning,可以直接存储到日志log中
        self.__cur.execute(sql, (goods_type,))
        self.__show_result(self.__cur.fetchall())

    # 关闭连接，退出
    def __close(self):
        self.__cur.close()
        self.__conn.close()
        exit()

    def run(self):
        while True:
            print('*' * 50)
            print("1查询所有商品信息")
            print("2查询所有商品在种类信息")
            print("3查询所有商品在品牌信息")
            print("4添加商品种类")
            print("5根据id查询商品信息")
            print("6根据id查询商品信息安全方式")
            print("0退出")
            print('*' * 50)

            option = int(input("please input your option: "))
            try:
                self.dic[option]()
                # string()  # eval()
            except KeyError:
                print("enter is error! ")


def main():
    jd = JD()
    jd.run()


if __name__ == '__main__':
    main()
