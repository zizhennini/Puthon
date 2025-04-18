import turtle

ms = turtle.Screen()
ms.setup(650,650,200,0)
ms.title('推箱子游戏')
ms.bgcolor("yellow")
ms.register_shape('wall.gif')
ms.register_shape('o.gif')
ms.register_shape('p.gif')
ms.register_shape('box.gif')
ms.register_shape('boxc.gif')
ms.tracer(0)

class Pen(turtle.Turtle):
    def __init__(self,pic):
        super().__init__()
        self.shape(pic)
        self.penup()
    def move(self,x,gx,y,gy):
        gox = x+gx
        goy = y+gy
        or_box = False
        if (gox,goy) in list_space:
            for i in list_box:
                if i.pos()==(gox,goy):
                    or_box = True
                    gox2,goy2 = x+gx*2,y+gy*2
                    if (gox2,goy2) in list_space:
                        self.goto(gox,goy)
                        i.goto(x+gx*2,y+gy*2)
                        if (gox2,goy2) in list_point:
                            i.shape("boxc.gif")
                        else:
                            i.shape("box.gif")
            if or_box==False:self.goto(gox,goy)
    def go_up(self):
        self.move(self.xcor(),+0,self.ycor(),+50)

    def go_down(self):
        self.move(self.xcor(),+0,self.ycor(),-50)

    def go_left(self):
        self.move(self.xcor(),-50,self.ycor(),+0)

    def go_right(self):
        self.move(self.xcor(),+50,self.ycor(),+0)

class Game():
    def show(self):
        for i in range(8):
            for j in range(8):
                x = -175 + j*50
                y = 175 - i*50
                if level_1[i][j] == "":
                    list_space.append((x,y))
                elif level_1[i][j] == 'X':
                    wall.goto(x,y)
                    wall.stamp()
                elif level_1[i][j] == 'O':
                    list_space.append((x,y))
                    box.goto(x,y)
                    box.stamp()
                    list_point.append((x,y))
                elif level_1[i][j] == 'P':
                    player.goto(x,y)
                    list_space.append((x,y))
                elif level_1[i][j] == 'B':
                    box1 = Pen('box.gif')
                    box1.goto(x,y)
                    list_space.append((x,y))
                    list_box.append(box1)
level_1 = [
    'CCXXXCCC',
    'CCXOXCCC',
    'CCX XXXX',
    'XXXB BOX',
    'XO BPXXX',
    'XXXXBXCC',
    'CCCXOXCC',
    'CCCXXXCC']

list_box = []
list_space = []
list_point = []
wall = Pen('wall.gif')
box = Pen('o.gif')
player = Pen('p.gif')

game = Game()

game.show()
ms.listen()
ms.onkey(player.go_up,"Up")
ms.onkey(player.go_left,"Left")
ms.onkey(player.go_down,"Down")
ms.onkey(player.go_right,"Right")

while True:
    ms.update()
ms.mainloop()