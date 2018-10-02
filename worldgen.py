
import pygame
from node1 import Node
import math
import random

class WorldGen():
    
    #randomly choose density used in spawning nodes
    def __init__(self, gridsize, screen):
        DENSITY = random.randint(1, 3)
        self.gridsize = gridsize
        self.screen = screen
        
        total_nodes = 0

        nodes = []
        for row in range(gridsize):
            nodes.append([])
            for column in range(gridsize):
                chance = DENSITY * .25
                if random.random() <= chance:
                    node = Node(screen, row, column)
                    nodes[row].append(node)
                    total_nodes += 1
                else:
                    nodes[row].append(0)
        
