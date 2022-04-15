from pickle import FRAME
import pygame , os, sys
from random import randint as rn
import random

pygame.init()

FPS = 60
FramePerSec = pygame.time.Clock()

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
BLUE = (0,0,255)
RED = (255,0,0 )
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255,255,255)
SCREEN_WIDTH = 600
SCREEN_HEIGT = 600
SPEED1 = 1
SPEED2 = 2
SCORE = 0

#main screen
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('RACER')
image_backround = pygame.image.load(r'C:\pp2_21B030767\Lab8\Circuit.png')
image_backround = pygame.transform.scale(image_backround,(SCREEN_WIDTH,SCREEN_HEIGHT))



class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        s1 = list(range(1, 5))
        s2 = list(range(5, 10))

        i = random.choice(s1)
        j = random.choice(s2)

        self.enemy = os.listdir(r'C:\Pygame\cars')
       
        self.image1 = pygame.image.load(os.path.join(f'C:/Pygame/cars/car_{i}.png'))
        self.image1 = pygame.transform.scale(self.image1,(60,116))

        # self.image2 = pygame.image.load(os.path.join(f'C:/Pygame/cars/car_{j}.png'))
        # self.image2 = pygame.transform.scale(self.image2,(60,116))

        self.rect1 = self.image1.get_rect()
        self.rect1.center = (rn(150, SCREEN_WIDTH - 325), 0)

        # self.rect2 = self.image2.get_rect()
        # self.rect2.center = (rn(320, SCREEN_WIDTH - 150), 0)

        
    def move(self):
        
        self.rect1.move_ip(0,SPEED1)
        # self.rect2.move_ip(0,SPEED2)
         
        s1 = list(range(1, 5))
        s2 = list(range(5, 10))

        i = random.choice(s1)
        j = random.choice(s2)

        if self.rect1.bottom > 600:
                self.rect1.top = 0
                self.rect1.center = (rn( 150, 275), 0)
                self.image1 = pygame.image.load(os.path.join(f'C:/Pygame/cars/car_{i}.png'))
                self.image1 = pygame.transform.scale(self.image1,(60,116))
        
        # if self.rect2.bottom > 600 :
        #         self.rect2.top = 0
        #         self.rect2.center = (rn( 320, SCREEN_WIDTH - 150), 0)
        #         self.image2 = pygame.image.load(os.path.join(f'C:/Pygame/cars/car_{j}.png'))
        #         self.image2 = pygame.transform.scale(self.image2,(60,116))
        

    def draw(self):
        screen.blit(self.image1,self.rect1)
        # screen.blit(self.image2,self.rect2)
       

        



class Player(pygame.sprite.Sprite):
    def __init__(self):
        self.image = pygame.image.load('C:/pp2_21B030767/Lab9/Racer/car_light_blue.png')
        self.image = pygame.transform.scale(self.image,(60,116))
        self.rect = self.image.get_rect()
        self.rect.center = (150,500)

    def move(self):
        pressed = pygame.key.get_pressed()
        
        if self.rect.right < 500:
            if pressed[pygame.K_RIGHT]:
               self.rect.move_ip(5,0)
        if self.rect.left > 100:
            if pressed[pygame.K_LEFT]:
               self.rect.move_ip(-5,0)
        if self.rect.top > 100:
            if pressed[pygame.K_UP]:
                self.rect.move_ip(0,-1)
        if self.rect.bottom < 550:
            if pressed[pygame.K_DOWN]:
                self.rect.move_ip(0,1)
        
    def draw(self):
        screen.blit(self.image,self.rect)

    def collosion(self):
        screen.fill((255,0,0))
        font = pygame.font.Font(None,50)
        game_over = font.render('Game Over', True , )
        screen.blit(game_over,(300,100))

E1 = Enemy()
P1 = Player()

# all_cars = pygame.sprite.Group()
# all_cars.add(E1)
# all_cars.add(P1)

# enemies = pygame.sprite.Group()
# enemies.add(E1)
 
        





while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
   
    # if pygame.sprite.spritecollideany(P1,):
    #     P1.collosion()
        
    screen.blit(image_backround,(0,0))
    P1.draw()
    P1.move()
    E1.draw()
    E1.move()

    pygame.display.update()

    FramePerSec.tick(FPS)




