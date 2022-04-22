import pygame
from datetime import datetime

pygame.init()
screen = pygame.display.set_mode((600,620))
pygame.display.set_caption("Clock")

angle = 0

mouse_image = pygame.image.load('lab7/clock.png')
mouse_image = pygame.transform.scale(mouse_image,(600,620))

righthand_image = pygame.image.load('lab7/2.png')
righthand_image = pygame.transform.scale(righthand_image,(250,260))
righthand_image.set_colorkey((0,0,0), 100)

lefthand_image = pygame.image.load('lab7/1.png')
lefthand_image = pygame.transform.scale(lefthand_image,(250,260))

# righthand_image = pygame.image.load('lab7/2.png')
# righthand_image = pygame.transform.scale(righthand_image,(250,260))
# right_h_rect = righthand_image.get_rect()

# lefthand_image = pygame.image.load('lab7/1.png')
# lefthand_image = pygame.transform.scale(lefthand_image,(250,260))

def rotate():
    right_h_rect = righthand_image.get_rect()

    
    left_h_rect = lefthand_image.get_rect()

    




done = False

while not done:
    angle += 0.0625
    pressed  = pygame.key.get_pressed()
    time =datetime.now()
    minute = time.minute
    seconds = time.second
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
        if event.type== pygame.MOUSEBUTTONDOWN:
            l = pygame.mouse.get_pos()
            print(l)
    righthand_image.set_colorkey((0,0,0), 100)
    im_copy = pygame.transform.rotate(righthand_image, angle)
    righthand_image.set_colorkey((0,0,0))
    screen.blit(mouse_image,(0,0))
    screen.blit(lefthand_image,(182,180))
    screen.blit(im_copy,(im_copy.get_width()/2, im_copy.get_height()/2))
    rotate()
   
    
    
    pygame.display.flip()