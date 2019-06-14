#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""
编写登陆接口：
- 输入用户名密码
- 认证成功后显示欢迎信息
- 输错三次后锁定

*********************** 解 ***********************
1.输入用户名、密码
2.检测用户名是否存在，如果不存在，返回“您输入的用户名不存在！”
3.用户名存在，检测密码是否正确，如果正确，提示登录成功
4.如果不正确，提示重新输入用户名、密码，并记录登录失败信息
5.同一用户名输入密码错误三次，锁定该用户名
"""

if __name__ == "__main__":

    usernames = []  # 记录所有用户名
    passwords = []  # 记录所有密码（顺序对应于usernames）
    fault_user = []  # 记录不重复的登录失败用户名
    fault_times = []  # 记录不重复的登录失败用户名的失败次数（顺序对应于fault_user）

    # 预处理所有用户记录
    username_password_book = [["张三", "123456"], ["李斯", "666666"], ["王五", "000000"], ["赵柳", "654321"]]
    for i in range(len(username_password_book)):
        if username_password_book[i][0] not in usernames:
            usernames.append(username_password_book[i][0])
            passwords.append(username_password_book[i][1])
        else:
            pass

    failure = True  # 判断是否登录失败
    while failure:

        # 提示用户输入用户名、密码
        print("=======================")
        username = input("==请输入用户名：")
        password = input("==请输入密码：")
        print("=======================")
        print("\n")

        # 检测用户名是否存在
        if username not in usernames:
            print("您输入的用户名不存在！\n")

        # 检测用户名是否存在于登录错误用户名单中
        elif username in fault_user:
            if fault_times[fault_user.index(username)] >= 3:
                print("该用户名已经被锁定！\n")
            elif password == passwords[usernames.index(username)]:
                print("欢迎登录！")
                failure = False
                break
            elif fault_times[fault_user.index(username)] + 1 == 3:
                print("您短时间内已经输入错误超过三次！该用户名已经被锁定！\n")
                fault_times[fault_user.index(username)] += 1
            else:
                print("用户名或密码输入错误！请重新输入！")
                fault_times[fault_user.index(username)] += 1

        # 未尝失败的用户
        elif password == passwords[usernames.index(username)]:
            print("欢迎登录！")
            failure = False
            break
        else:
            print("用户名或密码输入错误！请重新输入！")
            fault_user.append(username)
            fault_times.append(1)
