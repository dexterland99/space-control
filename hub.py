import pygame
from node1 import Node
import math

size = 10, 10
red = (255, 0, 0)

class Hub(pygame.sprite.Sprite):
    def __init__(self, location):
        self.system = pygame.sprite.RenderUpdates()
        self.image = pygame.Surface((size))
        self.image.fill(red)
        self.rect = self.image.get_rect()
        self.rect.center = location
        pygame.draw.rect(self.image, red, self.rect, 0)
        
        self.total_energy = 0
        self.total_energy_expended = 0

    def addNode(node):
        self.system.add(node)
    
    def removeNode(node):
        self.remove(node)

