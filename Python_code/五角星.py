#!/usr/bin/env python3
# -*- coding:utf-8 -*-


from turtle import Turtle

p = Turtle()
p.speed(3)
p.pensize(5)
p.color("red", "black")
p.begin_fill()
for i in range(5):
    p.forward(200)
    p.right(144)
p.end_fill()
