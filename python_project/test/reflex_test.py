#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""
反射
********************************
输入格式：[文件夹.][文件夹.][文件夹.]...py文件(module).函数
"""


def from_import_func2(func_path: str):
    function1 = func_path
    function2 = function1.split(".")
    function3 = function2[:-1]
    function4 = ".".join(function3)

    # mod1 = __import__(function4)
    # mod2 = getattr(mod1, function2[1])
    # mod3 = getattr(mod2, function2[2])
    # mod4 = getattr(mod3, function2[3])

    mod = __import__(function4)
    mod = getattr(mod, function2[1])
    mod = getattr(mod, function2[2])
    mod = getattr(mod, function2[3])

    return mod


def from_import_func(func_path: str):
    function1 = func_path
    function2 = function1.split(".")
    function3 = function2[:-1]
    function4 = ".".join(function3)

    mod = __import__(function4)
    for i in range(len(function2) - 1):
        mod = getattr(mod, function2[i + 1])

    return mod


if __name__ == "__main__":
    r = "project.business_online.bank_online.get_key"
    a = {"name": "zhangsan", "salary": 30000, "birthday": "1988-8-8"}
    b = "zhangsan"
    c = "1988-08-08"

    func2 = from_import_func2(r)
    print(func2(a, b))
    print(func2(a, c))

    module = input("What function do you wanting?\n")
    func = from_import_func(module)
    print(func(a, b))
    print(func(a, c))
