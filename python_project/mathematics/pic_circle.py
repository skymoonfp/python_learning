#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""


**************************
文件:     pic_circle.py
 IDE：    PyCharm
创建时间： 2019/5/28 8:14
@author： skymoon
"""

from tkinter import *

if __name__ == "__main__":

    canvas = Canvas(width=800, height=600, bg='yellow')
    canvas.pack(expand=YES, fill=BOTH)
    k = 1
    j = 1
    for i in range(0, 26):
        canvas.create_oval(310 - k, 250 - k, 310 + k, 250 + k, width=1)
        k += j
        j += 0.3

    mainloop()
