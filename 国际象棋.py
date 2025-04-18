from turtle import *

def draw_b4():
    for i in range(4):
        fd(50)
        rt(90)
    fd(50)

def go(x,y):
    up()
    goto(x,y)
    down()

bgcolor('lightyellow')
speed(0)
hideturtle() 

x = -200
y = 150
for k in range(4):
    go(x,y)
    for j in range(4):
        draw_b4()
        begin_fill()
        draw_b4()
        end_fill()
    y -= 50
    go(x,y)
    for j in range(4):
        begin_fill()
        draw_b4()
        end_fill() 
        draw_b4()
    y -= 50

x = -200-20
y = 150-35
for d in range(2):
    for u in range(8,0,-1):
        go(x,y)
        write(u, font = ('宋体', 15))
        y -= 50
        x = -200 + 8 * 50 + 10
        y = 150-35


x = -200 + 20
y = 150 + 5
for s in range(2):
    for g in range(97,97+8):
        go(x,y)
        write(chr(g).upper(), font = ('宋体', 15))
        x += 50
        x = -200 +20
        y = 150 - 8*50 - 25

go(0, 220)
write('国际象棋棋盘', align = 'center', font = ('楷体', 30 , 'bold'))


go(-130, 215)
seth(0)
for i in range(6):
    fd(23.5)
    up()
    fd(23.5)
    down()

pensize(5)
go(-130, 210)
fd(260)

done()
# ...
x = -200 + 20
y = 150 - 5  # Adjust starting y-position for alignment
for s in range(2):
    for g in range(65, 65+8):  # Change to ASCII A-H
        go(x,y)
        write(chr(g), font = ('宋体', 15))  # No need for .upper() as we start from 'A'
        x += 50
    x = -200 + 20  # Reset x for the next row
    y -= 50 * 2  # Move down two squares for the next row

x = -200 - 20  # Start x-position for numbers
y = 150 - 35  # Reset y-position to the top
for d in range(2):
    for u in range(8, 0, -1):  # Corrected range for numbers 8 to 1
        go(x,y)
        write(u, font = ('宋体', 15))
        y -= 50  # Move down one square
    x = -200 + 8 * 50 + 20  # Increment x-position to the right side for the next column

go(-130, 215)
# ...