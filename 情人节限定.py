import pygame
import random
import math
from pygame.locals import *

# 初始化Pygame
pygame.init()
info = pygame.display.Info()
SCREEN_WIDTH, SCREEN_HEIGHT = info.current_w, info.current_h
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), FULLSCREEN)
clock = pygame.time.Clock()

# 颜色配置
COLORS = {
    'bg': (0, 0, 0),
    'particle': (255, 50, 100),
    'accent': (255, 180, 200)
}


class Particle:
    def __init__(self, x=None, y=None):
        self.pos = pygame.Vector2(
            x if x is not None else random.uniform(0, SCREEN_WIDTH),
            y if y is not None else random.uniform(0, SCREEN_HEIGHT)
        )
        self.vel = pygame.Vector2(0, 0)
        self.acc = pygame.Vector2(0, 0)
        self.max_speed = 4.0
        self.target = self.pos.copy()
        self.size = 2.5
        self.base_size = 2.5
        self.alpha = 50
        self.friction = 0.85
        self.spring = 0.15
        self.wander = 0.3
        self.fixed = False  # 新增固定位置标记

    def apply_force(self, force):
        self.acc += force

    def update(self):
        if self.fixed: return  # 固定位置粒子不更新

        dx = self.target.x - self.pos.x
        dy = self.target.y - self.pos.y
        direction = pygame.Vector2(dx, dy).normalize() * self.spring

        wander_force = pygame.Vector2(
            random.uniform(-self.wander, self.wander),
            random.uniform(-self.wander, self.wander)
        )

        self.apply_force(direction + wander_force)

        self.vel += self.acc
        self.vel *= self.friction
        self.pos += self.vel
        self.acc *= 0

        self.size = self.base_size + abs(math.sin(pygame.time.get_ticks() * 0.002)) * 2

        self.pos.x = max(0, min(SCREEN_WIDTH, self.pos.x))
        self.pos.y = max(0, min(SCREEN_HEIGHT, self.pos.y))

    def draw(self):
        alpha_surface = pygame.Surface((self.size * 2, self.size * 2), SRCALPHA)
        pygame.draw.circle(alpha_surface,
                           (*COLORS['particle'], self.alpha),
                           (self.size, self.size),
                           self.size)
        screen.blit(alpha_surface, (self.pos.x - self.size, self.pos.y - self.size))


def create_text_shape(text, font_size=120):
    font = pygame.font.SysFont('simhei', font_size, bold=True)  # 使用黑体
    text_surf = font.render(text, True, COLORS['accent'])
    mask = pygame.mask.from_surface(text_surf)
    rect = text_surf.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))

    points = []
    for x in range(rect.width):
        for y in range(rect.height):
            if mask.get_at((x, y)):
                points.append((
                    x + rect.left + random.uniform(-3, 3),
                    y + rect.top + random.uniform(-3, 3)
                ))
    return points


def create_heart_shape(scale=1.0):
    points = []
    for t in range(0, 628, 5):  # 0到2π的采样
        theta = t / 100
        x = 16 * (math.sin(theta) ** 3)
        y = -(13 * math.cos(theta) - 5 * math.cos(2 * theta)
              - 2 * math.cos(3 * theta) - math.cos(4 * theta))

        # 缩放和平移
        x = x * 25 * scale + SCREEN_WIDTH / 2
        y = y * 25 * scale + SCREEN_HEIGHT / 2
        points.append((x, y))
    return points


