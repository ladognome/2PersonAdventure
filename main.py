#!/usr/bin/python

import os
import sys, pygame

pygame.init()

##############
# CONSTANTS
##############

# Set screen size
size = width, height = 640, 480
# set speed of ball...
speed = [2,2]
# set color black...
black = 0,0,0
white = 255,255,255

# set chat location (upper left corner is at left border 80% of the way down the y axis)
# the chat window ends at the bottom of the window and extends to the other side of the
# window. The percentage is used so that the scheme will scale with different screen sizes.
CHAT_X = int(0)
CHAT_Y = int(height*.80)
CHAT_W = width
CHAT_H = height - CHAT_Y

# Setup the screen size
screen = pygame.display.set_mode(size)

###################
# GLOBAL VARIABLES
###################

# setup important global variables.
ball = pygame.image.load(os.path.join("images","ball.bmp"))
splash = pygame.image.load(os.path.join("images","rosieSplash.png"))
ballrect = ball.get_rect()
splashrect = splash.get_rect()
chatRect = pygame.Rect(CHAT_X,CHAT_Y,CHAT_W,CHAT_H)
chatDisp = False # control whether chat window is displayed and excepting text.
chatStr = ""
chatFont = pygame.font.Font(None,14)
chatFontSurf = chatFont.render(chatStr,1,white) # 1 for smooth edges on text

#################
# MAIN LOOP
#################

while 1:
    # Test for Key Inputs 
    pressed = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        # Toggle the chatDisp variable when Enter is pressed.
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            if (chatDisp):
                chatDisp = False
                chatStr = ""
                chatFontSurf = chatFont.render(chatStr,1,white)
            else:
                chatDisp = True
        if (chatDisp):
            if event.type == pygame.KEYDOWN and event.key >= pygame.K_SPACE and event.key <= pygame.K_KP_EQUALS:
                myKey = event.key
                # Test to see if shift was pressed with a letter key.
                if (pressed[pygame.K_LSHIFT] or pressed[pygame.K_RSHIFT]) and (myKey >= pygame.K_a and myKey <= pygame.K_z):
                    myKey -= 32
                #print "Pressed key w/ number: %s =" % (chr(myKey), ), myKey
                chatStr += chr(myKey)
                chatFontSurf = chatFont.render(chatStr,1,white)

    # Move the ball...
    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    # Update objects on the screen.
    screen.fill(black)
    screen.blit(splash, splashrect)
    screen.blit(ball, ballrect)

    # Update the chat box by clearing it and then
    # displaying the appropriate text.
    if (chatDisp == True):
        pygame.draw.rect(screen, black, chatRect)
        screen.blit(chatFontSurf, chatRect)

    pygame.display.flip()
