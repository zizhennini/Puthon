#螺旋曲线彩色

from turtle import *
bgcolor('lightyellow')
pensize(2)
speed(0)
#设置颜色的列表
colors = ['red','blue','purple','green']
for i in range(1000):
    forward(2*i)
    pencolor(colors[i % 4])
    left(360/4+1)
done()
    