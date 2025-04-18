from turtle import *
bgcolor('lightyellow')
speed(0)
pensize(2)
colors = ['red', 'blue', 'green','purple']
up()

d = 30
for j in range(6):
    for i in range(210):
        forward(3*i)
        pencolor(colors[i % 4])
        write(i)
        left(d)
    goto(0,0)
    clear()
    d+=31
done()