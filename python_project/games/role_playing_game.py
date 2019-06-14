#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""

"""

import pickle
import time


# 人物类型定义
class Person(object):

    def __init__(self, name: str, birthday: str, gender: str, weight: int, height: int, hometown, country: str = "中国"):
        self.Name = name
        self.Birthday = birthday
        self.Gender = gender
        self.Weight = weight
        self.Height = height
        self.Hometown = hometown
        self.Country = country

    def learning(self, content, time_spend):
        print("您开始学习{content}，预计耗时{time}s!".format(content=content, time=time_spend))
        time.sleep(time_spend)
        print("您已经完成了{content}的学习，开始崭新的人生之旅吧！".format(content=content))

    def working(self):
        pass

    def time_count_down(self):
        pass

    @property
    def sweetheart(self):
        return

    # 星座判断
    def constellation(self, birthday):
        pass


# 游戏进行时
class Game(object):

    def __init__(self, player, npc01, npc02):
        self.Player = player
        self.NPC01 = npc01
        self.NPC02 = npc02

    # 人生起步
    def MNRS_start(self):
        print("一觉醒来，世界变了样……")
        time.sleep(1)
        print("你整理了一下思绪，努力回忆到底发生了什么，可是什么也想不起来……")
        time.sleep(2)
        print("正当你苦思冥想之时，突然，一只美女女仆跳到了你面前，吓了你一跳！")
        time.sleep(2)
        print(
            "\033[1;35m蕾姆\033[0m：\033[1;31m{name}\033[0m主人，您好！我是您的异世界之旅伴侣\033[1;34m蕾姆\033[0m！刚才没吓到您吧！请问主人有什么吩咐？".format(
                name=self.Player.Name))
        time.sleep(3)
        print("\033[1;35m我\033[0m：你……你……你是我媳妇？！")
        time.sleep(2)
        print("\033[1;35m蕾姆\033[0m：主人别逗了，\033[1;34m蕾姆\033[0m只是您的异世界之旅伴侣！能（在您的梦中）帮您打扫、做饭、暖床……以及")
        time.sleep(3)
        print("""
                        继续游戏     Continue
                        保存游戏进度 Save
                        读取游戏进度 Load
                        退出游戏     Exit
        """)
        time.sleep(2)
        print("请问主人需要什么服务呢？")
        choise = input("\033[1;35m我\033[0m：")
        print("\033[1;35m蕾姆\033[0m：好的，主人！下次有需要别忘记了召唤\033[1;34m蕾姆\033[0m（输入“\033[1;33mcall\033[0m”）!")
        return choise

    # 召唤系统助手
    def callming_sys_pet(self):
        print("\033[1;35m蕾姆\033[0m：\033[1;31m{name}\033[0m主人，您的异世界之旅伴侣\033[1;34m蕾姆\033[0m响应召唤而来！请问主人有什么吩咐？\n".format(
            name=self.Player.Name))
        time.sleep(1)
        choise = self.calling_sys_pet2()
        return choise

    # 召唤系统助手
    def calling_sys_pet2(self):
        print("""
                                继续游戏     Continue
                                保存游戏进度 Save
                                读取游戏进度 Load
                                退出游戏     Exit
                """)
        choise = input("\033[1;35m我\033[0m：")
        return choise

    # 系统助手选择
    def sys_pet(self, choise):
        while True:
            if choise == "Continue":
                print("\033[1;35m蕾姆\033[0m：好的，主人！下次有需要别忘记了召唤\033[1;34m蕾姆\033[0m（输入“\033[1;33mcall\033[0m”）!")
            elif choise == "Save":
                print("\033[1;35m蕾姆\033[0m：好的，主人！下次有需要别忘记了召唤\033[1;34m蕾姆\033[0m（输入“\033[1;33mcall\033[0m”）!")
            elif choise == "Load":
                print("\033[1;35m蕾姆\033[0m：好的，主人！下次有需要别忘记了召唤\033[1;34m蕾姆\033[0m（输入“\033[1;33mcall\033[0m”）!")
            elif choise == "Exit":
                print(
                    "\033[1;35m蕾姆\033[0m：\033[1;31m{name}\033[0m主人！您真的不想再玩一会儿吗？！……好吧，\033[1;34m蕾姆\033[0m帮您传送回去！好想能快点儿再次见到主人啊！……（\033[1;34m蕾姆\033[0m依依不舍，含着泪水把你传送了回去！）\n")
                self.game_exit()
            else:
                print("\033[1;35m蕾姆\033[0m：\033[1;31m{name}\033[0m主人！您的眼神儿不太好吧！怎么输入错了……请再输入一次！".format(
                    name=self.Player.Name))
                self.calling_sys_pet2()

    # 游戏进行中
    def MNRS_going_on(self):
        pass

    # 保存游戏进度
    def save(self, *args, **kwargs):
        pass

    # 读取游戏进度
    def load(self, *args, **kwargs):
        pass

    # 删除游戏进度
    def save_del(self, *args, **kwargs):
        pass

    # 删除游戏角色
    def role_del(self, *args, **kwargs):
        pass

    # 退出游戏
    def game_exit(self, *args, **kwargs):
        pass

    # \033[1;33mcall\033[0ming
    def __callm__(self):

        # 人生起步
        choise = self.MNRS_start()
        self.sys_pet(choise)


# 用户运行流程
class UserOnline(object):

    # 构造函数
    def __init__(self, users_info: str):
        self.UsersInfo = users_info

    # 登陆信息输入
    def __user_input(self):
        user = input("请输入您的用户名：\n")
        password = input("请输入您的密码：\n")
        return user, password

    # 用户登陆信息加载
    def __users_info_load(self):
        users_info_list = []
        with open(self.UsersInfo, "rb") as users_info_file:
            while True:
                try:
                    users_info_list.append(pickle.load(users_info_file))
                except EOFError:
                    break
            return users_info_list

    # 用户登陆判断
    def user_log_in(self):
        while True:
            user_input_info = self.__user_input()
            user = user_input_info[0]
            password = user_input_info[1]
            users_info_list = self.__users_info_load()
            for user_info in users_info_list:
                if user == user_info[0]:
                    if password == user_info[1]:
                        print("登陆成功！\n")
                        return
                    else:
                        print("您的密码有误！请重新输入！\n")
                        break
                else:
                    continue
            else:
                choise = input("您输入的用户名并不存在！请问是否注册！（y/n）\n")
                if choise == "y":
                    self.user_register()
                else:
                    pass

    # 用户注册
    def user_register(self):
        while True:
            user = input("请输入您的用户名：\n")
            password1 = input("请输入您的密码：\n")
            password2 = input("请再次输入您的密码：\n")
            if password1 != password2:
                print("您两次输入的密码不同，请重新输入！")
                continue
            else:
                print("恭喜您注册成功！\n")
                with open(self.UsersInfo, "ab") as users_info_file:
                    pickle.dump([user, password1], users_info_file)
                break


# 游戏运行流程
class GameOnline(UserOnline):

    # 构造函数
    def __init__(self, users_info: str, game_name: str):
        super(GameOnline, self).__init__(users_info)
        self.UsersInfo = users_info
        self.GameName = game_name

    # 开始游戏
    def game_start(self, *args, **kwargs):
        pass

    # 游戏角色创建
    def role(self, *args, **kwargs):
        pass

    # 保存游戏进度
    def save(self, *args, **kwargs):
        pass

    # 删除游戏进度
    def save_del(self, *args, **kwargs):
        pass

    # 删除游戏角色
    def role_del(self, *args, **kwargs):
        pass

    # 退出游戏
    def game_exit(self, *args, **kwargs):
        pass


# 模拟人生运行流程
class MNRSOnline(GameOnline):

    # 构造函数
    def __init__(self, users_info: str = r"..\data_files\customers_info_table.pk", game_name: str = "模拟人生"):
        super(MNRSOnline, self).__init__(users_info, game_name)

    # 游戏角色创建
    def role(self):
        print("欢迎登陆\033[1;31m" + self.GameName + "\033[0m!\n")
        name = input("请输入您的角色名：\n")
        birthday = input("请输入您的生日（mm-dd）：\n")
        while True:
            role_choise = "{role:^10}    {gender:^6}    {weight}kg    {height}cm    {hometown}"
            print()
            print(role_choise.format(role="Liz", gender="Female", weight=48, height=168, hometown="武汉"))
            print(role_choise.format(role="Peter", gender="Male", weight=58, height=178, hometown="北京"))
            print(role_choise.format(role="John Berry", gender="Male", weight=58, height=168, hometown="武汉"))
            print()
            role_choose = input("您想要体验谁的人生历程：Liz，Peter还是John Berry？\n")
            if role_choose == "Liz":
                print("对不起！您还不能体验该角色！请重新选择！")
                continue
            elif role_choose == "Peter":
                print("对不起！您还不能体验该角色！请重新选择！")
                continue
            elif role_choose == "John Berry":
                return "John Berry", name, birthday
            else:
                print("对不起！该角色尚不存在！请重新选择！")

    # 游戏开始
    def game_start(self, name, birthday, role_choose="John Berry"):
        if role_choose == "Liz":
            Liz = Person(name, birthday, "Female", 48, 168, "武汉")
            Peter = Person("Peter", "03-14", "Male", 58, 178, "北京")
            John = Person("John Berry", "10-08", "Male", 58, 168, "武汉")
            Game(Liz, Peter, John)()
        elif role_choose == "Peter":
            Liz = Person("Liz", "12-12", "Female", 48, 168, "武汉")
            Peter = Person(name, birthday, "Male", 58, 178, "北京")
            John = Person("John Berry", "10-08", "Male", 58, 168, "武汉")
            Game(Peter, Liz, John)()
        else:
            Liz = Person("Liz", "12-12", "Female", 48, 168, "武汉")
            Peter = Person("Peter", "03-14", "Male", 58, 178, "北京")
            John = Person(name, birthday, "Male", 58, 168, "武汉")
            Game(John, Liz, Peter)()

    # 游戏退出
    def game_end(self):
        pass

    # \033[1;33mcall\033[0ming
    def __call__(self):

        # 用户登陆判断
        self.user_log_in()

        # 游戏角色创建
        role_choose = self.role()

        # 游戏开始
        self.game_start(role_choose[0], role_choose[1], role_choose[2])


if __name__ == "__main__":
    your_simulated_life = MNRSOnline()
    your_simulated_life()