class AnimationSystem:
    def __init__(self):
        self.particles = [Particle() for _ in range(2500)]
        self.states = [
            "rain",  # 阶段1：LOVE雨
            "countdown",  # 阶段2：倒计时
            "message",  # 阶段3：文字显示
            "heart",  # 阶段4：爱心动画
            "end"  # 阶段5：结束
        ]
        self.current_state = 0
        self.last_update = 0
        self.heart_scale = 0.1
        self.heart_target_scale = 1.0
        self.init_rain()

    def init_rain(self):
        """初始化字母雨"""
        self.rain_letters = []
        letter_spacing = SCREEN_WIDTH // 6
        for i in range(5):
            targets = create_text_shape("LOVE", 50)
            for t in targets:
                t = (t[0] + i * letter_spacing, -100 - i * 200)  # 初始位置在屏幕上方
            self.rain_letters.extend(targets)

        # 分配粒子
        for i, p in enumerate(self.particles):
            if i < len(self.rain_letters):
                p.target = pygame.Vector2(self.rain_letters[i])
                p.spring = 0.3
                p.alpha = 200
                p.base_size = 3.0
                p.fixed = True  # 固定位置用于下雨

    def update_rain(self):
        """更新字母雨位置"""
        speed = 8
        for i in range(len(self.rain_letters)):
            x, y = self.rain_letters[i]
            new_y = y + speed
            if new_y > SCREEN_HEIGHT + 200:  # 重置位置到顶部
                new_y = -random.randint(100, 300)
            self.rain_letters[i] = (x, new_y)

        # 更新粒子目标位置
        for i, p in enumerate(self.particles):
            if i < len(self.rain_letters):
                p.target.xy = self.rain_letters[i]

        # 检测是否所有字母到底部
        if pygame.time.get_ticks() - self.last_update > 5000:
            self.current_state = 1
            self.last_update = pygame.time.get_ticks()
            self.init_countdown()

    def init_countdown(self):
        """初始化倒计时"""
        self.countdown_numbers = [3, 2, 1]
        self.current_number = 0
        self.transition_effect()

    def transition_effect(self):
        """粒子散开效果"""
        for p in self.particles:
            p.fixed = False
            p.target = pygame.Vector2(
                p.pos.x + random.uniform(-50, 50),
                p.pos.y + random.uniform(-50, 50))
            p.spring = 0.05
            p.alpha = 100

    def update_countdown(self):
        if pygame.time.get_ticks() - self.last_update > 1500:
            if self.current_number < len(self.countdown_numbers):
                targets = create_text_shape(
                    str(self.countdown_numbers[self.current_number]),
                    int(SCREEN_HEIGHT * 0.3))

                for i, p in enumerate(self.particles):
                    if i < len(targets):
                        p.target = pygame.Vector2(targets[i])
                        p.spring = 0.2
                        p.alpha = 200
                self.current_number += 1
                self.last_update = pygame.time.get_ticks()
            else:
                self.current_state = 2
                self.init_message()

    def init_message(self):
        targets = create_text_shape("情人节快乐啊", int(SCREEN_HEIGHT * 0.15))
        for i, p in enumerate(self.particles):
            if i < len(targets):
                p.target = pygame.Vector2(targets[i])
                p.spring = 0.15
        self.last_update = pygame.time.get_ticks()

    def init_heart(self):
        """初始化爱心动画"""
        heart_points = create_heart_shape(self.heart_scale)
        text_points = create_text_shape("我爱你", int(30 * self.heart_scale))

        # 合并爱心和文字位置
        combined = heart_points + text_points
        for i, p in enumerate(self.particles):
            if i < len(combined):
                p.target = pygame.Vector2(combined[i])
                p.spring = 0.1
        self.last_update = pygame.time.get_ticks()

    def update_heart(self):
        """更新爱心缩放"""
        if self.heart_scale < self.heart_target_scale:
            self.heart_scale = min(self.heart_scale + 0.02, self.heart_target_scale)
            self.init_heart()

        if pygame.time.get_ticks() - self.last_update > 10000:
            self.current_state = 4

    def update(self):
        now = pygame.time.get_ticks()

        if self.states[self.current_state] == "rain":
            self.update_rain()
        elif self.states[self.current_state] == "countdown":
            self.update_countdown()
        elif self.states[self.current_state] == "message":
            if now - self.last_update > 3000:
                self.current_state = 3
                self.init_heart()
        elif self.states[self.current_state] == "heart":
            self.update_heart()
        elif self.states[self.current_state] == "end":
            pygame.quit()
            exit()

        for p in self.particles:
            p.update()

    def draw(self):
        screen.fill(COLORS['bg'])
        for p in self.particles:
            p.draw()
        pygame.display.flip()


# 运行动画
system = AnimationSystem()
while True:
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            exit()

    system.update()
    system.draw()
    clock.tick(60)