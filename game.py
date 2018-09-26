# SPACE CONTROL
# temp name for a cool game
# https://www.github.com/dexterland99/space-control
#
# Currently unlicensed

import sys
import pygame
from pygame.locals import *
import math
import random
import os
from socket import *
from Ships import Ship
def load_png(name):
    """ Load Image and return Image Object"""
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
        if image.get_alpha() is None:
            image = image.convert()
        else:
            image = image.conver_alpha()
    except pygame.error:
        print ('Cannot load image: ', fullname)
        raise SystemExit(message)
    return image, image.get_rect()


size = width, height = 640, 480

def main():
    
    #initialise screen
    pygame.init()
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Space Control")
    
    #fill background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((250, 250, 250))

    #blit to the screen
    screen.blit(background, (0, 0))
    pygame.display.flip()

    #testing ships
    myShip = Ship(50,50,screen)
    allShips = pygame.sprite.RenderUpdates()
    myShip.add(allShips)
    #Event loop
    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:
                return
        screen.blit(background, (0, 0))
        allShips.draw(screen)
        pygame.display.flip()

if __name__ == '__main__': main()
