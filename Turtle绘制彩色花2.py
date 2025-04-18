#彩色花3
from turtle import *
speed(0)
color1 = ['red','purple', 'yellow','green','blue']

d = 20
for i in range(5):
    pencolor(color1[i])
    for i in range(200):
        fd(d)
        left(175)
        d +=20
    #画笔复位
    goto(0,0)   #画笔到达坐标为x=0，y=0的位置
    d=20
done()