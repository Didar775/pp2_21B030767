import pygame

pygame.init()

screen = pygame.display.set_mode((500,500))
pygame.display.set_caption('Rectangle')
x ,y = 0, 0
x_change = 2
y_change = 2
done = False
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    screen.fill((255,255,255))

    x += x_change
    y += y_change
    if x > 450 or x <0:
        x_change = x_change * -1
    if y > 450 or y < 50:
        y_change = y_change * -1
        
    pygame.draw.rect(screen,(255,0,0),(x,y,50,50))

    clock.tick(30)

    pygame.display.update()
