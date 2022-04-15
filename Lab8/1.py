import pygame, sys,time
import random
import os

pygame.init()

FPS = 60
FramePerSec = pygame.time.Clock()

BLUE = (0,0,255)
RED = (255,0,0 )
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255,255,255)
SCREEN_WIDTH = 400
SCREEN_HEIGT = 600
SPEED = 1
SCORE = 0


#Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana",0)
game_over = font.render("Game Over", True, BLACK)

DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGT))
image_fone = pygame.image.load(r'Lab8\Circuit.png')
image_fone = pygame.transform.scale(image_fone,(SCREEN_WIDTH,SCREEN_HEIGT))

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r'Lab8\Enemy.png')
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(80, SCREEN_WIDTH - 80), 0)
    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if (self.rect.bottom > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint( 75, SCREEN_WIDTH - 75), 0)
    def draw(self, surface):
        surface.blit(self.image, self.rect)
    
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r'Lab8\Player.png')
        self.rect = self.image.get_rect()
        self.rect.center = (100, 500)
    def move(self):
        pressed = pygame.key.get_pressed()
        if self.rect.left > 70:
            if pressed[pygame.K_LEFT]:
                self.rect.move_ip(-5,0)
        if self.rect.right < 330:
            if pressed[pygame.K_RIGHT]:
                self.rect.move_ip(5,0)
        if self.rect.top > 50:
            if pressed[pygame.K_UP]:
                self.rect.move_ip(0,-1)
        if self.rect.bottom < 600:
            if pressed[pygame.K_DOWN]:
                self.rect.move_ip(0,1)
    def draw(self,surface):
        surface.blit(self.image,self.rect)

l = os.listdir(r'C:\Pygame\Coins')
Coins = 0
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load((os.path.join((r'C:\Pygame\Coins'),l[random.randint(0,(len(l)-1))]))),(30,30))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(80, SCREEN_WIDTH - 80), random.randint(350,400)) 
        self.take = False
   
    def move(self):
        global Coins
        self.rect.move_ip(0, SPEED)
        if  self.take == True:
            self.take = False
            Coins += 1
            self.rect.center = (random.randint( 75, SCREEN_WIDTH - 75), 0)
        if (self.rect.bottom > 600):
            self.rect.top = 0
            self.rect.center = (random.randint( 75, SCREEN_WIDTH - 75), 0)
    def draw(self, surface):
        surface.blit(self.image, self.rect)


        


P1 = Player()
E1 = Enemy()
C1 = Coin()
#Creating Sprites Groups


enemies = pygame.sprite.Group()
enemies.add(E1)

coinn = pygame.sprite.Group()
coinn.add(C1)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)

# all_sprites.add(C1)
 
#Adding a new User event 
INC_SPEED = pygame.USEREVENT
pygame.time.set_timer(INC_SPEED, 1000)

while True:
    #Cycles through all events occuring  
    for event in pygame.event.get():
        if event.type == INC_SPEED:
              SPEED += 0.125

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
    for entity in all_sprites:
       DISPLAYSURF.blit(entity.image, entity.rect)
       entity.move()
    
    
    #To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30,250))
        pygame.display.update()
        for entity in all_sprites:
            entity.kill() 
        time.sleep(2)
        pygame.quit()
        sys.exit()  
        
    if pygame.sprite.spritecollideany(P1,coinn):
        C1.take = True
    

    

    #if pygame.sprite.spritecollide(P1,coines):
    DISPLAYSURF.blit(image_fone,(0,0))

    font = pygame.font.Font(None, 30)
    text1 = font.render(f'Coins: {Coins}', True, (255 , 250 , 0))
    DISPLAYSURF.blit(text1, [0, 0])

    font1 = pygame.font.Font(None,30)
    text_score = font.render(f'Score: {SCORE}', True,(255,100,0))
    DISPLAYSURF.blit(text_score, [310, 0])

    


    P1.update()
    C1.move()
    C1.draw(DISPLAYSURF)
    P1.draw(DISPLAYSURF)
    E1.draw(DISPLAYSURF)
    
    
    pygame.display.update()
    FramePerSec.tick(FPS)

                






