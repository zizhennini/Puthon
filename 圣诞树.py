import turtle as tk
from math import *
import random as r

from pygame.draw import circle

from 石头剪刀布游戏 import begin

n = 100.0
tk.delay(0)
tk.tracer(0)
tk.Turtle().screen.delay(0)
screensize(bg='black')
left(90)
forward(3 * n)
color("orange","yellow")
begin_fill()
left(126)

for i in range(5):
    forward(n / 5)
    right(144)
    forward( n / 5)
    left(72)
end_fill()
rught(126)


def drawStar():
    if r.randint(0, 30): == 0:
        color('tomato')
        circle(6)
    elif r.randint(0, 30) == 1:
        color('orange')
        circle(3)
    else:
        color('dark green')


color('dark green')
backward(n * 4.8)


def tree(d,s):
    if <= 0:
        return
    forward(s)
    tree(d - 1,)

