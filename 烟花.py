import pygame
from random import randint
from 粒子子GUI import Firework, Particle, running

pygame.init()
pygame.font.init()
pygame.display.set_caption("草海烟花秀！")
# Assuming image_path, DISPLAY_WIDTH, DISPLAY_HEIGHT are defined elsewhere
background = pygame.image.load(image_path)
win = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
clock = pygame.time.Clock()

fireworks = [Firework() for _ in range(2)]
running = True

while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                fireworks.append(Firework())
            elif event.key == pygame.K_7:
                fireworks.extend([Firework() for _ in range(10)])

    win.fill((20, 20, 30))
    win.blit(background, (0, 0))

    if randint(0, 20) == 1:
        fireworks.append(Firework())

    fireworks_to_remove = []
    for firework in fireworks:
        firework.show(win)
        if firework.remove():
            fireworks_to_remove.append(firework)
    for firework in fireworks_to_remove:
        fireworks.remove(firework)

    pygame.display.update()
