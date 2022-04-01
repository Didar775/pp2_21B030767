import pygame

pygame.init()

WHITE = (255, 255, 255)
RED = (255, 0, 0)

screen = pygame.display.set_mode((550, 550))
pygame.display.set_caption('Ball')
clock = pygame.time.Clock()
x, y = 0, 0

done = False
while not done:
    pressed = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    if y < 500:
        if pressed[pygame.K_DOWN]:
            y += 20
    if y > 0:
        if pressed[pygame.K_UP]:
            y -= 20
    if x > 0:
        if pressed[pygame.K_LEFT]:
            x -= 20
    if x < 500:
        if pressed[pygame.K_RIGHT]:
            x += 20 

    screen.fill(WHITE)
    pygame.draw.ellipse(screen, RED, [x, y, 50, 50])
    clock.tick(30)
    pygame.display.update()

pygame.quit()
