
'''
#Draw line
pygame.draw.line(screen, color, [0,0], [100,100],5)
pygame.draw.rect(screen,color,[x,y,width, height],1)
pygamw.draw.ellipse(screen,color, [x,y,width,height,],1)

#Text
font=pygame.font.Font(None,50)
text1=font.render('my text',True, color)
text2=font.render('my text',False,color)
screen=blit(text1,(250,250))
screen.bilt(text2,(x,y))

font = pygame.font.Sysfont('Arial',25,True,False)
text=font.rander('pps',True,color)
text = =pygame.transform.rotate(text, 90)
screen.bilt(text,(x,y))

'''
import random
import pygame

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pygame example")
clock = pygame.time.Clock()

colors = [BLACK, BLUE, RED, GREEN]
rect_x = 50
rect_y = 50
rect_change_x = 2
rect_change_y = 2
color = WHITE
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            color = colors[random.randint(0, 3)]

    rect_x += rect_change_x
    rect_y += rect_change_y

    if rect_y > 450 or rect_y < 0:
        rect_change_y = rect_change_y*-1
    if rect_x > 650 or rect_x < 0:
        rect_change_x = rect_change_x*-1


    screen.fill(BLACK)
    pygame.draw.rect(screen, color, [rect_x, rect_y, 70, 70])
    pygame.draw.rect(screen, RED, [rect_x+10, rect_y+10, 30, 30])
    clock.tick(60)
    pygame.display.update()

pygame.quit()
