#螺旋曲线
from turtle import *    #导入绘图模块
bgcolor('lightyellow')  #背景颜色设为亮黄色
pencolor('purple')      # 设置笔的颜色
pensize(2)              #设置笔尺寸
speed('fastest')        # 设置最快画图速度

for i in range(2000):   # 循环2000次以获得更细腻的螺旋
    forward(2*i)        #每次向前移动2倍的i
    left(91)            #向左旋转91度

done()                  #保持窗口在最前
left(91)                # 向左旋转91度