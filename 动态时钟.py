from turtle import *
import datetime

def kedu():
    """说明画刻度"""
penup()
goto(0,0)
pendown()
for i in range(60):
    if i % 5 == 0:
        penup()
        forward(195)
        pendown()
        forward(15)
    else:
        penup()
        forward(203)
        pendown()
        forward(7)
    penup()
    goto(0,0)
    left(360/60)

def biaopan():
    """画表盘"""
    penup()
    goto(0,-220)
    pendown()
    seth(0)
    fillcolor("lavender")
    begin_fill()
    circle(200)
    end_fill()

def shizi():
    seth(98)
    penup()
    goto(0,0)
    forward(150)
    write(12,font=("宋体",30))

    seth(186)
    penup()
    goto(0,0)
    forward(170)
    write(9, font=("宋体",30))

    seth(268)
    penup()
    goto(0,0)
    forward(190)
    write(6, font=("宋体",30))

    seth(-8)
    penup()
    goto(0, 0)
    forward(163)
    write(3, font=("宋体", 30))

def zhizhen():
    """"功能：画指针"""
    pen1.penup()
    pen1.goto(0,0)
    pen1.pendown()

    pen1.pensize(10)
    pen1.seth(90)
    pen1.right(h * 6 * 5)
    pen1.forward(75)

    # 分针
    pen1.penup()
    pen1.goto(0,0)
    pen1,pendown()

    pen1.pensize(5)
    pen1.seth(90)
    pen1.right(m * 5)
    pen1.forward(100)

    # 秒钟
    pen1.penup()
    pen1.goto(0, 0)
    pen1, pendown()

    pen1.pencolor('red')
    pen1.pensize(2)
    pen1.seth(90)
    pen1.right(s * 6)
    pen1.forward(130)
    
    # 黑螺母
    pen1.penup()
    pen1.goto(0, 0)
    pen1.pendown()

    pen1.pencolor('black')
    pen1.dot(15)


# 初始化
tracer(0)
bgcolor("LightCyan")
speed(0)
seth(90)
pensize(2)
hideturtle()

biaopan()  # 画表盘
kedu()  # 画刻度
shuzi()  # 写数字

pen1 = Turtle()
while True:
    update()
    pen1.clear()
    now = datetime.datetime.now()
    zhizhen(now.hour,now.minute,now.second)  # 画指针

done()
    