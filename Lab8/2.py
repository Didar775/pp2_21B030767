import os
import pygame, sys
from random import randint

pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Snake')
SCORE = 0
LEVEL = 0

background = pygame.image.load(r'Lab8\fone.png')
background =pygame.transform.scale(background,(600,600))

pygame.mixer.music.load(r'C:\My musics\Snake.mp3')
pygame.mixer.music.play(-1)

class Snake:
    def __init__(self, x, y):
        
        self.size = 1
        self.elements = [[x, y]]
        self.radius = 8
        self.dx = 5
        self.dy = 0
        self.is_add = False
        self.speed = 15

    def draw(self):
        for element in self.elements:
            pygame.draw.circle(screen, (0, 100, 100), element, self.radius)

    def check_fail(self):
        for block in self.elements[1:]:
            if block == self.elements[0]:
                screen.fill((0,255,0))
                screen.blit('Game over', (30,250))
                pygame.display.update()

    def add_to_snake(self):
        global SCORE, LEVEL

        SCORE += 1
        self.size += 1
        self.elements.append([0, 0])
        self.is_add = False
        if SCORE % 3 == 0:
           self.speed += 10
           LEVEL += 1

        

    def move(self):
        if self.is_add:
            self.add_to_snake()

        for i in range(self.size - 1, 0, -1):
            self.elements[i][0] = self.elements[i-1][0]
            self.elements[i][1] = self.elements[i-1][1]

        self.elements[0][0] += self.dx
        self.elements[0][1] += self.dy
        if self.elements[0][0] > 600:
            self.elements[0][0] = 0
        if self.elements[0][1] > 600:
            self.elements[0][1] = 0
        if self.elements[0][0] < 0:
            self.elements[0][0] = 600
        if self.elements[0][1] < 0:
            self.elements[0][1] = 600

        font2 = pygame.font.Font(None,30)
        text_level = font1.render(f'Level: {LEVEL}', True, (255,255,0))
        screen.blit(text_level,(500,0))

    def eat(self, foodx, foody):
        x = self.elements[0][0]
        y = self.elements[0][1]

        if foodx <= x <= foodx + 20 and foody <= y <= foody + 20 :
            return True
        if foodx -20 <= x <=foodx and foody-20 <= y <=foody:
            return True
        return False


class Food:
    def __init__(self):
        self.x = randint(0, 590)
        self.y = randint(0, 590)

    def gen(self):
        self.x = randint(5, 590)
        self.y = randint(5, 590)

    def draw(self):
        pygame.draw.circle(screen, (255, 0, 0), (self.x, self.y), 7)


snake = Snake(100, 100)
food = Food()
d = 5



FPS = 30
clock = pygame.time.Clock()

while True:
    clock.tick(snake.speed)
    pressed = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if pressed[pygame.K_RIGHT] and snake.dx != -d:
            snake.dx = d
            snake.dy = 0
        if pressed[pygame.K_LEFT] and snake.dx != d:
            snake.dx = -d
            snake.dy = 0
        if pressed[pygame.K_UP] and snake.dy != d:
            snake.dx = 0
            snake.dy = -d
        if pressed[pygame.K_DOWN] and snake.dy != -d:
            snake.dx = 0
            snake.dy = d

    screen.blit(background,(0,0))
    
    snake.check_fail()

    font1 = pygame.font.Font(None,30)
    text_score = font1.render(f'Score: {SCORE}', True, (255,255,0))
    screen.blit(text_score,(0,0))

    if snake.eat(food.x,food.y):
        snake.is_add = True
        food.gen()
    snake.move()
    
    snake.draw()
    food.draw()
    pygame.display.flip()
