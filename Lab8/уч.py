
import pygame
from random import randint

pygame.init()

screen = pygame.display.set_mode((400,400))
pygame.display.set_caption('Snake')

backround = pygame.Surface((400,200))
backround.fill((0,255,0))
xb = 0
yb = 100

surf = pygame.Surface((100,100))
surf.fill((255,0,0))
x = 0
y =50

backround.blit(surf,(x,y))
screen.blit(backround,(xb,yb))

pygame.display.update()


done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            yb = randint(0,200)

    if x < 400:
        x += 2
    else:
        x =0

    screen.fill((0,0,0))
    backround.fill((0,255,0))
    backround.blit(surf,(x,y))
    screen.blit(backround,(xb,yb))
    pygame.display.update()

    pygame.time.delay(30)

