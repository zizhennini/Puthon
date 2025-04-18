import turtle as t
def flag(x,y):
    t.up()
    t.goto(x,y)
    t.down()
    t.color("red")
    t.bdgin_fill()
    for i in range(4):
        if i % 2 ==0:
            t.forward(300)
        else:
            t.forward(200)
        t.left(90)
    t.end_fill()

def star(x):
    t.color("yellow")
    t.begin_fill()
    for i in range(5):
        t.forward(x)
        t.right(144)
    t.end_fill()

def bigstar(x,y):
    t.up()
    t.goto(x,y)
    t.down()
    star(35)

def littlestar(x,y,single):
    '''single代表小五角星旋转的角度，以保证小五角星的一个角正对大五角星中心'''
    t.up()
    t.goto(x,y)
    t.left(single)
    t.down()
    star(14)

flag(-500,-100)
bigstar(-130,60)
littlestar(-60,75,30)
littlestar(-40,50,60)
littlestar(-38,22,30)
littlestar(-50,8,60)
t.hideturtle()
t.done()


