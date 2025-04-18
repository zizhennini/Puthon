import random
import turtle


class BackGround(turtle.Turtle):
    block_pos = [(-150, 110), (-50, 110), (50, 110), (150, 110),
                 (-150, 10), (-50, 10), (50, 10), (150, 10),
                 (-150, -90), (-50, -90), (50, -90), (150, -90),
                 (-150, -190), (-50, -190), (50, -190), (150, -190)]

    def __init__(self):
        super().__init__()
        self.penup()
        self.ht()
        self.text_is_clear = True
        self.top_score = 0
        self.turtle_show_score = turtle.Turtle()
        self.turtle_show_text = turtle.Turtle()
        try:
            with open('score.txt', 'r') as f:
                self.top_score = int(f.read())
        except (FileNotFoundError, ValueError):
            self.top_score = 0
        self.draw_back_ground()

    def draw_back_ground(self):
        self.shape('block.gif')
        for i in self.block_pos:
            self.goto(i)
            self.stamp()
        self.color('white', 'white')
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

    def show_score(self, score):
        if score > self.top_score:
            self.top_score = score
            with open('score.txt', 'w') as f:
                f.write(str(self.top_score))
            self.turtle_show_score.penup()
            self.turtle_show_score.ht()
            self.turtle_show_score.color('white')
            self.turtle_show_score.goto(-120, 175)
            self.turtle_show_score.clear()
            self.turtle_show_score.write(str(score), align='center', font=('Arial', 20, 'bold'))
            self.turtle_show_score.goto(115, 175)
            self.turtle_show_score.write(str(self.top_score), align='center', font=('Arial', 20, 'bold'))

    def show_win_lose(self, win):
        self.turtle_show_text.color('blue')
        self.turtle_show_text.penup()
        self.turtle_show_text.ht()
        if win:
            self.turtle_show_text.write('     Win！2048\n重玩请按空格键', align='center', font=('黑体', 30, 'bold'))
        else:
            self.turtle_show_text.write('     GAME OVER\n重新开始请按空格键', align='center', font=('黑体', 30, 'bold'))
        self.text_is_clear = False


class Block(turtle.Turtle):
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
        if self.num > 0:
            self.color(dic_draw[self.num])
            self.begin_fill()
            self.goto(self.xcor() + 48, self.ycor() + 48)
            self.goto(self.xcor() - 96, self.ycor())
            self.goto(self.xcor(), self.ycor() - 96)
            self.goto(self.xcor() + 96, self.ycor())
            self.goto(self.xcor(), self.ycor() + 96)
            self.end_fill()
            self.goto(self.xcor() - 48, self.ycor() - 68)
            if self.num > 4:
                self.color('white')
            else:
                self.color('#6d6058')
            self.write(str(self.num), align='center', font=('Arial', 27, 'bold'))
            self.goto(self.xcor(), self.ycor() + 20)


class Game:
    def __init__(self):
        self.background = BackGround()
        self.score = 0
        self.is_win = True
        self.block_turtle_dict = {}
        for i in BackGround.block_pos:
            block = Block()
            block.goto(i)
            self.block_turtle_dict[i] = block
        # 初始随机生成两个数字方块
        self.new_num()
        self.new_num()

    def check_win_lose(self):
        judge = 0
        for i in self.block_turtle_dict.values():
            for j in self.block_turtle_dict.values():
                if i.num == 0 or (i.num == j.num and i.distance(j) == 100):
                    judge += 1
        if judge == 0:
            self.background.show_win_lose(False)
        if self.is_win:
            for k in self.block_turtle_dict.values():
                if k.num == 2048:
                    self.is_win = False
                    self.background.show_win_lose(True)

    def new_num(self):
        block_list = [block for block in self.block_turtle_dict.values() if block.num == 0]
        if block_list:
            turtle_choice = random.choice(block_list)
            turtle_choice.num = random.choice([2, 2, 2, 2, 4])
            turtle_choice.draw()
            self.background.show_score(self.score)
            self.check_win_lose()

    def get_positions(self, direction):
        if direction == 'up':
            return [BackGround.block_pos[::4], BackGround.block_pos[1::4], BackGround.block_pos[2::4], BackGround.block_pos[3::4]]
        elif direction == 'down':
            return [BackGround.block_pos[-4::-4], BackGround.block_pos[-3::-4], BackGround.block_pos[-2::-4], BackGround.block_pos[-1::-4]]
        elif direction == 'left':
            return [BackGround.block_pos[:4], BackGround.block_pos[4:8], BackGround.block_pos[8:12], BackGround.block_pos[12:16]]
        elif direction == 'right':
            return [BackGround.block_pos[-1:-5:-1], BackGround.block_pos[-5:-9:-1], BackGround.block_pos[-9:-13:-1], BackGround.block_pos[-13:-17:-1]]

    def move_up(self):
        self.do_move(*self.get_positions('up'))

    def move_down(self):
        self.do_move(*self.get_positions('down'))

    def move_left(self):
        self.do_move(*self.get_positions('left'))

    def move_right(self):
        self.do_move(*self.get_positions('right'))

    def do_move(self, allpos1, allpos2, allpos3, allpos4):
        if self.background.text_is_clear:
            count1 = self.move(allpos1)
            count2 = self.move(allpos2)
            count3 = self.move(allpos3)
            count4 = self.move(allpos4)
            if count1 or count2 or count3 or count4:
                self.new_num()

    def move(self, pos_list):
        num_list = [self.block_turtle_dict[i].num for i in pos_list]
        new_num_list, count = self.num_list_opr(num_list)
        for j in range(len(new_num_list)):
            self.block_turtle_dict[pos_list[j]].num = new_num_list[j]
            self.block_turtle_dict[pos_list[j]].draw()
        return count

    def num_list_opr(self, num_list):
        count = True
        non_zero_nums = [num for num in num_list if num != 0]
        new_list = []
        i = 0
        while i < len(non_zero_nums):
            if i < len(non_zero_nums) - 1 and non_zero_nums[i] == non_zero_nums[i + 1]:
                new_list.append(non_zero_nums[i] * 2)
                self.score += non_zero_nums[i]
                i += 2
            else:
                new_list.append(non_zero_nums[i])
                i += 1
        new_list.extend([0] * (len(num_list) - len(new_list)))
        if new_list == num_list:
            count = False
        return new_list, count

    def restart(self):
        self.score = 0
        for block in self.block_turtle_dict.values():
            block.num = 0
            block.clear()
        self.background.turtle_show_score.clear()
        self.background.turtle_show_text.clear()
        self.background.text_is_clear = True
        self.is_win = True
        # 重新开始时随机生成两个数字方块
        self.new_num()
        self.new_num()


if __name__ == '__main__':
    game_window = turtle.Screen()
    game_window.setup(410, 500, 400, 20)
    game_window.bgcolor('gray')
    game_window.title('2048')
    game_window.tracer(0)
    try:
        game_window.register_shape('block.gif')
        game_window.register_shape('score.gif')
        game_window.register_shape('top.gif')
    except Exception as e:
        print(f"注册图片形状时出错: {e}")
        import sys
        sys.exit(1)
    game = Game()
    game_window.listen()
    game_window.onkey(game.move_up, 'Up')
    game_window.onkey(game.move_down, 'Down')
    game_window.onkey(game.move_left, 'Left')
    game_window.onkey(game.move_right, 'Right')
    game_window.onkey(game.restart, 'space')
    game_window.mainloop()