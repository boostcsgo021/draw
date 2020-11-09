import pygame
import os

ball_image = pygame.image.load('ball.png')
speed_x, speed_y = 10, 10
ball_rect = ball_image.get_rect()

print(ball_rect)

os.environ['SDL_VIDEO_CENTERED'] = '1'
WIDTH_WIN, HEIGHT_WIN = 800, 600
collide = False

score = 0
score_ball = 0
block = False
block_ball = False

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

FPS = 120
clock = pygame.time.Clock()

surface = pygame.Surface((circle_radius * 2, circle_radius *2), pygame.SRCALPHA)
pygame.draw.circle(surface, YELLOW, (circle_radius, circle_radius), circle_radius)
rect1 = surface.get_rect()

def ball_move(x, y):
    global speed_x, speed_y, ball_rect
    if ball_rect.left < 0 or ball_rect.right > WIDTH_WIN:
        speed_x = -x
    if ball_rect.top < 0 or ball_rect.bottom > HEIGHT_WIN:
        speed_y = -y
    ball_rect = ball_rect.move(speed_x, speed_y)

run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
        elif e.type == pygame.MOUSEMOTION:
            rect1.center = e.pos
    screen.fill(BG)

    screen.blit(ball_image, ball_rect)


    ball_move(speed_x, speed_y)
    rect2 = pygame.draw.rect(screen, RED if collide else BLUE, (rect_pos, rect_size))

    screen.blit(surface, rect1)
    screen.blit(font.render(f"Счет: {score}", True, (0, 0, 0)), (0, 0))
    screen.blit(font.render(f"Счет мяча: {score_ball}", True, (0, 0, 0)), (WIDTH_WIN - font.size('Счет мяча: 848487')[0], 10))


    if rect1.colliderect(rect2):
        collide = True
        if not block:
            score += 1
            block = True
    elif ball_rect.colliderect(rect2):
        collide = True
        if not block_ball:
            score_ball += 1
            block_ball = True
    else:
        block = False
        block_ball = False
        collide = False
    pygame.display.update()
    clock.tick(FPS)
