#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""
自定义错误class
**********************************

"""


class MyException(Exception):

    def __init__(self, msg):
        self.error = msg

    def __str__(self, *args, **kwargs):
        return self.error


class SensitiveWordError(MyException):
    pass


# userNotExistError = MyException("用户名不存在！")
# print(userNotExistError)
# print(type(userNotExistError))
# print()
# passwordError = MyException("密码错误！")
# print(passwordError)
# print(type(passwordError))
# print()

# 主动触发异常
# raise userNotExistError
# raise passwordError

# dirtyWordError = MyException("您说了脏话！")
# print(dirtyWordError)
# print(type(dirtyWordError))
# raise dirtyWordError


# 子类
# dirtyWordError = SensitiveWordError("您说了脏话！")
# print(dirtyWordError)
# print(type(dirtyWordError))
# raise dirtyWordError

politicalSensitiveWordError = SensitiveWordError("您说了政治不正确的话！")
# print(politicalSensitiveWordError)
# print(type(politicalSensitiveWordError))
raise politicalSensitiveWordError
