import random
import turtle


class BackGround(turtle.Turtle):  # 定义一个类，用来画除了数字方块之外的图形
    block_pos = [(-150, 110), (-50, 110), (50, 110), (150, 110),
                 (-150, 10), (-50, 10), (50, 10), (150, 10),
                 (-150, -90), (-50, -90), (50, -90), (150, -90),
                 (-150, -190), (-50, -190), (50, -190), (150, -190)]

    def __init__(self):
        super().__init__()
        self.penup()
        self.ht()
        self.text_is_clear = True  # 用来判断失败或成功的提示文字是否有被清除，不清除不能继续移动方块
        self.top_score = 0  # 游戏最高分
        self.turtle_show_score = turtle.Turtle()
        self.turtle_show_text = turtle.Turtle()
        with open('.\\score.txt', 'r') as f:
            try:
                self.top_score = int(f.read())  # 读取score中的数据
            except:
                self.top_score = 0
        self.draw_back_ground()  # 实例画出游戏的背景

    def draw_back_ground(self):
        self.shape('block.gif')  # 画出背景方块
        for i in self.block_pos:
            self.goto(i)
            self.stamp()
        self.color('white', 'white')  # 画出其他背景
        self.goto(-210, 172)
        self.begin_fill()
        self.goto(215, 172)
        self.goto(215, 162)
        self.goto(-215, 162)
        self.end_fill()
        self.shape('score.gif')
        self.goto(-120, 210)
        self.stamp()
        self.shape('top.gif')
        self.goto(115, 210)
        self.stamp()

    def show_score(self, score):  # 分值的显示
        if score > self.top_score:
            self.top_score = score
            with open('.\\score.txt', 'w') as f:
                f.write(f'{self.top_score}')
            self.turtle_show_score.penup()
            self.turtle_show_score.ht()
            self.turtle_show_score.color('white')
            self.turtle_show_score.goto(-120, 175)
            self.turtle_show_score.clear()
            self.turtle_show_score.write(f'{score}', align='center', font=('Arial', 20, 'bold'))
            self.turtle_show_score.goto(115, 175)
            self.turtle_show_score.write(f'{self.top_score}', align='center', font=('Arial', 20, 'bold'))

    def show_win_lose(self, win):
        self.turtle_show_text.color('blue')
        self.turtle_show_text.penup()
        self.turtle_show_text.ht()
        if win:
            self.turtle_show_text.write('     Win！2048\n重玩请按空格键', align='center', font=('黑体', 30, 'bold'))
            self.text_is_clear = False
        else:
            self.turtle_show_text.write('     GAME OVER\n重新开始请按空格键', align='center', font=('黑体', 30, 'bold'))
            self.text_is_clear = False


class Block(turtle.Turtle):  # 数字方块类
    def __init__(self):
        super().__init__()
        self.ht()
        self.penup()
        self.num = 0

    def draw(self):
        self.clear()
        dic_draw = {2: '#eee6db', 4: '#efe0cd', 8: '#f5af7b',
                    16: '#fb9660', 32: '#f57d5a', 64: '#f95c3d',
                    128: '#eccc75', 256: '#eece61', 512: '#efc853',
                    1024: '#ebc53c', 2048: '#eec430', 4096: '#aeb879',
                    8192: '#aab767', 16384: '#a6b74f'}
        if self.num > 0:  # 数字大于0，画出方块
            self.color(f'{dic_draw[self.num]}')  # 选择颜色
            self.begin_fill()
            self.goto(self.xcor() + 48, self.ycor() + 48)
            self.goto(self.xcor() - 96, self.ycor())
            self.goto(self.xcor(), self.ycor() - 96)
            self.goto(self.xcor() + 96, self.ycor())
            self.goto(self.xcor(), self.ycor() + 96)
            self.end_fill()
            self.goto(self.xcor() - 48, self.ycor() - 68)
            if self.num > 4:  # 按照数字选择数字的颜色
                self.color('white')
            else:
                self.color('#6d6058')
            self.write(f'{self.num}', align='center', font=('Arial', 27, 'bold'))
            self.goto(self.xcor(), self.ycor() + 20)


