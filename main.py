import pygame
import os

os.environ['SDL_VIDEO_CENTERED'] = '1'
WIDTH_WIN, HEIGHT_WIN = 400, 400
collide = False

score = 0
block = False

#квадрат
rect_size = w, h = 70, 70
rect_pos = x, y = (WIDTH_WIN - w) // 2, (HEIGHT_WIN - h)//2

#круг
circle_radius = 35
circle_pos = (0, 0)

#цвета
RED = (255, 0, 0, 180)
BLUE = (0, 0, 255, 180)
YELLOW = (255, 255, 0, 180)
BG = (128, 128, 128)

pygame.init()
pygame.display.set_caption('Draw')
screen = pygame.display.set_mode((WIDTH_WIN, HEIGHT_WIN))

#шрифт
font = pygame.font.SysFont('Arial', 28)

FPS = 60
clock = pygame.time.Clock()

surface = pygame.Surface((circle_radius * 2, circle_radius *2), pygame.SRCALPHA)
pygame.draw.circle(surface, YELLOW, (circle_radius, circle_radius), circle_radius)
rect1 = surface.get_rect()

run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
        elif e.type == pygame.MOUSEMOTION:
            rect1.center = e.pos
    screen.fill(BG)

    rect2 = pygame.draw.rect(screen, RED if collide else BLUE, (rect_pos, rect_size))

    screen.blit(surface, rect1)
    screen.blit(font.render(f"Счет: {score}", True, (0, 0, 0)), (0, 0))

    if rect1.colliderect(rect2):
        collide = True
        if not block:
            score += 1
            block = True

    else:
        block = False
        collide = False

    pygame.display.update()
    clock.tick(FPS)