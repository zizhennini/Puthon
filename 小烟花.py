import pygame
import math
from random import randint
# 初始化
pygame.init()
# 设置窗口大小和标题
DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600
win = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
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
        self.radius = 3
        self.angle = randint(0, 360)
        self.speed = randint(1, 5)
        self.gravity = 0.1
        self.life = randint(20, 25)
    def update(self):
        if self.life > 0:
            radian = math.radians(self.angle)
            self.x += self.speed * math.cos(radian)
            self.y -= self.speed * math.sin(radian)
            self.speed -= self.gravity
            self.life -= 1
    def draw(self):
        pygame.draw.circle(win, self.color, (int(self.x), int(self.y)), self.radius)
# 定义烟花类
class Firework:
    def __init__(self):
        self.x = randint(100, DISPLAY_WIDTH - 100)
        self.y = DISPLAY_HEIGHT
        self.color = (randint(0, 255), randint(0, 255), randint(0, 255))
        self.particles = []
        self.exploded = False
    def explode(self):
        for _ in range(100):
            particle = Particle(self.x, self.y, self.color)
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
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    win.fill(BLACK)
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