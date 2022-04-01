
import pygame
import os

pygame.init()

screen = pygame.display.set_mode((,460))
pygame.display.set_caption('Music')
image_fone = pygame.image.load('lab7/music.jpg')
image_fone = pygame.transform.scale(image_fone,(394,460))


l = os.listdir(r'C:\My musics')
pygame.mixer.music.load(os.path.join(r'C:\My musics',l[0]))
pygame.mixer.music.play()

def music_change(pos):
    if pos < 0: i = len(l)-1
    elif pos > len(l): pos = 0
    pygame.mixer.music.load(os.path.join(r'C:\My musics',l[pos]))
    pygame.mixer.music.play()

clock = pygame.time.Clock()
done = False
flpayse = False
pos = 0
vol = 0.05
while not done:
    pressed = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
  
    screen.blit(image_fone,(0,0))
    flpayse = False 
    if pressed[pygame.K_SPACE]: pygame.mixer.music.pause()
    if pressed[pygame.K_RCTRL]: pygame.mixer.music.unpause()
    if pressed[pygame.K_RIGHT]:
        pos += 1 
        music_change(pos)
    if pressed[pygame.K_LEFT]:
        pos -= 1
        music_change(pos)
    if pressed[pygame.K_UP]: 
        vol += 0.05
        pygame.mixer.music.set_volume(vol)
    if pressed[pygame.K_DOWN]:
        vol -= 0.05
        pygame.mixer.music.set_volume(vol)


    clock.tick(10)
    
  
    pygame.display.flip()
