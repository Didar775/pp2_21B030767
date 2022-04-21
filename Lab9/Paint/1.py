
import pygame , os, sys
from random import randrange
pygame.init()

#main screen

screen = pygame.display.set_mode((800,600))
pygame.display.set_caption('Paint')
screen.fill((255,255,255))



draw_on = False
color = (0,0,0)
size = 1
mode = 'line'
equimpent = 'pen'
image_color = pygame.image.load('Lab9\Paint\main_colors.png')
image_color = pygame.transform.scale(image_color,(120,60))


image_chainge_size =pygame.image.load('Lab9\Paint\chainge_size.jpg')
image_chainge_size =pygame.transform.scale(image_chainge_size,(130,43))

image_eraser = pygame.image.load('Lab9\Paint\eraser.png')
image_eraser = pygame.transform.scale(image_eraser,(90,45))

image_pen = pygame.image.load('Lab9\Paint\pen.png')
image_pen = pygame.transform.scale(image_pen,(20,65))


# mode = None
# pos = mousebuttondown
# if 500 - 550
# mode = 'rect'


#colors
colors = {
       'red': (255, 0, 0),
       'blue': (0, 0, 255),
       'lime': (0, 255, 0),
       'yellow': (255 ,255, 0),
       'black': (0, 0, 0),
       'pink' : (255,192,203),
       'grey':(190,190,190),
       'white':(255,255,255),
       'orange':(255,165,0),
       'purple':(128,0,128),
       'sienna':(160,82,45),
       'dodger blue' : (30,144,255),
       'state blue' : (106,90,205),
       'deep pink' : (255,20,147),
       'green' : (0,128,0),
       'medium purple' :(147,112,219),
       'deep sky blue' : (0,191,255),
        
}

#print name of objects
def name_objects():
    font = pygame.font.Font(None, 20)
    text1 = font.render('colors', True, (0,0,0))
    screen.blit(text1,(695,63))
    text2 = font.render('thickness', True, (0,0,0))
    screen.blit(text2, (560, 63))
    text3 = font.render('figures', True, (0,0,0))
    screen.blit(text3,(450, 63))
    text3 = font.render('pen', True, (0,0,0))
    screen.blit(text3, (385,64))
    text4 = font.render('eraser', True, (0,0,0))
    screen.blit(text4, (307, 65))

#draw choosing shapes
def figures():
    pygame.draw.rect(screen , (0,0,0), (480, 5, 25, 15),1)
    pygame.draw.rect(screen, (0, 0, 0), (455, 5, 15 ,15), 1)
    pygame.draw.circle(screen, (0,0,0), (439, 13 ), 8, 1)
    pygame.draw.polygon(screen, (0,0,0), [[497,29], [506,38], [497,46],[489,38]],1)
    pygame.draw.polygon(screen, (0,0,0), [[463,31], [471,44], [455,44]],1)
    pygame.draw.polygon(screen,(0,0,0), [[430, 30], [430, 44], [444, 44],], 1)

    pygame.display.update()

#boundaries betwwen objects
def bound():
    pygame.draw.line(screen,(190,190,250),(658,1),(658,80))
    pygame.draw.line(screen,(190,190,250),(527,1),(527,80))
    pygame.draw.line(screen,(190,190,250), (420,1), (420,80))
    pygame.draw.line(screen,(190,190,250) ,(375,1), (375,80))
    pygame.draw.line(screen,(190,190,250), (280,1), (280,80) )
    pygame.draw.line(screen, (190,190,250), (0,80),(800,80))
    pygame.display.update()


width , height = 0 , 0

