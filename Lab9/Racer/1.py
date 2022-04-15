import pygame , os, sys,time
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
SCORE = 0



#main screen
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('RACER')
image_backround = pygame.image.load(r'C:\pp2_21B030767\Lab8\Circuit.png')
image_backround = pygame.transform.scale(image_backround,(SCREEN_WIDTH,SCREEN_HEIGHT))

surface_coin = pygame.Surface((60,30))
surface_coin.fill((255,255,255))

game_start = pygame.image.load('Lab9\Racer\game_start.jpg')
game_start = pygame.transform.scale(game_start,(SCREEN_WIDTH,SCREEN_HEIGHT))
screen.blit(game_start,(0,0))
pygame.display.update()

game_over = pygame.image.load('Lab9\Racer\game_over.png')
game_over = pygame.transform.scale(game_over,(SCREEN_WIDTH,SCREEN_HEIGHT))

time.sleep(3)
pygame.mixer.music.load('C:/Pygame/Sountracks/background.wav')
pygame.mixer.music.play(-1)


class Enemy(pygame.sprite.Sprite):

    def __init__(self,posx,im,speed):
        super().__init__()
        self.speed = speed
        self.take = False
        self.image1 = pygame.image.load(os.path.join(f'C:/Pygame/cars/car_{im}.png'))
        self.image1 = pygame.transform.scale(self.image1,(60,116))


        self.rect = self.image1.get_rect()
        self.rect.center = (posx, 0)
        
    def move(self, chainge_pos):
        if self.take == True:
            self.speed += 0.125
        self.take = False
        
        self.rect.move_ip(0,self.speed)
        
        s1 = list(range(1, 10))
        i = random.choice(s1)
      
        
        if self.rect.bottom > 600:
                s1 = list(range(1, 10))
                i = random.choice(s1)
                self.rect.top = 0
                self.rect.center = (chainge_pos)
                self.image1 = pygame.image.load(os.path.join(f'C:/Pygame/cars/car_{i}.png'))
                self.image1 = pygame.transform.scale(self.image1,(60,116))
        

    def draw(self):
        screen.blit(self.image1,self.rect)
        

        

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.colision = False
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

cnt = 1

class Coins(pygame.sprite.Sprite):
    def __init__(self,im,speed):
        super().__init__()
        self.speed = speed
     
        self.image = pygame.image.load(f"C:/Pygame/Coins/coin_{im}.png")
        self.image = pygame.transform.scale(self.image,(30,30))
        self.rect = self.image.get_rect()

        self.rect.center = (random.randint(80, SCREEN_WIDTH - 80), random.randint(350,400)) 
        self.take = False
   
    def move(self,chainge_pos):
        
        global cnt
        self.rect.move_ip(0, self.speed)
        if  self.take == True:
            self.take = False
            cnt += 1
            self.rect.center = (random.randint( 120, 400), 0)
        if self.take == 5:
            cnt += 5
            self.take = False
            self.rect.center = (random.randint( 120, 400), 0)
        if (self.rect.bottom > 600):
            self.rect.top = 0
            self.rect.center = (chainge_pos)
    def draw(self):
        screen.blit(self.image, self.rect)


    
E1 = Enemy(130,7,1)
E2 = Enemy(350,9,2)
P1 = Player()
C1 = Coins(1 , 2)
C2 = Coins(1, 1)
C3 = Coins(2, 1)

all_cars = pygame.sprite.Group()
all_cars.add(E1)
all_cars.add(P1)
all_cars.add(E2)

Coins = 0
coin1 = pygame.sprite.Group()
coin1.add(C1)
coin2 = pygame.sprite.Group()
coin2.add(C2)
coin3 = pygame.sprite.Group()
coin3.add(C3)

enemies = pygame.sprite.Group()
enemies.add(E1)
enemies.add(E2)
 
    

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
   
    if pygame.sprite.spritecollideany(P1,enemies):
        pygame.mixer.music.load('C:/Pygame/Sountracks/crash.wav')
        pygame.mixer.music.play()
        screen.blit(game_over, (0,0))
        pygame.display.update()
        for entity in all_cars:
            entity.kill() 
        time.sleep(5)
        pygame.quit()
        sys.exit() 


    if pygame.sprite.spritecollideany(P1,coin1):
       C1.take = True
    
    if pygame.sprite.spritecollideany(P1,coin2):
       C2.take = True
       
    
    if pygame.sprite.spritecollideany(P1,coin3):
       C3.take = 5
       
    
    if cnt%10 == 0:
        E1.take = True
        E2.take = True

    screen.blit(image_backround,(0,0))
    screen.blit(surface_coin,(520,0))
    
    font = pygame.font.Font(None,30)
    text = font.render(f'{cnt-1}', True, BLACK)
    screen.blit(text,[550,0])

    screen.blit(C1.image,(520,0))
    P1.draw()
    P1.move()
    E1.draw()
    E1.move((rn(150,240),0))
    E2.draw()
    E2.move((rn(300,480),0))
    C1.draw()
    C1.move((rn(150,240),0))
    C2.draw()
    C2.move((rn(300,400),0))
    C3.draw()
    C3.move((rn(150,480),0))


    pygame.display.update()

    FramePerSec.tick(FPS)




