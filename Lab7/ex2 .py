import pygame

pygame.init()

size=(500,500)
screen=pygame.display.set_mode(size)
pygame.display.set_caption("Didar")

done=False

while not done:

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
    screen.fill((255,255,255))

    pygame.draw.line(screen,(0,0,0),[0,0],[10,100],5)

    pygame.draw.rect(screen,(255,0,0),[0,0,50,100],5)
    pygame.draw.ellipse(screen,(0,0,255),[10,100,100,150],5)
    font=pygame.font.SysFont("Calibri",14,True,False)
    text1=font.render("Almaty",True,(0,0,0))
    text1=pygame.transform.rotate(text1,90)
    screen.blit(text1,(250,250))
    pygame.display.flip()


pygame.quit()

