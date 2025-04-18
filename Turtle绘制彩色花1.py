#彩色花心1
from turtle import *
speed(0)
color1 = ['red', 'yellow', 'green', 'blue']

d = 20
for i in range(200):  # Combining loops for efficiency and color cycling
    pencolor(color1[i])
    for i in range(200):
        fd(d)
        left(170)
        d += 20
done()
