import turtle
import datetime
import random

 # 设置屏幕
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("新年倒计时")


# 绘制烟花
def draw_firework(x,y):
    colors = ["green","orange","yellow","green","blue","purple"]
    for color in colors:
        turtle.pensize(color)
        turtle.goto(x,y)
        turtle.pendown()
        for _ in range(20):
            turtle.forward(162)
            turtle.right(162)
        turtle.penup()

# 绘制烟花
def draw_firework(x, y):
    colors = ["green", "orange", "yellow", "green", "blue", "purple"]
    for color in colors:
        turtle.pencolor(color)
        turtle.goto(x, y)
        turtle.pendown()
        for _ in range(20):
            turtle.forward(162)
            turtle.right(162)
        turtle.penup()


# 绘制气球
def draw_balloon(x, y):
    turtle.pencolor("pink")
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(20)
    turtle.end_fill()
    turtle.pencolor("gray")  # 更改画笔颜色为灰色
    turtle.goto(x, y + 30)
    turtle.pendown()
    turtle.right(45)
    turtle.forward(40)
    turtle.penup()


# 倒计时函数
def countdown():
    new_year = datetime.datetime.now().replace(year=datetime.datetime.now().year + 1, month=1, day=1, hour=0, minute=0,
                                               second=0, microsecond=0)
    while True:
        now = datetime.datetime.now()
        time_left = new_year - now
        if time_left.total_seconds() <= 0:  # 确保倒计时归零后再执行最后一次显示
            break
        day = time_left.days
        hours, remainder = divmod(time_left.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        countdown_text = f"距离新年还有：{day} 天 {hours:02d}:{minutes:02d}:{seconds:02d}"
        turtle.clear()
        turtle.pencolor("white")
        turtle.penup()
        turtle.goto(0, -100)
        turtle.write(countdown_text, align="center", font=("Arial", 24, "normal"))

        # 在倒计时结束前显示一次烟花
        if day == 0 and hours == 0 and minutes == 0:
            for _ in range(5):
                x = random.randint(-200, 200)
                y = random.randint(-100, 100)
                draw_firework(x, y)
            turtle.update()  # 确保更新屏幕显示
            break  # 倒计时结束后退出循环
        turtle.update()  # 确保更新屏幕显示


# 隐藏海龟图标
turtle.hideturtle()

# 启动倒计时
countdown()

# 保持窗口显示
turtle.done()


