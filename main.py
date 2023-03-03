from ast import main
from re import T
import pygame
import time

#screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

def game():
    pygame.init()
    screen = pygame.display.set_mode((900, 900))
    pygame.display.set_caption('dot')
    pygame.display.flip()
    clock = pygame.time.Clock()
    
    dot = pygame.image.load('2.jpg')
    dot = pygame.transform.scale(dot, (65, 50))
    
    x = 750
    y = 750
    
    k = 5
    a = 4
    down = True
    
    run = True
    
    jump = True
    
    while run:
        clock.tick(60)
        screen.fill([255, 255, 255])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    a = -40
                    jump = False
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_RETURN]):
            x = 100
            y = 100
        if (keys[pygame.K_RIGHT] and x < 800):
            x += 8
        if (keys[pygame.K_LEFT] and x > 0):
            x -= 8
        # if (keys[pygame.K_UP]):
        #     y -= 20
        if (keys[pygame.K_DOWN] and y < 820):
            y += 8
        # if (y > 420):
        #     a -= 1
        k = a
        a += 4
        y += a 
        if (y >= 420):
            jump = True
        if (down and y > 820):
            down = False
            a = -a
        elif (a == 0):  
            down = True
        if (k == 0 and a == -4):
            y -= 4
        screen.blit(dot, (x,y))
        pygame.display.update()
    pygame.quit()
    return

game()