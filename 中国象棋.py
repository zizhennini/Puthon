from turtle import *

# tracer(10)  # 加速显示，想看绘制过程可给此行加注释
speed(0)   #想看效果可取消这行注释，慢速
pensize(2)
width = 60
screensize(10 * width, 12 * width)
setup(width=10 * width, height=12 * width)
x, y = -4 * width, -4 * width

makerX = [x + width, x + 7 * width, x + width, x + 7 * width]
makerY = [y + 2 * width, y + 2 * width, y + 7 * width, y + 7 * width]
list = [['車', '馬', '相', '仕', '帅', '仕', '相', '馬', '車', '兵', '砲'],
        ['車', '馬', '象', '士', '将', '士', '象', '馬', '車', '卒', '炮']]
fontColor = ['red', 'green']


# 绘制棋盘
def drawChessboard(x, y, width):
    home()
    penup()
    goto(x - width // 5, y - width // 5)
    pendown()
    fillcolor('orange')
    begin_fill()
    for i in range(2):
        forward(8 * width + 2 * width // 5)
        left(90)
        forward(9 * width + 2 * width // 5)
        left(90)
    end_fill()
    penup()
    for i in range(10):
        goto(x, y + i * width)
        pendown()
        forward(8 * width)
        penup()
    left(90)
    for i in range(9):
        goto(x + i * width, y)
        pendown()
        forward(4 * width)
        penup()
        forward(width)
        pendown()
        forward(4 * width)
        penup()


# 绘制帅营
def drawCamp(x, y, width):
    home()
    goto(x + 3 * width, y)
    left(45)
    pendown()
    forward(2 ** 0.5 * width * 2)
    penup()
    goto(x + 3 * width, y + 2 * width)
    right(90)
    pendown()
    forward(2 ** 0.5 * width * 2)
    penup()


# 绘制标记

def drawMark(x, y):
    home()
    penup()
    goto(x - 9, y + 3)
    for i in range(4):
        pendown()
        forward(6)
        left(90)
        forward(6)
        right(90)
        penup()
        forward(6)
        pendown()
        right(90)
        penup()


def dMarker():
    for i in range(4):
        drawMark(makerX[i], makerY[i])
    for i in range(5):
        drawMark(x + 2 * i * width, y + 3 * width)
        drawMark(x + 2 * i * width, y + 6 * width)


# 绘制圆
def drawCircle(radius):
    pensize(3)
    begin_fill()
    fillcolor('white')
    circle(radius)
    end_fill()


# 写字
def drawWrite(x, fontColor):
    color(fontColor)
    write(x, font=('隶书', width // 2, 'normal'))


# 绘制字
def dWrite():
    home()
    goto(x + 7 / 4 * width, y + 17 / 4 * width)
    pendown()
    color("green")
    write("楚  河  汉  界", font=('隶书', width // 2, 'normal'))
    penup()
    for j in range(2):
        for i in range(9):  # 写主字
            penup()
            goto(x + i * width, y - 1 / 4 * width + 9 * j * width)
            pendown()
            pencolor(fontColor[j])
            drawCircle(1 / 3 * width)
            penup()
            goto(x + i * width - 1 / 3 * width, y - 1 / 4 * width + 9 * j * width)
            pendown()
            drawWrite(list[j][i], fontColor[j])

        for i in range(5):  # 写兵卒
            penup()
            goto(x + 2 * i * width, y + 3 * width - 1 / 4 * width + 3 * j * width)
            pendown()
            pencolor(fontColor[j])
            drawCircle(1 / 3 * width)
            penup()
            goto(x + 2 * i * width - 1 / 3 * width, y + 3 * width - 1 / 4 * width + 3 * j * width)
            pendown()
            drawWrite(list[j][9], fontColor[j])
        for i in range(2):  # 写炮
            penup()
            goto(x + width + 6 * i * width, y + 2 * width - 1 / 4 * width + j * 5 * width)
            pendown()
            pencolor(fontColor[j])
            drawCircle(1 / 3 * width)
            penup()
            goto(x + 2 / 3 * width + 6 * i * width, y + 2 * width - 1 / 4 * width + j * 5 * width)
            pendown()
            drawWrite(list[j][10], fontColor[j])


drawChessboard(x, y, width)
for i in range(2):
    drawCamp(x, y, width)
    drawCamp(x, y + 7 * width, width)
dMarker()
dWrite()
hideturtle()
update()  # 刷新
done()
