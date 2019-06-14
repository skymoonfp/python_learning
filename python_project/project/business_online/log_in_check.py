#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""
用户登陆
"""

import pickle
import time

from project.business_online import file_pretreatment


# 登录界面及用户输入
def log_in_input():
    print("\033[1;31m{:^50}\033[22;33m\n".format("欢迎光临"))
    print("{:^50}".format("请输入用户账号"))
    username = input()
    print("{:^50}".format("请输入用户密码"))
    password = input()
    print("\033[0m")
    return username, password


# 检测用户输入信息是否与指定文件中的用户信息匹配
def check_log_in(customers_log_in_information: list, username: str, password: str, try_times: int = 3):
    """
    检查登陆是否成功
    :param customers_log_in_information: 所有用户账户密码信息
    :param username: 用户输入的用户名
    :param password: 用户输入的密码
    :param try_times: 可以尝试次数
    :return: "success"；"failed"；"locked"
    """
    if log_in_fault(username, try_times):  # 是否锁定
        for i in range(len(customers_log_in_information)):
            if username == customers_log_in_information[i][0]:
                if password == customers_log_in_information[i][1]:
                    print("\033[1;35m{:^50}\033[22;33m\n".format("欢迎登陆"))
                    return "success"
                else:
                    if log_in_fault(username, try_times, 1):
                        print("用户名或密码输入错误！请重新输入！\n\n")
                        return "failed"
                    else:
                        print("您短时间内已经输入错误超过\033[1;35m%d\033[0m次！该用户名已经\033[1;31m被锁定\033[0m！\n\n" % try_times)
                        return "locked"
            else:
                continue
        else:
            print("您输入的用户名不存在！请重新输入！\n\n")
            return "failed"
    else:
        print("该用户名已经\033[1;31m被锁定\033[0m！\n\n")
        return "locked"


# 错误登陆信息记录
def log_in_fault(username: str, try_times: int = 3, flag: int = 0):
    """
    记录登陆失败信息，返回是否锁定
    :param username: 登陆失败时记录到的用户名
    :param try_times: 最大尝试次数
    :param flag: 判断是否需要添加新记录，默认0表示不添加
    :return: 用户是否锁定：锁定返回False，未锁定返回True
    """
    # 记录错误信息的文件为空时异常处理
    file_empty_exception_processing(r"..\..\data_files\customers_log_in_fault_table.pk")

    # flag = 0，即只判断，不添加记录时
    if not flag:
        return log_in_fault_judge(r"..\..\data_files\customers_log_in_fault_table.pk", username)

    # flag = 1, 写入记录
    else:
        return log_in_fault_register(r"..\..\data_files\customers_log_in_fault_table.pk", username, try_times)


def file_empty_exception_processing(file_name: str):
    """
    文件为空时异常处理
    :param file_name: 文件名
    :return: 无返回
    """
    with open(file_name, "rb") as log_fault_file:
        try:
            pickle.load(log_fault_file)
        except EOFError:
            log_fault_file.close()
            log_fault_file = open(file_name, "wb+")
            pickle.dump({"黄帝": []}, log_fault_file)  # 文件为空时，主动添加一条记录
        else:
            pass


def log_in_fault_judge(customers_log_in_fault_table: str, username: str):
    """
    判断登陆是否锁定
    :param customers_log_in_fault_table: 登录失败信息记录文件
    :param username: 登陆用户名
    :return: 未锁定返回True；锁定返回False
    """

    """
    记录形式：dict
        key: username, recording_time, locked_time, is_locked(0:is not locked; 1:is locked)
        value: 

    """

    with open(customers_log_in_fault_table, "rb") as log_fault_file:  # 打开所有用户账号密码记录文件
        log_fault_info = []
        while True:
            try:
                log_fault_info.append(pickle.load(log_fault_file))
            except EOFError:
                break
        for i in range(-1, -len(log_fault_info) - 1, -1):
            if username not in log_fault_info[i].values():  # 是否有记录
                continue
            else:
                if not log_fault_info[i]["is_locked"]:  # 是否锁定
                    return True
                else:
                    # 对于记录中显示锁定的用户，根据当前时间与锁定时间的间隔（例如24小时）判定是否解锁并重置错误次数
                    if time.time() - log_fault_info[i]["locked_time"] < 24 * 60 * 60:  # 锁定时间是否超过24小时
                        return False
                    else:  # 解锁设置并返回
                        return True
        else:  # 无记录用户
            return True


def log_in_fault_register(customers_log_in_fault_table: str, username: str, try_times: int = 3):
    """
    失败登陆信息记录，并判断是否锁定
    :param customers_log_in_fault_table: 登录失败信息记录文件
    :param username: 登陆用户名
    :param try_times: 最大尝试次数
    :return: 未锁定返回True；锁定返回False
    """

    """
    记录形式：dict
        key: username, recording_time, locked_time, is_locked(0:is not locked; 1:is locked)
        value: 

    """

    with open(customers_log_in_fault_table, "rb+") as log_fault_file:
        log_fault_info = []
        user_log_fault_info = []

        while True:
            try:
                log_fault_info.append(pickle.load(log_fault_file))
            except EOFError:
                break

        for i in range(-1, -len(log_fault_info) - 1, -1):
            if username in log_fault_info[i].values():  # 是否有记录
                user_log_fault_info.append(log_fault_info[i])

        # print(user_log_fault_info)

        # 无记录用户
        if user_log_fault_info == []:
            new_log_fault_info = {"username": username, "recording_time": time.time(), "locked_time": 0, "is_locked": 0}
            judgement = True
            pickle.dump(new_log_fault_info, log_fault_file)
            return judgement

        # 对于已有登陆错误记录的用户进行区分判断
        elif len(user_log_fault_info) < try_times - 1:
            new_log_fault_info = {"username": username, "recording_time": time.time(), "locked_time": 0, "is_locked": 0}
            judgement = True
        else:
            # 已经存在两条登陆错误记录，且当前错误登记时间与第一次错误登记时间间隔小于3分钟，锁定该账户
            if time.time() - user_log_fault_info[try_times - 2]["recording_time"] < 3 * 60:
                new_log_fault_info = {"username": username, "recording_time": time.time(), "locked_time": time.time(),
                                      "is_locked": 1}
                judgement = False
            else:
                new_log_fault_info = {"username": username, "recording_time": time.time(), "locked_time": 0,
                                      "is_locked": 0}
                judgement = True

        pickle.dump(new_log_fault_info, log_fault_file)
        return judgement


# 用户登陆
def customers_log_in(customers_log_in_file: str, try_times: int = 3):
    """
    用户登陆
    ————————————————————————
    短时间（3分钟）内登陆失败超过try_times（默认3）次账号锁定，24小时内不得重试
    :param customers_log_in_file: 记录用户登陆信息的文件名
    :param try_times: 用户登陆可尝试的次数
    :return: 登陆成功返回username；锁定或失败无返回（再次返回登陆界面）
    """

    # 从指定文件读取所有用户信息
    customers_log_in_information = file_pretreatment.table_file_pretreatment_list2d(customers_log_in_file)

    while True:
        # 显示登录界面，提示用户输入账户和密码
        username, password = log_in_input()

        # 检查登陆是否成功
        check = check_log_in(customers_log_in_information, username, password, try_times)

        # 根据登陆检查的返回值确定后续操作及返回值
        if check == "success":
            return username
        elif check == "failed":
            continue
        else:  # =="locked"
            continue


if __name__ == "__main__":
    customers_log_in(r"..\..\data_files\customers_info_table.txt")