class Game:

    def __init__(self):
        self.background = BackGround()
        self.score = 0  # 游戏得分
        self.is_win = True  # 达成2048的判断，让达成的文字仅出现一次
        self.block_turtle_dict = {}  # 放数字方块海龟的字典，位置坐标为key,对应海龟为value
        for i in BackGround.block_pos:  # 画出16个海龟对应16个数字块
            block = Block()
            block.goto(i)
            self.block_turtle_dict[i] = block
            self.new_num()

    def check_win_lose(self):  # 游戏失败及达成2048的提示文字
        judge = 0  # 判断是否还有位置可以移动
        for i in self.block_turtle_dict.values():
            for j in self.block_turtle_dict.values():
                if i.num == 0 or i.num == j.num and i.distance(j) == 100:
                    judge += 1
        if judge == 0:  # 无位置可移动，游戏失败
            self.background.show_win_lose(False)
        if self.is_win is True:  # 此条件让2048达成的判断只能进行一次
            for k in self.block_turtle_dict.values():
                if k.num == 2048:  # 游戏达成
                    self.is_win = False
                    self.background.show_win_lose(True)

    def new_num(self):  # 随机出现一个2或4的数字块
        block_list = []
        for i in BackGround.block_pos:
            if self.block_turtle_dict[i].num == 0:
                block_list.append(self.block_turtle_dict[i])  # 挑出空白方块的海龟
        turtle_choice = random.choice(block_list)  # 随机选中其中一个海龟
        turtle_choice.num = random.choice([2, 2, 2, 2, 4])  # 赋属性num=2/4
        turtle_choice.draw()
        self.background.show_score(self.score)
        self.check_win_lose()

    def move_up(self):
        allpos1 = BackGround.block_pos[::4]  # 切片为四列
        allpos2 = BackGround.block_pos[1::4]
        allpos3 = BackGround.block_pos[2::4]
        allpos4 = BackGround.block_pos[3::4]
        self.do_move(allpos1, allpos2, allpos3, allpos4)

    def move_down(self):
        allpos1 = BackGround.block_pos[-4::-4]
        allpos2 = BackGround.block_pos[-3::-4]
        allpos3 = BackGround.block_pos[-2::-4]
        allpos4 = BackGround.block_pos[-1::-4]
        self.do_move(allpos1, allpos2, allpos3, allpos4)

    def move_left(self):
        allpos1 = BackGround.block_pos[:4]
        allpos2 = BackGround.block_pos[4:8]
        allpos3 = BackGround.block_pos[8:12]
        allpos4 = BackGround.block_pos[12:16]
        self.do_move(allpos1, allpos2, allpos3, allpos4)

    def move_right(self):
        allpos1 = BackGround.block_pos[-1:-5:-1]
        allpos2 = BackGround.block_pos[-5:-9:-1]
        allpos3 = BackGround.block_pos[-9:-13:-1]
        allpos4 = BackGround.block_pos[-13:-17:-1]
        self.do_move(allpos1, allpos2, allpos3, allpos4)

    def do_move(self, allpos1, allpos2, allpos3, allpos4):
        if self.background.text_is_clear is True:
            count1 = self.move(allpos1)  # 四列或四行依次移动
            count2 = self.move(allpos2)
            count3 = self.move(allpos3)
            count4 = self.move(allpos4)
            if count1 or count2 or count3 or count4:  # 判断是否有方块移动，有才能继续出现新的数字块
                self.new_num()

    def move(self, pos_list):
        num_list = []  # 为某一列或行的数字块海龟的坐标
        for i in pos_list:
            num_list.append(self.block_turtle_dict[i].num)  # 把这些海龟的NUM形成list
        new_num_list, count = self.num_list_opr(num_list)  # 只是list_oper的方法形成新的list
        for j in range(len(new_num_list)):  # 把新的list依次赋值给对应的海龟.num属性并调用draw()方法
            self.block_turtle_dict[pos_list[j]].num = new_num_list[j]
            self.block_turtle_dict[pos_list[j]].draw()
        return count

    def num_list_opr(self, num_list):  # num_list的操作，假设其为【2,0,2,2】
        count = True
        temp = []
        new_temp = []
        for j in num_list:
            if j != 0:
                temp.append(j)  # temp=[2,2,2]
        flag = True
        for k in range(len(temp)):
            if flag:
                if k < len(temp) - 1 and temp[k] == temp[k + 1]:
                    new_temp.append(temp[k] * 2)
                    flag = False
                    self.score += temp[k]
                else:
                    new_temp.append(temp[k])  # new_temp=[4,2]
            else:
                flag = True
        for m in range(len(num_list) - len(new_temp)):
            new_temp.append(0)  # new_temp=[4,2,0,0]
        if new_temp == num_list:
            count = False  # 此变量判断num_list没有变化，数字块无移动
        return new_temp, count

    def restart(self):  # 重开游戏的方法
        self.score = 0
        for i in self.block_turtle_dict.values():
            i.num = 0
            i.clear()
        self.background.turtle_show_score.clear()
        self.background.turtle_show_text.clear()
        self.background.text_is_clear = True  # 此flag为游戏达成或失败出现提示语后的判断，要提示语被clear后才能继续move
        self.new_num()


if __name__ == '__main__':
    game_window = turtle.Screen()  # 创建游戏主窗口
    game_window.setup(410, 500, 400, 20)  # 设置主窗口的大小和位置。
    game_window.bgcolor('gray')  # 设置主窗口背景颜色。
    game_window.title('2048')  # 设置主窗口的标题。
    game_window.tracer(0)  # 关闭乌龟动画。
    game_window.register_shape('block.gif')  # 注册海龟形状，将形状加入 TurtleScreen 的形状列表。
    game_window.register_shape('score.gif')
    game_window.register_shape('top.gif')
    game = Game()  # 创建游戏实例
    game_window.listen()  # 开启事件监听
    game_window.onkey(game.move_up, 'Up')  # 向上键监听响应事件，当敲击向上键时，调用game.moveUp方法进行处理
    game_window.onkey(game.move_down, 'Down')
    game_window.onkey(game.move_left, 'Left')
    game_window.onkey(game.move_right, 'Right')
    game_window.onkey(game.restart, 'space')
    game_window.mainloop()  # 开始事件循环