while True:
    pressed = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        
        if event.type == pygame.MOUSEBUTTONDOWN:

            # choosing colors
            l = pygame.mouse.get_pos()
            print(l)
            if 740 < l[0] < 775 and  1 < l[1] < 21 :
                color = colors['black']
            if 730 < l[0] < 755 and 1 < l[1] < 21:
                color = colors['sienna']
            if 707 < l[0] < 735 and 1 < l[1] < 21:
                color = colors['red']
            if 685 < l[0] < 710 and 1 < l[1] < 21:
                color = colors['purple']
            if 660 < l[0] < 685 and 1 < l[1] < 21:
                color = colors['blue']
            if 660 < l[0] < 685 and 21 < l[1] < 41:
                color = colors['dodger blue']
            if 685 < l[0] < 710 and 21 < l[1] < 41:
                color = colors['state blue']
            if 707 < l[0] < 735 and 21 < l[1] < 41:
                color = colors['deep pink']
            if 707 < l[0] < 735 and 41 < l[1] < 61:
                color = colors['pink']
            if 730 < l[0] < 755 and 21 < l[1] < 41:
                color = colors['orange']
            if 750 < l[0] < 775 and  21 < l[1] < 41 :
                color = colors['green']
            if 752 < l[0] < 775 and  41 < l[1] < 61 :
                color = colors['lime']
            if 730 < l[0] < 755 and 41 < l[1] < 61:
                color = colors['yellow']
            if 685 < l[0] < 710 and 41 < l[1] < 61:
                color = colors['medium purple']
            if 660 < l[0] < 685 and 41 < l[1] < 61:
                color = colors['deep sky blue']


      
            # choosing equipment
            if 430 < l[0] < 509 and 6 < l[1] <46:
                equimpent ='figures'
            if 376 < l[0] < 416 and 2 < l[1] < 70:
                equimpent ='pen'
            if 286 < l[0] < 368 and 5 < l[1] < 64:
                equimpent = 'eraser'

            # chosing shapes
            if 432 < l[0] < 446 and 6 < l[1] <20:
                mode = 'circle'
            if 456 < l[0] < 468 and 4 < l[1] <18:
                mode = 'square'
            if 481 < l[0] < 503 and 6 < l[1] < 18:
                mode = 'rect'
            if 455 < l[0] < 471 and 32 < l[1] < 43:
                mode = 'triangle'
            if 490 < l[0] < 505 and 30 < l[1] <46:
                mode = 'rhombus'
            if 430 < l[0] < 444 and  30 < l[1] < 44:
                mode = 'right triangle'
            
            
           
                
            #chainge size
            if 610 < l[0] < 645 and 10 < l[1] < 35:
                size += 1
            if 540 < l[0] < 568 and 10 < l[1] < 35 and  size > 0:
                size -= 1

            draw_on = True
        
        if event.type == pygame.MOUSEBUTTONUP:
            draw_on = False

        #erase
        if equimpent == 'eraser':
            color = colors['white']
            if event.type == pygame.MOUSEMOTION:
                last_p = pygame.mouse.get_pos()
                if draw_on:
                    pygame.draw.line(screen, color , l, last_p, size)
                    l = last_p


        
        #draw line
        if equimpent == 'pen':
            if event.type == pygame.MOUSEMOTION:
                last_p = pygame.mouse.get_pos()
                if draw_on:
                    pygame.draw.line(screen, color , l, last_p, size)
                    l = last_p

        #draw shapes
        if equimpent == 'figures':
                if event.type == pygame.MOUSEBUTTONUP:

                    last_p = event.pos
                   
                    width = last_p[0] - l[0]
                    height = last_p[1] - l[1]

                    if mode == 'rect':
                        pygame.draw.rect(screen, color, (l[0], l[1],width, height), size)
                    if mode == 'square':
                       pygame.draw.rect(screen, color, (l[0], l[1], width, width), size)
                    if mode == 'circle':
                        pygame.draw.circle(screen, color, (l[0]+width/2, l[1]+height/2), height/2, size)
                    if mode == 'triangle':
                         pygame.draw.polygon(screen, color, [[l[0], last_p[1]], [l[0]+width/2, l[1]], [last_p[0], last_p[1]]], size)
                    if mode == 'rhombus':
                          pygame.draw.polygon(screen, color, [[l[0] + width/2, l[1]], [last_p[0], l[1] + width/2, ], [l[0] + width/2, l[1] + width],[l[0], l[1] + width/2, ]],size)
                    if mode == 'right triangle':
                        pygame.draw.polygon(screen, color, [[l[0], l[1]], [l[0], l[1] + height], [last_p[0], last_p[1]]], size)

                    
         
        if pressed[pygame.K_SPACE]:
            screen.fill((255, 255, 255))



    font = pygame.font.Font(None,20)
    text = font.render(f'{size}', True, (0,0,0))

    bound()
    name_objects()
    figures()
    screen.blit(image_color,(660,0))
    screen.blit(image_chainge_size,(528,0))
    screen.blit(image_eraser,(290,10))
    screen.blit(image_pen,(385,1))
    screen.blit(text,[585,15])
   
   

    pygame.display.flip()


