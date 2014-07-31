#!/usr/bin/python

import os
import sys, pygame

pygame.init()

size = width, height = 640, 480
speed = [2,2]
black = 0,0,0

screen = pygame.display.set_mode(size)

ball = pygame.image.load(os.path.join("images","ball.bmp"))
splash = pygame.image.load(os.path.join("images","rosieSplash.png"))
ballrect = ball.get_rect()
splashrect = splash.get_rect()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(black)
    screen.blit(splash, splashrect)
    screen.blit(ball, ballrect)
    pygame.display.flip()
