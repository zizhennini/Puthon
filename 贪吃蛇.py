import pygame
import random
import time

# 初始化 Pygame
pygame.init()

# 定义游戏窗口大小
window_x = 720
window_y = 480

# 定义颜色
black = pygame.Color(0,0,0)
white = pygame.Color(255,255,255)
red = pygame.Color(255,0,0)
green = pygame.Color(0,255,0)
blue = pygame.Color(0,0,255)

# 初始化游戏窗口
pygame.display.set_caption('贪吃蛇游戏')
game_window = pygame.display.set_mode((window_x, window_y))

# 控制游戏速度
fps = pygame.time.Clock()

# 初始化贪吃蛇的位置
snake_position = [100,50]
snake_body = [[100,50], [90,50], [80,50], [70,50]]

# 初始化食物的位置
food_position = [random.randrange(1, (window_x // 10)) * 10, random.randrange(1, (window_y // 10)) * 10]
food_spawn = True

# 设置初始方向
direction = 'RIGHT'
change_to = direction

# 初始化分数
score = 0

# 设置蛇的速度
speed = 10

# 加载支持中文的字体
chinese_font = pygame.font.SysFont('simhei',20)

# 显示分数函数
def show_score(choice, color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('分数 : '+ str(score),True, color)
    score_rect = score_surface.get_rect()
    if choice == 1:
        score_rect.midtop = (window_x / 10,15)
    else:
        score_rect.midtop = (window_x / 2, window_y / 1.25)
    game_window.blit(score_surface, score_rect)

# 游戏结束函数
def game_over():
    my_font = pygame.font.SysFont('simhei',50)
    game_over_surface = my_font.render(
        '你的分数 : ' + str(score),True, red)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (window_x / 2, window_y / 4)
    game_window.blit(game_over_surface, game_over_rect)

    # 添加提示信息
    restart_font = pygame.font.SysFont('simhei',30)
    restart_surface = restart_font.render('按C键重新开始游戏',True, white)
    restart_rect = restart_surface.get_rect()
    restart_rect.midtop = (window_x / 2, window_y / 2)
    game_window.blit(restart_surface, restart_rect)
    pygame.display.flip()

# 重新开始游戏函数
def reset_game():
    global snake_position, snake_body, food_position, food_spawn, direction, change_to, score, speed
    snake_position = [100,50]
    snake_body = [[100,50], [90,50], [80,50], [70,50]]
    food_position = [random.randrange(1, (window_x // 10)) * 10, random.randrange(1, (window_y // 10)) * 10]
    food_spawn = True
    direction = 'RIGHT'
    change_to = direction
    score = 0
    speed = 10

# 主函数
running = True
game_over_flag = False
key_press_time = None

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
                key_press_time = time.time()
                if event.key == pygame.K_DOWN:
                    change_to = 'DOWN'
                    key_press_time = time.time()
                    if event.key == pygame.K_LEFT:
                        change_to = 'LEFT'
                        key_press_time = time.time()
                        if event.key == pygame.K_RIGHT:
                            change_to = 'RIGHT'
                            key_press_time = time.time()
                            if event.key == pygame.K_c and game_over_flag:
                                reset_game()
                                game_over_flag = False
                                if event.type == pygame.KEYUP:
                                    y_press_time = None
# 增加蛇的速度
if key_press_time:
    elapsed_time = time.time()-key_press_time
    if elapsed_time < 0.5:
        speed = 15
    elif elapsed_time < 1:
        speed =20
    else:
        speed = 25
else:
    speed = 10
# 防止蛇反向移动
if change_to == 'UP' and direction!= 'DOWN':
    direction = change_to
    if change_to == 'DOWN' and direction != 'UP':
        direction = change_to
        if change_to == 'LEFT' and direction != 'RIGHT':
            direction = change_to
            if change_to == 'RIGHT' and direction !='LEFT':
                direction = change_to
# 根据方向移动蛇头位置
    if direction== 'UP':
        snake_position[1]-=10
        if direction == 'DOWN':
            snake_position[1] +=10
            if direction =='LEFT':
                snake_position[0]-=10
                if direction == 'RIGHT':
                    snake_position[0] += 10
# 增加蛇的长度
    snake_body.insert(0, list(snake_position))
    if snake_position == food_position:
        score += 10
        food_spawn =False
    else:
        snake_body.pop()
if not food_spawn:
    food_position=[random.randrange(1, (window_x // 10)) * 10, random.randrange(1, (window_y // 10)) * 10]
    food_spawn = True
# 绘制游戏窗口
    game_window.fill(black)
for pos in snake_body:
    pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1],10,10))
    pygame.draw.rect(game_window, white, pygame.Rect(food_position[0], food_position[1],10,10))
# 边界碰撞检测
if snake_position[0]<0 or snake_position[0] >window_x-10 or snake_position[1] <0 or snake_position[1]>window_y / 10:
    game_over_flag=True
# 自身碰撞检测
for block in snake_body[1:]:
    if snake_position == block:
        game_over_flag = True
if game_over_flag:
    game_over()
    reset_game()
else:
    # 显示分数
    show_score(1, white,'simhei',20)
    # 刷新游戏屏幕
    pygame.display.update()
    # 控制游戏速度
    fps.tick(speed)
pygame.quit()