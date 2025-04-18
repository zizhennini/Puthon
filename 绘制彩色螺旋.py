import turtle
import random
# 创建一个画布
screen = turtle.Screen()
screen.bgcolor("black")
# 创建一个海龟对象
pen = turtle.Turtle()
pen.speed(0)
turtle.colormode(255)   #设置颜色模式为RGB
# 绘制彩色螺旋
for i in range(36):
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    pen.color(r,g,b)
    pen.circle(100)
    pen.right(10)
#完成绘制后隐藏海龟
pen.hideturtle()
# 保持窗口打开
turtle.done()

