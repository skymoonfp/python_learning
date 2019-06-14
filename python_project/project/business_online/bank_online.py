#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""
网上银行
=============================
功能（必须）：
1.额度15000
2.可以提现，手续费5%
3.每月最后一天出账单，写入文件
4.记录每月日常消费流水
5.提供还款接口优化
——————————————————————
（可选）：
每月10号为还款日，过期未还，按欠款额5‱计息
"""

import calendar
import datetime
import pickle
import time

from mytime import timing_monthly
from project.business_online import log_in_check


# 用户账户信息读取
def customer_account_data(username: str = "", account: str = "main_account"):
    # 读取账户信息
    try:
        customers_account_file = open(r"..\..\data_files\bank_customers_account_table.pk", "rb+")
    except FileNotFoundError:  # 无用户账户文件时，创建文件，并初始化该账户
        account_number = next(account_generate())
        customers_account_data = {username: {("main_account", account_number): [
            {"total_amount": 15000, "balance": 15000, "operate_description": "customer_account_initiation",
             "operate_time": time.time(), "expenditure": 0, "income": 0}]}}
        customers_account_file = open(r"..\..\data_files\bank_customers_account_table.pk", "wb+")
        pickle.dump(customers_account_data, customers_account_file)
        customers_account_file.close()
    else:
        try:
            customers_account_data = pickle.load(customers_account_file)
        except EOFError:  # 用户账户文件为空时，写入该账户初始化信息
            customers_account_file.close()
            account_number = next(account_generate())
            customers_account_data = {username: {("main_account", account_number): [
                {"total_amount": 15000, "balance": 15000, "operate_description": "customer_account_initiation",
                 "operate_time": time.time(), "expenditure": 0, "income": 0}]}}
            customers_account_file = open(r"..\..\data_files\bank_customers_account_table.pk", "wb+")
            pickle.dump(customers_account_data, customers_account_file)
            customers_account_file.close()
        else:
            while True:
                try:
                    customers_account_data = pickle.load(customers_account_file)
                except EOFError:
                    break
                else:
                    pass
            if username == "":
                pass
            else:
                if username not in customers_account_data.keys():  # 账户不存在时，初始化
                    account_number = next(account_generate())
                    customers_account_data[username] = {("main_account", account_number): [
                        {"total_amount": 15000, "balance": 15000, "operate_description": "customer_account_initiation",
                         "operate_time": time.time(), "expenditure": 0, "income": 0}]}
                    pickle.dump(customers_account_data, customers_account_file)
                    customers_account_file.close()
                else:
                    pass

    # 返回账户信息
    customers_account_data_info = list(
        customer_account_data2(customers_account_data, username=username, account=account))
    return customers_account_data_info[0], customers_account_data_info[1], customers_account_data_info[2]


# 银行账号生成
def account_generate():
    account = 8888888
    while account < 888888888888:
        yield str(account).zfill(19)
        account += 1


# 根据用户银行账号读取用户信息
def customer_account_data2(customers_account_data: dict, username: str = "", account: str = "main_account"):
    if not username:
        username_account = positioning_customer_info(customers_account_data, account=account)
        if not username_account:
            username = positioning_customer_info(customers_account_data, account=account)[0][0]
            account_name = positioning_customer_info(customers_account_data, account=account)[1]
            customer_account_data_list = customers_account_data[username][account_name]
            return username, account_name, customer_account_data_list
        else:
            return
    else:
        account_name = positioning_customer_info(customers_account_data, username=username)[1]
        return username, account_name, customers_account_data[username][account_name]


# 操作选择
def function_choose(username: str):
    print("\033[1;31m{:^50}\033[0m".format("请选择您要执行的操作"))
    print("\033[22;34m{:^30}\033[22;35m{:^20}".format("查询余额", "1"))
    print("\033[22;34m{:^30}\033[22;35m{:^20}".format("提取现金", "2"))
    print("\033[22;34m{:^30}\033[22;35m{:^20}".format("账单查询", "3"))
    print("\033[22;34m{:^30}\033[22;35m{:^20}".format("信用还款", "4"))
    print("\033[22;34m{:^30}\033[22;35m{:^20}\033[0m".format("退出登陆", "0"))
    choose = input("请选择：\n")

    # 退出登陆
    if choose == "0":
        print("\033[1;35m{:^50}\033[22;33m\n".format("谢谢惠顾"))

    # 查询余额
    elif choose == "1":
        customer_balance_query(username)
        function_choose2(username)

    # 提取现金
    elif choose == "2":
        withdraw_cash(username)
        function_choose2(username)

    # 账单查询
    elif choose == "3":
        # 起止日期输入
        date_start = input("请输入要查询的起始日期（yyyy-mm-dd）：\n")
        date_end = input("请输入要查询的结束日期（yyyy-mm-dd）：\n")

        customer_detailed_list = customer_detailed_list_query(username, date_start, date_end)
        output_customer_detailed_list_query(customer_detailed_list, date_start, date_end)
        function_choose2(username)

    # 信用还款
    else:
        credit_repayment(username)
        function_choose2(username)


# 继续其他操作或退出
def function_choose2(username: str):
    choose = input("\033[22;33m继续其他操作请输入1，直接退出请输入0：\033[0m\n")
    if choose == "1":
        function_choose(username)
    else:
        print("\033[1;35m{:^50}\033[22;33m\n".format("谢谢惠顾"))


# 余额查询
def customer_balance_query(username: str):
    account_data = customer_account_data(username)[2]
    print(account_data)
    total_amount, balance = account_data[-1]["total_amount"], account_data[-1]["balance"]
    print("您的总额度是\033[1;31m{0:.2f}\033[0m元！\n剩余可用额度是\033[1;32m{1:.2f}\033[0m元！\n".format(total_amount, balance))


# 提取现金
def withdraw_cash(username: str):
    withdraw_cash_number = float(input("请问您想提取多少现金？\n"))
    account_data = customer_account_data(username)[2]
    # 可用额度不足
    if account_data[-1]["balance"] < withdraw_cash_number:
        print("您的剩余可用额度不足！请重新输入！")
    else:
        customer_account_data_update(withdraw_cash_number, "取现", username=username)
        print("\033[1;35m{:^50}\033[0m\n".format("取现成功"))


# 账单查询
def customer_detailed_list_query(username: str, date_start: str, date_end: str):
    # 起止时间转换
    date_start_stamp = time.mktime(time.strptime(date_start, "%Y-%m-%d"))
    date_end_stamp = time.mktime(time.strptime(date_end, "%Y-%m-%d")) + 24 * 60 * 60 - 1

    # 查找记录
    account_data = customer_account_data(username)[2]
    customer_detailed_list = []
    for data in account_data:
        operate_time = 0
        for item in data.items():
            if "operate_time" in item:
                operate_time = item[1]
        if date_start_stamp <= operate_time <= date_end_stamp:
            customer_detailed_list.append(data)
        else:
            pass
    else:
        return customer_detailed_list


# 打印账单记录
def output_customer_detailed_list_query(customer_detailed_list: list, date_start: str, date_end: str):
    print("您从\033[22;33m{date_start}\033[0m到\033[22;33m{date_end}\033[0m之间的详单如下：".format(date_start=date_start,
                                                                                         date_end=date_end))
    if not len(customer_detailed_list):
        print("您在该时间段内没有任何操作！\n")
    else:
        for data in customer_detailed_list:
            output_formation = "{operate_time}   {operate_description}   {expenditure}   {income}    {balance}"
            print(output_formation.format(**data))


# 信用还款
def credit_repayment(username: str):
    credit_repayment_amount = float(input("请输入还款金额：\n"))
    credit_repayment_interface(credit_repayment_amount, username=username)


# 信用还款接口
def credit_repayment_interface(repayment_amount: float, operate_description: str = "还款", username: str = "",
                               account: str = "main_account"):
    """
    可供外部程序调用的还款接口
    :param repayment_amount: 还款金额
    :param operate_description: 还款描述，例如“支付宝还款”、“转账还款”等（缺省时为“还款”）
    :param username: 还款用户账号
    :param account: 还款银行账号
    :return: 无该银行账户，提示相关信息，返回False；有该银行账户，进行还款操作，并提示相关信息，返回True
    """
    if username == "":
        account_data = customer_account_data(account=account)
        if not account_data:
            print("您输入的银行账号然而并不存在！\n")
            return False
        else:
            customer_account_data_update(repayment_amount, operate_description, account=account, operate_flag=1)
            print("\033[1;35m{:^50}\033[22;33m\n".format("还款成功"))
            return True
    else:
        customer_account_data_update(repayment_amount, operate_description, username=username, account=account,
                                     operate_flag=1)
        print("\033[1;35m{:^50}\033[22;33m\n".format("还款成功"))
        return True


# 由dict_value查找dict_key，返回全部key列表
def get_key(dictation: dict, value):
    return [k for k, v in dictation.items() if v == value]


# 定位包含指定信息的用户账户记录条目位置
def positioning_customer_info(customers_account_data: dict, username: str = "", account: str = "main_account"):
    """

    :param customers_account_data:
    :param username:
    :param account:
    :return: ([username], ("account_name", "account_number")
    """
    if username == "":
        for customer_account in customers_account_data.values():
            for account_name in customer_account.keys():
                if account in account_name:
                    return get_key(customers_account_data, {account_name: customer_account[account_name]}), account_name
                else:
                    continue
        else:
            return
    else:
        for customer_account_data in customers_account_data.items():
            if username == customer_account_data[0]:
                for account_data in customer_account_data[1].items():
                    if account in account_data[0]:
                        return [username], account_data[0]
                    else:
                        continue
            else:
                continue


# 更新用户账户信息
def customer_account_data_update(alter_amount: float, operate_description: str, username: str = "",
                                 account: str = "main_account", operate_flag: int = 0):
    # 读取用户账户信息
    customers_account_data_info = customer_account_data(username=username, account=account)
    username = customers_account_data_info[0]
    account_name = customers_account_data_info[1]
    account_data = customers_account_data_info[2]

    # 向用户账户下的银行账户里面添加记录
    balance = 0
    for item in account_data[-1].items():
        if "balance" in item:
            balance = item[1]
        else:
            pass
    account_data_new_record = dict()
    account_data_new_record["total_amount"] = 15000
    account_data_new_record["operate_description"] = operate_description
    account_data_new_record["operate_time"] = time.time()
    if operate_flag == 0:
        account_data_new_record["expenditure"] = alter_amount
        account_data_new_record["income"] = 0
        account_data_new_record["balance"] = balance - alter_amount
    else:
        account_data_new_record["expenditure"] = 0
        account_data_new_record["income"] = alter_amount
        account_data_new_record["balance"] = balance + alter_amount

    # 写入文件
    with open(r"..\..\data_files\bank_customers_account_table.pk", "rb+") as customers_account_file:
        while True:
            try:
                customers_account_data = pickle.load(customers_account_file)
            except EOFError:
                break
            else:
                pass
        customers_account_data[username][account_name].append(account_data_new_record)
        pickle.dump(customers_account_data, customers_account_file)


# 判断是否自动更新
def is_auto_update_time(shu_day: int, schedule_time: str, begin_date: str = "2000-01-01 00:00:00",
                        end_date: str = "2099-12-31 23:59:59"):
    day_in_months = timing_monthly.day_in_month_range(shu_day, schedule_time, begin_date, end_date)
    days = []  # 存放转换成时间戳的day_in_months
    datetime_run = 0  # 下一个要运行的时间
    for day_in_month in day_in_months:
        days.append(time.mktime(time.strptime(day_in_month, "%Y-%m-%d %H:%M:%S")))

    current_time = time.time()
    for i in range(len(day_in_months)):
        if current_time == days[i]:
            datetime_run = current_time + 1  # 推迟1秒
        elif days[i] < current_time < days[i + 1]:
            datetime_run = days[i + 1] + 1  # 推迟1秒
        else:
            pass

    if time.time() < datetime_run:
        return False
    else:
        return True


# 当前日份之前一个月内账单提取
def customer_past_a_month_detailed_list_query():
    # 起止时间
    year0 = datetime.datetime.now().year
    month0 = datetime.datetime.now().month
    day0 = datetime.datetime.now().day

    if month0 == 1:
        if day0 == 1:
            date_start = str(year0 - 1) + "-12-01 00:00:00"
            date_end = str(year0 - 1) + "-12-31 23:59:59"
        else:
            date_start = str(year0 - 1) + "-12-" + str(day0).zfill(2) + " 00:00:00"
            date_end = str(year0) + "-1-" + str(day0 - 1).zfill(2) + " 23:59:59"
    else:
        if day0 == 1:
            date_start = str(year0) + "-" + str(month0 - 1).zfill(2) + "-01 00:00:00"
            date_end = str(year0) + "-" + str(month0 - 1).zfill(2) + "-" + str(
                calendar.monthrange(year0, month0 - 1)[1]) + " 23:59:59"
        else:
            if calendar.monthrange(year0, month0 - 1)[1] >= day0:
                date_start = str(year0) + "-" + str(month0 - 1).zfill(2) + "-" + str(day0).zfill(2) + " 00:00:00"
                date_end = str(year0) + "-" + str(month0).zfill(2) + "-" + str(day0 - 1).zfill(2) + " 23:59:59"
            else:  # 上个月天数小于当前日份
                date_start = str(year0) + "-" + str(month0 - 1).zfill(2) + "-" + str(
                    calendar.monthrange(year0, month0 - 1)[1]) + " 00:00:00"
                date_end = str(year0) + "-" + str(month0).zfill(2) + "-" + str(day0 - 1).zfill(2) + " 23:59:59"

    # 载入文件bank_customers_account_table.pk，提取账单
    with open(r"..\..\data_files\bank_customers_account_table.pk", "rb") as customers_account_file:
        try:
            customers_account_data = pickle.load(customers_account_file)
        except FileNotFoundError:
            return
        except EOFError:
            return
        else:
            while True:
                try:
                    customers_account_data = pickle.load(customers_account_file)
                except EOFError:
                    break
                else:
                    pass
            customer_past_a_month_detailed_list = {}
            for customer_account in customers_account_data.items():
                for account_data in customer_account[1].itesm():
                    customer_past_a_month_detailed_list[customer_account[0]] = {
                        account_data[0]: customer_detailed_list_query(account_data[1], date_start, date_end)}
            customer_past_a_month_detailed_list_list = [date_start + " ~ " + date_end + "账单",
                                                        customer_past_a_month_detailed_list]
            return customer_past_a_month_detailed_list_list


# 超期未还计息
def customer_overdue_loan_interest(customer_past_a_month_detailed_list: dict):
    interest_info = []
    for customer_account in customer_past_a_month_detailed_list.items():
        for account_data in customer_account[1].itesm():
            if account_data[0]["balance"] >= account_data[0]["total_amount"]:
                interest = 0
            else:
                interest_reduce = 0
                for data in account_data:
                    if data["income"] != 0:
                        interest_reduce_days = (time.time() - data["operate_time"]) // (24 * 60 * 60)
                        interest_reduce += data["income"] * 0.0005 * interest_reduce_days
                    else:
                        pass
                interest = (account_data[0]["total_amount"] - account_data[0]["balance"]) * 0.0005 * (
                            (time.time() - account_data[0]["operate_time"]) // (24 * 60 * 60)) - interest_reduce
            interest_info.append([customer_account[0], account_data[0], interest])
    return interest_info


# 超期未还更新
def customer_overdue_loan_update():
    if not is_auto_update_time(10, "23:59:59"):
        return
    else:
        customer_past_a_month_detailed_list_list = customer_past_a_month_detailed_list_query()
        interest_info = customer_overdue_loan_interest(customer_past_a_month_detailed_list_list[1])
        for item in interest_info:
            customer_account_data_update(item[2], "超期未还利息", item[0], item[1])


# 月度账单更新
def customer_monthly_detailed_list_query():
    if not is_auto_update_time(31, "23:59:59"):
        return
    else:
        customer_monthly_detailed_list_list = customer_past_a_month_detailed_list_query()

        # 写入文件bank_customers_account_monthly_detailed_list.pk
        with open(r"..\..\data_files\bank_customers_account_monthly_detailed_list.pk",
                  "ab+") as customers_monthly_detailed_list_file:
            try:
                pickle.dump(customer_monthly_detailed_list_list, customers_monthly_detailed_list_file)
            except EOFError:
                customers_monthly_detailed_list_file.close()
                customers_monthly_detailed_list_file = open(
                    r"..\..\data_files\bank_customers_account_monthly_detailed_list.pk", "wb+")
                pickle.dump(customer_monthly_detailed_list_list, customers_monthly_detailed_list_file)
            else:
                return


# 定时自动更新所有用户账户信息
def auto_update():
    # 更新用户信息（超期未还计息）
    customer_overdue_loan_update()

    # 更新用户信息（月度账单）
    customer_monthly_detailed_list_query()


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


def bank_online_process():
    while True:
        # 自动定时更新所有用户账户信息
        auto_update()

        # 用户登陆与操作
        customer_log_in_and_operate()


if __name__ == "__main__":
    bank_online_process()
