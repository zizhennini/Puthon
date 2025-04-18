import pygame
import random
import math

# 初始化Pygame
pygame.init()

# 屏幕设置
SCREEN_WIDTH, SCREEN_HEIGHT = 1200, 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("情人节代码雨特效")

# 颜色定义
MATRIX_GREEN = (0, 255, 0)
HIGHLIGHT_COLORS = [(255, 50, 50), (255, 105, 180), (147, 112, 219)]  # 红/粉/紫
BACKGROUND_COLOR = (0, 0, 0)

# 字体配置
FONT_SIZE = 20
font = pygame.font.SysFont('consolas', FONT_SIZE, bold=True)


class CodeDrop:
    def __init__(self, x, y, is_special=False):
        self.x = x
        self.base_y = y
        self.speed = random.randint(10, 30)
        self.alpha = 255
        self.chars = self.generate_code(is_special)
        self.rot_angle = random.randint(-5, 5)

    def generate_code(self, special):
        """生成代码序列，包含特殊字符概率"""
        charset = list("01LOVE") if special else list("10█▓▒░")
        return [random.choice(charset) for _ in range(random.randint(5, 15))]

    def update(self):
        """更新下落状态"""
        self.base_y += self.speed * 0.5
        self.alpha = max(0, self.alpha - 8)

        if self.base_y > SCREEN_HEIGHT + len(self.chars) * FONT_SIZE:
            self.reset()

    def draw(self, surface):
        """绘制字符序列"""
        for i, char in enumerate(self.chars):
            y_offset = self.base_y + i * FONT_SIZE
            alpha = max(0, self.alpha - i * 15)

            # 随机高亮效果
            if random.random() < 0.3:
                color = random.choice(HIGHLIGHT_COLORS) + (alpha,)
            else:
                color = MATRIX_GREEN + (alpha,)

            text = font.render(char, True, color[:3])
            text.set_alpha(alpha)

            # 添加旋转效果
            rotated = pygame.transform.rotate(text, self.rot_angle)
            surface.blit(rotated, (self.x - rotated.get_width() / 2,
                                   y_offset - rotated.get_height() / 2))

    def reset(self):
        """重置到屏幕顶部"""
        self.base_y = -random.randint(100, 500)
        self.alpha = 255
        self.speed = random.randint(10, 30)
        self.chars = self.generate_code(random.random() < 0.2)


# 初始化代码雨列（每20像素一列）
columns = [CodeDrop(x, -random.randint(100, 500))
           for x in range(0, SCREEN_WIDTH, 20)]


# 爱心粒子系统
class HeartParticle:
    def __init__(self):
        self.x = random.randint(0, SCREEN_WIDTH)
        self.y = SCREEN_HEIGHT
        self.size = random.randint(8, 15)
        self.life = 255

    def update(self):
        self.y -= 2
        self.x += random.uniform(-1, 1)
        self.life = max(0, self.life - 5)

    def draw(self, surface):
        if self.life > 0:
            # 绘制爱心形状
            alpha = int(self.life)
            points = [
                (self.x, self.y + self.size / 2),
                (self.x + self.size, self.y),
                (self.x, self.y - self.size / 2),
                (self.x - self.size, self.y)
            ]
            pygame.draw.polygon(surface, (255, 50, 100, alpha), points)


hearts = []

# 主循环
clock = pygame.time.Clock()
running = True
message_alpha = 0
show_message = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 绘制背景残影
    fade_surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
    fade_surface.fill((0, 20, 0, 15))  # 残影透明度
    screen.blit(fade_surface, (0, 0))

    # 更新并绘制代码雨
    for drop in columns:
        drop.update()
        drop.draw(screen)

    # 随机生成爱心粒子
    if random.random() < 0.05:
        hearts.append(HeartParticle())

    # 更新绘制爱心
    for heart in hearts[:]:
        heart.update()
        heart.draw(screen)
        if heart.life <= 0:
            hearts.remove(heart)

    # 显示情人节消息
    if pygame.time.get_ticks() > 5000 and not show_message:
        message_alpha = min(255, message_alpha + 3)
        if message_alpha == 255:
            show_message = True

    if message_alpha > 0:
        msg_font = pygame.font.SysFont('simhei', 72, bold=True)
        text = msg_font.render("情人节快乐", True, (255, 100, 200, message_alpha))
        text.set_alpha(message_alpha)
        screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2,
                           SCREEN_HEIGHT // 2 - text.get_height() // 2))

    pygame.display.flip()
    clock.tick(30)

pygame.quit()