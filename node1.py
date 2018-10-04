
import pygame
import pygame.gfxdraw
import random
import math

green = (0, 255, 0)


class Node(pygame.sprite.Sprite):
    def __init__(self, radius, location):
        pygame.sprite.Sprite.__init__(self)
        

        #nodes produce energy, radius is derived upon initialization
        self.produced = 1
        self.extracted = 0
        self.efficiency = 1

        self.radius = radius

        self.image = pygame.Surface((self.radius*2, self.radius*2))
        #self.image.fill(green)
        self.rect = self.image.get_rect()
        self.rect.center = location
        pygame.draw.circle(self.image, green, (radius, radius), radius, 0)
        
        #the circles are buttfuck ugly so explore using anti-alias
        #pygame.gfxdraw.aacircle(self.image, location[0], location[1], radius, green)
        #pygame.gfxdraw.filled_circle(self.image, location[0], location[1], radius, green)
        
        """self.image = pygame.Surface([self.radius*2, self.radius*2])
        self.image.fill(green)
        self.image.set_colorkey(green)
        self.rect = self.image.get_rect(center=(self.drawx, self.drawy))
        pygame.draw.ellipse(self.image, green, self.rect, self.radius)"""

    # pygame.gfxdraw.aacircle(NODE_IMG,

    #calculate new radius
    #is there a way to give builder ships an efficiency variable that would change how much the node's size increases?

    def getCoords(self):
        return(x, y)

    def update(self):
        self.radius = (self.produced-self.extracted)*self.efficiency


