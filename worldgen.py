
import pygame
from node1 import Node
import math
import random
from hub import Hub

class WorldGen():


    total_nodes = 0
    DENSITY = 0
    
    
    #randomly choose density used in spawning nodes
    def __init__(self, gridsize, screen):
        self.gridsize = gridsize
        self.screen = screen
        self.total_nodes = 0
        self.DENSITY = random.randint(1, 3)
        self.nodeGroup = pygame.sprite.RenderUpdates()
        self.map = [[0 for x in range(gridsize)] for y in range(gridsize)]
    
    def generateMap(self):
        for x in range(self.gridsize):
            for y in range(self.gridsize):
                self.map.append(0)

    def generateHubs(self):
        hub = Hub((50, 50))
        for row in range(self.gridsize):
            

    
    def generateNodes(self):
        
        nodes = []
        for row in range(self.gridsize):
            nodes.append([])
            
            for column in range(self.gridsize):
                chance = self.DENSITY * .1
                
                if random.random() <= chance and self.map[row][column] == 0:
                    """node = Node(self.screen, row, column)
                    node.drawx = 1+(40*row)
                    node.drawy = 1+(40*column)
                    
                    self.nodeGroup.add(node)
                    self.total_nodes += 1"""
                    nodes[row].append(2)
                    self.map[row][column] = 2
                    location = (1+20*column+column, 20*row+row)
                    node = Node(2, location)
                    self.nodeGroup.add(node)
                    print(location)

    def drawNodes(self):
        self.nodeGroup.draw(self.screen)




