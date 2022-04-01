import pygame
from datetime import datetime

pygame.init()
screen = pygame.display.set_mode((800, 800))

def blitRotate(surf, image, pos, originPos, angle):

    # offset from pivot to center
    image_rect = image.get_rect(topleft = (pos[0] - originPos[0], pos[1]-originPos[1]))
    offset_center_to_pivot = pygame.math.Vector2(pos) - image_rect.center
    
    # roatated offset from pivot to center
    rotated_offset = offset_center_to_pivot.rotate(angle)

    # roatetd image center
    rotated_image_center = (pos[0] - rotated_offset.x, pos[1] - rotated_offset.y)

    # get a rotated image
    rotated_image = pygame.transform.rotate(image, -angle)
    rotated_image_rect = rotated_image.get_rect(center = rotated_image_center)

    # rotate and blit the image
    surf.blit(rotated_image, rotated_image_rect)
  

image = pygame.image.load('lab7/1.png')
rhand = pygame.image.load('lab7/2.png')
w, h = image.get_size()

angle = 0
done = False
while not done:
    time = datetime.now()
    minutes = time.minute
    seconds = time.second

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pos = (screen.get_width()/2, screen.get_height()/2)
    
    screen.fill((255, 255, 255))
    blitRotate(screen, image, pos, (w/2, h/2), minutes * 6 + 45)
    blitRotate(screen, rhand, pos, (w/2, h/2), seconds * 6 + 45)
    #blitRotate2(screen, image, pos, angle)
    angle += 1

    pygame.display.flip()
    
pygame.quit()
exit()