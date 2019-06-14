#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""

"""


class Province(object):
    memo = "中国三十省之一"

    def __init__(self, name, capital, gdp, population, Thailand="没有去过泰国"):
        self.Name = name
        self.Capital = capital
        self.GDP = gdp
        self.Population = population

        self.__Thailand = Thailand

    def sport_meeting(self):
        print(self.Name + "正在举办运动会！")
        return "Yeah!"

    @staticmethod
    def foo():
        print("各个省要带头反腐！")
        return "Oh!"

    @property
    def avg_gdp(self):
        return self.Name + "人均GDP是" + str("{:9.2f}".format(self.GDP / self.Population))

    def show(self):
        print(self.Name + self.__Thailand)

    # 只读特性
    @property
    def Thailand_show(self):
        return self.Name + self.__Thailand

    # 可读可写特性（删除此段，Thailand_show变为只读）
    @Thailand_show.setter
    def Thailand_show(self, value):
        self.__Thailand = value

    def __march(self):
        print(self.Name + "军队集结！")

    def foo2(self):
        self.__march()


hubei = Province("湖北", "武汉", 28000000, 50000)
shanghai = Province("上海", "上海", 88888888, 70000)

print(Province.memo)
print(hubei.memo)
print(shanghai.memo)
memo = "中国三十六省之一"  # 无法修改静态字段
print(Province.memo)
print(hubei.memo)
Province.memo = "中国三十六省之一"  # 成功修改整个类的静态字段
print(Province.memo)
print(hubei.memo)
hubei.memo = "中国三十四省之一"  # 成功修改某个对象的静态字段
print(Province.memo)
print(hubei.memo)
print(shanghai.memo)
print()

print(hubei.Capital)
print(shanghai.GDP)
print()

hubei.sport_meeting()
Province.foo()
hubei.foo()
print()

print(Province("湖南", "长沙", 25000000, 48888).Name)
print(Province("湖南", "长沙", 25000000, 48888).sport_meeting())
print(Province("湖南", "长沙", 25000000, 48888).foo())
print()

hunan = Province("湖南", "长沙", 25000000, 48888)

print(hubei.avg_gdp)
print(shanghai.avg_gdp)
print(hunan.avg_gdp)
print()

# 私有字段调用与修改
japan = Province("日本", "东京", 125000000, 140000, "去过泰国")
# print(japan.__Thailand)
japan.show()
print(japan.Thailand_show)
japan.Thailand_show = "没有去过泰国"
japan.show()
print("修改后：" + japan.Thailand_show)
hunan.show()
print(shanghai.Thailand_show)
shanghai.Thailand_show = "去过泰国"
print("修改后：" + shanghai.Thailand_show)
print()

# 私有方法调用
# japan.__march()
japan.foo2()
japan._Province__march()  # 强制调用私有方法


# 修改私有字段对比
class test3(object):

    def __init__(self):
        self.__private = "原始3"

    @property
    def show(self):
        return self.__private

    @show.setter
    def show(self, value):
        self.__private = value


t3 = test3()
print(t3.show)
t3.show = "修改3"
print(t3.show)


class test1:

    def __init__(self):
        self.__private = "原始"

    @property
    def show(self):
        return self.__private


t1 = test1()
print(t1.show)
# t1.show = "修改"
# print(t1.show)
print()


# # __init__，__del__，__call__
# class Foo:
#
#     def __del__(self):
#         print("死了！")
#
#     def __call__(self):
#         print("call!")
#
#     def go(self):
#         print("go!")
#
#     def __init__(self):
#         pass
#
#
# print(Foo)
# f = Foo()
# print(f)
# print()
#
# f.go()
# print(f.go())
# print()
#
# f()
# print(f())
# print()


# 继承
class Father(object):

    def __init__(self):
        self.Fname = "father"
        print("Father.__init__")

    def func(self):
        print("father.func")

    def bad(self):
        print("father.抽烟喝酒烫头")


class Son(Father):

    def __init__(self):
        self.Sname = "son"
        print("Son.__init__")
        Father.__init__(self)
        super(Son, self).__init__()

    def bar(self):
        print("son.bar")

    # def bad(self):
    #     print("son.抽烟喝酒烫头")

    def bad(self):
        Father.bad(self)
        print("son.赌博")


s1 = Son()
s1.bar()
s1.func()
s1.bad()
print()


# 多重继承（python3经典类和新式类相同——广度优先）
class A:
    def __init__(self):
        print("This is A.")

    def save(self):
        print("save method from A")


class B(A):
    def __init__(self):
        print("This is B.")


class C(A):
    def __init__(self):
        print("This is C.")

    def save(self):
        print("save method from --C--")


class D(C, B):
    def __init__(self):
        print("This is D.")


f = D()
f.save()
print(D.__mro__)
print()

# 抽象类（失败：子类未实现方法send时不报错）
from abc import ABCMeta, abstractclassmethod


class Alert:
    __metaclass__ = ABCMeta

    @abstractclassmethod
    def send(cls): pass


class WeiXin(Alert):
    def __init__(self):
        print("__init__")

    # def send(self):
    #     print("send.WeiXin")


f = WeiXin()
f.send()
print()

# 抽象类（成功：子类未实现方法send时报错）
import abc


class Alert(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def send(self): pass


class WeiXin(Alert):
    def __init__(self):
        print("__init__")

    def send(self):
        print("send.WeiXin")


f = WeiXin()
f.send()
