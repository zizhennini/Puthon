import turtle
wn = turtle.Screen()
turtle.bgcolor("black")
turtle.shape("turtle")
turtle.setup(1400,880)
tr = turtle.Turtle()
ts = turtle.Turtle()
tt = turtle.Turtle()
t2 = turtle.Turtle()
t3 = turtle.Turtle()
t4 = turtle.Turtle()
t5 = turtle.Turtle()
move = 1

#######################
t5.speed("fastest")
for i in range(10):
    for i in range(4):
        t5.pu()
        t5.goto(500,200)
        t5.pd()
        t5.color('cyan')
        t5.pensize(3)
        t5.circle(50,steps=4)
        t5.right(100)

t5.speed("fastest")
for i in range(6):
    for i in range(4):
        t5.pu()
        t5.goto(0,0)
        t5.pd()
        t5.color("light green")
        t5.circle(100,steps=6)
        t5.right(100)

t2.speed("fastest")
for i in range(10):
    for i in range(2):
        t2.pensize(5)
        t2.goto(170,0)
        t2.color("green")
        t2.forward(100)
        t2.right(60)
        t2.color("cyan")
        t2.forward(50)
        t2.right(120)
    t2.right(30)

tr.speed("fastest")
for i in range(10):
    for i in range(2):
        tr.pensize(7)
        tr.goto(-270,0)
        tr.color("purple")
        tr.forward(100)
        tr.circle(5,steps=4)
        tr.right(60)
        tr.color("violet")
        tr.forward(50)
        tr.right(120)
    tr.right(30)

ts.speed("fastest")
t5.speed("fastest")
for i in range(10):
    for i in range(4):
        t5.pu()
        t5.goto(-500,200)
        t5.pd()
        t5.color("yellow")
        t5.pensize(3)
        t5.circle(50,steps=4)
        t5.right(100)

    t5.speed("fastest")
for i in range(10):
    for i in range(4):
        t5.up()
        t5.goto(-500,-200)
        t5.pd()
        t5.color("white")
        t5.pensize(3)
        t5.circle(50,steps=3)
        t5.right(100)

t5.speed("normal")
    for i in range(10):
        for i in range(4):
            t5.pu()
            t5.goto(500,-200)
            t5.pd()
            t5.pd()
            t5.color("pink")
            t5.pensize(3)
            t5.circle(50,steps=3)
            t5.right(100)

for i in range(20):
    for i in range(2):
        ts.pensize(2)
        ts.goto(0,300)
        ts.color("red")
        ts.forward(100)
        ts.circle(6,steps=3)
        ts.right(70)
        ts.color("yellow")
        ts.forward(50)
        ts.right(120)
    ts.left(30)

ts.speed("fastest")
for i in range(20):
    for i in range(2):
        ts.pensize(2)
        ts.pu()
        ts.goto(0,-300)
        ts.color("pink")
        ts.pd()
        ts.forward(100)
        ts.circle(6,steps=3)
        ts.right(70)
        ts.color("orange")
        ts.forward(50)
        ts.right(120)
    ts.left(30)

t3.speed("fastest")
for i in range(10):
    for i in range(2):
        t3.pensize(3)
        t3.goto(-320,300)
        t3.color("light green")
        t3.begin_fill()
        t3.forward(30)
        t3.right(50)
        t3.color("green")
        t3.forward(50)
        t3.circle(5,steps=6)
        t3.right(120)
        t3.end_fill()
    t3.right(60)

t3.speed("fastest")
for i in range(10):
    for i in range(2):
        t3.pensize(3)
        t3.pu()
        t3.goto(320,-300)
        t3.pd()
        t3.color("red")
        t3.begin_fill()
        t3.forward(30)
        t3.right(50)
        t3.color("orange")
        t3.forward(50)
        t3.circle(5,steps=6)
        t3.right(120)
        t3.end_fill()
    t3.right(100)

t3.speed("fastest")
for i in range(10):
    for i in range(2):
        t3.pensize(3)
        t3.up()
        t3.goto(320,300)
        t3.pd()
        t3.color("light blue")
        t3.begin_fill()
        t3.forward(30)
        t3.right(50)
        t3.color("blue")
        t3.forward(50)
        t3.circle(5,steps=6)
        t3.right(120)
        t3.end_fill()
    t3.right(60)

t3.speed("fastest")
for i in range(10):
    for i in range(2):
        t3.pensize(3)
        t3.pu()