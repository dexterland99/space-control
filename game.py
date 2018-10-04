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
from node1 import Node
from worldgen import WorldGen

GRIDSIZE = 10
GRIDW = 20
GRIDH = 20
size = width, height = 640, 480
BLACK = (0, 0, 0)

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
    
    
    #creating grid background/points to host nodes
    MARGIN = 1

    #create empty node array that mimics grid to compare, may not be the most efficient way(?)
    #nGrid = [100][100]

    world = WorldGen(GRIDSIZE, screen)
    world.generateMap()
    world.generateHubs()
    world.generateNodes()
    #testing ships
    myShip = Ship(50,50,screen)
    allShips = pygame.sprite.RenderUpdates()
    #myShip.add(allShips)
    
    #Event loop
    while 1:
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                print(event.pos)
            if event.type == QUIT:
                return
        screen.blit(background, (0, 0))
        
        #draw grid
        for row in range(GRIDSIZE):
            for column in range(GRIDSIZE):
                color = BLACK
                pygame.draw.rect(screen, color, [(MARGIN + GRIDW) * column + MARGIN, (MARGIN + GRIDH) * row + MARGIN, GRIDW, GRIDH])
        allShips.draw(screen)
        world.drawNodes()
        pygame.display.flip()

if __name__ == '__main__': main()
