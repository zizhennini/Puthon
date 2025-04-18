import turtle


def draw_koch_snowflake(order, size):
    def koch_curve(t, order, size):
        if order == 0:
            t.forward(size)
        else:
            for angle in [60, -120, 60, 0]:
                koch_curve(t, order - 1, size / 3)
                t.left(angle)

    # 创建一个画布
    screen = turtle.Screen()
    screen.bgcolor("white")

    # 创建一个海龟对象
    pen = turtle.Turtle()
    pen.speed(0)
    pen.penup()
    pen.goto(-200, 0)
    pen.pendown()

    # 绘制分型雪花
    for _ in range(3):
        koch_curve(pen, order, size)
        pen.right(120)

    # 完成绘制后隐藏海龟
    pen.hideturtle()

    # 保持窗口打开，确保所有绘制操作完成后再结束
    turtle.done()


# 调用函数绘制雪花
draw_koch_snowflake(4, 400)
