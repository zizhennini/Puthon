import pygame
import math
from random import randint, uniform
import copy

# 初始化
pygame.init()
pygame.font.init()
# 获取屏幕信息
info = pygame.display.Info()
screen_width = info.current_w
screen_height = info.current_h
# 设置窗口大小和标题
win = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("烟花")

# 定义颜色
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


# 定义粒子类
class Particle:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.radius = randint(2, 5)
        self.angle = randint(0, 360)
        self.speed = randint(1, 8)
        self.gravity = 0.1
        self.life = randint(15, 30)
        self.alpha = 255
        self.prev_positions = []

    def update(self):
        if self.life > 0:
            radian = math.radians(self.angle)
            self.x += self.speed * math.cos(radian)
            self.y -= self.speed * math.sin(radian)
            self.speed -= self.gravity
            self.life -= 1
            self.alpha = int(self.alpha * (self.life / (self.life + 1)))
            self.color = (self.color[0], self.color[1], self.color[2], self.alpha)
            self.prev_positions.append((self.x, self.y))
            if len(self.prev_positions) > 5:
                self.prev_positions.pop(0)

    def draw(self):
        pygame.draw.circle(win, self.color, (int(self.x), int(self.y)), self.radius)
        for i in range(len(self.prev_positions) - 1):
            start_pos = self.prev_positions[i]
            end_pos = self.prev_positions[i + 1]
            alpha = int(self.alpha * (i / len(self.prev_positions)))
            color_with_alpha = (self.color[0], self.color[1], self.color[2], alpha)
            pygame.draw.line(win, color_with_alpha, start_pos, end_pos, 1)


# 定义烟花类
class Firework:
    def __init__(self):
        self.x = randint(100, screen_width - 100)
        self.y = screen_height
        self.color = (randint(0, 255), randint(0, 255), randint(0, 255))
        self.particles = []
        self.exploded = False

    def explode(self):
        for _ in range(100):
            particle_color = (randint(0, 255), randint(0, 255), randint(0, 255))
            particle = Particle(self.x, self.y, particle_color)
            self.particles.append(particle)

    def update(self):
        if not self.exploded:
            self.y -= 3
            if self.y <= randint(200, 400):
                self.explode()
                self.exploded = True
        else:
            for particle in self.particles:
                particle.update()

    def draw(self):
        pygame.draw.circle(win, self.color, (int(self.x), int(self.y)), 5)


# 创建烟花列表
fireworks = []
# 游戏主循环
running = True
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)
title_text = font.render("新年好！！！", True, WHITE)
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    win.fill(BLACK)
    # 绘制标题文字
    win.blit(title_text, (screen_width/2 - title_text.get_width()/2, 20))
    # 添加新的烟花
    if len(fireworks) < 10 and randint(0, 100) < 2:
        fireworks.append(Firework())
    # 更新和绘制烟花
    for firework in fireworks:
        firework.update()
        firework.draw()
        for particle in firework.particles:
            particle.draw()
    # 移除完成的烟花及消失的粒子
    fireworks = [firework for firework in fireworks if not firework.exploded or len(firework.particles) > 0]
    for firework in fireworks:
        firework.particles = [particle for particle in firework.particles if particle.life > 0]
    pygame.display.update()

pygame.quit()