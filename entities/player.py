__author__ = 'David'

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
            self.image = pygame.image.load(os.path.join("rhotrax","rhotrax.png"))
            self.rect = self.image.get_rect()

        #store the original image so that all scaling is based on the original size
        self.originalImage = self.image.copy()
        self.mapScale = 1.0 #determines the initial size of the character, i.e. how much of the screen it will fill up on a given map
        self.screenHeight = 480 #TODO: get this dynamically instead

    def update(self, *args):
        self.updateScale()

    # Update the sprite scale based on the y-value and the map scale
    def updateScale(self):
        groundPoint = self.rect.midbottom
        scale = self.mapScale*(1.8/self.screenHeight*groundPoint[1]-.8)
        self.rect = self.originalImage.get_rect()
        self.image = pygame.transform.scale(self.originalImage, (int(self.rect.width*scale), int(self.rect.height*scale)))
        self.rect = self.image.get_rect()
        self.rect.midbottom = groundPoint
