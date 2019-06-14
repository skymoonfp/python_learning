#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""
1.执行一个循环，指定暂停位置信息（无须暂停请输入end）
2.输入end直接执行循环到最后
3.到达指定位置时暂停，并提示“已经到达……！”
4.询问是否继续
5.不继续则直接结束
6.继续则要求输入下一个暂停位置信息（无须暂停请输入end）
7.输入end直接执行循环到最后
8.（1）输入小于或者当前位置时，提示"您已经错过了该位置！当前位置是：……！"，并询问是否继续；（2）输入等于当前位置时，提示"您已经停在了该位置！"，并询问是否继续
9.不继续则直接结束
10.继续则要求输入下一个暂停位置信息（无须暂停请输入end）
"""

if __name__ == "__main__":
    pause_number = input("请问您想在什么位置暂停？\n")  # 第1步
    count = 0
    while count < 100000:
        if pause_number == "end":
            print("loop:", count)  # 第2步
        elif count == int(pause_number):
            print("已经到达%d！" % int(pause_number))  # 第3步
            choice = input("请问是否继续？(y/n)")  # 第4步
            if choice == "n":
                break  # 第5步
            else:
                while True:
                    pause_number = input("请问您下次想在什么位置暂停（无须暂停请输入end）？\n")  # 第6步
                    if pause_number == "end":
                        break  # 第7步，跳向第2步
                    else:
                        pause_number = int(pause_number)
                        if pause_number < count:
                            print("您已经错过了该位置！当前位置是：%d！" % count)  # 第8（1）步
                        elif pause_number == count:
                            print("您已经停在了该位置！")  # 第8（2）步
                        else:
                            break
                        choice = input("请问是否继续？(y/n)")
                        if choice == "n":
                            break  # 第9步（1）
                        else:
                            continue  # 第10步，跳向第6步
                if choice == "n":
                    break  # 第9步（2）
                else:
                    pass
        else:
            print("loop:", count)
        count += 1
