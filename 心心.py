from itertools import cycle
from turtle import *
from colorsys import *


def curve():
    for _ in range(200):
        right(1)
        forward(1)


speed(0)
pensize(3)
bgcolor("black")

cycle_number = 2
s = 1
for _ in range(cycle_number):
    for i in range(36):
        # 使用单一颜色，如果您需要渐变色，请考虑其他实现方式
        pencolor("#C90055")
        fillcolor(hsv_to_rgb(0.92, s, 1))
        begin_fill()
        forward(111.65)
        curve()
        left(120)
        curve()
        forward(111.65)
        end_fill()
        hideturtle()
        right(90)
        s -= 0.02
done()
