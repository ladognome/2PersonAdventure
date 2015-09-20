#!/usr/bin/python
import os
import sys, pygame
import copy
import web.client
import entities.player
import random

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
grey  = 50,50,50
white = 255,255,255

# set chat location (upper left corner is at left border 80% of the way down the y axis)
# the chat window ends at the bottom of the window and extends to the other side of the
# window. The percentage is used so that the scheme will scale with different screen sizes.
CHAT_X = int(0)
CHAT_Y = int(height*.80)
CHAT_W = width
CHAT_H = height - CHAT_Y

CHAT_HIST_LEN = 5

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
chatAreaRect = pygame.Rect(CHAT_X,CHAT_Y,CHAT_W,CHAT_H)
chatDisp = False # control whether chat window is displayed and excepting text.
chatStr = ""
chatRepStr = ""
chatHistory = []
chatFont = pygame.font.Font(None,18)
chatHistFontSurf = chatFont.render("\n".join(chatHistory),1,white) # 1 for smooth edges on text
chatFontSurf = chatFont.render(chatStr,1,white) # 1 for smooth edges on text
chatTypeRect = chatFontSurf.get_rect().move((CHAT_X,CHAT_Y + CHAT_H*0.8))
#chatClient = web.client.ChatClient()
player_sprites = pygame.sprite.Group() # list of player sprites (probably only 1)
rosie = entities.player.player("rosie")
rosie.add(player_sprites)

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
                #chatClient.send(chatStr)
                chatHistory.append(copy.deepcopy(chatStr))
                if (len(chatHistory) > CHAT_HIST_LEN):
                    chatHistory.pop(0)
                chatStr = ""
                chatFontSurf = chatFont.render(chatStr,1,white)
            else:
                chatDisp = True
        if (chatDisp):
            if event.type == pygame.KEYDOWN and ((event.key >= pygame.K_SPACE and event.key <= pygame.K_KP_EQUALS) or event.key == pygame.K_BACKSPACE):
                myKey = event.key
                # Test to see if shift was pressed with a letter key.
                if (pressed[pygame.K_LSHIFT] or pressed[pygame.K_RSHIFT]) and (myKey >= pygame.K_a and myKey <= pygame.K_z):
                    myKey -= 32
		if (myKey == pygame.K_BACKSPACE):
		    chatStr = chatStr[:-1]
                    chatFontSurf = chatFont.render(chatStr,1,white)
                elif (len(chatStr) < 150):
                    chatStr += chr(myKey)
                    chatFontSurf = chatFont.render(chatStr,1,white)
        if (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE):
            rosie.rect.midbottom=[random.randrange(1,640),random.randrange(240,480)]
            #rosie.rect.move_ip(10,10)
            #rosie.rect.x += 10

    # Move the ball...
    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    player_sprites.update()

    # Update objects on the screen.
    screen.fill(black)
    screen.blit(splash, splashrect)
    screen.blit(ball, ballrect)
    player_sprites.draw(screen)

    # Update the chat box by clearing it and then
    # displaying the appropriate text.
    if (chatDisp == True):
        pygame.draw.rect(screen, grey, chatAreaRect)
        screen.blit(chatFontSurf, chatTypeRect)
    else:
        pygame.draw.rect(screen, black, chatAreaRect)
    
    #chatRepStr = chatClient.recv()
    if (len(chatRepStr) > 0):
        chatHistory.append(copy.deepcopy(chatRepStr))
        if (len(chatHistory) > CHAT_HIST_LEN):
            chatHistory.pop(0)
    i = 0
    for line in chatHistory:
        chatHistFontSurf = chatFont.render(line,1,white) # 1 for smooth edges on text
        chatHistRect = chatHistFontSurf.get_rect().move(CHAT_X, CHAT_Y + i*chatFont.get_linesize())
        screen.blit(chatHistFontSurf, chatHistRect)
        i += 1

    pygame.display.flip()
