'''
Ship Classes
'''
import pygame
class Ship(pygame.sprite.Sprite):
    '''
    Ship Class
    '''
    def __init__(self,width,height,screen):
        super().__init__()
        
        self.image = pygame.image.load("Ship.png")
        self.rect = self.image.get_rect()
