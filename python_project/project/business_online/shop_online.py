#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""

"""

from project.business_online import log_in_check
from project.business_online import shopping


# 信用卡还款
def credit_repayment(account, money):
    pass


# 清单查询显示
def output_shopping_list_query(customer_detailed_list: list, date_start: str, date_end: str):
    pass


# 清单查询
def shopping_list_query(username: str, date_start: str, date_end: str):
    pass


# 购物
def shopping(username: str):
    pass


# 继续其他操作或退出
def function_choose2(username: str):
    choose = input("\033[22;33m继续其他操作请输入1，直接退出请输入0：\033[0m\n")
    if choose == "1":
        function_choose(username)
    else:
        print("\033[1;35m{:^50}\033[22;33m\n".format("谢谢惠顾"))


# 操作选择
def function_choose(username: str):
    print("\033[1;31m{:^50}\033[0m".format("请选择您要执行的操作"))
    print("\033[22;34m{:^30}\033[22;35m{:^20}".format("购物", "1"))
    print("\033[22;34m{:^30}\033[22;35m{:^20}".format("清单查询", "2"))
    print("\033[22;34m{:^30}\033[22;35m{:^20}".format("信用卡还款", "3"))
    print("\033[22;34m{:^30}\033[22;35m{:^20}\033[0m".format("退出登陆", "0"))
    choose = input("请选择：\n")

    # 退出登陆
    if choose == "0":
        print("\033[1;35m{:^50}\033[22;33m\n".format("谢谢惠顾"))

    # 购物
    elif choose == "1":
        shopping(username)
        function_choose2(username)

    # 清单查询
    elif choose == "2":
        # 起止日期输入
        date_start = input("请输入要查询的起始日期（yyyy-mm-dd）：\n")
        date_end = input("请输入要查询的结束日期（yyyy-mm-dd）：\n")

        customer_detailed_list = shopping_list_query(username, date_start, date_end)
        output_shopping_list_query(customer_detailed_list, date_start, date_end)
        function_choose2(username)

    # 信用卡还款
    else:
        # 还款银行账号和金额输入
        account = input("请输入要还款的银行账号：\n")
        money = input("请输入要还款的金额：\n")

        credit_repayment(account, money)
        function_choose2(username)


# 用户登陆与操作
def customer_log_in_and_operate():
    # 登陆
    username = log_in_check.customers_log_in(r"..\..\data_files\customers_info_table.txt")

    # 登陆成功，进入操作选择界面
    if username:
        # 操作选择
        function_choose(username)
    else:
        pass


def shop_online_process():
    # 用户登陆与操作
    customer_log_in_and_operate()


if __name__ == "__main__":
    shop_online_process()
