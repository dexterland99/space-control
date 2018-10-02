
import pygame
import pygame.gfxdraw
import random
import math

NODE_IMG = pygame.Surface((30, 30), pygame.SRCALPHA)

class Node(pygame.sprite.Sprite):
    def __init__(self, screen, x, y):
        super().__init__()

        self.x = x
        self.y = y

        #nodes produce energy, radius is derived upon initialization
        produced = 1
        extracted = 0
        efficiency = 1.0
        
        

        radius = (produced-extracted)*efficiency
    
    # pygame.gfxdraw.aacircle(NODE_IMG,

    #calculate new radius
    #is there a way to give builder ships an efficiency variable that would change how much the node's size increases?

    def getCoords(self):
        cx = 1+(40 * x)
        cy = 1+(40 * y)
        return(cx, cy)

