import pygame
import random
import time

# 初始化 pygame
pygame.init()

# 设置游戏窗口
screen_width = 600
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("跳一跳游戏")

# 定义颜色
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# 定义时钟
clock = pygame.time.Clock()

# 定义角色参数
player_width = 50
player_height = 50
player_x = screen_width // 4
player_y = screen_height - player_height - 10
player_velocity = 0  # 垂直速度
gravity = 0.5  # 重力加速度

# 定义平台参数
platform_width = 100
platform_height = 10
platforms = []

# 跳跃控制
jumping = False
jump_force = 10  # 初始跳跃力度

# 游戏循环标志
running = True

def create_platforms():
    """生成随机平台"""
    global platforms
    platforms = []
    for i in range(5):
        platform_x = random.randint(50, screen_width - platform_width - 50)
        platform_y = random.randint(100, screen_height - 50)
        platforms.append(pygame.Rect(platform_x, platform_y, platform_width, platform_height))

def draw_player():
    """绘制玩家"""
    pygame.draw.rect(screen, RED, pygame.Rect(player_x, player_y, player_width, player_height))

def draw_platforms():
    """绘制平台"""
    for platform in platforms:
        pygame.draw.rect(screen, GREEN, platform)

def check_collisions():
    """检查是否与平台碰撞"""
    global player_y, player_velocity
    player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
    on_platform = False

    for platform in platforms:
        if player_rect.colliderect(platform):
            if player_velocity > 0 and player_y + player_height <= platform.top:
                player_y = platform.top - player_height  # 在平台上
                player_velocity = 0  # 重置垂直速度
                on_platform = True
                break

    if not on_platform:
        player_velocity += gravity  # 若不在平台上，受重力影响

def jump():
    """跳跃控制"""
    global player_velocity, jumping
    if jumping:
        player_velocity = -jump_force  # 初始跳跃速度向上

def game_over():
    """游戏结束"""
    font = pygame.font.SysFont("Arial", 40)
    game_over_text = font.render("游戏结束", True, BLACK)
    screen.blit(game_over_text, (screen_width // 3, screen_height // 3))
    pygame.display.flip()
    time.sleep(2)

# 创建初始平台
create_platforms()

# 游戏主循环
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not jumping:
                jumping = True
                jump()

    # 控制玩家的跳跃
    if player_y + player_height < screen_height:
        player_y += player_velocity  # 更新玩家的垂直位置

    check_collisions()

    # 绘制玩家、平台
    draw_player()
    draw_platforms()

    # 检查是否掉出屏幕
    if player_y > screen_height:
        game_over()
        running = False

    # 更新游戏界面
    pygame.display.flip()

    # 控制游戏帧率
    clock.tick(60)

# 退出 pygame
pygame.quit()