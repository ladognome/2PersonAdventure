__author__ = 'David'

import math
import os
import pygame

class player(pygame.sprite.Sprite):
    def __init__(self, name):
        pygame.sprite.Sprite.__init__(self)

        if (name.lower() == "rosie"):
            self.image = pygame.image.load(os.path.join("images","rosie.png"))
            self.rect = self.image.get_rect()
            self.rect.topleft = [100,100]
        elif (name.lower() == "rhotrax"):
            self.image = pygame.image.load(os.path.join("images","rhotrax.png"))
            self.rect = self.image.get_rect()

        #store the original image so that all scaling is based on the original size
        self.originalImage = self.image.copy()
        self.mapScale = 0.5 #determines the initial size of the character, i.e. how much of the screen it will fill up on a given map
        self.screenHeight = 480 #TODO: get this dynamically instead
        self.waypoints = []
        self.walking = False
        self.maxSpeed = 4  #walking speed in pixels/frame
        self.pos = (float(self.rect.midbottom[0]), float(self.rect.midbottom[1]))   #float representation of the sprite's position

    def update(self, *args):
        self.updateScale()

        if (len(self.waypoints) != 0):
            #goal check
            while (len(self.waypoints) > 0 and self.waypoints[0] == self.rect.midbottom):
                self.waypoints.pop(0)

            #if there are still waypoints, move towards the first one in the list
            if (len (self.waypoints) > 0):
                if (not(self.walking)):
                    self.walking = True

                currentPoint = self.waypoints[0]
                xUpdate = currentPoint[0] - self.rect.midbottom[0]
                yUpdate = currentPoint[1] - self.rect.midbottom[1]
                speed = math.sqrt(xUpdate**2 + yUpdate**2)
                if (speed > self.maxSpeed):
                    scaleFactor = self.maxSpeed/speed
                    xUpdate *= scaleFactor
                    yUpdate *= scaleFactor

                self.pos = (self.pos[0] + xUpdate, self.pos[1] + yUpdate)
                self.rect.midbottom = self.pos
            else:
                self.walking = False

    # Update the sprite scale based on the y-value and the map scale
    def updateScale(self):
        groundPoint = self.rect.midbottom
        scale = self.mapScale*groundPoint[1]/(self.screenHeight*.8)
        self.rect = self.originalImage.get_rect()
        self.image = pygame.transform.scale(self.originalImage, (int(self.rect.width*scale), int(self.rect.height*scale)))
        self.rect = self.image.get_rect()
        self.rect.midbottom = groundPoint