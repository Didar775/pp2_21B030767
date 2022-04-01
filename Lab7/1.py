import pygame
from datetime import datetime

pygame.init()
screen = pygame.display.set_mode((600,620))
pygame.display.set_caption("Clock")


mouse_image = pygame.image.load('lab7/clock.png')
mouse_image = pygame.transform.scale(mouse_image,(600,620))

righthand_image = pygame.image.load('lab7/2.png')
righthand_image = pygame.transform.scale(righthand_image,(250,260))
right_h_rect = righthand_image.get_rect()

lefthand_image = pygame.image.load('lab7/1.png')
lefthand_image = pygame.transform.scale(lefthand_image,(250,260))

done = False

while not done:
    pressed  = pygame.key.get_pressed()
    time =datetime.now()
    minute = time.minute
    seconds = time.second
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    screen.blit(mouse_image,(0,0))
    screen.blit(lefthand_image,(182,180))
    screen.blit(righthand_image,(170,175))
    
    
    
    pygame.display.flip()