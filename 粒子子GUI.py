import pygame
import random
import math

# 初始化Pygame
pygame.init()

# 设置屏幕尺寸
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("粒子效果示例")

# 定义粒子类
class Particle:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.radius = random.randint(2, 5)
        self.angle = random.uniform(0, 2 * math.pi)
        self.speed = random.uniform(1, 5)

    def update(self):
        # 更新粒子位置
        self.x += math.cos(self.angle) * self.speed
        self.y += math.sin(self.angle) * self.speed

        # 检查粒子是否超出屏幕边界，如果是则重新生成位置
        if self.x < 0 or self.x > screen_width:
            self.x = random.randint(0, screen_width)
            self.angle = random.uniform(0, 2 * math.pi)
            self.speed = random.uniform(1, 5)

        if self.y < 0 or self.y > screen_height:
            self.y = random.randint(0, screen_height)
            self.angle = random.uniform(0, 2 * math.pi)
            self.speed = random.uniform(1, 5)

    def draw(self, screen):
        # 绘制粒子
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)

# 创建粒子列表
particles = [Particle(random.randint(0, screen_width), random.randint(0, screen_height), (255, 0, 255)) for _ in range(100)]

# 主循环
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 更新粒子位置
    for particle in particles:
        particle.update()

    # 绘制背景（可选，这里用黑色背景）
    screen.fill((0, 0, 0))

    # 绘制粒子
    for particle in particles:
        particle.draw(screen)

    # 更新屏幕显示
    pygame.display.flip()

    # 控制帧率
    clock.tick(120)

# 退出Pygame
pygame.quit()
